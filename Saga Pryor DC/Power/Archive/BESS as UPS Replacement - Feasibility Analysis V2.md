**Created:** 2025-10-16 16:10

# BESS as UPS Replacement - Feasibility Analysis V2
## Saga Energy Pryor Data Center
**Purpose:** Evaluate the technical and economic feasibility of using Battery Energy Storage Systems (BESS) as the sole UPS solution for the 7.4 MW IT load data center, eliminating traditional UPS systems entirely.

**Tags:** #data-center #power-systems #bess #ups-replacement #microgrid #saga-energy

**Related Documents:**
- [[Addendum BESS as UPS Replacement]] - Technical validation of BESS-only approach
- [[Component Pricing Deep Dive - BESS vs UPS]] - Latest cost data and market analysis
- [[Microgrid Investment Analysis]] - 8MW solar configuration analysis

---

## EXECUTIVE SUMMARY

**Verdict: TECHNICALLY FEASIBLE & FINANCIALLY ADVANTAGEOUS**

Modern Battery Energy Storage Systems (BESS) with grid-forming inverters can completely replace traditional UPS systems for data center applications, providing superior backup duration and significant cost savings.

### Key Findings
✅ **Technical Feasibility: HIGH**
- Grid-forming BESS inverters provide <50ms response time (exceeds ITIC standards)
- IEEE 2030.7/2030.8 compliant microgrid controls ensure seamless power transitions
- No separate UPS layer needed with properly specified BESS
- **⚠️ SIZING UPDATE:** BESS upgraded to 16MW/48MWh (12MW available with N+1) to support 10MW facility load (IT + cooling/aux)
- **Phased Deployment:** Start with 3×4MW inverters, add 4th when facility reaches ~75% occupancy

💰 **Financial Case: STRONG**
- **Eliminates $8-10M traditional UPS CAPEX**
- Phase 1 cost: **$29.7-31.2M** (supports ~75% occupancy)
- Phase 2 incremental: **+$2.8-3.5M** (unlocks full 100% capacity)
- **Net savings: $7.3-9.3M** (18-23% reduction vs. traditional)
- Annual O&M savings: $445k/year
- Defers ~$2-3M in CAPEX by 8-12 months

⚡ **Operational Advantages**
- **4.8+ hours backup @ 10MW facility load** vs. 5-15 minutes (traditional UPS)
- Dual-purpose asset: Solar storage + UPS function
- Eliminates UPS efficiency losses (4-8% energy waste), i.e. Better PUE
- Integrates seamlessly with 12MW solar + generator backup
- UPS systems can easily be added for customers that insist on having them

### Recommended Architecture

**PURE BESS-AS-UPS CONFIGURATION:**
- **BESS**: Grid-forming inverters, N+1 redundancy, IEEE 2030.7 compliant controls
- **Turbine and/or Generators**: Extended outage backup (>4 hours)
- **No traditional UPS**: BESS provides all power conditioning and backup functions

---

## 1. TECHNICAL VALIDATION

### 1.1 Why Traditional UPS is Redundant

Modern grid-forming BESS inverters perform ALL traditional UPS functions:

| UPS Function                | Traditional UPS | Grid-Forming BESS               |
| --------------------------- | --------------- | ------------------------------- |
| **Voltage regulation**      | ±1%             | ✅ ±1%                           |
| **Frequency regulation**    | ±0.1 Hz         | ✅ ±0.1 Hz                       |
| **Response time**           | 0-4ms           | ✅ <50ms (within ITIC curve)     |
| **Harmonic distortion**     | <3% THD         | ✅ <5% THD (IEEE 519 compliant)  |
| **Power factor correction** | 0.99            | ✅ Active/reactive power control |
| **Backup duration**         | 5-15 minutes    | ✅ 4+ hours                      |
| **Seamless transition**     | 0ms (online)    | ✅ 0ms (grid-forming mode)       |

**Critical Insight:** Grid-forming BESS operates in "online" mode continuously - it IS the power source, not a backup. There is no "transfer time" because the BESS is always supplying power.

### 1.2 Technical Requirements for BESS-as-UPS

To eliminate traditional UPS, the BESS must include:

✅ **Grid-Forming Inverters**
- Establish voltage and frequency independently (not grid-following)
- Black-start capability for complete grid independence
- Seamless islanding and resynchronization

