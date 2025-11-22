**Created:** 2025-10-20 19:00
**Updated:** 2025-10-21 16:45 (v2.0 - Major revision post-meeting)

# Part 1: Technical Architecture & Modular Deployment
## 10 MW Data Center with BESS-as-UPS and Solar Integration
**Saga Energy Pryor Data Center**

**Document Purpose:** Technical feasibility analysis for a 10 MW data center using BESS-as-UPS architecture with modular deployment and grid-tied solar integration.

**Tags:** #saga-project #10mw #bess-sizing #modular-deployment #technical-architecture #client-deliverable

**Document Status:** DRAFT FOR CLIENT REVIEW - v2.0 (MAJOR UPDATE)
**Date:** 2025-10-21 (Updated post-meeting)
**Version:** 2.0 - See revision history at end for changes
**Prepared By:** PACHYDERM GLOBAL / PGCIS
**Prepared For:** Saga Energy

**Related Documents:**
- [[Part 2 - Strategic DC Sizing Analysis - ARCHIVE]] - Comparison of 10 MW vs. 20 MW options
- [[Feasibility Memo V3]] - Project requirements and strategic context (internal)
- [[Camelot SOW Summary]] - Pending grid interconnection study

---

## EXECUTIVE SUMMARY

### Strategic Challenge
**How do you optimize a 10 MW data center with integrated solar and BESS to maximize renewable energy utilization while maintaining grid reliability?**

Traditional approach: Separate UPS ($8-10M) + oversized BESS (48 MWh @ $24M) = $32-34M in power systems.
<!-- 48MW BESS has never been part of the equation, this should not be in there -->

**Recommended approach: BESS replaces UPS entirely + modular deployment in 2-3 MW customer blocks.**

### Key Findings

**1. BESS Replaces Traditional UPS Entirely**
- Traditional architecture: Separate UPS ($8-10M) + BESS for solar = $32-34M <!-- wrong size -->
- New approach: BESS with grid-forming inverters serves both functions = $6-7.5M
- **Total savings: $25-27M** while providing **6× longer backup** (1.5 hrs vs 15 min)

**2. Modular 2-3 MW Deployment Optimizes Capital Efficiency**
- Deploy power/cooling infrastructure in 2-3 MW blocks as customers lease space
- Aligns CAPEX with revenue, improves IRR
- Matches market demand (enterprises want 2-5 MW blocks, not full 10 MW)

**3. Solar Provides 25% of Annual Energy (Not Primary Power)**
- 12 MW solar array generates at full capacity only 5-6 hours/day
- 10 MW IT load runs 24/7 → grid power is required, not optional
- Solar supplements grid to reduce operating costs and carbon footprint 

**4. Natural Gas Turbines Eliminate Fuel Storage Complexity**
- Pipeline natural gas = unlimited runtime, no on-site diesel tanks
- 12-month lead time requires early procurement
- Lower emissions and operating costs vs. diesel 

### Financial Summary (10 MW Data Center)

**Total Project CAPEX:**
```
Core Infrastructure: $45-50M
  - Solar Array: $12M (12 MW DC)<!-- Remove array -->
  - BESS: $6-7.5M (12-15 MWh with grid-forming inverters)
  - Natural Gas Turbines: $12-15M (4×4 MW, N+1 redundancy)
  - Grid Interconnection: $3-5M <!-- confirm this -->
  - Microgrid Controls: $1.5M (IEEE 2030.7/8 compliant)
  - Fire Safety: $2M (NFPA 855 BESS protection)
  - Switchgear & Electrical: $8-10M

**Modular Deployment (2-3 MW Blocks):**
  - Deploy power/cooling as customers lease space
  - Initial block: ~$15-20M
  - Additional blocks: ~$5-7M each
```

**vs. Traditional Architecture:**
- Traditional UPS + oversized BESS: $44-47M
- **Net savings: $7-9M** ✅ <!-- confirm after resizing BESS to normal size, this doesn't change between the two options, it's just removal of UPS  - but we do have more cost for microgrid, etc. It's in the other docs, look that up -->

**Revenue & Returns:**
```
Annual Revenue (100% occupancy): $18M @ $150/kW/month × 10,000 kW
Monthly Revenue: $1.5M
Modular Ramp-Up:
  - First 3 MW block: $5.4M/year
  - At 5 MW (50%): $9M/year
  - At 10 MW (100%): $18M/year

IRR: 14-16% (improved with modular deployment)
Payback: 6-7 years
```

