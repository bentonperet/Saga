

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



---

## 12.0 COST AND EQUIPMENT SUMMARY

### 12.1 ESTIMATION METHODOLOGY

**Approach:** Cost per kilowatt ($/kW) based on IT load capacity

This estimate uses industry-confirmed benchmarks for Tier III data center electrical systems, organized into seven major equipment categories. Rather than line-item pricing, we apply validated cost ranges ($/kW) to the IT load capacity and back into total project costs by 6MW block.

**Key Definitions:**
- **IT Load:** Power consumed by servers/storage/network equipment (critical load)
- **Facility Load:** IT load × PUE = Total electrical load including cooling, lighting, UPS losses
- **PUE:** 1.6 (electrical sizing), 1.4 (average operating target)
- **6MW Block:** One modular deployment unit = 6 MW IT load = 9.6 MW facility load @ 1.6 PUE

**Scope:**
- **Included:** All electrical equipment from 161 kV substation through cabinet PDUs (CSI Division 26)
- **Excluded:** Mechanical equipment (chillers, pumps - Division 23), Fire protection (Division 21), BMS/DCIM (Division 25), Site electrical duct banks (Division 33)

---

### 12.2 EQUIPMENT CATEGORIES & INDUSTRY RANGES

#### Category 1: Utility Service & 161 kV Substation

**Equipment Included:**
- Customer-owned 161 kV substation infrastructure
- 2×35 MVA power transformers (161kV/13.8kV, N+1 redundancy)
- Utility metering and protection
- Substation grounding and lightning protection
- Substation control building

**Industry Range:** **$4-8M** (complete substation serving 20-40 MW facility)
**Alternative Basis:** $150-300/kW (facility load) = $5.8-11.5M for 38.4 MW

**Phasing:** Installed Phase 1, sized for full 38.4 MW Phase 4 capacity

---

#### Category 2: Medium Voltage Distribution (13.8 kV)

**Equipment Included:**
- 13.8 kV dual-ring distribution infrastructure
- 8 Ring Main Units (RMUs) with SF6 or vacuum breakers (630A, 20 kA rating)
- MV switchboards (count TBD based on final design)
- SCADA control system for self-healing ring topology
- MV cable, terminations, and accessories

**Industry Range:** **$50-100/kW** (facility load)

**Calculation (Phase 4):**
- 38.4 MW facility load × $50-100/kW = **$1.9-3.8M**

**Phasing:** Ring infrastructure installed Phase 1, switchgear/SCADA added per block

---

#### Category 3: Generator System (13.8 kV)

**Equipment Included:**
- Diesel generators @ 13.8 kV (3.6 MW continuous rating each)
- Generator switchgear and paralleling controls
- Fuel systems (day tanks, distribution piping)
- Generator pads and foundations
- Exhaust systems and sound attenuation
- EPA Tier 4 Final emissions controls

**Industry Range:** **$150-250/kW** (nameplate generator capacity)

**Calculation by Phase (N+1 per 6MW block):**

| Phase | IT Load | Facility Load @ 1.6 PUE | Generators (3.6 MW) | Total Capacity | Cost Range @ $150-250/kW |
|-------|---------|------------------------|---------------------|----------------|--------------------------|
| **1** | 6 MW | 9.6 MW | 4 units (N+1) | 14.4 MW | $2.2-3.6M |
| **2** | 12 MW | 19.2 MW | 8 units (N+1) | 28.8 MW | $4.3-7.2M |
| **3** | 18 MW | 28.8 MW | 12 units (N+1) | 43.2 MW | $6.5-10.8M |
| **4** | 24 MW | 38.4 MW | 16 units (N+1) | 57.6 MW | **$8.6-14.4M** |

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

**Calculation by Phase (N+1 modular):**

| Phase | IT Load | UPS Modules (1,250 kVA) | Configuration | Cost Range @ $100-200/kW |
|-------|---------|-------------------------|---------------|--------------------------|
| **1** | 6 MW | 7 units | 6+1 (N+1) | $0.6-1.2M |
| **2** | 12 MW | 13 units | 12+1 (N+1) | $1.2-2.4M |
| **3** | 18 MW | 19 units | 18+1 (N+1) | $1.8-3.6M |
| **4** | 24 MW | 25 units | 24+1 (N+1) | **$2.4-4.8M** |

**Phasing:** UPS modules added per 6MW block to maintain N+1 redundancy

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

**Summary Table:**