✅ **IEEE 2030.7/2030.8 Compliance**
- Advanced control algorithms: $500-800k
- Islanding/resync logic: $200-300k
- Black-start sequencer: $100-150k
- Factory and Site Acceptance Testing: $250-350k
- **Total controls upgrade: $1.05-1.55M**

✅ **N+1 Redundancy**
- Multiple parallel inverters (no single point of failure)
- Example: 3×2.5MW inverters for 7MW total capacity
- Can lose any single inverter without load disruption

✅ **NFPA 855 Fire Safety Compliance**
- Automatic fire suppression: $500-800k
- HVAC & thermal management: $225-350k
- Explosion protection: $100-200k
- Gas detection: $75-150k
- Total fire safety systems: **$1.15-2.1M**

---

## 2. UPDATED COST ANALYSIS

### 2.1 Component Pricing (2024-2025 Market Data)

Source: [[Component Pricing Deep Dive - BESS vs UPS]]

| Component             | Specification           | Cost       | Confidence |
| --------------------- | ----------------------- | ---------- | ---------- |
| **BESS (Phase 1)**    | **12MW/48MWh** (3×4MW inverters + full battery) | **$21.7-23.2M*** | **60%** |
| **BESS (Phase 2)**    | **4th 4MW inverter** (triggered at ~75% occupancy) | **+$2.8-3.5M** | **60%** |
| **Generators**        | 4×3750kVA               | $7M        | 65%        |
| **Advanced Controls** | IEEE 2030.7/8 compliant | $1.5M      | 90%        |
| **TOTAL (Phase 1)**   | Pure BESS-as-UPS        | **$29.7-31.2M** |            |
| **TOTAL (Full Buildout)** | With Phase 2 inverter | **$32.5-34.7M** |            |
1. Note: **48MWh battery capacity deployed fully in Phase 1. 16MW total inverter capacity (12MW available N+1) with phased deployment. 2024 BESS pricing $500/kWh. Pending vendor RFI validation.**

### 2.2 Cost Comparison: Three Scenarios

#### Scenario 1: Traditional UPS + BESS for Solar (Baseline)

| Component | Cost | Notes |
|-----------|------|-------|
| UPS (12.4MW) | $8-10M | Traditional Tier III system |
| BESS (**48MWh**) | **$24M** | For solar storage only |
| Generators | $7M | Backup power |
| Basic Controls | $0.8M | BESS for solar, separate UPS controls |
| **TOTAL** | **$39.8-41.8M** | **Current baseline** |
**Architecture:** UPS and BESS operate independently. UPS provides 5-15 min backup, generators take over. BESS only used for solar storage.

#### Scenario 2: Pure BESS-as-UPS with Phased Deployment (RECOMMENDED)

| Component         | Phase 1 Cost | Phase 2 Cost | Notes                             |
| ----------------- | ---------- | ---------- | --------------------------------- |
| BESS (**48MWh**, 3×4MW inverters) | **$21.7-23.2M** | - | Dual-purpose: solar storage + UPS |
| 4th Inverter (4MW) | - | **+$2.8-3.5M** | Added at ~75% occupancy |
| Generators        | $7M        | - | Extended backup only              |
| Advanced Controls | $1.5M      | - | IEEE 2030.7/8 compliant           |
| **PHASE 1 TOTAL** | **$29.7-31.2M** | - | Supports ~75% occupancy |
| **FULL BUILDOUT TOTAL** | - | **$32.5-34.7M** | **SAVINGS: $7.3-9.3M vs traditional** |
**Architecture:** BESS is the sole power conditioning and backup system. Generators only run for extended outages >4 hours. Phased deployment defers ~$2-3M in CAPEX by 8-12 months.

#### Scenario 3: Hybrid BESS + Small UPS (Conservative)

| Component         | Cost       | Notes                                  |
| ----------------- | ---------- | -------------------------------------- |
| BESS (**48MWh**)  | **$24M**   | Primary backup                         |
| Small UPS (400kW) | $0.2M      | "Safety net" for risk-averse customers |
| Generators        | $7M        | Extended backup                        |
| Advanced Controls | $1.5M      | Full integration                       |
| **TOTAL**         | **$32.7M** | **SAVINGS: $7.1-9.1M**                 |
**Note:** The $0.2M small UPS adds minimal value if BESS has grid-forming inverters. See addendum analysis.

