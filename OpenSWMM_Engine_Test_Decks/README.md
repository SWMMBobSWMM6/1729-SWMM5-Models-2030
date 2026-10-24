# OpenSWMM engine test decks (October 2026)

Added October 23, 2026. These are the 335 input files from the
[OpenSWMM engine repository](https://github.com/HydroCouple/openswmm.engine) (`swmm6_rel` at
`c7cf8844`, October 23, 2026) that were not already in this corpus, together with the data
and reference files that sit beside them. The repository holds 348 `.inp` files; the other 13
were already here, as the same file or a near copy.

Most of them exercise OpenSWMM 6 features (2D coupling, reactions, new options and sections),
so this folder is the corpus's SWMM6 test set.

## What EPA SWMM 5.2.4 does with them

[deck_status_epa524.csv](deck_status_epa524.csv) gives the result for every deck:

| EPA SWMM 5.2.4 | Decks |
|---|--:|
| Runs | 64 |
| Needs OpenSWMM 6 (stops with an input error, mostly ERROR 205 for an unknown keyword) | 250 |
| Stops with another error (ERROR 191, 3xx and similar) | 18 |
| Still running after 120 s | 3 |

Many decks under `tests/unit/` are parser and round-trip tests, not runnable models. Some
name files that do not exist on purpose (absolute paths such as `Z:/data/rain.dat`, or
`../`-chains that test path rebasing), so 5.2.4 stops on them with a file error.

## Layout

Each deck keeps its path from the OpenSWMM repository, for example
`tests/unit/engine/data/...` or `examples/...`, so relative references to data files still
resolve. Keep the folders together when copying.

Copied beside the decks: data files (`.dat`, `.csv`, `.tsv`, `.json`, `.h5`, `.rxn`, `.tsf`,
`.heat`, `.age`, `.ard`), hot start files (`.hsf`, committed even though this repository's
`.gitignore` excludes them, because the decks read them), the OpenSWMM reference reports
(`.rpt`) and the folder notes (`.md`). Not copied: Python and C test code, logs, and binary
`.out` files.

## Source and license

The decks and their files are copied unmodified from openswmm.engine at `c7cf8844`.
Copyright 2026 HydroCouple Developers. Licensed under the Apache License, Version 2.0; see
[LICENSE](LICENSE) and [NOTICE](NOTICE), which also describes the public-domain EPA SWMM
material the engine derives from.

## AI use

Claude (Anthropic) compared these decks with the corpus, ran them on EPA SWMM 5.2.4,
assembled this folder and drafted this README. Bob Dickinson reviewed it before adding it.
