#!/usr/bin/env python3
"""
fix_rainfall_paths.py  --  1729-SWMM5-Models-2030 corpus maintenance

Repoints every external data-file reference in every .inp/.INP file at the
repository's DataFiles/ folder, and consolidates into DataFiles/ any data file
that already exists somewhere else in the repo.

WHY RELATIVE PATHS
------------------
Verified against EPA SWMM 5.2.4: the engine resolves a relative data-file path
against the directory of the .inp file itself, NOT the process working
directory.  Proof -- a model in <root>/Sub run with cwd=/ and the path written
as "../DataFiles/rain.dat" opens the file, and a deliberately bad name reports
    ERROR 317: cannot open rainfall data file /<root>/Sub/../DataFiles/BAD.dat
i.e. the engine prepended the .inp's own folder.  So "..\\DataFiles\\x.dat"
points at the same folder an absolute path would, but survives moving or
cloning the repo -- which is precisely what broke the old
C:\\Users\\rober\\OneDrive\\Documents\\GitHub\\1729-SWMM5-Models\\... paths.

Pass --absolute to write C:\\...\\1729-SWMM5-Models-2030\\DataFiles\\x.dat
instead (not recommended; it re-creates the fragility).

SECTIONS TOUCHED
----------------
  [RAINGAGES]   ... FILE <fname> ...     -> ERROR 317 when unresolvable
  [TEMPERATURE] FILE <fname>             -> climate file
  [TIMESERIES]  <name> FILE <fname>      -> ERROR 361 when unresolvable

NOT touched: [FILES] USE/SAVE (interface + hot-start files -- these are run
artifacts, not input data, and SAVE targets get overwritten by the engine), and
the placeholder gage filename "-" used by the XP-converted SWMM5_NCIMM models.

USAGE
-----
    python fix_rainfall_paths.py                 # dry run, prints the plan
    python fix_rainfall_paths.py --apply         # edit in place
    python fix_rainfall_paths.py --apply --absolute
    python fix_rainfall_paths.py --root "C:\\Users\\rober\\GitHub\\1729-SWMM5-Models-2030"

Idempotent: running it twice changes nothing the second time.
Writes rainfall_path_manifest.csv next to the repo root.
"""

import argparse
import collections
import csv
import ntpath
import os
import re
import shutil
import sys

SECTIONS = ("RAINGAGES", "TEMPERATURE", "TIMESERIES")
DATA_DIR = "DataFiles"
ABS_ROOT = r"C:\Users\rober\GitHub\1729-SWMM5-Models-2030"
SKIP_TOKENS = {"", "-", '""'}
# folders that hold engine output, not source models
SKIP_DIRS = {".git", "__pycache__"}

TOKEN = re.compile(r'"([^"]*)"|(\S+)')


def tokens(line):
    """Quote-aware token split; returns (text, start, end) per token."""
    return [
        (m.group(1) if m.group(1) is not None else m.group(2), m.start(), m.end())
        for m in TOKEN.finditer(line)
    ]


def index_repo(root):
    """basename(upper) -> [relative paths], for locating data files already in the repo."""
    index = collections.defaultdict(list)
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for name in filenames:
            rel = os.path.relpath(os.path.join(dirpath, name), root).replace("\\", "/")
            index[name.upper()].append(rel)
    return index


def find_models(root):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for name in sorted(filenames):
            if name.lower().endswith(".inp"):
                yield os.path.relpath(os.path.join(dirpath, name), root).replace("\\", "/")


def target_path(model_rel, basename, absolute):
    if absolute:
        return "%s\\%s\\%s" % (ABS_ROOT, DATA_DIR, basename)
    depth = model_rel.count("/")
    return "../" * depth + DATA_DIR + "/" + basename


