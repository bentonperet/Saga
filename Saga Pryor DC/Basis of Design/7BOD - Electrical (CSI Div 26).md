

# BASIS OF DESIGN - ELECTRICAL (CSI DIVISION 26)
## Pryor Data Center - PACHYDERM GLOBAL 

---

## 1.0 OVERVIEW

### 1.1 Project Summary

This Basis of Design defines the electrical infrastructure for a two-hall, 20,000 SF data center with an ultimate IT load of **24 MW** and a total facility load of approximately **38.4 MW**. The system is designed to meet Tier III standards, providing N+1 component redundancy and dual-path redundancy for all critical loads.

The electrical backbone is a self-healing 13.8 kV dual-ring MV distribution with 8 RMU switchgear and SCADA-controlled automated switching, enabling concurrent maintainability of any transformer or electrical component. The 13.8 kV common bus allows for flexible integration of utility power, backup generators, solar arrays, and battery energy storage systems.

**Key Infrastructure:**
- Customer-owned 161 kV substation with 2×35 MVA transformers (N+1 redundancy)
- Self-healing 13.8 kV dual-ring distribution (8 RMUs, SCADA-controlled) providing path redundancy
- Medium voltage switchboards at 13.8 kV (count TBD)
- 16×3.6 MW diesel generators @ 13.8 kV (N+1 for 38.4 MW facility load, phased in 6MW blocks)
- LV transformers, 13.8kV/480V (3.5 MVA, N+1 redundancy with concurrent maintainability) **[SIZE CONFIRMATION NEEDED]**
- N+1 UPS architecture: Modular UPS units (1,250 kVA each) with path redundancy from MV dual-ring
- 16 Electrical Houses (E-Houses): Prefabricated power delivery buildings (4 per 6MW block)

### 1.2 Design Philosophy

- **Availability:** Tier III (Concurrent Maintainability). Any single electrical component can be removed for maintenance without impacting IT operations.
- **Component Redundancy:** N+1 for all core infrastructure (Substation Transformers, Generators, LV Transformers, IT UPS modules, and Mechanical UPS).
- **Path Redundancy:** Dual (A/B) path diversity from the MV dual-ring distribution through independent transformer banks, switchboards, and distribution panels to dual-PDUs in each cabinet. Self-healing 13.8 kV dual-ring with SCADA-controlled automated switching provides path reconfiguration without human intervention, eliminating the need for duplicate UPS systems.
- **UPS Architecture:** N+1 modular UPS provides component redundancy (can lose one module), while the self-healing MV dual-ring provides path redundancy. This approach delivers Tier III concurrent maintainability with significantly lower CAPEX than traditional 2N UPS systems (~50% reduction in UPS module count).
- **Concurrent Maintainability:** Self-healing dual-ring topology enables isolation of any transformer or ring segment for maintenance while maintaining full N+1 redundancy on alternate path. 8 RMU switchgear with automated SCADA controls ensure continuous operation during maintenance activities.
- **Phasing Strategy:** All infrastructure (substation, generator pads, E-House pads, electrical yard, conduit rough-in) designed for 38.4 MW full build-out from day 1. Capital equipment (generators, transformers, UPS modules, mechanical UPS) purchased and commissioned in 6MW IT load blocks to match growth.

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

**Configuration:** N+1 Redundancy - Either transformer capable of supporting full 38.4 MW facility load

| Parameter    | Specification                                |
| ------------ | -------------------------------------------- |
| **Quantity** | Two (2) transformers                         |
| **Rating**   | 35 MVA each @ 161kV/13.8kV |

## 3.0 MEDIUM VOLTAGE (13.8 KV) DISTRIBUTION

### 3.1 13.8 kV Common Bus

A 13.8 kV "common bus" infrastructure serves as the single voltage platform for all power sources and loads:
- Utility power (from 2×35 MVA substation transformers)
- Backup generators (16×3.6 MW @ 13.8 kV)
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

### 3.4 Medium Voltage Switchboards

**Configuration:** 13.8 kV switchboards providing distribution and protection for the electrical system

