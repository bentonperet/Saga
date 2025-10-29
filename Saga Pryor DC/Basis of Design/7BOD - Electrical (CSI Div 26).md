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
- UPS: N+1 modular UPS with dual paths A/B (Phase 1: 6MW N+1 for $4.5M, ultimate 28MW for $26.3M total) {TBC}
- UPS Topology: Dual A/B busways, concurrent maintainability
- Generators: 5-6 units (N+1 redundancy), fuel type TBD based on grid availability <!-- there's a decision tree here and multiple options / tradeoffs, including demand response participation, power availability, etc.-->
- Generator Fuel: Diesel (if grid Day 1) or natural gas turbine (if no grid Day 1)
- Electrical Enclosures: Outdoor containerized (2-3 units, ~12 ft × 55 ft each {TBC})
- Distribution: 480V overhead busway or whips  {TBD by the client}
- Electrical Code: NEC 2023, Oklahoma amendments


---

## EQUIPMENT LIST

<!-- Start with switch ATL electrical design to create the equipment list - ex: each chiller is tuned to the market (we can specify by size and generic) -->

**Phasing Reminder**

| Phase | IT Load | Facility Load (PUE 1.2-1.35) |
| ----- | ------- | ---------------------------- |
| **1** | 3MW     | 3.6-4.05 MW                  |
| **2** | 6MW     | 7.2-8.1 MW                   |
| **3** | 9MW     | 10.8-12.15 MW                |
| **4** | 12MW    | 14.4-16.2 MW                 |
| **5** | 20-24MW | 24.0-32.4 MW                 |

### List of Equipment for Natural Gas Generation

| Equipment                | Location        | Description                                                                                                                     | Phase1 Qty 3MW | Phase4 Qty 12MW | Phase5 Qty 24MW |
| ------------------------ | --------------- | ------------------------------------------------------------------------------------------------------------------------------- | -------------- | --------------- | --------------- |
| Generator                | Outdoor         | 4.3 MW Natural Gas Turbine Generator                                                                                            | 2              | 5               | 10              |
| IT Transformer           | Outdoor         | 5,000 kVA, 13.8kV-480Y/277V, VPI dry-type, outdoor rated, 5.75% impedance, forced air cooling, feeds IT switchboards      | 2              | 5               | 10               |
| Mechanical Transformer   | Outdoor         | 2,000 kVA (Phase 1) or 5,000 kVA (Phase 4-5), 13.8kV-480Y/277V, VPI dry-type, outdoor rated, 5.75% impedance, feeds mechanical loads (chillers, pumps, etc.) | 2              | 3               | 3               |
| IT Switchboard           | Electrical Shed | 6,000A, 480V, 3-phase, 65kA SCCR, main lug or breaker, feeds overhead busway to data hall                                 | 2              | 5               | 10               |
| UPS Module               | Electrical Shed | 500 kW modular hot-swappable UPS, double-conversion, 96-97% efficiency, 480V input/output, dual A/B paths (N+1 per path)  | 8              | 32              | 64              |
| UPS Battery Cabinet      | Electrical Shed | Lithium-ion or VRLA battery cabinet, 15-min backup at full load, distributed per UPS module                                     | 32             | 128              | 256             |
| Mechanical Switchboard   | Mechanical Room | 2,000A (Phase 1) or 6,000A (Phase 4-5), 480V, 3-phase, 35kA SCCR, feeds chiller plant, pumps, DX units, support HVAC                                      | 2              | 3               | 3               |
| Mechanical UPS           | Mechanical Room | 250 kW UPS for critical mechanical controls, pumps, BMS, 480V input, dual-conversion, N+1 configuration                     | 2              | 4               | 6               |
| Mechanical UPS Batteries | Mechanical Room | VRLA or Li-ion batteries for mechanical UPS, 15-min backup for critical mechanical systems                                      | 2              | 4               | 6               |


## TRADITIONAL N+1 UPS ARCHITECTURE WITH DUAL POWER PATHS {TBC}

### System Configuration

