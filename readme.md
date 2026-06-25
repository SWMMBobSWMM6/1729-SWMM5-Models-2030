# 1729-SWMM5-Models

A reference library of **~3,800 EPA SWMM5 (`.inp`) models** — hydrology, hydraulics, LID, water quality, force mains, pumps, weirs, orifices, and dynamic-wave routing, plus XPSWMM conversions and training examples. Every model is paired with an auto-generated Markdown summary.

## Repository at a glance

| | |
|---|---|
| SWMM5 input models (`.inp`) | ~3,800 |
| Per-model summaries (`.md`) | one per model |
| Report files (`.rpt`) | ~2,100 |
| Tracked files | ~13,100 |
| Repository size (`.git`) | ~670 MB |
| Output files (`.out`) | kept on disk, **not** tracked (see below) |

## Folder breakdown

| Folder | Models | Contents |
|---|--:|---|
| `XPSWMM` | ~1,860 | Models converted from XPSWMM (`.xp`) to EPA SWMM5 via the XPSWMM Card Reader |
| `SWMM5_NCIMM` | ~590 | Core EPA SWMM5 examples and stress tests, from tiny cases to very large networks |
| `EPA` | ~150 | EPA SWMM5 examples, Extran-manual cases, and hydraulic-structure tests |
| `OWA_USER` | ~150 | Open Water Analytics user and regression examples |
| `Hydrology` | ~150 | Runoff/infiltration, snowmelt, RDII, and continuous-simulation models |
| `Hydraulics` | ~140 | Dynamic-wave routing, force mains, and structure tests |
| `LID` | ~95 | Low Impact Development controls (bioretention, permeable pavement, green roofs, …) |
| `Simon_EPA` | ~86 | Curated Session 1–81 training set |
| `OWA_EXTRAN` | ~82 | Open Water Analytics Extran-style hydraulic cases |
| `NCIMM_Training` | ~82 | NC IMM training-course models |
| `Semi_Real_Models` | ~78 | Semi-realistic / real-world-style networks |
| `Training` | ~69 | General training and course examples |
| `OWA_ROUTING` | ~45 | OWA routing regression cases |
| `NCIMM_ROUTING` | ~30 | NCIMM routing analyses |
| `LEW_update_v5113` / `LEW_update_v5115` | ~27 / ~11 | Version-specific regression sets (SWMM 5.1.013 / 5.1.015) |
| `SWMM5_1_014_Bug_Examples` | ~24 | Cases reproducing SWMM 5.1.014 issues |
| `LEW_CHI_SWMM5.2` | ~23 | LEW / CHI SWMM5.2 test cases |
| `Weirs` / `Orifices` / `Pumps` | ~23 / ~18 / ~12 | Hydraulic-structure test models |
| `z1000Years` | ~9 | Long continuous (1,000-year) simulations |
| `WQ` | ~9 | Water-quality / pollutant-routing models |
| `OWA_update_v5111` | ~8 | OWA SWMM 5.1.011 regression set |
| `VRough_Tests` / `VRough_Tests_EPA` | ~3 | Variable Manning's-roughness tests |
| `Greenville`, `Matt_Anderson_Teams`, `Sam`, `logan`, `Special`, `AD_SSF`, `15100`, `RED_Files`, `Test_Interface_Files` | misc | Named, contributed, and special-case models |
| `DataFiles` | — | Shared rainfall and external data files (`.dat`, `.rff`, …) referenced by the models |

*Counts are approximate; the `XPSWMM` set dominates the file total.*

## Per-model Markdown summaries

Every `<model>.inp` has a matching `<model>.md` beside it — a one-page summary you can read on GitHub without opening SWMM. Each summary includes:

- **Badges** — flow units, routing method, infiltration method, and node / link / subcatchment counts
- **Run status** — a colored callout pulled from the model's `.rpt` (clean / warnings / errors, with continuity error)
- **Configuration** — flow units, infiltration, routing, simulation window, and time steps
- **Inventory** — junctions, outfalls, storage, conduits, pumps, orifices, weirs, outlets, plus subcatchment count and total area
- **LID, water quality, controls, and forcing** sections, shown only when the model uses them

The summaries are generated directly from each `.inp` (and its sibling `.rpt`), so they stay in step with the models.

## Output files (`.out`) are not tracked

SWMM5 binary results files (`*.out`, roughly **8.8 GB** across the library) are **git-ignored**. They stay on disk for immediate use but are kept out of version control so the repository stays small — `.git` is ~670 MB instead of several GB. Hot-start interface files (`*.hsf`) are excluded for the same reason. See [`.gitignore`](.gitignore).

To recreate any `.out`, re-run its model in EPA SWMM 5.2.

## Running a model

Open any `.inp` in **EPA SWMM 5.2**, or run it from the command line:

```
runswmm.exe  model.inp  model.rpt  model.out
```

`runswmm.bat` in the repository root wraps this for batch runs.

---

*EPA SWMM5 model library maintained by Robert (Bob) Dickinson.*