def rewrite_file(path, model_rel, absolute):
    """Return (new_text, [(line_no, section, old, new)]) or (None, []) if unchanged."""
    with open(path, "r", errors="replace", newline="") as fh:
        lines = fh.read().splitlines(keepends=True)

    section, edits = "", []
    for i, raw in enumerate(lines):
        stripped = raw.strip()
        if stripped.startswith("["):
            inner = stripped.strip("[]")
            section = inner.upper().split()[0] if inner else ""
            continue
        if not stripped or stripped.startswith(";"):
            continue

        # SWMM section headers are matched on their first 4+ chars; RAINGAGE/RAINGAGES both occur
        sec = "RAINGAGES" if section.startswith("RAINGAGE") else section
        if sec not in SECTIONS:
            continue

        tok = tokens(raw)
        upper = [t[0].upper() for t in tok]
        if "FILE" not in upper:
            continue
        k = upper.index("FILE")
        if sec == "TEMPERATURE" and k != 0:
            continue  # [TEMPERATURE] only uses FILE as the leading keyword
        if k + 1 >= len(tok):
            continue

        old, start, end = tok[k + 1]
        if old.strip() in SKIP_TOKENS:
            continue

        base = ntpath.basename(old.replace("\\", "/"))
        if not base:
            continue
        new = target_path(model_rel, base, absolute)
        if old == new:
            continue  # already fixed -- idempotent

        replacement = '"%s"' % new
        # absorb some of the trailing padding so column alignment survives
        tail = raw[end:]
        pad = len(tail) - len(tail.lstrip(" "))
        shrink = min(pad - 1, max(0, len(replacement) - (end - start))) if pad > 1 else 0
        lines[i] = raw[:start] + replacement + raw[end + shrink:]
        edits.append((i + 1, sec, old, new))

    return ("".join(lines) if edits else None), edits


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default=".", help="repository root (default: current directory)")
    ap.add_argument("--apply", action="store_true", help="write changes (default is a dry run)")
    ap.add_argument("--absolute", action="store_true", help="write absolute DataFiles paths instead of relative")
    ap.add_argument("--no-copy", action="store_true", help="do not consolidate data files into DataFiles/")
    ap.add_argument("--manifest", default="rainfall_path_manifest.csv")
    args = ap.parse_args()

    root = os.path.abspath(args.root)
    if not os.path.isdir(root):
        sys.exit("no such directory: %s" % root)
    datadir = os.path.join(root, DATA_DIR)
    if not os.path.isdir(datadir):
        sys.exit("expected a %s folder under %s" % (DATA_DIR, root))

    index = index_repo(root)
    manifest, touched, copied, missing = [], {}, [], collections.Counter()

    for model_rel in find_models(root):
        full = os.path.join(root, model_rel)
        new_text, edits = rewrite_file(full, model_rel, args.absolute)
        if not edits:
            continue
        touched[model_rel] = len(edits)
        if args.apply and new_text is not None:
            with open(full, "w", newline="") as fh:
                fh.write(new_text)
        for line_no, sec, old, new in edits:
            base = ntpath.basename(new.replace("\\", "/"))
            hits = index.get(base.upper(), [])
            source = ""
            for h in hits:
                if h.upper().startswith(DATA_DIR.upper() + "/"):
                    source = h
                    break
            if not source and hits:
                source = hits[0]
            if not source:
                missing[base] += 1
            manifest.append(dict(model=model_rel, line=line_no, section=sec,
                                 old_path=old, new_path=new,
                                 data_source=source,
                                 status="RESOLVES" if source else "DATA MISSING"))

    # consolidate data files that exist elsewhere in the repo
    if not args.no_copy:
        for row in manifest:
            src = row["data_source"]
            if not src or src.upper().startswith(DATA_DIR.upper() + "/"):
                continue
            dst_rel = DATA_DIR + "/" + ntpath.basename(row["new_path"].replace("\\", "/"))
            dst = os.path.join(root, dst_rel)
            if os.path.exists(dst):
                continue
            copied.append((src, dst_rel))
            if args.apply:
                shutil.copy2(os.path.join(root, src), dst)

    mode = "APPLIED" if args.apply else "DRY RUN (use --apply to write)"
    style = "absolute" if args.absolute else "relative"
    print("%s  --  %s paths, root %s" % (mode, style, root))
    print("  reference lines rewritten : %d" % len(manifest))
    print("  models touched            : %d" % len(touched))
    print("  data files consolidated   : %d" % len(set(d for _, d in copied)))
    for src, dst in sorted(set(copied), key=lambda x: x[1]):
        print("      %-34s <- %s" % (dst, src))
    resolves = sum(1 for r in manifest if r["status"] == "RESOLVES")
    print("  lines that now resolve    : %d" % resolves)
    print("  lines still missing data  : %d  (%d distinct filenames)" % (len(manifest) - resolves, len(missing)))
    if missing:
        print("  most-referenced missing files:")
        for base, n in missing.most_common(8):
            print("      %5d lines  %s" % (n, base))

    out = os.path.join(root, args.manifest)
    if args.apply or True:  # the manifest is always useful, even on a dry run
        with open(out, "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=["model", "line", "section", "old_path",
                                               "new_path", "data_source", "status"])
            w.writeheader()
            w.writerows(manifest)
        print("  manifest written          : %s" % out)


if __name__ == "__main__":
    main()
