# 1729-SWMM5-Models-2030

A reference library of 3,854 EPA SWMM5 input (`.inp`) files covering hydrology, hydraulics, low impact development (LID), water quality, force mains, pumps, weirs, orifices, and dynamic-wave routing. The collection also includes XPSWMM conversions, training examples, and version-specific regression cases.

Maintained by Robert (Bob) Dickinson.

## Recent additions: EPA and PySWMM test models

Added October 23, 2026: [EPA_PYSWMM_Additions](EPA_PYSWMM_Additions/), assembled by comparing EPA, PySWMM, and swmm-python test inputs against the existing corpus.

| Subfolder | Contents |
|---|---|
| `EPA_nrtestsuite_v2.5.0-dev/swc/` | 25 National Stormwater Calculator input decks, three NCDC rainfall files, and EPA documentation |
| `EPA_nrtestsuite_v2.5.0-dev/examples/` | Example2 and Example3 |
| `EPA_nrtestsuite_v2.5.0-dev/revisions/` | Four alternate or updated inputs: Example4, user2, CoS-Reduced-Inlets, and CoS-Reduced-Outlets |
| `PYSWMM_tests/` | Seven PySWMM test and documentation models |
| `SWMM_PYTHON_tests/` | test_Example3 and test_Example3.old |

The addition's README reports 40 previously missing models and separately lists four alternate or updated revisions. Matching used file content rather than filenames, including normalized comparisons and nearest-neighbor similarity. See the [addition's README](EPA_PYSWMM_Additions/README.md) for the comparison method, source revision, licensing, and AI-use disclosure. These are documented corpus-comparison results, not a claim that every input is unique or independently validated.

## Start here

- Learning SWMM: [Training](Training/), [Simon_EPA](Simon_EPA/), and [NCIMM_Training](NCIMM_Training/).
- Rainfall-runoff processes: [Hydrology](Hydrology/) and shared forcing data in [DataFiles](DataFiles/).
- Hydraulic routing and structures: [Hydraulics](Hydraulics/), [Pumps](Pumps/), [Weirs](Weirs/), and [Orifices](Orifices/).
- Green infrastructure and water quality: [LID](LID/) and [WQ](WQ/).
- Solver comparisons and regression work: OWA and version-specific folders, plus [EPA_PYSWMM_Additions](EPA_PYSWMM_Additions/).
- Converted XPSWMM models: [XPSWMM](XPSWMM/).

## Collection overview

Counts below come from a local inventory of the maintainer's working copy taken October 23, 2026: 20,463 files totaling 15,962 MB (about 15.6 GB), excluding the `.git` directory. The working copy includes generated results and other files that Git may ignore, so these figures may differ from the files tracked on GitHub and are not a download-size estimate.

All 42 top-level folders and the repository root are listed, ordered by file count. Sizes are rounded to the nearest MB; folders shown as 0 MB are under 0.5 MB.

