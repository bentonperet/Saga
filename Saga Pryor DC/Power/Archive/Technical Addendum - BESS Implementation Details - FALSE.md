**Created:** 2025-10-21

# Technical Addendum: BESS Implementation Details
## Detailed Specifications, Standards, and Requirements
**Saga Energy Pryor Data Center - 10MW IT Load**

**Document Purpose:** Provide comprehensive technical specifications and implementation requirements for BESS-as-UPS architecture. This addendum supports [[BESS as UPS Replacement - FALSE]] with detailed engineering data.

**Tags:** #saga-project #bess #technical-specs #ieee-standards #nfpa-855 #commissioning #vendor-evaluation

**Document Status:** TECHNICAL REFERENCE
**Date:** 2025-10-21
**Prepared By:** Pachyderm Global / PGCIS
**Prepared For:** Saga Energy Engineering Team

**Related Documents:**
- [[BESS as UPS Replacement - FALSE]] - Executive summary and decision framework
- [[Part 1 - Solar-First Startup Strategy - BAD]] - System architecture and phasing
- [[Part 2 - Strategic DC Sizing Analysis - ARCHIVE]] - Financial analysis

---

## CHANGELOG V5.0 (2025-10-21)

**Major Updates:**
- ✅ Recalculated for **10MW IT load** (vs. 7.4MW in previous versions)
- ✅ Updated BESS sizing: **15-18 MWh** (vs. 12-15 MWh)
- ✅ Updated solar sizing: **16MW** (vs. 12MW)
- ✅ Revised phasing: **3MW IT load blocks** (3.3MW → 6.6MW → 10MW)
- ✅ Updated facility load: **13.5-14.2MW** (PUE 1.35-1.42)
- ✅ Revised backup duration: **1.0-1.3 hours** (still 5× better than UPS)

---

## 1. BESS TECHNICAL SPECIFICATIONS

### 1.1 System Overview

**Solar-Excess-Capture Sizing Philosophy:**
- BESS sized for solar excess capture (15-18 MWh), NOT backup duration
- 16MW solar - 13MW daytime load = 3MW peak excess × 4-5 hours = 12-15 MWh/day
- Right-sized BESS provides 1.0-1.3 hours backup at 13.5-14MW load (5× better than traditional UPS)
- **Inverters scale with occupancy, batteries remain constant**

**Phased Deployment Configuration (3MW IT Blocks):**

| Specification | Phase 0 (3.3MW IT) | Phase 1 (6.6MW IT) | Phase 2 (10MW IT) | Rationale |
|--------------|---------|---------|---------|-----------|
| **IT Load** | 3.3MW | 6.6MW | 10MW | 3MW incremental blocks |
| **Facility Load** | 4.5MW | 9MW | 13.5MW | PUE 1.35 average |
| **Power Rating** | **8MW AC** | **12MW AC** | **16MW AC** | Scales with occupancy |
| **Configuration** | 2×4MW inverters | 3×4MW inverters | 4×4MW inverters | N+1 redundancy at all phases |
| **Available Capacity (N+1)** | 4MW | 8MW | 12MW | Lose 1 inverter, still serve load |
| **Energy Capacity** | **15-18 MWh** | **15-18 MWh** | **15-18 MWh** | **Constant - sized for solar, NOT load** ✅ |
| **Battery Containers** | 4 containers | 4 containers | 4 containers | ~4.5 MWh per container |
| **Backup Duration** | 3.5 hrs @ 4.5 MW | 1.8 hrs @ 9 MW | 1.2 hrs @ 13.5 MW | Solar-sized BESS provides adequate backup |

**Key Insight:** Traditional approach sizes BESS for backup duration (56 MWh @ $28M for 10MW IT). Correct approach sizes BESS for solar excess capture (16 MWh @ $8M), which naturally provides adequate backup.

### 1.2 Inverter Specifications

**Power Conversion System (PCS) Requirements:**
- **Type:** Grid-forming (NOT grid-following) - **CRITICAL**
- **Rating:** 4 MW continuous @ 0.8 power factor per inverter
- **Voltage:** Output 480V AC, 3-phase (matches critical bus)
- **Frequency:** 60 Hz ±0.1 Hz regulation
- **Efficiency:** ≥96% at rated load, ≥95% at 50% load
- **Response Time:** <50ms to grid disturbances (ITIC compliant)
- **THD (Total Harmonic Distortion):** <5% (IEEE 519 compliant)
- **Power Factor:** 0.95-1.0 leading/lagging (active/reactive control)
- **Black-Start:** Yes (can restart without utility grid)
- **Islanding:** Seamless (<50ms detection and transition)
- **Resynchronization:** <1 second after grid returns
- **Overload Capability:** 110% for 10 minutes, 150% for 1 minute

**Vendor Examples:**
- Tesla Megapack: 3.9 MW inverter (grid-forming capable)
- Fluence Gridstack Pro: 4.0 MW inverter (grid-forming capable)
- Wärtsilä GridSolv Quantum: 4.0 MW inverter (modular, grid-forming)

### 1.3 Battery Specifications

**Chemistry:** LFP (Lithium Iron Phosphate)
- Safer than NMC (Nickel Manganese Cobalt)
- Longer cycle life: 6,000 cycles @ 80% DoD
- Better thermal stability (lower thermal runaway risk)
- Lower energy density (acceptable for stationary applications)

