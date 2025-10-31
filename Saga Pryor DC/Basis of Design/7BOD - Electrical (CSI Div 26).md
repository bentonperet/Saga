**Created:** 2025-10-29
**Updated from:** Pryor_Bod_EVS_Rev01.md

# BASIS OF DESIGN - ELECTRICAL
## CSI Division 26
### Pryor Data Center - PACHYDERM GLOBAL

**Parent Document:** [[Saga Pryor DC/Basis of Design/Erik_BOD_Updated/_BOD - Exec Summary and TOC|_BOD - Exec Summary and TOC]]

---

## OVERVIEW

Electrical systems provide Tier III-compliant power distribution with N+1 IT UPS architecture backed by self-healing 13.8 kV dual-ring MV distribution, N+1 generators and transformers, supporting 3 MW Phase 1 (expandable to 12 MW Phase 2). Customer-owned 345 kV substation with 13.8 kV distribution integrates utility, solar, BESS, and generators on common voltage infrastructure. 

**Design Philosophy:**
- **Path redundancy:** 13.8 kV self-healing dual-ring MV distribution with automated SCADA switching
- **Component redundancy:** N+1 (IT UPS, generators, transformers, mechanical UPS)
- **Concurrent maintainability:** Service any component without IT interruption
- **345kV/13.8kV substation:** Customer-owned, integrates all power sources at 13.8 kV
- **Prefabricated PDMs:** Factory-tested electrical enclosures accelerate schedule

---

## UTILITY SERVICE & SUBSTATION

### Customer-Owned 345 kV Substation

**Configuration:**
```
345 kV TRANSMISSION (Utility)
        │
   [Utility Revenue Metering - 345 kV]
        │
        ▼
   ┌─────────────────────────────────┐
   │  CUSTOMER-OWNED SUBSTATION       │
   │                                  │
   │  [345 kV Switchyard]             │
   │        │                         │
   │  [XFMR-A: 345kV/13.8kV, 25MVA]  │
   │  [XFMR-B: 345kV/13.8kV, 25MVA]  │ (2N redundancy)
   │        │                         │
   └────────┼─────────────────────────┘
            │
            ▼
   ┌─────────────────────────────────┐
   │    13.8 kV COMMON BUS            │
   │  (Dual Ring Topology)            │
   ├─────────────────────────────────┤
   │ • Solar Inverters (8+ MW)        │
   │ • BESS Inverters (4-8 MWh)       │
   │ • Generators (6 × 4 MW)          │
   │ • Data Center Load (12-24MW)     │
   └─────────────────────────────────┘
```

### 345 kV Primary Service

**Utility Interconnection:**
- **Voltage:** 345 kV transmission (planning basis)
- **Available Substations (Kamo Power Electric Co-op):**
  - **Sportsman Substation (SW):** 345 kV service, 3 lines
  - **Dry Gulch Substation (N):** 161 kV service, 2 lines
- **Note:** Final voltage selection (345 kV vs 161 kV) depends on utility interconnection study, available capacity, and comparative economics. If the utility saving favor purchasing a larger step-down transformer, it may be the ideal path. Or if there is no savings, and the 161 kV service is possible then that may be the better economic decision.
- **Capacity:** ~30 MVA (sized for 24 MW master plan + solar/BESS with margin)
- **Metering:** Revenue-grade metering at transmission voltage (utility-owned)
- **Protection:** Per utility interconnection requirements

**345kV/13.8kV Substation Transformers:**
- **Quantity:** 2 transformers (N+1 redundancy - either can carry full load)
- **Rating:** 25 MVA each @ 345kV/13.8kV
- **Type:** Oil-filled, ONAN cooling
- **Configuration:** Delta-wye with neutral solidly grounded
- **Location:** Outdoor substation yard on data center site

**Cost:** ~$7-12M for complete customer-owned substation (345 kV requires larger equipment and clearances than lower voltages)


---

## MEDIUM VOLTAGE DISTRIBUTION (13.8 kV)

### System Configuration

