# 💧 bug19.inp

![flow units](https://img.shields.io/badge/flow_units-CFS-blue) ![routing](https://img.shields.io/badge/routing-Kinwave-yellowgreen) ![infiltration](https://img.shields.io/badge/infiltration-Green__Ampt-9cf) ![nodes](https://img.shields.io/badge/nodes-4-informational) ![links](https://img.shields.io/badge/links-2-informational) ![subcatchments](https://img.shields.io/badge/subcatchments-0-informational) ![status](https://img.shields.io/badge/status-clean_run-2ea44f)

> [!TIP]
> Ran clean -- no errors or warnings reported.<br>Continuity error(s): 0.000 %

**Title:** Demonstrates the fix for a v5.1.013 bug that ignored soil moisture deficit recovery for Green-Ampt exfiltration from storage units. Running this data set shows that for second storm event the storage unit using G-A exfiltration correctly em…  
**Location:** `SWMM5_1_014_Bug_Examples/bug19.inp`

## ⚙️ Configuration

| Setting | Value |
|---|---|
| Flow units | CFS |
| Infiltration | GREEN_AMPT |
| Flow routing | KINWAVE |
| Simulation start | 01/01/2010 00:00:00 |
| Simulation end | 01/28/2010 01:00:00 |
| Duration | 27 days 1 hr |
| Report step | 00:05:00 |
| Routing step | 0:00:30 s |

## 🔧 Hydraulics

| Nodes | Count | Links | Count |
|---|--:|---|--:|
| Junctions | 0 | Conduits | 0 |
| Outfalls | 2 | Pumps | 0 |
| Storage | 2 | Orifices | 0 |
| Dividers | 0 | Weirs | 0 |
| **Total nodes** | **4** | Outlets | 2 |
|  |  | **Total links** | **2** |

## 📈 Forcing & Data

| Item | Count |
|---|--:|
| Direct inflows | 2 |
| Time series | 3 |
| Curves | 2 |

---
<sub>📄 Auto-generated 2026-06-24 • summary of `bug19.inp`</sub>