**Performance:**
- **Energy Capacity:** 15-18 MWh total (all phases)
- **Usable Capacity:** 85% DoD (depth of discharge)
- **Roundtrip Efficiency:** ≥95% (AC-AC), ≥98% (DC-DC)
- **Cycle Life:** 6,000 cycles @ 80% DoD = 20-24 year lifespan
- **Degradation:** <2% per year (first 10 years)
- **Capacity Retention:** ≥80% after 6,000 cycles (warranty requirement)
- **Temperature Range:** Operating: -20°C to +50°C; Optimal: +15°C to +35°C
- **Self-Discharge:** <3% per month

**Thermal Management:**
- **Type:** Active liquid cooling (required for Oklahoma climate)
- **Cooling Capacity:** Sized for 100°F ambient + solar radiation
- **Heat Rejection:** ~200-300 kW per container (during charge/discharge)
- **Coolant:** Propylene glycol/water mix (non-toxic, freeze-protected)
- **Redundancy:** N+1 cooling pumps and heat exchangers

### 1.4 Enclosure & Physical Specifications

**Container Configuration:**
- **Type:** ISO 20-foot shipping containers (weatherproof, modular)
- **Quantity:** 4 containers total (deployed in Phase 0)
- **Capacity:** ~4.5 MWh per container (16.5 MWh midpoint ÷ 4 = 4.125 MWh each)
- **Dimensions:** 20' L × 8' W × 9.5' H per container
- **Weight:** ~35-45 tons per container (loaded)
- **Footprint:** 4 containers + 4 inverters = ~2,500 SF total
- **Separation:** 10-15 feet between containers (NFPA 855 requirement)

**Environmental Protection:**
- **IP Rating:** IP54 minimum (dust + water splash protection)
- **Corrosion:** Marine-grade coatings (Oklahoma humidity)
- **Wind Loading:** 250 mph (tornado-rated per FEMA 361 / ICC 500)
- **Seismic:** Zone 2 (Oklahoma seismic requirements)
- **Impact Resistance:** Missile impact testing (15 lb 2×4 @ 100 mph)

---

## 2. POWER QUALITY STANDARDS & COMPLIANCE

### 2.1 IEEE Standards

**IEEE 2030.7 - Microgrid Controller Standard:**
- Real-time power balancing (solar + BESS + generators = load)
- Seamless mode transitions (grid-connected ↔ islanded ↔ generator-supported)
- State management (BESS SOC optimization, thermal limits, cycle life)
- Generator dispatch (auto-start on low SOC, load sharing)
- Power quality monitoring (voltage/frequency/harmonic tracking)
- **Implementation Cost:** $500-800k for control algorithms

**IEEE 2030.8 - Microgrid Testing Procedures:**
- Factory Acceptance Test (FAT) protocols
- Site Acceptance Test (SAT) protocols
- Integrated systems testing (all operating modes)
- Performance verification
- **Implementation Cost:** $250-350k for FAT/SAT execution

**IEEE 1547 - Interconnection Standard:**
- Voltage regulation: ±5% (456-504V for 480V nominal)
- Frequency regulation: 59.3-60.5 Hz (normal), 57.0-61.8 Hz (abnormal)
- Islanding detection: <2 seconds (IEEE 1547.1)
- Resynchronization: Voltage ±3%, frequency ±0.3 Hz, phase angle ±20°
- **Compliance:** Required for utility interconnection approval

**IEEE 519 - Harmonic Limits:**
- Total Harmonic Distortion (THD): <5% voltage, <15% current
- Individual harmonics: <3% for any single harmonic
- Measurement: At point of common coupling (PCC)
- **Compliance:** Required for power quality certification

### 2.2 ANSI Standards

**ANSI C84.1 - Voltage Ratings:**
- Range A (preferred): 480V ±5% = 456-504V
- Range B (acceptable): 480V ±10% = 432-528V
- BESS must maintain Range A during all operating modes
- **Compliance:** Industry standard for electrical equipment

### 2.3 ITIC Curve Compliance

**IT Equipment Tolerance (ITIC Curve):**
- Voltage tolerance: 480V ±10% indefinite, ±20% for <0.5 seconds
- Frequency tolerance: 60 Hz ±5% indefinite
- **BESS Response Requirement:** Return to normal within 50ms
- **Testing:** Verified during SAT with load bank simulation

---

## 3. SAFETY STANDARDS & CERTIFICATIONS

### 3.1 NFPA 855 - Fire Protection for Stationary Energy Storage Systems

**Fire Suppression Requirements:**

**Automatic Systems:**
- **Type:** Clean agent (FM-200, Novec 1230) OR aerosol (Stat-X)
- **Activation:** Dual-sensor (smoke + heat) with cross-zone verification
- **Coverage:** 100% of battery container interior volume
- **Discharge Time:** <10 seconds from detection to full discharge
- **Redundancy:** Independent suppression per container (no single failure)
- **Manual Override:** Emergency suppression activation outside containers
- **Cost:** $150-200k per container × 12 containers = **$1.8-2.4M**

**Gas Detection:**
- **Gases Monitored:** H₂ (hydrogen), CO (carbon monoxide), CO₂ (carbon dioxide)
- **Sensor Locations:** Multiple per container (top, middle, bottom)
- **Alarm Thresholds:** H₂ >1,000 ppm, CO >50 ppm, CO₂ >5,000 ppm
- **Response:** Ventilation activation + alarm + suppression prep
- **Cost:** $75-150k total system