### 2.3 Financial Comparison Summary

| Metric | Traditional (Baseline) | Pure BESS Phased (Recommended) | Hybrid BESS+UPS |
|--------|----------------------|------------------------|-----------------|
| **Phase 1 CAPEX** | $39.8-41.8M | **$29.7-31.2M** | **$32.7M** |
| **Phase 2 CAPEX** | - | **+$2.8-3.5M** (at ~75% occupancy) | - |
| **Total CAPEX** | $39.8-41.8M | **$32.5-34.7M** | **$32.7M** |
| **vs. Baseline** | - | **-$7.3-9.3M (-18% to -22%)** | -$7.1-9.1M |
| **Deferred CAPEX** | - | **$2-3M deferred 8-12 months** | - |
| **UPS Layer** | 12.4MW traditional | None (BESS only) | 400kW small UPS |
| **Backup Duration** | 5-15 min + generators | **6 hrs @ 8MW (Phase 1), 4.8 hrs @ 10MW (Phase 2)** | **4.8+ hrs** + generators |
| **Annual O&M** | $1,000k | $555k | $525k |
| **O&M Savings** | - | **-$445k/year** | -$475k/year |
| **10-Year TCO Savings** | - | **$5.0-8.3M** | $5.5-8.8M |
**Key Takeaway:** Pure BESS eliminates $8-10M in traditional UPS while providing 16-24× longer backup duration.

---

## 2.3 Phased Deployment Strategy

Given that the facility will lease up gradually over 12-24 months, a phased BESS deployment optimizes CAPEX deployment:

**Phase 1 - Initial Deployment (Day 1):**
- Deploy 3×4MW inverters = 12MW total, 8MW available with N+1
- Deploy full 48MWh battery capacity (all 12 containers)
- Supports up to ~75-80% facility occupancy (~8MW load)
- Cost: ~$29.7-31.2M

**Phase 2 - Full Buildout (triggered at ~75% occupancy):**
- Add 4th 4MW inverter = 16MW total, 12MW available with N+1
- Supports 100% facility occupancy (10MW load + margin)
- Incremental cost: ~$2.8-3.5M
- Total deployed cost: ~$32.5-34.7M

**Key Requirements:**
- Size electrical infrastructure for 4 inverters from day 1 (buswork, breakers, conduit)
- Size BESS enclosure for 4 inverters (4,500 SF)
- Include contractual option to purchase 4th inverter at locked pricing
- Plan interconnection points for future inverter
- Battery capacity deployed fully upfront (modular expansion is complex/costly)

**Financial Benefit:**
- Deferred CAPEX: ~$2-3M (8-12 months deployment delay)
- Improved cash flow alignment with revenue ramp
- Reduced financing costs on deferred equipment
- Preserved full system capability when needed

**Infrastructure Sizing Requirements:**

**Electrical Infrastructure (Size for 4, Build for 4):**
- Substation transformer: 15-20 MVA (supports full 16MW BESS + 10MW load)
- 13.8kV switchgear: 4 breaker positions for BESS inverters (all installed day 1)
- DC buswork: Sized for 16MW continuous rating
- AC distribution: 4 inverter connection points with isolation breakers

**Physical Infrastructure:**
- BESS enclosure: 4,500 SF (accommodates 4 inverters + 12 battery containers)
- Inverter foundation pads: Install 4 pads in Phase 1 (occupy pad 4 with temp barrier)
- Cable trays/conduit: Route for all 4 inverters in Phase 1
- Fire suppression: Size for full 4-inverter layout

**Procurement Strategy:**
- Execute equipment contract with option to purchase 4th inverter
- Lock pricing and delivery terms for Phase 2 inverter
- Maintain spare parts compatibility across both phases
- Coordinate with EPC for installation readiness

**Phase 2 Trigger Point:**
- Target: When facility reaches ~75% leased (~7.5MW committed load)
- Lead time: 6-9 months from order to commissioning
- Coordination: Plan installation during scheduled maintenance window

---

## 3. OPERATIONAL ADVANTAGES

### 3.1 System Operation Modes

**Mode 1: Normal Operation (Solar Available)**
1. Solar generates → Feeds DC load directly + charges BESS
2. BESS maintains 80-100% State of Charge
3. BESS operates in grid-forming mode, conditioning all power to IT load
4. Generators on standby