**Dual-Path Modular UPS Topology (A-Side / B-Side)**
- **Configuration:** Dual independent UPS trains (A and B) feed separate power paths to IT equipment
- **Redundancy:** Each path N+1 (multiple UPS modules per side, any one can fail without impact)
- **Concurrent Maintainability:** Can take entire A-side offline for maintenance while B-side carries full load
- **Backup Duration:** 15 minutes at full load (bridges to generator startup)

### UPS Technical Specifications

**Power Modules:**
- **Type:** Modular hot-swappable UPS modules (500 kW per module)
- **Topology:** Double-conversion online UPS (VFI per IEC 62040-3)
- **Efficiency:** 96-97% at full load, 98-99% in eco-mode
- **Input:** 480V, 3-phase
- **Output:** 480V, 3-phase for overhead busway distribution
- **Scaling:** 8 modules per 3 MW IT load block (4 modules per A/B side, N+1 redundancy per side)

**Battery Systems:**
- **Type:** Valve-Regulated Lead-Acid (VRLA) or Lithium-Ion (vendor-dependent)
- **Backup Time:** 15 minutes at full load
- **Replacement Cycle:** VRLA (5-7 years), Li-Ion (10-12 years)
- **Configuration:** Distributed battery cabinets per UPS module
- **Maintenance:** Individual module replacement ($50-100K) vs forklift BESS upgrade ($4M+)

**Recommended UPS Vendors:**
- **Schneider Electric Galaxy VX/VL:** Proven data center platform, strong service network
- **Eaton 93PM/93PR:** Modular design, high efficiency
- **Vertiv Liebert EXL S1:** Compact footprint, scalable

### TIER III Compliance

**Concurrent Maintainability:**
```
A-Side UPS (Modules 1-5)  ←→  B-Side UPS (Modules 6-10)
        │                              │
        ▼                              ▼
   A-Side Busway                  B-Side Busway
        │                              │
        └──────→ Dual-Corded ←─────────┘
                 IT Equipment
```

**Maintenance Scenario:**
1. Transfer all load to B-Side
2. Take A-Side offline for UPS module replacement, battery service, or firmware updates
3. B-Side carries 100% facility load (no IT impact)
4. Return A-Side to service, transfer load back to balanced A+B operation

**Why This Works:**
- No single point of failure (loss of A or B does not impact IT)
- Concurrently maintainable (service either side without downtime)
- Proven topology (40+ years track record, thousands of deployments)
- Lender acceptance (no exotic risk premium, standard DC design)

---

## OUTDOOR CONTAINERIZED ELECTRICAL ENCLOSURES

### Configuration
- **Type:** Weather-rated containerized electrical enclosures
- **Quantity:** 2-3 outdoor enclosures (A-side, B-side, +1 optional)
- **Size:** ~12 ft × 55 ft per enclosure {TBC}
- **Access:** Ground-level access for equipment delivery and maintenance

### Equipment Housed in Electrical Enclosures
- **UPS Modules:** A-side and B-side UPS frames with hot-swappable modules
- **Battery Cabinets:** Distributed battery strings per UPS module
- **IT Switchboards (SWBD):** 4× units, 4,000A, 480V, 65kA SCCR
- **Mechanical Switchboards (MECH SWBD):** 2× units, 1,600A, 480V, 35kA SCCR
- **Distribution Panels:** Branch circuit distribution
- **Protective Relaying:** Microprocessor-based relays with arc flash detection

### Environmental Protection
- **Climate Control:** Integrated HVAC within containers (maintains 25°C ± 2°C)
- **Fire Suppression:** Integrated clean agent or pre-action systems per enclosure
- **Weather Rating:** NEMA 3R or better, sealed against moisture and dust
- **Ventilation:** Forced air cooling with redundant fans

---

## SWITCHBOARD EQUIPMENT - RETAINED {TBC}

### Low Voltage Switchboards
- **IT Switchboards (SWBD):** 6,000A, 480V, 3-phase, 65kA SCCR
  - Phase 1: 2 units (one per IT transformer)
  - Phase 4: 5 units (one per IT transformer)
  - Phase 5: 10 units (one per IT transformer)
  - Each feeds overhead busway to data hall
- **Mechanical Switchboards (MECH SWBD):** 480V, 3-phase, 35kA SCCR
  - Phase 1: 2× units at 2,000A (feeds chiller plant, pumps, support spaces)
  - Phase 4-5: 3× units at 6,000A (N+1 redundancy for mechanical loads)

