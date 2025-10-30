**Created:** 2025-10-23 10:40

# BASIS OF DESIGN - ELECTRICAL
## CSI Division 26
### Saga Energy – Pryor Data Center

**Parent Document:** [[_BOD - Exec Summary and TOC]]
**Related:** [[Why BESS Should Not Be UPS]] | [[Excess Solar Monetization Strategy]] | [[Architectural Meeting Changes by CSI Division]]

---

## OVERVIEW
Electrical systems provide Tier III-compliant N+1 redundant power distribution with dual power paths (A/B) supporting 12 MW initial IT load (20-24 MW ultimate). Traditional modular UPS architecture confirmed as only proven, bankable solution for project finance.

**Major Design Decision:** Traditional modular UPS provides concurrent maintainability required for Tier III compliance. BESS-as-UPS topology rejected due to non-maintainable single point of failure (see [[Why BESS Should Not Be UPS]]). Economic BESS separately evaluated and rejected due to negative NPV (see [[Excess Solar Monetization Strategy]]).

#### **ELECTRICAL SYSTEMS**
- Primary Service: 138 kV to 13.8 kV substation (15-20 MVA transformer)
- UPS: N+1 modular UPS (500 kW modules) with dual paths A/B
  - Phase 1: 8 modules (4 MW capacity)
  - Phase 4: 32 modules (16 MW capacity)
  - Phase 5: 64 modules (32 MW capacity)
- UPS Topology: Dual A/B busways, concurrent maintainability
- IT Transformers: 5,000 kVA, 13.8kV-480Y/277V (Phase 1: 2, Phase 4: 5, Phase 5: 10 units)
- IT Switchboards: 7,000A, 480V (quantities match transformers for N+1 chain)
- Generators: 4.3 MW natural gas turbine (Phase 1: 2, Phase 4: 5, Phase 5: 10 units, N+1 redundancy)
- Electrical Enclosures: Outdoor containerized (12 units with space for 16, ~12 ft × 55 ft each {TBC})
- Distribution: 480V overhead busway at 12-14 ft elevation
- Electrical Code: NEC 2023, Oklahoma amendments

---

## EQUIPMENT LIST

**Phasing Reminder**

| Phase | IT Load | Facility Load (PUE 1.2-1.35) |
| ----- | ------- | ---------------------------- |
| **1** | 3MW     | 3.6-4.05 MW                  |
| **2** | 6MW     | 7.2-8.1 MW                   |
| **3** | 9MW     | 10.8-12.15 MW                |
| **4** | 12MW    | 14.4-16.2 MW                 |
| **5** | 20-24MW | 24.0-32.4 MW                 |

### List of Equipment for Natural Gas Generation

| Equipment              | Description                                                                                                                                                    | Phase1 Qty 3MW | Phase2 Qty 6MW | Phase3 Qty 9MW | Phase4 Qty 12MW | Phase5 Qty 24MW |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | -------------- | -------------- | --------------- | --------------- |
| Generator              | 4.3 MW Natural Gas Turbine Generator                                                                                                                           | 2              | 3              | 4              | 5               | 10              |
| IT Transformer         | 5,000 kVA, 13.8kV-480Y/277V, VPI dry-type, outdoor rated, 5.75% impedance, forced air cooling, feeds IT switchboards                                           | 2              | 3              | 4              | 5               | 10              |
| Mechanical Transformer | 2,000 kVA (Phase 1-2) or 5,000 kVA (Phase 3-5), 13.8kV-480Y/277V, VPI dry-type, outdoor rated, 5.75% impedance, feeds mechanical loads (chillers, pumps, etc.) | 2              | 2              | 3              | 3               | 3               |
| IT Switchboard         | 7,000A, 480V, 3-phase, 65kA SCCR, main lug or breaker, feeds overhead busway to data hall                                                                      | 2              | 3              | 4              | 5               | 10              |
| UPS Module             | 500 kW modular hot-swappable UPS, double-conversion, 96-97% efficiency, 480V input/output, dual A/B paths (N+1 per path)                                       | 8              | 16             | 24             | 32              | 64              |
| UPS Battery Cabinet    | Lithium-ion or VRLA battery cabinet, 15-min backup at full load, distributed per UPS module                                                                    | 32             | 64             | 96             | 128             | 256             |
| Mechanical Switchboard | 2,000A (Phase 1-2) or 6,000A (Phase 3-5), 480V, 3-phase, 35kA SCCR, feeds chiller plant, pumps, DX units, support HVAC                                         | 2              | 2              | 3              | 3               | 3               |
| Mechanical UPS           | 250 kW UPS for critical mechanical controls, pumps, BMS, 480V input, dual-conversion, N+1 configuration                                                        | 2              | 3              | 3              | 4               | 6               |
| Mechanical UPS Batteries | VRLA or Li-ion batteries for mechanical UPS, 15-min backup for critical mechanical systems                                                                     | 2              | 3              | 3              | 4               | 6               |


<!-- @benton REVIEW BATTERY CABINET COUNT: Equipment table specifies 32 battery cabinets for only 8 UPS modules (4:1 ratio). Industry standard is typically 1-2 cabinets per 500kW module. Is the 15-minute runtime requirement driving this high count? Verify with UPS vendor quotes. Potential cost optimization opportunity. -->

