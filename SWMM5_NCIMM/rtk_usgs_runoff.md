# 💧 rtk_usgs_runoff.inp

![flow units](https://img.shields.io/badge/flow_units-LPS-blue) ![routing](https://img.shields.io/badge/routing-Dynwave-2ea44f) ![infiltration](https://img.shields.io/badge/infiltration-Green__Ampt-9cf) ![nodes](https://img.shields.io/badge/nodes-5-informational) ![links](https://img.shields.io/badge/links-5-informational) ![subcatchments](https://img.shields.io/badge/subcatchments-4-informational) ![status](https://img.shields.io/badge/status-4_errors-red)

> [!CAUTION]
> **Run failed** -- 4 fatal error(s) in `rtk_usgs_runoff.rpt`.<br>ERROR 235: invalid infiltration parameters at line 76 of [INFIL] section:; ERROR 235: invalid infiltration parameters at line 77 of [INFIL] section:

**Title:** make a change and have it stick  
**Location:** `SWMM5_NCIMM/rtk_usgs_runoff.inp`

## ⚙️ Configuration

| Setting | Value |
|---|---|
| Flow units | LPS |
| Infiltration | GREEN_AMPT |
| Flow routing | DYNWAVE |
| Simulation start | 07/15/1977 00:00:00 |
| Simulation end | 07/17/1977 06:00:00 |
| Duration | 2 days 6 hr |
| Report step | 00:01:00 |
| Routing step | 0:00:10 s |

## 💧 Hydrology

| Item | Count |
|---|--:|
| Subcatchments | 4 |
| Total area (ha) | 4.00 |
| Raingages | 1 |
| Aquifers | 1 |
| Groundwater links | 1 |

## 🔧 Hydraulics

| Nodes | Count | Links | Count |
|---|--:|---|--:|
| Junctions | 3 | Conduits | 4 |
| Outfalls | 1 | Pumps | 0 |
| Storage | 1 | Orifices | 0 |
| Dividers | 0 | Weirs | 1 |
| **Total nodes** | **5** | Outlets | 0 |
|  |  | **Total links** | **5** |

> Cross-sections: **5**

## 🌿 LID Controls

LID control definitions: **1** &nbsp;|&nbsp; Subcatchment deployments: **1**

## ⚗️ Water Quality

Pollutants: **5** &nbsp;|&nbsp; Land uses: **1**

## 📈 Forcing & Data

| Item | Count |
|---|--:|
| Time series | 2 |

---
<sub>📄 Auto-generated 2026-06-24 • summary of `rtk_usgs_runoff.inp`</sub>