**Explosion Protection:**
- **Venting:** Pressure relief vents (prevent container rupture)
- **Design Pressure:** Withstand 2-3 psi overpressure before venting
- **Vent Location:** Directed away from buildings and equipment
- **Deflagration Venting:** Sized per NFPA 68 calculations
- **Cost:** $100-200k (venting + pressure relief systems)

**Thermal Management:**
- **HVAC:** Dedicated active cooling (liquid + air circulation)
- **Capacity:** Remove 200-300 kW heat per container
- **Redundancy:** N+1 cooling loops (can lose one, maintain operation)
- **Temperature Monitoring:** Continuous cell-level temperature sensors
- **Cost:** $225-350k (active cooling systems)

**Fire Barriers & Setbacks:**
- **Separation Distance:** 10-15 feet between containers (NFPA 855 Table 4.5.2.2)
- **Separation from Buildings:** 50-100 feet OR 4-hour fire-rated barrier
- **Barrier Construction:** Concrete block or fire-rated panels
- **Cost:** $250-600k (barriers + site layout)

**Total NFPA 855 Compliance Cost:**
- Phase 0 (4 containers): **$1.8-2.0M**
- Phase 1: **$0** (no additional batteries)
- Phase 2: **$0** (no additional batteries)
- **Total (4 containers): $1.8-2.0M**

### 3.2 UL 9540 - Energy Storage System Safety

**Product Safety Certification:**
- Third-party testing lab (UL, Intertek, CSA)
- Complete system testing (batteries + inverters + enclosure)
- Nameplate listing on all major components
- **Requirement:** Insurance and AHJ (Authority Having Jurisdiction) approval
- **Cost:** Included in vendor equipment pricing

### 3.3 UL 9540A - Thermal Runaway Propagation Testing

**Fire Testing Protocol:**
- Heat one battery cell to thermal runaway
- Measure propagation to adjacent cells, modules, containers
- Document time to propagation and temperatures
- **Pass Criteria:** No propagation beyond single module OR >30 min to propagation
- **Requirement:** Insurance underwriters demand this data
- **Cost:** $50-100k per battery model (vendor typically provides)

### 3.4 Oklahoma Tornado Hardening

**Wind Rating:**
- Design Wind Speed: 250 mph (FEMA 361 / ICC 500 tornado shelter standard)
- Continuous Wind: 180 mph (Oklahoma design wind per ASCE 7)
- **Container Anchoring:** Embedded foundations, resist 250 mph uplift
- **Electrical Gear:** Seismic Zone 2 mounting (Oklahoma seismic hazard)
- **Cost:** $300-500k (reinforced foundations + anchoring)

---

## 4. LOAD CALCULATIONS & PUE ANALYSIS

### 4.1 IT Load Profile

**Base IT Load (Updated for 10MW Data Center):**
- **Total IT Load: 10,000 kW = 10 MW**
- Rack Mix (assumption):
  - AI/HPC Racks: 60 racks × 130 kW = 7,800 kW
  - Enterprise Racks: 100 racks × 22 kW = 2,200 kW
  - Total: 10,000 kW

**Load Diversity:**
- Not all racks draw peak power simultaneously
- Diversity factor: 0.7-0.85 for average load
- Peak diversity factor: 0.9-0.95 for design load
- **This analysis assumes: NO diversity credit** (conservative, 100% peak + 5% margin)

### 4.2 Facility Load by PUE

**PUE (Power Usage Effectiveness) Variation:**

| Scenario | IT Load | PUE | Facility Load | Conditions |
|----------|---------|-----|---------------|------------|
| **Winter Base** | 10 MW | 1.20 | 12.0 MW | Mild cooling, optimal conditions |
| **Annual Average** | 10 MW | 1.30 | 13.0 MW | Design target |
| **Daytime (Solar Offset)** | 10 MW | 1.30 | 13.0 MW | Solar reduces cooling load |
| **Summer Peak** | 10 MW | 1.40 | 14.0 MW | July/August, full cooling |
| **Design Basis** | 10 MW | 1.42 | 14.2 MW | Peak + 5% margin |

**Key Finding:** Facility load varies by **2.2 MW (18%)** between winter and summer. **BESS is sized for solar excess capture (15-18 MWh), which provides adequate backup for all seasons.**

### 4.3 Cooling Load Breakdown

**Cooling Components (Summer Peak, PUE 1.42):**
- IT Load: 10.0 MW
- Cooling (CRAC/CRAH): 2.5 MW (25% of IT load)
- Fans & Air Handling: 1.0 MW (10% of IT load)
- Pumps & Chillers: 0.5 MW (5% of IT load)
- Lighting & Misc: 0.2 MW (2% of IT load)
- **Total Facility Load: 14.2 MW**

**PUE Calculation:**
```
PUE = Facility Load / IT Load
PUE = 14.2 MW / 10.0 MW = 1.42
```

### 4.4 Load Profile by Phase (3MW IT Blocks)

**Phase 0 (3.3MW IT):**
- IT Load: 3.3 MW
- PUE: 1.35 (average, low occupancy overhead offset by better cooling efficiency)
- Facility Load: 4.5 MW
- **BESS Backup Duration: 16 MWh ÷ 4.5 MW = 3.5 hours**

**Phase 1 (6.6MW IT):**
- IT Load: 6.6 MW
- PUE: 1.35
- Facility Load: 9.0 MW
- **BESS Backup Duration: 16 MWh ÷ 9.0 MW = 1.8 hours**