<!-- @benton VERIFY MECHANICAL UPS SIZING: 250 kW UPS × 4 units = 1 MW total capacity for Phase 4. Mechanical load analysis: 3× 5,000 kVA transformers = 4.2 MW total mechanical capacity. If critical mechanical loads (chillers, pumps) represent 30-40% of total = ~1.5 MW minimum requirement. Current specification may be undersized. Recommend load calculation review. -->

## GENERATOR SYSTEMS {TBC}

### Current Design Basis & Recommendation
The project's current design basis defaults to 4.3 MW natural gas turbines in a phased, N+1 architecture. This technology is the _default_ selection as it presents several key advantages:

1. **Permitting & ESG:** The significantly lower emissions profile is a critical advantage for air quality permitting and for aligning with investor ESG (Environmental, Social, and Governance) preferences.
2. **Runtime & Reliability:** The "unlimited" runtime via pipeline gas offers a superior reliability posture for extended utility outages compared to on-site diesel storage.    
3. **Day 1 Power Contingency:** This design provides crucial flexibility, allowing the turbines to operate in a prime power capacity if the utility grid connection is not available on Day 1.
4. **Revenue Generation:** It creates a future revenue opportunity by enabling participation in utility demand response programs.

However, this decision is **contingent** on the technical, financial, and client-acceptance factors outlined below. Natural gas turbines represent a higher capital expenditure than a diesel solution. A negative outcome in any of these areas (e.g., client rejection of turbine start-times, gas pipeline infeasibility) will force a pivot to a traditional diesel engine design.

### System Architecture (NatGas)
The generator system is designed as a unitized N+1 "power block." Each 4.3 MW turbine is paired 1:1 with a dedicated 5,000 kVA transformer and 7,000A switchboard. This N+1 redundancy chain is repeated in a modular "pay-as-you-grow" model for each phase, ensuring full concurrent maintainability.

_Design Note: The Phase 5 quantity of N=9 operating units + 1 redundant = 10 total units is a conservative design, providing 20% (6.3 MW) of headroom above the minimum N=8 requirement. This is far in the future and may change for cost savings, but we want to have enough yard space to accommodate all 10 units.

### Technical Justification & Risk Analysis (NatGas Basis)
The primary technical challenge of turbines is a 5-10 minute (300-600 second) startup time, versus 10-20 seconds for a diesel engine. This risk is a core trade-off for the emissions benefit.
- **Risk:** Generator start time exceeds UPS battery capacity.
- **Mitigation:** The facility's specified **15-minute (900-second) UPS battery runtime** provides a minimum 1.5x to 3x safety factor over the turbine's worst-case cold start. The UPS system is fully capable of bridging this gap, _assuming_ this 15-minute window is acceptable to the end-user.

### Key Factors & Final Decision Drivers
The final decision to proceed with natgas turbines or pivot to diesel is dependent on these three key factors:

1. **Client & Technical Acceptance:** We must confirm that our target tenants will accept natural gas as the backup power source. We also require a binding, contractual guarantee from the turbine vendor confirming the worst-case cold start-to-load acceptance time.
2. **Permitting & Grid Availability:** This design is contingent on two key schedule risks: **(a)** confirmation of the Day 1 availability of the utility grid and **(b)** the air permitting timeline for either generator type. If the grid is _not_ available on Day 1, the permitting path must be re-evaluated for a _prime power_ runtime, which is a significant schedule and cost risk.
3. **Fuel Availability & Reliability:** The team must confirm the pressure and capacity of the utility gas main. A separate, on-site gas compressor station may be required, which adds cost and complexity. The gas pipeline also represents a single point of failure, and this risk must be deemed acceptable over the high-reliability (but finite) on-site storage of diesel.

**Cost Analysis:**
- [[Diesel vs NatGas Generator CAPEX]] 
- [[Natural Gas Generator TCO with Demand Response Analysis]]

---

## UPS ARCHITECTURE

### System Configuration & Tier III Compliance
The design is a **2N (A/B) dual-path topology**, which is the industry standard for Tier III concurrent maintainability. Each path is independently redundant (N+1), ensuring no single point of failure and allowing an entire power train (e.g., A-Side) to be taken offline for maintenance while the B-Side supports 100% of the IT load.

- **Topology:** Dual independent A/B power trains.
- **Redundancy:** N+1 modular redundancy per A/B path.
- **Maintainability:** Fully concurrently maintainable.
- **Backup Duration:** 15 minutes at full load (bridges to generator startup).

```
A-Side UPS (N+1)   ←→   B-Side UPS (N+1)
      │                       │
      ▼                       ▼
A-Side Busway           B-Side Busway
      │                       │
      └──────→ Dual-Corded ←───┘
              IT Equipment
```

### UPS Technical Specifications
The system is built using 500 kW modular blocks, with 8 modules (4A + 4B) deployed for every 3 MW IT load block.

