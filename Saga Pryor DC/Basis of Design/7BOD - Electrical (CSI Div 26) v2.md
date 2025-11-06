**Created:** 2025-11-04
**Project:** Saga Pryor Data Center - PACHYDERM GLOBAL
**Owner:** Saga
**Parent Document:** [[_BOD - Exec Summary]]

# BASIS OF DESIGN - ELECTRICAL (CSI DIVISION 26)
## Pryor Data Center - PACHYDERM GLOBAL

---

## 1.0 OVERVIEW

### 1.1 Project Summary

This Basis of Design defines the electrical infrastructure for a two-hall, 20,000 SF data center with an ultimate IT load of **24 MW** and a total facility load of approximately **30 MW**. The system is designed to meet Tier III standards, providing N+1 component redundancy and dual-path redundancy for all critical loads.

The electrical backbone is a self-healing 13.8 kV dual-ring MV distribution with 8 RMU switchgear and SCADA-controlled automated switching, enabling concurrent maintainability of any transformer or electrical component. The 13.8 kV common bus allows for flexible integration of utility power, backup generators, solar arrays, and battery energy storage systems.

**Key Infrastructure:**
- Customer-owned 345 kV substation with 2×35 MVA transformers (N+1 redundancy)
- Self-healing 13.8 kV dual-ring distribution (8 RMUs, SCADA-controlled) providing path redundancy
- 9×4.0 MW diesel generators @ 13.8 kV (N+1 for 30 MW facility load)
- 11×3,500 kVA LV transformers, 13.8kV/480V (N+1 redundancy with concurrent maintainability)
- N+1 UPS architecture: 25 modular UPS units (1,250 kVA each) at Phase 4, with path redundancy from MV dual-ring
- Prefabricated Power Delivery Modules (PDMs) for accelerated schedule

### 1.2 Design Philosophy

- **Availability:** Tier III (Concurrent Maintainability). Any single electrical component can be removed for maintenance without impacting IT operations.
- **Component Redundancy:** N+1 for all core infrastructure (Substation Transformers, Generators, LV Transformers, IT UPS modules, and Mechanical UPS).
- **Path Redundancy:** Dual (A/B) path diversity from the MV dual-ring distribution through independent transformer banks, switchboards, and distribution panels to dual-PDUs in each cabinet. Self-healing 13.8 kV dual-ring with SCADA-controlled automated switching provides path reconfiguration without human intervention, eliminating the need for duplicate UPS systems.
- **UPS Architecture:** N+1 modular UPS provides component redundancy (can lose one module), while the self-healing MV dual-ring provides path redundancy. This approach delivers Tier III concurrent maintainability with significantly lower CAPEX than traditional 2N UPS systems (~50% reduction in UPS module count).
- **Concurrent Maintainability:** Self-healing dual-ring topology enables isolation of any transformer or ring segment for maintenance while maintaining full N+1 redundancy on alternate path. 8 RMU switchgear with automated SCADA controls ensure continuous operation during maintenance activities.
- **Phasing Strategy:** All infrastructure (substation, generator pads, PDM pads, electrical yard, conduit rough-in) shall be designed and built for the 30 MW full build-out from day 1. Capital equipment (generators, transformers, UPS modules, mechanical UPS) will be purchased and commissioned in phases to match IT load growth.
- **Prefabricated Construction:** Prefabricated Power Delivery Modules (PDMs) containing LV switchboards, UPS systems, battery cabinets, and distribution panels provide 8-12 week schedule acceleration and factory-tested quality.

## 2.0 UTILITY SERVICE & SUBSTATION

### 2.1 System Topology

The following diagram illustrates the overall electrical system architecture, showing the dual-path (A/B) power distribution from utility service through the 13.8 kV dual-ring to the data center loads:

