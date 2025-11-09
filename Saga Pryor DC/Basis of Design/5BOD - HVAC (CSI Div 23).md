

# BASIS OF DESIGN - HVAC
## CSI Division 23
### Pryor Data Center - PACHYDERM GLOBAL

**Parent Document:** [[Saga Pryor DC/Basis of Design/Erik_BOD_Updated/_BOD - Exec Summary and TOC]]  

---

## OVERVIEW

This document defines the phased mechanical cooling strategy for a 24 MW IT (~38.4 MW facility) data center deployed in 6MW blocks. The design is optimized for AI/ML workloads and supports both liquid cooling and traditional air-cooled solutions.

The facility supports advanced cooling technologies including a 3-loop architecture with warm-water L2C (Liquid-to-Chip) and cold-water RDHx (Rear-Door Heat Exchanger) capabilities. **Note:** Specific cooling deployment is client-dependent and excluded from this basis of design.

**Design Philosophy:**
- **Block Deployment:** Cooling infrastructure sized per 6MW IT block (~7MW cooling load per block @ 1.6 PUE)
- **3-Loop Architecture:** Facility supports independent warm water (85°F) and cold water (60°F) cooling loops
  - **Loop 3 (L2C):** 85°F warm water maximizes chiller efficiency and free cooling hours
  - **Loops 1+2 (RDHx):** 60°F cold water enables rear-door heat exchangers
- **Redundancy:** N+1 for all chillers and distribution equipment
- **Zero Water Consumption:** All air-cooled chillers, closed-loop glycol systems, zero evaporative cooling
- **Target PUE:** 1.4 average (electrical sizing at 1.6 PUE for Oklahoma heat conditions)

---

## COOLING LOAD PHASING

### Load Summary by Phase

| Phase | IT MW | Design PUE | Facility MW | Cooling Load per Block |
| ----- | ----- | ---------- | ----------- | ---------------------- |
| **1** | 6     | 1.6        | 9.6         | ~7 MW                  |
| **2** | 12    | 1.6        | 19.2        | ~7 MW                  |
| **3** | 18    | 1.6        | 28.8        | ~7 MW                  |
| **4** | 24    | 1.6        | 38.4        | ~7 MW                  |

**Note:** Each 6MW IT block requires approximately 7MW of cooling capacity (accounts for UPS losses, mechanical loads, and environmental overhead).

### Mechanical Plant Phasing

Cooling plant deployed per 6MW block:
- **Chillers:** N+1 configuration sized for ~7MW cooling load per block
- **Estimated:** 3-4 chillers per block (vendor-dependent sizing)
- **Phase 4:** 12-16 chillers total across 4 blocks
- **Free Cooling:** 85°F warm water loop enables ~3,500-4,000 hours/year of economization in Oklahoma climate

**Client-Specific:** Final cooling distribution (L2C vs RDHx vs air-cooled) determined by tenant requirements. Facility infrastructure supports all approaches.

---

## LOOP 3: WARM WATER L2C PLANT

**Facility supports advanced liquid-to-chip (L2C) cooling for high-density AI/ML workloads.**

### L2C Chiller Plant

- **Supply Temperature:** **85°F (29°C)** warm water
- **Efficiency Advantage:** 85°F supply maximizes chiller COP and enables ~3,500-4,000 hours/year free cooling in Oklahoma
- **Fluid:** 25% Propylene Glycol / Water Mixture
- **Configuration:** N+1 air-cooled chiller plant with variable primary flow (VPF)
- **Sizing:** Deployed per 6MW block requirements

### L2C Distribution Concept

**3-Loop Architecture:**
- **Primary Loop:** Facility glycol/water from chillers to CDU heat exchangers
- **Secondary Loop:** Dielectric fluid from CDU to rack cold plates
- **Tertiary Loop:** Cold plate micro-channels for component-level cooling
- **Separation:** Loops isolated via heat exchangers (prevents cross-contamination)

**Key Benefits:**
- Supports 100+ kW/rack densities for GPU clusters
- Significantly improved PUE vs air cooling (1.2-1.3 achievable)
- Reduced data hall HVAC loads
- Extended free cooling season with warm water

**Note:** Detailed L2C specifications (CDUs, cold plates, secondary piping, commissioning) are client-specific and determined during tenant build-out. Facility provides primary infrastructure to support L2C deployment.

