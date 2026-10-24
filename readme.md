# 1729-SWMM5-Models-2030

A reference library of approximately 3,800 EPA SWMM5 (`.inp`) models covering hydrology, hydraulics, low impact development (LID), water quality, force mains, pumps, weirs, orifices, and dynamic-wave routing. The collection also includes XPSWMM conversions, training examples, and version-specific regression cases.

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

The following model counts are approximate figures from the existing catalog, not a fresh inventory. They should not be interpreted as counts of distinct networks or passing tests.

| Folder | Approximate models | Contents |
|---|--:|---|
| `XPSWMM` | 1,860 | XPSWMM-to-EPA-SWMM5 conversions using the XPSWMM Card Reader |
| `SWMM5_NCIMM` | 590 | Examples and stress tests, from small cases to large networks |
| `EPA` | 150 | EPA examples, Extran-manual cases, and hydraulic-structure tests |
| `OWA_USER` | 150 | Open Water Analytics user and regression examples |
| `Hydrology` | 150 | Runoff, infiltration, snowmelt, RDII, and continuous simulation |
| `Hydraulics` | 140 | Dynamic-wave routing, force mains, and hydraulic structures |
| `LID` | 95 | Bioretention, permeable pavement, green roofs, and other LID controls |
| `Simon_EPA` | 86 | Session 1–81 training collection |
| `OWA_EXTRAN` | 82 | Extran-style hydraulic cases |
| `NCIMM_Training` | 82 | Training-course models |
| `Semi_Real_Models` | 78 | Semi-realistic and real-world-style networks |
| `Training` | 69 | General training examples |
| `OWA_ROUTING` / `NCIMM_ROUTING` | 45 / 30 | Routing test collections |
| `LEW_update_v5113` / `LEW_update_v5115` | 27 / 11 | SWMM 5.1.013 and 5.1.015 regression collections |
| `SWMM5_1_014_Bug_Examples` | 24 | Historical issue-reproduction cases |
| `LEW_CHI_SWMM5.2` | 23 | SWMM 5.2 test cases |
| `Weirs` / `Orifices` / `Pumps` | 23 / 18 / 12 | Hydraulic-structure examples |
| `z1000Years` | 9 | Long continuous-simulation cases |
| `WQ` | 9 | Water-quality and pollutant-routing examples |
| `OWA_update_v5111` | 8 | SWMM 5.1.011 regression cases |

Other collections include variable-roughness tests, named contributions, interface-file tests, and special cases. Preserve each model's accompanying files when copying an example.

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

Repository size, report counts, and summary coverage change as the collection grows; earlier local disk-size estimates are not download guarantees.

## License and provenance

The repository-level dedication is [The Unlicense](LICENSE). Source-specific terms and provenance still need to be checked for contributed or imported material.

- The existing collection includes EPA examples, Open Water Analytics examples and regression models, and Bob Dickinson's XPSWMM-to-SWMM5 conversions.
- Named or contributed folders, including `Greenville`, `Matt_Anderson_Teams`, `Sam`, `logan`, and `Special`, require provenance checks before redistribution.
- The new PySWMM inputs include a BSD-2-Clause license; the swmm-python material includes its own license notice. The addition's README notes that the EPA regression-suite source repository carries no license file.

Consult the [EPA/PySWMM provenance notes](EPA_PYSWMM_Additions/README.md) and accompanying license files rather than assuming the repository-level dedication overrides third-party terms.
