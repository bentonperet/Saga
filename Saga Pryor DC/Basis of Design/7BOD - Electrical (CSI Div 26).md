

# BASIS OF DESIGN - ELECTRICAL (CSI DIVISION 26)
## Pryor Data Center - PACHYDERM GLOBAL 

---

## 1.0 OVERVIEW

### 1.1 Project Summary

This Basis of Design defines the electrical infrastructure for a two-hall, 20,000 SF data center with an ultimate IT load of **24 MW** and a total facility load of approximately **38.4 MW**. The system is designed to meet Tier III standards, providing N+1 component redundancy and dual-path redundancy for all critical loads.

The electrical backbone is a self-healing 13.8 kV dual-ring MV distribution with 16 RMU switchgear and SCADA-controlled automated switching, enabling concurrent maintainability of any transformer or electrical component. The 13.8 kV common bus allows for flexible integration of utility power, backup generators, solar arrays, and battery energy storage systems.

**Key Infrastructure:**
- Customer-owned 161 kV substation with 2×50 MVA transformers (N+1 redundancy)
- Self-healing 13.8 kV dual-ring distribution (16 RMUs, SCADA-controlled) providing path redundancy
- Medium voltage switchboards at 13.8 kV (count TBD)
- 16×3.6 MW diesel generators @ 13.8 kV (N+1 for 38.4 MW facility load, phased in 6MW blocks)
- LV transformers, 13.8kV/480V (3.5 MVA, N+1 redundancy with concurrent maintainability)
- Distributed 1+1 UPS architecture (16 locations, 2×1.0 MW modules each) with path redundancy from MV dual-ring
- 16 Electrical Houses (E-Houses): Prefabricated power delivery buildings (4 per 6MW block)

### 1.2 Design Philosophy

- **Availability:** Tier III (Concurrent Maintainability). Any single electrical component can be removed for maintenance without impacting IT operations.
- **Component Redundancy:** N+1 for all core infrastructure (Substation Transformers, Generators, LV Transformers, IT UPS modules, and Mechanical UPS).
- **Path Redundancy:** Dual (A/B) path diversity from the MV dual-ring distribution through independent transformer banks, switchboards, and distribution panels to dual-PDUs in each cabinet. Self-healing 13.8 kV dual-ring with SCADA-controlled automated switching provides path reconfiguration without human intervention, eliminating the need for duplicate UPS systems.
- **UPS Architecture:** N+1 modular UPS provides component redundancy (can lose one module), while the self-healing MV dual-ring provides path redundancy.
- **Concurrent Maintainability:** Self-healing dual-ring topology enables isolation of any transformer or ring segment for maintenance while maintaining full N+1 redundancy on alternate path. 16 RMU switchgear with automated SCADA controls ensure continuous operation during maintenance activities.
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
- **Capacity:** 50 MVA minimum service capacity

### 2.3 Substation Transformers

**Configuration:** N+1 Redundancy - Either transformer capable of supporting full 38.4 MW facility load

| Parameter    | Specification              |
| ------------ | -------------------------- |
| **Quantity** | Two (2) transformers       |
| **Rating**   | 50 MVA each @ 161kV/13.8kV |

## 3.0 MEDIUM VOLTAGE (13.8 KV) DISTRIBUTION

### 3.1 13.8 kV Common Bus

A 13.8 kV "common bus" infrastructure serves as the single voltage platform for all power sources and loads:
- Utility power (from 2×50 MVA substation transformers)
- Backup generators (16×3.6 MW @ 13.8 kV)
- Data center critical IT and mechanical loads (via 13.8kV/480V transformers)

### 3.2 MV Dual-Ring Topology

The electrical flowchart diagram shows the self-healing 13.8 kV dual-ring architecture with 16 RMU and A/B transformer bank connections:

**Configuration:**
- Two (2) independent 13.8 kV distribution rings (Ring A and Ring B)
- Each ring provides redundant power path to data center A/B electrical systems
- Self-healing topology with automated fault isolation and load transfer

### 3.3 Ring Main Units (RMUs)

| Parameter    | Specification                                                                         |
| ------------ | ------------------------------------------------------------------------------------- |
| **Quantity** | Sixteen (16) RMUs                                                                     |
| **Type**     | SF6 or vacuum circuit breakers                                                        |
| **Rating**   | 13.8 kV, 630A continuous, 20 kA short-circuit rating {TBC}                            |
| **Function** | Isolate transformers, enable ring reconfiguration, interconnect generators/solar/BESS |


### 3.4 Medium Voltage Switchboards

**Configuration:** 13.8 kV switchboards providing distribution and protection for the electrical system

| Parameter    | Specification                              |
| ------------ | ------------------------------------------ |
| **Voltage**  | 13.8 kV                                    |
| **Quantity** | 8 total (2 per phase: A and B)             |
| **Layout**   | Phase 1: SWBD 1-A and 1-B; Phase 2: SWBD 2-A and 2-B, etc. |
| **Type**     | Metal-clad switchgear with vacuum breakers |
| **Function** | Main distribution, metering, protection    |

**Topology:**
- Each 6MW block (phase) has two Main MV Switchboards (A and B paths)
- Generators connect in a loop between the A and B switchboards, supplying both
- RMUs connect from each switchboard to provide distribution to transformers

## 4.0 GENERATOR SYSTEM

### 4.1 Configuration

**Redundancy:** N+1 per 6MW IT load block (4 generators per block: 3 running + 1 backup)

**Block Architecture:**
- Each 6MW IT block (9.6 MW facility @ 1.6 PUE) protected by 4×3.6 MW generators
- Phase 4: 16 generators total (4 blocks × 4 generators)

**Electrical Topology:**
- Generators are connected in a loop configuration between the two Main MV Switchboards (e.g., Phase 1-A and Phase 1-B)
- This loop topology allows generators to supply power to both MV switchboards simultaneously
- Provides enhanced reliability and load sharing across both A and B electrical paths

### 4.2 Generator Specifications

| Parameter            | Specification                                                                                |
| -------------------- | -------------------------------------------------------------------------------------------- |
| **Rating**           | 3,600 kW continuous / 3,960 kW standby @ 13.8 kV                                             |
| **Voltage**          | 13,800V ±5%, 3-phase, 60 Hz, 0.8 power factor                                                |
| **Fuel**             | Diesel, EPA Tier 4 Final (NOx < 0.67 g/bhp-hr)                                               |
| **Sizing Rationale** | 3×3.6 MW = 10.8 MW capacity covers 9.6 MW block load with ~12% margin for OK heat conditions |

### 4.3 Generator Yard Layout

- **Location:** Electrical equipment yard
- **Quantity:** 16 generator positions at Phase 4 (4 per 6MW block) lined up in a row.

## 5.0 TRANSFORMER SYSTEM (13.8 KV / 480V)

### 5.1 Configuration

**Redundancy:** N+1 for total 38.4 MW facility load

**Phase 4 Configuration:**
- Quantity: 16
- One per RMU, on dedicated outside concrete pad.

### 5.2 Transformer Specifications

| Parameter   | Specification                                       |
| ----------- | --------------------------------------------------- |
| **Rating**  | 3,500 kVA / 3.15 MW @ 0.9 power factor              |
| **Voltage** | 13,800V delta primary / 480Y/277V secondary         |
| **Type**    | Oil-filled, ONAN cooling (Oil Natural, Air Natural) |


## 6.0 IT UPS SYSTEM (N+1 DUAL-PATH ARCHITECTURE)

### 6.1 Configuration