## LOOPS 1+2: COLD WATER RDHx PLANT

**Facility supports rear-door heat exchanger (RDHx) cooling for medium-density workloads.**

### RDHx Chiller Plant

- **Supply Temperature:** **60°F (15.5°C)** cold water
- **Rationale:** Colder water required for effective rear-door air-to-water cooling
- **Fluid:** 25% Propylene Glycol / Water Mixture
- **Configuration:** N+1 air-cooled chiller plant with variable primary flow (VPF)
- **Sizing:** Deployed per facility cooling requirements

### RDHx Distribution Concept

- **Distribution:** Cold water piped via overhead manifolds to rack-mounted heat exchangers
- **Typical Density:** Supports 25-40 kW/rack for traditional enterprise and AI inference workloads
- **Installation:** RDHx units mounted on rear door of standard racks

**Note:** RDHx deployment and specifications are client-specific and determined during tenant build-out.

---

## CHILLER & FREE COOLING SPECIFICATIONS

### General Chiller Specifications

- **Type:** Air-cooled screw or scroll compressors with integrated VFDs and free-cooling (waterside economizer) coils.
- **Refrigerant:** Shall be a **Low-GWP (Global Warming Potential) fluid** compliant with all current and anticipated EPA/AIM Act regulations.
- **Controls:** BACnet/IP integration with facility BMS for staging, rotation, and free-cooling optimization.

### Free Cooling Operation

- **L2C Loop (85°F):** The warm-water loop allows for an extended free-cooling season. The BMS shall optimize for waterside economization when ambient conditions permit.
- **RDHx Loop (60°F):** Free cooling shall be utilized when ambient conditions permit.
- **Estimated Hours:** The 85°F loop is projected to provide ~3,500-4,000 hours/year of full or partial free cooling in the Pryor, OK climate.

---

## DATA HALL ENVIRONMENTAL CONTROL (HVAC)

The L2C and RDHx systems handle 100% of the IT heat load. A separate HVAC system is required to manage the data hall environment (air quality, humidity, pressurization).

### DOAS (Dedicated Outdoor Air System)

- **Purpose:** To provide ventilation, humidity control, and positive pressurization to the data halls, per ASHRAE TC 9.9 guidelines.
- **Type:** Dedicated 100% outdoor air units with energy recovery (enthalpy wheel).
- **Redundancy:** N+1 DOAS units shall be provided for each data hall.
- **Pressurization:** System shall maintain a positive pressure to prevent dust/contaminant infiltration.
- **Filtration:** System shall provide air filtration compliant with ASHRAE TC 9.9 for a Class A1 data center.
- **Humidity Control:**
  - **Target:** 40-60% RH
  - **Humidification:** Steam injection humidifiers
  - **Dehumidification:** Integrated cooling coil + reheat in DOAS units

### Support Space HVAC

- **Offices, NOC, Support:** Standard rooftop package units (RTUs) will provide comfort cooling and ventilation.
- **Electrical/PDM Rooms:** Integrated, redundant HVAC units (factory-installed) will maintain the optimal operating temperature for UPS and switchgear.

---

## CHILLED WATER PIPING & DISTRIBUTION

This section defines the complete chilled water infrastructure for all three cooling loops (Loops 1, 2, and 3). **Note:** All chilled water piping and glycol systems are Division 23 (HVAC) scope per industry standard practice.

### Primary Loop Piping

**Loop 3 (L2C - 85°F Warm Water):**
- **Route:** From chillers → mechanical gallery → data hall overhead distribution → CDU connections
- **Pipe Size:** 6" - 12" steel pipe (sized per flow requirements, final sizing in detailed design)
- **Material:** Schedule 40 carbon steel with welded joints (preferred) or grooved fittings
- **Insulation:** 2" closed-cell elastomeric insulation with vapor barrier (prevent condensation)
- **Isolation:** Ball valves at each major equipment connection for concurrent maintainability
- **Hangers/Supports:** Engineered hangers designed for seismic loads per IBC 2021
- **Expansion Compensation:** Expansion loops or flexible connectors at appropriate intervals