**Energy Profile (Grid-Tied Operation):**
```
Annual Energy Consumption: 10 MW IT × 1.4 PUE × 8,760 hrs = 123,000 MWh/year

Energy Sources:
- Solar: 25% (30,750 MWh/year) ☀️
- Grid: 75% (92,250 MWh/year) ⚡
- Generators: Emergency backup only (minimal annual usage) 🔥

Solar Reality: 12 MW solar generates at full capacity only 5-6 hours/day.
24/7 data center load requires grid as primary power source.
```

### Investment Decision

**✅ PROCEED IF:**
- Grid interconnection cost <$5M and available at facility opening (CRITICAL PATH)
- BESS vendor confirms grid-forming inverter capability meeting ITIC curve
- Natural gas service confirmed available with adequate capacity
- Customers identified for initial 2-3 MW blocks

**⚠️ VALIDATE BEFORE FINALIZING:**
- Issue BESS RFI for 12-15 MWh with grid-forming inverters (confirm Tesla/Fluence/Wärtsilä)
- Issue Natural Gas Turbine RFI (4×4 MW, note 12-month lead time)
- Confirm grid interconnection timeline with Camelot - must align with construction schedule
- Confirm natural gas line capacity during site visit (David/Aaron - Oct 22-23)

**🔴 RECONSIDER IF:**
- Grid interconnection timeline extends beyond facility completion (no operation without grid)
- BESS grid-forming capability cannot be validated
- Natural gas service unavailable (would require diesel + fuel storage complexity)

### Critical Path Actions (Before Nov 7 Investor Delivery)

**THIS WEEK (Oct 20-25):**
1. Issue BESS RFI (12-15 MWh, grid-forming, confirm vendors)
2. Issue Natural Gas Turbine RFI (4×4 MW, 12-month lead time)
3. Site visit: Confirm gas line capacity and pressure (David/Aaron)
4. Camelot: Request grid interconnection timeline clarity (CHILL vs HILL process)

**NEXT WEEK (Oct 27-Nov 1):**
5. Evaluate RFI responses and update CAPEX confidence
6. Finalize modular deployment phasing (2-3 MW block sizing)
7. Prepare solar analysis showing 25% annual contribution (send to David/Walker)
8. Prepare investor presentation materials

---

## 1. PROJECT CONTEXT & CONSTRAINTS

### 1.1 Site Characteristics

**Location:** Pryor, Oklahoma

**Solar Resource:**
- Capacity: 12 MW DC solar array (fixed constraint)
- Location: On-site, adjacent to data center facility
- Ownership: Saga Energy (project owner)
- Configuration: Behind-the-meter (BTM)

**Grid Availability:**
- Status: **REQUIRED for operations** - data center cannot operate without grid
- Timeline: Must be available at facility opening (CRITICAL PATH ITEM)
- Process: CHILL (interruptible) vs HILL (firm) interconnection - clarification needed from Camelot
- Distance: TBD (awaiting Camelot Task 1 - Market Study results)
- Cost: Estimated $3-5M (conservative assumption, to be validated)
- **10 MW load runs 24/7, solar only provides 25% of annual energy**

**Natural Gas:**
- Availability: Yes (industrial pipeline service available)
- Primary use: Generator fuel
- Pricing: $3-5/MCF (Oklahoma industrial rates)

### 1.2 Design Requirements

**Reliability:**
- Target: Tier III equivalent reliability
- N+1 redundancy at all levels (no single point of failure)
- 99.9%+ uptime guarantee

**Workload:**
- High-density AI workloads (up to 132 kW/rack)
- Mix of AI compute and network equipment
- Total IT Load: 10 MW (130 racks @ ~77 kW/rack average)
- Facility Load: ~14 MW @ 1.4 PUE

**Deployment:**
- Modular deployment in 2-3 MW blocks (align CAPEX with customer lease-up)
- Grid-tied operation from day 1 (grid power is required, not optional)
- Solar and BESS integrated for cost reduction and sustainability

**Renewable Integration:**
- Behind-the-meter solar integration
- Energy storage for solar excess capture
- Minimize curtailment of solar generation

### 1.3 Key Unknowns (Pending Camelot Market Study - Task 1)

**Critical Grid Questions:**
1. CHILL vs HILL interconnection process - which is appropriate? What are trade-offs?
2. Interconnection distance from site to nearest substation
3. Utility interconnection cost and timeline
4. Grid reliability statistics (uptime %) - affects generator sizing
5. Transmission capacity available
6. What % of time is CHILL power interrupted (if CHILL selected)?

**Impact on Strategy:**
- Grid must be available when facility opens - this is non-negotiable
- If grid timeline >18 months → Delays entire project (cannot operate without grid)
- CHILL vs HILL affects: reliability requirements, backup power sizing, operating costs
- Solar provides 25% of energy, grid provides 75% - no "off-grid" operation possible at 10 MW

