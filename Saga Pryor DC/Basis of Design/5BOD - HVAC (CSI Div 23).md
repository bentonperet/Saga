**Created:** 2025-10-29
**Updated from:** Pryor_Bod_EVS_Rev01.md

# BASIS OF DESIGN - HVAC
## CSI Division 23
### Pryor Data Center - PACHYDERM GLOBAL

**Parent Document:** [[Saga Pryor DC/Basis of Design/Erik_BOD_Updated/_BOD - Exec Summary and TOC]]

---

## OVERVIEW

This document defines the phased mechanical cooling strategy for a 22 MW IT (28 MW facility) data center. The design is optimized for AI/ML workloads, starting with a 3 MW L2C (Liquid-to-Chip) anchor tenant (Phase 1) and expanding to a 22 MW ultimate capacity.

The design is built on a zoned-hall (DH-W vs. DH-E) concept with two independent, physically separate cooling plants (a 16.2 MW warm-water L2C plant and a 5.8 MW cold-water RDHx plant).

**Design Philosophy:**
- **Phased Deployment:** Cooling plant CapEx is deployed in phases to match IT load and rack growth (30 → 150 → 285 → 394 racks).
- **Zoned-Hall Strategy:**
  - **Data Hall West:** Served by Loop 3 (L2C)
  - **Data Hall East:** Served by Loops 1+2 (RDHx)
- **Separate Loop Architecture:**
  - **Loop 3 (L2C):** 16.2 MW plant with an **85°F (29°C)** "warm water" supply. This temperature is specified to maximize chiller efficiency and free cooling hours.
  - **Loops 1+2 (RDHx):** 5.8 MW plant with a **60°F (15.5°C)** "cold water" supply. This temperature is required for effective rear-door air cooling.
- **Redundancy:** N+1 for all chillers, pumps, and cooling distribution units.
- **Zero Water Consumption:** Design uses all air-cooled chillers, closed-loop glycol/fluid systems, and zero evaporative cooling.
- **Target PUE:** 1.45 (Phase 1) to 1.35 (Phase 4) at scale, driven by warm-water cooling efficiencies.

---

## COOLING LOAD PHASING


### Load Summary by Phase

| Phase | IT MW | PUE  | Facility MW |
| ----- | ----- | ---- | ----------- |
| **1** | 3     | 1.45 | 4.35        |
| **2** | 6     | 1.45 | 8.7         |
| **3** | 15    | 1.35 | 20.25       |
| **4** | 22    | 1.35 | 29.7        |


### IT Load & Rack Phasing

| **Phase** | **IT MW (Cumulative)** | **Racks (Total)** | **L2C Racks (100kW)** | **RDHx Racks (25kW)** | **L2C Load** | **RDHx Load** |
|---|---|---|---|---|---|---|
| **1** | 3 MW | 30 | 30 | 0 | 3.0 MW | 0 MW |
| **2** | 6 MW | 150 | 30 | 120 | 3.0 MW | 3.0 MW |
| **3** | 15 MW | 285 | 105 | 180 | 10.5 MW | 4.5 MW |
| **4** | 22 MW | 394 | 162 | 232 | **16.2 MW** | **5.8 MW** |

### Mechanical Plant Phasing

| **Phase** | **L2C Load** | **L2C Plant (N+1)** | **RDHx Load** | **RDHx Plant (N+1)** | **L2C CDU Solution** |
|---|---|---|---|---|---|
| **1** | 3.0 MW | Phased to 3 MW | 0 MW | Not Commissioned | A/B for 30 Racks |
| **2** | 3.0 MW | Phased to 3 MW | 3.0 MW | Phased to 3 MW | A/B for 30 Racks |
| **3** | 10.5 MW | Phased to 10.5 MW | 4.5 MW | Phased to 4.5 MW | A/B for 105 Racks |
| **4** | 16.2 MW | Phased to 16.2 MW | 5.8 MW | Phased to 5.8 MW | A/B for 162 Racks |

---

## LOOP 3: WARM WATER L2C PLANT (16.2 MW)

This plant serves the 162 high-density (100 kW) L2C racks in Data Hall West.

### L2C Chiller Plant

- **Capacity (Phase 4):** Shall be an N+1 air-cooled chiller plant, phased to meet the ultimate **16.2 MW** L2C load.
- **Fluid:** 25% Propylene Glycol / Water Mixture
- **Supply Temperature:** **85°F (29°C)**
- **Efficiency:** The 85°F supply temperature is specified to maximize mechanical COP and free-cooling opportunities.
- **Pumping:** **Variable Primary Flow (VPF)**. All primary pumps shall be integrated into the packaged chillers with VFDs. No separate pump rooms required.