### Distribution Architecture
- Each IT switchboard feeds overhead busway running through data hall
- Mechanical switchboards feed chillers, pumps, AHUs, support spaces
- Critical mechanical loads (chillers, pumps) have dual redundant feeds (A+B)
- Non-critical loads (lighting, office HVAC) fed from single switchboard

### Circuit Protection
- Main breakers: Molded-case or insulated-case breakers with electronic trip units
- Branch breakers: Thermal-magnetic or electronic trip
- Arc flash labels: Calculated per IEEE 1584 and NFPA 70E

---

## GENERATOR SYSTEMS {TBC}

### Fuel Type Selection

**Option A - Diesel Generators (if grid power available Day 1):**
- **Count:** 5-6 units (N+1 for IT load + 1 for mechanical)
- **Fuel:** Belly tanks or above-ground storage (48-hour minimum)
- **Rationale:** Lower CAPEX, rare runtime (utility backup only)

**Option B - Natural Gas Turbine (if no grid power Day 1):**
- **Count:** 2-3 turbines (~4.3 MW each) + 1 diesel for mechanical
- **Fuel:** Pipeline natural gas (unlimited runtime)
- **Rationale:** Must run nightly to cover solar gap, diesel fuel costs prohibitive
- **Temporary Option:** Mobile turbine until permanent units commissioned

**Decision Driver:** Grid availability at facility opening determines fuel type

**Cost Analysis:** See [[Diesel vs NatGas Generator CAPEX]] for detailed comparison

### Generator Yard
- **Layout:** Horizontal arrangement, 8-10 ft clearances between units
- **Enclosures:** Sound-attenuated (75 dBA @ 23 ft per RD109)
- **Fuel Storage:** Diesel belly tanks (Option A) or NG pipeline connection (Option B)

---

## MEDIUM VOLTAGE DISTRIBUTION {TBC}

### Voltage Level & Equipment
- **Voltage:** 13.8 kV, 3-phase
- **Main Switchgear:** Arc-resistant metal-clad switchgear per IEEE C37.20.7
- **Protective Relaying:** Microprocessor-based relays with arc flash detection and trip
- **Grounding:** Solidly grounded system per NEC Article 250

### Distribution Topology
- Utility service → 138kV/13.8kV transformer → Main switchgear
- Main switchgear → Generator paralleling switchgear
- Generator switchgear → IT transformers (Phase 1: 2×, Phase 4: 5×, Phase 5: 10× at 5,000 kVA each)
- Generator switchgear → Mechanical transformers (Phase 1: 2× at 2,000 kVA, Phase 4-5: 3× at 5,000 kVA)

### Transformer Specifications
- **IT Transformers:** 5,000 kVA, 13.8kV-480Y/277V, VPI dry-type, outdoor rated
  - Phase 1: 2 units (N+1 for 4.3 MW generator blocks)
  - Phase 4: 5 units (N+1 for 4.3 MW generator blocks)
  - Phase 5: 10 units (N+1 for 4.3 MW generator blocks)
- **Mechanical Transformers:** 13.8kV-480Y/277V, VPI dry-type, outdoor rated
  - Phase 1: 2× 2,000 kVA (supports ~1.05 MW mechanical load)
  - Phase 4-5: 3× 5,000 kVA (N+1 redundancy, supports 4.2-8.4 MW mechanical load)
- **Impedance:** 5.75% typical
- **Cooling:** Dry-type, forced air (fans for overload conditions)
- **Design Note:** IT transformer sizing (5,000 kVA) is matched to 4.3 MW generator output to ensure proper power delivery through the N+1 redundancy chain

**Note:** Substation transformer sizing addressed in [[11BOD - Utilities DC Critical (CSI Div 33)]].

---

## RACK POWER DISTRIBUTION {TBC}

### Overhead Busway System
- **Voltage:** 480V, 3-phase, 4-wire
- **Capacity:** 800-1000A per busway run (sized for rack density + growth)
- **Routing:** Parallel to hot aisles, mounted at ~12-14 ft elevation
- **Redundancy:** Dual feeds (A+B busway from independent UPS trains)
- **Manufacturer:** Starline, Eaton, or equivalent

