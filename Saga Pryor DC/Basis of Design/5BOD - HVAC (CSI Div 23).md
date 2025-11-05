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
| **RDHx Plant Capacity (N+1)** | - | 3 MW | 4.5 MW | 5.8 MW | Cold water (60°F) for RDHx cooling |
| **CDUs (A/B Redundant)** | 30 racks | 30 racks | 105 racks | 162 racks | L2C coolant distribution |
| **RDHx Units** | 0 | 120 | 180 | 232 | Rear-door heat exchangers |

### IT Load Summary by Phase

| Phase | IT MW | Racks | L2C Racks | RDHx Racks | L2C MW | RDHx MW | Facility MW | PUE |
|-------|-------|-------|-----------|------------|--------|---------|-------------|-----|
| **1** | 3 | 30 | 30 | 0 | 3.0 | 0 | 4.35 | 1.45 |
| **2** | 6 | 150 | 30 | 120 | 3.0 | 3.0 | 8.7 | 1.45 |
| **3** | 15 | 285 | 105 | 180 | 10.5 | 4.5 | 20.25 | 1.35 |
| **4** | 22 | 394 | 162 | 232 | 16.2 | 5.8 | 29.7 | 1.35 |

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