| **Component**     | **Specification**                             |
| ----------------- | --------------------------------------------- |
| **Power Module**  | 500 kW hot-swappable, double-conversion (VFI) |
| **Scaling**       | 8 modules per 3MW IT block (4A + 4B)          |
| **Efficiency**    | 96-97% (double-conversion), 98-99% (eco-mode) |
| **Voltage**       | 480V, 3-phase (Input & Output)                |
| **Battery Type**  | Li-Ion or VRLA (Vendor/TCO dependent)         |
| **Backup Time**   | 15 minutes at full load                       |
| **Configuration** | Distributed battery cabinets per UPS          |

<!-- @benton CONFIRM UPS OUTPUT VOLTAGE: Current spec shows 480V input AND output. This means dual transformation: 480V UPS → RPP (480V-208V step-down) → 208V racks. Verify this matches vendor quotes and is intentional vs. alternative of 480V input / 208V output UPS (single transformation). Dual transformation reduces efficiency but may improve distribution flexibility.   -->

---

## SWITCHBOARD EQUIPMENT

### Low Voltage Switchboards

- **IT Switchboards (SWBD):** 7,000A, 480V, 3-phase, 65kA SCCR
  - Phase 1: 2 units (one per IT transformer)
  - Phase 4: 5 units (one per IT transformer)
  - Phase 5: 10 units (one per IT transformer)
  - Each feeds overhead busway to data hall
  - **Design Note:** 7,000A bus rating required to accommodate 5,000 kVA transformer FLA of 6,014A at 480V. A 6,000A bus would be undersized with no safety margin; 7,000A is the next standard size, providing 16% margin for safe operation.

- **Mechanical Switchboards (MECH SWBD):** 480V, 3-phase, 35kA SCCR
  - Phase 1: 2× units at 2,000A (feeds chiller plant, pumps, support spaces)
  - Phase 4-5: 3× units at 6,000A (N+1 redundancy for mechanical loads)

### Distribution Architecture
- **IT Loads:** Each IT Switchboard feeds a dedicated overhead busway to the data hall, maintaining the A/B dual-path topology.
- **Mechanical Loads:** Switchboards feed chillers, pumps, and AHUs. Critical mechanical components (chillers, pumps) are provisioned with dual redundant A/B feeds.
- **Non-Critical Loads:** Support spaces (lighting, office HVAC) are fed from a single, non-redundant switchboard to optimize cost.
### Circuit Protection & Safety
- **Breakers:** Main and branch breakers will utilize electronic trip units for precise coordination and monitoring.
- **Arc Flash:** All equipment will have arc flash labels calculated per IEEE 1584 and NFPA 70E.

---

## ELECTRICAL MONITORING & CONTROLS (BMS/EPMS) {TBC}

### System Recommendation (BMS + EPMS)
To ensure operational visibility and optimize for the best IRR, the facility will not deploy a full-suite DCIM. Instead, monitoring will be handled by two integrated systems:
1. **Building Management System (BMS):** The primary "single pane of glass" for facility operations, focused on the mechanical plant (chillers, AHUs, environmental controls).
2. **Electrical Power Monitoring System (EPMS):** A specialized, high-speed system focused on the electrical power chain (breakers, UPS, generators, PDUs).
### Integration Architecture
The EPMS will monitor all electrical components and pass critical data and alarms to the BMS via a high-level interface (e.g., BACnet/IP). This provides a unified dashboard for the operations team without the high software licensing and integration costs of a single, all-encompassing DCIM.
- **Protocols:** BMS will use **BACnet/IP** (mechanical standard). EPMS will use **Modbus TCP/IP** (electrical standard).
- **Network:** All controls will operate on a physically separate, dual-path redundant IP network, fully isolated from IT and corporate traffic to ensure reliability.
### Monitoring Points
Monitoring is divided into two categories: critical alarms (for immediate action) and performance metrics (for optimization, billing, and PUE).

| **Category**            | **System** | **Monitored Points**                                                                                                                                                                                                                  |
| ----------------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Critical Alarms**     | EPMS       | Breaker Status (Open/Closed/Tripped) at all Switchboards<br><br>UPS Alarms (On Battery, Bypass, Fault)<br><br>Generator Status (Running, On-Load, Fault)<br><br>SPD (Surge Protection) Fault Alarms<br><br>RPP/PDU Main Breaker Trips |
| **Critical Alarms**     | BMS        | Chiller/Pump/Fan Faults<br><br>Water Flow & Leak Detection Alarms<br><br>High/Low Temperature & Humidity (per CRAC/CRAH)                                                                                                              |
| **Performance Metrics** | EPMS       | Per-Rack kW & kWh (for billing)<br><br>UPS Load (kW, %), Module Status, Battery String Health<br><br>Busway & Switchboard Load (V, A, kW)<br><br>Transformer Temperature                                                              |
| **Performance Metrics** | BMS        | Total Facility PUE (calculated)<br><br>Chiller Plant Efficiency (kW/ton)<br><br>Water Usage Effectiveness (WUE)                                                                                                                       |

---

## OUTDOOR ELECTRICAL ENCLOSURES