**Decision Gate:** Grid interconnection process and timeline must be confirmed by Nov 1 to finalize construction schedule.

---

## 2. BESS SIZING PHILOSOPHY

### 2.1 BESS Sizing for 10 MW Data Center

**Core Principle:**
**BESS sized for backup duration and solar storage during lower occupancy periods, NOT solar excess at full load.**

**Reality Check at Full 10 MW Operation:**
```
Peak solar generation: 12 MW (5-6 hours/day)
Facility load: 14 MW (24/7 constant)
Solar excess at full load: 0 MW (solar < facility load)

Conclusion: At 10 MW, solar provides SUPPLEMENT to grid, not excess to store.
```

**Sizing Logic - Two Functions:**

**Function 1: Backup Duration (Primary)**
```
Target backup: 1.5 hours before generators start
Facility load: 14 MW peak
BESS capacity needed: 14 MW × 1.5 hrs = 21 MWh

BUT: Traditional UPS provides only 15 minutes
1.5 hours = 6× longer than UPS ✅
Conservative sizing: 12-15 MWh is adequate
```

**Function 2: Solar Storage During Ramp-Up (Secondary)**
```
During initial 30-50% occupancy (5-7 MW facility load):
Peak solar: 12 MW
Facility load: 5-7 MW
Solar excess: 5-7 MW × 2-3 peak hours = 10-21 MWh/day

12-15 MWh BESS captures most excess during ramp-up phase ✅
```

**Selected Size: 12-15 MWh**
- Cost: $6-7.5M (@ $500/kWh with grid-forming inverters)
- Backup: 1-1.5 hours @ 10-14 MW load (6× longer than traditional UPS)
- Solar storage: Adequate for ramp-up phase (30-50% occupancy)
- At full load: Primarily backup function, minimal solar excess to capture

### 2.2 BESS Operating Modes

**Grid-Tied Mode (All Phases):**
- BESS charges from solar during peak generation hours (10am-3pm)
- BESS maintains 90-100% State of Charge when not capturing solar excess
- Grid provides majority of power (75% annual average)
- Grid outage: BESS provides 1.5 hours backup → Generators start
- **Function: Solar cost reduction + reliable backup power**

### 2.3 Technical Requirements for BESS-as-UPS
**For complete technical requirements, specifications, and implementation details, see:**
- **[[BESS as UPS Replacement - FALSE]]** - Cost analysis, power quality proof, decision criteria
- **[[Technical Addendum - BESS Implementation Details - FALSE]]** - Detailed specs, IEEE/NFPA standards, commissioning timeline

**Summary:** BESS-as-UPS requires grid-forming inverters, IEEE 2030.7/2030.8 compliant controls, N+1 redundancy, and NFPA 855 fire safety compliance. All major vendors (Tesla, Fluence, Wärtsilä) support this configuration. Total cost: $1.5M for controls + $2M for fire safety (included in Phase 0 CAPEX). **Eliminates $8-10M traditional UPS** while providing **1.5 hours backup** vs. 15 minutes.

---

## 4. MODULAR DEPLOYMENT STRATEGY

### 4.1 Overview: 2-3 MW Customer Blocks

**Why Modular Deployment:**
- **Market Fit:** Enterprise customers want 2-5 MW blocks, not full 10 MW
- **Capital Efficiency:** Deploy power/cooling infrastructure only when customers sign leases
- **Better IRR:** Shorter window between CAPEX deployment and revenue generation
- **Risk Reduction:** Don't overbuild infrastructure before demand is proven

**Deployment Philosophy:**
```
Traditional: Build entire 10 MW upfront → Wait for customers → High carrying costs
Modular: Build first 3 MW block → Sign customer → Build next block → Repeat
```

**Power System Baseline (Full 10 MW):**

| Component | Specification | Quantity | Total Cost | Notes |
|-----------|---------------|----------|------------|-------|
| **Solar Array** | 12 MW DC | 1 array | $12M | Deploy upfront (long lead time) |
| **BESS** | 12-15 MWh, grid-forming | 1 system | $6-7.5M | Deploy upfront (replaces UPS) |
| **Nat Gas Turbines** | 4 MW each | 4 units | $12-15M | Deploy 1-2 per block as needed |
| **Grid Connection** | 138 kV interconnect | 1 connection | $3-5M | **Must be ready at opening** |
| **Microgrid Controls** | IEEE 2030.7/8 | 1 system | $1.5M | Deploy upfront |
| **Fire Safety** | NFPA 855 BESS | 1 system | $2M | Deploy with BESS |
| **Switchgear** | Per block | Modular | $8-10M | Deploy per block |
| **Cooling** | RDHx per rack | Modular | Variable | Deploy per customer |
| **Total** | | | **$45-55M** | Deployed over 18-24 months |

