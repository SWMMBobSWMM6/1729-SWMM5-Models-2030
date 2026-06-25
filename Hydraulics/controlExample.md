# 💧 controlExample.inp

![flow units](https://img.shields.io/badge/flow_units-CFS-blue) ![routing](https://img.shields.io/badge/routing-Dynwave-2ea44f) ![infiltration](https://img.shields.io/badge/infiltration-Horton-9cf) ![nodes](https://img.shields.io/badge/nodes-34-informational) ![links](https://img.shields.io/badge/links-33-informational) ![subcatchments](https://img.shields.io/badge/subcatchments-0-informational) ![status](https://img.shields.io/badge/status-clean_run-2ea44f)

> [!TIP]
> Ran clean -- no errors or warnings reported.<br>Continuity error(s): 0.567 %

**Title:** Example of using control rules with a pump.  
**Location:** `Hydraulics/controlExample.inp`

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
| Routing step | 0:00:05 s |

## 🔧 Hydraulics

| Nodes | Count | Links | Count |
|---|--:|---|--:|
| Junctions | 31 | Conduits | 32 |
| Outfalls | 2 | Pumps | 1 |
| Storage | 1 | Orifices | 0 |
| Dividers | 0 | Weirs | 0 |
| **Total nodes** | **34** | Outlets | 0 |
|  |  | **Total links** | **33** |

> Cross-sections: **32**

## 🎛️ Control Rules

Real-time control rules: **2**

## 📈 Forcing & Data

| Item | Count |
|---|--:|
| Direct inflows | 30 |
| Time series | 30 |
| Curves | 2 |

---
<sub>📄 Auto-generated 2026-06-24 • summary of `controlExample.inp`</sub>