### Configuration
- **Type:** Weather-rated, factory-integrated containerized electrical enclosures.
- **Phasing:** Deployed in phases, starting with 2-3 enclosures for Phase 1 to house the A/B and mechanical systems.
- **Size:** ~12 ft × 55 ft per enclosure {TBC}.
- **Access:** Ground-level access for modular deployment and major equipment service.

<!-- @benton DEFINE ENCLOSURE PHASING PLAN: Total site capacity = 16 enclosures maximum. Equipment space analysis needed:
- Phase 1 (3 MW): 2-3 enclosures specified
- Phase 5 (24 MW): Must fit in 16 enclosures total
- Equipment per enclosure: 2× IT Switchboards (7,000A) + UPS modules + battery cabinets + mechanical switchboard
- Space constraint: Each enclosure ~12' × 55' = 660 sq ft
- Question: Can 16 enclosures accommodate 10× IT switchboards + 64× UPS modules + 256× battery cabinets + mechanical equipment?
- May require equipment density increase or reconfiguration in later phases.
Recommend detailed space planning before Phase 2 procurement. -->
### Equipment Housed
Enclosures are pre-fabricated to house the primary 480V distribution systems, maintaining physical separation between A/B paths. Contents include:
- IT Switchboards (per `SWITCHBOARD EQUIPMENT` section)
- UPS Modules & Frames (per `UPS ARCHITECTURE` section)
- UPS Battery Cabinets
- Mechanical Switchboards
- Associated Distribution Panels & Controls
### Environmental Protection
- **Climate Control:** Integrated, redundant N+1 HVAC to maintain 25°C ± 2°C.
- **Fire Suppression:** Integrated clean agent or pre-action systems per enclosure.
- **Weather Rating:** NEMA 3R minimum, sealed against moisture and dust.

### Maintenance Access & Serviceability {TBC}
- **Equipment Replacement Clearances:** Minimum 10 ft clearance on switchboard/UPS replacement side for rigging and equipment movement
- **Crane Access:** Mobile crane pad provisions for transformer and large UPS module replacement (50-ton capacity minimum)
- **Service Vehicle Access:** 20 ft wide access roads to all enclosure faces, load-rated for delivery trucks
- **Laydown Area:** Dedicated equipment staging area adjacent to enclosures (~2,000 sq ft minimum)
- **Design Consideration:** Outdoor enclosure siting must coordinate with site civil plan to ensure permanent access paths are maintained through all construction phases

<!-- @benton MAINTENANCE ACCESS: This section will likely move to Site & Infrastructure BOD (Div 31-32) or Procurement BOD (Div 00) during detailed design. Placeholder here for electrical equipment access requirements. -->

---

## MEDIUM VOLTAGE DISTRIBUTION {TBC}

### Voltage Level & Equipment
- **Voltage:** 13.8 kV, 3-phase.
- **Main Switchgear:** Arc-resistant metal-clad switchgear (per IEEE C37.20.7) located at the primary utility and generator yard.
- **Protective Relaying:** Microprocessor-based relays with arc flash detection.
- **Grounding:** Solidly grounded system per NEC Article 250.
### Distribution Topology
This diagram shows the primary N+1 power flow from the utility/generators to the low-voltage (480V) transformers.

```
Utility Service (138kV)
       │
       ▼
Main Substation (138kV / 13.8kV)
       │
       ▼
13.8kV Main Switchgear
       │
       ├─► Generator Paralleling Switchgear
       │        (Tied to 10x 4.3MW Gens)
       │
       └─► Feeds to 13.8kV Transformer Inputs
```
_Note: All Low Voltage (13.8kV / 480V) transformers are specified in the `TRANSFORMER SYSTEMS` section._

<!-- @benton CLARIFY GENERATOR PARALLELING STRATEGY:
- Are generators intended to parallel with utility (emergency paralleling with grid)?
- Or only parallel with each other during maintenance operations?
- What is the synchronization strategy during grid loss events?
- This affects: switchgear specification, protection relay settings, and utility interconnection agreement requirements.
Recommend coordination with utility (OG&E) on paralleling requirements. -->

## TRANSFORMER SYSTEMS {TBC}
Transformers are specified in two N+1 redundant groups: one for the IT load and one for the mechanical/cooling load. All transformers are 13.8kV-480Y/277V, VPI dry-type, and outdoor rated with forced-air cooling.
### IT Transformers (N+1)
- **Function:** Paired 1:1 with each 4.3 MW Generator to form a unitized N+1 power block.
- **Sizing:** 5,000 kVA. This rating is selected to support the 4.3 MW (4.78 MVA @ 0.9PF) generator output.
### Mechanical Transformers (N+1)
- **Function:** Provides N+1 power to the central mechanical plant (chillers, pumps, etc.).
- **Sizing:** 2,000 kVA (Phase 1) and 5,000 kVA (Phase 4-5)

**Note:** Substation transformer sizing addressed in [[11BOD - Utilities DC Critical (CSI Div 33)]].


---