### Rack Power Panels (RPPs)
- **Input:** 480V from A+B busway
- **Output:** 208V, 3-phase for rack PDUs
- **Transformer:** Integrated 480V-208V step-down transformer
- **Protection:** Branch circuit breakers with remote monitoring
- **Redundancy:** Dual-corded equipment receives A+B feeds

### Rack-Level Power
- **Power Density:**
  - AI racks: Up to 132 kW/rack (liquid-cooled)
  - Network racks: Up to 22 kW/rack (air-cooled with RDHx)
- **PDU Configuration:** Vertical rack-mount PDUs, dual-corded for redundancy
- **Outlets:** C13/C19 or high-density outlets per customer requirements
- **Monitoring:** Real-time kW, kWh, voltage, current, power factor per rack (integrated with DCIM)

---

## ELECTRICAL REDUNDANCY & FAULT TOLERANCE {TBC}

### N+1 Redundancy with Dual Power Paths
- **UPS:** Dual paths (A-side and B-side independent trains, each N+1 within path)
  - Phase 1: 8 modules (4A + 4B)
  - Phase 4: 32 modules (16A + 16B)
  - Phase 5: 64 modules (32A + 32B)
- **Generators:** N+1 configuration (Phase 1: 2, Phase 4: 5, Phase 5: 10 units at 4.3 MW each)
- **Transformers:** IT transformers match generator quantities for complete N+1 chain (Phase 1: 2, Phase 4: 5, Phase 5: 10 at 5,000 kVA each)
- **Switchboards:** IT switchboards match transformer quantities (Phase 1: 2, Phase 4: 5, Phase 5: 10 at 6,000A each)

### Dual Power Paths to Racks
- **A-Side:** Utility/Gen → TX-A → UPS-A → SWBD-A → Busway-A → RPP-A → Rack PDU-A
- **B-Side:** Utility/Gen → TX-B → UPS-B → SWBD-B → Busway-B → RPP-B → Rack PDU-B
- Dual-corded IT equipment receives both A and B feeds (automatic failover)

### Concurrent Maintainability
- Can take entire A-side UPS offline for maintenance → B-side carries full load
- Can take entire B-side UPS offline for maintenance → A-side carries full load
- Maintenance performed without impacting IT load (zero downtime)
- Procedures documented in O&M manuals

### Single Points of Failure (Intentionally Accepted)
- Utility service entry (mitigated by generators for backup)
- Rack-level single-corded equipment (customer responsibility to deploy dual-corded servers)

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

## PHASED DEPLOYMENT INFRASTRUCTURE {TBC}

### Phase 1 (Build Day One - 3 MW IT Load)
- Substation transformer: 15-20 MVA (sized for ultimate capacity)
- 13.8kV switchgear: Sized for ultimate load
- UPS: 8 modules (500 kW each, 4A + 4B for N+1 per side)
- IT Transformers: 2 units at 5,000 kVA each
- IT Switchboards: 2 units at 6,000A each
- Generators: 2 units at 4.3 MW each (N+1 configuration)
- Mechanical Transformers: 2 units at 2,000 kVA each
- Mechanical Switchboards: 2 units at 2,000A each
- Mechanical UPS: 2 units at 250 kW each
- Electrical enclosures: 2-3 outdoor containerized enclosures (houses Phase 1 equipment)

### Phase 2-3 (6 MW and 9 MW IT Load)
- Add UPS modules to existing frames (maintaining N+1 per side)
- Add generators, transformers, and switchboards as needed for intermediate phases

### Phase 4 (12 MW IT Load)
- UPS: Total 32 modules (16A + 16B)
- IT Transformers: Total 5 units at 5,000 kVA each (maintains N+1 chain)
- IT Switchboards: Total 5 units at 6,000A each (maintains N+1 chain)
- Generators: Total 5 units at 4.3 MW each (N+1 configuration)
- Mechanical Transformers: Total 3 units at 5,000 kVA each (N+1 for mech load)
- Mechanical Switchboards: Total 3 units at 6,000A each
- Mechanical UPS: Total 4 units at 250 kW each