| Folder | `.inp` | `.rpt` | `.out` | `.md` | All files | MB | Contents |
|---|--:|--:|--:|--:|--:|--:|---|
| [`XPSWMM`](XPSWMM/) | 1,859 | 1,859 | 1,859 | 1,859 | 9,461 | 1,906 | XPSWMM-to-EPA-SWMM5 conversions using the XPSWMM Card Reader; also 1,859 `.xp` and 111 `.xpx` files |
| [`SWMM5_NCIMM`](SWMM5_NCIMM/) | 589 | 589 | 386 | 589 | 2,177 | 6,388 | Examples and stress tests, from small cases to large networks |
| [`EPA`](EPA/) | 154 | 154 | 149 | 154 | 899 | 995 | EPA examples, Extran-manual cases, and hydraulic-structure tests |
| [`OWA_USER`](OWA_USER/) | 151 | 151 | 120 | 151 | 854 | 406 | Open Water Analytics user and regression examples |
| [`Simon_EPA`](Simon_EPA/) | 86 | 86 | 84 | 86 | 848 | 691 | Session 1–81 training collection |
| [`NCIMM_Training`](NCIMM_Training/) | 82 | 85 | 76 | 82 | 844 | 2,217 | Training-course models; includes 391 `.dat` files and course materials |
| [`Hydraulics`](Hydraulics/) | 140 | 140 | 127 | 140 | 799 | 636 | Dynamic-wave routing, force mains, and hydraulic structures |
| [`Hydrology`](Hydrology/) | 149 | 149 | 131 | 149 | 644 | 825 | Runoff, infiltration, snowmelt, RDII, and continuous simulation |
| [`LID`](LID/) | 95 | 95 | 78 | 95 | 528 | 7 | Bioretention, permeable pavement, green roofs, and other LID controls |
| [`OWA_EXTRAN`](OWA_EXTRAN/) | 82 | 82 | 76 | 82 | 470 | 13 | Extran-style hydraulic cases |
| [`Semi_Real_Models`](Semi_Real_Models/) | 78 | 78 | 60 | 78 | 455 | 566 | Semi-realistic and real-world-style networks |
| [`Training`](Training/) | 69 | 69 | 57 | 69 | 380 | 259 | General training examples |
| [`january5_2003_examples`](january5_2003_examples/) | 0 | 16 | 16 | 0 | 311 | 1 | Historical examples: 276 `.dat` files plus reports and outputs; no `.inp` files |
| [`Viewer-Demo-Results`](Viewer-Demo-Results/) | 17 | 17 | 17 | 1 | 244 | 18 | Viewer demonstration models and results |
| [`OWA_ROUTING`](OWA_ROUTING/) | 45 | 45 | 43 | 45 | 189 | 12 | Open Water Analytics routing tests |
| [`EPA_PYSWMM_Additions`](EPA_PYSWMM_Additions/) | 40 | 40 | 40 | 3 | 139 | 212 | EPA, PySWMM, and swmm-python test models (see below) |
| [`Weirs`](Weirs/) | 23 | 23 | 22 | 23 | 122 | 1 | Weir examples |
| [`v13`](v13/) | 0 | 118 | 0 | 0 | 119 | 5 | Reports only; no `.inp` files |
| [`Orifices`](Orifices/) | 18 | 18 | 17 | 18 | 118 | 1 | Orifice examples |
| [`NCIMM_ROUTING`](NCIMM_ROUTING/) | 30 | 30 | 21 | 30 | 112 | 293 | Routing test collection |
| [`LEW_update_v5113`](LEW_update_v5113/) | 27 | 27 | 8 | 27 | 102 | 7 | SWMM 5.1.013 regression collection |
| [`LEW_CHI_SWMM5.2`](LEW_CHI_SWMM5.2/) | 23 | 23 | 21 | 23 | 92 | 2 | SWMM 5.2 test cases |
| [`v12`](v12/) | 0 | 89 | 0 | 0 | 90 | 2 | Reports only; no `.inp` files |
| [`Pumps`](Pumps/) | 12 | 12 | 11 | 12 | 84 | 28 | Pump examples |
| [`SWMM5_1_014_Bug_Examples`](SWMM5_1_014_Bug_Examples/) | 24 | 24 | 9 | 24 | 81 | 7 | Historical issue-reproduction cases |
| [`OWA_update_v5111`](OWA_update_v5111/) | 8 | 8 | 3 | 8 | 44 | 52 | SWMM 5.1.011 regression cases |
| [`LEW_update_v5115`](LEW_update_v5115/) | 11 | 11 | 10 | 11 | 44 | 1 | SWMM 5.1.015 regression collection |
| [`z1000Years`](z1000Years/) | 9 | 9 | 2 | 9 | 40 | 92 | Long continuous-simulation cases |
| [`WQ`](WQ/) | 9 | 9 | 7 | 9 | 36 | 21 | Water-quality and pollutant-routing examples |
| [`Greenville`](Greenville/) | 3 | 3 | 2 | 3 | 33 | 35 | Contributed models; includes ICM transfer (`.icmt`) files |
| [`Matt_Anderson_Teams`](Matt_Anderson_Teams/) | 6 | 6 | 2 | 6 | 20 | 19 | Contributed models |
| (root) | 0 | 0 | 0 | 2 | 15 | 0 | Repository metadata, scripts, and support files |
| [`DataFiles`](DataFiles/) | 0 | 0 | 0 | 1 | 13 | 42 | Shared rainfall and forcing data (`.dat`, `.ncd`) |
| [`Special`](Special/) | 2 | 4 | 1 | 1 | 12 | 201 | Special cases |
| [`Sam`](Sam/) | 2 | 2 | 2 | 2 | 9 | 1 | Contributed models |
| [`AD_SSF`](AD_SSF/) | 2 | 2 | 2 | 2 | 8 | 0 | Small test set |
| [`15100`](15100/) | 2 | 2 | 2 | 2 | 8 | 0 | Small test set |
| [`VRough_Tests`](VRough_Tests/) | 2 | 2 | 0 | 2 | 6 | 0 | Variable-roughness tests |
| [`logan`](logan/) | 1 | 1 | 0 | 1 | 3 | 0 | Contributed model |
| [`VRough_Tests_EPA`](VRough_Tests_EPA/) | 1 | 1 | 0 | 1 | 3 | 0 | Variable-roughness test |
| [`RED_Files`](RED_Files/) | 1 | 1 | 0 | 1 | 3 | 0 | Single test model |
| [`Test_Interface_Files`](Test_Interface_Files/) | 1 | 0 | 0 | 1 | 2 | 0 | Interface-file test |
| [`Simple Test Models`](Simple%20Test%20Models/) | 1 | 0 | 0 | 0 | 2 | 0 | Simple test model |
| Total | 3,854 | 4,080 | 3,461 | 3,802 | 20,463 | 15,962 | |