## RACK POWER DISTRIBUTION {TBC}
Power is delivered from the 480V IT switchboards to the racks via a 2N (A/B) overhead busway system.
### A/B Distribution Path
The voltage is transformed from 480V to 208V at the row or rack level.
1. **480V Busway:** Overhead busways (800-1000A) are run in A/B pairs, fed from independent UPS trains.
2. **Rack Power Panels (RPPs):**
    - **Input:** Dual 480V feeds from A/B busway tap boxes.
    - **Transformer:** Integrated 480V-208V step-down transformer.
    - **Output:** 208V, 3-phase feeds to rack PDUs.
3. **Rack-Level Power:**
    - **PDUs:** Dual-corded vertical PDUs (one A, one B).
    - **Density:** Designed to support high-density AI (up to 132 kW/rack) and network (22 kW/rack) loads.
    - **Monitoring:** Per-outlet monitoring (kW, kWh, V, A) integrated with the BMS/EPMS.


---

## ELECTRICAL REDUNDANCY & FAULT TOLERANCE SUMMARY {TBC}
This section summarizes the project's adherence to a Tier III-compliant design.
### Redundancy Model
All critical systems—Generators, IT Transformers, IT Switchboards, and UPS modules—are deployed in a phased **N+1 'block' architecture** as defined in their respective sections. The IT power distribution from the UPS to the rack is a **2N (dual-path)** topology.
### Concurrent Maintainability
The 2N (A/B) dual-path design allows for an entire power train to be taken offline for maintenance, testing, or repair without impacting the IT load.
- **Maintenance Scenario:** The A-Side UPS, switchboard, and busway can be completely de-energized for service while the B-Side systems carry 100% of the facility load.
### Intentionally Accepted Single Points of Failure
To optimize cost and complexity, the following are accepted single points of failure:
- **Utility Service Entry:** A single utility substation feeds the facility. This is mitigated by the N+1 generator plant, which is designed to assume the entire facility load upon utility failure.
- **Rack-Level:** Any single-corded IT equipment deployed by the customer. The facility provides A/B power to the rack; the customer is responsible for deploying dual-corded servers.

---

## GROUNDING & LIGHTNING PROTECTION {TBC}

### Electrical Grounding
- **Ground Electrode System:** Building steel, concrete-encased electrode (Ufer ground), ground ring, driven rods
- **Target Resistance:** <5 ohms (measured via fall-of-potential test)
- **TIA-942 Compliance:** Telecommunications grounding per TIA-607-C
- **Isolated Ground:** Dedicated isolated ground for IT equipment (if required by customer)
### Lightning Protection
- **Roof-Level Air Terminals:** Lightning rods per NFPA 780 or UL 96A
- **Down Conductors:** Minimum 2 down conductors, bonded to building ground system
- **Surge Protection Devices (SPDs):**
  - Utility service entrance (Type 1 SPD)
  - Main switchboards (Type 2 SPD)
  - Rack PDUs (optional Type 3 SPD for sensitive equipment)

---

## ELECTRICAL/MECHANICAL SEPARATION

### Equipment Yard Organization
- **Electrical Equipment:**
  - Outdoor containerized electrical enclosures (2-3 units)
  - Generator yard
- **Mechanical Equipment:**
  - Chiller yard
  - Pumping equipment
  - CDU access

**Layout:** Equipment yard organization and side placement TBD during detailed design

**Benefits:**
- Clear separation of electrical and mechanical equipment
- Outdoor enclosures eliminate indoor space requirements
- Shorter cable/pipe runs within each discipline
- Easier equipment expansion and replacement

---

## COST ESTIMATION METHODOLOGY

### Equipment Cost Confidence Assessment (2025 Market Basis)

| Component | Unit Size/Rating | Confidence Level | Low Estimate | Mid Estimate | High Estimate | Key Risk Factors |
|-----------|------------------|------------------|--------------|--------------|---------------|------------------|
| **Natural Gas Turbine Generator** | 4.3 MW (installed) | Medium (70%) | $3.13M ($728/kW) | $3.72M ($867/kW) | $6.64M ($1,544/kW) | 5-7 year lead times; supply shortages; EIA data shows $824-875/kW but market at $1,200-2,500/kW |
| **IT Transformer** | 5,000 kVA dry-type | Medium (75%) | $40,000 | $55,000 | $75,000 | 44% price increase since 2021; 2-4 year lead times; copper/steel volatility |
| **Mechanical Transformer** | 2,000 kVA dry-type | Medium (75%) | $16,000 | $22,000 | $28,000 | Same market conditions as IT transformers |
| **IT Switchboard** | 7,000A @ 480V, 65kA SCCR | Low (50%) | $85,000 | $125,000 | $175,000 | Custom configuration; 50% price increase since 2021; 46-48 week lead times |
| **Mechanical Switchboard** | 6,000A @ 480V, 35kA SCCR | Low (50%) | $70,000 | $105,000 | $150,000 | Custom quotes required; manufacturer-dependent |
| **Mechanical Switchboard** | 2,000A @ 480V, 35kA SCCR | Low (50%) | $18,000 | $28,000 | $42,000 | Limited public pricing data |
| **UPS Module + Battery Cabinet** | 500 kW module w/ 15-min battery | Medium (65%) | $300,000 | $450,000 | $600,000 | New products (Schneider Galaxy VXL); range $600-1,200/kW industry standard |
| **Mechanical UPS** | 250 kW w/ batteries | Medium (65%) | $200,000 | $250,000 | $300,000 | Flywheel or battery-based; $800-1,200/kW typical |
| **Containerized Enclosure** | ~12' × 55' E-house | Medium (60%) | $50,000 | $150,000 | $300,000 | $50-300/sq ft based on complexity; HVAC/fire suppression included |
| **MV Switchgear** | 13.8kV arc-resistant | Low (50%) | $60,000 | $100,000 | $180,000 | Custom design; limited 2025 public quotes |
| **Generator Paralleling Switchgear** | 13.8kV (complete system) | Low (40%) | $500,000 | $750,000 | $1,000,000 | Highly custom; protection relay complexity |
| **Overhead Busway** | 800-1000A @ 480V (per 100 LF) | Low (50%) | $8,000 | $12,000 | $18,000 | Installation $80-150/LF typical; project-dependent |