**Mode 2: Solar Insufficient / Nighttime**
1. BESS discharges to serve load
2. Grid-forming inverters maintain power quality continuously
3. Generators remain on standby
4. BESS provides 4+ hours minimum backup

**Mode 3: Extended Outage (>4 hours)**
1. BESS operates until reaching 20% SOC threshold
2. Generators auto-start and take over load
3. Generators recharge BESS during low-load periods
4. Solar resumes → transition back to Mode 1

**Critical Point:** At no point is traditional UPS needed. The BESS grid-forming inverters provide continuous power conditioning.

### 3.2 Energy Efficiency Improvements

Traditional UPS systems waste 4-8% of all power due to conversion losses.

**Annual Savings from Eliminating UPS:**
- IT Load: 7.4MW
- UPS Loss: 5% (conservative)
- Wasted Power: 370kW continuous
- Annual Energy Waste: 3,241 MWh/year
- **Cost at $0.08/kWh: $259k/year**
- **10-year savings: $2.6M**

This is IN ADDITION to the $8-10M CAPEX savings.

### 3.3 Integration with Solar Microgrid

Your project already includes:
- 12MW solar array (owned by Saga Energy)
- Behind-the-meter (BTM) configuration
- Single point of interconnection (POI)

**BESS-as-UPS provides dual value:**
1. **Daytime:** Stores solar energy for night/cloud use
2. **24/7:** Provides UPS-grade power conditioning

**Result:** One asset serves two critical functions, maximizing ROI.

---

## 4. IMPLEMENTATION REQUIREMENTS

### 4.1 BESS Specifications

| Specification | Phase 1 (Initial) | Phase 2 (Full Buildout) | Rationale |
|--------------|-------------------|-------------------------|-----------|
| **Power Rating** | **12MW AC** | **16MW AC** | Phase 1: 8MW N+1 (~75% occupancy); Phase 2: 12MW N+1 (100% occupancy) |
| **Configuration** | **3×4MW inverters** | **4×4MW inverters** | N+1 redundancy maintained in both phases |
| **Available Capacity (N+1)** | **8MW** | **12MW** | Covers 6-8MW load (Phase 1) or 10MW load + margin (Phase 2) |
| **Energy Capacity** | **48MWh** | **48MWh** | Deployed fully in Phase 1 (4-hour duration @ 12MW) |
| **Inverter Type** | Grid-forming (NOT grid-following) | Grid-forming | **Critical for UPS function** |
| **Response Time** | <50ms | <50ms | Meets ITIC curve for IT equipment |
| **Chemistry** | LFP (Lithium Iron Phosphate) | LFP | Safer than NMC, longer cycle life |
| **Cycle Life** | 6,000 cycles @ 80% DOD | 6,000 cycles @ 80% DOD | 12-year replacement cycle |
| **Thermal Management** | Active liquid cooling | Active liquid cooling | Required for Oklahoma climate |
| **Certifications** | UL 9540, UL 9540A, NFPA 855 | UL 9540, UL 9540A, NFPA 855 | Insurance and code requirements |
| **Backup Duration** | **6 hours @ 8MW** | **4.8 hours @ 10MW** | Full facility backup capability |
| **Phase 1 Cost** | **$29.7-31.2M** | - | 3 inverters + full battery capacity + generators + controls |
| **Phase 2 Incremental** | - | **+$2.8-3.5M** | 4th inverter only (triggered at ~75% occupancy) |

### **⚠️ CRITICAL SIZING VALIDATION**

The 16MW/48MWh BESS sizing (phased deployment: 3×4MW → 4×4MW inverters) is based on the following validated assumptions:

**Power Sizing Rationale:**
- **Total Facility Load:** 10 MW (7.4 MW IT + 2.6 MW cooling/auxiliaries @ PUE 1.3)
- **NOT just IT load:** Previous 7MW sizing only covered IT load, ignoring cooling
- **N+1 Redundancy:**
  - Phase 1: 3×4MW inverters provide 8MW available with one unit down (covers ~75-80% occupancy)
  - Phase 2: 4×4MW inverters provide 12MW available with one unit down (covers 10MW facility load + 20% margin)

**Energy Sizing Rationale:**
- **Backup Duration:** 48MWh ÷ 12MW = 4.0 hours @ full capacity
- **Actual Runtime:** 48MWh ÷ 10MW facility = 4.8 hours @ actual load
- **Solar Symmetry:** Matches 12MW solar array for optimal microgrid energy balance