**Phase 2 (10MW IT):**
- IT Load: 10.0 MW
- PUE: 1.35 (average) to 1.42 (summer peak)
- Facility Load: 13.5-14.2 MW
- **BESS Backup Duration: 16 MWh ÷ 13.5 MW = 1.2 hours**

**Solar Excess by Phase:**
- **All Phases:** 16MW solar deployed in Phase 0
- **Phase 0:** 16MW - 4.5MW = 11.5MW excess (high)
- **Phase 1:** 16MW - 9MW = 7MW excess (medium)
- **Phase 2:** 16MW - 13MW = 3MW excess (optimal for BESS charging)

---

## 5. SCHNEIDER RD109 INTEGRATION

### 5.1 RD109 Baseline Architecture

**Schneider Reference Design 109 (RD109):**
- Proven Tier III data center electrical architecture
- UPS-based power conditioning
- N+1 redundancy at all levels
- Scalable to 10-15 MW IT capacity range

**Baseline Components (Traditional - 10MW IT):**
- UPS: 10×1500 kW + 2×200 kW = 15.4 MW capacity (N+1)
- UPS Batteries: Li-ion, 5-15 minute backup
- Generators: 5×4000 kW = 20 MW total (N+1 for 14.2MW facility load)
- Utility Service: 138 kV → 13.8 kV → 480V critical bus

### 5.2 Modifications for BESS-as-UPS

**Electrical System Changes:**

| RD109 Baseline | BESS-as-UPS Modification | Justification |
|----------------|--------------------------|---------------|
| **UPS Layer (480V)** | **ELIMINATED** | BESS inverters provide power conditioning |
| **UPS Batteries** | **ELIMINATED** | BESS provides backup (1.5 hrs vs. 15 min) |
| **BESS Tie-In** | **ADDED at 480V** | BESS inverters output directly to critical bus |
| **Step-Down Transformers** | **MODIFIED** | Sized for BESS inverter output (4×3.5 MVA) |
| **BESS Switchgear** | **ADDED** | 4 breaker positions for inverters + isolation |
| **Microgrid Controller** | **UPGRADED** | IEEE 2030.7/8 compliance (+$1.05M vs. baseline) |
| **Generators** | **UNCHANGED** | Same 4×4MW configuration |

**Single-Line Diagram Modifications:**
1. **Remove:** Traditional UPS modules and battery cabinets from 480V critical bus
2. **Add:** BESS inverter tie-in at 480V bus (4 connection points)
3. **Add:** Isolation breakers for each BESS inverter (manual + automatic trip)
4. **Add:** Step-down transformers if BESS output voltage ≠ 480V (vendor-dependent)
5. **Modify:** Critical bus fed from BESS inverters (instead of UPS output)
6. **Maintain:** Generator tie-in at 13.8 kV level (no change from baseline)
7. **Maintain:** N+1 distribution topology at 480V level (no change)

### 5.3 Controls Integration

**RD109 Baseline Controls:**
- Schneider EcoStruxure SCADA for UPS + generator monitoring
- Cost: $0.8M

**BESS-as-UPS Controls Upgrade:**
- **Microgrid Controller:** Schneider EcoStruxure Microgrid Advisor (IEEE 2030.7/8 compliant)
- **Integration:** Coordinates BESS, solar, generators, utility grid
- **Functions:**
  - Real-time power balancing (solar + BESS + grid + generators = load)
  - Mode transitions (grid-connected ↔ islanded ↔ generator-supported)
  - BESS state management (SOC, thermal, cycle life optimization)
  - Generator dispatch logic (auto-start on low SOC, load sharing)
  - Power quality monitoring (voltage, frequency, harmonics with fault detection)
  - Predictive analytics (solar forecasting, load prediction)
  - SCADA integration (24/7 monitoring, alarms, remote control)
- **Cost:** $1.85M (vs. $0.8M baseline = **+$1.05M**)

**Vendor Coordination:**
- Schneider Electric: Provide RD109 baseline + microgrid controls upgrade
- BESS Vendor: Provide BESS-specific control interface (Modbus, DNP3, or proprietary)
- EPC Contractor: System integration and commissioning

### 5.4 Physical Layout Changes

**Space Requirements:**

| System | RD109 Baseline (10MW IT) | BESS-as-UPS | Delta |
|--------|---------------|-------------|-------|
| **UPS Room (Indoor)** | 2,500 SF | 0 SF | **-2,500 SF** ✅ |
| **Battery Room (Indoor)** | 2,000 SF | 0 SF | **-2,000 SF** ✅ |
| **BESS Enclosure (Outdoor)** | 0 SF | 2,500 SF | **+2,500 SF** ⚠️ |
| **Transformer Pad (Outdoor)** | 0 SF | 600 SF | **+600 SF** ⚠️ |
| **Fire Suppression** | Included in UPS/battery rooms | Separate NFPA 855 system | **+$1.8-2.0M** ⚠️ |

**Net Space Impact:**
- **Indoor space savings:** -4,500 SF (UPS + batteries eliminated)
- **Outdoor space required:** +3,100 SF (BESS enclosure + transformer pad)
- **Benefit:** Repurpose 4,500 SF climate-controlled indoor space for IT racks or offices

**Site Plan Considerations:**
- BESS enclosure located adjacent to solar field (minimize cable runs to solar inverters)
- Separation distance from data center: 50-100 feet (NFPA 855 requirement OR fire barriers)
- Access for maintenance: 25-foot clearance on 2 sides for container removal
- Tornado-rated foundations embedded 6-8 feet deep