```
                     UTILITY GRID (Kamo Power Electric Co-op)
                              │
        ┌─────────────────────┴─────────────────────┐
        │  345 kV TRANSMISSION (or 161 kV option)   │
        │       Revenue Metering @ HV Side          │
        └───────────┬───────────────────┬───────────┘
                    │                   │
              [XFMR-SUB-A]        [XFMR-SUB-B]
              35 MVA              35 MVA
              345kV/13.8kV        345kV/13.8kV
                    │                   │
        ┌───────────┴───────────────────┴───────────┐
        │      13.8 kV COMMON BUS (Dual-Ring)       │
        │    ┌──────────────────────────────┐       │
        │    │  RING A  │  │  RING B        │       │
        │    │ (RMU-1A  │  │ RMU-1B)        │       │
        │    │  RMU-2A  │  │ RMU-2B         │       │
        │    │  RMU-3A  │  │ RMU-3B         │       │
        │    │  RMU-4A  │  │ RMU-4B)        │       │
        │    └──────────────────────────────┘       │
        │                                            │
        ├─── Generators: 9×4.0 MW @ 13.8 kV        │
        ├─── Solar: 8+ MW DC (inverters @13.8kV)   │
        ├─── BESS: 4-8 MWh (inverters @13.8kV)     │
        └────────────────┬──────────────────────────┘
                         │
        ┌────────────────┴────────────────┐
        │                                 │
   [XFMR Bank A]                    [XFMR Bank B]
   13.8kV/480V                      13.8kV/480V
   (N+1 transformers)               (N+1 transformers)
        │                                 │
    [SWBD-A]                          [SWBD-B]
        │                                 │
        └────────────┬────────────────────┘
                     │
              [UPS Modules]
             25×1,250 kVA (N+1)
             24 MW IT capacity
                     │
        ┌────────────┴────────────────┐
        │                             │
   [Panel-A]                      [Panel-B]
        │                             │
        └────────────┬────────────────┘
                     │
              ┌──────┴──────┐
              │   RACK      │
              │ [PDU-A] [PDU-B] │
              └─────────────┘
```

### 2.2 Utility Interconnection

**Utility Provider:** Kamo Power Electric Co-op

**Available Substations:**
- **Sportsman Substation (SW):** 345 kV, 3 lines
- **Dry Gulch Substation (N):** 161 kV, 2 lines

**Primary Service:**
- **Voltage:** 345 kV (preferred) or 161 kV, based on final utility interconnection study, capacity analysis, and cost comparison
- **Configuration:** Customer-owned and maintained substation constructed on-site
- **Metering:** Utility revenue-grade metering at transmission voltage point of interconnection
- **Capacity:** 35 MVA minimum service capacity
- **Protection:** Distance relay, differential protection, overcurrent per utility interconnection standards

### 2.3 Substation Transformers

**Configuration:** N+1 Redundancy - Either transformer capable of supporting full 30 MW facility load

| Parameter    | Specification                                |
| ------------ | -------------------------------------------- |
| **Quantity** | Two (2) transformers                         |
| **Rating**   | 35 MVA each @ 345kV/13.8kV (or 161kV/13.8kV) |

## 3.0 MEDIUM VOLTAGE (13.8 KV) DISTRIBUTION

### 3.1 13.8 kV Common Bus

A 13.8 kV "common bus" infrastructure serves as the single voltage platform for all power sources and loads:
- Utility power (from 2×35 MVA substation transformers)
- Backup generators (9×4.0 MW @ 13.8 kV)
- Solar array (8+ MW DC, inverters output 13.8 kV AC directly)
- Battery Energy Storage (4-8 MWh, inverters output 13.8 kV AC directly)
- Data center critical IT and mechanical loads (via 13.8kV/480V transformers)

### 3.2 MV Dual-Ring Topology

The following diagram shows the self-healing 13.8 kV dual-ring architecture with 8 RMU switchgear and A/B transformer bank connections:

