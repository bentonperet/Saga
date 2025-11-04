**Created:** 2025-10-29
**Updated from:** Pryor_Bod_EVS_Rev01.md

# BASIS OF DESIGN - HVAC
## CSI Division 23
### Pryor Data Center - PACHYDERM GLOBAL

**Parent Document:** [[Saga Pryor DC/Basis of Design/Erik_BOD_Updated/_BOD - Exec Summary and TOC]]

---

## OVERVIEW

Phased mechanical cooling strategy optimized for AI/ML workload growth: **Phase 1 = 3 MW L2C liquid cooling only** (anchor tenant), expanding to 24 MW ultimate capacity (16.8 MW L2C + 7.2 MW RDHx) across 4 phases with **separate warm/cold loop architecture**. Target PUE 1.40 (Phase 1) improving to 1.25 (Phase 4) through warm water cooling efficiency, extended free cooling, and zero water consumption.

**Design Philosophy:**
- **Phase 1 Strategy:** L2C liquid cooling only (no RDHx cooling plant) = lower CAPEX, proves high-density capability
- **Phased deployment:** Cooling capacity matches rack deployment (30 → 150 → 285 → 468 racks)
- **Separate loop architecture:** Loop 3 (warm water, 85°F for L2C) independent from Loops 1+2 (cold water, 60°F for RDHx)
  - **Rationale:** 85°F warm water maximizes L2C efficiency; 60°F required for RDHx air cooling
  - **Load separation:** L2C loads swing violently (GPU workloads), RDHx loads are stable - separate plants prevent control instability
- **N+1 redundancy:** Each cooling plant has N+1 chillers
- **Zero water consumption:** Air-cooled chillers only, closed-loop glycol
- **Total racks at Phase 4:** 168 L2C racks + 288 RDHx racks = 468 racks total

---

## PHASE 1: L2C LIQUID COOLING ONLY (3 MW IT LOAD)

### Strategy

**Anchor Tenant Approach:**
- Focus on single high-density AI training customer
- Proves liquid cooling capability from day 1
- Lower Phase 1 CAPEX (skip RDHx cooling plant entirely = ~$2-3M savings)
- Optimal chiller efficiency (67% utilization in N+1 operation)

### IT Heat Load

**30 racks @ 100 kW each = 3,000 kW IT load**
- Customer: AI cloud provider or enterprise ML team
- Workload: Large-scale GPU training clusters (H100, GB200 NVL72, etc.)
- L2C mandatory for this density

### L2C Cooling Architecture

**L2C (Liquid-to-Chip) cooling uses CDUs to cool 100% of rack heat:**

L2C captures all rack heat via:
- **CDUs (Coolant Distribution Units):** Pump chilled warm water (85°F) to chip-level cold plates on CPUs, GPUs, memory
- **Integrated in-rack cooling:** Each L2C rack is a fully self-contained liquid-cooled unit

**Phase 1 uses 100% L2C racks** - no RDHx racks, no air cooling plant

### Heat Load (Per 100 kW L2C Rack)

| Component | Heat Captured | Method |
|-----------|---------------|--------|
| L2C cold plates (entire server) | 100 kW | CDU warm water (85°F supply) |
| **Total** | **100 kW** | All heat via Loop 3 |

**Phase 1 load:**
- 30 L2C racks × 100 kW = **3,000 kW total Loop 3 load**

### Equipment Per Rack

**L2C Rack Equipment:**
- 1× CDU (100-150 kW capacity, sized for potential future densification)
- Warm water connections: Supply/return from Loop 3 (85°F supply)

**Phase 1 Total:**
- 30× CDUs
- All connected to Loop 3 distribution manifold
- No RDHx units in Phase 1

### Building HVAC (Separate System)

**Phase 1 has NO data center air cooling plant.**

Building services (offices, NOC, support spaces) served by:
- Rooftop package units (RTUs) - standard commercial HVAC
- Separate from IT cooling infrastructure
- ~300-500 kW building load

---

## LOOP 3: L2C WARM WATER CHILLER PLANT (PHASE 1)

### Configuration