---

## 6. DETAILED RISK ASSESSMENT & SUCCESS CRITERIA

### 6.1 Comprehensive Risk Analysis (Top 5 Risks)

**Risk 1: BESS Costs Higher Than Estimated (55% Confidence)**

| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|------------|
| BESS pricing exceeds $13M for 15-18 MWh | Savings reduced but still significant | Medium | **Issue RFI this week** to Tesla, Fluence, Wärtsilä; lock pricing early; 2024-2025 market trend is -30% (favorable); build 15% contingency |

**Detailed Analysis:**
- Current estimate: $7-10M based on $450-550/kWh LFP pricing
- Market conditions: LFP prices dropped 40% in 2024, continued decline expected
- Risk trigger: If quotes exceed $13M ($720/kWh), financial case weakens significantly
- Response: If >$13M, evaluate hybrid approach (smaller BESS + minimal UPS)

**Risk 2: Lender/Insurance Skepticism on Non-Traditional Architecture**

| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|------------|
| Lenders reject BESS-only design | Project financing delayed 3-6 months | Medium | Independent engineering review (Schneider, Black & Veatch); reference projects (Microsoft Azure, Switch); emphasize RD109 foundation compliance; add small UPS if needed ($0.2M fallback) |

**Detailed Analysis:**
- Traditional lenders prefer proven UPS architectures
- Insurance underwriters may require higher premiums for novel designs
- Mitigation: Third-party engineering validation report ($50-100k)
- Fallback: Add 400kW UPS ($0.2M) as "safety net" for comfort
- Industry precedent: Microsoft, Switch, Quantum Loophole approved by major lenders

**Risk 3: BESS Lead Time Exceeds 12 Months**

| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|------------|
| BESS delivery delayed by 6+ months | Revenue delayed, financing costs increase by $500k-1M | Medium | **Order BESS by Q1 2026** (critical path); Tesla backlog 15-18 months, Fluence/Wärtsilä 10-12 months faster; include liquidated damages in contract ($50k/month); consider dual-source strategy |

**Detailed Analysis:**
- Tesla Megapack: Currently 15-18 month lead time (high demand)
- Fluence Gridstack: 10-12 months (more availability)
- Wärtsilä GridSolv: 10-14 months (modular, faster)
- Critical path: BESS drives overall project timeline
- Mitigation: Early PO (Q1 2026), liquidated damages clause, backup vendor identified

**Risk 4: Power Quality Issues During Islanding**

| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|------------|
| BESS fails to maintain voltage/frequency during grid outage | Load interruption, customer SLA violation, revenue loss | Low | IEEE 2030.7 compliant controls ($1.5M); FAT/SAT testing (100% validation before go-live); continuous monitoring; proven technology (Microsoft, Switch validate); black-start testing during commissioning |

**Detailed Analysis:**
- Grid-forming inverters proven in data center applications
- IEEE 2030.8 testing protocols ensure ITIC compliance
- Factory Acceptance Test validates performance before shipment
- Site Acceptance Test with full load simulation required
- Continuous monitoring detects anomalies before failures
- Probability: Low (technology proven, but new to this project)

**Risk 5: Battery Degradation Faster Than Expected**

| Risk | Impact | Probability | Mitigation |
|------|--------|-------------|------------|
| Batteries degrade >2%/year, replacement needed before Year 15 | Unplanned CAPEX $5-8M (full replacement) | Low-Medium | LFP chemistry (longer life than NMC); conservative cycling (20-30 cycles/yr vs. 250 for grid apps); warranty with capacity guarantees (80% @ 6,000 cycles); budget Year 15 replacement in pro forma; thermal management critical (Oklahoma heat) |

**Detailed Analysis:**
- LFP chemistry: 6,000 cycles @ 80% DoD (vs. 3,000 for NMC)
- Data center duty cycle: 20-30 full cycles/year (low stress)
- Expected lifespan: 20-24 years (6,000 cycles ÷ 25 cycles/yr)
- Degradation: <2%/year for first 10 years, accelerates after
- Warranty: Demand 80% capacity retention at 6,000 cycles or 15 years
- Thermal stress: Oklahoma summers (100°F) require robust cooling

### 6.2 Risk Mitigation Summary

**Overall Risk Profile: MODERATE-LOW**

**High-Confidence Areas (85%+):**
- ✅ Technical feasibility (grid-forming inverters proven in data centers)
- ✅ Power quality performance (IEEE standards well-established)
- ✅ Industry validation (Microsoft, Switch, Quantum Loophole)
- ✅ Solar-excess-capture sizing logic (validated by multiple analyses)

**Medium-Confidence Areas (55-75%):**
- ⚠️ BESS pricing (need vendor RFI validation by Nov 1)
- ⚠️ Generator pricing (need vendor RFI validation by Nov 1)
- ⚠️ Fire safety costs (NFPA 855 validation needed)
- ⚠️ Lender acceptance (independent engineering review recommended)

**Mitigation Strategy:**
- Issue RFIs by Oct 25 to increase confidence to 80%+ by Nov 1
- Independent engineering review for lender comfort ($50-100k)
- Reference project site visits for insurance validation
- Early PO (Q1 2026) to secure lead time