| Phase | IT Load | Category 1 | Category 2 | Category 3 | Category 4 | Category 5 | Category 6 | Category 7 | **TOTAL RANGE** |
|-------|---------|------------|------------|------------|------------|------------|------------|------------|-----------------|
| **1** | 6 MW | $4.0-8.0M | $0.5-1.0M | $2.2-3.6M | $0.5-1.0M | $0.6-1.2M | $6.6-15.2M | $1.5-2.5M | **$15.9-32.5M** |
| **2** | 12 MW | $4.0-8.0M | $1.0-1.9M | $4.3-7.2M | $0.9-2.0M | $1.2-2.4M | $13.2-30.4M | $2.0-3.5M | **$26.6-55.4M** |
| **3** | 18 MW | $4.0-8.0M | $1.4-2.9M | $6.5-10.8M | $1.4-3.0M | $1.8-3.6M | $19.8-45.6M | $2.5-4.5M | **$37.4-78.4M** |
| **4** | 24 MW | $4.0-8.0M | $1.9-3.8M | $8.6-14.4M | $1.8-4.0M | $2.4-4.8M | $26.4-60.8M | $3.0-6.0M | **$48.1-101.8M** |

**Cost per kW (Phase 4):**
- Low estimate: $48.1M ÷ 24,000 kW = **$2,004/kW**
- High estimate: $101.8M ÷ 24,000 kW = **$4,242/kW**
- **Midpoint: ~$3,123/kW**

---

### 12.4 INDUSTRY BENCHMARK VALIDATION

**Target Range:** $400-700/kW (IT load) for complete Tier III electrical system

**Our Estimate:** $2,004-4,242/kW (midpoint $3,123/kW)

**Position Analysis:**

| Source | Benchmark | Our Estimate | Position |
|--------|-----------|--------------|----------|
| Industry (Tier III all-in) | $400-700/kW | $2,004-4,242/kW | +186-506% ⚠️ |

**⚠️ ESTIMATE SIGNIFICANTLY EXCEEDS INDUSTRY BENCHMARK**

**Likely Causes:**
1. **E-House cost dominance:** Category 6 ($26.4-60.8M) represents 55-60% of total estimate
   - High estimate uses $3.5M per E-House (turnkey premium)
   - Industry benchmarks may assume stick-built electrical rooms, not prefab E-Houses
   - **Recommendation:** Obtain competitive E-House quotes; consider stick-built alternative

2. **Component over-specification or double-counting:**
   - Verify E-House scope doesn't duplicate Categories 2, 5 (MV dist, UPS already in E-Houses)
   - Confirm whether industry $/kW benchmarks include or exclude E-House enclosures

3. **Category 4 (LV Transformers) pending confirmation:**
   - Transformer count/sizing needs verification
   - May be over-estimated or under-estimated pending final design

**Required Actions:**
1. **Research E-House vs. stick-built cost differential** (may be $1-1.5M premium per E-House)
2. **Clarify scope overlap** between Categories 2/5/6 (avoid double-counting MV switchgear, UPS)
3. **Obtain budget quotes** for 3+ E-House manufacturers
4. **Validate transformer sizing** for 6MW block architecture
5. **Research additional sources** for $/kW benchmarks specific to 13.8 kV MV distribution architecture

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

1. **Internal:** [[zEstimating Methods - Data Center Cost Research]] (Division 26 section)
2. **Uptime Institute:** "Data Center Capital Cost Survey 2024" (Tier III electrical costs)
3. **Cushman & Wakefield:** "Data Center Development Cost Guide 2025" (Electrical $/kW ranges)
4. **Schneider Electric (APC):** White papers on UPS sizing and electrical distribution
5. **IEEE 141 (Red Book):** Electric Power Distribution standards
6. **Equipment Manufacturers:** Caterpillar, Cummins, Eaton, Vertiv (reference specifications)

**Additional Research Required:**
- E-House manufacturers (budget pricing)
- Data center case studies with 13.8 kV MV distribution
- Updated $/kW benchmarks specific to MV distribution architecture

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

### 12.8 NEXT STEPS

**Immediate Actions (Before Phase 1 Procurement):**
1. ✅ **WebSearch:** Research E-House costs vs. stick-built electrical rooms
2. ✅ **WebSearch:** Find 2024-2025 case studies for data centers with 13.8 kV MV distribution
3. ✅ **Obtain quotes:** Contact 3+ E-House manufacturers for budget pricing (4 units, Phase 1)
4. ✅ **Engineering:** Finalize LV transformer count/sizing for 6MW block architecture
5. ✅ **Clarify scope:** Define E-House internal equipment scope to avoid category overlaps
6. ✅ **Update SLD:** Complete single-line diagram with all equipment counts

**Phase 1 Budget Refinement (Target: ±15% confidence):**
- Complete 60% electrical design documents
- Obtain preliminary quotes for Phase 1 equipment (4 generators, 4 E-Houses, 7 UPS modules)
- Validate $/kW ranges against vendor quotes
- Revise estimate based on actual market pricing

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