### L2C Coolant Distribution

**Loop Architecture:**
- **Primary Loop (Loop 3):** Facility water (25% glycol) from chillers to CDU heat exchanger
- **Secondary Loop:** Dielectric fluid (or facility-safe coolant) from CDU to rack cold plates
- **Tertiary Loop:** Cold plate internal micro-channels
- **Separation:** Primary and secondary loops isolated via plate heat exchanger in CDU (no cross-contamination)

**CDU Configuration:**
- **Location:** High-capacity CDUs located in the adjacent mechanical galleries, not in the data hall.
- **Redundancy:** Each 100 kW L2C rack shall be fed by an **A/B redundant CDU solution.**
- **Capacity (Each CDU):** The A/B CDU solution shall be sized to support the full 100 kW rack load.
- **Components:** Plate heat exchanger, secondary pumps (N+1), expansion tank, filtration system, control system with PLC, leak detection sensors.
- **Primary Side:** 85°F warm water from Loop 3.
- **Secondary Side:** Dielectric fluid (or facility-safe fluid) piped via overhead manifolds to quick-disconnects at each rack's cold plates.
- **Controls:** Integrated leak detection at all connections, reporting to BMS.

**Design Requirements (Next Phase):**
- **Water Quality:** Water quality requirements for primary and secondary loops shall be specified in detailed design.
- **Cold Plate Specifications:** Cold plate performance requirements, thermal interface materials, and component coverage shall be specified by system engineers.
- **Piping Specifications:** Manifold materials, pressure ratings, isolation valves, and quick-disconnect specifications shall be determined in detailed design.
- **Commissioning:** L2C commissioning is a specialized effort requiring coordination with commissioning professionals. Pachyderm Global has experience with liquid cooling commissioning.
- **Maintenance & Monitoring:** Routine testing schedules, filter replacement protocols, and water quality monitoring shall be specified in the next phase.

## LOOPS 1+2: COLD WATER RDHx PLANT (5.8 MW)

This plant serves the 232 medium-density (25 kW) RDHx racks in Data Hall East.

### RDHx Chiller Plant

- **Capacity (Phase 4):** Shall be an N+1 air-cooled chiller plant, phased to meet the ultimate **5.8 MW** RDHx load.
- **Fluid:** 25% Propylene Glycol / Water Mixture
- **Supply Temperature:** **60°F (15.5°C)**
- **Rationale:** This colder temperature is required for the RDHx units to effectively cool air.
- **Pumping:** **Variable Primary Flow (VPF)**. All primary pumps shall be integrated into the packaged chillers with VFDs.

### RDHx Distribution

- **RDHx Units:** One (1) Rear-Door Heat Exchanger shall be mounted on each of the 232 racks.
- **Capacity (Each RDHx):** Sized to support the 25 kW rack load.
- **Distribution:** 60°F cold water shall be piped via overhead manifolds to quick-disconnects at each RDHx unit.

---

## CHILLER & FREE COOLING SPECIFICATIONS

### General Chiller Specifications

- **Type:** Air-cooled screw or scroll compressors with integrated VFDs and free-cooling (waterside economizer) coils.
- **Refrigerant:** Shall be a **Low-GWP (Global Warming Potential) fluid** compliant with all current and anticipated EPA/AIM Act regulations.
- **Controls:** BACnet/IP integration with facility BMS for staging, rotation, and free-cooling optimization.

### Free Cooling Operation

- **L2C Loop (85°F):** The warm-water loop allows for an extended free-cooling season. The BMS shall optimize for waterside economization when ambient conditions permit.
- **RDHx Loop (60°F):** Free cooling shall be utilized when ambient conditions permit.
- **Estimated Hours:** The 85°F loop is projected to provide **~3,500-4,000 hours/year** of full or partial free cooling in the Pryor, OK climate.

---

## DATA HALL ENVIRONMENTAL CONTROL (HVAC)

The L2C and RDHx systems handle 100% of the IT heat load. A separate HVAC system is required to manage the data hall environment (air quality, humidity, pressurization).

### DOAS (Dedicated Outdoor Air System)