- **Redundancy:** Distributed 1+1 (N+1) UPS architecture. Each of the 16 Low Voltage Main Distribution Boards (LV-MDBs) feeds a dedicated UPS system.
- **Path Redundancy:** Provided by the 13.8 kV dual-ring MV topology. 8 UPS systems are fed from MV Ring A and 8 UPS systems are fed from MV Ring B, providing full A/B path diversity to the IT loads.
- **Component Redundancy:** Provided at each of the 16 locations by a 1+1 (N+1) module configuration. The failure of a single UPS module will not impact the critical load.
- **Topology:** The 24 MW IT load (Phase 4) is protected by 16 independent 1+1 UPS systems. Each system provides A/B power (from its respective A or B logical source) to the PDUs/RPPs in its data hall zone.

### 6.2 UPS Module Specifications

| Parameter    | Specification                                     |
| ------------ | ------------------------------------------------- |
| **Rating**   | 1,250 kVA / 1,000 kW per module (or similar size) |
| **Topology** | Online double-conversion (VFI per IEC 62040-3)    |
| **Voltage**  | 480V input/output, 3-phase                        |

### 6.3 Battery System

- **Type:** Lithium-Ion (preferred) or VRLA
- **Configuration:** 16 independent external battery systems, one per 1+1 UPS system. Each battery plant is sized to support the full load for its location
- **Runtime:** 5 minutes
- **Purpose:** Sized to allow for MV generator synchronization to 13.8 kV common bus (~30-60 seconds) with margin for two startup attempts if needed.
- **Why Lithium-Ion:** Higher energy density, longer lifespan (10-15 years vs 5-7 for VRLA), lower maintenance, better performance at elevated temperatures, superior performance for high-rate discharge applications.

### 6.4 Recommended UPS Vendors
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

### 7.3 Mechanical UPS Distribution Boards

**Configuration:** Distributed mechanical power delivery architecture

| Parameter    | Specification                                                                     |
| ------------ | --------------------------------------------------------------------------------- |
| **Quantity** | 16 Mechanical UPS Distribution Boards (Mech DB) at Phase 4                        |
| **Location** | One Mech DB per LV-MDB location (co-located with IT UPS systems)                  |
| **Function** | Distribute UPS-backed power to mechanical equipment                               |
| **Input**    | Fed from mechanical UPS modules (parallel feed from LV-MDB, isolated from IT UPS) |

### 7.4 Chiller Buffer Vessels

**Purpose:** Provide thermal inertia to maintain cooling during brief power interruptions and utility-to-generator transfer events.

**Configuration:**
- **Buffer vessels** integrated with chiller systems to store thermal capacity
- Sized to maintain cooling continuity during generator startup sequence (30-60 seconds)
- Works in conjunction with mechanical UPS to protect critical cooling infrastructure

**Function:**
- Provide thermal mass to absorb cooling load during power transitions
- Reduce immediate electrical demand on battery-backed mechanical systems
- Maintain stable chilled water temperature during utility outages
- Allow time for generators to synchronize and come online without thermal stress

**Benefits:**
- Reduces mechanical UPS capacity requirements (thermal storage offsets electrical storage)
- Provides smoother transition during utility-to-generator transfer
- Protects IT equipment from thermal excursions during brief outages
- Enhances overall system resilience during multiple startup attempts

**Integration:** Buffer vessels coordinate with mechanical UPS, generators, and building automation system (BAS) to optimize cooling continuity and minimize electrical load during transitions.

## 8.0 LOW VOLTAGE (480V) DISTRIBUTION

### 8.1 Main Switchboards

**Configuration:** Dual switchboards for dual-path (A/B) distribution

| Parameter          | Specification                                                                             |
| ------------------ | ----------------------------------------------------------------------------------------- |
| **Quantity**       | Sixteen (16) LV-MDBs (one per 3.5 MVA transformer)                                        |
| **Logical System** | 8 MDBs fed from MV Ring A ("A" System); 8 MDBs fed from MV Ring B ("B" System)            |
| **Rating**         | 4,000A copper busbar, 480V, 3-phase, 4-wire {_Rating TBC, must match transformer output_} |
| **Short-Circuit**  | 65 kA SCCR (TBC)                                                                          |
| **Function**       | Main 480V distribution for all mechanical and UPS loads.                                  |

**Distribution Architecture:**
- Each LV-MDB feeds two parallel branches:
  1. **IT UPS branch** - Powers 2×1.0 MW IT UPS modules (1+1 redundancy) for critical IT loads
  2. **Mechanical UPS branch** - Powers mechanical UPS modules (parallel feed, not downstream of IT UPS) for mechanical equipment (CHW pumps, fuel pumps, CRRWA, CDU, CDB)
- This parallel configuration ensures mechanical loads are isolated from IT UPS systems

### 8.2 Distribution Panels

All critical IT and mechanical loads served by dual (A/B) distribution panels fed from respective (A/B) main switchboards.

## 9.0 CABINET POWER DISTRIBUTION

**Status:** Rack power distribution strategy is TBD and will be finalized during detailed design phase.

**Potential Configurations:**
- **Option 1:** Remote Power Panels (RPPs) with branch circuits to rack-mounted PDUs
- **Option 2:** Direct connection from UPS distribution to rack-mounted PDUs
- **Option 3:** Combination approach with RPPs for high-density zones and direct PDU connection for standard zones

**Placeholder in SLD:** PDU/RPP symbols in the single-line diagram represent the final power delivery to IT equipment, regardless of the specific distribution method selected.

## 10.0 NON-CRITICAL (HOUSE) POWER

### 10.1 Philosophy

All non-critical support spaces shall be on an electrical system completely separate from the critical data center infrastructure. This separation prevents non-critical load faults from impacting critical IT operations and enables independent maintenance and testing.

### 10.2 Non-Critical Areas Served

House power serves office spaces, NOC (non-IT systems), security control rooms, common areas (break rooms, restrooms), circulation spaces, building HVAC, storm shelter, general lighting, elevator, and staging/storage areas.

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



---

## 12.0 COST AND EQUIPMENT SUMMARY

### 12.1 ESTIMATION METHODOLOGY

**Approach:** Cost per kilowatt ($/kW) based on IT load capacity

This estimate uses industry-confirmed benchmarks for Tier III data center electrical systems, organized into seven major equipment categories. Rather than line-item pricing, we apply validated cost ranges ($/kW) to the IT load capacity and back into total project costs by 6MW block.

**Key Definitions:**
- **IT Load:** Power consumed by servers/storage/network equipment (critical load)
- **Facility Load:** IT load × PUE = Total electrical load including cooling, lighting, UPS losses
- **PUE:** 1.6 for electrical sizing
- **6MW Block:** One modular deployment unit = 6 MW IT load = 9.6 MW facility load @ 1.6 PUE

**Scope:**
- **Included:** All electrical equipment from 161 kV substation through cabinet PDUs
- **Excluded:** Mechanical equipment (chillers, pumps - Division 23), Fire protection (Division 21), BMS/DCIM (Division 25)

---

### 12.2 EQUIPMENT CATEGORIES & INDUSTRY RANGES

#### Category 1: Utility Service & 161 kV Substation

**Equipment Included:**
- Customer-owned 161 kV substation infrastructure
- 2×50 MVA power transformers (161kV/13.8kV, N+1 redundancy)
- Utility metering and protection
- Substation grounding and lightning protection
- Substation control building

**Industry Range:** **$4-8M** (complete substation serving 20-40 MW facility)
**Alternative Basis:** $150-300/kW (facility load) = $5.8-11.5M for 38.4 MW

**Phasing:** Installed Phase 1, sized for full 38.4 MW Phase 4 capacity

*Note: We included this as a placeholder as I know Saga is working on the substation*

---

#### Category 2: Medium Voltage Distribution (13.8 kV)

