**Created:** 2025-10-29
**Updated from:** Pryor_Bod_EVS_Rev01.md

# BASIS OF DESIGN - HVAC
## CSI Division 23
### Pryor Data Center - PACHYDERM GLOBAL

**Parent Document:** [[_BOD - Exec Summary and TOC]]

---

## OVERVIEW

Phased mechanical cooling strategy supporting 3 MW Phase 1 (air cooling only) expandable to 12 MW Phase 2 (air + direct-to-chip cooling). Target PUE 1.35 (Phase 1) and 1.25 (Phase 2) through extended free cooling, efficient equipment, and zero water consumption.

**Design Philosophy:**
- **Phased deployment:** Cooling capacity matches IT load growth
- **Separate cooling plants:** Loops 1+2 (air cooling) independent from Loop 3 (D2C cooling)
- **N+1 redundancy:** Each cooling plant has N+1 chillers
- **N+N air cooling:** Dual loops (1+2) each capable of full 3,000 kW air cooling load
- **Zero water consumption:** Air-cooled chillers, closed-loop glycol

---

## PHASE 1: AIR COOLING ONLY (3 MW IT LOAD)

### IT Heat Load

**30 cabinets @ 100 kW each = 3,000 kW IT load**

### Cabinet Integrated Cooling

**DDC S-Series Cabinets with Integrated 100 kW FCUs:**
- **30 cabinets total**
- Each cabinet contains:
  - **Dual coils:** 50 kW capacity each
    - Coil #1 → connected to Loop 1
    - Coil #2 → connected to Loop 2
  - **Dual fans:** Component-level redundancy
  - Total FCU capacity: 100 kW per cabinet
- **Normal operation:** Both coils run in parallel (50 kW + 50 kW = 100 kW)
- **N operation:** Either loop provides full 100 kW to cabinet

**Total cooling capacity:**
- Loop 1 load: 30 cabinets × 50 kW = 1,500 kW
- Loop 2 load: 30 cabinets × 50 kW = 1,500 kW
- **Combined: 3,000 kW** ✓

### Redundancy Test (N+N)

**Normal operation:**
- Both loops carry 1,500 kW each
- 3,000 kW total cooling matches 3,000 kW IT load ✓

**N operation (Loop 1 failure):**
- Loop 2 carries full 3,000 kW
- All 30 cabinets receive 100 kW cooling from Loop 2 coils only
- **Zero IT impact** ✓

**This is true N+N redundancy at the cabinet level.**


---

## LOOPS 1+2 SHARED CHILLER PLANT

### Configuration

**4 × 1,500 kW Air-Cooled Chillers (N+1)**
- **Normal operation:** 3 chillers running (4,500 kW capacity for 3,000 kW load)
- **Utilization:** 67% (optimal efficiency range)
- **N+1 redundancy:** One chiller fails → 3 remain with 4,500 kW capacity ✓
- **Either loop can draw full 3,000 kW** during N operation

### Chiller Specifications (Each Unit)

| Parameter | Specification |
|-----------|---------------|
| **Capacity** | 1,500 kW (430 ton) |
| **Type** | Air-cooled screw compressor with integrated free cooling |
| **Supply Temperature** | 7-10°C (45-50°F) |
| **Return Temperature** | 15-18°C (59-64°F) |
| **Refrigerant** | R-134a or R-513A (low-GWP) |
| **COP (Mechanical)** | 3.8-4.2 at design conditions |
| **COP (Free Cooling)** | 15-25 when ambient < 10°C |
| **Power Consumption** | ~395 kW at full mechanical cooling load |
| **Integrated Pumps** | VFD-controlled, 30 HP (22 kW) each |
| **Free Cooling Mode** | Waterside economizer, active below 10°C ambient |
| **Controls** | BACnet/IP integration with facility BMS |
| **Enclosure** | Outdoor-rated, sound-attenuated |

### Free Cooling Operation (Oklahoma Climate)