---

### 4.2 Block 1: First 2-3 MW (Months 0-12)

**Target:** Sign first anchor customer for 2-3 MW

**Infrastructure Deployment:**

**Deploy Upfront (Long Lead Items):**
```
- Solar Array: $12M (12 MW - cannot phase, long lead time)
- BESS: $6-7.5M (12-15 MWh - serves all blocks, replaces UPS)
- Grid Connection: $3-5M (required before any operations)
- Microgrid Controls: $1.5M (IEEE 2030.7/8 system)
- Fire Safety: $2M (NFPA 855 for BESS)
Upfront Total: $25-28M
```

**Deploy for Block 1 (Customer-Specific):**
```
- Natural Gas Turbines: 2×4 MW = $6-8M (N+1 for 3 MW load)
- Switchgear/Electrical: $2-3M (for 3 MW block)
- Cooling (RDHx): $200-400K (deployed per rack as customer installs)
- Building fit-out: $2-3M (cages, power distribution, monitoring)
Block 1 Total: $10-14M
```

**Block 1 Total CAPEX: $35-42M**

**Energy Balance (3 MW IT Load, 4.2 MW Facility Load):**
```
Daily consumption: 4.2 MW × 24 hrs = 101 MWh/day

Solar provides: 66 MWh/day (65% of daily energy) ☀️
Grid provides: 35 MWh/day (35%) ⚡
Annual solar contribution: ~40% (accounting for seasonal variation)
```

**Block 1 Economics:**
```
Revenue: 3,000 kW × $150/kW/month = $450k/month = $5.4M/year
OpEx: ~$2M/year (grid, gas, maintenance, solar O&M)
NOI: $3.4M/year
```

---

### 4.3 Block 2-3: Scale to 5-7 MW (Months 12-24)

**Target:** Add 2-4 MW in additional customer commitments

**Incremental Infrastructure:**
```
- Natural Gas Turbine: 1×4 MW = $3-4M (maintain N+1 as load grows)
- Switchgear: $1.5-2M per additional block
- Cooling: Deploy per customer
- Building: Minimal (hall pre-built)
Incremental: $5-7M per additional 2-3 MW block
```

**Energy Balance at 5 MW IT Load (7 MW Facility):**
```
Daily consumption: 7 MW × 24 hrs = 168 MWh/day

Solar provides: 66 MWh/day (39% of daily energy) ☀️
Grid provides: 102 MWh/day (61%) ⚡
Annual solar contribution: ~30%
```

**Economics at 5 MW:**
```
Revenue: 5,000 kW × $150 = $750k/month = $9M/year
OpEx: ~$3M/year
NOI: $6M/year
```

---

### 4.4 Block 4+: Scale to Full 10 MW (Months 24-36)

**Target:** Fill remaining capacity to 10 MW

**Incremental Infrastructure:**
```
- Natural Gas Turbine: 1-2×4 MW = $3-8M (final units for N+1 @ 10 MW)
- Switchgear: $3-4M for final blocks
- Cooling: Deploy per customer
Incremental: $6-12M
```

**Energy Balance at 10 MW IT Load (14 MW Facility):**
```
Daily consumption: 14 MW × 24 hrs = 336 MWh/day

Solar provides: 66 MWh/day (20% of daily energy) ☀️
Grid provides: 270 MWh/day (80%) ⚡
Annual solar contribution: ~25%

Reality: At full 10 MW, solar provides supplement only.
Grid is primary power source.
```

**Full 10 MW Economics:**
```
Revenue: 10,000 kW × $150 = $1.5M/month = $18M/year
OpEx: ~$5.5M/year (grid, gas, maintenance, insurance)
NOI: $12.5M/year

IRR: 14-16% (improved vs traditional due to modular deployment)
Payback: 6-7 years
```

---

### 4.5 Deployment Summary

**Total CAPEX by Milestone:**

| Milestone | Timing | Incremental | Cumulative | IT Load | Annual Revenue |
|-----------|--------|-------------|------------|---------|----------------|
| **Block 1** | Month 0-12 | $35-42M | $35-42M | 3 MW | $5.4M |
| **Block 2-3** | Month 12-24 | $10-14M | $45-56M | 5-7 MW | $9-12.6M |
| **Block 4+** | Month 24-36 | $6-12M | $51-68M | 10 MW | $18M |