**Equipment Included:**
- 13.8 kV dual-ring distribution infrastructure
- 4 Ring Main Units (RMUs) with SF6 or vacuum breakers (630A, 20 kA rating)
- 2 MV switchboards
- SCADA control system for self-healing ring topology
- MV cable, terminations, and accessories

**Industry Range:** **$50-100/kW** (facility load)

**Calculation (1 block):**
- 9.6 MW facility load × $50-100/kW = <!-- calculate with code -->

**Phasing:** One block at a time

---

#### Category 3: Generator System (13.8 kV)

**Equipment Included:**
- Diesel generators @ 13.8 kV (3.6 MW continuous rating each)
- Generator switchgear and paralleling controls
- Fuel systems (day tanks, distribution piping)
- Generator pads and foundations
- Exhaust systems and sound attenuation
- EPA Tier 4 Final emissions controls

**Industry Range:** **$600-900/kW** (nameplate generator capacity)
- **Estimate for 13.8 kV MV generators: $750/kW typical**


**Calculation by Phase (N+1 per 6MW block):**

| Phase | IT Load | Facility Load @ 1.6 PUE | Generators (3.6 MW) | Total Capacity | Cost Range @ $600-800/kW |
|-------|---------|------------------------|---------------------|----------------|--------------------------|
| **1** | 6 MW | 9.6 MW | 4 units (N+1) | 14.4 MW | **$8.6-11.5M** |
| **2** | 12 MW | 19.2 MW | 8 units (N+1) | 28.8 MW | **$17.3-23.0M** |
| **3** | 18 MW | 28.8 MW | 12 units (N+1) | 43.2 MW | **$25.9-34.6M** |
| **4** | 24 MW | 38.4 MW | 16 units (N+1) | 57.6 MW | **$34.6-46.1M** |

**Phasing:** 4 generators per 6MW block added incrementally


---

#### Category 4: Low Voltage Transformers (13.8kV/480V)

**Equipment Included:**
- Oil-filled pad-mounted transformers (3.5 MVA each)
- Outdoor concrete pads with oil containment
- MV and LV terminations
- Transformer protection and monitoring

**Industry Range:** **$40-80/kW** (transformer capacity)

**Note:** **Transformer count and sizing requires confirmation** for 6MW block architecture (flagged in Section 5.0)

**Placeholder Calculation (Phase 4, pending confirmation):**
- Assuming N+1 for 38.4 MW facility load
- Est. capacity: ~45-50 MVA total
- Cost range: **$1.8-4.0M** (pending transformer count verification)

**Phasing:** Transformers added per 6MW block, aligned with generators

---

#### Category 5: IT UPS System (N+1 Modular)

**Equipment Included:**
- Modular UPS units (1,250 kVA / 1,000 kW each)
- Lithium-ion battery cabinets (5-minute runtime)
- UPS input/output switchgear
- Battery management system (BMS)
- UPS monitoring and controls

**Industry Range:** **$100-200/kW** (IT load, including batteries)

**Calculation by Phase (1+1 redundancy per location):**

| Phase | IT Load | UPS Modules (1.0 MW / 1,250 kVA) | Configuration | Cost Range @ $100-200/kW |
|-------|---------|----------------------------------|---------------|--------------------------|
| **1** | 6 MW | 8 units | 2×1.0 MW at 4 locations | $0.6-1.2M |
| **2** | 12 MW | 16 units | 2×1.0 MW at 8 locations | $1.2-2.4M |
| **3** | 18 MW | 24 units | 2×1.0 MW at 12 locations | $1.8-3.6M |
| **4** | 24 MW | 32 units | 2×1.0 MW at 16 locations | **$2.4-4.8M** |

**Phasing:** UPS modules added per 6MW block (4 LV-MDBs × 2 UPS modules = 8 modules per block) to maintain 1+1 redundancy at each location

---

#### Category 6: LV Distribution & E-Houses

**Equipment Included:**
- **E-Houses (Prefabricated Electrical Buildings):** 14'×260' climate-controlled enclosures containing:
  - MV switchgear (RMUs for ring connection)
  - LV switchboards (SWBD-A/B)
  - IT UPS modules and battery cabinets
  - Mechanical UPS modules
  - Distribution panels (IT Dist A/B, Mech Dist 1A/1B/2A/2B, UPS Dist A/B)
- **LV Switchboards:** 4,000A copper busbar, 480V, 65 kA SCCR
- **Distribution Panels:** Various ratings (400A-1,200A) for IT and mechanical loads
- **Cabinet PDUs:** Dual rack-mounted PDUs per IT cabinet (PDU-A/PDU-B)
- **Cable tray, conduit, and wire:** Overhead cable distribution infrastructure

**Industry Ranges:**
- **E-Houses:** $1.5-3.5M per unit (complete with internal equipment)
- **Switchgear & Distribution:** $75-150/kW (IT load)
- **Cabinet PDUs:** $25-50/kW (IT load)

**Calculation by Phase:**

| Phase | IT Load | E-Houses (4 per block) | E-House Cost @ $1.5-3.5M | Dist/PDU @ $100-200/kW* | Total Category 6 |
|-------|---------|------------------------|--------------------------|------------------------|------------------|
| **1** | 6 MW | 4 units | $6.0-14.0M | $0.6-1.2M | $6.6-15.2M |
| **2** | 12 MW | 8 units | $12.0-28.0M | $1.2-2.4M | $13.2-30.4M |
| **3** | 18 MW | 12 units | $18.0-42.0M | $1.8-3.6M | $19.8-45.6M |
| **4** | 24 MW | 16 units | $24.0-56.0M | $2.4-4.8M | **$26.4-60.8M** |

*Combined switchgear/distribution and PDU ranges ($75-150/kW + $25-50/kW = $100-200/kW)

**Phasing:** 4 E-Houses per 6MW block (complete power delivery infrastructure)

**Note:** E-House cost dominates this category. Wide range ($1.5-3.5M) reflects turnkey vs. shell-only pricing. Recommend obtaining quotes from E-House manufacturers (PowerHouse, DRS/EPC, Ermco) for Phase 1 block.

---

#### Category 7: Supporting Systems

**Equipment Included:**
- **Mechanical UPS:** Modular static UPS (250 kW units) for chiller pumps, CDUs, CRAH fans
- **House Generators:** 2×300 kW natural gas generators (N+1 for non-critical building loads)
- **House UPS:** 2×30 kVA units (N+1 for NOC, security, offices)
- **Lighting:** LED lighting with emergency backup in all areas
- **Grounding:** Building ground grid, equipment grounding, lightning protection
- **Testing & Commissioning:** Factory acceptance testing (FAT), site acceptance testing (SAT), integrated systems testing (IST)

**Industry Ranges:**
- Mechanical UPS: $80-120/kW (mechanical load)
- House generators: $150-250/kW (nameplate capacity)
- Supporting systems: ~5-8% of major electrical equipment cost

**Placeholder Calculation (Phase 4):**
- Mechanical UPS (22×250 kW modules): ~$1.5-2.2M
- House generators (2×300 kW): ~$0.1-0.15M
- House UPS (2×30 kVA): ~$0.015-0.025M
- Lighting, grounding, testing: ~5% of Categories 1-6
- **Estimated range: $3-6M** (Phase 4)

**Phasing:** Mechanical UPS scaled with cooling loads per block; house systems installed Phase 1

---

### 12.3 TOTAL ELECTRICAL COST BY PHASE (6MW BLOCKS)

#### Original Estimate (SUPERSEDED - See Revised Estimate Below)

