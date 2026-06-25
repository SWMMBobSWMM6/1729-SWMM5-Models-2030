# 💧 usgs_runoff.inp

![flow units](https://img.shields.io/badge/flow_units-LPS-blue) ![routing](https://img.shields.io/badge/routing-Dynwave-2ea44f) ![infiltration](https://img.shields.io/badge/infiltration-Curve__Number-9cf) ![nodes](https://img.shields.io/badge/nodes-6-informational) ![links](https://img.shields.io/badge/links-6-informational) ![subcatchments](https://img.shields.io/badge/subcatchments-4-informational) ![status](https://img.shields.io/badge/status-16_errors-red)

> [!CAUTION]
> **Run failed** -- 16 fatal error(s) in `usgs_runoff.rpt`.<br>ERROR 305: cannot open report file.at line 137 of [LID_USAGE] section:; ERROR 305: cannot open report file.at line 138 of [LID_USAGE] section:

**Title:** Scenario Run :  BASE  
**Location:** `SWMM5_NCIMM/usgs_runoff.inp`

## ⚙️ Configuration

| Setting | Value |
|---|---|
| Flow units | LPS |
| Infiltration | CURVE_NUMBER |
| Flow routing | DYNWAVE |
| Simulation start | 07/15/1977 00:00 |
| Simulation end | 07/16/1977 00:00 |
| Duration | 1 day |
| Report step | 00:10:00 |
| Routing step | 30 s |

## 💧 Hydrology

| Item | Count |
|---|--:|
| Subcatchments | 4 |
| Total area (ha) | 400.00 |
| Raingages | 1 |
| Aquifers | 1 |
| Groundwater links | 4 |
| Snowpacks | 4 |

## 🔧 Hydraulics

| Nodes | Count | Links | Count |
|---|--:|---|--:|
| Junctions | 4 | Conduits | 5 |
| Outfalls | 1 | Pumps | 0 |
| Storage | 1 | Orifices | 0 |
| Dividers | 0 | Weirs | 1 |
| **Total nodes** | **6** | Outlets | 0 |
|  |  | **Total links** | **6** |

> Cross-sections: **6**

## 🎛️ Control Rules

Real-time control rules: **1**

## 🌿 LID Controls

LID control definitions: **4** &nbsp;|&nbsp; Subcatchment deployments: **16**

## ⚗️ Water Quality

Pollutants: **2** &nbsp;|&nbsp; Land uses: **2**

## 📈 Forcing & Data

| Item | Count |
|---|--:|
| Direct inflows | 1 |
| Dry-weather inflows | 1 |
| Time series | 2 |
| Curves | 1 |

---
<sub>📄 Auto-generated 2026-06-24 • summary of `usgs_runoff.inp`</sub>
