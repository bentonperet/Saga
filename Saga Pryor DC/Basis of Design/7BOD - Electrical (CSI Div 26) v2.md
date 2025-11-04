**Created:** 2025-11-04
**Project:** Saga Pryor Data Center - PACHYDERM GLOBAL
**Owner:** Saga
**Parent Document:** [[_BOD - Exec Summary]]
**Tags:** #pryor-dc #electrical #csi-div-26 #bod #tier-iii #2n-architecture

# BASIS OF DESIGN - ELECTRICAL (CSI DIVISION 26)
## Pryor Data Center - PACHYDERM GLOBAL

---

## 1.0 OVERVIEW

### 1.1 Project Summary

This Basis of Design defines the electrical infrastructure for a two-hall, 20,000 SF data center with an ultimate IT load of **24 MW** and a total facility load of approximately **30 MW**. The system is designed to meet Tier III standards, providing N+1 component redundancy and 2N path redundancy for all critical loads.

The electrical backbone is a **self-healing 13.8 kV dual-ring MV distribution** with **8 RMU switchgear** and **SCADA-controlled automated switching**, enabling concurrent maintainability of any transformer or electrical component. The 13.8 kV common bus allows for flexible integration of utility power, backup generators, solar arrays, and battery energy storage systems.

**Key Infrastructure:**
- Customer-owned 345 kV substation with 2×35 MVA transformers (N+1 redundancy)
- Self-healing 13.8 kV dual-ring distribution (8 RMUs, SCADA-controlled)
- 9×4.0 MW diesel generators @ 13.8 kV (N+1 for 30 MW facility load)
- 11×3,500 kVA LV transformers, 13.8kV/480V (N+1 redundancy with concurrent maintainability)
- 2N UPS architecture: Two independent 12 MW (N+1) UPS systems (26 modules total)
- Prefabricated Power Delivery Modules (PDMs) for accelerated schedule

### 1.2 Design Philosophy

- **Availability:** Tier III (Concurrent Maintainability). Any single electrical component can be removed for maintenance without impacting IT operations.
- **Component Redundancy:** N+1 for all core infrastructure (Substation Transformers, Generators, LV Transformers, Mechanical UPS, and UPS modules within each 2N system).
- **Path Redundancy (2N):** True 2N (A/B) path diversity from the MV dual-ring distribution through independent transformer banks, UPS systems (A and B), and distribution panels to dual-PDUs in each cabinet. Self-healing 13.8 kV dual-ring with SCADA-controlled automated switching provides path reconfiguration without human intervention.
- **Concurrent Maintainability:** Self-healing dual-ring topology enables isolation of any transformer or ring segment for maintenance while maintaining full N+1 redundancy on alternate path. 8 RMU switchgear with automated SCADA controls ensure continuous operation during maintenance activities.
- **Phasing Strategy:** All infrastructure (substation, generator pads, PDM pads, electrical yard, conduit rough-in) shall be designed and built for the 30 MW full build-out from day 1. Capital equipment (generators, transformers, UPS modules, mechanical UPS) will be purchased and commissioned in phases to match IT load growth.
- **Prefabricated Construction:** Prefabricated Power Delivery Modules (PDMs) containing LV switchboards, UPS systems, battery cabinets, and distribution panels provide 8-12 week schedule acceleration and factory-tested quality.

## 2.0 UTILITY SERVICE & SUBSTATION

### 2.1 System Topology

The following diagram illustrates the overall electrical system architecture, showing the 2N power distribution from utility service through the 13.8 kV dual-ring to the data center loads:

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
   [UPS-System-A]                   [UPS-System-B]
   12 MW (N+1)                      12 MW (N+1)
        │                                 │
   [Panel-A]                          [Panel-B]
        │                                 │
        └────────────┬────────────────────┘
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

| Parameter | Specification |
|-----------|---------------|
| **Quantity** | Eight (8) RMUs (4 per ring) |
| **Type** | SF6 or vacuum circuit breakers |
| **Rating** | 13.8 kV, 630A continuous, 20 kA short-circuit rating |
| **Controls** | SCADA-controlled remote switching with automated fault detection |
| **Location** | Electrical equipment yard adjacent to transformers and generators |
| **Function** | Isolate transformers, enable ring reconfiguration, interconnect generators/solar/BESS |