| Phase | IT Load | Category 1 | Category 2 | Category 3 | Category 4 | Category 5 | Category 6 | Category 7 | **TOTAL RANGE** |
|-------|---------|------------|------------|------------|------------|------------|------------|------------|-----------------|
| **1** | 6 MW | $4.0-8.0M | $0.5-1.0M | $2.2-3.6M | $0.5-1.0M | $0.6-1.2M | $6.6-15.2M | $1.5-2.5M | **$15.9-32.5M** |
| **2** | 12 MW | $4.0-8.0M | $1.0-1.9M | $4.3-7.2M | $0.9-2.0M | $1.2-2.4M | $13.2-30.4M | $2.0-3.5M | **$26.6-55.4M** |
| **3** | 18 MW | $4.0-8.0M | $1.4-2.9M | $6.5-10.8M | $1.4-3.0M | $1.8-3.6M | $19.8-45.6M | $2.5-4.5M | **$37.4-78.4M** |
| **4** | 24 MW | $4.0-8.0M | $1.9-3.8M | $8.6-14.4M | $1.8-4.0M | $2.4-4.8M | $26.4-60.8M | $3.0-6.0M | **$48.1-101.8M** |

**Original Cost per kW (Phase 4):** $2,004-4,242/kW (midpoint $3,123/kW)

**Issues with original estimate:**
- Generator costs used 480V pricing ($150-250/kW), not 13.8 kV MV pricing ($600-800/kW)
- Potential double-counting between Categories 2, 5, 6 (MV dist, UPS, E-Houses)

---

#### **REVISED ESTIMATE (RECOMMENDED)** ✅

**Restructured Categories:**

| Category                         | Description                          | Components                                                             |
| -------------------------------- | ------------------------------------ | ---------------------------------------------------------------------- |
| **1. Utility & Substation**      | 161 kV substation complete           | 2×50 MVA transformers, metering, protection, control building          |
| **2. MV Distribution (Outdoor)** | 13.8 kV ring infrastructure only     | Outdoor cable, SCADA backbone (RMUs in E-Houses)                       |
| **3. Generators (13.8 kV)**      | Medium voltage diesel generators     | 16×3.6 MW @ 13.8 kV (N+1 per block)                                    |
| **4. LV Transformers**           | Outdoor pad-mounted 13.8kV/480V      | Oil-filled transformers with containment                               |
| **5. E-Houses (Turnkey)**        | Prefab electrical buildings complete | MV switchgear, LV switchboards, UPS, batteries, fire suppression, HVAC |
| **6. Cabinet PDUs & Dist**       | Final distribution to IT racks       | Rack PDUs, cable tray, overhead distribution                           |
| **7. Supporting Systems**        | Ancillary electrical systems         | Mech UPS, house generators, house UPS, lighting, testing               |

**Revised Cost Summary by Phase:**

| Phase | IT Load | Cat 1 (Substation) | Cat 2 (MV Outdoor) | Cat 3 (Generators) ⚠️ | Cat 4 (LV Xfmr) | Cat 5 (E-Houses) | Cat 6 (PDUs) | Cat 7 (Support) | **TOTAL RANGE** |
|-------|---------|-------------------|-------------------|---------------------|-----------------|------------------|--------------|----------------|-----------------|
| **1** | 6 MW | $4.0-8.0M | $0.5-1.0M | **$8.6-11.5M** | $0.5-1.0M | $6.0-14.0M | $0.6-1.2M | $1.5-2.5M | **$21.7-39.2M** |
| **2** | 12 MW | $4.0-8.0M | $0.8-1.5M | **$17.3-23.0M** | $0.9-2.0M | $12.0-28.0M | $1.2-2.4M | $2.0-3.5M | **$38.2-68.4M** |
| **3** | 18 MW | $4.0-8.0M | $1.0-1.8M | **$25.9-34.6M** | $1.4-3.0M | $18.0-42.0M | $1.8-3.6M | $2.5-4.5M | **$54.6-97.5M** |
| **4** | 24 MW | $4.0-8.0M | $1.0-2.0M | **$34.6-46.1M** | $1.8-4.0M | $24.0-56.0M | $2.4-4.8M | $3.0-6.0M | **$70.8-126.9M** |

**Revised Cost per kW (Phase 4):**
- Low estimate: $70.8M ÷ 24,000 kW = **$2,950/kW**
- High estimate: $126.9M ÷ 24,000 kW = **$5,288/kW**
- **Midpoint: $4,119/kW**

**Change from Original:**
- Increase: +$22.7M to +$25.1M (47-25% increase)
- Primary driver: Generator cost correction (+$26.0-31.7M)
- Offset by: Elimination of double-counting in MV distribution (-$0.9-1.8M)

---

### 12.4 INDUSTRY BENCHMARK VALIDATION

**Corrected Industry Benchmarks (2024-2025 Research):**

| Source                              | Scope                             | Range                | Confidence | Notes                                                 |
| ----------------------------------- | --------------------------------- | -------------------- | ---------- | ----------------------------------------------------- |
| **Dgtl Infra / Multiple sources**   | Total data center (all divisions) | $7-12M per MW        | High       | Greenfield construction                               |
| **Hyperscale builders**             | Total data center (optimized)     | $6M per MW           | High       | Experienced builders, minimal support infra           |
| **Electrical portion**              | 40-45% of total DC cost           | **$2.8-5.4M per MW** | High       | **= $2,800-5,400/kW (IT load)**                       |


**Our Estimate (Phase 4):** $2,004-4,242/kW (midpoint $3,123/kW)

**Revised Position Analysis:**

| Benchmark | Range | Our Estimate | Position |
|-----------|-------|--------------|----------|
| **Electrical (40-45% of total)** | **$2,800-5,400/kW** | $2,004-4,242/kW | -28% to +51% ✅ |
| Total DC cost (for reference) | $6,000-12,000/kW | N/A (elec only) | Electrical is 34-71% of total |


Our estimate of $2,004-4,242/kW falls within or slightly below the validated industry range of $2,800-5,400/kW for electrical systems (40-45% of total data center cost).

---

### 12.4.1 CRITICAL FINDINGS FROM RESEARCH

#### Finding 1: E-House Scope Includes Internal Equipment ✅

**Research Confirms:** Prefabricated E-Houses are **turnkey solutions** that include:
- Medium voltage switchgear (RMUs for ring connection)
- Low voltage switchboards
- UPS systems and battery cabinets
- Transformers (project-dependent)
- Fire suppression systems (clean agent)
- HVAC systems for the enclosure
- SCADA and control systems
- Factory testing and commissioning

**Source:** Eaton, Schneider Electric, WEG, multiple E-House manufacturers (2024)

**Implication:** E-Houses contain the equipment, not just the building shell. This is appropriate and NOT double-counting if we structure categories correctly.

---

#### Finding 2: E-House Cost Premium is Justified ✅

**Research Confirms:** Prefabricated E-Houses can cost **MORE** than stick-built electrical rooms when:
- High degree of customization is required
- Specialized equipment integration needed
- Turnkey delivery with factory testing desired
- Remote site with limited skilled labor availability

**Cost Comparison:**
- General modular: 30% less expensive than stick-built (standardized)
- Specialized data center E-Houses: Can be MORE expensive than stick-built
- Premium justified by: Faster deployment, factory testing, reduced site risk, concurrent installation

**Sources:** Data Center Dynamics, C&C Technology Group, Schneider Electric (2024)

**Implication:** $1.5-3.5M per E-House is reasonable for 14'×260' climate-controlled prefab buildings with integrated MV/LV equipment.

---

#### Finding 3: Generator Costs Are Underestimated ⚠️

**Research Confirms:** 13.8 kV medium voltage diesel generators cost:
- Base multi-MW diesel generator: **$700/kW** (capital cost)
- Medium voltage premium (480V → 13.8 kV): **+$50/kW**
- **Total: $750/kW** for 13.8 kV MV generators

