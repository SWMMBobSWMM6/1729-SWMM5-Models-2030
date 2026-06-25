# 💧 bug20_TS_Date.inp

![flow units](https://img.shields.io/badge/flow_units-CFS-blue) ![routing](https://img.shields.io/badge/routing-Dynwave-2ea44f) ![infiltration](https://img.shields.io/badge/infiltration-Green__Ampt-9cf) ![nodes](https://img.shields.io/badge/nodes-4-informational) ![links](https://img.shields.io/badge/links-3-informational) ![subcatchments](https://img.shields.io/badge/subcatchments-2-informational) ![status](https://img.shields.io/badge/status-2_errors-red)

> [!CAUTION]
> **Run failed** -- 2 fatal error(s) in `bug20_TS_Date.rpt`.<br>ERROR 235: invalid infiltration parameters at line 78 of [INFIL] section:; ERROR 235: invalid infiltration parameters at line 79 of [INFIL] section:

**Title:** Demonstrates the fix for a v5.1.013 bug that produced incorrect rainfall when the same time series was used by one rain gage assigned to a Unit Hydrograph and another assigned to a subcatchment. The results for total RDII volume and total w…  
**Location:** `SWMM5_1_014_Bug_Examples/bug20_TS_Date.inp`

## ⚙️ Configuration

| Setting | Value |
|---|---|
| Flow units | CFS |
| Infiltration | GREEN_AMPT |
| Flow routing | DYNWAVE |
| Simulation start | 06/03/2019 00:00:00 |
| Simulation end | 06/04/2019 06:00:00 |
| Duration | 1 day 6 hr |
| Report step | 00:15:00 |
| Routing step | 0:00:30 s |

## 💧 Hydrology

| Item | Count |
|---|--:|
| Subcatchments | 2 |
| Total area (ac) | 100.00 |
| Raingages | 4 |

## 🔧 Hydraulics

| Nodes | Count | Links | Count |
|---|--:|---|--:|
| Junctions | 3 | Conduits | 3 |
| Outfalls | 1 | Pumps | 0 |
| Storage | 0 | Orifices | 0 |
| Dividers | 0 | Weirs | 0 |
| **Total nodes** | **4** | Outlets | 0 |
|  |  | **Total links** | **3** |

> Cross-sections: **3**

## 📈 Forcing & Data

| Item | Count |
|---|--:|
| Time series | 1 |

---
<sub>📄 Auto-generated 2026-06-24 • summary of `bug20_TS_Date.inp`</sub>