**Showstoppers (Revert to Traditional if Triggered):**
- ❌ BESS vendor cannot confirm grid-forming capability for data center application
- ❌ Lenders reject design even with independent engineering review
- ❌ BESS costs exceed $13M for 15-18 MWh (destroys financial case)
- ❌ Insurance premium >$150k/year vs. traditional (risk not acceptable)
- ❌ No local BESS service network within 4 hours of Pryor, OK

### 6.3 Detailed Success Criteria

**Technical Success (6-12 Months Post-Commissioning):**
- ✅ BESS provides seamless power transitions (<50ms validated via continuous monitoring)
- ✅ No unplanned outages due to BESS or microgrid control failures (99.99% availability target)
- ✅ Grid-forming inverters maintain power quality within ITIC curve (voltage ±10%, frequency ±0.3 Hz)
- ✅ N+1 redundancy tested and operational (can lose 1 inverter, backup maintained for 1.2 hours)
- ✅ NFPA 855 fire systems tested and certified (annual re-certification)
- ✅ Solar excess capture: 12-15 MWh/day average (validates sizing)

**Financial Success (12-24 Months):**
- ✅ Phase 0 CAPEX ≤$35M (target: $29-35M)
- ✅ Phase 2 total CAPEX ≤$44M (target: $36-44M)
- ✅ Achieved $30-35M savings vs. traditional UPS + oversized BESS
- ✅ O&M costs tracking at <$675k/year (vs. $760-970k traditional)
- ✅ Energy efficiency improvements measurable (PUE <1.35 annual average)
- ✅ No cost overruns >15% of budget

**Operational Success (12-24 Months):**
- ✅ Staff trained and comfortable operating BESS-as-UPS (no external support needed for routine ops)
- ✅ 24/7 remote monitoring operational with <4-hour vendor response (tested quarterly)
- ✅ Customers accept architecture (no lease cancellations due to power concerns)
- ✅ Insurance premiums within $100k/year of traditional (<$200k/year total)
- ✅ Lenders satisfied with performance (no covenant issues, refinancing options available)
- ✅ Generator runtime <500 hours/year (validates solar + BESS effectiveness)

**Strategic Success (24+ Months):**
- ✅ Model replicable for future Saga Energy projects (standardized design)
- ✅ BESS participates in SPP markets during grid-connected phases (incremental revenue)
- ✅ Enhanced company reputation as sustainability leader (carbon-free operations marketed)
- ✅ Competitive advantage in tenant acquisition (lower PUE, greener power)

---

## 7. COMMISSIONING TIMELINE

### 7.1 Critical Path Overview

**Total Duration: 18-24 months**
- Procurement: 12 months (BESS lead time drives)
- Construction: 8 months (site prep + installation)
- Commissioning: 3-4 months (FAT/SAT/integrated testing)

### 7.2 Phased Timeline

**Month 1-2: RFI & Vendor Selection**
- Issue RFI to 3 BESS vendors (Tesla, Fluence, Wärtsilä) ✅ **Oct 20-25**
- Receive and analyze responses (2-3 weeks)
- Vendor down-select and negotiations (2 weeks)
- **Milestone:** Vendor selected by Nov 15, 2025

**Month 3-4: Contract Execution**
- Purchase order execution (legal review, terms negotiation)
- 10% deposit payment
- Engineering kickoff (vendor + Schneider + EPC)
- Electrical single-line finalization (BESS integration with RD109)
- **Milestone:** PO executed by Jan 1, 2026

**Month 5-12: Equipment Manufacturing**
- BESS manufacturing (inverters + battery containers)
- Factory testing and QC at vendor facility
- Long-lead electrical gear (transformers, switchgear)
- Utility interconnection application (if not already submitted)
- NFPA 855 permitting (Oklahoma AHJ coordination)
- **Milestone:** Equipment ships by Aug 1, 2026

**Month 13-14: Site Preparation**
- BESS foundation (2,000 SF reinforced concrete pad, tornado-rated)
- Transformer pad (500 SF)
- Conduit and cable tray rough-in (480V AC + DC buswork)
- Fire barrier installation (NFPA 855 separation requirements)
- **Milestone:** Site ready for delivery by Sept 1, 2026

**Month 15-17: BESS Installation**
- BESS delivery to site (3-4 battery containers + 3 inverters)
- Crane operations (container placement, ~30-40 tons each)
- Electrical terminations (DC battery connections + AC inverter outputs)
- Transformer installation (if needed for voltage matching)
- Switchgear installation (3 breaker positions for inverters)
- **Milestone:** BESS mechanically complete by Nov 1, 2026

**Month 18-19: Fire Suppression & Controls**
- NFPA 855 fire suppression system installation
- Gas detection sensors (H₂, CO, CO₂)
- HVAC and thermal management systems
- Microgrid controller installation (Schneider EcoStruxure)
- SCADA integration (with RD109 baseline systems)
- **Milestone:** All systems installed by Jan 1, 2027

**Month 20: Generator Integration**
- Generator installation (2×4MW Phase 0, scales to 4×4MW in later phases)
- Generator tie-in to 480V bus (via step-down from 13.8 kV)
- Fuel storage system (24hr or 72hr natural gas capacity)
- Automatic start logic integration with microgrid controller
- **Milestone:** Generators operational by Feb 1, 2027

**Month 21: Factory Acceptance Test (FAT)**
- Travel to vendor facility (if FAT not done during manufacturing)
- Test protocols: Inverter response, black-start, islanding, power quality
- Documentation review: O&M manuals, training materials, warranties
- **Milestone:** FAT complete by Mar 1, 2027