**Source:** Multi-MW generator analysis, Penn State Extension (2024)

**Current Estimate:** $150-250/kW (significantly LOW)

**Correction Required:** Generator costs should be $600-800/kW for 13.8 kV diesel generators

**Implication:** Category 3 (Generators) is underestimated by 3-5×

---

#### Finding 4: Recommended Category Restructure to Eliminate Confusion

**Current Issue:** Categories 2, 5, and 6 have overlapping scopes because E-Houses contain MV switchgear and UPS

**Recommended Approach:** Two options:

**Option A: E-Houses as Complete Integrated Systems (RECOMMENDED)**
- **Category 6: E-Houses (Turnkey Complete)**
  - Price per E-House includes ALL internal equipment:
    - MV switchgear (RMUs for ring connection)
    - LV switchboards
    - UPS modules and batteries
    - Distribution panels
    - Fire suppression, HVAC, SCADA
  - **Eliminate** separate Categories 2 and 5 (now included in E-House cost)
  - Keep Categories 1, 3, 4, 7 separate (not in E-Houses)

**Option B: Separate Equipment from Enclosure**
- **Category 6a: E-House Shells Only** (building enclosure, HVAC, fire suppression)
  - Estimate: $500K-1.0M per shell (14'×260' prefab building)
- **Category 6b: Electrical Equipment Installed in E-Houses**
  - MV switchgear, LV switchboards, UPS, batteries, panels
  - Estimate: $1.0-2.5M per E-House worth of equipment
- Keep Categories 2, 5 but clarify they are **installed inside E-Houses**

**Recommendation:** Use **Option A** for simplicity and accuracy. E-House vendors quote turnkey pricing inclusive of equipment.

---

### 12.4.2 REVISED ESTIMATE WITH CORRECTIONS

**Restructured Categories (Eliminating Double-Count, Correcting Generator Costs):**

| Category | Description | Phase 4 Cost | Notes |
|----------|-------------|--------------|-------|
| **1. Utility & Substation** | 161 kV substation, 2×50 MVA transformers | $4.0-8.0M | Validated ✅ |
| **2. MV Distribution (Outdoor)** | 13.8 kV ring infrastructure, cable, SCADA backbone | $1.0-2.0M | Reduced (RMUs now in E-Houses) |
| **3. Generators (13.8 kV)** | 16×3.6 MW diesel generators @ 13.8 kV | **$34.6-46.1M** | **CORRECTED: $600-800/kW × 57.6 MW** ⚠️ |
| **4. LV Transformers** | Outdoor pad-mounted 13.8kV/480V transformers | $1.8-4.0M | Pending count confirmation |
| **5. E-Houses (Turnkey Complete)** | 16 prefab electrical buildings with ALL internal equipment | $24.0-56.0M | Includes MV switchgear, UPS, LV dist ✅ |
| **6. Cabinet PDUs & Distribution** | Rack PDUs, cable tray, final distribution | $2.4-4.8M | $100-200/kW for PDUs and cabling |
| **7. Supporting Systems** | Mech UPS, house generators, lighting, testing | $3.0-6.0M | Validated ✅ |

**REVISED TOTAL (Phase 4):** **$70.8-126.9M**

**Revised Cost per kW:**
- Low: $70.8M ÷ 24,000 kW = **$2,950/kW**
- High: $126.9M ÷ 24,000 kW = **$5,288/kW**
- **Midpoint: $4,119/kW**

**Position vs. Industry Benchmark:**

| Benchmark | Range | Revised Estimate | Position |
|-----------|-------|------------------|----------|
| **Electrical (40-45% of $7-12M/MW)** | $2,800-5,400/kW | **$2,950-5,288/kW** | **Within range ✅** |

**Confidence Level Improvement:** ±25% → ±20% (with generator cost correction and scope clarification)

---

### 12.4.3 KEY ADJUSTMENTS EXPLAINED

**Adjustment 1: Generator Cost Correction (+$26.0-31.7M)**
- **Previous:** $8.6-14.4M (using $150-250/kW, which was for 480V generators)
- **Corrected:** $34.6-46.1M (using $600-800/kW for 13.8 kV MV generators)
- **Justification:** Multi-MW diesel generators cost $700/kW base + $50/kW for MV capability
- **Source:** Penn State Extension, multi-MW generator cost analysis

**Adjustment 2: Eliminated Double-Counting in MV Distribution (-$0.9-1.8M)**
- **Previous Category 2:** $1.9-3.8M (included all RMUs and MV switchgear)
- **Revised Category 2:** $1.0-2.0M (outdoor ring infrastructure only; RMUs now in E-Houses)
- **Justification:** E-House scope includes MV switchgear (RMUs) for ring connection

**Adjustment 3: Eliminated UPS as Separate Category (Moved to E-Houses)**
- **Previous Category 5:** $2.4-4.8M (standalone UPS systems)
- **Revised:** UPS cost now embedded in Category 5 (E-Houses Turnkey Complete)
- **Justification:** E-House vendors provide UPS as integrated system within enclosure

**Adjustment 4: Renamed and Clarified Category 6**
- **Previous:** "LV Distribution & E-Houses" (confusing scope)
- **Revised Category 5:** "E-Houses (Turnkey Complete)" - clearly includes all internal equipment
- **Revised Category 6:** "Cabinet PDUs & Distribution" - final distribution to racks only

---

### 12.5 CONFIDENCE LEVEL

**Confidence Level:** **±30%** (Low Confidence - Requires Additional Research)

**Justification:**
- **Pre-conceptual estimate** with no vendor quotes or detailed design
- **Wide cost ranges** reflect uncertainty ($1.5-3.5M per E-House is 133% spread)
- **Industry benchmark mismatch** requires investigation and validation
- **Key equipment sizing unconfirmed** (LV transformers, MV switchboard count)
- **Limited sources:** Primarily from single estimating methods document

**To Improve to ±20%:**
1. Obtain budget quotes from E-House manufacturers (PowerHouse, DRS/EPC, Ermco)
2. Research 3+ additional sources for 13.8 kV MV distribution costs
3. Confirm LV transformer count and sizing for 6MW block architecture
4. Validate whether industry $/kW benchmarks include or exclude E-House enclosures
5. WebSearch for recent data center electrical cost case studies (2024-2025)

**To Improve to ±15%:**
- Complete 60% design documents
- Obtain preliminary quotes from 2+ vendors per major equipment category
- Finalize single-line diagram (SLD) with all equipment counts
- Conduct value engineering workshop comparing E-House vs. stick-built

---

### 12.6 SOURCES & REFERENCES

#### Primary Industry Sources (2024-2025)

1. **Dgtl Infra** - "How Much Does it Cost to Build a Data Center?" (2024)
   - Total greenfield DC cost: $7-12M per MW
   - Electrical systems: 40-45% of total cost
   - **Derived electrical range: $2.8-5.4M per MW**
   - URL: https://dgtlinfra.com/how-much-does-it-cost-to-build-a-data-center/

2. **Data Center Dynamics** - "Building at Scale: Hyperscalers aim to build at $6m per MW" (2024)
   - Optimized hyperscale construction: $6M per MW
   - Electrical: 40-45% = $2.4-2.7M per MW
   - URL: https://www.datacenterdynamics.com/en/news/building-scale-hyperscalers-aim-build-6m-mw/

3. **Multiple Industry Sources** - Data center cost breakdown consensus
   - Land and Building Shell: 15-20%
   - **Electrical Systems: 40-45%**
   - HVAC/Mechanical/Cooling: 15-20%
   - Building Fit-Out: 20-25%

#### E-House and Prefabrication Sources