Equal counts of `.inp`, `.rpt`, `.out`, and `.md` files in a folder do not by themselves prove that each input has a matching report, output, and summary. Confirming result coverage requires matching files by folder and base name. Likewise, `.inp` totals are file counts, not counts of distinct networks or passing tests.

Preserve each model's accompanying files when copying an example.

### By file type

| File type | Files | Size (MB) |
|---|--:|--:|
| Binary results (`.out`) | 3,461 | 10,464.6 |
| SWMM input files (`.inp`) | 3,854 | 2,161.8 |
| Data files (`.dat`) | 688 | 1,700.8 |
| XPSWMM files (`.xp`) | 1,859 | 793.2 |
| Text reports (`.rpt`) | 4,080 | 531.1 |
| XPSWMM `.xpx` files | 111 | 119.0 |
| Text files (`.txt`) | 1,762 | 30.5 |
| Markdown files (`.md`) | 3,802 | 5.1 |
| Other files | 846 | about 156 |
| Total | 20,463 | 15,962 |

Binary `.out` results account for about two-thirds (65.6%) of the local collection's size. `SWMM5_NCIMM` is the largest folder by size (6,388 MB), while `XPSWMM` holds 46% of all files but about 12% of the space.

## Per-model Markdown summaries

The library includes auto-generated Markdown summaries alongside model inputs. Where available, these provide:

- Flow units, routing and infiltration methods, and object counts.
- Simulation dates, time steps, and model configuration.
- Inventories of subcatchments, nodes, links, and hydraulic structures.
- LID, water-quality, control-rule, and forcing details where applicable.
- Report-derived run status, warnings, errors, and continuity information when an accompanying report is available.

Check the actual `.inp` and `.rpt` files before relying on a summary. A stored report describes a particular run; it does not establish that a changed input or a different solver version will produce the same result. Summary coverage should not be assumed for newly added files.

## Running a model

1. Clone or download the repository:

   ```bash
   git clone https://github.com/SWMMBobSWMM6/1729-SWMM5-Models-2030.git
   cd 1729-SWMM5-Models-2030
   ```

2. Select an input and review its title, options, external-file references, and any accompanying documentation.
3. Use EPA SWMM 5.2 as a starting point, while checking version requirements for historical regression cases. Confirm rainfall, time-series, and interface-file paths before running.
4. Open the input in the SWMM interface, or run an installed command-line solver:

   ```text
   runswmm.exe model.inp model.rpt model.out
   ```

   Replace the executable name or path with your installed solver. The repository also includes `runswmm.bat`; review its local paths and settings before use.

5. Inspect the new report for errors, warnings, continuity, and numerical behavior before interpreting results. For comparisons, record the solver version and preserve the input and supporting data used.

The collection includes stress tests and historical bug-reproduction inputs. Inclusion is not a guarantee of successful execution, calibration, or suitability for design.

## Reports, binary results, and ignored files

- `.inp`: model input.
- `.md`: documentation and model summaries where available.
- `.rpt`: text reports from stored runs where included.
- `.out`: binary simulation results; availability varies by folder.

The root [`.gitignore`](.gitignore) excludes `.out`, `.hsf`, and `.rdii` files in upper- and lowercase forms, along with temporary artifacts. Ignore rules do not remove files already tracked in Git, so selected committed outputs may still be present. Do not assume that every model includes binary results; regenerate outputs using the intended solver and required supporting data.

Repository size, report counts, and summary coverage change as the collection grows. The inventory above describes a local working copy, not the GitHub download size.

## License and provenance

The repository-level dedication is [The Unlicense](LICENSE). Source-specific terms and provenance still need to be checked for contributed or imported material.

- The existing collection includes EPA examples, Open Water Analytics examples and regression models, and Bob Dickinson's XPSWMM-to-SWMM5 conversions.
- Named or contributed folders, including `Greenville`, `Matt_Anderson_Teams`, `Sam`, `logan`, and `Special`, require provenance checks before redistribution.
- The new PySWMM inputs include a BSD-2-Clause license; the swmm-python material includes its own license notice. The addition's README notes that the EPA regression-suite source repository carries no license file.

Consult the [EPA/PySWMM provenance notes](EPA_PYSWMM_Additions/README.md) and accompanying license files rather than assuming the repository-level dedication overrides third-party terms.
