**Created:** 2025-11-04
**Project:** Saga Pryor Data Center - PACHYDERM GLOBAL
**Owner:** Saga
**Parent Document:** [[_BOD - Exec Summary]]

# BASIS OF DESIGN - ELECTRICAL (CSI DIVISION 26)
## Pryor Data Center - PACHYDERM GLOBAL

---

## 1.0 OVERVIEW

### 1.1 Project Summary

This Basis of Design defines the electrical infrastructure for a two-hall, 20,000 SF data center with an ultimate IT load of **22 MW** and a total facility load of approximately **30 MW**. The system is designed to meet Tier III standards, providing N+1 component redundancy and dual-path redundancy for all critical loads.

The electrical backbone is a self-healing 13.8 kV dual-ring MV distribution with 8 RMU switchgear and SCADA-controlled automated switching, enabling concurrent maintainability of any transformer or electrical component. The 13.8 kV common bus allows for flexible integration of utility power, backup generators, solar arrays, and battery energy storage systems.

**Key Infrastructure:**
- Customer-owned 161 kV substation with 2×35 MVA transformers (N+1 redundancy)
- Self-healing 13.8 kV dual-ring distribution (8 RMUs, SCADA-controlled) providing path redundancy
- 9×4.0 MW diesel generators @ 13.8 kV (N+1 for 30 MW facility load)
- 11×3,500 kVA LV transformers, 13.8kV/480V (N+1 redundancy with concurrent maintainability)
- N+1 UPS architecture: 23 modular UPS units (1,250 kVA each) at Phase 4, with path redundancy from MV dual-ring
- Prefabricated Power Delivery Modules (PDMs) for accelerated schedule

### 1.2 Design Philosophy

- **Availability:** Tier III (Concurrent Maintainability). Any single electrical component can be removed for maintenance without impacting IT operations.
- **Component Redundancy:** N+1 for all core infrastructure (Substation Transformers, Generators, LV Transformers, IT UPS modules, and Mechanical UPS).
- **Path Redundancy:** Dual (A/B) path diversity from the MV dual-ring distribution through independent transformer banks, switchboards, and distribution panels to dual-PDUs in each cabinet. Self-healing 13.8 kV dual-ring with SCADA-controlled automated switching provides path reconfiguration without human intervention, eliminating the need for duplicate UPS systems.
- **UPS Architecture:** N+1 modular UPS provides component redundancy (can lose one module), while the self-healing MV dual-ring provides path redundancy. This approach delivers Tier III concurrent maintainability with significantly lower CAPEX than traditional 2N UPS systems (~50% reduction in UPS module count).
- **Concurrent Maintainability:** Self-healing dual-ring topology enables isolation of any transformer or ring segment for maintenance while maintaining full N+1 redundancy on alternate path. 8 RMU switchgear with automated SCADA controls ensure continuous operation during maintenance activities.
- **Phasing Strategy:** All infrastructure (substation, generator pads, PDM pads, electrical yard, conduit rough-in) shall be designed and built for the 30 MW full build-out from day 1. Capital equipment (generators, transformers, UPS modules, mechanical UPS) will be purchased and commissioned in phases to match IT load growth.

## 2.0 UTILITY SERVICE & SUBSTATION

### 2.1 System Topology
See the SLD Document for more details.

### 2.2 Utility Interconnection

**Utility Provider:** Kamo Power Electric Co-op

**Available Substations:**
- **Sportsman Substation (SW):** 345 kV, 3 lines
- **Dry Gulch Substation (N):** 161 kV, 2 lines

**Primary Service:**
- **Voltage:** 161 kV (confirmed by client)
- **Configuration:** Customer-owned and maintained substation constructed on-site
- **Metering:** Utility revenue-grade metering at transmission voltage point of interconnection
- **Capacity:** 35 MVA minimum service capacity

### 2.3 Substation Transformers

**Configuration:** N+1 Redundancy - Either transformer capable of supporting full 30 MW facility load

| Parameter    | Specification                                |
| ------------ | -------------------------------------------- |
| **Quantity** | Two (2) transformers                         |
| **Rating**   | 35 MVA each @ 161kV/13.8kV |

## 3.0 MEDIUM VOLTAGE (13.8 KV) DISTRIBUTION

### 3.1 13.8 kV Common Bus

A 13.8 kV "common bus" infrastructure serves as the single voltage platform for all power sources and loads:
- Utility power (from 2×35 MVA substation transformers)
- Backup generators (9×4.0 MW @ 13.8 kV)
- Solar array (8+ MW DC, inverters output 13.8 kV AC directly)
- Battery Energy Storage (4-8 MWh, inverters output 13.8 kV AC directly)
- Data center critical IT and mechanical loads (via 13.8kV/480V transformers)