4. **Eaton** - "E-House | Prefabricated electrical house | Custom PDC" (2024)
   - Turnkey scope: Switchgear, transformers, UPS, controls, fire suppression
   - Factory testing and commissioning included
   - URL: https://www.eaton.com/us/en-us/catalog/low-voltage-power-distribution-controls-systems/integrated-power-assemblies-e-house.html

5. **Schneider Electric** - "Prefabricated vs Traditional Data Center Cost Calculator" (2024)
   - Modular prefab can be 30% less expensive (standardized)
   - Custom E-Houses can be MORE expensive than stick-built
   - Benefits: Faster deployment, reduced site risk, factory testing
   - URL: https://blog.schneider-electric.com/datacenter/

6. **Data Center Dynamics** - "Stick built or prefab?" (2024)
   - E-House cost depends on customization level
   - Specialized data center applications: Premium pricing justified
   - URL: https://www.datacenterdynamics.com/en/opinions/stick-built-or-prefab/

7. **C&C Technology Group** - "Modular Data Centers and Electrical Power Skid" (2024)
   - Prefab electrical houses can be MORE expensive than traditional methods
   - Specialized equipment and controlled environment increase costs
   - Shipping costs add 10-20% for long distances

#### Generator Cost Sources

8. **Penn State Extension** - "Calculate Costs for On-Site Electricity Generation" (2024)
   - Multi-MW diesel generators: **$700/kW capital cost**
   - URL: https://extension.psu.edu/calculate-costs-for-on-site-electricity-generation

9. **Consulting-Specifying Engineer** - "Designing medium-voltage genset systems" (2024)
   - 480V to 15 kV upgrade: **+$100K for 2 MW generator = +$50/kW**
   - MV alternators typically ≥1 MW, common ≥2 MW
   - 13.8 kV is highest nominal voltage for gensets
   - URL: https://www.csemag.com/articles/designing-medium-voltage-genset-systems/

10. **Thunder Said Energy** - "Diesel power generation levelized costs" (2024)
    - Multi-MW scale diesel: $700/kW capital cost confirmed
    - Operating cost: 20¢/kWh effective power price for 10% IRR
    - URL: https://thundersaidenergy.com/downloads/diesel-power-generation-levelized-costs/

#### UPS and Battery Sources

11. **BloombergNEF / Statista** - "Battery price per kWh 2024" (2024)
    - Lithium-ion battery packs: **$115/kWh** (2024 pricing)
    - Down from $139/kWh (2023)
    - URL: https://www.statista.com/statistics/883118/global-lithium-ion-battery-pack-costs/

12. **Schneider Electric** - "Galaxy VXL modular UPS series" (Dec 2024)
    - 500-1,250 kW modular UPS units
    - 97.5% efficiency in double conversion mode
    - Lithium-ion battery integration

13. **Uptime Institute** - "Data Center Capital Cost Survey 2024"
    - Tier III construction: $23,000/kW of redundant UPS capacity (OUTDATED - includes all systems)
    - Industry moving toward cost-optimized Tier III: $6,500/kW total facility

#### Medium Voltage Distribution Sources

14. **Schneider Electric Blog** - "Why medium-voltage distribution is ideal for large data centers" (2024)
    - MV switchgear/transformers/generators cost MORE than LV
    - Economic breakeven: >10-20 MW of power
    - Single 4" conduit at 13.2 kV distributes 4,000 kW (vs. 12×4" at 480V)
    - URL: https://blog.se.com/datacenter/2014/04/29/large-data-centers-medium-voltage-distribution-makes-lots-sense/

15. **Data Center Dynamics** - "Medium voltage power distribution in data centers" (2024)
    - Substations: $3-7M typical (not voltage-specific)
    - 13.2 kV, 13.8 kV, 27.6 kV are common MV levels
    - URL: https://www.datacenterdynamics.com/en/opinions/medium-voltage-power-distribution-in-data-centers/

#### Tier III Redundancy and Cost

16. **PowerMag** - "Understanding Uptime Institute's Tier III Standard" (2024)
    - N+1 redundancy for all critical systems
    - Concurrent maintainability requirement
    - 99.982% availability (1.6 hours downtime/year)
    - URL: https://www.powermag.com/understanding-uptime-institutes-tier-iii-standard/

17. **Webwerks** - "Tier III vs. Tier IV Data Centers" (2024)
    - Tier IV costs 25-40% more than Tier III
    - Tier III balances availability and cost-effectiveness
    - URL: https://www.webwerks.in/blogs/tier-iii-vs-tier-iv-data-centers

#### Internal References

18. **Internal:** [[zEstimating Methods - Data Center Cost Research]] (Division 26 section)
    - Initial $/kW methodology and framework
    - $400-700/kW range (now confirmed incomplete)

19. **IEEE 141 (Red Book):** Electric Power Distribution standards
20. **NFPA 110:** Emergency and Standby Power Systems
21. **NEC 2023:** National Electrical Code (Oklahoma amendments)

---

### 12.7 ASSUMPTIONS & LIMITATIONS