**Key Advantages of Modular Approach:**
1. ✅ **Better IRR** - Deploy capital only when customers commit
2. ✅ **Lower Risk** - Don't overbuild before demand proven
3. ✅ **Market Fit** - 2-3 MW blocks match customer demand patterns
4. ✅ **Flexibility** - Can pause/adjust deployment based on market
5. ✅ **Cash Flow** - Revenue starts flowing before full build-out

---

## 5. GENERATOR SCALING REQUIREMENTS

### 5.1 Generator Sizing by Deployment Block

**Block 1 (3 MW IT Load):**
```
IT Load: 3 MW
Facility Load: 4.2 MW (@ 1.4 PUE)
Generator Requirement (N+1): 2×4 MW = 8 MW total, 4 MW available

Configuration:
- Quantity: 2 units (natural gas turbines)
- Rating: 4 MW each continuous
- Total capacity: 8 MW
- Available (N+1): 4 MW (lose one unit, 4 MW remaining)
- Margin: 4 MW available - 4.2 MW peak load = minimal margin

Cost: $6-8M ($3-4M per unit)
Runtime: 50-100 hrs/year (grid backup only, testing)
Fuel: $50-80k/year (minimal, emergency backup only)
```

**Block 2-3 (5-7 MW IT Load):**
```
IT Load: 5-7 MW
Facility Load: 7-10 MW (@ 1.4 PUE)
Generator Requirement (N+1): 3×4 MW = 12 MW total, 8 MW available

Configuration:
- Add 3rd unit (2→3 units)
- Total capacity: 12 MW
- Available (N+1): 8 MW
- Margin: 8 MW available - 10 MW peak load = minimal at high end

Incremental Cost: +$3-4M (3rd unit)
Cumulative Cost: $9-12M
Runtime: 50-100 hrs/year (grid backup only)
Fuel: $60-100k/year
```

**Full 10 MW Buildout:**
```
IT Load: 10 MW
Facility Load: 14 MW (@ 1.4 PUE peak)
Generator Requirement (N+1): 4×4 MW = 16 MW total, 12 MW available

Configuration:
- Add 4th unit (3→4 units)
- Total capacity: 16 MW
- Available (N+1): 12 MW
- Margin: 12 MW - 14 MW peak = need all 4 units for full N+1

Incremental Cost: +$3-4M (4th unit)
Cumulative Cost: $12-16M
Runtime: 50-100 hrs/year (grid backup only)
Fuel: $80-120k/year
```

### 5.2 Natural Gas Turbine Specifications

**Technology:** Natural Gas Turbines (DECISION CONFIRMED per 2025-10-21 meeting)

**Key Specifications:**
- Rating: 4 MW (4,000 kW) continuous @ 0.8 power factor
- Voltage: 480V output (matches critical bus voltage)
- Fuel: Pipeline natural gas (Oklahoma industrial service)
- Enclosure: Outdoor, tornado-rated (Oklahoma EF-2 requirement)
- Control: Automatic start, paralleling capability, remote monitoring
- Standards: IEEE 1547, UL 2200 certified
- **Lead Time: 12 months** (CRITICAL - order early in project)

**Why 4 MW Units?**
- Modular sizing matches 2-3 MW customer blocks
- N+1 redundancy achievable at all deployment stages
- Standard size for good vendor availability
- Parallel operation capability (2-4 units)

**Why Natural Gas Turbines vs. Diesel:**

| Factor | Natural Gas Turbines ✅ | Diesel (Not Selected) |
|--------|------------------------|----------------------|
| **Fuel Storage** | Pipeline (unlimited runtime) | Tanks required (EPA SPCC complexity) |
| **Fuel Cost** | $4-6/MMBtu (~$0.04-0.06/kWh) | $3-4/gal (~$0.12/kWh) |
| **Emissions** | Lower NOx, CO2, particulates | Higher emissions |
| **Maintenance** | Lower (cleaner combustion) | Higher (carbon buildup) |
| **Oklahoma Fit** | Pipeline infrastructure excellent | Must truck fuel to site |
| **Lead Time** | **12 months** | 6-9 months |
| **CAPEX** | $3-4M per 4 MW unit | $2.5-3M per unit |

**Critical Action:** Confirm gas line capacity and pressure during site visit (David/Aaron, Oct 22-23)

### 5.3 Generator Runtime (Grid-Tied Operation)