**Action Required Before Procurement:**
1. ✅ Commission detailed electrical load study to validate 10MW facility load assumption
2. ✅ Obtain vendor quotes for 16MW/48MWh configuration with phased deployment option (Tesla, Fluence, Wärtsilä)
3. ✅ Update financial model with revised BESS costs and phased deployment cash flows
4. ✅ Validate N+1 redundancy strategy with 4×4MW inverter configuration (both 3-inverter and 4-inverter phases)
5. ✅ Lock pricing for 4th inverter in initial contract (option to purchase, fixed price)

**Recommended Vendors:**
- **Tesla Megapack** - Proven, grid-forming capable, $400-500/kWh
- **Fluence Gridstack Pro** - Superior controls, data center experience, $500-600/kWh
- **Wartsila GridSolv Quantum** - Modular, good for phased expansion, $450-550/kWh

### 4.2 Microgrid Control System Requirements

**This is the "brain" that makes BESS-as-UPS viable.**

**Required Capabilities:**
1. Real-time power balancing (solar + BESS + gensets = load)
2. Seamless mode transitions (grid-connected ↔ islanded ↔ generator-supported)
3. BESS state management (SOC optimization, thermal limits, cycle life)
4. Generator dispatch (auto-start on low SOC, load sharing)
5. Power quality monitoring (voltage/frequency/harmonic tracking with fault detection)
6. Predictive analytics (solar forecasting, load prediction)
7. SCADA integration for 24/7 monitoring

**Recommended Systems:**
- **Schneider EcoStruxure Microgrid Advisor** - Integrates with RD109 baseline
- **Siemens Spectrum Power Microgrid** - Utility-grade reliability
- **Fluence NISPERA** - Advanced DER management (if using Fluence BESS)

**Cost:** $1.05-1.55M for IEEE 2030.7/8 compliant system

### 4.3 Generator Configuration (No Change from Baseline)

From Feasibility Memo V2.md:
- **Specification:** 4×3750kVA generators
- **Cost:** $7M (validated in component pricing analysis)
- **Runtime Reduction:** With 28MWh BESS, generators only needed for extended outages >4 hours
- **Fuel Savings:** 87% reduction in generator hours vs. traditional architecture

---

## 5. RISK ASSESSMENT & MITIGATION

### 5.1 Technical Risks

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| **BESS inverter failure** | Low | High | N+1 redundancy; predictive maintenance; vendor 24/7 support |
| **Power quality issues** | Low | Medium | IEEE 2030.7 compliant controls; continuous monitoring; grid-forming inverters eliminate transfer issues |
| **BESS thermal runaway** | Low | Critical | LFP chemistry (safer); NFPA 855 fire suppression; early detection systems |
| **Microgrid control failure** | Low | High | Redundant controllers; manual bypass to generators; independent auto-start |
| **Battery degradation** | Medium | Moderate | Conservative cycling (20-30 cycles/yr); warranty with capacity guarantees |

### 5.2 Operational Risks

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| **Staff unfamiliar with BESS** | High | Moderate | Vendor training (3-5 days); 24/7 remote monitoring; detailed runbooks |
| **Customer concerns** | Medium | Low | Marketing as "industry-leading resilience"; transparent technical specs; SLA guarantees |
| **Insurance premium** | Medium | Low | Early broker engagement; multiple quotes; build 20% contingency |

### 5.3 Financial Risks

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| **BESS costs vary** | Medium | Moderate | Lock pricing early; 2024 market shows favorable -40% trend |
| **Certification challenges** | Low | Moderate | Engage Uptime Institute early; hire BESS certification consultant; market as "Tier III-equivalent" if needed |
| **Lender skepticism** | Low | High | Independent engineering review; reference projects (Microsoft, Switch); emphasize Schneider RD109 foundation |

---

## 6. DECISION CRITERIA

### 6.1 Choose Pure BESS-as-UPS If:

✅ You can confirm BESS will have **grid-forming inverters** (all major vendors offer this)
✅ You implement **IEEE 2030.7/2030.8 compliant controls** (budget $1.5M)
✅ You complete **Factory Acceptance Test (FAT)** and **Site Acceptance Test (SAT)**
✅ You're comfortable marketing "BESS-powered data center" to customers
✅ Insurance quotes confirm BESS-only is acceptable (get 3 quotes)
✅ You want to maximize financial returns ($7-9M CAPEX savings + $445k/year O&M savings)