```
    SUBSTATION XFMR-A (35 MVA)    SUBSTATION XFMR-B (35 MVA)
              │                              │
    ┌─────────┴────────┐         ┌──────────┴─────────┐
    │                  │         │                    │
┌───┴───┐          ┌───┴───┐ ┌───┴───┐          ┌───┴───┐
│RMU-1A │══════════│RMU-2A │ │RMU-1B │══════════│RMU-2B │
└───┬───┘  RING A  └───┬───┘ └───┬───┘  RING B  └───┬───┘
    │                  │         │                    │
  [XFMR-A1]        [XFMR-A2]  [XFMR-B1]          [XFMR-B2]
  13.8kV/480V      13.8kV/480V 13.8kV/480V       13.8kV/480V
    │                  │         │                    │
┌───┴───┐          ┌───┴───┐ ┌───┴───┐          ┌───┴───┐
│RMU-3A │══════════│RMU-4A │ │RMU-3B │══════════│RMU-4B │
└───┬───┘          └───┬───┘ └───┬───┘          └───┬───┘
    │                  │         │                    │
  [XFMR-A3]        [XFMR-A4]  [XFMR-B3]          [XFMR-B4]
    │                  │         │                    │
    └──────────────────┴─────────┴────────────────────┘
                       │
            ┌──────────┴──────────┐
            │                     │
        Generators (9×4MW)    Solar + BESS
        @ 13.8 kV             @ 13.8 kV
```

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
- **Topology:** The 24 MW IT load (Phase 4) will be protected by 25 UPS modules (24+1 for N+1) with power distributed via dual A/B paths to dual-corded IT equipment
- **Tier III Compliance:** Meets Uptime Institute Tier III concurrent maintainability requirements through combination of N+1 UPS component redundancy and dual-path MV distribution

### 6.2 System Sizing (Phase 4)

- **IT Load:** 24 MW (24,000 kW)
- **UPS Modules:** 25 × 1,250 kVA modules
  - N = 24 modules (24 × 1 MW = 24 MW capacity)
  - N+1 = 25 modules total
  - Operating load: ~83% per module (optimal efficiency range of 80-90%)
- **N+1 Verification:** 24 running modules = 24 MW capacity = full IT load ✓

### 6.3 Path Redundancy Philosophy

**Path diversity is provided by the 13.8 kV self-healing dual-ring MV distribution, not by duplicate UPS systems:**

- **Path A:** `MV Ring A -> XFMRs-A -> SWBD-A -> UPS Modules (distributed) -> Panel-A -> Cabinet PDU-A`
- **Path B:** `MV Ring B -> XFMRs-B -> SWBD-B -> UPS Modules (distributed) -> Panel-B -> Cabinet PDU-B`

**Key Design Features:**
- Dual-corded IT equipment receives power from both A and B paths, fed from different MV ring segments
- Loss of any single MV ring segment, transformer, switchboard, or distribution path does not impact IT operations
- UPS modules can be distributed across both paths or configured in a common pool with dual output distribution
- Self-healing MV dual-ring automatically reconfigures power paths without human intervention during faults or maintenance

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

| Parameter | Specification |
|-----------|---------------|
| **Quantity** | Two (2): SWBD-A and SWBD-B |
| **Rating** | 4,000A copper busbar, 480V, 3-phase, 4-wire |
| **Short-Circuit** | 65 kA SCCR (Short-Circuit Current Rating) |
| **Source** | SWBD-A fed from MV Ring A transformers; SWBD-B fed from MV Ring B transformers |
| **Configuration** | Dual-path distribution: All critical loads served by both A and B paths |

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


## 12.0 PREFABRICATED POWER DELIVERY MODULES (PDMs)

### 12.1 Configuration

**Quantity:** Two (2) outdoor PDMs for Phase 1, expandable in subsequent phases

**Contents:**
- LV Main Switchboards (SWBD-A and SWBD-B)
- IT UPS Systems (System A and System B with modular UPS modules)
- Battery Cabinets (Lithium-Ion battery arrays for UPS systems)
- Distribution Panels (IT Dist, Mech Dist, UPS Dist - A and B sides)
- Integrated fire suppression, HVAC, and monitoring systems