**Oklahoma provides ~3,500-4,000 hours/year of free cooling opportunity**

**Mode 1: Full Free Cooling (Ambient < 10°C)**
- Compressors off, heat rejected via air-cooled coils only
- COP: 15-25 (vs. 3.8-4.2 mechanical)
- Power: ~30 kW (pumps + fans only, no compressor load)
- **Season:** Late October through April (~215 days/year)

**Mode 2: Partial Free Cooling (Ambient 10-15°C)**
- Compressors run at reduced capacity (part-load)
- COP: 6-10 (blended)
- **Season:** Spring/fall transition periods

**Mode 3: Full Mechanical Cooling (Ambient > 15°C)**
- Compressors run at full capacity
- COP: 3.8-4.2
- **Season:** May through September (peak summer)

**Annual PUE Impact:**
- Extended free cooling season reduces annual cooling energy by 35-40%
- Target Phase 1 PUE: 1.35 (includes all infrastructure losses)

### Piping Strategy (Shared Plant, Dual Distribution)

**Shared chiller plant with dual distribution headers:**
- **Primary loop:** Constant flow through chillers (4 chillers in parallel)
- **Header A → Loop 1 distribution** (feeds 30 cabinets, Coil #1)
- **Header B → Loop 2 distribution** (feeds 30 cabinets, Coil #2)
- **Isolation valves:** Enable maintenance on one loop while other operates
- **Cross-tie valves:** Allow full plant capacity to serve either loop during N operation

**Pumping:**
- **Primary pumps:** 4 × 22 kW (integrated in chiller packages, 3 running + 1 standby)
- **Secondary pumps:** 4 × 22 kW (distributed to cabinet headers, 3 running + 1 standby)
- **VFD control:** Variable speed on all pumps for energy optimization

**Glycol System:**
- **Fluid:** 25% propylene glycol / water mixture
- **Purpose:** Freeze protection, corrosion inhibition
- **Treatment:** pH 7.5-8.5, biocide dosing

**Bypass Valves and Temporary Equipment Provisions:**
- **Chiller bypass valves:** Each chiller equipped with isolation and bypass valves for maintenance
- **Quick-connect points:** Camlock or similar fittings at strategic piping locations for temporary chiller connection
- **Purpose:** Support rental/backup chillers during maintenance or emergency situations
- **Sizing:** Quick-connects sized for standard rental chiller capacities (300-1,500 kW range)
- **Access:** Connection points accessible from equipment yard with cable pass-through provisions in building envelope
- **Documentation:** As-built drawings showing all connection points and rental equipment compatibility specifications

---

## PHASE 2: ADD DIRECT-TO-CHIP COOLING (12 MW TOTAL IT LOAD)

### IT Heat Load Breakdown

**30 cabinets @ 400 kW each = 12,000 kW IT load**
- **Air cooling portion:** 100 kW per cabinet × 30 = 3,000 kW (unchanged from Phase 1)
- **D2C cooling portion:** 300 kW per cabinet × 30 = 9,000 kW (new)

### Air Cooling (Loops 1+2) - No Change

**Same 4 × 1,500 kW chillers from Phase 1:**
- Load remains 3,000 kW (air portion unchanged)
- Chillers now operate at higher utilization (3,000 kW load vs. 4,500 kW capacity = 67%)
- **No additional air cooling equipment required**

---

## LOOP 3: DIRECT-TO-CHIP COOLING PLANT (INDEPENDENT)

### Configuration

**8 × 1,500 kW Air-Cooled Chillers (N+1 with Margin)**
- **Normal operation:** 6 chillers running (9,000 kW capacity for 9,000 kW load)
- **Utilization:** 100% at peak (design point)
- **N+1 redundancy:** One chiller fails → 7 remain with 10,500 kW capacity (17% margin) ✓
- **Alternative operation:** Run 7 chillers normally (10,500 kW capacity, 17% margin)

### Why Independent Loop 3 (Not Shared with Loops 1+2)

**Air Cooling (Loops 1+2) Load Profile:**
- Predictable, stable loads
- Diurnal patterns (±10% variation day-to-night)
- Traditional HVAC control strategies work well
- Load changes: minutes to hours

**D2C Cooling (Loop 3) Load Profile:**
- **Violent load swings:** 0-100% in seconds as GPU jobs launch
- **Unpredictable:** AI/ML batch jobs start/stop without warning
- **Requires aggressive control tuning:** Fast-acting VFDs, buffer tanks

**Problems if Mixed on Shared Plant:**
- **Control hunting:** Rapid D2C swings cause chiller staging instability
- **Reduced efficiency:** Frequent load cycling reduces COP
- **Accelerated wear:** Compressors and valves cycle excessively
- **Complicated troubleshooting:** Which loop caused the upset? Air or D2C?

**Benefits of Separation:**
- **Optimized controls:** Tune Loop 3 for fast response, Loops 1+2 for stability
- **Clear contractor boundaries:** Traditional HVAC contractor (Loops 1+2) vs. liquid cooling specialist (Loop 3)
- **Independent maintenance:** Service Loop 3 without impacting air cooling
- **Fault isolation:** Loop 3 failure doesn't cascade to air cooling (and vice versa)

### Loop 3 Chiller Specifications

**Same 1,500 kW air-cooled chillers, but optimized for D2C:**
- **Supply temperature:** 25°C (77°F) - warmer than air cooling for efficiency
- **Return temperature:** 30-35°C (86-95°F)
- **ΔT:** 5-10°C (enables higher COP)
- **COP:** 5.0-5.5 (better than air cooling due to elevated supply temp)
- **Power consumption:** ~273 kW at full load (vs. 395 kW for colder air cooling)

**Why warmer supply temp:**
- D2C cold plates can accept 25-30°C coolant (GPUs tolerate higher temps than air-cooled servers)
- Higher chiller leaving water temp = higher COP = lower energy consumption
- **Phase 2 PUE improvement:** Loop 3 efficiency gain contributes to target PUE 1.25

---

## CDU DISTRIBUTION (COOLANT DISTRIBUTION UNITS)

### Configuration

**60 × CDU Units (2 per cabinet, A/B redundancy)**
- Each CDU: 300 kW capacity
- Total CDU capacity: 60 × 300 = 18,000 kW (2× redundancy for 9,000 kW D2C load) ✓
- CDU power: 15 kW each (pumps + controls) × 60 = 900 kW total

**CDU Location:**
- **Mechanical Gallery (Pipe Gallery)** on north end of building envelope
- NOT located inside data halls
- CDUs housed in dedicated mechanical gallery flanking both data halls
- Secondary fluid distribution from CDUs to cabinets via overhead manifolds

### CDU Specifications (Each Unit)

| Parameter | Specification |
|-----------|---------------|
| **Capacity** | 300 kW heat rejection |
| **Primary Side** | Chilled water from Loop 3 (25°C supply, 30-35°C return) |
| **Secondary Side** | Dielectric fluid to cold plates (30-40°C) |
| **Flow Rate** | [ROM] 60-80 GPM |
| **Pressure Drop** | [ROM] 15-25 psi |
| **Power** | 15 kW (pumps + controls + monitoring) |
| **Redundancy** | Dual CDUs per cabinet (A-side + B-side) |
| **Controls** | Modbus TCP, BACnet integration |
| **Leak Detection** | Integrated sensors at all connections |

### Cabinet D2C Manifolds

**Distribution from Mechanical Gallery to Data Halls:**
- CDUs located in mechanical gallery (north pipe gallery)
- Secondary dielectric fluid distribution via overhead piping into data halls
- **Quick-disconnect fittings:** Rapid connection/removal at cabinet level without draining system
- **Isolation valves:** Enable cabinet service without system shutdown
- **Leak detection:** Sensors at all connections (integrated with BMS)
- **Overhead distribution:** Dielectric fluid manifolds from pipe gallery to cabinet rows

**Deployment Strategy:**
- Phase 1: Install pipe gallery infrastructure and CDU rough-in (capped)
- Phase 2: Install CDUs in mechanical gallery, commission D2C cooling cabinet-by-cabinet
- **Zero downtime:** Air cooling continues during D2C commissioning

---

## MECHANICAL EQUIPMENT YARD

### Layout

**Location:** North side of building (opposite electrical yard)
**Area:** ~50,000 SF (sized for all 12 chillers)

**Equipment Arrangement:**
- **Loops 1+2 Zone:** 4 × 1,500 kW chillers (Phase 1)
- **Loop 3 Zone:** 8 × 1,500 kW chillers (Phase 2)
- **Elevated Platforms:** All chillers on 1.5-meter (5 ft) structural steel platforms
- **Buffer Tanks:** Integrated with chiller platforms for thermal mass
- **Clearances:** 8-10 ft between chillers for airflow and maintenance access

**No Pump Rooms Required:**
- All pumps integrated within packaged chiller systems
- VFDs and controls factory-installed
- Eliminates separate pump room construction

**Enclosure:**
- Solid CMU walls (12-15 ft height) with exterior trellis and vine plantings ("green wall")
- Security, noise attenuation, visual screening
- Gated access for maintenance and equipment delivery

---

## BUILDING HVAC (NON-CRITICAL)

### White Space Environmental Control

**Purpose:** Maintain positive pressure, humidity control, and air quality in data halls

**Pressurization System:**
- **Type:** Dedicated DOAS (Dedicated Outdoor Air System)
- **Capacity:** [ROM] 10,000-15,000 CFM per data hall
- **Pressure Target:** +0.02-0.05 in. w.g. relative to adjacent spaces
- **Why:** Prevents dust/contaminant infiltration, maintains ASHRAE A1 environment
- **Redundancy:** N+1 units (2 × 100% capacity per data hall)

**Humidity Control:**
- **Target:** 40-60% RH (ASHRAE allowable: 20-80% RH)
- **Dehumidification:** Integrated in DOAS units (cooling coil + reheat)
- **Humidification:** Steam injection humidifiers (redundant units)
- **Monitoring:** Continuous RH sensors (min 4 per data hall), BMS alarming

**Air Filtration:**
- **Pre-filters:** MERV 8 (removes large particulate)
- **Final filters:** MERV 13 (removes fine dust, meets ASHRAE 52.2)
- **Filter monitoring:** Differential pressure sensors, scheduled replacement

**DOAS Specifications:**
- **Supply air temp:** 18-20°C (tempered, not for primary cooling)
- **Outdoor air:** 100% OA (no recirculation)
- **Energy recovery:** Enthalpy wheel (recovers cooling/heating energy)
- **Controls:** BACnet/IP to BMS, modulating dampers for pressure control
- **Location:** Rooftop-mounted, ducted to data halls via overhead distribution

**Why Separate from IT Cooling:**
- Cabinet FCUs provide 100% of IT heat removal (closed-loop chilled water)
- DOAS only maintains environment (pressure, humidity, air quality)
- If DOAS fails, cabinet cooling continues without interruption

### Common Area Comfort HVAC

**Rooftop Air Handling Units (RTUs):**

**Purpose:** Comfort cooling and ventilation for support spaces

**Equipment:**
- **Quantity:** [ROM] 3-4 RTU units
- **Capacity:** Sized for office/NOC/support space loads (~300-400 kW total)
- **Supply:** Conditioned air for temperature and humidity control
- **Zones:** Office areas, conference rooms, break rooms, corridors, restrooms

### NOC Precision Cooling

**Purpose:** 24/7 temperature control for Network Operations Center

**Equipment:**
- **Type:** Precision CRAC or mini-split systems
- **Capacity:** [ROM] 50 kW
- **Redundancy:** N+1 (dual units)
- **Supply temp:** 20-22°C (68-72°F) for operator comfort

### PDM/Electrical Room Cooling

**Purpose:** Climate control for prefabricated power delivery modules

**Equipment:**
- **Type:** Integrated HVAC within PDM containers (factory-installed)
- **Capacity:** [ROM] 50-75 kW per PDM
- **Setpoint:** 25°C ±2°C (maintains UPS/switchboard optimal operating temp)

---

## MECHANICAL CODES AND STANDARDS

- **IMC 2021** (International Mechanical Code), Oklahoma amendments
- **ASHRAE 90.1-2019** (Energy Standard for Buildings)
- **ASHRAE 62.1** (Ventilation for Acceptable Indoor Air Quality)
- **ASHRAE TC 9.9** (Mission Critical Facilities)
- **ASHRAE Thermal Guidelines** for Data Processing Environments (Class A1)
- **NFPA 90A** (Installation of Air-Conditioning and Ventilating Systems)

---

## TARGET PERFORMANCE METRICS

### PUE (Power Usage Effectiveness)

**Phase 1 Target: 1.35 (Air Cooling)**
- IT load: 3,000 kW
- Cooling: ~650 kW (chillers + pumps + fans)
- Power distribution losses: ~200 kW (transformers, UPS, cable)
- Building/lighting: ~200 kW
- Total facility: 4,050 kW
- PUE = 4,050 / 3,000 = **1.35** ✓

**Phase 2 Target: 1.25 (Air + D2C Cooling)**
- IT load: 12,000 kW
- Cooling: ~2,200 kW (all loops, improved efficiency from Loop 3)
- Power distribution losses: ~800 kW
- Building/lighting: ~200 kW
- Total facility: 15,200 kW
- PUE = 15,200 / 12,000 = **1.27** (target 1.25) ✓

### WUE (Water Usage Effectiveness)

**Target: <0.5 L/kWh**
- **Air-cooled chillers:** Zero water consumption (no evaporative cooling)
- **Closed-loop glycol:** No makeup water required (only initial fill)
- **Domestic water only:** Restrooms, kitchen, landscaping (~500-1,000 gal/day)

**Why This Matters:**
- Water scarcity concerns in many regions
- ESG reporting increasingly focuses on water consumption
- Air-cooled systems eliminate cooling tower water treatment and blowdown costs

---

## EQUIPMENT SUMMARY

| Equipment | Phase 1 | Phase 2 Add | Total | Unit Size | Purpose |
|-----------|---------|-------------|-------|-----------|---------|
| **Chillers (Loops 1+2)** | 4 | 0 | 4 | 1,500 kW | Air cooling |
| **Chillers (Loop 3)** | 0 | 8 | 8 | 1,500 kW | D2C cooling |
| **Cabinet FCUs** | 30 | 0 | 30 | 100 kW | In-cabinet air cooling |
| **CDUs** | 0 | 60 | 60 | 300 kW | D2C coolant distribution |
| **Primary Pumps (Loops 1+2)** | 4 | 0 | 4 | 22 kW | Chiller loop circulation |
| **Secondary Pumps (Loops 1+2)** | 4 | 0 | 4 | 22 kW | Cabinet distribution |
| **Primary Pumps (Loop 3)** | 0 | 4 | 4 | 56 kW | Loop 3 circulation |
| **Building RTUs** | 3-4 | 0 | 3-4 | Varies | Office/NOC HVAC |


---

**Tags:** #pryor-dc #hvac #csi-div-23 #air-cooling #direct-to-chip #free-cooling #zero-water

**Next Steps:**
1. Chiller vendor selection and performance verification
2. CDU specification and integration testing
3. Glycol system design and chemical treatment plan
4. BMS programming for chiller rotation and free cooling optimization
5. Mechanical yard layout and crane access planning

---

**Document Control:**
- **Source:** Pryor_Bod_EVS_Rev01.md
- **Date Updated:** October 29, 2025
- **Prepared by:** EVS / PGCIS Team
