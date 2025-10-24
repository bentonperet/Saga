**Created:** 2025-10-23 10:40

# BASIS OF DESIGN - ELECTRICAL
## CSI Division 26
### Saga Energy – Pryor Data Center

**Parent Document:** [[_BOD - Exec Summary and TOC]]
**Related:** [[Why BESS Should Not Be UPS]] | [[Excess Solar Monetization Strategy]] | [[Architectural Meeting Changes by CSI Division]]

---

## OVERVIEW

Electrical systems provide Tier III-compliant N+1 redundant power distribution with dual power paths (A/B) supporting 12 MW initial IT load (20-24 MW ultimate). Traditional modular UPS architecture confirmed as only proven, bankable solution for project finance.

**Major Design Decision:** Traditional modular UPS provides concurrent maintainability required for Tier III compliance. BESS-as-UPS topology rejected due to non-maintainable single point of failure (see [[Why BESS Should Not Be UPS]]). Economic BESS separately evaluated and rejected due to deeply negative NPV (see [[Excess Solar Monetization Strategy]]).

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

## TRADITIONAL N+1 UPS ARCHITECTURE WITH DUAL POWER PATHS {TBC}

### System Configuration

**Dual-Path Modular UPS Topology (A-Side / B-Side)**
- **Configuration:** Dual independent UPS trains (A and B) feed separate power paths to IT equipment
- **Redundancy:** Each path N+1 (multiple UPS modules per side, any one can fail without impact)
- **Concurrent Maintainability:** Can take entire A-side offline for maintenance while B-side carries full load
- **Backup Duration:** 15 minutes at full load (bridges to generator startup)

**JIT Phased Deployment:**

| Phase | Facility Load | UPS Capacity Deployed | UPS CAPEX | Cumulative Cost |
|-------|---------------|----------------------|-----------|-----------------|
| **1** | 4.0-4.3MW | 6MW (N+1) | $4.5M | $4.5M |
| **2** | 8.0-8.5MW | Add 4MW modules | $3.0M | $7.5M |
| **3** | 12.0-12.8MW | Add 5MW modules | $3.8M | $11.3M |
| **4** | 16.0-17.0MW | Add 6MW modules | $4.5M | $15.8M |
| **5** | 27.0-28.4MW | Add 14MW modules | $10.5M | $26.3M |

**Phase 1 CAPEX Advantage (illustrative numbers):**
- Deploy only $4.5M Phase 1 vs $26.3M upfront
- Preserves $21.8M cash for improved IRR
- Matches capacity deployment with revenue generation

### UPS Technical Specifications

**Power Modules:**
- **Type:** Modular hot-swappable UPS modules (500kW or 1MW per module)
- **Topology:** Double-conversion online UPS (VFI per IEC 62040-3)
- **Efficiency:** 96-97% at full load, 98-99% in eco-mode
- **Input:** 480V, 3-phase
- **Output:** 480V, 3-phase for overhead busway distribution

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
- ✅ No single point of failure (loss of A or B does not impact IT)
- ✅ Concurrently maintainable (service either side without downtime)
- ✅ Proven topology (40+ years track record, thousands of deployments)
- ✅ Lender acceptance (no exotic risk premium, standard DC design)

---

## OUTDOOR CONTAINERIZED ELECTRICAL ENCLOSURES

### Configuration
- **Type:** Weather-rated containerized electrical enclosures
- **Quantity:** 2-3 outdoor enclosures (A-side, B-side, +1 optional)
- **Size:** ~12 ft × 55 ft per enclosure {TBC}
- **Location:** Outdoor equipment yard (side TBD)
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
- **IT Switchboards (SWBD):** 4× units, 4,000A, 480V, 65kA SCCR
  - One per transformer (feeds overhead busway to data hall)
- **Mechanical Switchboards (MECH SWBD):** 2× units, 1,600A, 480V, 35kA SCCR
  - Feeds chiller plant, pumps, DX units, support spaces

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
- Main switchgear → Generator paralleling switchgear (or BESS inverter switchgear)
- Generator/BESS switchgear → 4× IT transformers (3,000 kVA each)
- Generator/BESS switchgear → 2× Mechanical transformers (1,500 kVA each)

### Transformer Specifications
- **IT Transformers:** 4× 3,000 kVA, 13.8kV-480Y/277V, VPI dry-type, outdoor rated
- **Mechanical Transformers:** 2× 1,500 kVA, 13.8kV-480Y/277V, VPI dry-type, outdoor rated
- **Impedance:** 5.75% typical
- **Cooling:** Dry-type, forced air (fans for overload conditions)

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
- **Generators:** 5-6 total (fuel type TBD, N+1 configuration)
- **Transformers:** 4 IT transformers (2 per path, can lose one per side)
- **Switchboards:** 4 IT switchboards (2 per path, each side feeds A or B busway)

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

### Phase 1 (Build Day One)
- Substation transformer: 15-20 MVA (sized for ultimate capacity)
- 13.8kV switchgear: Sized for ultimate load
- UPS: Dual path frames installed with Phase 1 modules (6MW N+1 total)
- Generator yard: 2× generators (N+1 for Phase 1 load)
- Electrical enclosures: 2-3 outdoor containerized enclosures (houses Phase 1 UPS/battery capacity)

### Phase 2-5 (Triggered by IT Load Growth)
- Add UPS modules to existing frames (no new frames required)
- Add generators as load increases (Phases 2-5 per table in Generator Systems section)
- Add electrical enclosures if needed for expansion (modular approach)

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
| Traditional N+1 UPS with dual paths (Phase 1: 6MW N+1)          | $4.5M                          |
| Traditional N+1 UPS with dual paths (Phases 2-5, ultimate 28MW) | +$21.8M (phased over 4 phases) |
| **Total UPS (all phases)**                                      | **$26.3M**                     |
| Generator systems Phase 1 (2× units, N+1)                       | $2.4M                          |
| Generator systems ultimate (8× units total, phased)             | +$8.4M (Phases 2-5)            |
| **Total Generators (all phases)**                               | **$10.8M**                     |
| Outdoor electrical enclosures (2-3 containerized units)         | ~$1-2M {TBC}                   |
| Medium voltage distribution (transformers, switchgear)          | ~$3-5M                         |
| Low voltage distribution (switchboards, busway, RPPs)           | ~$4-6M                         |
| **Total Electrical (Phase 1)**                                  | ~$15-21M                       |
| **Total Electrical (Ultimate, Phases 1-5)**                     | ~$46-55M                       |

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