**4 × 1,500 kW Air-Cooled Chillers (N+1)**
- **Normal operation:** 3 chillers running (4,500 kW capacity for 3,000 kW load)
- **Utilization:** 67% per operating chiller in N+1 configuration (3,000 kW ÷ 4,500 kW total) ✓
  - Well above 40% minimum efficiency threshold
  - Optimal operating range for part-load efficiency
- **N+1 redundancy:** One chiller fails → 3 remain with 4,500 kW capacity ✓
- **Future-ready:** Can support Phase 2-3 L2C load increase with moderate chiller additions

### Chiller Specifications (Each Unit)

| Parameter | Specification |
|-----------|---------------|
| **Capacity** | 1,500 kW (430 ton) |
| **Type** | Air-cooled screw compressor with integrated free cooling |
| **Supply Temperature** | **29°C (85°F)** - warm water optimized for L2C efficiency |
| **Return Temperature** | 35-38°C (95-100°F) |
| **Refrigerant** | R-134a or R-513A (low-GWP) |
| **COP (Mechanical)** | **5.0-6.5** at design conditions (high COP due to warm water) |
| **COP (Free Cooling)** | 20-35 with waterside economizer |
| **Integrated Pumps** | VFD-controlled |
| **Free Cooling Mode** | Waterside economizer, active below 25°C (77°F) ambient |
| **Controls** | BACnet/IP integration with facility BMS |
| **Enclosure** | Outdoor-rated, sound-attenuated |

**Key Advantage:** 85°F supply temperature enables significantly higher COP (5.0-6.5 vs. 3.8-4.2 for traditional 55°F systems) and extends free cooling hours.

### Free Cooling Operation (Oklahoma Climate)

**With 85°F warm water supply, Oklahoma provides ~5,000-6,000 hours/year of free cooling opportunity** (significantly more than traditional 55°F systems)

**Mode 1: Full Free Cooling (Ambient < 25°C / 77°F)**
- Compressors off, heat rejected via air-cooled coils only
- Significantly improved COP vs. mechanical cooling
- **Season:** October through May (extended free cooling season vs. 55°F systems)
- **Hours/year:** ~5,000-6,000 hours (60-70% of the year)

**Mode 2: Partial Free Cooling (Ambient 25-30°C / 77-86°F)**
- Compressors run at reduced capacity (part-load)
- Blended efficiency mode
- **Season:** Late spring/early fall transition periods

**Mode 3: Full Mechanical Cooling (Ambient > 30°C / 86°F)**
- Compressors run at full capacity
- Still higher efficiency than 55°F systems (higher COP at warm water temperatures)
- **Season:** June through August (peak summer only)

**Annual PUE Impact:**
- Extended free cooling season (5,000+ hours vs. 3,500 for 55°F systems) reduces annual cooling energy by 50-60%
- Target Phase 1 PUE: 1.40 (includes all infrastructure losses)
- 85°F supply enables dramatic PUE improvement vs. traditional 55-60°F L2C systems

### Piping Strategy (Loop 3 Serving L2C CDUs Only)

**Loop 3 serves L2C CDUs in Phase 1 (RDHx added in Phase 2):**

```
Loop 3 Chiller Plant (4× 1,500 kW chillers in parallel)
    ↓
Primary pumps (N+1 configuration)
    ↓
Loop 3 Distribution Header (29°C / 85°F warm water supply)
    ↓
    ├─→ CDU #1 (rack 1, L2C chip cooling) → returns ~35°C / 95°F
    ├─→ CDU #2 (rack 2, L2C chip cooling) → returns ~35°C / 95°F
    ├─→ CDU #3 (rack 3, L2C chip cooling) → returns ~35°C / 95°F
    └─→ [30 L2C racks total, each with CDU]
    ↓
Return header (~35-38°C / 95-100°F mixed return)
    ↓
Back to chillers
```

**Phase 1 Simplified Infrastructure:**
- **One chiller plant** (Loop 3 for L2C only)
- **One fluid makeup system**
- **One chemical treatment program**
- **Warm water (85°F)** maximizes efficiency