**Loops 1+2 (RDHx - 60°F Cold Water):**
- **Route:** From chillers → mechanical gallery → data hall overhead distribution → RDHx connections
- **Pipe Size:** 4" - 8" steel pipe (sized per flow requirements)
- **Material & Details:** Same specifications as Loop 3

### Secondary Loop Piping (L2C Only)

**CDU to Rack Cold Plates:**
- **Fluid:** Dielectric fluid or facility-safe coolant (specified by CDU manufacturer)
- **Route:** From CDU heat exchanger → overhead manifolds → quick-disconnect drops to rack cold plates
- **Pipe Size:** 1" - 2" (per CDU manufacturer specifications)
- **Material:** Stainless steel or approved dielectric-compatible tubing
- **Pressure Rating:** Designed for 150+ psi operating pressure
- **Leak Detection:** Integrated at all connections (see Leak Detection section)

### Overhead Manifolds & Quick-Disconnects

**Data Hall Distribution Manifolds:**
- **L2C Manifolds (DH-W):** Overhead pipe manifolds with 162 quick-disconnect drop points (one per L2C rack)
- **RDHx Manifolds (DH-E):** Overhead pipe manifolds with 232 quick-disconnect drop points (one per RDHx rack)
- **Quick-Disconnects:** Dry-break couplings with automatic shutoff on both sides (prevent spillage during rack maintenance)
- **Labeling:** All connections clearly labeled with zone and rack identification
- **Accessibility:** Maintained clearances for overhead access (coordinate with cable tray routing)

### Piping Accessories

**Expansion Tanks:**
- One expansion tank per loop (3 total)
- Sized for thermal expansion of glycol/water mixture
- Bladder-type or diaphragm-type (preferred over open tanks)
- Mounted at high point with isolation valves

**Air/Dirt Separators:**
- One air separator per loop (removes entrained air)
- One dirt separator per loop (removes particulates)
- Side-stream filtration with replaceable cartridge filters

**Isolation Valves:**
- Ball valves at all major equipment (chillers, CDUs, RDHx units, expansion tanks)
- Enables concurrent maintainability (isolate equipment without draining entire loop)

**Pressure Gauges & Thermometers:**
- Installed at key points: chiller inlet/outlet, CDU inlet/outlet, loop supply/return headers
- Digital sensors integrated with BMS for continuous monitoring

---

## GLYCOL SYSTEMS & WATER TREATMENT

### Glycol Specification

**Fluid Type:** Propylene glycol (non-toxic, food-grade) mixed with deionized water

**Concentration:**
- **Target:** 25-30% glycol by volume

**System Volumes:**
- **Loop 3 (L2C):** ~15,000 gallons total (includes piping, CDUs, expansion tanks)
- **Loops 1+2 (RDHx):** ~5,000 gallons total (includes piping, RDHx units, expansion tanks)
- **Total glycol required:** ~6,000 gallons propylene glycol (30% of 20,000 gal total system volume)

### Glycol Storage & Fill Systems

**Bulk Glycol Storage:**
- **Phase 1:** 1,500 gallons propylene glycol (for Loops 1+2 initial fill)
- **Phase 2:** 4,500 gallons additional (for Loop 3)
- **Delivery:** 55-gallon drums or 275-gallon totes (bulk tanker truck if available)
- **Storage Location:** Outdoor chemical storage shed with secondary containment per EPA SPCC requirements
- **Safety:** SDS (Safety Data Sheets) on-site, spill kit and containment equipment

**Glycol Mix Tanks (3 Total):**
- **Capacity:** 500-gallon mixing tanks (one per loop: Loop 1, Loop 2, Loop 3)
- **Purpose:** Pre-mix glycol to proper concentration before filling system
- **Equipment:** Mixing pumps, level indicators, sample ports for testing
- **Location:** Near respective chiller plants in mechanical yard

**Fill Stations (3 Total):**
- **Location:** One fill station per loop, adjacent to each chiller plant
- **Equipment:**
  - Hose connection points with isolation valves
  - Drain connections for maintenance
  - Portable transfer pump (200-300 GPM for initial fill)
  - Totalizing flow meters (track makeup volume over time)
- **Venting:** Manual high-point air vents for purging during initial fill

### Initial Fill Procedure