### 3.4 Advantages of Dual-Ring Topology
- **Concurrent Maintainability:** Any transformer can be isolated via RMU switching while maintaining full N+1 redundancy on alternate ring segment
- **Automated Load Transfer:** SCADA system detects faults and automatically reconfigures ring topology without human intervention (self-healing)
- **Generator/Solar/BESS Flexibility:** Multiple connection points enable paralleling of generators, solar inverters, and BESS inverters onto either ring for maximum operational flexibility

## 4.0 GENERATOR SYSTEM

### 4.1 Configuration

**Redundancy:** N+1 for total 30 MW facility load

**Phase 4 Configuration:**
- N = 8 generators (8 × 4.0 MW = 32 MW capacity)
- N+1 = 9 generators total
- Phased deployment: 3 (Phase 1) → 4 (Phase 2) → 6 (Phase 3) → 9 (Phase 4)

### 4.2 Generator Specifications

| Parameter | Specification |
|-----------|---------------|
| **Rating** | 4,000 kW continuous / 4,400 kW standby @ 13.8 kV |
| **Voltage** | 13,800V ±5%, 3-phase, 60 Hz, 0.8 power factor |
| **Fuel** | Diesel, EPA Tier 4 Final (NOx < 0.67 g/bhp-hr) |
| **Fuel Storage** | On-site bulk fuel storage for 24-hour runtime at 30 MW facility load |
| **Paralleling Controls** | PLC-based paralleling switchgear (Woodward easYgen 3500 or equivalent) to sync all generators onto 13.8 kV common bus |
| **Enclosure** | Sound-attenuated outdoor enclosure (65 dBA @ 7m), seismic rated per IBC 2018 |

### 4.3 Generator Yard Layout

- **Location:** South side of building, electrical equipment yard
- **Arrangement:** Horizontal layout with 8-10 ft clearances between units for maintenance access
- **Testing Protocol:** Closed-transition load bank for commissioning; monthly run tests; annual full-load tests
- **Maintenance Access:** Crane pad for major overhauls and component replacement
    

## 5.0 TRANSFORMER SYSTEM (13.8 KV / 480V)

### 5.1 Configuration

**Redundancy:** N+1 for total 30 MW facility load

**Phase 4 Configuration:**
- N = 10 transformers (10 × 3.15 MW = 31.5 MW capacity @ 0.9 PF)
- N+1 = 11 transformers total
- Phased deployment: 3 (Phase 1) → 4 (Phase 2) → 8 (Phase 3) → 11 (Phase 4)

### 5.2 Transformer Specifications

| Parameter | Specification |
|-----------|---------------|
| **Rating** | 3,500 kVA / 3.15 MW @ 0.9 power factor |
| **Voltage** | 13,800V delta primary / 480Y/277V secondary |
| **Type** | Oil-filled, ONAN cooling (Oil Natural, Air Natural) |
| **Impedance** | 5.75% |
| **Containment** | Secondary containment per EPA 40 CFR 112 |
| **Location** | Outdoor electrical yard with transformer pads |

### 5.3 Why 11 Transformers (N+1 Calculation for Phase 4)

**Design Load:** 30,000 kW (30 MW facility load at Phase 4)

**Transformer Capacity:**
- 11 transformers × 3,500 kVA = 38,500 kVA total
- At 0.9 power factor = 34,650 kW total capacity

**N+1 Operation:**
- Running: 10 transformers = 31,500 kW capacity
- Design load: 30,000 kW
- **Margin: 5% above design load** ✓

**Rationale:** N+1 redundancy with adequate margin for load growth and peak demand while enabling concurrent maintainability via dual-ring RMU switching
    

## 6.0 IT UPS SYSTEM (2N ARCHITECTURE)

### 6.1 Configuration

- **Redundancy:** 2N (fully redundant, dual-path) architecture to meet Tier III concurrent maintainability.
    
