**Created:** 2025-10-29
**Updated from:** Pryor_Bod_EVS_Rev01.md

# BASIS OF DESIGN - HVAC
## CSI Division 23
### Pryor Data Center - PACHYDERM GLOBAL

**Parent Document:** [[Saga Pryor DC/Basis of Design/Erik_BOD_Updated/_BOD - Exec Summary and TOC]]

---

## OVERVIEW

Phased mechanical cooling strategy optimized for AI/ML workload growth: **Phase 1 = 3 MW D2C liquid cooling only** (anchor tenant), expanding to 24 MW ultimate capacity across 4 phases with mixed air + D2C cooling. Target PUE 1.35 (Phase 1) improving to 1.20-1.25 (Phase 4) through extended free cooling, efficient equipment, and zero water consumption.

**Design Philosophy:**
- **Phase 1 Strategy:** D2C liquid cooling only (no air cooling plant) = lower CAPEX, proves high-density capability
- **Phased deployment:** Cooling capacity matches customer growth (3 → 6 → 15 → 24 MW)
- **Separate cooling plants:** Loops 1+2 (air cooling) independent from Loop 3 (D2C cooling)
  - **Rationale:** D2C loads swing violently (GPU workloads 0-100% in seconds), air loads are stable - separate plants prevent control instability
- **N+1 redundancy:** Each cooling plant has N+1 chillers
- **Zero water consumption:** Air-cooled chillers only, closed-loop glycol
- **Single fluid loop for D2C:** Same water/glycol mix serves both CDUs and RDHx units

---

## PHASE 1: D2C LIQUID COOLING ONLY (3 MW IT LOAD)

### Strategy