| Parameter    | Specification                                 |
| ------------ | --------------------------------------------- |
| **Voltage**  | 13.8 kV, 3-phase, 60 Hz                       |
| **Quantity** | Count TBD (to be specified)                   |
| **Type**     | Metal-clad switchgear with vacuum breakers    |
| **Function** | Main distribution, metering, protection       |

## 4.0 GENERATOR SYSTEM

### 4.1 Configuration

**Redundancy:** N+1 per 6MW IT load block (4 generators per block: 3 running + 1 backup)

**Block Architecture:**
- Each 6MW IT block (9.6 MW facility @ 1.6 PUE) protected by 4×3.6 MW generators
- N = 3 generators running (10.8 MW capacity)
- N+1 = 4 generators total per block
- Phase 4: 16 generators total (4 blocks × 4 generators)

**Phased Deployment:** 4 (Phase 1) → 8 (Phase 2) → 12 (Phase 3) → 16 (Phase 4)

### 4.2 Generator Specifications

| Parameter                | Specification                                                                                                         |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------- |
| **Rating**               | 3,600 kW continuous / 3,960 kW standby @ 13.8 kV                                                                      |
| **Voltage**              | 13,800V ±5%, 3-phase, 60 Hz, 0.8 power factor                                                                         |
| **Fuel**                 | Diesel, EPA Tier 4 Final (NOx < 0.67 g/bhp-hr)                                                                        |
| **Sizing Rationale**     | 3×3.6 MW = 10.8 MW capacity covers 9.6 MW block load with ~12% margin for OK heat conditions                          |

### 4.3 Generator Yard Layout

- **Location:** South side of building, electrical equipment yard
- **Quantity:** 16 generator positions at Phase 4 (4 per 6MW block)

## 5.0 TRANSFORMER SYSTEM (13.8 KV / 480V)

### 5.1 Configuration

**Redundancy:** N+1 for total 38.4 MW facility load

**Phase 4 Configuration:**
- Quantity TBD based on block architecture
- **[CONFIRMATION NEEDED: Verify 3.5 MVA sizing adequate for new 6MW block structure]**
- Phased deployment aligned with 6MW IT load blocks

### 5.2 Transformer Specifications

| Parameter       | Specification                                       |
| --------------- | --------------------------------------------------- |
| **Rating**      | 3,500 kVA / 3.15 MW @ 0.9 power factor              |
| **Voltage**     | 13,800V delta primary / 480Y/277V secondary         |
| **Type**        | Oil-filled, ONAN cooling (Oil Natural, Air Natural) |
| **Note**        | **Sizing requires confirmation for 6MW block architecture** |

## 6.0 IT UPS SYSTEM (N+1 DUAL-PATH ARCHITECTURE)

### 6.1 Configuration

- **Redundancy:** N+1 modular UPS architecture with concurrent maintainability enabled by self-healing 13.8 kV dual-ring MV distribution
- **Path Redundancy:** Provided by MV dual-ring topology (Ring A / Ring B) with SCADA-controlled automated switching
- **Component Redundancy:** Provided by N+1 UPS modules (can lose one module and continue operation)
- **Topology:** The 24 MW IT load (Phase 4) protected by 25 UPS modules (24+1 for N+1) with power distributed via dual A/B paths to dual-corded IT equipment

### 6.2 System Sizing (Phase 4)

- **IT Load:** 24 MW (24,000 kW)
- **UPS Modules:** 25 × 1,250 kVA modules
  - N = 24 modules (24 × 1 MW = 24 MW capacity)
  - N+1 = 25 modules total
  - Operating load: ~96% per module (N+1 redundancy maintained)
- **N+1 Verification:** 24 running modules = 24 MW capacity = full IT load ✓

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

**Phased Deployment:** 250 kW static UPS modules added in phases to match mechanical load growth. Phase 4: 22×250 kW modules (N+1) for 6,000 kW mechanical load.

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

### 10.5 Centralized UPS for Non-Critical Loads (N+1)

**Configuration:** Dual UPS units (N+1 redundancy) serving NOC, security control rooms, and critical office workstations

