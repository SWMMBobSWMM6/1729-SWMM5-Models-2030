# 💧 routing_controls_rules.inp

![flow units](https://img.shields.io/badge/flow_units-CFS-blue) ![routing](https://img.shields.io/badge/routing-Dynwave-2ea44f) ![infiltration](https://img.shields.io/badge/infiltration-Horton-9cf) ![nodes](https://img.shields.io/badge/nodes-11-informational) ![links](https://img.shields.io/badge/links-10-informational) ![subcatchments](https://img.shields.io/badge/subcatchments-0-informational) ![status](https://img.shields.io/badge/status-2_errors-red)

> [!CAUTION]
> **Run failed** -- 2 fatal error(s) in `routing_controls_rules.rpt`.<br>ERROR 205: invalid keyword SETTING at line 85 of [CONTROL] section:; ERROR 205: invalid keyword SETTING at line 90 of [CONTROL] section:

**Title:** TEST1 Test CONTROLS/RULES for conduit throttling  
**Location:** `OWA_ROUTING/routing_controls_rules.inp`

## ⚙️ Configuration

| Setting | Value |
|---|---|
| Flow units | CFS |
| Infiltration | HORTON |
| Flow routing | DYNWAVE |
| Simulation start | 02/02/2002 00:00:00 |
| Simulation end | 02/02/2002 05:00:00 |
| Duration | 5 hr |
| Report step | 00:00:30 |
| Routing step | 0:00:05 s |

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

## 🎛️ Control Rules

Real-time control rules: **2**

## 📈 Forcing & Data

| Item | Count |
|---|--:|
| Direct inflows | 1 |
| Time series | 1 |

---
<sub>📄 Auto-generated 2026-06-24 • summary of `routing_controls_rules.inp`</sub>