1. **Pre-Fill Preparation:**
   - Flush systems with deionized or softened water (no raw municipal water)
   - Pressure test systems per ASME standards
   - Verify all isolation valves, connections, and accessories

2. **Glycol Mixing:**
   - Mix propylene glycol to 25-30% concentration in mixing tanks
   - Test concentration with refractometer
   - Add corrosion inhibitors and pH buffers per treatment program

3. **System Fill:**
   - Pump glycol mixture into system via fill stations
   - Purge air via high-point manual vents and automatic air separators
   - Circulate fluid for 24-48 hours
   - Retest concentration and pH
   - Top off as needed via fill stations

### Makeup Water System

**Makeup Water Source:**
- Division 22 (Plumbing) shall provide 3/4" domestic water stub connections (with isolation valve + union) at three locations (one per glycol mix tank)
- Division 23 (HVAC) shall connect makeup water from these stubs to glycol mix tanks

**Annual Makeup Requirements:**
- **Target:** <1% of system volume per year (~200 gallons/year)
- **Typical Use:** Leak replacement, expansion tank overflow, sampling losses
- **Alarm Threshold:** If makeup exceeds 2% of system volume, investigate for leaks

**Totalizing Flow Meters:**
- Install at each makeup water connection
- Track cumulative makeup volume
- Integrate with BMS for alarm if threshold exceeded

### Chemical Water Treatment

**Treatment Program:**
- **Corrosion Inhibitors:** Protect steel, copper, aluminum, and stainless steel components
- **Biological Inhibitors:** Prevent algae/bacteria growth in closed-loop systems
- **pH Buffers:** Maintain pH 7.5-8.5 for corrosion control
- **Supplier:** [TBD - e.g., Nalco, ChemTreat, Kurita] - specify in detailed design

**Chemical Dosing:**
- Manual dosing via chemical dosing pots (CDPs) - one per loop
- Sized per loop volume and treatment program requirements
- Chemical replenishment per testing schedule

**Water Quality Monitoring:**
- **Quarterly Testing:** pH, conductivity, inhibitor concentration, glycol concentration
- **Annual Full Analysis:** Dissolved metals, biological activity, fluid degradation
- **BMS Integration:** Continuous conductivity sensors provide real-time monitoring and alarms

---

## LEAK DETECTION SYSTEMS

Critical system for protecting IT equipment from water/glycol damage. All chilled water leak detection is Division 23 (HVAC) scope.

### Detection Zones

**Data Hall Coverage:**
- Under all overhead chilled water piping (Loops 1, 2, 3)
- At all CDU manifold connections (162 locations in DH-W)
- At all RDHx manifold connections (232 locations in DH-E)
- Under CDU equipment locations (if CDUs located in mechanical galleries adjacent to data halls)

**Mechanical Yard/Gallery Coverage:**
- Under chiller connections and headers
- At all pumps, valves, heat exchangers
- Near expansion tanks and fill stations
- At mechanical room penetrations into data halls

### Detection Technology

**Sensing Cable:**
- **Type:** Conductive fluid detection cable (continuous sensing)
- **Detection:** Water, glycol, or other conductive fluids
- **Length:** [ROM] 2,000-3,000 ft total (data halls + mechanical areas)
- **Routing:** Mounted in cable tray or direct attachment under all piping

**Spot Detectors:**
- **Type:** Discrete leak detectors at high-risk points
- **Locations:**
  - Under each CDU (162 detectors at Phase 4)
  - At each quick-disconnect fitting (394 total: 162 L2C + 232 RDHx)
  - At chiller drain pans
- **Response Time:** <1 second alarm notification

**Control Panels:**
- **Quantity:** 2 × leak detection control panels (N+1 redundancy)
- **Integration:** BACnet/IP integration to BMS
- **Alarms:** Local audible/visual alarms + BMS notification
- **Zoning:** System shall identify leak location to within 10-ft zone

### Alarm Response & Integration

**Automatic Actions (via BMS):**
1. Visual + audible alarm in NOC
2. Email/SMS notification to on-call maintenance engineer
3. DCIM integration (log event with timestamp and location)
4. Optional automatic actions: Close isolation valves if leak zone can be safely isolated