**Cost Basis:** October 2025 USD, Tulsa/Oklahoma market. Labor rates: IBEW Local 584 (Tulsa).
**Confidence Definitions:** High (>80% likely within range), Medium (60-80%), Low (<60% - requires vendor quotes).
**Market Context:** Electrical equipment costs up 44-50% since Q3 2021; lead times at historic highs (transformers 2-4 years, turbines 5-7 years).

---

## PHASED COST ESTIMATES

### Phase 1: 3 MW IT Load (Day One Build)

| Equipment Item | Qty | Unit Cost (Mid) | Subtotal | Notes |
|----------------|-----|-----------------|----------|-------|
| **Power Generation** |
| Natural Gas Turbine Generator (4.3 MW) | 2 | $3,720,000 | $7,440,000 | N+1 for 4.05 MW facility load |
| Generator Paralleling Switchgear | 1 system | $750,000 | $750,000 | 13.8kV system for 2 units |
| **Transformation** |
| IT Transformer (5,000 kVA) | 2 | $55,000 | $110,000 | One per generator |
| Mechanical Transformer (2,000 kVA) | 2 | $22,000 | $44,000 | N+1 for mechanical loads |
| **UPS Systems** |
| UPS Module + Battery (500 kW) | 8 | $450,000 | $3,600,000 | 4A + 4B configuration |
| Mechanical UPS (250 kW) | 2 | $250,000 | $500,000 | Critical mechanical controls |
| **Distribution** |
| IT Switchboard (7,000A) | 2 | $125,000 | $250,000 | One per IT transformer |
| Mechanical Switchboard (2,000A) | 2 | $28,000 | $56,000 | N+1 for mech loads |
| MV Switchgear (13.8kV main) | 1 system | $100,000 | $100,000 | Main utility interconnect |
| Overhead Busway (800-1000A, 500 LF est.) | 5 | $12,000 | $60,000 | Data hall distribution |
| **Enclosures & Infrastructure** |
| Containerized Electrical Enclosure | 3 | $150,000 | $450,000 | A-side, B-side, mechanical |
| Rack Power Panels (RPPs) | 40 | $8,000 | $320,000 | 480V-208V step-down |
| **Installation & Other** |
| Electrical installation labor (20% of equipment) | - | - | $2,736,000 | IBEW Local 584 rates |
| Commissioning services (3% of equipment) | - | - | $410,400 | FAT, SAT, integrated testing |
| Arc flash study & PPE | 1 | $75,000 | $75,000 | IEEE 1584 / NFPA 70E |
| Spare parts inventory | 1 lot | $300,000 | $300,000 | UPS modules, batteries, breakers |
| **Phase 1 Subtotal** | | | **$17,201,400** | |
| **Contingency (15%)** | | | **$2,580,210** | Class 3 estimate (+/- 15-20%) |
| **Phase 1 TOTAL** | | | **$19,781,610** | **~$19.8M** |

<!-- @benton PHASING TABLE REVIEW: Does this Phase 1 breakdown clearly show what's needed for Day One? Equipment quantities match the equipment list table. Current estimate ~$19.8M vs. original $11-16M - significant increase driven by 2025 market research showing generator costs 50-150% higher than original estimate. -->

---

### Phase 2: 6 MW IT Load (Cumulative)

| Equipment Item | Qty Added | Unit Cost (Mid) | Phase 2 Incremental | Cumulative Total |
|----------------|-----------|-----------------|---------------------|------------------|
| **Power Generation** |
| Natural Gas Turbine Generator (4.3 MW) | +1 | $3,720,000 | $3,720,000 | 3 units total |
| Generator Paralleling Switchgear expansion | 1 bay | $200,000 | $200,000 | Expanded for 3 units |
| **Transformation** |
| IT Transformer (5,000 kVA) | +1 | $55,000 | $55,000 | 3 units total |
| Mechanical Transformer (2,000 kVA) | 0 | - | - | 2 units sufficient |
| **UPS Systems** |
| UPS Module + Battery (500 kW) | +8 | $450,000 | $3,600,000 | 16 units total (8A + 8B) |
| Mechanical UPS (250 kW) | +1 | $250,000 | $250,000 | 3 units total |
| **Distribution** |
| IT Switchboard (7,000A) | +1 | $125,000 | $125,000 | 3 units total |
| Mechanical Switchboard (2,000A) | 0 | - | - | 2 units sufficient |
| Overhead Busway (additional 300 LF) | +3 | $12,000 | $36,000 | - |
| **Enclosures & Infrastructure** |
| Containerized Electrical Enclosure | +1 | $150,000 | $150,000 | 4 units total |
| Rack Power Panels (RPPs) | +40 | $8,000 | $320,000 | 80 total |
| **Installation & Other** |
| Electrical installation labor (20%) | - | - | $1,691,200 | - |
| Commissioning services (3%) | - | - | $253,680 | - |
| **Phase 2 Incremental** | | | **$10,400,880** | |
| **Contingency (15%)** | | | **$1,560,132** | |
| **Phase 2 Total** | | | **$11,961,012** | **~$12.0M** |
| **Cumulative Through Phase 2** | | | **$31,742,622** | **~$31.7M** |