### 12.2 Benefits

- **Factory Testing:** Complete system factory-tested and commissioned before shipment, reducing field commissioning risk
- **Schedule Acceleration:** 8-12 week schedule acceleration vs. traditional stick-built construction. PDMs can be manufactured in parallel with building construction.
- **Quality Control:** Factory environment provides controlled conditions for assembly, wiring, and testing - higher quality than field construction
- **Simplified Field Installation:** Pre-wired and pre-tested modules require only MV/LV connections and startup - reduces field labor by 30-40%


---

## 13.0 ELECTRICAL PHASING STRATEGY

Electrical infrastructure designed for 30 MW (Phase 4), with equipment added in phases.

---

### 13.1 PHASE 1: 3 MW IT LOAD (30 L2C RACKS)

**Rack Deployment:** 30 racks × L2C @ 100 kW = 3,000 kW IT load

**Load Summary:**

| Load Type | Power (kW) | Description |
|-----------|------------|-------------|
| **IT Load** | 3,000 | 30×L2C racks @ 100 kW each |
| **Mechanical** | 840 | Loop 3 chillers, pumps, CDUs (L2C cooling only) |
| **Building** | 360 | HVAC, lighting, NOC, security, house loads |
| **Total Facility Load** | **~4,200 kW** | **PUE 1.40** |

**Electrical Infrastructure:**

| Equipment           | Quantity  | Sizing Notes                                                      |
| ------------------- | --------- | ----------------------------------------------------------------- |
| **Generators**      | 3×4.0 MW  | N+1 for 4.2 MW (2 running = 8 MW capacity, 90% margin)            |
| **LV Transformers** | 3×3.5 MVA | N+1 for 4.2 MW (2 running = 6.3 MW capacity, 50% margin)          |
| **IT UPS Modules**  | 4 × 1,250 kVA | N+1 for 3 MW IT load (3+1 modules @ ~80% loading) |
| **Mechanical UPS**  | 8×250 kW  | N+1 for 840 kW mechanical load (7 running = 1,750 kW)             |

---

### 13.2 PHASE 2: 6 MW IT LOAD (150 TOTAL RACKS)

**Rack Deployment:**
- 30 racks × L2C @ 100 kW = 3,000 kW
- 120 racks × RDHx @ 25 kW = 3,000 kW
- **Total: 150 racks = 6,000 kW IT load**

**Load Summary:**

| Load Type | Power (kW) | Description |
|-----------|------------|-------------|
| **IT Load** | 6,000 | 3 MW L2C + 3 MW RDHx |
| **Mechanical** | 1,350 | All 3 cooling loops operational |
| **Building** | 360 | Building systems unchanged |
| **Total Facility Load** | **~8,100 kW** | **PUE 1.35** |

**Electrical Infrastructure:**

| Equipment | Phase 2 Total | Add from Phase 1 | Sizing Notes |
|-----------|---------------|------------------|--------------|
| **Generators** | 4×4.0 MW | Add 1 unit | N+1 for 8.1 MW |
| **LV Transformers** | 4×3.5 MVA | Add 1 unit | N+1 for 8.1 MW |
| **IT UPS Modules** | 7 × 1,250 kVA | Add 3 modules | N+1 for 6 MW IT load (6+1 modules @ ~86% loading) |
| **Mechanical UPS** | 12×250 kW | Add 4 modules | N+1 for 1,350 kW |

---

### 13.3 PHASE 3: 15 MW IT LOAD (285 TOTAL RACKS)

**Rack Deployment:**
- 105 racks × L2C @ 100 kW = 10,500 kW
- 180 racks × RDHx @ 25 kW = 4,500 kW
- **Total: 285 racks = 15,000 kW IT load**

**Load Summary:**

| Load Type | Power (kW) | Description |
|-----------|------------|-------------|
| **IT Load** | 15,000 | 10.5 MW L2C + 4.5 MW RDHx |
| **Mechanical** | 3,000 | All loops scaled for higher capacity |
| **Building** | 450 | Building systems at operational capacity |
| **Total Facility Load** | **~19,500 kW** | **PUE 1.30** |

