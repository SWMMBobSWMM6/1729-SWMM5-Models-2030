# EPA and PySWMM test models added to the corpus

Added 2026-10-23. These 40 models were missing from this corpus before this folder:
every other model in EPA's regression suite and in the pyswmm and swmm-python test
sets was already here, as the same file or a near copy.

## How "missing" was decided

Models were matched by content, not file name, in four steps: identical bytes;
identical after whitespace and number formatting; identical outside `[TITLE]`,
`[MAP]`, `[COORDINATES]` and the other drawing sections; and finally the nearest
neighbour by Jaccard similarity of the normalized input lines. A model counts as
missing when its best match in the corpus scored below 0.70.

## What is here

| Folder | Source | Contents |
|---|---|---|
| `EPA_nrtestsuite_v2.5.0-dev/swc/` | USEPA/swmm-nrtestsuite | 25 National Stormwater Calculator decks (LID controls, climate scenarios, 3-year continuous and 5- to 100-year extreme events), their 3 NCDC rain files and EPA's README |
| `EPA_nrtestsuite_v2.5.0-dev/examples/` | USEPA/swmm-nrtestsuite | Example2 and Example3 (best corpus matches 0.65 and 0.40) |
| `EPA_nrtestsuite_v2.5.0-dev/revisions/` | USEPA/swmm-nrtestsuite | Example4, user2, CoS-Reduced-Inlets, CoS-Reduced-Outlets: the corpus held an older or different revision (0.81 to 0.94) |
| `PYSWMM_tests/` | pyswmm/pyswmm | 7 test and docs models |
| `SWMM_PYTHON_tests/` | pyswmm/swmm-python | test_Example3 and test_Example3.old |

EPA's suite came from its default branch (d23f9d6); the v2.5.0-dev tag that EPA's CI
pins holds the same 73 input files.

## Licenses

pyswmm is BSD-2-Clause; its `LICENSE.txt` travels with those files. swmm-python's
swmm-toolkit declares its material a U.S. Government work with no copyright
restriction (`LICENSE.md` included). The EPA suite repository carries no license file.

## AI use

Claude (Anthropic) ran the comparison and assembled this folder; Bob Dickinson
reviewed it before adding it.