### Phase 5 (24 MW IT Load - Ultimate)
- UPS: Total 64 modules (32A + 32B)
- IT Transformers: Total 10 units at 5,000 kVA each (maintains N+1 chain)
- IT Switchboards: Total 10 units at 6,000A each (maintains N+1 chain)
- Generators: Total 10 units at 4.3 MW each (N+1 configuration)
- Mechanical Transformers: 3 units at 5,000 kVA each (N+1 for mech load)
- Mechanical Switchboards: 3 units at 6,000A each
- Mechanical UPS: Total 6 units at 250 kW each

### Procurement Strategy
- Execute UPS contract with modular expansion options
- Lock pricing for future UPS modules
- Maintain spare parts compatibility across all phases
- Stock critical spares (UPS modules, battery strings)

---

## ELECTRICAL/MECHANICAL SEPARATION

### Equipment Yard Organization
- **Electrical Equipment:**
  - Outdoor containerized electrical enclosures (2-3 units)
  - Generator yard
- **Mechanical Equipment:**
  - Chiller yard (16 chillers in horizontal rows)
  - Pumping equipment
  - CDU access

**Layout:** Equipment yard organization and side placement TBD during detailed design

**Benefits:**
- Clear separation of electrical and mechanical equipment
- Outdoor enclosures eliminate indoor space requirements
- Shorter cable/pipe runs within each discipline
- Easier equipment expansion and replacement

---

## COST IMPACTS

| System                                                          | Cost Estimate                  |
| --------------------------------------------------------------- | ------------------------------ |
| Traditional N+1 UPS Phase 1 (8 modules @ 500 kW = 4 MW)         | $3.0-4.0M                      |
| Traditional N+1 UPS Phase 4 (32 modules total = 16 MW)          | +$9.0-12.0M (Phases 2-4)       |
| Traditional N+1 UPS Phase 5 (64 modules total = 32 MW)          | +$12.0-16.0M (Phase 5)         |
| **Total UPS (all phases)**                                      | **$24.0-32.0M**                |
| Generator systems Phase 1 (2× units @ 4.3 MW)                   | $2.4M                          |
| Generator systems Phase 4 (5× units total)                      | +$3.6M (Phases 2-4)            |
| Generator systems Phase 5 (10× units total)                     | +$6.0M (Phase 5)               |
| **Total Generators (all phases)**                               | **$12.0M**                     |
| IT Transformers Phase 1 (2× 5,000 kVA)                          | $0.4M                          |
| IT Transformers Phase 4 (5× total)                              | +$0.6M (Phases 2-4)            |
| IT Transformers Phase 5 (10× total)                             | +$1.0M (Phase 5)               |
| **Total IT Transformers (all phases)**                          | **$2.0M**                      |
| Outdoor electrical enclosures (2-3 containerized units)         | ~$1-2M {TBC}                   |
| Medium voltage distribution (switchgear, cabling)               | ~$2-3M                         |
| Low voltage distribution (switchboards, busway, RPPs)           | ~$4-6M                         |
| **Total Electrical (Phase 1)**                                  | ~$11-16M                       |
| **Total Electrical (Ultimate, Phases 1-5)**                     | ~$45-58M                       |

**BESS-as-UPS Avoided:**
- BESS-as-UPS Phase 1 would have been $29.7-31.2M (vs $4.5M traditional UPS Phase 1)
- But violates Tier III compliance (see [[Why BESS Should Not Be UPS]])
- Lender rejection risk or +100 bps financing penalty
- **Traditional UPS is only proven, bankable Tier III solution**

---

**Tags:** #saga-project #electrical #traditional-ups #tier3-compliance #generators #distribution #csi-division-26

**Related Documents:**
- [[_BOD - Exec Summary and TOC]] - Main title page
- [[Why BESS Should Not Be UPS]] - Technical analysis rejecting BESS-as-UPS
- [[Excess Solar Monetization Strategy]] - Economic BESS evaluation (rejected)
- [[12BOD - Process Equipment (CSI Divs 40-48)]] - Generator and solar details
- [[11BOD - Utilities DC Critical (CSI Div 33)]] - Utility interconnection
- [[Architectural Meeting Changes by CSI Division]] - October 2025 updates