**Dual-Ring MV Topology:**
```
345kV UTILITY ──[XFMR-A: 25MVA]──[RMU-1]──[RMU-2]──[RMU-3]── RING A
                                     │        │        │
                                 [XFR-1]  [XFR-3]  [XFR-5]

345kV UTILITY ──[XFMR-B: 25MVA]──[RMU-4]──[RMU-5]──[RMU-6]── RING B
                                     │        │        │
                                 [XFR-2]  [XFR-4]  [XFR-6]

Phase 2: Add [XFR-7] and [XFR-8]

GENERATORS (6 × 4.0 MW @ 13.8 kV) ─► Connect to both rings via paralleling switchgear
SOLAR INVERTERS (8+ MW) ──────────► Connect to 13.8 kV common bus (direct - no transformer)
BESS INVERTERS (4-8 MWh) ─────────► Connect to 13.8 kV common bus (direct - no transformer)
```
@Muhammed - NEEDS CONFIRMATION
### Ring Main Units (RMUs)

**Equipment:** 6 × RMUs (13.8 kV, 630A rated)
- **Configuration:** 3 RMUs per ring (Ring A and Ring B)
- **Type:** SF6 or vacuum circuit breakers
- **Rating:** 13.8 kV, 630A continuous (short-circuit rating per fault study)
- **Controls:** SCADA-controlled remote switching for load transfer
- **Location:** Electrical equipment yard, generator/PDM boundary
- **Function:** Isolate transformers, enable ring reconfiguration, interconnect generators/solar/BESS

**Advantages:**
- Any transformer can be isolated for maintenance without facility shutdown
- Load automatically transfers to remaining transformers via SCADA
- Generators, solar, and BESS parallel onto either or both rings
- True concurrent maintainability

---

## GENERATOR SYSTEM

### Configuration

**6 × 4.0 MW @ 13.8 kV Diesel Generators (N+1 Redundancy)**
- **Phase 1:** 3 generators (positions 1-3)
- **Phase 2:** +3 generators (positions 4-6)
- **N+1 Operation:** 5 generators carry full Phase 2 load (18.2 MW), 1 standby

### Generator Specifications (Each Unit)

| Parameter                | Specification                                                                                 |
| ------------------------ | --------------------------------------------------------------------------------------------- |
| **Rating**               | 4,000 kW continuous @ 13.8 kV, 3-phase, 60 Hz                                                 |
| **Fuel**                 | Diesel (EPA Tier 4 Final emissions)                                                           |
| **Fuel Capacity**        | ~2,000 gal belly tank per unit (connected to central bulk fuel tank farm via common manifold) |
| **Endurance**            | ~24 hours at full load (central bulk fuel storage + redundant supply contracts)               |
| **Synchronizing**        | Automatic paralleling with load sharing                                                       |
| **Enclosure**            | Sound-attenuated outdoor enclosure                                                             |
| **Seismic**              | Per IBC seismic requirements for site location                                                 |

### Why 13.8 kV Generators (Not 480V)

**Technical Advantages:**
- **US standard voltage:** 13.8 kV is the dominant voltage for US data center generators (better availability, shorter lead times)
- **Common voltage:** Matches utility substation, solar inverters, BESS inverters (13.8 kV is standard US renewable voltage)

### Generator Yard Layout
- **Location:** Outdoor electrical equipment yard (south side)
- **Arrangement:** Horizontal layout per vendor and code clearance requirements
- **Maintenance Access:** Crane pad for major overhauls

---

## TRANSFORMER SYSTEM (13.8 kV/480V)

### Configuration

**8 × 3,500 kVA (13.8 kV/480V) Oil-Filled Transformers**
- **Phase 1:** 3 transformers (N+1 for 5.8 MW load)
- **Phase 2:** +5 transformers (8 total for 18.2 MW load)

### Transformer Specifications (Each Unit)

| Parameter | Specification |
|-----------|---------------|
| **Rating** | 3,500 kVA |
| **Voltage** | 13,800V delta / 480Y/277V |
| **Cooling** | ONAN (oil natural, air natural) |
| **Liquid** | Mineral oil or high fire-point vegetable oil |
| **Containment** | Secondary containment per EPA 40 CFR 112 |

### Why 8 Transformers

**Phase 1:** 3 × 3,500 kVA transformers
- N+1 operation: 2 transformers support ~5.8 MW design load with margin