**Manual Response Protocol:**
1. Maintenance team dispatched within 15 minutes
2. Locate leak via zone indication on control panel
3. Isolate affected loop/equipment if possible (concurrent maintainability design)
4. Repair leak, pressure test, refill system, verify water quality
5. Document incident in maintenance logs

---

## SCOPE CLARIFICATION - DIVISION 23 vs DIVISION 22

**Critical Note:** To prevent scope gaps and bid-day confusion, this section clarifies the boundary between Division 23 (HVAC) and Division 22 (Plumbing) scopes.

### Division 23 (HVAC) INCLUDES:

**Cooling Equipment:**
- All air-cooled chillers (L2C and RDHx plants)
- All CDUs (Coolant Distribution Units) - 162 units at Phase 4
- All RDHx (Rear-Door Heat Exchangers) - 232 units at Phase 4
- Primary pumps (integrated with chillers)
- Secondary pumps (integrated with CDUs)
- DOAS units for data hall environmental control
- Support space RTUs and mechanical room HVAC

**Chilled Water Piping Systems (Complete):**
- All primary loop piping (Loop 1, Loop 2, Loop 3) from chillers to equipment
- All secondary loop piping (CDU to rack cold plates via dielectric fluid)
- Overhead manifolds in data halls with quick-disconnect drop points (394 total connections)
- All pipe hangers, supports, seismic bracing
- All pipe insulation for chilled water systems
- Expansion loops and flexible connectors
- Isolation valves at all equipment connections

**Glycol & Water Treatment Systems:**
- Glycol storage (3 × 500-gallon mixing tanks)
- Bulk propylene glycol procurement (~6,000 gallons total)
- Fill pumps and fill stations (3 locations, one per loop)
- Chemical storage shed with secondary containment
- Expansion tanks (3 total, one per loop)
- Air separators and dirt separators (3 sets)
- Chemical dosing pots and treatment chemicals
- Water quality testing equipment and procedures
- Totalizing flow meters for makeup water tracking
- Initial system fill, flushing, commissioning, and balancing

**Leak Detection for Chilled Water:**
- Conductive sensing cable (2,000-3,000 LF) under all chilled water piping
- Spot leak detectors (500+ total: under CDUs, at quick-disconnects, at equipment)
- Leak detection control panels (2 × panels, N+1 redundancy)
- BMS integration for chilled water leak detection
- All cabling, conduit, and field devices for leak detection

**Controls & Monitoring:**
- BMS integration for all HVAC equipment
- Temperature and pressure sensors for all loops
- Flow meters and monitoring devices
- Chiller sequencing and optimization controls


---

## CODES AND STANDARDS

- **IMC 2021** (International Mechanical Code)
- **ASHRAE 90.1-2019** (Energy Standard)
- **ASHRAE 62.1** (Ventilation)
- **ASHRAE TC 9.9** (Mission Critical Facilities)
- **NFPA 90A** (Installation of A/C and Ventilating Systems)

---

## EQUIPMENT AND COST SUMMARY

### Cooling Plant Equipment by Phase

| Equipment | Phase 1 | Phase 2 | Phase 3 | Phase 4 | Purpose |
|-----------|---------|---------|---------|---------|---------|
| **Cooling Capacity (N+1)** | ~7 MW | ~14 MW | ~21 MW | ~28 MW | Per 6MW IT block @ 1.6 PUE |
| **Estimated Chillers** | 3-4 units | 6-8 units | 9-12 units | 12-16 units | N+1 configuration per block |
| **Cooling Loops** | 3-loop support | 3-loop support | 3-loop support | 3-loop support | 85°F warm + 60°F cold water capable |

### Phase 4 Equipment Count (Ultimate Build-Out)

**COOLING PLANT EQUIPMENT**

| Equipment                       | Quantity   | Unit Size/Rating   | Total Capacity | Notes                                 |
| ------------------------------- | ---------- | ------------------ | -------------- | ------------------------------------- |
| **Air-Cooled Chillers**         | 12-16      | Vendor-dependent   | ~28 MW (N+1)   | 3-loop architecture (85°F + 60°F)     |
| **Primary Pumps**               | Integrated | -                  | -              | Factory-integrated in chillers, VFD   |
| **Expansion Tanks**             | 3          | 500-1,000 gal each | -              | 1 per loop (Loop 1, 2, 3)             |
| **Air/Dirt Separators**         | 6          | -                  | -              | 2 per loop (air + dirt)               |