**Electrical Infrastructure:**

| Equipment | Phase 3 Total | Add from Phase 2 | Sizing Notes |
|-----------|---------------|------------------|--------------|
| **Generators** | 6×4.0 MW | Add 2 units | N+1 for 19.5 MW |
| **LV Transformers** | 8×3.5 MVA | Add 4 units | N+1 for 19.5 MW |
| **IT UPS Modules** | 16 × 1,250 kVA | Add 9 modules | N+1 for 15 MW IT load (15+1 modules @ ~94% loading) |
| **Mechanical UPS** | 16×250 kW | Add 4 modules | N+1 for 3,000 kW |

---

### 13.4 PHASE 4: 24 MW IT LOAD (468 TOTAL RACKS) - FULL BUILD-OUT

**Rack Deployment:**
- 168 racks × L2C @ 100 kW = 16,800 kW
- 288 racks × RDHx @ 25 kW = 7,200 kW
- **Total: 468 racks = 24,000 kW IT load**

**Load Summary:**

| Load Type | Power (kW) | Description |
|-----------|------------|-------------|
| **IT Load** | 24,000 | 16.8 MW L2C + 7.2 MW RDHx |
| **Mechanical** | 4,500 | All loops at capacity (Phase 4 chiller deployment complete) |
| **Building** | 500 | Building systems at full capacity |
| **Total Facility Load** | **~30,000 kW** | **PUE 1.25 (optimized at scale)** |

**Electrical Infrastructure:**

| Equipment | Phase 4 Total | Add from Phase 3 | Sizing Notes |
|-----------|---------------|------------------|--------------|
| **Generators** | 9×4.0 MW | Add 3 units | N+1 for 30 MW: 8 running = 32 MW capacity |
| **LV Transformers** | 11×3.5 MVA | Add 3 units | N+1 for 30 MW: 10 running = 31.5 MW capacity |
| **IT UPS Modules** | 25 × 1,250 kVA | Add 9 modules | N+1 for 24 MW IT load (24+1 modules @ ~83% loading) |
| **Mechanical UPS** | 25×250 kW | Add 9 modules | N+1 for 6,000 kW: 24 running = 6,000 kW capacity |

---

### 13.5 PHASING SUMMARY TABLE

**Note:** UPS module counts reflect N+1 architecture (N modules to serve IT load + 1 redundant). Path redundancy provided by 13.8 kV self-healing dual-ring MV distribution.

| **Phase** | **IT MW** | **Racks (L2C/RDHx)** | **PUE** | **Facility MW** | **Generators (4 MW)** | **LV XFMRs (3.5 MVA)** | **IT UPS Modules (1,250 kVA)** |
|-----------|-----------|----------------------|---------|-----------------|------------------------|-------------------------|---------------------------|
| **1** | 3 | 30 (30/0) | 1.40 | ~4.2 | 3 (N+1) | 3 (N+1) | 4 (3+1, N+1) |
| **2** | 6 | 150 (30/120) | 1.35 | ~8.1 | 4 (N+1) | 4 (N+1) | 7 (6+1, N+1) |
| **3** | 15 | 285 (105/180) | 1.30 | ~19.5 | 6 (N+1) | 8 (N+1) | 16 (15+1, N+1) |
| **4** | 24 | 468 (168/288) | 1.25 | ~30.0 | 9 (N+1) | 11 (N+1) | 25 (24+1, N+1) |

---

## 14.0 COST IMPACTS & CAPEX SAVINGS

### 14.1 UPS System Costs (N+1 Architecture)

**Estimated UPS CAPEX by Phase:**