**Phase 2:** 8 × 3,500 kVA transformers
- N+1 operation: 6 transformers support ~18.2 MW design load with margin

**8th transformer provides:**
- Better load distribution (lower per-unit utilization = longer life)
- Future expansion headroom
- True concurrent maintainability with margin


---

## IT UPS SYSTEM (N+1 ARCHITECTURE)

### System Configuration

**N+1 Modular Topology with MV Dual-Ring Path Redundancy**

```
           13.8 kV DUAL RING (Ring A + Ring B)
                 │           │
           [XFMR-A]       [XFMR-B]
                 │           │
                480V         480V
                 │           │
           [SWBD-A]──────[SWBD-B]
                 │           │
         ┌───────┴───────────┴───────┐
         │                           │
         │   UPS MODULES (N+1)       │
         │                           │
         │  UPS-1  UPS-2  UPS-3 ...  │
         │ (1,250)(1,250)(1,250)...  │
         │                           │
         │  (N running, +1 standby)  │
         └───────────┬───────────────┘
                     │
                     ▼
            IT Distribution Panels
                     │
           ┌─────────┴─────────┐
           │                   │
      Panel-A             Panel-B
        (fed from          (fed from
       different           different
       SWBD/Ring)          SWBD/Ring)
           │                   │
           └──► Cabinet PDUs ◄──┘
               (Dual PDUs per cabinet)
```

### Phase 1: ~5 × 1,250 kVA IT UPS Modules

**Modular Configuration:**
- ~5 × 1,250 kVA / 1,000 kW modules in parallel
- 4 modules running, 1 standby (N+1)
- Running capacity: ~4,000 kW for ~3,000 kW IT load
- Feeds: Multiple IT distribution panels fed from different 480V switchboards

**Path Redundancy:**
- **MV dual-ring:** Switchboards A and B fed from different segments of 13.8 kV dual-ring
- **Automated switching:** SCADA-controlled ring switching provides path redundancy
- **Cabinet dual PDUs:** Fed from different 480V distribution panels (connected to SWBD-A and SWBD-B)

**Component Redundancy:**
- **N+1 UPS:** One UPS module fails → remaining N modules continue
- **Modular hot-swap:** Individual module replacement without downtime

**Battery:** 5-minute runtime maximum (allows for MV generator sync to bus, even two attempts) (Lithium-ion preferred)

### Phase 2: ~13 × 1,250 kVA IT UPS Modules (add ~8)

**Modular Configuration:**
- ~13 × 1,250 kVA total
- 12 modules running, 1 standby (N+1)
- Running capacity: ~12,000 kW for ~12,000 kW IT load

### Redundancy Philosophy

**Two Layers of Redundancy:**
1. **Path redundancy:** 13.8 kV dual-ring with self-healing automated switching (feeds SWBD-A and SWBD-B from different ring segments)
2. **Component redundancy:** N+1 UPS modular architecture (any single UPS module failure tolerated)

**Cabinet Dual PDUs:**
- Each cabinet has two PDUs fed from different 480V distribution panels
- Distribution panels connected to different switchboards (SWBD-A vs SWBD-B)
- SWBD-A and SWBD-B fed from different 13.8 kV ring segments
- Result: Full path diversity from 13.8 kV through cabinet PDU

**Advantages over Traditional 2N UPS:**
- **Lower capital cost:** ~40-50% fewer/smaller UPS modules
- **Higher efficiency:** Single UPS path = one fewer conversion stage
- **Simplified maintenance:** Fewer UPS systems to maintain
- **Equivalent reliability:** MV dual-ring provides path redundancy; N+1 UPS provides component redundancy

### UPS Technical Specifications

| Parameter | Specification |
|-----------|---------------|
| **Rating** | 1,250 kVA / 1,000 kW per module |
| **Topology** | Online double-conversion (VFI per IEC 62040-3) |
| **Input/Output** | 480V, 3-phase |
| **Battery** | External Lithium-ion cabinets, 5-minute runtime |

**Recommended UPS Vendors:**
- Schneider Electric Galaxy VX/VL (or equivalent approved)
- Eaton 93PM/93PR (or equivalent approved)
- Vertiv Liebert EXL S1 (or equivalent approved)