- **Topology:** The 24 MW IT load will be protected by two (2) independent **12 MW (N+1)** UPS systems (System A and System B).
    

### 6.2 System Sizing (Phase 4)

- **System A (12 MW N+1):**
    
    - Load: 12 MW
        
    - UPS Modules: 13 x 1,250 kVA (or similar) modules (12+1)
        
- **System B (12 MW N+1):**
    
    - Load: 12 MW
        
    - UPS Modules: 13 x 1,250 kVA (or similar) modules (12+1)
        
- **Total Modules (Phase 4):** 26
    

### 6.3 Path Redundancy

- **Path A:** `MV Ring A -> XFMRs-A -> SWBD-A -> UPS-System-A (12MW N+1) -> Panel-A -> Cabinet PDU-A`
    
- **Path B:** `MV Ring B -> XFMRs-B -> SWBD-B -> UPS-System-B (12MW N+1) -> Panel-B -> Cabinet PDU-B`
    

### 6.4 UPS Module Specifications

| Parameter | Specification |
|-----------|---------------|
| **Rating** | 1,250 kVA / 1,000 kW per module |
| **Topology** | Online double-conversion (VFI per IEC 62040-3) |
| **Efficiency** | 96% (ECO mode), 94% (double-conversion mode) |
| **Voltage** | 480V input/output, 3-phase |
| **Bypass** | Automatic static bypass + manual maintenance bypass |
| **Monitoring** | SNMP, Modbus TCP, BACnet integration, hot-swap capable |

### 6.5 Battery System

- **Type:** Lithium-Ion (preferred) or VRLA
- **Configuration:** External battery cabinets for each UPS system
- **Runtime:** 5-minute at full 12 MW load per system (A or B)
- **Purpose:** Sized to allow for MV generator synchronization to 13.8 kV common bus (~30-60 seconds) with margin
- **Why Lithium-Ion:** Higher energy density, longer lifespan (10-15 years vs 5-7 for VRLA), lower maintenance, better performance at elevated temperatures

### 6.6 Recommended UPS Vendors

- **Schneider Electric:** Galaxy VX or Galaxy VL series
- **Eaton:** 93PM or 93PR series
- **Vertiv:** Liebert EXL S1 series
    

### 6.7 Conceptual Diagram (2N UPS)

```
     MV RING A                         MV RING B
         │                                 │
    [XFMRs A]                           [XFMRs B]
         │                                 │
     [SWBD-A]                            [SWBD-B]
         │                                 │
┌───────────────────┐               ┌───────────────────┐
│ UPS-SYSTEM-A (N+1)│               │ UPS-SYSTEM-B (N+1)│
│ [M1] [M2]... [M13]│               │ [M1] [M2]... [M13]│
└─────────┬─────────┘               └─────────┬─────────┘
          │                                 │
    [Dist Panel A]                      [Dist Panel B]
          │                                 │
          └───────────┐   ┌─────────────┘
                      │   │
                ┌─────┴───┴─────┐
                │   RACK 1      │
                │ [PDU-A] [PDU-B] │
                └───────────────┘
```

## 7.0 MECHANICAL UPS SYSTEM

### 7.1 Purpose

The mechanical UPS system protects critical mechanical loads (chiller pumps, CDU pumps, building fans) from brief utility interruptions during generator startup and synchronization to the 13.8 kV common bus (~30-60 seconds).

**Important:** Mechanical UPS is a separate system from IT UPS. IT equipment is protected by the dedicated 2N IT UPS system (Section 6.0).

### 7.2 Configuration

**Redundancy:** N+1 modular static UPS architecture

**Protected Equipment:**
- Chiller pumps for Loop 3 (L2C warm water - 85°F)
- Chiller pumps for Loops 1+2 (RDHx cold water - 60°F)
- CDU pumps (L2C coolant distribution)
- Building HVAC fans (data hall pressurization and humidity control)

**Phased Deployment:** UPS modules added in phases to match mechanical load growth

### 7.3 Phase 4 Sizing (N+1 Calculation)

