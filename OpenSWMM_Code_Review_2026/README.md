# OpenSWMM code review decks (October 2026)

Added October 23, 2026. This folder holds the 351 reproducer input files from the
[HydroCouple swmm-code-review](https://github.com/HydroCouple/swmm-code-review) at commit
`e13c013` (October 6, 2026): one folder per finding, 200 findings in six categories, each
with its write-up, its decks and data files, the test programs that check the correct
answer, and the fix patches for OpenSWMM 5.3.0 and 6.0.0. The review covers EPA SWMM 5.2.4,
OpenSWMM's legacy 5.3.0 and OpenSWMM 6.0.0. Its own summary is in
[REVIEW_README.md](REVIEW_README.md).

## Why these decks are here

Before this folder, the corpus did not reach the trigger of 53 of the review's
input-reachable findings, and reached 25 more in only one to three models. Every
input-reachable finding now has at least one deck here that reaches it.
[corpus_coverage_vs_code_review.csv](corpus_coverage_vs_code_review.csv) lists all 200
findings with the number of distinct corpus models (outside this folder) that reach each
trigger, example models, and the number of decks here.

How the coverage was measured: each finding's "Reached from" condition was written as a
check on the input file, for example "SURCHARGE_METHOD SLOT with dynamic wave" or "a TIDAL
outfall in a run whose START_TIME is not 00:00". As a control, every check fires on its own
finding's decks. The checks were then run on the 3,189 distinct models of the corpus,
duplicates removed. Checks marked "input feature + runtime condition" can only test the input
features a finding needs, not the runtime condition (a conduit drying out, say).

| Status | Findings |
|---|--:|
| Covered by the corpus (4 or more models) | 90 |
| Thin (1 to 3 models) | 25 |
| Missing (no model) | 53 |
| Reachable only through the toolkit or output API, or the run environment | 29 |
| Reached by every model | 3 |

## Before you batch-run this folder

These are minimal decks built to trigger defects, not ordinary models.
[deck_status_epa524.csv](deck_status_epa524.csv) gives what EPA SWMM 5.2.4 does with each
one: 302 run, 38 stop with an input or file error (often the point of the finding), and
**11 crash or hang EPA SWMM 5.2.4**. Skip or sandbox these:

| Finding | Deck |
|---|---|
| IO-02 | `4-io/IO-02-time-options-accept-nan-inf-huge/IO-02_end-time-1e30.inp` (runs without end) |
| CRASH-03 | `5-crashes/CRASH-03-curve-without-points/CRASH-03_empty-curve.inp` |
| CRASH-03 | `5-crashes/CRASH-03-curve-without-points/CRASH-03_empty-timeseries.inp` |
| CRASH-04 | `5-crashes/CRASH-04-curve-id-only-line-count-pass/CRASH-04_curve-id-only.inp` |
| CRASH-04 | `5-crashes/CRASH-04-curve-id-only-line-count-pass/CRASH-04_quoted-shape.inp` |
| CRASH-05 | `5-crashes/CRASH-05-expression-buffer-overflow/CRASH-05_long-number.inp` |
| CRASH-07 | `5-crashes/CRASH-07-xsection-lookup-nan-index/CRASH-07_nan-diameter.inp` |
| CRASH-07 | `5-crashes/CRASH-07-xsection-lookup-nan-index/CRASH-07_nan-initflow.inp` |
| CRASH-07 | `5-crashes/CRASH-07-xsection-lookup-nan-index/CRASH-07_tiny-diameter.inp` |
| CRASH-08 | `5-crashes/CRASH-08-rule-expression-freed-after-input-error/CRASH-08_expr-bad-option.inp` |
| CRASH-08 | `5-crashes/CRASH-08-rule-expression-freed-after-input-error/CRASH-08_expr-duplicate-id.inp` |

Other notes:

- Keep each deck in its own folder. Rain, climate and interface files sit beside the decks
  that read them, and some findings are about how relative paths resolve.
- Several findings depend on the order of sections or on exact token layout. Do not
  reformat or re-save these decks through a GUI, which writes its own order and layout.
- The decks in `6-api/` and the API parts of `5-crashes/` are inputs for the C test
  programs beside them. Running the deck alone does not show the defect.
- The test programs (`*_test.c`, `*_test6.c`) and patches build with the review's harness,
  which is in the upstream repository and not copied here. See
  [reproducing.md](reproducing.md).
- The status column came from EPA SWMM 5.2.4 built from the `v5.2.4` tag with gcc on Linux.
  The review reports results for OpenSWMM 5.3.0 and 6.0.0 in [verification.md](verification.md).

## Source and license

Everything except this README, `deck_status_epa524.csv` and
`corpus_coverage_vs_code_review.csv` is copied unmodified from swmm-code-review at `e13c013`.
The review's top-level README is renamed `REVIEW_README.md` so that this file can sit at
the folder root; the review's `tools/` folder is not copied.

Copyright 2026 HydroCouple Developers. Licensed under the Apache License, Version 2.0; see
[LICENSE](LICENSE).

## AI use

Claude (Anthropic) ran the coverage comparison and the EPA SWMM 5.2.4 runs, assembled this
folder, and drafted this README. Bob Dickinson reviewed it before adding it.