---

## MECHANICAL UPS SYSTEM

### Purpose
Protect critical mechanical loads (pumps, fans, CDUs) from brief utility interruptions during generator startup and sync to bus (~30-60 seconds).

**NOT for IT loads** - IT equipment protected by dedicated IT UPS system.

### Configuration

**Phase 1: ~8 × 250 kW Static UPS Modules (N+1)**
- Protected load: ~1,600 kW (chillers, pumps, fans)

**Phase 2: ~20 × 250 kW Static UPS Modules (add ~12)**
- Protected load: ~4,600 kW (all loops, chillers, pumps, CDUs, fans)

**Design Rationale:** Mechanical UPS provides cost-effective protection for HVAC/cooling loads with shorter runtime requirements (~30-60 seconds for generator start). This approach reserves expensive long-runtime battery capacity for IT loads only, optimizing capital cost while maintaining Tier III reliability.

---

## LOW VOLTAGE DISTRIBUTION (480V)

### Main Switchboards (Dual Switchboards Fed from Different MV Ring Segments)

**SWBD-A and SWBD-B**
- **Configuration:** Dual main switchboards rated for design load with redundant feeds from separate MV ring segments
- **SWBD-A fed from:** Transformers on Ring A (MV dual-ring segment A)
- **SWBD-B fed from:** Transformers on Ring B (MV dual-ring segment B)
- **Path diversity:** Each switchboard receives power from different 13.8 kV ring segment
- **Final ratings:** Per detailed engineering (load study and fault analysis)

### Distribution Panels (All Dual-Fed)

**Philosophy:** Dual A/B distribution panels provide redundant paths from separate MV ring segments. Final panel quantities, ratings, and circuit allocation will be determined during detailed engineering.

**Key Distribution Categories:**
- **IT Distribution** - Cabinet PDUs, dual-fed
- **Mechanical Distribution** - Chillers, pumps, CDUs (separate panels for Loops 1+2 and Loop 3)
- **UPS Distribution** - IT UPS output distribution
- **Building/House Power** - Separate system (see Non-Critical Building Power)

---



## NON-CRITICAL BUILDING POWER (HOUSE POWER)

### Philosophy

**Separate from Critical Systems:** Non-critical building services operate on independent electrical infrastructure from data hall and MMR critical systems.

**Purpose:** Avoid impact to critical infrastructure from non-critical loads; enable independent maintenance and testing.

### Non-Critical Areas Served

- **Office spaces** (conference rooms, hoteling offices, call pods, seating areas)
- **Bathrooms** (restrooms, showers)
- **Hallways and corridors**
- **Security Control Room (SCR)** - main entrance
- **Security Control Booth (SCB)** - loading dock
- **Loading dock** (lighting, doors, HVAC)
- **Staging and storage areas**
- **Break room, lounge, gaming area**
- **NOC** (Network Operations Center) - non-IT systems
- **Gym/fitness center**
- **Storm shelter/safe room** (lighting, ventilation)
- **Building HVAC** (office RTUs, exhaust fans)
- **General lighting** (non-emergency)
- **Elevator** (non-critical use)

### Utility Service

**Primary Power:**
- **Source:** Single 13.8kV/480V transformer fed from Solar/BESS system (via 13.8 kV common bus)
- **Voltage:** 480V, 3-phase, 4-wire
- **Capacity:** ~400 kVA for non-critical building loads
- **Single Point of Failure:** Acceptable (redundant natural gas house generators provide backup)
- **No PDMs Required:** House power uses standard distribution, not prefabricated modules

### Backup Power - Natural Gas House Generators

**Configuration:** Redundant natural gas generators provide backup power to non-critical areas during utility failure

**Specifications:**
- **Quantity:** 2 generators (N+1 redundancy)
- **Rating:** 250-350 kW each @ 480V, 3-phase, 60 Hz
- **Fuel:** Natural gas (piped from utility or on-site propane if NG not available)
- **Fuel supply:** Utility natural gas service
- **Endurance:** Unlimited runtime (continuous fuel supply)
- **Enclosure:** Sound-attenuated outdoor enclosure
- **Emissions:** EPA-compliant natural gas emissions

