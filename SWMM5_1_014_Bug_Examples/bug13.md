# 💧 bug13.inp

![flow units](https://img.shields.io/badge/flow_units-CFS-blue) ![routing](https://img.shields.io/badge/routing-Kinwave-yellowgreen) ![infiltration](https://img.shields.io/badge/infiltration-Horton-9cf) ![nodes](https://img.shields.io/badge/nodes-0-informational) ![links](https://img.shields.io/badge/links-0-informational) ![subcatchments](https://img.shields.io/badge/subcatchments-2-informational) ![status](https://img.shields.io/badge/status-1_error-red)

> [!CAUTION]
> **Run failed** -- 1 fatal error(s) in `bug13.rpt`.<br>ERROR 317: cannot open rainfall data file C:\Xing_Test_Programs\SWMM5_1_014_Bug_Examples\sta310301.dat.

**Title:** Demonstrates the fix for a v5.1.013 bug that skipped the first rain gage when checking if two gages have the same station ID but use different data files. Running this file now correctly produces "Error 156: ambiguous station ID for Rain Ga…  
**Location:** `SWMM5_1_014_Bug_Examples/bug13.inp`

## ⚙️ Configuration

| Setting | Value |
|---|---|
| Flow units | CFS |
| Infiltration | HORTON |
| Flow routing | KINWAVE |
| Simulation start | 06/09/2019 00:00:00 |
| Simulation end | 06/09/2019 06:00:00 |
| Duration | 6 hr |
| Report step | 00:15:00 |
| Routing step | 0:00:30 s |

## 💧 Hydrology

| Item | Count |
|---|--:|
| Subcatchments | 2 |
| Total area (ac) | 10.00 |
| Raingages | 2 |

## 🔧 Hydraulics

| Nodes | Count | Links | Count |
|---|--:|---|--:|
| Junctions | 0 | Conduits | 0 |
| Outfalls | 0 | Pumps | 0 |
| Storage | 0 | Orifices | 0 |
| Dividers | 0 | Weirs | 0 |
| **Total nodes** | **0** | Outlets | 0 |
|  |  | **Total links** | **0** |

---
<sub>📄 Auto-generated 2026-06-24 • summary of `bug13.inp`</sub>