**Month 22: Site Acceptance Test (SAT)**
- Onsite testing with vendor support (2-4 weeks)
- Individual subsystem testing (BESS, generators, controls)
- Grid-forming mode validation (voltage/frequency regulation)
- N+1 redundancy testing (simulate inverter failure)
- NFPA 855 fire suppression test (alarm verification, not full discharge)
- **Milestone:** SAT complete by Apr 1, 2027

**Month 23: Integrated Systems Test**
- Full microgrid testing (all operating modes):
  - Mode 1: Grid + solar + BESS normal operation
  - Mode 2: Grid outage, solar available (islanding test)
  - Mode 3: Grid outage, nighttime (BESS discharge + generator start)
  - Mode 4: Extended outage (generators run, BESS recharge)
- Power quality measurements (voltage, frequency, harmonics at critical bus)
- Backup duration validation (full discharge test)
- **Milestone:** Integrated test complete by May 1, 2027

**Month 24: Staff Training & Handover**
- Operations staff training (3-5 days onsite with vendor)
- Emergency procedure drills (grid outage, fire alarm, BESS failure scenarios)
- Maintenance training (routine inspections, troubleshooting, battery replacement)
- Final documentation handover (as-builts, O&M manuals, warranties, test reports)
- 24/7 remote monitoring activation (vendor NOC connection)
- **Milestone:** Commercial Operation Date (COD) - **June 1, 2027**

---

## 7. VENDOR EVALUATION CRITERIA

### 7.1 Technical Requirements Scorecard

**Must-Have (Go/No-Go):**

| Requirement | Weight | Evaluation Method |
|-------------|--------|-------------------|
| Grid-forming inverter capability | 20% | Vendor confirmation + spec sheet review |
| Data center reference projects (3+) | 15% | Reference calls + site visits |
| LFP chemistry | 10% | Spec sheet + UL 9540 cert review |
| N+1 configuration support | 10% | Engineering drawings review |
| UL 9540/9540A certification | 10% | Certificate verification |
| 6,000 cycle warranty @ 80% DoD | 10% | Warranty terms review |

**Nice-to-Have (Scoring Factors):**

| Criterion | Weight | Scoring Method |
|-----------|--------|----------------|
| Pricing (target: $6-7.5M total) | 15% | 5 = <$6M, 3 = $6-7.5M, 1 = >$7.5M |
| Lead time (target: ≤12 months) | 5% | 5 = <10 mo, 3 = 10-12 mo, 1 = >12 mo |
| Service network (<4 hrs from Pryor, OK) | 5% | 5 = Oklahoma City, 3 = Tulsa, 1 = >4 hrs |

**Minimum Passing Score: 70/100**

### 7.2 Vendor Comparison Matrix

| Criteria | Weight | Tesla Megapack | Fluence Gridstack Pro | Wärtsilä GridSolv Quantum |
|----------|--------|----------------|----------------------|---------------------------|
| **Grid-Forming** | 20% | TBD (RFI) | TBD (RFI) | TBD (RFI) |
| **DC Experience** | 15% | TBD (RFI) | TBD (RFI) | TBD (RFI) |
| **Pricing** | 15% | TBD (RFI) | TBD (RFI) | TBD (RFI) |
| **Lead Time** | 15% | TBD (RFI) | TBD (RFI) | TBD (RFI) |
| **Service Network** | 10% | TBD (RFI) | TBD (RFI) | TBD (RFI) |
| **Warranty** | 10% | TBD (RFI) | TBD (RFI) | TBD (RFI) |
| **Phasing Support** | 10% | TBD (RFI) | TBD (RFI) | TBD (RFI) |
| **RD109 Integration** | 5% | TBD (RFI) | TBD (RFI) | TBD (RFI) |
| **TOTAL** | **100%** | **TBD** | **TBD** | **TBD** |

**Update after RFI responses (target: Nov 1, 2025)**

---

## 8. O&M COST BREAKDOWN

### 8.1 Annual O&M Costs (BESS-as-UPS)

**BESS Maintenance:**
- Annual inspections: $50k (vendor contract, 2×/year)
- Software updates: $30k/year (included in remote monitoring)
- Battery monitoring: $50k/year (continuous cell-level monitoring)
- Inverter preventive maintenance: $75k/year (quarterly inspections)
- Thermal system maintenance: $45k/year (cooling pumps, heat exchangers)
- **Subtotal: $250-350k/year**

**Generator Maintenance:**
- Monthly inspections: $40k/year (4 units × $10k each)
- Quarterly load testing: $20k/year (fuel + labor)
- Annual overhauls: $20k/year (amortized over 5-year cycle)
- **Subtotal: $80-120k/year**

**Fire Suppression Maintenance:**
- System inspections: $30k/year (NFPA 855 compliance)
- Gas sensor calibration: $15k/year
- Suppression agent refill: $5k/year (minor leaks)
- **Subtotal: $50k/year**

**Microgrid Controls:**
- Software licenses: $30k/year (Schneider EcoStruxure)
- Cybersecurity updates: $25k/year
- Remote monitoring service: $50-100k/year (vendor NOC 24/7)
- **Subtotal: $105-155k/year**

**Fuel Management:**
- Fuel testing: $10k/year
- Pipeline capacity fee: $30k/year (firm capacity agreement)
- Generator fuel (testing only): $10k/year (100 hrs/year @ $3/MCF)
- **Subtotal: $50k/year**