- **Purpose:** To provide ventilation, humidity control, and positive pressurization to the data halls, per ASHRAE TC 9.9 guidelines.
- **Type:** Dedicated 100% outdoor air units with energy recovery (enthalpy wheel).
- **Redundancy:** N+1 DOAS units shall be provided for each data hall.
- **Pressurization:** System shall maintain a positive pressure to prevent dust/contaminant infiltration.
- **Filtration:** System shall provide air filtration compliant with **ASHRAE TC 9.9 for a Class A1 data center.**
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
- **Purpose:** Freeze protection, corrosion inhibition, thermal stability
- **Verification:** Test concentration with refractometer quarterly

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

### Division 23 (HVAC) SHALL INCLUDE:

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

### Division 23 (HVAC) SHALL NOT INCLUDE:

**Domestic Systems (Division 22 Scope):**
- ❌ Domestic water service (municipal connection, meter, backflow preventer)
- ❌ Domestic water distribution to plumbing fixtures
- ❌ Plumbing fixtures (toilets, sinks, showers, etc.)
- ❌ Domestic hot water system (water heaters, recirculation)
- ❌ Sanitary sewer and vent piping
- ❌ Storm drainage (roof drains, leaders, site connections)
- ❌ Emergency eyewash/safety shower stations (even if in mechanical rooms - these are safety fixtures)
- ❌ Natural gas piping (if applicable)

**Coordination Point - Makeup Water:**
- Division 22 shall provide 3/4" domestic water stub connections (with isolation valve + union) at three locations specified by Division 23
- Division 23 shall connect these stubs to glycol mix tanks and is responsible for all makeup water metering, treatment, and system filling

**Electrical Power (Division 26 Scope):**
- ❌ Electrical power to chillers, pumps, CDUs, leak detection panels
- ❌ Conduit and wire to field devices (coordinate locations only)

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
| **L2C Plant Capacity (N+1)** | 3 MW | 3 MW | 10.5 MW | 16.2 MW | Warm water (85°F) for L2C cooling |
| **RDHx Plant Capacity (N+1)** | - | 3 MW | 6.0 MW | 7.5 MW | Cold water (60°F) for RDHx cooling |
| **CDUs (A/B Redundant)** | 30 racks | 30 racks | 105 racks | 162 racks | L2C coolant distribution (2 physical units per rack) |
| **RDHx Units** | 0 | 120 | 180 | 232 | Rear-door heat exchangers |

<!-- @claude add cost summary table here -->

---

## VERSIONING CALLOUTS

This section details key "de-risking" changes made to this Basis of Design. The goal is to define the _performance requirement_ without over-prescribing a specific _solution_, which protects the project from being locked into a single vendor or costly, non-optimal design.

- **Chiller & CDU Sizing (Sections 2.2, 3.1, 4.1):**
  - **Removed:** Specific counts of chillers (e.g., "13 chillers") and specific CDU sizes (e.g., "300 kW").
  - **Why:** This document now defines the _total N+1 capacity_ required at each phase (e.g., "Phased to 16.2 MW N+1"). This gives the engineering team the flexibility to select the most cost-effective solution (e.g., 10 larger chillers vs. 13 smaller ones) that still meets the N+1 performance goal.

- **Refrigerant (Section 5.1):**
  - **Removed:** Specific chemical names (e.g., "R-134a").
  - **Why:** Replaced with a performance requirement ("Low-GWP... compliant with EPA/AIM Act"). This future-proofs the design against changing regulations and prevents being locked into a chemical that may become obsolete or expensive.

- **Return Temps & COP (Sections 3.1, 4.1):**
  - **Removed:** Specific "Return Temperature" (e.g., 95°F) and "COP" (e.g., 5.0-6.5) values.
  - **Why:** The BOD's job is to set the _input_ (the 85°F supply), which is the key design decision. The return temperature and COP are _outcomes_ dependent on the final load and vendor-specific chiller performance. Promising a specific COP in a BOD is a commercial risk.

- **Filtration (Section 6.1):**
  - **Removed:** Specific solution ("MERV 8/13").
  - **Why:** Replaced with the _standard_ ("compliant with ASHRAE TC 9.9 for a Class A1 data center"). This ensures the goal is met (a clean data hall) without over-prescribing the exact method.

---

**Tags:** #pryor-dc #hvac #csi-div-23 #air-cooling #direct-to-chip #free-cooling #zero-water

---

**Document Control:**
- **Created:** 2025-10-29
- **Updated:** 2025-11-04
- **Related:** [[7BOD - Electrical (CSI Div 26) v2]]