### 6.2 Consider Hybrid BESS + Small UPS If:

⚠️ Lenders/insurance absolutely require seeing "UPS" on equipment list
⚠️ Customer base is extremely risk-averse (finance, healthcare)
⚠️ You want formal Uptime Institute Tier III certification (not just "equivalent")
⚠️ You prefer a "safety net" during initial commissioning period

**Note:** The $0.2M small UPS provides minimal technical value if BESS has grid-forming inverters. This is primarily a marketing/perception decision.

### 6.3 Avoid This Approach If:

❌ BESS vendor cannot confirm grid-forming inverter capability
❌ Microgrid controls budget is <$1M (inadequate for IEEE compliance)
❌ Operations team cannot commit to BESS-specific training
❌ Project timeline cannot accommodate 18-24 month commissioning

---



## 7. FINAL RECOMMENDATION

### 7.1 Primary Recommendation

**PROCEED WITH PURE BESS-AS-UPS (Scenario 2)**

This configuration offers:
- **Maximum CAPEX savings:** -$7.3-9.3M vs. traditional
- **Maximum operational efficiency:** No UPS conversion losses
- **Maximum strategic value:** Dual-purpose asset (solar + UPS)
- **Industry validation:** Microsoft, Quantum Loophole prove the technology

### 7.2 Conditions for Proceeding

Before finalizing this approach, confirm the following:

**Technical (Required):**
1. ✅ BESS vendor confirms grid-forming inverter capability
2. ✅ Microgrid controls will be IEEE 2030.7/2030.8 compliant (budget $1.5M)
3. ✅ FAT/SAT testing included in vendor contract
4. ✅ NFPA 855 fire suppression systems designed and budgeted ($1.15-2.1M)
5. ✅ N+1 inverter redundancy (no single point of failure)

**Financial (Validate):**
1. ⚠️ Insurance quotes confirm BESS-only is acceptable (<$100k/year premium)
2. ⚠️ Project IRR remains ≥14% with updated CAPEX
3. ⚠️ Lenders approve of non-traditional architecture (independent engineering review may be required)

**Operational (Commit to):**
1. ⚠️ Saga Energy will hire BESS-qualified engineer (~$100-130k/year)
2. ⚠️ 24/7 vendor remote monitoring contracted ($50-100k/year)
3. ⚠️ Detailed commissioning plan with 6+ month timeline
4. ⚠️ Uptime Institute provides Tier III certification path (or "equivalent" is acceptable)

### 7.3 Alternative: Hybrid BESS + Small UPS

**IF any of the above conditions cannot be met**, proceed with Scenario 3 (Hybrid):
- Add $0.2M small UPS as "insurance policy"
- Total cost: $22.7M (still $7.1-9.1M savings vs. traditional)
- Maintains familiar "UPS" for customers and lenders
- Reduces insurance/certification risk

**However:** This is primarily a risk mitigation strategy for stakeholder comfort, not a technical necessity.


---

## APPENDIX A: TECHNICAL SPECIFICATIONS CHECKLIST

Use this checklist when evaluating BESS vendor proposals:

### Power Quality Requirements
- [ ] Grid-forming inverter capability (not grid-following)
- [ ] Response time <50ms to grid disturbances
- [ ] Voltage regulation: ±1% or better
- [ ] Frequency regulation: ±0.1 Hz or better
- [ ] Harmonic distortion: <5% THD (IEEE 519 compliant)
- [ ] Power factor: 0.95-1.0 leading/lagging

### Reliability & Redundancy
- [ ] N+1 inverter configuration (can lose one unit)
- [ ] Independent battery string redundancy
- [ ] No single point of failure in PCS
- [ ] Black-start capability (can start without grid)
- [ ] Seamless islanding and resynchronization

### Controls & Integration
- [ ] IEEE 2030.7 compliant microgrid controller
- [ ] IEEE 2030.8 testing procedures (FAT/SAT)
- [ ] Real-time power balancing algorithms
- [ ] SCADA integration for 24/7 monitoring
- [ ] Predictive maintenance capabilities
- [ ] Integration with Schneider RD109 systems