**Anchor Tenant Approach:**
- Focus on single high-density AI training customer (Customer #2 profile)
- Proves liquid cooling capability from day 1
- Lower Phase 1 CAPEX (skip air cooling plant entirely = ~$2-3M savings)
- Better chiller efficiency (44% utilization vs. 27% if mixed)

### IT Heat Load

**30 racks @ 100 kW each = 3,000 kW IT load**
- Customer: AI cloud provider or enterprise ML team
- Workload: Large-scale GPU training clusters (H100, GB200 NVL72, etc.)
- D2C mandatory for this density

### D2C Cooling Architecture

**Critical Understanding: D2C ≠ 100% Heat Capture**

D2C (Direct-to-Chip) liquid cooling captures 70-90% of rack heat via cold plates mounted directly on:
- CPUs
- GPUs
- High-power memory modules

**D2C does NOT cool:**
- Power supplies
- Network cards (NICs)
- Storage drives
- VRMs (voltage regulators)
- Ambient cabinet heat

**Solution: CDU + RDHx Hybrid**

Each rack requires TWO cooling components:
1. **CDU (Coolant Distribution Unit):** Pumps chilled water to chip-level cold plates (70-90% of heat)
2. **RDHx (Rear-Door Heat Exchanger):** Captures residual heat from non-liquid-cooled components (10-30% of heat)

**Both CDU and RDHx connect to the same Loop 3 chiller plant.**

### Heat Load Split (Per 100 kW Rack)

| Component | Heat Captured | Method |
|-----------|---------------|--------|
| D2C cold plates (CPUs, GPUs) | 70-90 kW | CDU chilled water |
| Residual (PSU, NIC, storage) | 10-30 kW | RDHx chilled water |
| **Total** | **100 kW** | Both fed from Loop 3 |

**Typical design assumption: 80% D2C, 20% RDHx**
- Per rack: 80 kW via CDU, 20 kW via RDHx
- 30 racks total: 2,400 kW via CDUs, 600 kW via RDHx = **3,000 kW total Loop 3 load**

### Equipment Per Rack

**Rack Equipment:**
- 1× CDU (100-150 kW capacity, sized for future densification)
- 1× RDHx unit (integrated rear door or standalone, 20-30 kW capacity)
- Chilled water connections: Supply/return to both CDU and RDHx

**Phase 1 Total:**
- 30× CDUs
- 30× RDHx units
- All connected to single Loop 3 distribution manifold

### Building HVAC (Separate System)

**Phase 1 has NO data center air cooling plant.**

Building services (offices, NOC, support spaces) served by:
- Rooftop package units (RTUs) - standard commercial HVAC
- Separate from IT cooling infrastructure
- ~300-500 kW building load

---

## LOOP 3: D2C CHILLER PLANT (PHASE 1)

### Configuration

**4 × 1,500 kW Air-Cooled Chillers (N+1)**
- **Normal operation:** 3 chillers running (4,500 kW capacity for 3,000 kW load)
- **Utilization:** 44% per running chiller (3,000 ÷ 4,500 = 67% plant utilization) ✓
  - Well above 40% minimum efficiency threshold
  - Optimal operating range for part-load efficiency
- **N+1 redundancy:** One chiller fails → 3 remain with 4,500 kW capacity ✓
- **Future-ready:** Can support Phase 2 D2C load increase without adding chillers initially

### Chiller Specifications (Each Unit)

| Parameter | Specification |
|-----------|---------------|
| **Capacity** | 1,500 kW (430 ton) |
| **Type** | Air-cooled screw compressor with integrated free cooling |
| **Supply Temperature** | 12-15°C (54-59°F) for D2C (higher than air cooling) |
| **Return Temperature** | 18-22°C (64-72°F) |
| **Refrigerant** | R-134a or R-513A (low-GWP) |
| **COP (Mechanical)** | 3.8-4.2 at design conditions |
| **COP (Free Cooling)** | 15-25 with waterside economizer |
| **Integrated Pumps** | VFD-controlled |
| **Free Cooling Mode** | Waterside economizer, active below 10°C ambient |
| **Controls** | BACnet/IP integration with facility BMS |
| **Enclosure** | Outdoor-rated, sound-attenuated |

### Free Cooling Operation (Oklahoma Climate)

**Oklahoma provides ~3,500-4,000 hours/year of free cooling opportunity**

**Mode 1: Full Free Cooling (Ambient < 10°C)**
- Compressors off, heat rejected via air-cooled coils only
- Significantly improved COP vs. mechanical cooling
- **Season:** Late October through April (extended free cooling season)

**Mode 2: Partial Free Cooling (Ambient 10-15°C)**
- Compressors run at reduced capacity (part-load)
- Blended efficiency mode
- **Season:** Spring/fall transition periods

**Mode 3: Full Mechanical Cooling (Ambient > 15°C)**
- Compressors run at full capacity
- Standard mechanical cooling efficiency
- **Season:** May through September (peak summer)

**Annual PUE Impact:**
- Extended free cooling season reduces annual cooling energy by 35-40%
- Target Phase 1 PUE: 1.35 (includes all infrastructure losses)

### Piping Strategy (Single Loop 3 Serving CDU + RDHx)

**Single fluid loop serves both CDU and RDHx equipment:**

```
Chiller Plant (4× 1,500 kW chillers in parallel)
    ↓
Primary pumps (N+1 configuration)
    ↓
Loop 3 Distribution Header (12-15°C supply)
    ↓
    ├─→ CDU #1 (rack 1, chip cooling) → returns ~18°C
    ├─→ CDU #2 (rack 2, chip cooling) → returns ~18°C
    ├─→ RDHx #1 (rack 1, residual heat) → returns ~16°C
    ├─→ RDHx #2 (rack 2, residual heat) → returns ~16°C
    └─→ [30 racks total, each with CDU + RDHx]
    ↓
Return header (~18-22°C mixed return)
    ↓
Back to chillers
```

**Why Single Loop Works:**
- **Temperature compatibility:** Both CDUs and RDHx operate with same supply temperature (12-15°C)
- **Pressure compatibility:** Both operate at similar pressure ranges (30-60 PSI typical)
- **Simplified infrastructure:** One chiller plant, one fluid makeup system, one chemical treatment program
- **Load diversity:** Mixing CDU and RDHx loads improves overall plant efficiency

**Pumping:**
- **Primary pumps:** Integrated in chiller packages (N+1 configuration, VFD-controlled)
- **Secondary pumps:** Distributed to rack distribution manifolds (N+1 configuration)
- **CDU pumps:** Internal pumps within each CDU unit (circulate fluid through cold plates)
- **Total pumping strategy:** Primary → secondary → CDU internal pumps

**Fluid System:**
- **Fluid:** 25% propylene glycol / water mixture
- **Purpose:** Freeze protection, corrosion inhibition, compatible with both CDU and RDHx
- **Supply temperature:** 12-15°C (54-59°F) - warmer than air cooling, within GPU/CPU thermal limits
- **Return temperature:** 18-22°C (64-72°F) - mixed return from CDUs and RDHx units
- **Treatment:** pH 7.5-8.5, biocide dosing, filtration to remove particulates
- **Makeup system:** Automatic glycol/water dosing to maintain 25% concentration

**Distribution:**
- **Rack manifolds:** Isolation valves per rack enable maintenance without affecting neighbors
- **Quick-disconnects:** Tool-less connections at each CDU and RDHx for rapid service
- **Flexible hoses:** Between manifold and equipment to accommodate rack repositioning

**Bypass Valves and Temporary Equipment Provisions:**
- **Chiller bypass valves:** Each chiller equipped with isolation and bypass valves for maintenance
- **Quick-connect points:** Camlock fittings at strategic piping locations for temporary chiller connection
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
- D2C cold plates can accept warmer coolant (GPUs tolerate higher temps than air-cooled servers)
- Higher chiller leaving water temp enables improved efficiency
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
| **Primary Side** | Chilled water from Loop 3 (supply/return per design) |
| **Secondary Side** | Dielectric fluid to cold plates |
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
- Infrastructure loads: cooling, power distribution losses, building/lighting
- Target PUE: 1.35

**Phase 2 Target: 1.25 (Air + D2C Cooling)**
- IT load: 12,000 kW
- Infrastructure loads: all cooling loops, power distribution, building systems
- Target PUE: 1.25
- Improved efficiency from Loop 3 warmer supply temperature and free cooling

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