**All Blocks (Grid-Tied from Day 1):**
```
Grid outages: 3-5 per year (typical Oklahoma utility reliability)
Outage duration: 2-8 hours average
Monthly testing: 2 hours/month × 12 = 24 hrs/year
Annual runtime: 50-100 hrs/year (outages + testing)
Duty cycle: ~1% (minimal runtime, emergency backup only)
Classification: Standby duty
Maintenance: Annual preventive maintenance (1×/year per unit)
```

**Maintenance Cost Estimates:**

| Deployment Stage | Units | Annual Runtime | Maint Cost/Unit | Total Annual Maint |
|-----------------|-------|---------------|----------------|-------------------|
| **Block 1** | 2 units | 75 hrs | $50-60k | $100-120k |
| **Block 2-3** | 3 units | 75 hrs | $50-60k | $150-180k |
| **Full (10 MW)** | 4 units | 75 hrs | $50-60k | $200-240k |

**Key Insight:** With grid-tied operation from day 1, generators run minimal hours (emergency backup only). This extends maintenance intervals and reduces operating costs vs. any off-grid scenario.

### 5.4 Natural Gas Supply Requirements

**Pipeline Service (All Blocks):**
- **Requirement:** Firm capacity agreement with pipeline operator
- **Capacity Needed:** Sufficient for all generators running simultaneously (worst case)
  - Block 1: 2×4 MW = 8 MW peak demand
  - Full buildout: 4×4 MW = 16 MW peak demand
- **Consumption at Full Load:** ~160-200 MMBtu/hr (all 4 units)
- **Daily consumption (if 24-hr outage):** ~4,000-5,000 MMBtu
- **Oklahoma Infrastructure:** Excellent - Pryor area has robust industrial gas service

**No On-Site Fuel Storage Required:**
- Pipeline provides unlimited runtime (no diesel tanks needed)
- Eliminates EPA SPCC compliance for fuel storage
- Reduces site development costs and environmental permits
- **Trade-off:** Dependent on gas pipeline reliability (add to risk register)

**Critical Action Items:**
1. **Site Visit (Oct 22-23):** Confirm gas line pressure and capacity at site
2. **Utility Engagement:** Negotiate firm capacity agreement with gas provider
3. **Backup Plan:** Consider small propane tank for dual-fuel capability (optional)


---

## 6. TECHNICAL APPENDICES

**⚠️ APPENDIXES REQUIRE UPDATE ⚠️**

**Status:** The appendixes below are based on the OLD 7.4 MW sizing and Phase 0/1/2 structure. They need to be updated to reflect:
- 10 MW IT load (14 MW facility load)
- Modular 2-3 MW block deployment
- Natural gas turbine fuel calculations (not diesel)
- Grid-tied operation from day 1 (no off-grid Phase 0)
- 25% solar contribution (not 26% or 91%)

**Action Required:** Update Appendix B (Generator Sizing) and Appendix C (Solar Integration) before final delivery.

**For now, use the main document sections above for accurate 10 MW calculations.**

---

### Appendix A: BESS Technical Specifications for RFI

**For complete BESS RFI template and technical specifications, see:**
- **[[Technical Addendum - BESS Implementation Details - FALSE]]** - Appendix A contains full RFI template
- **[[BESS as UPS Replacement - FALSE]]** - Technical requirements and vendor evaluation criteria

**Quick Reference for RFI:**
- **Capacity:** 12-15 MWh (LFP chemistry)
- **Power:** 12 MW AC (3×4MW grid-forming inverters, N+1)
- **Configuration:** Grid-forming (NOT grid-following) - CRITICAL
- **Application:** Dual-mode (off-grid Phase 0, grid-tied Phase 1-2)
- **Lead Time:** ≤12 months
- **Vendors:** Tesla, Fluence, Wärtsilä

---

### Appendix B: Generator Sizing Calculations

**Load Profile by Phase:**

**Phase 0 (30% Occupancy):**
```
IT Load: 2.3 MW (48 racks × 48 kW × 30% occupancy)
PUE: 1.30 (low occupancy, proportionally more facility overhead)
Facility Load: 2.3 MW × 1.30 = 3.0 MW

Peak Load (summer): 3.0 MW × 1.05 = 3.15 MW
Generator Sizing (N+1): (3.15 MW ÷ (N-1)) where N = number of units
With N=2: (2-1) × X = 3.15 → X = 3.15 MW minimum
Selected: 2×4 MW = 8 MW total, 4 MW available (N+1)
Margin: 4 MW - 3.15 MW = 0.85 MW (27% margin) ✅
```