### 3.2 MV Dual-Ring Topology

The electrical flowchart diagram shows the self-healing 13.8 kV dual-ring architecture with 8 RMU switchgear and A/B transformer bank connections:
[insert link]

**Configuration:**
- Two (2) independent 13.8 kV distribution rings (Ring A and Ring B)
- Each ring provides redundant power path to data center A/B electrical systems
- Self-healing topology with automated fault isolation and load transfer

### 3.3 Ring Main Units (RMUs)

| Parameter    | Specification                                                                         |
| ------------ | ------------------------------------------------------------------------------------- |
| **Quantity** | Eight (8) RMUs (4 per ring)                                                           |
| **Type**     | SF6 or vacuum circuit breakers                                                        |
| **Rating**   | 13.8 kV, 630A continuous, 20 kA short-circuit rating                                  |
| **Function** | Isolate transformers, enable ring reconfiguration, interconnect generators/solar/BESS |

## 4.0 GENERATOR SYSTEM

### 4.1 Configuration

**Redundancy:** N+1 for total 30 MW facility load

**Phase 4 Configuration:**
- N = 8 generators (8 × 4.0 MW = 32 MW capacity)
- N+1 = 9 generators total
- Phased deployment: 3 (Phase 1) → 4 (Phase 2) → 6 (Phase 3) → 9 (Phase 4)

### 4.2 Generator Specifications

| Parameter                | Specification                                                                                                         |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------- |
| **Rating**               | 4,000 kW continuous / 4,400 kW standby @ 13.8 kV                                                                      |
| **Voltage**              | 13,800V ±5%, 3-phase, 60 Hz, 0.8 power factor                                                                         |
| **Fuel**                 | Diesel, EPA Tier 4 Final (NOx < 0.67 g/bhp-hr)                                                                        |

### 4.3 Generator Yard Layout

- **Location:** South side of building, electrical equipment yard

## 5.0 TRANSFORMER SYSTEM (13.8 KV / 480V)

### 5.1 Configuration

**Redundancy:** N+1 for total 30 MW facility load

**Phase 4 Configuration:**
- N = 10 transformers (10 × 3.15 MW = 31.5 MW capacity @ 0.9 PF)
- N+1 = 11 transformers total
- Phased deployment: 3 (Phase 1) → 4 (Phase 2) → 8 (Phase 3) → 11 (Phase 4)

### 5.2 Transformer Specifications

| Parameter       | Specification                                       |
| --------------- | --------------------------------------------------- |
| **Rating**      | 3,500 kVA / 3.15 MW @ 0.9 power factor              |
| **Voltage**     | 13,800V delta primary / 480Y/277V secondary         |
| **Type**        | Oil-filled, ONAN cooling (Oil Natural, Air Natural) |

## 6.0 IT UPS SYSTEM (N+1 DUAL-PATH ARCHITECTURE)

### 6.1 Configuration

- **Redundancy:** N+1 modular UPS architecture with concurrent maintainability enabled by self-healing 13.8 kV dual-ring MV distribution
- **Path Redundancy:** Provided by MV dual-ring topology (Ring A / Ring B) with SCADA-controlled automated switching
- **Component Redundancy:** Provided by N+1 UPS modules (can lose one module and continue operation)
- **Topology:** The 22 MW IT load (Phase 4) will be protected by 23 UPS modules (22+1 for N+1) with power distributed via dual A/B paths to dual-corded IT equipment

### 6.2 System Sizing (Phase 4)

- **IT Load:** 22 MW (22,000 kW)
- **UPS Modules:** 23 × 1,250 kVA modules
  - N = 22 modules (22 × 1 MW = 22 MW capacity)
  - N+1 = 23 modules total
  - Operating load: ~89% per module (optimal efficiency range of 80-90%)
- **N+1 Verification:** 22 running modules = 22 MW capacity = full IT load ✓

### 6.3 Path Redundancy Philosophy

**Path diversity is provided by the 13.8 kV self-healing dual-ring MV distribution, not by duplicate UPS systems:**

**Concurrent Maintainability:**
- Can isolate and maintain any MV ring segment via RMU switching while maintaining full N+1 UPS capacity on alternate path
- Can remove UPS modules for maintenance (firmware updates, battery service) while maintaining N redundancy
- Can transfer full facility load to either A-side or B-side independently during planned maintenance

### 6.4 UPS Module Specifications