**Insurance & Misc:**
- BESS property insurance: $75k/year
- Liability insurance: $25k/year
- Spare parts inventory: $20k/year (critical components on-site)
- Training refreshers: $15k/year (annual 1-day sessions)
- **Subtotal: $135k/year**

**TOTAL ANNUAL O&M (BESS-as-UPS): $555-675k/year**

### 8.2 Annual O&M Costs (Traditional UPS + BESS)

**UPS Maintenance:**
- Quarterly inspections: $100k/year (UPS vendor contract)
- UPS battery replacement: $40-80k/year (amortized, Li-ion 10-12 year life)
- **Subtotal: $140-180k/year**

**BESS Maintenance (Solar Only):**
- Same as BESS-as-UPS: $250-350k/year
- (BESS still needed for solar storage in traditional architecture)

**Generators, Fire, Controls, Fuel, Insurance:**
- Same as BESS-as-UPS: $370-440k/year

**TOTAL ANNUAL O&M (Traditional): $760-970k/year**

### 8.3 O&M Savings Summary

**Annual Savings (BESS-as-UPS vs. Traditional):**
- UPS maintenance eliminated: $100k/year
- UPS battery replacement eliminated: $40-80k/year
- BESS efficiency improvement: $50-100k/year (better PUE, less energy waste)
- **Total Annual O&M Savings: $190-280k/year**
- **10-Year O&M Savings: $1.9-2.8M**

**Plus Energy Efficiency Savings:**
- Traditional UPS losses: 4-8% of all power
- Wasted power: 7.4 MW × 5% = 370 kW continuous
- Annual energy waste: 370 kW × 8760 hrs = 3,241 MWh/year
- **Cost @ $0.08/kWh: $259k/year**
- **10-Year Energy Savings: $2.6M**

**Combined O&M + Energy Savings: $4.5-5.4M over 10 years**

---

## APPENDIX A: BESS RFI TEMPLATE

**Request for Information (RFI)**
**BESS-as-UPS System for 10 MW Data Center**

**To:** [Vendor Name]
**From:** Saga Energy / PGCIS
**Date:** October 25, 2025
**Response Due:** November 15, 2025

**Project Overview:**
Saga Energy is developing a 10 MW IT load data center in Pryor, Oklahoma with integrated 16 MW solar array. We are evaluating BESS-as-UPS architecture to eliminate traditional UPS systems while providing superior backup duration.

**System Requirements:**

**Phased Deployment:**
- Phase 0 (Day 1, 3.3MW IT): 2×4MW inverters + 15-18 MWh batteries
- Phase 1 (~Month 12, 6.6MW IT): +1×4MW inverter (NO additional batteries)
- Phase 2 (~Month 24, 10MW IT): +1×4MW inverter (NO additional batteries)
- **Total: 16MW/15-18MWh (4×4MW inverters, N+1 configuration)**

**Technical Specifications:**
- Chemistry: LFP (Lithium Iron Phosphate) required
- Inverter Type: **Grid-forming (NOT grid-following)** - CRITICAL
- Response Time: <50ms (ITIC compliant)
- Voltage Regulation: ±1% (ANSI C84.1)
- Frequency Regulation: ±0.1 Hz (IEEE 1547)
- THD: <5% (IEEE 519)
- Cycle Life: 6,000 cycles @ 80% DoD minimum
- Certifications: UL 9540, UL 9540A, NFPA 855 compliant

**Information Requested:**

**1. Pricing (Phased):**
- Phase 0 pricing (2×4MW inverters + 15-18 MWh batteries)
- Phase 1 incremental (1×4MW inverter only, NO additional batteries)
- Phase 2 incremental (1×4MW inverter only, NO additional batteries)
- Total target price: $7-10M (all phases complete)

**2. Lead Time & Delivery:**
- Manufacturing lead time from PO
- Delivery schedule (single shipment vs. phased)
- Installation duration estimate

**3. Technical Capabilities:**
- Confirm grid-forming inverter capability (spec sheet)
- Black-start capability (yes/no + spec)
- Seamless islanding/resynchronization (response time)
- N+1 configuration support (electrical drawings)

**4. Service & Support:**
- Service network coverage (distance from Pryor, OK 74361)
- 24/7 remote monitoring (included or additional cost?)
- Response time for critical issues (<4 hours required)
- Training program (duration, location, cost)

**5. Warranty & Guarantees:**
- Battery warranty (years, cycles, capacity retention %)
- Inverter warranty (years)
- Performance guarantees (efficiency, availability)
- Liquidated damages for late delivery?

**6. Reference Projects:**
- 3+ data center projects with similar configuration
- Contact information for references
- Site visit availability?

**7. Documentation:**
- Spec sheets (batteries, inverters, enclosures)
- UL 9540/9540A certificates
- Single-line diagram (typical for 4×4MW configuration)
- O&M manual (sample or table of contents)

**Evaluation Criteria:**
- Pricing: 30%
- Technical capability (grid-forming, N+1): 30%
- Lead time: 20%
- Service network: 10%
- Reference projects: 10%

**Questions? Contact:**
Benton Peret, Project Manager
Pachyderm Global / PGCIS
[Contact Information]

---

**Document Status:** TECHNICAL REFERENCE - COMPREHENSIVE
**Version:** 1.0
**Date:** 2025-10-20
**Next Review:** Following vendor RFI responses (Nov 1, 2025)

**Tags:** #saga-project #bess #technical-specs #commissioning #vendor-eval #ieee-2030 #nfpa-855 #ul-9540