| Phase | UPS Modules | Total UPS Capacity | Estimated Cost | Incremental Cost |
|-------|-------------|-------------------|----------------|------------------|
| **Phase 1** | 4 × 1,250 kVA | 4 MW (3+1, N+1) | $3.0-3.5M | $3.0-3.5M |
| **Phase 2** | 7 × 1,250 kVA | 7 MW (6+1, N+1) | $5.3-6.0M | $2.3-2.5M |
| **Phase 3** | 16 × 1,250 kVA | 16 MW (15+1, N+1) | $12.0-13.5M | $6.7-7.5M |
| **Phase 4** | 25 × 1,250 kVA | 25 MW (24+1, N+1) | $18.8-21.0M | $6.8-7.5M |

**Pricing Assumptions:**
- $750K-$850K per UPS module (1,250 kVA, including batteries)
- Lithium-ion batteries (10-15 year life, 5-minute runtime)
- Factory integration and commissioning included

### 14.2 CAPEX Savings vs 2N UPS Architecture

**Comparison: N+1 vs 2N UPS Systems**

| Phase | N+1 Modules | 2N Modules | Module Reduction | Cost Savings |
|-------|-------------|------------|------------------|--------------|
| **Phase 1** | 4 | 6 | 2 modules (33%) | $1.5-1.7M |
| **Phase 2** | 7 | 10 | 3 modules (30%) | $2.3-2.5M |
| **Phase 3** | 16 | 18 | 2 modules (11%) | $1.5-1.7M |
| **Phase 4** | 25 | 26 | 1 module (4%) | $0.8-0.9M |
| **Total Savings** | - | - | **8 modules** | **$6.1-6.8M** |

**Additional Lifecycle Savings:**
- Battery replacement cycles (15-year facility life):
  - VRLA batteries: 2 replacement cycles = additional savings of ~$1.6-1.8M
  - Li-ion batteries: 1 replacement cycle = additional savings of ~$0.8-0.9M
- Reduced footprint: ~15-20% less PDM space required
- Lower maintenance labor: Fewer modules to service

**Total NPV Savings (N+1 vs 2N):** $7-8M over facility lifecycle

### 14.3 Total Electrical System Costs

| System Component | Phase 1 | Ultimate (Phase 4) | Notes |
|------------------|---------|-------------------|-------|
| **UPS Systems** | $3.0-3.5M | $18.8-21.0M | N+1 modular architecture |
| **Generators** | $3.0-3.5M | $9.0-10.5M | 9 × 4 MW diesel @ 13.8 kV |
| **LV Transformers** | $1.5-1.8M | $5.5-6.5M | 11 × 3,500 kVA oil-filled |
| **Substation** | $8.0-10.0M | $8.0-10.0M | 345 kV/13.8 kV, 2×35 MVA (built Phase 1) |
| **MV Distribution** | $2.0-2.5M | $2.0-2.5M | 8 RMUs, dual-ring (built Phase 1) |
| **LV Distribution** | $2.5-3.0M | $6.0-7.0M | Switchboards, panels, busway |
| **PDMs (Prefab Modules)** | $2.0-2.5M | $5.0-6.0M | Climate-controlled enclosures |
| **Mechanical UPS** | $0.6-0.8M | $1.9-2.2M | N+1 for critical mechanical loads |
| **Total Electrical CAPEX** | **$22.6-27.6M** | **$56.2-65.7M** | Phased deployment |

**Key Design Advantages:**
- ✅ N+1 UPS saves $7-8M vs 2N architecture
- ✅ Tier III compliance maintained (dual MV ring provides path redundancy)
- ✅ Higher module utilization (80-90%) improves efficiency vs 2N (40-50%)
- ✅ Bankable design - industry-standard N+1 topology with dual-path MV distribution
- ✅ Phased deployment optimizes cash flow and IRR

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
- **Date Updated:** 2025-11-04
- **Prepared by:** PGCIS Team
- **Key Updates:**
  - Updated for 468-rack deployment (168 L2C + 288 RDHx)
  - Detailed 4-phase buildout to 30 MW facility load
  - All equipment properly sized for facility load (IT × PUE)
  - Added comprehensive phasing narratives with load tables
  - Enhanced solar/BESS integration details