**Module Size:** 250 kW static UPS modules

**Protected Load:** 6,000 kW (mechanical systems at Phase 4)

**Module Count:**
- N = 24 modules (24 × 250 kW = 6,000 kW)
- N+1 = 25 modules total

**N+1 Verification:** 24 running modules = 6,000 kW capacity = full mechanical load ✓
    

## 8.0 LOW VOLTAGE (480V) DISTRIBUTION

### 8.1 Main Switchboards

**Configuration:** Dual switchboards for 2N distribution

| Parameter | Specification |
|-----------|---------------|
| **Quantity** | Two (2): SWBD-A and SWBD-B |
| **Rating** | 4,000A copper busbar, 480V, 3-phase, 4-wire |
| **Short-Circuit** | 65 kA SCCR (Short-Circuit Current Rating) |
| **Source** | SWBD-A fed from MV Ring A transformers; SWBD-B fed from MV Ring B transformers |
| **Configuration** | 2N distribution: All critical loads served by both A and B paths |

**Path Diversity:** Each switchboard is fed from different 13.8 kV ring segment via independent transformer banks, ensuring complete electrical separation for concurrent maintainability.

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
    
- **Rating:** PDUs shall be sized based on the cabinet's designed load (e.g., 2N for 25 kW or 2N for 100 kW).
    

## 10.0 NON-CRITICAL (HOUSE) POWER

### 10.1 Philosophy

All non-critical support spaces shall be on an electrical system **completely separate** from the critical data center infrastructure. This separation prevents non-critical load faults from impacting critical IT operations and enables independent maintenance and testing.

### 10.2 Non-Critical Areas Served

The house power system serves the following spaces:

- **Office Spaces:** Conference rooms, offices, call pods, seating areas, hoteling workstations
- **NOC (Network Operations Center):** Non-IT building systems only (workstation power on portable UPS)
- **Security:** Control Room (SCR) at main entrance, Control Booth (SCB) at loading dock
- **Common Areas:** Bathrooms, showers, break room, lounge, gym/fitness center
- **Circulation:** Hallways, corridors, loading dock
- **Building HVAC:** Office RTUs, exhaust fans (non-critical ventilation)
- **Storm Shelter:** Safe room ventilation and lighting
- **General Lighting:** Non-emergency building lighting
- **Elevator:** Non-critical passenger elevator
- **Staging/Storage:** Warehouse and equipment storage areas

### 10.3 Utility Service

- **Source:** Single 13.8kV/480V transformer fed from 13.8 kV common bus (via Solar/BESS connection point)
- **Capacity:** ~400 kVA (300-350 kW sustained load)
- **Single Point of Failure:** Acceptable - house generators provide backup for loss of utility

### 10.4 Natural Gas House Generators

| Parameter | Specification |
|-----------|---------------|
| **Quantity** | Two (2) generators (N+1 redundancy) |
| **Rating** | 250-350 kW each @ 480V, 3-phase, 60 Hz |
| **Fuel** | Natural gas (piped utility) or on-site propane if NG not available |
| **Start Time** | <10 seconds from utility loss to generator online |
| **Enclosure** | Sound-attenuated outdoor enclosure |
| **ATS** | Automatic Transfer Switches with priority load shedding if required |

**Why Natural Gas:**
- **Unlimited Runtime:** No refueling required during extended utility outages
- **Independent Supply:** Preserves diesel fuel supply for critical generator operation
- **Lower Emissions:** Cleaner burning than diesel, easier EPA compliance

### 10.5 Portable UPS for Workstations

**Purpose:** Provide 10-15 minute ride-through during transfer to house generators (~10 seconds)

**Applications:**
- NOC workstations and display systems
- Security control room (SCR) and booth (SCB) workstations and surveillance systems
- Office IT equipment (workstations, network switches, VoIP phones)
- BMS/DCIM servers (if not on critical IT UPS)

**Configuration:**
- Type: Rack-mount or tower UPS units
- Capacity: 1-3 kVA per workstation/equipment cluster
- Runtime: 10-15 minutes
- Quantity: ~20-30 units distributed throughout facility
    

