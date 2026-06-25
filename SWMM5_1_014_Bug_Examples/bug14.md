# 💧 bug14.inp

![flow units](https://img.shields.io/badge/flow_units-CFS-blue) ![routing](https://img.shields.io/badge/routing-Kinwave-yellowgreen) ![infiltration](https://img.shields.io/badge/infiltration-Horton-9cf) ![nodes](https://img.shields.io/badge/nodes-0-informational) ![links](https://img.shields.io/badge/links-0-informational) ![subcatchments](https://img.shields.io/badge/subcatchments-0-informational) ![status](https://img.shields.io/badge/status-clean_run-2ea44f)

> [!TIP]
> Ran clean -- no errors or warnings reported.

**Title:** Demonstrates the fix for a v5.1.013 access violation error when a model has LID units but no subcatchments. This file now runs successfully.  
**Location:** `SWMM5_1_014_Bug_Examples/bug14.inp`

## ⚙️ Configuration

| Setting | Value |
|---|---|
| Flow units | CFS |
| Infiltration | HORTON |
| Flow routing | KINWAVE |
| Simulation start | 06/07/2019 00:00:00 |
| Simulation end | 06/07/2019 06:00:00 |
| Duration | 6 hr |
| Report step | 00:15:00 |
| Routing step | 0:00:30 s |

## 🔧 Hydraulics

| Nodes | Count | Links | Count |
|---|--:|---|--:|
| Junctions | 0 | Conduits | 0 |
| Outfalls | 0 | Pumps | 0 |
| Storage | 0 | Orifices | 0 |
| Dividers | 0 | Weirs | 0 |
| **Total nodes** | **0** | Outlets | 0 |
|  |  | **Total links** | **0** |

## 🌿 LID Controls

LID control definitions: **2** &nbsp;|&nbsp; Subcatchment deployments: **0**

---
<sub>📄 Auto-generated 2026-06-24 • summary of `bug14.inp`</sub>
