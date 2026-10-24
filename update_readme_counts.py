#!/usr/bin/env python3
"""Rebuild the README inventory from tracked files. Run from the repository root."""
import csv
import re
import subprocess
from collections import Counter
from pathlib import Path
from urllib.parse import quote

root = Path(subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip())
paths = [p.decode('utf-8') for p in subprocess.check_output(['git', 'ls-files', '-z'], cwd=root).split(b'\0') if p]
commit = subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD'], cwd=root, text=True).strip()
folders = sorted({p.split('/')[0] for p in paths if '/' in p}, key=str.casefold)
rows = []
for folder in folders:
    members = [p for p in paths if p.startswith(folder + '/')]
    ext = Counter(Path(p).suffix.lower() for p in members)
    rows.append((folder, ext['.inp'], ext['.md'], ext['.rpt'], ext['.out'], len(members)))
root_files = [p for p in paths if '/' not in p]
root_ext = Counter(Path(p).suffix.lower() for p in root_files)
root_row = ('(repository root)', root_ext['.inp'], root_ext['.md'], root_ext['.rpt'], root_ext['.out'], len(root_files))
all_rows = rows + [root_row]
totals = tuple(sum(r[i] for r in all_rows) for i in range(1, 6))
lines = ['## Collection overview', '',
    f'Inventory generated from Git-tracked paths at commit `{commit}`. Counts include nested subfolders and match extensions case-insensitively. Each top-level folder appears below, including folders with zero `.inp` files. Counts describe files, not unique networks or successful runs. Markdown totals include documentation as well as model summaries.', '',
    '| Folder | .inp | .md | .rpt | .out | All files |',
    '|---|---:|---:|---:|---:|---:|']
for r in all_rows:
    label = r[0] if r[0] == '(repository root)' else f'[{r[0]}]({quote(r[0])}/)'
    lines.append('| ' + label + ' | ' + ' | '.join(f'{n:,}' for n in r[1:]) + ' |')
lines.append('| Total | ' + ' | '.join(f'{n:,}' for n in totals) + ' |')
lines.extend(['', 'A complete nested-folder breakdown is provided in [folder_inventory.csv](folder_inventory.csv). Nested totals overlap their parents and must not be summed across levels.', ''])
readme = root / 'readme.md'
text = readme.read_text(encoding='utf-8')
pattern = r'(?ms)^## Collection overview\s*\n.*?(?=^## |\Z)'
if not re.search(pattern, text):
    raise SystemExit('Collection overview heading not found; no README changes made.')
text = re.sub(pattern, lambda m: '\n'.join(lines) + '\n', text, count=1)
text = re.sub(r'approximately [\d,]+ EPA SWMM5', f'{totals[0]:,} EPA SWMM5', text, count=1)
readme.write_text(text, encoding='utf-8')
parents = set()
for p in paths:
    parts = p.split('/')
    for i in range(1, len(parts)):
        parents.add('/'.join(parts[:i]))
with (root / 'folder_inventory.csv').open('w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['folder', 'inp_recursive', 'md_recursive', 'rpt_recursive', 'out_recursive', 'all_files_recursive'])
    for folder in sorted(parents, key=str.casefold):
        members = [p for p in paths if p.startswith(folder + '/')]
        c = Counter(Path(p).suffix.lower() for p in members)
        writer.writerow([folder, c['.inp'], c['.md'], c['.rpt'], c['.out'], len(members)])
print(f'Updated {readme.name}: {len(folders)} top-level folders, {totals[0]:,} tracked .inp files.')
print('Wrote folder_inventory.csv with all nested folders. Review with git diff before committing.')