## 11.0 RENEWABLE ENERGY INTEGRATION

### 11.1 Solar Array Interconnection

**Capacity:** 8+ MW DC solar array (adjacent to data center site)

**Inverter Configuration:**
- Type: String or central inverters outputting **13.8 kV AC directly**
- **Key Design Detail:** Inverters output at 13.8 kV - **no step-up transformer required**
- Connection: Dedicated circuit breaker to 13.8 kV common bus
- Metering: Bi-directional revenue metering (production + export to grid)

**Location:** Solar array field adjacent to data center, within property boundary

### 11.2 Battery Energy Storage System (BESS) Interconnection

**Capacity:** 4-8 MWh battery energy storage system

**Inverter Configuration:**
- Type: Bi-directional inverters (charge/discharge) outputting **13.8 kV AC directly**
- **Key Design Detail:** Inverters output at 13.8 kV - **no step-up transformer required**
- Connection: Dedicated circuit breaker to 13.8 kV common bus
- Controls: Grid-forming inverter controls (if required for islanded microgrid operation)

**Functions:**
- **Peak Shaving:** Reduce utility demand charges during peak periods
- **Demand Response:** Participate in utility demand response programs
- **Solar Smoothing:** Buffer solar output variability for stable grid integration
- **Backup Power:** Supplement generators during utility outages

### 11.3 Advantages of 13.8 kV Integration

The 13.8 kV common bus architecture eliminates the need for step-up transformers typically required for solar and BESS integration. Standard commercial solar inverters and BESS inverters are available with 13.8 kV output, enabling direct connection to the MV distribution system and reducing cost, complexity, and energy losses.


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

### 12.3 Location

Outdoor PDMs located adjacent to electrical equipment yard with weather-protected enclosures. Designed for Oklahoma climate (temperature extremes, humidity, wind loads per local codes).

---

## 13.0 ELECTRICAL PHASING STRATEGY

The electrical infrastructure is designed for ultimate 30 MW facility load (Phase 4), with capital equipment purchased and commissioned in phases to match IT load growth. All infrastructure (substation, electrical yard, generator pads, PDM pads, conduit rough-in) is designed and built for Phase 4 from day 1.

---

### 13.1 PHASE 1: 3 MW IT LOAD (30 L2C RACKS)

**Strategy:** Commission DH-W (Data Hall West) for high-density L2C anchor tenant, commission 2N UPS System A+B with minimum module count, build all infrastructure for future expansion.

**Rack Deployment:** 30 racks × L2C @ 100 kW = 3,000 kW IT load

**Load Summary:**

| Load Type | Power (kW) | Description |
|-----------|------------|-------------|
| **IT Load** | 3,000 | 30×L2C racks @ 100 kW each |
| **Mechanical** | 840 | Loop 3 chillers, pumps, CDUs (L2C cooling only) |
| **Building** | 360 | HVAC, lighting, NOC, security, house loads |
| **Total Facility Load** | **~4,200 kW** | **PUE 1.40** |

**Electrical Infrastructure:**

| Equipment | Quantity | Sizing Notes |
|-----------|----------|--------------|
| **Generators** | 3×4.0 MW | N+1 for 4.2 MW (2 running = 8 MW capacity, 90% margin) |
| **LV Transformers** | 3×3.5 MVA | N+1 for 4.2 MW (2 running = 6.3 MW capacity, 50% margin) |
| **IT UPS Modules** | 6 total | 2N: System A=3 modules, System B=3 modules (1.5MW N+1 per system) |
| **Mechanical UPS** | 8×250 kW | N+1 for 840 kW mechanical load (7 running = 1,750 kW) |

**Data Halls:** DH-W commissioned with L2C cooling (Loop 3), DH-E shell only

---

### 13.2 PHASE 2: 6 MW IT LOAD (150 TOTAL RACKS)

**Strategy:** Commission DH-E (Data Hall East) for medium-density RDHx racks, commission Loops 1+2 for RDHx cooling, expand both UPS systems, add generators and transformers.

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

