# 💧 bug17.inp

![flow units](https://img.shields.io/badge/flow_units-CMS-blue) ![routing](https://img.shields.io/badge/routing-Dynwave-2ea44f) ![infiltration](https://img.shields.io/badge/infiltration-Horton-9cf) ![nodes](https://img.shields.io/badge/nodes-11-informational) ![links](https://img.shields.io/badge/links-10-informational) ![subcatchments](https://img.shields.io/badge/subcatchments-1-informational) ![status](https://img.shields.io/badge/status-2_warnings-orange)

> [!WARNING]
> Ran with **2 warning(s)** and no fatal errors.<br>Continuity error(s): -0.501, -0.121 %

**Title:** Demonstrates the fix for a v5.1.013 parsing bug that incorrectly interpreted an ID name in the [REPORT] section begining with "ALL" as the "ALL" keyword (with the same behavior for the "NONE" keyword). Running this file shows that the entri…  
**Location:** `SWMM5_1_014_Bug_Examples/bug17.inp`

## ⚙️ Configuration

| Setting | Value |
|---|---|
| Flow units | CMS |
| Infiltration | HORTON |
| Flow routing | DYNWAVE |
| Simulation start | 04/08/2008 10:00:00 |
| Simulation end | 04/08/2008 22:00:00 |
| Duration | 12 hr |
| Report step | 00:01:00 |
| Routing step | 0:00:05 s |

## 💧 Hydrology

| Item | Count |
|---|--:|
| Subcatchments | 1 |
| Total area (ha) | 7.39 |
| Raingages | 1 |

## 🔧 Hydraulics

| Nodes | Count | Links | Count |
|---|--:|---|--:|
| Junctions | 10 | Conduits | 10 |
| Outfalls | 1 | Pumps | 0 |
| Storage | 0 | Orifices | 0 |
| Dividers | 0 | Weirs | 0 |
| **Total nodes** | **11** | Outlets | 0 |
|  |  | **Total links** | **10** |

> Cross-sections: **10**

## 📈 Forcing & Data

| Item | Count |
|---|--:|
| Dry-weather inflows | 1 |
| Time series | 1 |

---
<sub>📄 Auto-generated 2026-06-24 • summary of `bug17.inp`</sub>