**Pumping:**
- **Primary pumps:** Integrated in chiller packages (N+1 configuration, VFD-controlled)
- **Secondary pumps:** Distributed to rack distribution manifolds (N+1 configuration)
- **CDU pumps:** Internal pumps within each CDU unit (circulate fluid through cold plates)
- **Total pumping strategy:** Primary → secondary → CDU internal pumps

**Fluid System:**
- **Fluid:** 25% propylene glycol / water mixture
- **Purpose:** Freeze protection, corrosion inhibition, optimized for L2C warm water cooling
- **Supply temperature:** 29°C (85°F) - warm water optimized for efficiency
- **Return temperature:** 35-38°C (95-100°F) - from L2C CDUs
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

## PHASE 2: OPEN BOTH HALLS + ADD RDHx COOLING (6 MW TOTAL IT LOAD)

### Strategy

**Commission DH-E + RDHx Cooling Plant:**
- Open second data hall (DH-E) for medium-density racks
- Commission Loops 1+2 (cold water, 60°F) for RDHx cooling
- L2C load unchanged at 3 MW (30 racks in DH-W)
- Add 3 MW of RDHx capacity (120 racks in DH-E)

### IT Heat Load Breakdown

**150 racks total = 6,000 kW IT load**
- **L2C cooling (Loop 3):** 30 racks × 100 kW = 3,000 kW (unchanged from Phase 1)
- **RDHx cooling (Loops 1+2):** 120 racks × 25 kW = 3,000 kW (new)

### Loop 3 (L2C) - No Change

**Keep existing 4 × 1,500 kW chillers from Phase 1:**
- L2C load unchanged: 3,000 kW (30 racks)
- No additional L2C equipment in Phase 2

### Loops 1+2 (RDHx) - NEW Commission

**3 × 1,500 kW Air-Cooled Chillers (N+1 for 3 MW RDHx load)**
- **Normal operation:** 2 chillers running (3,000 kW capacity for 3,000 kW load)
- **Utilization:** 100% per operating chiller in N+1 configuration
- **N+1 redundancy:** One chiller fails → 2 remain with 3,000 kW capacity ✓
- **Temperature:** 60°F supply (15.5°C) - required for rear-door air cooling
- **Return temperature:** 68-72°F (20-22°C)

### RDHx Equipment

**120 × RDHx Units (Rear-Door Heat Exchangers)**
- Each RDHx: 25 kW capacity
- Total RDHx capacity: 120 × 25 kW = 3,000 kW
- Rear-door mounted on standard racks
- Cold water from Loops 1+2 cools air exiting rack

---

## PHASE 3: SCALE BOTH COOLING PLANTS (15 MW TOTAL IT LOAD)

### Strategy

**Major Expansion of Both L2C and RDHx:**
- Scale L2C (Loop 3) to 10.5 MW (105 racks total)
- Scale RDHx (Loops 1+2) to 4.5 MW (180 racks total)
- Both data halls active with mixed rack types

### IT Heat Load Breakdown

**285 racks total = 15,000 kW IT load**
- **L2C cooling (Loop 3):** 105 racks × 100 kW = 10,500 kW
- **RDHx cooling (Loops 1+2):** 180 racks × 25 kW = 4,500 kW

### Loop 3 (L2C) Expansion

**Add 5 chillers (9 × 1,500 kW total, N+1 for 10.5 MW)**
- **Normal operation:** 7 chillers running (10,500 kW capacity for 10,500 kW load)
- **Utilization:** 100% per operating chiller in N+1 configuration
- **CDUs:** 105 total units (1 per L2C rack)

### Loops 1+2 (RDHx) Expansion

**Add 1 chiller (4 × 1,500 kW total, N+1 for 4.5 MW)**
- **Normal operation:** 3 chillers running (4,500 kW capacity for 4,500 kW load)
- **Utilization:** 100% per operating chiller in N+1 configuration
- **RDHx units:** 180 total units (1 per RDHx rack)

---

## PHASE 4: FULL BUILD-OUT (24 MW TOTAL IT LOAD)

### Strategy

**Complete Build-Out to 468 Racks:**
- L2C at maximum: 16.8 MW (168 racks)
- RDHx at maximum: 7.2 MW (288 racks)
- Both halls at 234-rack capacity each

### IT Heat Load Breakdown