**GLYCOL & WATER TREATMENT**

| Equipment | Quantity | Size/Capacity | Notes |
|-----------|----------|---------------|-------|
| **Propylene Glycol (Bulk)** | ~6,000 gal | - | 25-30% concentration for all loops |
| **Glycol Mix Tanks** | 3 | 500 gal each | Pre-mix stations (1 per loop) |
| **Fill Stations** | 3 | - | With transfer pumps, meters, valves |
| **Chemical Dosing Pots** | 3 | - | 1 per loop for corrosion inhibitors |

**PIPING & DISTRIBUTION**

| Equipment | Quantity | Size/Type | Notes |
|-----------|----------|-----------|-------|
| **Primary Loop Piping** | TBD | 4"-12" steel, insulated | Chillers to distribution points |
| **Isolation Ball Valves** | TBD | Various sizes | Equipment isolation for maintainability |
| **Quick-Disconnect Infrastructure** | TBD | Dry-break type | Client-specific deployment |

**LEAK DETECTION SYSTEMS**

| Equipment | Quantity | Type | Coverage |
|-----------|----------|------|----------|
| **Sensing Cable** | TBD | Conductive fluid detection | Under all chilled water piping |
| **Spot Leak Detectors** | TBD | Discrete sensors | Equipment and connection points |
| **Leak Detection Control Panels** | 2 | BACnet/IP integration | N+1 redundancy |

**DATA HALL ENVIRONMENTAL CONTROL**

| Equipment | Quantity | Capacity/Type | Notes |
|-----------|----------|---------------|-------|
| **DOAS Units (Data Hall West)** | 2 | 100% OA, enthalpy wheel | N+1 redundancy, L2C hall |
| **DOAS Units (Data Hall East)** | 2 | 100% OA, enthalpy wheel | N+1 redundancy, RDHx hall |
| **Steam Humidifiers** | 4 | - | Integrated in DOAS units |

**SUPPORT SPACE HVAC**

| Equipment | Quantity | Type | Serves |
|-----------|----------|------|--------|
| **Rooftop Units (RTUs)** | 4-6 | Package DX units | Offices, NOC, support spaces |
| **Mechanical Room HVAC** | 4-6 | Factory-integrated | UPS modules, PDMs, switchgear |

### Phase 4 Cost Summary (ROM - Rough Order of Magnitude)

**Note:** Costs reflect primary cooling infrastructure only. Client-specific liquid cooling distribution (CDUs, RDHx units, secondary piping) priced separately per tenant requirements.

| Category                            | Cost Placeholder | Notes                                                  |
| ----------------------------------- | ---------------- | ------------------------------------------------------ |
| **Chillers (12-16 units)**          | TBD              | 3-loop architecture, N+1 per 6MW block                 |
| **Glycol Systems**                  | TBD              | Bulk glycol, mix tanks, fill stations, treatment       |
| **Primary Piping & Distribution**   | TBD              | Steel piping, valves, tanks, separators                |
| **Leak Detection**                  | TBD              | Sensing cable, spot detectors, control panels          |
| **Data Hall Environmental**         | TBD              | DOAS units + humidification                            |
| **Support Space HVAC**              | TBD              | RTUs + mechanical room cooling                         |
|                                     |                  |                                                        |
| **TOTAL MECHANICAL (PHASE 4)**      | **TBD**          | Pricing update in progress - shell infrastructure only |

**Cost Approach:**
- **Base Infrastructure:** Chillers, primary piping, glycol systems (estimated $2,000-3,000/kW IT)
- **Client-Specific:** Liquid cooling distribution per tenant deployment

**Industry Benchmarks:**
- Air-cooled DCs: $1,000-2,000/kW
- With liquid cooling: $2,000-4,000/kW (client-dependent)



---

**Document Control:**
- **Created:** 2025-10-29
- **Updated:** 2025-11-07
- **Version:** v2
- **Key Updates:** Phase restructure to 6MW blocks (6/12/18/24 MW), chillers recalculated per block (~7MW each), L2C details simplified, rack counts removed, PUE 1.6 for sizing
- **Related:** [[Saga Pryor DC/Basis of Design/7BOD - Electrical (CSI Div 26)]]