| Parameter      | Specification                                          |
| -------------- | ------------------------------------------------------ |
| **Rating**     | 1,250 kVA / 1,000 kW per module                        |
| **Topology**   | Online double-conversion (VFI per IEC 62040-3)         |
| **Voltage**    | 480V input/output, 3-phase                             |

### 6.5 Battery System

- **Type:** Lithium-Ion (preferred) or VRLA
- **Configuration:** External battery cabinets distributed across UPS modules
- **Runtime:** 5 minutes at full IT load (sized for each phase's IT load capacity)
- **Purpose:** Sized to allow for MV generator synchronization to 13.8 kV common bus (~30-60 seconds) with margin for two startup attempts if needed
- **Why Lithium-Ion:** Higher energy density, longer lifespan (10-15 years vs 5-7 for VRLA), lower maintenance, better performance at elevated temperatures, superior performance for high-rate discharge applications

### 6.6 Recommended UPS Vendors

- Schneider Electric, Eaton, Vertiv

## 7.0 MECHANICAL UPS SYSTEM

### 7.1 Purpose

The mechanical UPS system protects critical mechanical loads (chiller pumps, CDU pumps, building fans) from brief utility interruptions during generator startup and synchronization to the 13.8 kV common bus (~30-60 seconds).

**Important:** Mechanical UPS is a separate system from IT UPS. IT equipment is protected by the dedicated N+1 IT UPS system (Section 6.0).

### 7.2 Configuration

**Redundancy:** N+1 modular static UPS architecture

**Protected Equipment:**
- Chiller pumps for Loop 3 (L2C warm water - 85°F)
- Chiller pumps for Loops 1+2 (RDHx cold water - 60°F)
- CDU pumps (L2C coolant distribution)
- Building HVAC fans (data hall pressurization and humidity control)

**Phased Deployment:** 250 kW static UPS modules added in phases to match mechanical load growth. Phase 4: 25×250 kW modules (N+1) for 6,000 kW mechanical load.

## 8.0 LOW VOLTAGE (480V) DISTRIBUTION

### 8.1 Main Switchboards

**Configuration:** Dual switchboards for dual-path (A/B) distribution

| Parameter         | Specification                                                                  |
| ----------------- | ------------------------------------------------------------------------------ |
| **Quantity**      | Two (2): SWBD-A and SWBD-B                                                     |
| **Rating**        | 4,000A copper busbar, 480V, 3-phase, 4-wire                                    |
| **Short-Circuit** | 65 kA SCCR (Short-Circuit Current Rating)                                      |
| **Source**        | SWBD-A fed from MV Ring A transformers; SWBD-B fed from MV Ring B transformers |


### 8.2 Distribution Panels

All critical IT and mechanical loads served by dual (A/B) distribution panels fed from respective (A/B) main switchboards.

| Panel | Rating | Loads Served | Path |
|-------|--------|--------------|------|
| **IT Dist A / IT Dist B** | 800A | Cabinet PDUs for IT racks | A / B |
| **Mech Dist 1A / 1B** | 800A | Loops 1+2 chillers, pumps (RDHx cooling) | A / B |
| **Mech Dist 2A / 2B** | 1,200A | Loop 3 chillers, CDUs (L2C cooling) | A / B |
| **UPS Dist A / UPS Dist B** | 400A | UPS System A/B output distribution | A / B |

## 9.0 CABINET POWER DISTRIBUTION

- **PDUs:** Each IT cabinet will be equipped with two (2) rack-mounted Power Distribution Units (PDUs), PDU-A and PDU-B.
- **Source:** PDU-A shall be fed from the "A" power path, and PDU-B from the "B" power path.
- **Rating:** PDUs shall be sized based on the cabinet's designed load 

## 10.0 NON-CRITICAL (HOUSE) POWER

### 10.1 Philosophy

All non-critical support spaces shall be on an electrical system completely separate from the critical data center infrastructure. This separation prevents non-critical load faults from impacting critical IT operations and enables independent maintenance and testing.

### 10.2 Non-Critical Areas Served

House power serves office spaces, NOC (non-IT systems), security control rooms, common areas (break rooms, gym, restrooms), circulation spaces, building HVAC, storm shelter, general lighting, elevator, and staging/storage areas.

### 10.3 Utility Service

- **Source:** Single 13.8kV/480V transformer fed from 13.8 kV common bus (via Solar/BESS connection point)
- **Capacity:** ~400 kVA (300-350 kW sustained load)
- **Single Point of Failure:** Acceptable - house generators provide backup for loss of utility

### 10.4 Natural Gas House Generators

| Parameter      | Specification                                                       |
| -------------- | ------------------------------------------------------------------- |
| **Quantity**   | Two (2) generators (N+1 redundancy)                                 |
| **Rating**     | 250-350 kW each @ 480V, 3-phase, 60 Hz                              |
| **Fuel**       | Natural gas (piped utility) or on-site propane if NG not available  |

### 10.5 Portable UPS for Workstations

Distributed UPS units (1-3 kVA, 10-15 min runtime) for NOC, security, and office workstations. Approximately 20-30 units provide ride-through during transfer to house generators.

<!-- @claude, I thought we agreed on having a dedicated UPS for all this vs. managing 20-30 distributed units! -->

## 11.0 RENEWABLE ENERGY INTEGRATION
<!-- @claude Remove this section and renumber -->



---

## 13.0 ELECTRICAL PHASING STRATEGY

Electrical infrastructure designed for 30 MW (Phase 4), with equipment added in phases.

---

### 13.1 PHASING SUMMARY TABLE

**Note:** UPS module counts reflect N+1 architecture (N modules to serve IT load + 1 redundant). Path redundancy provided by 13.8 kV self-healing dual-ring MV distribution.

| **Phase** | **IT MW** | **Racks (L2C/RDHx)** | **PUE** | **Facility MW** | **Generators (4 MW)** | **LV XFMRs (3.5 MVA)** | **IT UPS Modules (1,250 kVA)** |
|-----------|-----------|----------------------|---------|-----------------|------------------------|-------------------------|---------------------------|
| **1** | 3 | 30 (30/0) | 1.45 | ~4.35 | 3 (N+1) | 3 (N+1) | 4 (3+1, N+1) |
| **2** | 6 | 150 (30/120) | 1.45 | ~8.7 | 4 (N+1) | 4 (N+1) | 7 (6+1, N+1) |
| **3** | 15 | 285 (105/180) | 1.35 | ~20.25 | 7 (N+1) | 8 (N+1) | 16 (15+1, N+1) |
| **4** | 22 | 394 (162/232) | 1.35 | ~29.7 | 9 (N+1) | 11 (N+1) | 23 (22+1, N+1) |

---

### 13.2 PHASE 4 DATA HALL BREAKDOWN

**Total IT Capacity:** 22 MW across 394 racks in two 10,000 SF data halls

| **Data Hall**   | **Cooling Type**                | **Rack Count** | **Rack Density**  | **IT Load per Hall** | **Cooling Plant**           | **Strategy**                             |
| --------------- | ------------------------------- | -------------- | ----------------- | -------------------- | --------------------------- | ---------------------------------------- |
| **DH-W (West)** | L2C (Liquid-to-Chip)            | 162 racks      | 100 kW/rack       | 16.2 MW              | Loop 3 (85°F warm water)    | High-density AI training workloads       |
| **DH-E (East)** | RDHx (Rear-Door Heat Exchanger) | 232 racks      | 25 kW/rack        | 5.8 MW               | Loops 1+2 (60°F cold water) | Medium-density AI inference / enterprise |
| **TOTAL**       | -                               | **394 racks**  | Avg: 55.8 kW/rack | **22.0 MW**          | 3 independent loops         | Dual market strategy                     |

**Key Observations:**
- DH-W (162 racks) represents 73.6% of IT load despite having only 41% of total rack count - demonstrates high-density advantage
- DH-E (232 racks) provides 59% of total rack inventory for customer flexibility at lower densities
- Power density: DH-W = 1,620 W/SF, DH-E = 580 W/SF

---

## 14.0 EQUIPMENT AND COST SUMMARY

Please see the separate doc for electrical pricing and equipment.

---

## 15.0 CODES AND STANDARDS

- **NEC 2023** (National Electrical Code), Oklahoma amendments
- **IEEE 141** (Red Book - Electric Power Distribution)
- **IEEE 142** (Green Book - Grounding)
- **IEEE 242** (Buff Book - Protection and Coordination)
- **NFPA 70E** (Standard for Electrical Safety in the Workplace)
- **NFPA 110** (Emergency and Standby Power Systems)
- **IEC 62040-3** (UPS Classification)

---

**Document Control:**
- **Version:** v2
- **Date Updated:** 2025-11-05
- **Prepared by:** PGCIS Team
- **Key Updates:**
  - Updated for 394-rack deployment (162 L2C + 232 RDHx)
  - Detailed 4-phase buildout to 28 MW facility load (22 MW IT)
  - All equipment properly sized for facility load (IT × PUE)
  - Added comprehensive phasing narratives with load tables
  - Enhanced solar/BESS integration details