**468 racks total = 24,000 kW IT load**
- **L2C cooling (Loop 3):** 168 racks × 100 kW = 16,800 kW
- **RDHx cooling (Loops 1+2):** 288 racks × 25 kW = 7,200 kW

### Loop 3 (L2C) Final Build

**Add 5 chillers (14 × 1,500 kW total, N+1 for 16.8 MW)**
- **Normal operation:** 12 chillers running (18,000 kW capacity for 16,800 kW load)
- **Utilization:** 93% per operating chiller in N+1 configuration
- **CDUs:** 168 total units (1 per L2C rack)
- **Temperature:** 85°F supply (29°C) - warm water optimized

### Loops 1+2 (RDHx) Final Build

**Add 2 chillers (6 × 1,500 kW total, N+1 for 7.2 MW)**
- **Normal operation:** 5 chillers running (7,500 kW capacity for 7,200 kW load)
- **Utilization:** 96% per operating chiller in N+1 configuration
- **RDHx units:** 288 total units (1 per RDHx rack)
- **Temperature:** 60°F supply (15.5°C) - cold water for air cooling

---

## COOLING LOOP SEPARATION RATIONALE

**Why Separate Warm/Cold Loops:**
- **Loop 3 (85°F warm water):** Optimized for L2C direct liquid cooling - provides 30-50% better COP than cold water systems
- **Loops 1+2 (60°F cold water):** Required temperature for RDHx rear-door air heat exchangers
- **Efficiency advantage:** 85°F supply enables 5,000-6,000 hours/year of free cooling vs. 3,500-4,000 hours with traditional cold water
- **Load isolation:** Separates stable L2C loads from more volatile RDHx loads for better control stability

---

## CDU DISTRIBUTION (L2C COOLING)

### Phased CDU Deployment

**Ultimate Capacity: 336 CDUs (2 per L2C cabinet, A/B redundancy)**
- Phase 1: 60 CDUs (30 L2C racks in DH-W)
- Phase 2: 60 CDUs (no change to L2C rack count)
- Phase 3: 210 CDUs total (105 L2C racks)
- Phase 4: 336 CDUs total (168 L2C racks)

**CDU Specifications:**
- Each CDU: 300 kW heat rejection capacity
- Primary side: Warm chilled water from Loop 3 (85°F supply)
- Secondary side: Dielectric fluid to CPU/GPU cold plates
- Power: 15 kW each (pumps + controls)

**CDU Location:**
- **Mechanical Gallery (Pipe Gallery)** on north end of building envelope
- NOT located inside data halls
- CDUs housed in dedicated mechanical gallery flanking both data halls
- Secondary dielectric fluid distribution from CDUs to cabinets via overhead manifolds

### CDU Specifications (Each Unit)

| Parameter | Specification |
|-----------|---------------|
| **Capacity** | 300 kW heat rejection |
| **Primary Side** | Warm chilled water from Loop 3 (85°F / 29°C supply) |
| **Secondary Side** | Dielectric fluid to cold plates |
| **Redundancy** | Dual CDUs per cabinet (A-side + B-side) |
| **Controls** | Modbus TCP, BACnet integration |
| **Leak Detection** | Integrated sensors at all connections |

### Cabinet L2C Manifolds

**Distribution from Mechanical Gallery to Data Halls:**
- CDUs located in mechanical gallery (north pipe gallery)
- Secondary dielectric fluid distribution via overhead piping into data halls
- **Quick-disconnect fittings:** Rapid connection/removal at cabinet level without draining system
- **Isolation valves:** Enable cabinet service without system shutdown
- **Leak detection:** Sensors at all connections (integrated with BMS)
- **Overhead distribution:** Dielectric fluid manifolds from pipe gallery to cabinet rows

**Deployment Strategy:**
- Phase 1: Install pipe gallery infrastructure and 60 CDUs for anchor tenant
- Phase 2: L2C rack count unchanged (60 CDUs remain)
- Phase 3: Add 150 CDUs (210 total for 105 L2C racks)
- Phase 4: Add 126 CDUs (336 total for 168 L2C racks)

---

## MECHANICAL EQUIPMENT YARD

### Layout