**Assumptions:**
1. All infrastructure (pads, yards, conduit rough-in) sized for Phase 4 (38.4 MW) from day 1
2. Capital equipment (generators, transformers, UPS, E-Houses) purchased in 6MW IT load blocks
3. PUE = 1.6 for electrical sizing (facility load = IT load × 1.6)
4. N+1 redundancy maintained throughout all phases
5. E-House scope includes all internal electrical equipment (may overlap with other categories)
6. Costs are hard construction costs only (exclude A&E design fees, permits, owner's costs)

**Limitations:**
1. **No competitive bids or vendor quotes** - ranges from industry benchmarks only
2. **E-House cost uncertainty** - wide range reflects lack of market data
3. **Transformer sizing unconfirmed** - placeholder estimate pending design verification
4. **Scope boundary unclear** - potential overlap between categories requires clarification
5. **Regional cost factors not applied** - Oklahoma pricing may differ from national averages
6. **Escalation not included** - costs in 2024-2025 dollars, no escalation to construction dates

**Items Flagged for Confirmation:**
- LV transformer count and sizing (Section 5.2)
- MV switchboard count (Section 3.4)
- E-House internal equipment scope definition
- Mechanical UPS module count for Phase 1-3 (Section 11.1 shows TBD)

---

### 12.8 RECOMMENDATIONS & NEXT STEPS

#### Immediate Recommendations

**Recommendation 1: Adopt Revised Estimate ($70.8-126.9M for Phase 4)** ✅

The revised estimate of **$2,950-5,288/kW** is now validated against industry benchmarks ($2,800-5,400/kW for electrical systems representing 40-45% of total data center cost). This is a 47% increase from the initial estimate, primarily due to:
- Generator cost correction: +$26.0-31.7M (now $600-800/kW for 13.8 kV MV generators)
- Scope clarification for E-Houses (turnkey complete, includes MV switchgear and UPS)
- Elimination of double-counting in MV distribution

**Recommendation 2: Prioritize Generator Cost Validation** ⚠️ CRITICAL

**Issue:** Generator costs represent the largest single category ($34.6-46.1M, or 49-36% of total electrical cost).

**Actions:**
1. Obtain budget quotes from 3+ MV generator manufacturers:
   - Caterpillar (Cat 3516 or 3612 series @ 13.8 kV)
   - Cummins (QSK60G or QSK78G series with MV alternator)
   - MTU (16V 4000 or 20V 4000 series @ 13.8 kV)
2. Specify 3.6 MW continuous, 13.8 kV output, EPA Tier 4 Final, diesel fuel
3. Request pricing for 4-unit order (Phase 1) and 16-unit order (Phase 4) to assess volume pricing
4. Target: Validate $600-800/kW range or revise estimate based on actual quotes

**Expected Timeline:** 2-3 weeks for budget quotes (non-binding)

**Recommendation 3: Structure E-House Procurement as Turnkey Packages** ✅

**Rationale:** Industry practice confirms E-Houses are quoted as turnkey systems including all internal equipment.

**Procurement Strategy:**
- Issue RFQ for 4×E-Houses (Phase 1), specify:
  - Complete turnkey delivery (MV switchgear, LV switchboards, UPS, batteries, HVAC, fire suppression)
  - Factory testing and commissioning
  - 14'×260' climate-controlled prefab building
  - Equipment capacity: 1.5 MW IT load per E-House (6 MW total for 4 units)
- Vendors to contact:
  - Eaton (Integrated Power Assemblies division)
  - Schneider Electric (Power Modules)
  - PowerHouse (PE Modules)
  - DRS/EPC (Data Center Solutions)
  - Ermco (Prefabricated Electrical Buildings)

**Target pricing:** $1.5-3.5M per E-House (validate current estimate)

**Recommendation 4: Value Engineering Alternatives to Reduce Cost**

If budget constraints require cost reduction, consider these alternatives:

**VE Option 1: Stick-Built Electrical Rooms vs. E-Houses**
- **Savings potential:** 20-40% on enclosure costs (if stick-built is less expensive in Oklahoma)
- **Trade-off:** +4-6 months construction time, increased site labor, no factory testing
- **Net impact:** Potentially -$4-10M on E-House premium, but delays revenue by 6 months
- **Recommendation:** Only pursue if schedule allows and local skilled labor is available

**VE Option 2: Reduce Generator Redundancy to "N" (Eliminate "+1")**
- **Savings potential:** -$2.2-2.9M per phase (eliminate 1 of 4 generators per 6MW block)
- **Trade-off:** Loss of Tier III certification, no concurrent maintainability, higher risk
- **Recommendation:** NOT RECOMMENDED - destroys key value proposition

**VE Option 3: Lower Voltage Generators (480V vs. 13.8 kV)**
- **Savings potential:** ~$50/kW × 57.6 MW = -$2.9M in generator costs
- **Trade-off:** Requires step-up transformers, increased complexity, more copper, higher losses
- **Net impact:** Generator savings offset by transformer costs (~$1-1.5M), minimal net benefit
- **Recommendation:** NOT RECOMMENDED - 13.8 kV is optimal for this scale

**VE Option 4: VRLA Batteries vs. Lithium-Ion**
- **Savings potential:** -$200/kWh on battery systems (upfront capex)
- **Trade-off:** Shorter lifespan (5-7 yrs vs. 10-15 yrs), lower efficiency, higher OPEX
- **10-year TCO:** Lithium-ion is lower despite higher upfront cost
- **Recommendation:** NOT RECOMMENDED - lithium-ion has better lifecycle economics

**VE Option 5: Phase 1 Only, Defer Future Phases**
- **Savings potential:** Deploy only 6 MW (Phase 1): $15.9-32.5M electrical capex
- **Trade-off:** Must secure tenant commitment before expanding (reduces speculative risk)
- **Recommendation:** RECOMMENDED - aligns capex with revenue, reduces stranded capital risk

**Recommendation 5: Finalize LV Transformer Count and Sizing** 🔧

**Current Status:** Placeholder estimate of $1.8-4.0M for LV transformers, count TBD

**Required Engineering:**
1. Determine transformer strategy:
   - **Option A:** One transformer per E-House (16 transformers total @ 2.4 MVA each = 38.4 MVA)
   - **Option B:** Centralized transformer bank (11 transformers @ 3.5 MVA as currently spec'd)
   - **Option C:** Hybrid approach (transformers outside E-Houses, distribution inside)
2. Confirm whether transformers are:
   - **Inside E-Houses** (included in turnkey E-House pricing)
   - **Outside E-Houses** on separate pads (separate line item)
3. Update single-line diagram (SLD) to reflect transformer locations and counts

**Impact on estimate:** Current placeholder is reasonable, but count confirmation affects E-House vs. separate transformer budget allocation

**Recommendation 6: Eliminate the $400-700/kW Benchmark from Marketing Materials** ⚠️

**Issue:** The $400-700/kW benchmark is incomplete and does not represent total electrical system costs.

**Corrected benchmarks for communication:**
- **Electrical systems:** $2,800-5,400/kW (40-45% of total data center cost)
- **Total data center:** $6,000-12,000/kW (all divisions, greenfield)
- **Optimized hyperscale:** $6,000/kW (experienced builders, minimal support infrastructure)

**Use in presentations:**
- "Our electrical system estimate of $2,950-5,288/kW is within industry norms of $2,800-5,400/kW for Tier III data center electrical infrastructure."

---

#### Phase 1 Budget Refinement Actions (Target: ±15% confidence)

**Engineering & Design:**
1. ✅ Complete 60% electrical design documents
2. ✅ Finalize single-line diagram (SLD) with all equipment counts and locations
3. ✅ Complete transformer sizing and location study
4. ✅ Prepare detailed E-House technical specifications for RFQ

**Vendor Engagement:**
1. ✅ Obtain budget quotes from 3+ MV generator manufacturers (Caterpillar, Cummins, MTU)
2. ✅ Obtain budget quotes from 3+ E-House manufacturers (Eaton, Schneider, PowerHouse, DRS, Ermco)
3. ✅ Obtain budget quotes from 2+ substation contractors for 161 kV substation
4. ✅ Obtain preliminary pricing from UPS vendors (Schneider, Eaton, Vertiv) for modular systems

**Cost Validation:**
- Compare vendor quotes against estimate ranges
- Revise estimate based on actual market pricing
- Identify value engineering opportunities
- Update confidence level to ±15% once quotes received

**Timeline:** 4-6 weeks for budget quote collection and evaluation

---

#### Long-Term Actions (Phase 2-4 Planning)

1. **Equipment Standardization:** Select single manufacturer for generators, UPS, E-Houses to achieve volume pricing and operational consistency
2. **Phasing Optimization:** Model capex deployment scenarios based on customer contract pipeline
3. **Procurement Strategy:** Consider pre-purchasing long-lead equipment (generators, E-Houses) at Phase 1 pricing to lock in costs for future phases
4. **Financing:** Use refined estimate for debt financing, equity raise, or power purchase agreements (PPAs)

---

## 12.9 SOFT COSTS (TO BE INTEGRATED INTO AGGREGATED PROJECT BUDGET)

**⚠️ NOTE:** This section documents soft cost research and multipliers for project planning purposes. These costs are **NOT included in the equipment cost estimates in Section 12.3**. Soft costs will be applied at the **aggregated project budget level** across all divisions (electrical, mechanical, fire protection, architectural, site/civil).

---

### 12.9.1 Labor & Installation

**Cost Range:** **18-33% of equipment cost** (typical: 25%)

**Breakdown:**
- **Installation labor (field work):** 15-25% of equipment cost
  - Cable pulling, terminations, testing, connections
  - Setting E-Houses, generators, transformers on pads
  - Panel installations, grounding, conduit installation
  - Equipment startup and integration

- **Electrical Contractor (EC) Overhead & Profit:** 3-8% of equipment cost
  - Typically 17.5% markup on labor costs
  - Supervision, project management, tools, mobilization
  - Insurance, bonds, warranty administration
  - Contractor profit margin

**Confidence Level:** ±25% (Medium)

---

#### Research Findings: Why Data Centers Have Lower Labor Costs

**Prefabricated Equipment Advantage:**
- **Prefab electrical equipment:** 10-20% labor fraction (very low)
- **Traditional field-built electrical:** 50-60% labor fraction (very high)
- **Data center equipment is prefab-heavy:**
  - E-Houses: Factory-built, tested, and shipped complete
  - UPS modules: Pre-assembled and factory-tested
  - Generators: Complete units on skids with integrated controls
  - Transformers: Factory-assembled pad-mounted units
  - Switchgear: Pre-assembled and tested at manufacturer

**Industry Data:**
- One data center project reduced labor costs by **60%** using prefabricated conduit vs. field-built
- General electrical work: "Expect to pay 4-5× more for labor than materials" (50-80% labor)
- Data center electrical: 18-33% labor due to factory prefabrication

**Labor Burden Rates (Fully-Burdened Labor Cost):**
- Electrical contractors: 28-65% burden on top of base wages
- Texas specialty subcontractors: 20-30% burden typical
- Includes: Payroll taxes, workers' comp, health insurance, 401(k), PTO, training
- Example: $30/hr base wage + 25% burden = $40/hr fully-burdened rate

**Division-Specific Labor Rates:**

| Division | Labor % of Equipment | Notes |
|----------|---------------------|-------|
| **Electrical (Div 26)** | 18-33% (typical 25%) | Prefab-heavy: E-Houses, UPS, generators |
| **Mechanical (Div 23)** | 30-45% (typical 40%) | More field assembly: piping, ductwork, controls |
| **Fire Protection (Div 21)** | 35-50% (typical 45%) | Field installation: sprinkler piping, testing |
| **Architectural (Div 00)** | 40-60% (typical 50%) | Labor-intensive: finishes, framing, doors |
| **Site/Civil (Div 33)** | 25-40% (typical 35%) | Equipment-heavy: excavation, paving, utilities |

**Sources:**
- Construction Physics - "Construction Cost Breakdown and Partial Industrialization" (2024)
- Knowify - "Electrical Contractors Guide to Job Costing" (2024)
- Buildforce - "What is Labor Burden for Trade Contractors" (March 2024)
- RSMeans 2024 Electrical Cost Data
- Electrical contractor forums and industry benchmarks

---

### 12.9.2 Engineering & Design

**Cost Range:** **4.5-5% of equipment cost**

**Scope:**

1. **Electrical Engineering (EE) Firm - 3.5-4%**
   - Detailed design: MV/LV distribution, one-line diagrams, panel schedules
   - Lighting design, grounding design, arc flash analysis
   - Short circuit and protective device coordination studies
   - Load calculations and transformer sizing
   - NEC compliance and code review
   - Construction documents and specifications
   - Permitting coordination with AHJ

2. **Specialty Consultants - 1.0-1.5%**
   - 161 kV substation design (high voltage engineering)
   - SCADA system programming and integration
   - Utility interconnection engineering and coordination
   - Relay coordination and protection studies
   - Self-healing dual-ring topology design (complex)

3. **Value Engineering - 0.3-0.5%**
   - Post-30% design review
   - Post-60% design review
   - Cost optimization studies
   - Constructability reviews

4. **Owner's Electrical Consultant - 0.4-0.6%**
   - Independent third-party design review
   - QA/QC oversight
   - Constructability and operability reviews
   - Standards compliance verification

**Confidence Level:** ±20% (Medium-High)

**Notes:**
- Tier III N+1 redundancy and 13.8 kV self-healing dual-ring topology add design complexity
- 161 kV substation requires specialized high-voltage engineering expertise
- Data center electrical design is more complex than typical commercial buildings (4.5-5% vs. 2-3% typical)

**Sources:**
- Appendix - Phase 4 Electrical Equipment and Cost Analysis (internal document)
- Industry standard: 3-5% for data center MEP design
- AIA B101 Standard Form of Agreement (typical architect/engineer fees)

---

### 12.9.3 Commissioning & Testing

**Cost Range:** **3-4% of equipment cost** (industry standard: 2-5%)

**Scope:**

1. **Independent Commissioning Agent (CxA) - 2.5-3%**
   - Design phase review (30%, 60%, 90% reviews)
   - Factory Acceptance Testing (FAT) witness at manufacturer facilities
   - Site Acceptance Testing (SAT) oversight during installation
   - Integrated Systems Testing (IST) coordination
   - Functional performance testing
   - Final commissioning report and O&M documentation
   - Continuous oversight from design through completion

2. **Factory Acceptance Testing (FAT) - 0.3-0.5%**
   - Travel and testing at manufacturer facilities
   - Witness testing for major equipment:
     - 13.8 kV generators (16 units, 48-52 week lead time)
     - UPS modules (32 units, 1.0 MW / 1,250 kVA each)
     - 161 kV substation transformers (2 units, 52 week lead time)
     - MV/LV switchgear and E-Houses (16 RMUs, 16 LV switchboards)
   - Review of factory test reports and certifications

3. **Site Acceptance Testing (SAT) - 0.4-0.6%**
   - On-site functional testing after installation
   - Point-to-point verification of all systems
   - Control system verification and SCADA testing
   - Protective relay testing and coordination verification
   - Documentation of as-built conditions

4. **Integrated Systems Testing (IST) - 0.3-0.5%**
   - Full facility load testing with load banks
   - Generator paralleling and load transfer testing
   - UPS transfer and failover scenarios
   - Emergency power off (EPO) testing
   - Dual-ring self-healing topology validation
   - 72-hour burn-in test at full load

5. **Uptime Institute Tier III Certification - ~$350K (0.3-0.5%)**
   - Design review for Tier III compliance
   - Construction oversight and inspections
   - Final certification audit
   - Tier III Certificate of Compliance
   - Third-party validation of concurrent maintainability

**Confidence Level:** ±20% (Medium-High)

**Notes:**
- Commissioning is critical for Tier III data centers to validate N+1 redundancy and concurrent maintainability
- Industry standard: 2-5% of construction cost for commissioning
- Data centers require more rigorous testing than typical commercial buildings
- Independent CxA (not affiliated with contractor) is required for Tier III certification

**Sources:**
- Appendix - Phase 4 Electrical Equipment and Cost Analysis (internal document)
- Uptime Institute - Tier III certification requirements
- ASHRAE Guideline 0 - The Commissioning Process
- Industry benchmarks for data center commissioning

---

### 12.9.4 Contingency

**Cost Range:** **12.5% of base cost** (design + construction contingency combined)

**Breakdown:**

1. **Design Contingency - 5.0%**
   - Allowance for design development and scope refinements
   - Unknown site conditions discovered during design
   - Equipment specification changes
   - Code or regulatory requirement changes
   - Covers changes during 30% → 60% → 90% → 100% design progression

2. **Construction Contingency - 7.5%**
   - Field issues and unforeseen site conditions
   - Equipment substitutions or long-lead equipment delays
   - Change orders during construction
   - Testing failures requiring rework
   - Weather delays and schedule impacts
   - Industry standard for data center electrical: 7-10%

**Total Combined Contingency: 12.5%**

**Confidence Level:** ±10% (High) - Industry standard is well-established

**Notes:**
- Contingency is applied to base cost (equipment + labor + engineering + commissioning)
- Contingency is typically drawn down to 3-5% remaining at project completion
- Some owners separate design contingency (released at 100% CDs) from construction contingency
- Tier III data centers require lower contingency than Tier IV (less design complexity)
- Pre-fabricated equipment (E-Houses, modular UPS) reduces field contingency risk

**Industry Benchmarks:**
- Data center electrical: 10-15% combined contingency
- Commercial electrical: 5-10% combined contingency
- Mission-critical facilities: 12-18% combined contingency

**Sources:**
- Appendix - Phase 4 Electrical Equipment and Cost Analysis (internal document)
- AACE International - Contingency estimation guidelines
- Industry practice for data center construction

---


---


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