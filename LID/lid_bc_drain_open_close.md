# 💧 lid_bc_drain_open_close.inp

![flow units](https://img.shields.io/badge/flow_units-CFS-blue) ![routing](https://img.shields.io/badge/routing-Dynwave-2ea44f) ![infiltration](https://img.shields.io/badge/infiltration-Horton-9cf) ![nodes](https://img.shields.io/badge/nodes-1-informational) ![links](https://img.shields.io/badge/links-0-informational) ![subcatchments](https://img.shields.io/badge/subcatchments-2-informational) ![status](https://img.shields.io/badge/status-2_errors-red)

> [!CAUTION]
> **Run failed** -- 2 fatal error(s) in `lid_bc_drain_open_close.rpt`.<br>ERROR 185: invalid parameter value for LID; ERROR 185: invalid parameter value for LID %s..

**Title:** Test BC with DRAIN open/close level control (not tested) A simple groundwater example.  
**Location:** `LID/lid_bc_drain_open_close.inp`

## ⚙️ Configuration

| Setting | Value |
|---|---|
| Flow units | CFS |
| Infiltration | HORTON |
| Flow routing | DYNWAVE |
| Simulation start | 09/13/2014 00:00:00 |
| Simulation end | 09/15/2014 00:00:00 |
| Duration | 2 days |
| Report step | 01:00:00 |
| Routing step | 0:00:30 s |

## 💧 Hydrology

| Item | Count |
|---|--:|
| Subcatchments | 2 |
| Total area (ac) | 10.00 |
| Raingages | 1 |

## 🔧 Hydraulics

| Nodes | Count | Links | Count |
|---|--:|---|--:|
| Junctions | 0 | Conduits | 0 |
| Outfalls | 1 | Pumps | 0 |
| Storage | 0 | Orifices | 0 |
| Dividers | 0 | Weirs | 0 |
| **Total nodes** | **1** | Outlets | 0 |
|  |  | **Total links** | **0** |

## 🌿 LID Controls

LID control definitions: **1** &nbsp;|&nbsp; Subcatchment deployments: **1**

## 📈 Forcing & Data

| Item | Count |
|---|--:|
| Time series | 1 |

---
<sub>📄 Auto-generated 2026-06-24 • summary of `lid_bc_drain_open_close.inp`</sub>
