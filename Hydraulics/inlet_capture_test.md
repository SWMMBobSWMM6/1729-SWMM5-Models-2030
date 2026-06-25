# 💧 inlet_capture_test.inp

![flow units](https://img.shields.io/badge/flow_units-CFS-blue) ![routing](https://img.shields.io/badge/routing-Dynwave-2ea44f) ![infiltration](https://img.shields.io/badge/infiltration-Horton-9cf) ![nodes](https://img.shields.io/badge/nodes-11-informational) ![links](https://img.shields.io/badge/links-8-informational) ![subcatchments](https://img.shields.io/badge/subcatchments-0-informational) ![status](https://img.shields.io/badge/status-15_errors-red)

> [!CAUTION]
> **Run failed** -- 15 fatal error(s) in `inlet_capture_test.rpt`.<br>ERROR 211: invalid number P-50 at line 89 of [INLET] section:; ERROR 205: invalid keyword 0.0 at line 93 of [INLET_USAGE] section:

**Title:** Two Streets with HEC-22 Inlets - Full Flow vs. Distributed Flow Street 1: 2.4 cfs at top (J1) Street 2: 0.6 cfs at each node (J6-J9)  
**Location:** `Hydraulics/inlet_capture_test.inp`

## ⚙️ Configuration

| Setting | Value |
|---|---|
| Flow units | CFS |
| Infiltration | HORTON |
| Flow routing | DYNWAVE |
| Simulation start | 05/01/2025 00:00:00 |
| Simulation end | 05/01/2025 03:00:00 |
| Duration | 3 hr |
| Report step | 00:01:00 |
| Routing step | 0:00:30 s |

## 🔧 Hydraulics

| Nodes | Count | Links | Count |
|---|--:|---|--:|
| Junctions | 10 | Conduits | 8 |
| Outfalls | 1 | Pumps | 0 |
| Storage | 0 | Orifices | 0 |
| Dividers | 0 | Weirs | 0 |
| **Total nodes** | **11** | Outlets | 0 |
|  |  | **Total links** | **8** |

> Cross-sections: **8**

## 📈 Forcing & Data

| Item | Count |
|---|--:|
| Direct inflows | 5 |
| Time series | 2 |

---
<sub>📄 Auto-generated 2026-06-24 • summary of `inlet_capture_test.inp`</sub>