---

### Phase 3: 9 MW IT Load (Cumulative)

| Equipment Item | Qty Added | Unit Cost (Mid) | Phase 3 Incremental | Cumulative Total |
|----------------|-----------|-----------------|---------------------|------------------|
| **Power Generation** |
| Natural Gas Turbine Generator (4.3 MW) | +1 | $3,720,000 | $3,720,000 | 4 units total |
| Generator Paralleling Switchgear expansion | 1 bay | $200,000 | $200,000 | Expanded for 4 units |
| **Transformation** |
| IT Transformer (5,000 kVA) | +1 | $55,000 | $55,000 | 4 units total |
| Mechanical Transformer (5,000 kVA - UPSIZE) | +1 | $55,000 | $55,000 | 3× 5,000 kVA replaces 2× 2,000 kVA |
| **UPS Systems** |
| UPS Module + Battery (500 kW) | +8 | $450,000 | $3,600,000 | 24 units total (12A + 12B) |
| Mechanical UPS (250 kW) | 0 | $250,000 | - | 3 units sufficient |
| **Distribution** |
| IT Switchboard (7,000A) | +1 | $125,000 | $125,000 | 4 units total |
| Mechanical Switchboard (6,000A - UPSIZE) | +1 | $105,000 | $105,000 | 3× 6,000A replaces 2× 2,000A |
| Overhead Busway (additional 300 LF) | +3 | $12,000 | $36,000 | - |
| **Enclosures & Infrastructure** |
| Containerized Electrical Enclosure | +2 | $150,000 | $300,000 | 6 units total |
| Rack Power Panels (RPPs) | +40 | $8,000 | $320,000 | 120 total |
| **Installation & Other** |
| Electrical installation labor (20%) | - | - | $1,703,200 | - |
| Commissioning services (3%) | - | - | $254,880 | - |
| **Phase 3 Incremental** | | | **$10,473,080** | |
| **Contingency (15%)** | | | **$1,570,962** | |
| **Phase 3 Total** | | | **$12,044,042** | **~$12.0M** |
| **Cumulative Through Phase 3** | | | **$43,786,664** | **~$43.8M** |

---

### Phase 4: 12 MW IT Load (Cumulative)

| Equipment Item                             | Qty Added | Unit Cost (Mid) | Phase 4 Incremental | Cumulative Total           |
| ------------------------------------------ | --------- | --------------- | ------------------- | -------------------------- |
| **Power Generation**                       |           |                 |                     |                            |
| Natural Gas Turbine Generator (4.3 MW)     | +1        | $3,720,000      | $3,720,000          | 5 units total              |
| Generator Paralleling Switchgear expansion | 1 bay     | $200,000        | $200,000            | Expanded for 5 units       |
| **Transformation**                         |           |                 |                     |                            |
| IT Transformer (5,000 kVA)                 | +1        | $55,000         | $55,000             | 5 units total              |
| Mechanical Transformer (5,000 kVA)         | 0         | -               | -                   | 3 units sufficient (N+1)   |
| **UPS Systems**                            |           |                 |                     |                            |
| UPS Module + Battery (500 kW)              | +8        | $450,000        | $3,600,000          | 32 units total (16A + 16B) |
| Mechanical UPS (250 kW)                    | +1        | $250,000        | $250,000            | 4 units total              |
| **Distribution**                           |           |                 |                     |                            |
| IT Switchboard (7,000A)                    | +1        | $125,000        | $125,000            | 5 units total              |
| Mechanical Switchboard (6,000A)            | 0         | -               | -                   | 3 units sufficient (N+1)   |
| Overhead Busway (additional 300 LF)        | +3        | $12,000         | $36,000             | -                          |
| **Enclosures & Infrastructure**            |           |                 |                     |                            |
| Containerized Electrical Enclosure         | +2        | $150,000        | $300,000            | 8 units total              |
| Rack Power Panels (RPPs)                   | +40       | $8,000          | $320,000            | 160 total                  |
| **Installation & Other**                   |           |                 |                     |                            |
| Electrical installation labor (20%)        | -         | -               | $1,721,200          | -                          |
| Commissioning services (3%)                | -         | -               | $258,180            | -                          |
| **Phase 4 Incremental**                    |           |                 | **$10,585,380**     |                            |
| **Contingency (15%)**                      |           |                 | **$1,587,807**      |                            |
| **Phase 4 Total**                          |           |                 | **$12,173,187**     | **~$12.2M**                |
| **Cumulative Through Phase 4**             |           |                 | **$55,959,851**     | **~$56.0M**                |

