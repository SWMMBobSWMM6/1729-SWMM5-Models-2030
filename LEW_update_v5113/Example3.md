# 💧 Example3.inp

![flow units](https://img.shields.io/badge/flow_units-CFS-blue) ![routing](https://img.shields.io/badge/routing-Dynwave-2ea44f) ![infiltration](https://img.shields.io/badge/infiltration-Horton-9cf) ![nodes](https://img.shields.io/badge/nodes-68-informational) ![links](https://img.shields.io/badge/links-66-informational) ![subcatchments](https://img.shields.io/badge/subcatchments-0-informational) ![status](https://img.shields.io/badge/status-68_errors-red)

> [!CAUTION]
> **Run failed** -- 68 fatal error(s) in `Example3.rpt`.<br>ERROR 205: invalid keyword CROWN_CUTOFF at line 343 of [OPTION] section:; ERROR 207: duplicate ID name KRO3001 at line 354 of [JUNC] section:

**Title:** Example 3 Use of Rule-Based Pump Controls and Dry Weather Flow Patterns Example 3 Use of Rule-Based Pump Controls and Dry Weather Flow Patterns  
**Location:** `LEW_update_v5113/Example3.inp`

## ⚙️ Configuration

| Setting | Value |
|---|---|
| Flow units | CFS |
| Infiltration | HORTON |
| Flow routing | DYNWAVE |
| Simulation start | 01/01/2001 00:00:00 |
| Simulation end | 01/02/2001 00:00:00 |
| Duration | 1 day |
| Report step | 00:05:00 |
| Routing step | 0:00:20 s |

## 🔧 Hydraulics

| Nodes | Count | Links | Count |
|---|--:|---|--:|
| Junctions | 62 | Conduits | 64 |
| Outfalls | 4 | Pumps | 2 |
| Storage | 2 | Orifices | 0 |
| Dividers | 0 | Weirs | 0 |
| **Total nodes** | **68** | Outlets | 0 |
|  |  | **Total links** | **66** |

> Cross-sections: **64**

## 🎛️ Control Rules

Real-time control rules: **4**

## 📈 Forcing & Data

| Item | Count |
|---|--:|
| Dry-weather inflows | 60 |
| Curves | 1 |

---
<sub>📄 Auto-generated 2026-06-24 • summary of `Example3.inp`</sub>