**Location:** North side of building (opposite electrical yard)
**Area:** ~60,000 SF (sized for ultimate 20 chillers)

**Equipment Arrangement by Phase:**

**Phase 1 (3 MW IT Load):**
- Loop 3: 4 × 1,500 kW chillers (N+1 for L2C)
- Loops 1+2: Not commissioned

**Phase 2 (6 MW IT Load):**
- Loop 3: 4 × 1,500 kW chillers (no change)
- Loops 1+2: 3 × 1,500 kW chillers (N+1 for RDHx)

**Phase 3 (15 MW IT Load):**
- Loop 3: 9 × 1,500 kW chillers total (add 5 units)
- Loops 1+2: 4 × 1,500 kW chillers total (add 1 unit)

**Phase 4 (24 MW IT Load):**
- Loop 3: 14 × 1,500 kW chillers total (add 5 units)
- Loops 1+2: 6 × 1,500 kW chillers total (add 2 units)
- **Total chillers at Phase 4:** 20 units

**Infrastructure:**
- **Elevated Platforms:** All chillers on 1.5-meter (5 ft) structural steel platforms
- **Buffer Tanks:** Integrated with chiller platforms for thermal mass
- **Clearances:** 8-10 ft between chillers for airflow and maintenance access
- **Future expansion:** Yard sized for additional chiller capacity if needed

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

**Phase 1 Target: 1.40**
- IT load: 3,000 kW
- Facility load: ~4,200 kW (includes cooling, power distribution losses, building systems)
- Target PUE: 1.40
- Conservative target for initial operations

**Phase 2 Target: 1.35**
- IT load: 6,000 kW
- Facility load: ~8,100 kW
- Target PUE: 1.35
- Both cooling loops operational

**Phase 3 Target: 1.30**
- IT load: 15,000 kW
- Facility load: ~19,500 kW
- Target PUE: 1.30
- Efficiency improvements from scale and optimization

**Phase 4 Target: 1.25**
- IT load: 24,000 kW
- Facility load: ~30,000 kW
- Target PUE: 1.25 (optimized at scale)
- Improved efficiency from:
  - Loop 3 warm water (85°F) providing 30-50% better COP
  - Extended free cooling hours (5,000-6,000 hours/year)
  - Optimized chiller staging and load balancing

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

### Cooling Plant Equipment by Phase

| Equipment | Phase 1 | Phase 2 | Phase 3 | Phase 4 | Unit Size | Purpose |
|-----------|---------|---------|---------|---------|-----------|---------|
| **Chillers (Loop 3 - L2C)** | 4 | 4 | 9 | 14 | 1,500 kW | Warm water (85°F) for L2C cooling |
| **Chillers (Loops 1+2 - RDHx)** | 0 | 3 | 4 | 6 | 1,500 kW | Cold water (60°F) for RDHx cooling |
| **CDUs (L2C)** | 60 | 60 | 210 | 336 | 300 kW | L2C coolant distribution |
| **RDHx Units** | 0 | 120 | 180 | 288 | 25 kW | Rear-door heat exchangers |
| **Primary Pumps (Loop 3)** | 4 | 4 | 6 | 8 | Varies | Loop 3 circulation (N+1) |
| **Primary Pumps (Loops 1+2)** | 0 | 4 | 4 | 4 | Varies | Loops 1+2 circulation (N+1) |
| **Building RTUs** | 3-4 | 3-4 | 3-4 | 3-4 | Varies | Office/NOC HVAC |

### IT Load Summary by Phase

| Phase | IT MW | Racks | L2C Racks | RDHx Racks | L2C MW | RDHx MW | Facility MW | PUE |
|-------|-------|-------|-----------|------------|--------|---------|-------------|-----|
| **1** | 3 | 30 | 30 | 0 | 3.0 | 0 | 4.2 | 1.40 |
| **2** | 6 | 150 | 30 | 120 | 3.0 | 3.0 | 8.1 | 1.35 |
| **3** | 15 | 285 | 105 | 180 | 10.5 | 4.5 | 19.5 | 1.30 |
| **4** | 24 | 468 | 168 | 288 | 16.8 | 7.2 | 30.0 | 1.25 |


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