---

### Phase 5: 20-24 MW IT Load Ultimate (Cumulative)

| Equipment Item | Qty Added | Unit Cost (Mid) | Phase 5 Incremental | Cumulative Total |
|----------------|-----------|-----------------|---------------------|------------------|
| **Power Generation** |
| Natural Gas Turbine Generator (4.3 MW) | +5 | $3,720,000 | $18,600,000 | 10 units total (N=9 + 1 redundant) |
| Generator Paralleling Switchgear expansion | 5 bays | $200,000 | $1,000,000 | Expanded for 10 units |
| **Transformation** |
| IT Transformer (5,000 kVA) | +5 | $55,000 | $275,000 | 10 units total |
| Mechanical Transformer (5,000 kVA) | 0 | - | - | 3 units sufficient (N+1) |
| **UPS Systems** |
| UPS Module + Battery (500 kW) | +32 | $450,000 | $14,400,000 | 64 units total (32A + 32B) |
| Mechanical UPS (250 kW) | +2 | $250,000 | $500,000 | 6 units total |
| **Distribution** |
| IT Switchboard (7,000A) | +5 | $125,000 | $625,000 | 10 units total |
| Mechanical Switchboard (6,000A) | 0 | - | - | 3 units sufficient (N+1) |
| Overhead Busway (additional 1,000 LF) | +10 | $12,000 | $120,000 | Ultimate build-out |
| **Enclosures & Infrastructure** |
| Containerized Electrical Enclosure | +8 | $150,000 | $1,200,000 | 16 units total (site max) |
| Rack Power Panels (RPPs) | +200 | $8,000 | $1,600,000 | 360 total |
| **Installation & Other** |
| Electrical installation labor (20%) | - | - | $7,664,000 | - |
| Commissioning services (3%) | - | - | $1,149,600 | - |
| Transformer/Switchboard decommissioning | - | - | $150,000 | Remove old 2,000 kVA units from Phase 1 |
| **Phase 5 Incremental** | | | **$47,283,600** | |
| **Contingency (15%)** | | | **$7,092,540** | |
| **Phase 5 Total** | | | **$54,376,140** | **~$54.4M** |
| **ULTIMATE BUILD-OUT TOTAL (All Phases)** | | | **$110,335,991** | **~$110.3M** |

---

### Cost Summary Across All Phases

| Phase | IT Load | Incremental Cost | Cumulative Cost | $/kW IT Load | Key Drivers |
|-------|---------|------------------|-----------------|--------------|-------------|
| **Phase 1** | 3 MW | $19.8M | $19.8M | $6,594/kW | Initial infrastructure + 2 turbines + dual UPS trains |
| **Phase 2** | 6 MW | $12.0M | $31.7M | $5,289/kW | +1 turbine, +8 UPS modules, +1 enclosure |
| **Phase 3** | 9 MW | $12.0M | $43.8M | $4,865/kW | +1 turbine, +8 UPS, mechanical system upsize |
| **Phase 4** | 12 MW | $12.2M | $56.0M | $4,663/kW | +1 turbine, +8 UPS, system optimization |
| **Phase 5** | 20-24 MW | $54.4M | $110.3M | $4,595/kW (avg) | +5 turbines, +32 UPS, ultimate build-out |

**Key Observations:**
- **Phase 1 $/kW premium:** 43% higher than ultimate blended cost due to fixed infrastructure costs (switchgear, enclosures, commissioning)
- **Ultimate $/kW cost:** $4,595/kW competitive vs. industry benchmark of $9,300-$15,000/kW (San Antonio-Reno range), driven by:
  - Natural gas turbines (lower $/kW than diesel)
  - Modular phasing (no stranded capacity)
  - Outdoor containerized enclosures (lower cost than building integration)
- **Major cost variance risk:** Natural gas turbines ($3.1M-$6.6M range per unit) represent 40-50% of total electrical budget
- **Lead time critical path:** Turbines (5-7 years), transformers (2-4 years) require early procurement lockdown

**Recommendation:** Execute turbine and transformer contracts with locked pricing and delivery schedules before final financing close to manage cost/schedule risk.

---

**Tags:** #saga-project #electrical #traditional-ups #tier3-compliance #generators #distribution #csi-division-26

**Related Documents:**
- [[_BOD - Exec Summary and TOC]] - Main title page
- [[Why BESS Should Not Be UPS]] - Technical analysis rejecting BESS-as-UPS
- [[Excess Solar Monetization Strategy]] - Economic BESS evaluation (rejected)
- [[12BOD - Process Equipment (CSI Divs 40-48)]] - Generator and solar details
- [[11BOD - Utilities DC Critical (CSI Div 33)]] - Utility interconnection
- [[Architectural Meeting Changes by CSI Division]] - October 2025 updates