| Equipment | Phase 2 Total | Add from Phase 1 |
|-----------|---------------|------------------|
| **Generators** | 4×4.0 MW | Add 1 unit (N+1 for 8.1 MW) |
| **LV Transformers** | 4×3.5 MVA | Add 1 unit (N+1 for 8.1 MW) |
| **IT UPS Modules** | 10 total | Add 4 modules (System A=5, System B=5 for 3MW N+1 per system) |
| **Mechanical UPS** | 12×250 kW | Add 4 modules (N+1 for 1,350 kW) |

**Data Halls:** Both DH-W and DH-E operational

---

### 13.3 PHASE 3: 15 MW IT LOAD (285 TOTAL RACKS)

**Strategy:** Scale both data halls, expand L2C capacity in DH-W and RDHx capacity in DH-E, significant expansion of generators, transformers, and UPS systems.

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

| Equipment | Phase 3 Total | Add from Phase 2 |
|-----------|---------------|------------------|
| **Generators** | 6×4.0 MW | Add 2 units (N+1 for 19.5 MW) |
| **LV Transformers** | 8×3.5 MVA | Add 4 units (N+1 for 19.5 MW) |
| **IT UPS Modules** | 18 total | Add 8 modules (System A=9, System B=9 for 7.5MW N+1 per system) |
| **Mechanical UPS** | 16×250 kW | Add 4 modules (N+1 for 3,000 kW) |

---

### 13.4 PHASE 4: 24 MW IT LOAD (468 TOTAL RACKS) - FULL BUILD-OUT

**Strategy:** Maximize both data halls to full capacity, complete all electrical infrastructure to ultimate 30 MW facility design.

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

| Equipment | Phase 4 Total | Add from Phase 3 |
|-----------|---------------|------------------|
| **Generators** | 9×4.0 MW | Add 3 units (N+1 for 30 MW: 8 running = 32 MW capacity) |
| **LV Transformers** | 11×3.5 MVA | Add 3 units (N+1 for 30 MW: 10 running = 31.5 MW capacity) |
| **IT UPS Modules** | 26 total | Add 8 modules (System A=13, System B=13 for 12MW N+1 per system) |
| **Mechanical UPS** | 25×250 kW | Add 9 modules (N+1 for 6,000 kW: 24 running = 6,000 kW capacity) |

---

### 13.5 PHASING SUMMARY TABLE

**Note:** UPS Module count is based on a 2N (A/B) 12 MW N+1 system, using 1 MW (1250 kVA) modules.

| **Phase** | **IT MW** | **Racks (L2C/RDHx)** | **PUE** | **Facility MW** | **Generators (4 MW)** | **LV XFMRs (3.5 MVA)** | **IT UPS Modules (1 MW)** |
|-----------|-----------|----------------------|---------|-----------------|------------------------|-------------------------|---------------------------|
| **1** | 3 | 30 (30/0) | 1.40 | ~4.2 | 3 (N+1) | 3 (N+1) | 6 (2N × 1.5MW N+1) |
| **2** | 6 | 150 (30/120) | 1.35 | ~8.1 | 4 (N+1) | 4 (N+1) | 10 (2N × 3MW N+1) |
| **3** | 15 | 285 (105/180) | 1.30 | ~19.5 | 6 (N+1) | 8 (N+1) | 18 (2N × 7.5MW N+1) |
| **4** | 24 | 468 (168/288) | 1.25 | ~30.0 | 9 (N+1) | 11 (N+1) | 26 (2N × 12MW N+1) |

---

## 14.0 CODES AND STANDARDS

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
- **Prepared by:** EVS / PGCIS Team
- **Key Updates:**
  - Implemented 2N UPS architecture (fully redundant dual-path)
  - Updated for 468-rack deployment (168 L2C + 288 RDHx)
  - Detailed 4-phase buildout to 30 MW facility load
  - All equipment properly sized for facility load (IT × PUE)
  - Added comprehensive phasing narratives with load tables
  - Enhanced solar/BESS integration details
  - Added PDM section for accelerated construction schedule