**Rationale for Natural Gas:**

Natural gas for non-critical loads is standard practice in data centers. This design preserves critical diesel fuel for IT loads and provides unlimited runtime for comfort/office power during extended outages (ice storms, multi-day events). Natural gas generators offer:
- **Unlimited runtime:** No fuel storage/delivery logistics (utility gas supply)
- **Lower maintenance:** Cleaner burning than diesel (~30-40% lower O&M costs)
- **Cost-effective:** Lower capital cost ($200-300/kW vs $400-500/kW diesel) and fuel costs
- **Independent fuel source:** Preserves diesel supply for critical IT generators; separate utility infrastructure reduces single-point failure risk
- **Simplified permitting:** Lower emissions (NOx, PM, CO); easier to permit for extended runtime vs diesel restrictions in some jurisdictions
### Portable UPS for IT Systems in Non-Critical Areas

**Purpose:** Provide ride-through battery power for IT equipment in non-critical spaces during transfer to house generators (~10-15 seconds)

**Applications:**
- **NOC workstations** and display systems
- **SCR/SCB security workstations** and surveillance equipment
- **Office IT equipment** (workstations, network switches, VoIP phones)
- **BMS/DCIM servers** (if not on critical UPS)

**Configuration:**
- **Type:** Portable rack-mount or tower UPS units
- **Capacity:** Sized per load (typical: 1-3 kVA per workstation/equipment cluster)
- **Runtime:** 10-15 minutes for graceful shutdown during extended outages
- **Quantity:** ~20-30 units distributed throughout facility

**Cost:** ~$50-100K for house generators; ~$30-50K for portable UPS units

**Note:** Portable UPS for non-critical areas is not required for Tier III compliance but provides operational continuity for NOC, security systems, and staff during utility transfer.

---

## PREFABRICATED POWER DELIVERY MODULES (PDMs)

**2 × Outdoor PDMs** (Phase 1)
- Contents: LV Switchboards, IT UPS modules, Battery cabinets, Distribution panels
- Benefits: Factory testing, 8-12 week schedule acceleration, quality control
- Cost premium: 5-10% justified by schedule and quality benefits

---

## ELECTRICAL LOAD SUMMARY

### Phase 1

| Load | Power (kW) |
|------|------------|
| IT (through IT UPS) | ~3,100 |
| Mechanical (through Mech UPS) | ~1,700 |
| Building/Lighting | ~400 |
| **Design Load** | **~5,800** |

**Generator Capacity (N+1):** 3 × 4.0 MW = 12 MW (N+1 operation with margin)

### Phase 2

| Load | Power (kW) |
|------|------------|
| IT (through IT UPS) | ~12,500 |
| Mechanical (through Mech UPS) | ~4,600 |
| Building/Lighting | ~400 |
| **Design Load** | **~18,200** |

**Generator Capacity (N+1):** 6 × 4.0 MW = 24 MW (N+1 operation with margin)

---

## CODES AND STANDARDS

- **NEC 2023** (National Electrical Code), Oklahoma amendments
- **IEEE 141** (Red Book - Electric Power Distribution)
- **IEEE 142** (Green Book - Grounding)
- **IEEE 242** (Buff Book - Protection and Coordination)
- **NFPA 110** (Emergency and Standby Power Systems)
- **IEC 62040-3** (UPS Classification - VFI topology)

---

**Tags:** #pryor-dc #electrical #345kv-substation #13.8kv-distribution #microgrid #tier-iii

**Next Steps:**
1. Utility interconnection study for 345 kV transmission connection
2. Substation engineering design (345kV/13.8kV transformers, switchyard, increased clearances)
3. Solar and BESS inverter specifications (13.8 kV output - US standard voltage)
4. Generator paralleling and microgrid control strategy
5. Protection coordination study (345 kV through 480V)

---

**Document Control:**
- **Source:** Pryor_Bod_EVS_Rev01.md
- **Date Updated:** October 30, 2025
- **Prepared by:** EVS / PGCIS Team
- **Key Updates:** Changed from 138kV/11kV to 345kV/13.8kV (US data center standard voltage, better renewable integration)
