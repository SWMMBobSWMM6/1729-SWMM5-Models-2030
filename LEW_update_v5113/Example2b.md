# 💧 Example2b.inp

![flow units](https://img.shields.io/badge/flow_units-CFS-blue) ![routing](https://img.shields.io/badge/routing-Dynwave-2ea44f) ![infiltration](https://img.shields.io/badge/infiltration-Horton-9cf) ![nodes](https://img.shields.io/badge/nodes-20-informational) ![links](https://img.shields.io/badge/links-18-informational) ![subcatchments](https://img.shields.io/badge/subcatchments-0-informational) ![status](https://img.shields.io/badge/status-20_errors-red)

> [!CAUTION]
> **Run failed** -- 20 fatal error(s) in `Example2b.rpt`.<br>ERROR 205: invalid keyword CROWN_CUTOFF at line 205 of [OPTION] section:; ERROR 207: duplicate ID name 80408 at line 216 of [JUNC] section:

**Title:** Closed Storage Node Example that Pressurizes Closed Storage Node Example that Pressurizes  
**Location:** `LEW_update_v5113/Example2b.inp`

## ⚙️ Configuration

| Setting | Value |
|---|---|
| Flow units | CFS |
| Infiltration | HORTON |
| Flow routing | DYNWAVE |
| Simulation start | 01/01/2002 00:00:00 |
| Simulation end | 01/01/2002 08:00:00 |
| Duration | 8 hr |
| Report step | 00:15:00 |
| Routing step | 0:00:20 s |

## 🔧 Hydraulics

| Nodes | Count | Links | Count |
|---|--:|---|--:|
| Junctions | 16 | Conduits | 18 |
| Outfalls | 2 | Pumps | 0 |
| Storage | 2 | Orifices | 0 |
| Dividers | 0 | Weirs | 0 |
| **Total nodes** | **20** | Outlets | 0 |
|  |  | **Total links** | **18** |

> Cross-sections: **18**

## 📈 Forcing & Data

| Item | Count |
|---|--:|
| Direct inflows | 6 |
| Time series | 3 |

---
<sub>📄 Auto-generated 2026-06-24 • summary of `Example2b.inp`</sub>
