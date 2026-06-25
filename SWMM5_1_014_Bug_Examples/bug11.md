# 💧 bug11.inp

![flow units](https://img.shields.io/badge/flow_units-CFS-blue) ![routing](https://img.shields.io/badge/routing-Dynwave-2ea44f) ![infiltration](https://img.shields.io/badge/infiltration-Horton-9cf) ![nodes](https://img.shields.io/badge/nodes-0-informational) ![links](https://img.shields.io/badge/links-0-informational) ![subcatchments](https://img.shields.io/badge/subcatchments-1-informational) ![status](https://img.shields.io/badge/status-clean_run-2ea44f)

> [!TIP]
> Ran clean -- no errors or warnings reported.<br>Continuity error(s): -0.297, 0.000 %

**Title:** Demonstrates the fix for a v5.1.013 bug that ignored street sweeping when thesweeping period began with a higher day of the year than the end of the period. Running this file, with a sweeping period of October - June, now shows a Sweeping R…  
**Location:** `SWMM5_1_014_Bug_Examples/bug11.inp`

## ⚙️ Configuration

| Setting | Value |
|---|---|
| Flow units | CFS |
| Infiltration | HORTON |
| Flow routing | DYNWAVE |
| Simulation start | 06/08/2019 00:00:00 |
| Simulation end | 06/20/2019 00:00:00 |
| Duration | 12 days |
| Report step | 00:15:00 |
| Routing step | 0:00:30 s |

## 💧 Hydrology

| Item | Count |
|---|--:|
| Subcatchments | 1 |
| Total area (ac) | 1.00 |
| Raingages | 1 |

## 🔧 Hydraulics

| Nodes | Count | Links | Count |
|---|--:|---|--:|
| Junctions | 0 | Conduits | 0 |
| Outfalls | 0 | Pumps | 0 |
| Storage | 0 | Orifices | 0 |
| Dividers | 0 | Weirs | 0 |
| **Total nodes** | **0** | Outlets | 0 |
|  |  | **Total links** | **0** |

## ⚗️ Water Quality

Pollutants: **1** &nbsp;|&nbsp; Land uses: **1**

## 📈 Forcing & Data

| Item | Count |
|---|--:|
| Time series | 1 |

---
<sub>📄 Auto-generated 2026-06-24 • summary of `bug11.inp`</sub>