| Parameter      | Specification                                          |
| -------------- | ------------------------------------------------------ |
| **Quantity**   | Two (2) UPS units (N+1 redundancy)                     |
| **Rating**     | 30 kVA each @ 480V, 3-phase                            |
| **Topology**   | Online double-conversion (VFI per IEC 62040-3)         |
| **Runtime**    | 10-15 minutes at full load                             |
| **Purpose**    | Provide ride-through during transfer to house generators (~30-60 seconds) with margin for extended outages |

**Protected Loads:**
- NOC workstations and displays
- Security control room systems
- Critical office infrastructure (servers, network equipment)
- Building management system (BMS) workstations

**Sizing Basis:** System sized for ~22.7 kVA actual load (NOC, security, offices, BMS) with 30% growth margin. Each 30 kVA unit can support full house load independently.

---

## 11.0 ELECTRICAL PHASING STRATEGY

Electrical infrastructure designed for 38.4 MW facility load (Phase 4), with equipment added in 6MW IT load blocks.

---

### 11.1 PHASING SUMMARY TABLE

**Note:** All equipment reflects N+1 architecture per 6MW block. Path redundancy provided by 13.8 kV self-healing dual-ring MV distribution.

| **Phase** | **IT MW** | **Design PUE** | **Facility MW** | **Generators (3.6 MW)** | **E-Houses** | **LV XFMRs (3.5 MVA)** | **IT UPS Modules (1,250 kVA)** |
|-----------|-----------|----------------|-----------------|-------------------------|--------------|-------------------------|--------------------------------|
| **1** | 6 | 1.6 | 9.6 | 4 (N+1) | 4 | TBD | 7 (6+1, N+1) |
| **2** | 12 | 1.6 | 19.2 | 8 (N+1) | 8 | TBD | 13 (12+1, N+1) |
| **3** | 18 | 1.6 | 28.8 | 12 (N+1) | 12 | TBD | 19 (18+1, N+1) |
| **4** | 24 | 1.6 | 38.4 | 16 (N+1) | 16 | TBD | 25 (24+1, N+1) |

**Key Changes:**
- **Block Structure:** Each phase adds 6MW IT load (one 6MW block)
- **PUE:** Electrical calculations use 1.6 PUE (accounts for OK heat + 10% overhead). Marketing materials state 1.4 average PUE.
- **E-Houses:** 4 electrical houses per 6MW block (prefabricated power delivery buildings)
- **Transformers:** 3.5 MVA sizing requires confirmation for block architecture

---

### 11.2 PHASE 4 DATA HALL BREAKDOWN

**Total IT Capacity:** 24 MW across two 10,000 SF data halls

| **Data Hall**   | **Cooling Type**                | **IT Load**    | **Cooling Plant**           | **Strategy**                             |
| --------------- | ------------------------------- | -------------- | --------------------------- | ---------------------------------------- |
| **DH-W (West)** | L2C (Liquid-to-Chip)            | High-density   | Loop 3 (85°F warm water)    | High-density AI training workloads       |
| **DH-E (East)** | RDHx (Rear-Door Heat Exchanger) | Medium-density | Loops 1+2 (60°F cold water) | Medium-density AI inference / enterprise |
| **TOTAL**       | 3-loop architecture             | **24.0 MW**    | Independent loops           | Dual market strategy                     |

**Note:** Rack counts are client-specific and excluded from basis of design. For estimating purposes only: assume 60 DDC (Direct-to-Chip) racks per 6MW block.

---

## 12.0 EQUIPMENT AND COST SUMMARY

Please see the separate doc for electrical pricing and equipment.

---

## 13.0 CODES AND STANDARDS

- **NEC 2023** (National Electrical Code), Oklahoma amendments
- **IEEE 141** (Red Book - Electric Power Distribution)
- **IEEE 142** (Green Book - Grounding)
- **IEEE 242** (Buff Book - Protection and Coordination)
- **NFPA 70E** (Standard for Electrical Safety in the Workplace)
- **NFPA 110** (Emergency and Standby Power Systems)
- **IEC 62040-3** (UPS Classification)

---

**Document Control:**
- **Version:** v5
- **Date Updated:** 2025-11-07
- **Prepared by:** PGCIS Team
- **Key Updates:** Phase restructure to 6MW blocks (6/12/18/24 MW), 16×3.6MW generators, 16 E-Houses, MV switchboards added, PUE 1.6 for sizing