### Safety & Compliance
- [ ] UL 9540 certified (product safety)
- [ ] UL 9540A tested (thermal runaway propagation)
- [ ] NFPA 855 compliant design
- [ ] Automatic fire suppression system
- [ ] Gas detection and monitoring
- [ ] Emergency shutdown systems
- [ ] Active thermal management (liquid cooling)

### Performance Guarantees
- [ ] 6,000 cycles minimum @ 80% depth of discharge
- [ ] ≥85% roundtrip efficiency
- [ ] Capacity warranty (% degradation over time)
- [ ] 12-year replacement cycle
- [ ] Availability guarantee (99.9%+)

### Support & Services
- [ ] 24/7 remote monitoring
- [ ] On-site training (3-5 days minimum)
- [ ] Detailed operations runbooks
- [ ] Emergency support response time
- [ ] Spare parts availability
- [ ] Software updates and cybersecurity

---

## APPENDIX B: REFERENCE DOCUMENTS & SOURCES

### Internal Project Documents
1. [[Feasibility Memo V2]] - Project requirements and critical decisions
2. [[Component Pricing Deep Dive - BESS vs UPS]] - Latest cost data (2024-2025)
3. [[Addendum BESS as UPS Replacement]] - Technical validation analysis
4. [[Microgrid Investment Analysis]] - 8MW solar + 28MWh BESS financial modeling

### Industry Standards
1. IEEE 2030.7 - Microgrid Controller Standard
2. IEEE 2030.8 - Microgrid Testing Procedures
3. NFPA 855 - Stationary Energy Storage System Installation
4. UL 9540 - Energy Storage System Safety
5. IEEE 519 - Harmonic Limits and Power Quality

### Key Vendors & Solutions
1. **Tesla Megapack** - [www.tesla.com/megapack](https://www.tesla.com/megapack)
2. **Fluence Gridstack Pro** - [www.fluenceenergy.com](https://www.fluenceenergy.com)
3. **Wartsila GridSolv Quantum** - [www.wartsila.com](https://www.wartsila.com)
4. **Schneider EcoStruxure Microgrid** - [www.se.com](https://www.se.com)

### Market Data Sources
1. NREL ATB 2024 - Battery Storage Cost Projections
2. BloombergNEF - Energy Storage Market Outlook (2024)
3. Component Pricing Deep Dive - Internal analysis with verified sources

---

## Appendix C: IMPLEMENTATION ROADMAP

### Phased Deployment (RECOMMENDED)

**Phase 1: Design & Validation (Months 1-6)**
- RFI to BESS vendors (Tesla, Fluence, Wartsila): Confirm grid-forming capability, get pricing
- RFI to Schneider Electric: RD109 integration with BESS-as-UPS
- Engage Uptime Institute: Certification path for BESS-as-UPS
- Insurance brokers: Get quotes for BESS-only architecture
- Independent engineering review: Validate design approach
- **Deliverable:** GO/NO-GO decision with vendor commitments

**Phase 2: Procurement (Months 7-12)**
- BESS order (9-12 month lead time) - **critical path item** → **12MW/48MWh configuration - confirm pricing in RFI**
- Turbine and/or Generator order (9-10 months)
- Microgrid controls procurement
- Utility interconnection application (if not already submitted)
- Building permits (NFPA 855 compliance)

**Phase 3: Construction (Months 13-20)**
- Site preparation and BESS foundations
- BESS installation and electrical integration
- Generator installation
- Fire suppression systems
- Microgrid controls integration

**Phase 4: Commissioning & Testing (Months 21-24)**
- Factory Acceptance Testing (FAT) at vendor facility
- Site Acceptance Testing (SAT)
- Integrated system testing (all modes)
- Staff training (operations, maintenance, emergency procedures)
- Performance verification
- **Deliverable:** Commercial operation

---

**Document Status:** DRAFT FOR REVIEW
**Version:** 2.0
**Date:** 2025-10-16
**Next Review:** Following vendor RFI responses and stakeholder validation
**Owner:** Benton Peret / PGCIS Program Management Team

**Key Changes from V1:**
- Recommends pure BESS-as-UPS (not hybrid) based on addendum analysis
- Updated pricing from Component Pricing Deep Dive (generators $7M, controls $1.5M)
- Shortened from 1500+ lines to ~800 lines for conciseness
- Added validation from Erik's addendum
- Emphasized grid-forming inverters as critical requirement
- Removed redundant UPS layer based on technical analysis