**Phase 1 (50% Occupancy):**
```
IT Load: 3.7 MW (50% occupancy)
PUE: 1.40 (mid occupancy)
Facility Load: 3.7 MW × 1.40 = 5.18 MW

Peak Load (summer): 5.18 MW × 1.05 = 5.44 MW
Generator Sizing (N+1): With N=3: (3-1) × 4 MW = 8 MW available
Margin: 8 MW - 5.44 MW = 2.56 MW (47% margin) ✅
```

**Phase 2 (100% Occupancy):**
```
IT Load: 7.4 MW (100% occupancy)
PUE: 1.42 (full occupancy, summer peak)
Facility Load: 7.4 MW × 1.42 = 10.51 MW

Peak Load (summer + margin): 10.51 MW × 1.05 = 11.04 MW
Generator Sizing (N+1): With N=4: (4-1) × 4 MW = 12 MW available
Margin: 12 MW - 11.04 MW = 0.96 MW (9% margin) ✅
```

**Fuel Consumption Calculations:**

**Phase 0 (Off-Grid, 2,500 hrs/year):**
```
Average load: 3 MW
Annual runtime: 2,500 hrs
Annual energy: 3 MW × 2,500 hrs = 7,500 MWh

Generator heat rate: 10,000 BTU/kWh (typical natural gas turbine)
Annual gas consumption: 7,500 MWh × 10,000 BTU/kWh = 75 billion BTU
In MCF: 75 billion BTU ÷ 1.03 million BTU/MCF = 72,815 MCF

Fuel cost @ $4/MCF: 72,815 × $4 = $291k
Or in $/kWh: 7,500 MWh × $0.04 = $300k
Rounded: ~$800k/year (includes testing, startup cycles, inefficiencies)
```

**Phase 1-2 (Grid-Tied, 100 hrs/year):**
```
Testing: 2 hrs/month × 12 = 24 hrs
Grid outages: 3-5 per year × 4 hrs avg = 12-20 hrs
Total: ~50-100 hrs/year

Annual energy: 10 MW × 100 hrs = 1,000 MWh
Annual gas: 1,000 MWh × 10,000 BTU/kWh ÷ 1.03M BTU/MCF = 9,709 MCF
Fuel cost: 9,709 MCF × $4 = $38.8k
Rounded: ~$50k/year
```

---

### Appendix C: Solar Integration Details

**Solar Array Configuration:**
- Capacity: 12 MW DC (approximately 10.5-11 MW AC after inverter losses)
- Technology: Monocrystalline silicon PV modules
- Mounting: Fixed-tilt ground mount (optimal for Oklahoma latitude)
- Orientation: South-facing, ~30° tilt
- Inverters: String inverters or central inverters (grid-forming not required for solar, BESS handles that)

**Annual Solar Generation (Pryor, Oklahoma):**
```
Solar irradiance: ~5.5 kWh/m²/day (annual average)
Capacity factor: ~20-22% (typical for fixed-tilt in Oklahoma)
Annual generation: 12 MW × 8,760 hrs × 21% CF = 22,031 MWh/year

Or by sun hours method:
12 MW × 5.5 sun hrs/day × 365 days = 24,090 MWh/year
(Includes seasonal variation, ~10% losses)
```

**Hourly Generation Profile (Summer Day):**

| Time | Solar Output | Facility Load | Excess to BESS | Notes |
|------|--------------|---------------|----------------|-------|
| 6am | 1 MW | 10 MW | 0 | Sunrise, BESS discharging |
| 8am | 5 MW | 10 MW | 0 | BESS still discharging |
| 10am | 10 MW | 10 MW | 0 | Solar matches load |
| 12pm | 12 MW | 10 MW | +2 MW | **Peak solar excess** |
| 2pm | 11 MW | 10 MW | +1 MW | Excess to BESS |
| 4pm | 8 MW | 10 MW | 0 | BESS charged, grid supplements |
| 6pm | 3 MW | 10 MW | 0 | Sunset, grid primary |
| 8pm | 0 MW | 10 MW | 0 | Grid + BESS backup |

**Daily Excess Solar:**
- Peak excess hours: 10am-3pm (~5 hours)
- Average excess: 1.5-2 MW during peak hours
- Daily excess: 1.5 MW × 5 hrs = 7.5 MWh (captured by 12-15 MWh BESS) ✅
- Curtailed: Minimal (BESS has adequate capacity)

**BESS Charge/Discharge Patterns:**

**Phase 0 (Off-Grid):**
```
6am-8am: BESS empty (0%), generators running
8am-3pm: BESS charging from solar excess (0% → 100%)
3pm-7pm: BESS at 100%, holding for nighttime discharge
7pm-11pm: BESS discharging (100% → 20%)
11pm-6am: BESS at 20% minimum, generators running
Daily cycles: 1 cycle @ 80% DoD (20% → 100% → 20%)
```

