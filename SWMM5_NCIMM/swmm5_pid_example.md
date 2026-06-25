# 💧 swmm5_pid_example.inp

![flow units](https://img.shields.io/badge/flow_units-CFS-blue) ![routing](https://img.shields.io/badge/routing-Dynwave-2ea44f) ![infiltration](https://img.shields.io/badge/infiltration-Horton-9cf) ![nodes](https://img.shields.io/badge/nodes-61-informational) ![links](https://img.shields.io/badge/links-57-informational) ![subcatchments](https://img.shields.io/badge/subcatchments-0-informational) ![status](https://img.shields.io/badge/status-9_errors-red)

> [!CAUTION]
> **Run failed** -- 9 fatal error(s) in `swmm5_pid_example.rpt`.<br>ERROR 205: invalid keyword BYPASS at line 32 of [OPTION] section:; ERROR 205: invalid keyword MAX_ITERATIONS at line 33 of [OPTION] section:

**Title:** Input and Output FilesSW 1 0 20 Input and Output FilesSW 1 0 20  
**Location:** `SWMM5_NCIMM/swmm5_pid_example.inp`

## ⚙️ Configuration

| Setting | Value |
|---|---|
| Flow units | CFS |
| Infiltration | HORTON |
| Flow routing | DYNWAVE |
| Simulation start | 01/01/1988 00:00:00 |
| Simulation end | 01/01/1988 06:00:00 |
| Duration | 6 hr |
| Report step | 00:05:00 |
| Routing step | 0:00:20 s |

## 🔧 Hydraulics

| Nodes | Count | Links | Count |
|---|--:|---|--:|
| Junctions | 54 | Conduits | 54 |
| Outfalls | 6 | Pumps | 1 |
| Storage | 1 | Orifices | 2 |
| Dividers | 0 | Weirs | 0 |
| **Total nodes** | **61** | Outlets | 0 |
|  |  | **Total links** | **57** |

> Cross-sections: **56**

## 🎛️ Control Rules

Real-time control rules: **1**

## 📈 Forcing & Data

| Item | Count |
|---|--:|
| Direct inflows | 18 |
| Dry-weather inflows | 1 |
| Time series | 18 |
| Curves | 10 |

---
<sub>📄 Auto-generated 2026-06-24 • summary of `swmm5_pid_example.inp`</sub>