**Phase 1-2 (Grid-Tied):**
```
Daytime: BESS charges from solar excess to 90-100%
Nighttime: BESS holds at 90-100% (grid provides power)
Grid outage: BESS discharges for 1.5 hours, then generators start
Daily cycles: 0.2-0.3 cycles @ 30-40% DoD (normal operation, no outages)
Annual cycles: 100-150 cycles/year (mostly shallow discharge)
```

**Cycle Life Impact:**
- LFP warranty: 6,000 cycles @ 80% DoD = 20+ year lifespan
- Phase 0: 365 cycles/year × 1 year = 365 cycles (6% of warranty)
- Phase 1-2: 100 cycles/year × 20 years = 2,000 cycles (33% of warranty)
- **Total expected cycles: 2,365 cycles over 21 years** (40% of warranty) ✅
- No battery replacement needed within project life

---

### Appendix D: Grid Interconnection Checklist

**Information Needed from Camelot Task 1 (Market Study):**

**Interconnection Point:**
- Distance from site to nearest substation: ___ km/miles
- Substation name and voltage: ___ kV
- Substation capacity available: ___ MW
- Transmission line path: ___ (route description)

**Utility Requirements:**
- Utility name: Oklahoma Gas & Electric (OG&E) or Public Service Company of Oklahoma (PSO)
- Service voltage: 138 kV or 69 kV (preferred)
- Interconnection application process: ___ (timeline and steps)
- Study requirements: Impact study, protection study, etc.
- Queue position: ___ (if interconnection queue exists)

**Cost Estimates:**
- Line extension cost: $___ (based on distance)
- Substation upgrades: $___ (if needed)
- Protection equipment: $___ (relays, breakers)
- Engineering and permitting: $___
- **Total estimated cost: $___** (target: <$5M)

**Timeline:**
- Application to study completion: ___ months
- Study completion to construction start: ___ months
- Construction duration: ___ months
- **Total timeline: ___** months (target: <18 months)

**Reliability:**
- System Average Interruption Duration Index (SAIDI): ___ min/year
- System Average Interruption Frequency Index (SAIFI): ___ outages/year
- Estimated uptime: ___% (target: >99%)

**Decision Criteria:**
- If cost <$3M and timeline <12 months: May skip Phase 0 (wait for grid)
- If cost $3-5M and timeline 12-18 months: **Phase 0 strategy optimal** ✅
- If cost >$5M or timeline >18 months: Extended Phase 0 or reconsider architecture

---

## DOCUMENT REVISION HISTORY

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| **1.0** | 2025-10-20 | Benton Peret / PGCIS | Initial client-facing document (7.4 MW) |
| **2.0** | 2025-10-21 | Benton Peret / PGCIS | **MAJOR UPDATE:** Updated to 10 MW sizing, removed Phase 0 off-grid (not viable), changed to modular 2-3 MW blocks, natural gas turbines confirmed, corrected solar contribution to 25% |

**Status:** DRAFT FOR CLIENT REVIEW - **UPDATED POST-MEETING**
**Next Review:** After BESS & Generator RFI responses (target: Nov 1, 2025)
**Final Delivery:** Nov 7, 2025 (Investor Package)

**Key Changes in v2.0:**
- ✅ Data center size: 7.4 MW → **10 MW IT load** (14 MW facility load)
- ✅ Removed "Phase 0 off-grid operation" - grid required from day 1
- ✅ Solar contribution: Corrected from "91% Phase 0" to **25% annual** (realistic)
- ✅ Deployment strategy: Changed from 3 phases → **modular 2-3 MW customer blocks**
- ✅ Generators: Diesel → **Natural gas turbines** (12-month lead time)
- ✅ All financials recalculated for 10 MW
- ⚠️ Appendixes B & C: Flagged for update (still show old 7.4 MW calcs)

---

**Related Documents:**
- [[Part 2 - Strategic DC Sizing Analysis - ARCHIVE]] - Comparison of 10 MW vs. 20 MW options
- [[BESS as UPS Replacement - FALSE]] - Complete BESS-as-UPS technical analysis
- [[Feasibility Memo V3]] - Project requirements (internal)
- [[Basis of Design - Part 1 Core Systems]] - Complete facility design specs
- [[Camelot SOW Summary]] - Grid interconnection study (pending)
- [[saga-meeting-actions-2025-10-21]] - Action items from client meeting

**Tags:** #saga-project #10mw #bess-as-ups #modular-deployment #natural-gas-turbines #grid-required #client-deliverable #part-1
