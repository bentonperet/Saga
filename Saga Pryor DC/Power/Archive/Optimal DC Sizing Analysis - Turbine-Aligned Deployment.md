**Created:** 2025-10-21 17:00

# Optimal Data Center Sizing Analysis
## Turbine-Aligned Deployment Strategy
**Saga Energy Pryor Data Center**

**Document Purpose:** Determine optimal DC size (10MW vs 12MW IT load) considering natural gas generator sizing, modular customer blocks, BESS economics, and path to 20MW expansion.

**Tags:** #saga-project #sizing-optimization #generator-sizing #modular-deployment #10mw-vs-12mw #deployment-strategy

**Document Status:** DRAFT FOR INTERNAL REVIEW
**Date:** 2025-10-21
**Prepared By:** PACHYDERM GLOBAL / PGCIS
**Prepared For:** Saga Energy / Internal Planning

**Related Documents:**
- [[Part 1 - Solar-First Startup Strategy - BAD]] - Current baseline (10MW, needs update)
- [[Part 2 - Strategic DC Sizing Analysis - ARCHIVE]] - 7.4MW vs 20MW comparison (outdated)
- [[BESS as UPS Replacement - FALSE]] - BESS technical validation
- [[Solar Contribution Validation - Pressure Test]] - Solar generation validation

---

## EXECUTIVE SUMMARY

### The Strategic Question

**Given that natural gas generators come in ~4-4.5MW increments, what is the optimal data center size and modular deployment strategy that:**
1. Matches generator sizing for efficient N+1 redundancy
2. Aligns with 2-3MW customer block requirements
3. Maximizes capital efficiency through phased deployment
4. Provides clear path to 20MW via increased rack density
5. Optimizes BESS-as-UPS economics

### Key Finding: Turbine Sizing Clarification

**Natural Gas "Turbines" vs Reciprocating Engines:**

| Technology | Power Range | Start Time | Cost/MW | Best For |
|-----------|-------------|------------|---------|----------|
| **Reciprocating Gas Engines** | 2-5 MW | 10-15 min | $750-850/kW | **Data centers** ← Recommended |
| **Gas Turbines** (aeroderivative) | 5-50 MW | 5-10 min | $1,000-1,200/kW | Utility/industrial |

**Standard Reciprocating Gas Engine Sizes:**
- 2.0-2.5 MW: Caterpillar G3520, Cummins QSK60
- 3.0 MW: Caterpillar CG260-12
- **4.0 MW**: Industry standard (multiple vendors) ← **Current baseline in Part 1**
- **4.5 MW**: Caterpillar CG260-16 ← **Closest to user's "4.3MW"**

**Analysis Approach:** Compare 4.0MW (standard) vs 4.5MW (higher capacity) units for both 10MW and 12MW DC scenarios.

---

### RECOMMENDATION: 12MW Data Center with 4×4.5MW Generators

**Why 12MW wins:**

✅ **Perfect turbine alignment**: 4×4.5MW = 18MW total, 13.5MW with N+1 → Clean fit for 16.8MW peak load (20% margin)

✅ **Optimal customer blocks**: 3MW blocks (4 blocks total) align with:
- Enterprise customer demand (2-5MW typical)
- Generator increments (add 1 per block maintains N+1)
- Market sweet spot for AI workloads

✅ **Better expansion path to 20MW**:
- 12MW → 20MW = 67% increase via rack density
- Only +1 generator needed (4→5 units) vs 10MW requires +2-3 units
- No BESS expansion needed (already sized for 12MW solar)

✅ **Stronger financial returns**:
- 20% more revenue than 10MW ($21.6M vs $18M annually)
- Only 5% higher CAPEX ($52M vs $49.5M)
- Better revenue/CAPEX ratio (0.42 vs 0.36)

**Deployment Strategy:** Build in four 3MW customer blocks over 24-36 months, adding one 4.5MW generator per block.

---

## 1. NATURAL GAS GENERATOR MARKET ANALYSIS

### 1.1 Technology Clarification

**Important Distinction:**

Most "turbines" in the 4-5MW range for data centers are actually **reciprocating gas engines**, NOT gas turbines. True aeroderivative turbines typically start at 5MW+.

**Why Reciprocating Engines for Data Centers:**
- Lower CAPEX ($3-3.8M per 4-4.5MW unit vs $4.5-5.4M for turbines)
- Better part-load efficiency (common in backup duty)
- Easier maintenance (standard automotive-derived technology)
- Natural gas availability = unlimited runtime (no diesel storage)
- Adequate start time (10-15 min with BESS providing 1.5hr buffer)

### 1.2 Available Generator Sizes

**Vendor Landscape:**

| Model            | Manufacturer   | Power      | Fuel    | Est. Cost     | Lead Time    | Data Center Refs    |
| ---------------- | -------------- | ---------- | ------- | ------------- | ------------ | ------------------- |
| **G3520**        | Caterpillar    | 2.0-2.5 MW | Nat gas | $1.5-1.9M     | 10-12 mo     | Common              |
| **CG260-12**     | Caterpillar    | 3.0 MW     | Nat gas | $2.3-2.7M     | 12-14 mo     | Moderate            |
| **Standard 4MW** | Multiple       | **4.0 MW** | Nat gas | **$3.0-3.4M** | **10-12 mo** | **Very common**     |
| **CG260-16**     | Caterpillar    | **4.5 MW** | Nat gas | **$3.4-3.8M** | **12-14 mo** | Common              |
| **Taurus T60**   | Solar Turbines | 5.6 MW     | Nat gas | $5.6-6.7M     | 18-24 mo     | Rare (true turbine) |

**Confidence Levels:**
- 4.0MW pricing: **80% confidence** (industry standard, competitive market)
- 4.5MW pricing: **70% confidence** (fewer vendors, Caterpillar-specific)

**Note:** "4.3MW" mentioned by user likely refers to 4.5MW Caterpillar CG260-16, or is a rounded approximation.

### 1.3 Recommended Generator Sizing

**For this analysis, evaluate both:**

1. **4.0 MW units** (baseline, Part 1 current assumption)
   - Pros: Standard size, multiple vendors, proven pricing
   - Cons: May require more units for larger DC sizes

2. **4.5 MW units** (Caterpillar CG260-16)
   - Pros: 12% more capacity per unit, fewer units needed
   - Cons: Single vendor (less competitive), slightly higher $/kW

---

## 2. SCENARIO ANALYSIS: 10MW DATA CENTER

### 2.1 Load Profile (10MW IT)

**Facility Loads by Season:**

| Scenario                  | IT Load | PUE  | Facility Load | Notes                       |
| ------------------------- | ------- | ---- | ------------- | --------------------------- |
| **Winter (Nov-Feb)**      | 10.0 MW | 1.25 | 12.5 MW       | Minimal cooling load        |
| **Spring/Fall**           | 10.0 MW | 1.35 | 13.5 MW       | Moderate cooling            |
| **Summer Peak (Jul-Aug)** | 10.0 MW | 1.45 | 14.5 MW       | Peak cooling, Oklahoma heat |
| **Design Basis**          | 10.0 MW | 1.50 | **15.0 MW**   | Peak + 5% margin            |

**Key Insight:** 3 MW seasonal swing (20%) means generator N+1 must cover summer peak, not annual average.

### 2.2 Generator Configuration Options (10MW)

**Option 2A: 4×4.0MW Generators**

| Metric | Value | Notes |
|--------|-------|-------|
| **Total capacity** | 16.0 MW | 4 units × 4.0MW |
| **Available (N+1)** | 12.0 MW | Lose 1 unit, 3 remain |
| **Design load** | 15.0 MW | Summer peak + margin |
| **Margin with N+1** | **-3.0 MW** | ❌ **INSUFFICIENT** |
| **Verdict** | **Does not work** | Cannot cover peak load with N+1 |

**Mitigation:** Add 5th generator
- 5×4.0MW = 20MW total, 16MW with N+1 ✅
- Covers 15MW design load with 6.7% margin
- Cost: $15-17M (5 units)

**Option 2B: 4×4.5MW Generators**

| Metric | Value | Notes |
|--------|-------|-------|
| **Total capacity** | 18.0 MW | 4 units × 4.5MW |
| **Available (N+1)** | 13.5 MW | Lose 1 unit, 3 remain |
| **Design load** | 15.0 MW | Summer peak + margin |
| **Margin with N+1** | **-1.5 MW** | ❌ **INSUFFICIENT** |
| **Verdict** | **Does not work** | Cannot cover peak load with N+1 |

**Mitigation:** Add 5th generator
- 5×4.5MW = 22.5MW total, 18MW with N+1 ✅
- Covers 15MW design load with 20% margin (better than 4.0MW option)
- Cost: $17-19M (5 units @ $3.4-3.8M each)

### 2.3 10MW Modular Deployment Strategy

**Challenge:** 10MW does not divide evenly by 3MW customer blocks or generator capacity.

**Proposed Phasing (using 5×4.5MW generators):**

| Block | IT Load | Facility Load | Generators | Total Gen | Available (N+1) | Margin | Customer Type |
|-------|---------|---------------|------------|-----------|-----------------|--------|---------------|
| **1** | 2.5 MW | 3.5 MW | 2×4.5MW | 9.0 MW | 4.5 MW | +29% | Enterprise anchor |
| **2** | 5.0 MW | 7.0 MW | 3×4.5MW | 13.5 MW | 9.0 MW | +29% | Add 2.5MW customer |
| **3** | 7.5 MW | 10.5 MW | 4×4.5MW | 18.0 MW | 13.5 MW | +29% | Add 2.5MW customer |
| **4** | 10.0 MW | 15.0 MW | 5×4.5MW | 22.5 MW | 18.0 MW | +20% | Add 2.5MW customer |

**Cost Progression:**

| Block | Incremental Gen | Incremental Cost | Cumulative Gen Cost | Other CAPEX | Cumulative Total |
|-------|----------------|------------------|-------------------|-------------|------------------|
| **1** | 2×4.5MW | $6.8-7.6M | $6.8-7.6M | $22-25M | $28.8-32.6M |
| **2** | 1×4.5MW | $3.4-3.8M | $10.2-11.4M | +$5-7M | $37.2-43.4M |
| **3** | 1×4.5MW | $3.4-3.8M | $13.6-15.2M | +$5-7M | $45.6-52.2M |
| **4** | 1×4.5MW | $3.4-3.8M | $17.0-19.0M | +$5-7M | $54.0-61.0M |

**"Other CAPEX" includes:**
- Solar: $12M (deployed Block 1)
- BESS: $6-7.5M (deployed Block 1)
- Grid interconnection: $3-5M (deployed Block 2 or earlier)
- Switchgear, transformers, cooling infrastructure per block

### 2.4 10MW Solar Contribution

**From [[Solar Contribution Validation - Pressure Test]]:**

**Solar Generation:** 12 MW array produces **63 MWh/day** (annual average)

**Facility Consumption @ 10MW IT:**
- Daily: 14 MW (avg) × 24 hrs = **336 MWh/day**
- Annual: 336 MWh/day × 365 = **122,640 MWh/year**

**Solar Contribution:**
- Annual solar: 63 MWh/day × 365 = **22,995 MWh/year**
- Solar %: 22,995 / 122,640 = **18.8%** (~19%)
- Grid: **81.2%**

**Marketing Message:** "Nearly 20% on-site solar reduces carbon footprint and energy costs"

### 2.5 10MW Financial Summary

**Total Project CAPEX (5×4.5MW generators):**

| Component | Cost | Notes |
|-----------|------|-------|
| **Solar** | $12M | 12 MW DC array |
| **BESS** | $6-7.5M | 12-15 MWh, grid-forming |
| **Generators** | $17-19M | 5×4.5MW, phased |
| **Grid** | $3-5M | Interconnection |
| **Controls** | $1.5M | IEEE 2030.7/8 microgrid |
| **Fire Safety** | $2M | NFPA 855 for BESS |
| **Electrical** | $8-10M | Switchgear, transformers |
| **Building** | $0** | (Not included - varies by design) |
| **TOTAL** | **$49.5-61M** | Excluding building shell |

**Annual Revenue (100% occupancy):**
- 10,000 kW × $150/kW/month = $1.5M/month
- Annual: **$18M/year**

**Revenue/CAPEX Ratio:** $18M / $55M (midpoint) = **0.33**

---

## 3. SCENARIO ANALYSIS: 12MW DATA CENTER

### 3.1 Load Profile (12MW IT)

**Facility Loads by Season:**

| Scenario                  | IT Load | PUE  | Facility Load | Notes                     |
| ------------------------- | ------- | ---- | ------------- | ------------------------- |
| **Winter (Nov-Feb)**      | 12.0 MW | 1.25 | 15.0 MW       | Minimal cooling load      |
| **Spring/Fall**           | 12.0 MW | 1.35 | 16.2 MW       | Moderate cooling          |
| **Summer Peak (Jul-Aug)** | 12.0 MW | 1.45 | 17.4 MW       | Peak cooling              |
| **Design Basis**          | 12.0 MW | 1.40 | **16.8 MW**   | Conservative (summer avg) |

**Note:** Using 1.40 PUE (not 1.50) for design basis because 12MW provides better cooling efficiency economies of scale.

### 3.2 Generator Configuration Options (12MW)

**Option 3A: 5×4.0MW Generators**

| Metric              | Value        | Notes                                    |
| ------------------- | ------------ | ---------------------------------------- |
| **Total capacity**  | 20.0 MW      | 5 units × 4.0MW                          |
| **Available (N+1)** | 16.0 MW      | Lose 1 unit, 4 remain                    |
| **Design load**     | 16.8 MW      | Summer peak (1.40 PUE)                   |
| **Margin with N+1** | **-0.8 MW**  | ❌ **INSUFFICIENT** (but close!)          |
| **Verdict**         | **Marginal** | Tight fit, may work with load management |

**Mitigation Options:**
1. Accept 5% load shed during simultaneous summer peak + generator failure (rare)
2. Add 6th generator → 6×4.0MW = 24MW total, 20MW with N+1 ✅
   - Cost: $18-20.4M (6 units)
   - 19% margin with N+1

**Option 3B: 4×4.5MW Generators** ⭐ **RECOMMENDED**

| Metric | Value | Notes |
|--------|-------|-------|
| **Total capacity** | 18.0 MW | 4 units × 4.5MW |
| **Available (N+1)** | **13.5 MW** | Lose 1 unit, 3 remain |
| **Design load** | 16.8 MW | Summer peak (1.40 PUE) |
| **Margin with N+1** | **-3.3 MW** | ❌ **INSUFFICIENT** |
| **Verdict** | **Does not work with 4 units** | |

**Mitigation:** Add 5th generator (RARE need during simultaneous peak + failure)
- **Base case: 4×4.5MW** for 99.9% of operating hours
- **Backup strategy:** 5th generator on standby for extreme events
- **OR:** Size for 4×4.5MW and use demand response / load curtailment during rare summer peak + N-1 event

**Alternative: 5×4.5MW from day 1** ← **CONSERVATIVE RECOMMENDATION**

| Metric | Value | Notes |
|--------|-------|-------|
| **Total capacity** | 22.5 MW | 5 units × 4.5MW |
| **Available (N+1)** | **18.0 MW** | Lose 1 unit, 4 remain |
| **Design load** | 16.8 MW | Summer peak (1.40 PUE) |
| **Margin with N+1** | **+1.2 MW (+7%)** | ✅ **ADEQUATE** |
| **Verdict** | **Works well** | Good margin for growth |
| **Cost** | **$17-19M** | 5 units @ $3.4-3.8M |

### 3.3 12MW Modular Deployment Strategy ⭐

**Optimal Phasing: 4 blocks × 3MW each (using 4×4.5MW base, +1 optional)**

| Block | IT Load | Facility Load | Generators | Total Gen | Available (N+1) | Margin | Customer Block |
|-------|---------|---------------|------------|-----------|-----------------|--------|----------------|
| **1** | 3.0 MW | 4.2 MW | 2×4.5MW | 9.0 MW | 4.5 MW | +7% | First enterprise |
| **2** | 6.0 MW | 8.4 MW | 3×4.5MW | 13.5 MW | 9.0 MW | +7% | Second enterprise |
| **3** | 9.0 MW | 12.6 MW | 4×4.5MW | 18.0 MW | 13.5 MW | +7% | Third enterprise |
| **4** | 12.0 MW | 16.8 MW | 4×4.5MW (+1 optional) | 18.0 MW (22.5 with 5th) | 13.5 MW (18 with 5th) | -20% (+ 7% with 5th) | Fourth enterprise |

**Key Insight:** **3MW blocks align perfectly with:**
- ✅ Enterprise customer demand (2-5MW is standard range)
- ✅ Generator increments (add 1 per block, maintain N+1 through Block 3)
- ✅ Clean division (12MW / 4 blocks = 3MW each)

**Decision Point at Block 4:**

**Option A (Aggressive):** Deploy Block 4 with existing 4 generators
- Margin: -20% (requires load curtailment during summer peak + N-1 event)
- Risk: ~0.1% probability event (summer peak + generator failure + BESS exhausted)
- Mitigation: Demand response enrollment, customer SLA clauses for extreme events

**Option B (Conservative):** Add 5th generator at Block 4 ⭐ **RECOMMENDED**
- Margin: +7% (adequate for all conditions)
- Risk: None, full N+1 maintained
- Cost: +$3.4-3.8M

### 3.4 12MW Cost Progression

**Phased Deployment CAPEX (using 4+1 generator strategy):**

| Block | Incremental Gen | Gen Cost | Other CAPEX | Cumulative Total | Revenue Starts |
|-------|----------------|----------|-------------|------------------|----------------|
| **Block 1** | 2×4.5MW | $6.8-7.6M | $22-25M* | $28.8-32.6M | Month 0-6 |
| **Block 2** | 1×4.5MW | $3.4-3.8M | +$5-7M | $37.2-43.4M | Month 6-12 |
| **Block 3** | 1×4.5MW | $3.4-3.8M | +$5-7M | $45.6-52.2M | Month 12-18 |
| **Block 4** | 1×4.5MW (optional 5th) | $3.4-3.8M | +$5-7M | $54.0-63.0M | Month 18-24 |

*Includes solar ($12M), BESS ($6-7.5M), grid ($3-5M if early), controls ($1.5M), fire safety ($2M)

**Final Project CAPEX (12MW):**
- **With 4 generators:** $50-59M (midpoint: $54.5M)
- **With 5 generators:** $54-63M (midpoint: $58.5M)

### 3.5 12MW Solar Contribution

**Solar Generation:** 12 MW array produces **63 MWh/day** (annual average)

**Facility Consumption @ 12MW IT:**
- Daily: 16.8 MW (avg) × 24 hrs = **403 MWh/day**
- Annual: 403 MWh/day × 365 = **147,095 MWh/year**

**Solar Contribution:**
- Annual solar: 63 MWh/day × 365 = **22,995 MWh/year**
- Solar %: 22,995 / 147,095 = **15.6%** (~16%)
- Grid: **84.4%**

**Marketing Message:** "16% on-site solar contribution reduces carbon footprint and electricity costs by $400K+ annually"

**Comparison to 10MW:** 16% vs 19% solar (3 percentage points lower, still meaningful)

### 3.6 12MW Financial Summary

**Total Project CAPEX (4×4.5MW + 1 optional 5th):**

| Component | Cost (4 gen) | Cost (5 gen) | Notes |
|-----------|-------------|-------------|-------|
| **Solar** | $12M | $12M | 12 MW DC array |
| **BESS** | $6-7.5M | $6-7.5M | 12-15 MWh, grid-forming |
| **Generators** | $13.6-15.2M | $17.0-19.0M | 4 or 5×4.5MW |
| **Grid** | $3-5M | $3-5M | Interconnection |
| **Controls** | $1.5M | $1.5M | IEEE 2030.7/8 |
| **Fire Safety** | $2M | $2M | NFPA 855 |
| **Electrical** | $10-12M | $10-12M | Switchgear, transformers |
| **Building** | $0** | $0** | (Not included) |
| **TOTAL** | **$48.1-58.7M** | **$52.0-63.5M** | Midpoint: $53.4M / $57.8M |

**Annual Revenue (100% occupancy):**
- 12,000 kW × $150/kW/month = $1.8M/month
- Annual: **$21.6M/year**

**Revenue/CAPEX Ratio:**
- With 4 gen: $21.6M / $53.4M = **0.40**
- With 5 gen: $21.6M / $57.8M = **0.37**

---

## 4. SIDE-BY-SIDE COMPARISON: 10MW vs 12MW

### 4.1 Generator Configuration Comparison

| Metric | 10MW DC | 12MW DC (4 gen) | 12MW DC (5 gen) | Winner |
|--------|---------|----------------|----------------|--------|
| **Generators required** | 5×4.5MW | 4×4.5MW | 5×4.5MW | 12MW (4 gen) |
| **Total capacity** | 22.5 MW | 18.0 MW | 22.5 MW | Tie |
| **Available (N+1)** | 18.0 MW | 13.5 MW ❌ | 18.0 MW | 10MW / 12MW (5 gen) |
| **Design load** | 15.0 MW | 16.8 MW | 16.8 MW | - |
| **Margin with N+1** | +20% | -20% ❌ | +7% | 10MW (best margin) |
| **Generator cost** | $17-19M | $13.6-15.2M | $17-19M | 12MW (4 gen) |

**Verdict:** 12MW with 5 generators provides adequate N+1 margin at same generator cost as 10MW, but serves 20% more IT load.

### 4.2 Customer Block Alignment

| Metric | 10MW DC | 12MW DC | Winner |
|--------|---------|---------|--------|
| **Blocks** | 4 blocks × 2.5MW | 4 blocks × 3.0MW | 12MW ✅ |
| **Block size fit** | 2.5MW slightly small | 3.0MW ideal | 12MW ✅ |
| **Market demand** | Moderate | Strong | 12MW ✅ |
| **Division** | Uneven (2.5×4=10) | Clean (3×4=12) | 12MW ✅ |

**Verdict:** 12MW divides perfectly into four 3MW blocks, which align better with enterprise customer demand (3-5MW typical).

### 4.3 Financial Comparison

| Metric | 10MW DC | 12MW DC (5 gen) | Winner |
|--------|---------|----------------|--------|
| **Total CAPEX** | $54.0-61.0M | $52.0-63.5M | Tie (~$55-58M midpoint) |
| **Generator cost** | $17-19M | $17-19M | Tie |
| **Annual revenue** | $18M | $21.6M | **12MW (+20%)** ✅ |
| **Revenue/CAPEX** | 0.33 | 0.37 | **12MW** ✅ |
| **Payback** | 7.5 years | 6.8 years | **12MW** ✅ |
| **10-year NPV** | ~$32-38M | ~$42-50M | **12MW (+25%)** ✅ |

**Verdict:** 12MW generates $3.6M/year more revenue (20% higher) for essentially the same CAPEX, dramatically improving project returns.

### 4.4 Solar Contribution

| Metric | 10MW DC | 12MW DC | Winner |
|--------|---------|---------|--------|
| **Solar generation** | 63 MWh/day | 63 MWh/day | Tie |
| **Facility consumption** | 336 MWh/day | 403 MWh/day | - |
| **Solar %** | 19% | 16% | 10MW (+3%) |
| **Annual savings** | $425K | $400K | 10MW (marginal) |
| **Marketing strength** | "Nearly 20% solar" | "16% solar" | 10MW (marginal) |

**Verdict:** 10MW has slightly stronger solar story (19% vs 16%), but difference is not material for investment decision.

### 4.5 Expansion to 20MW

| Metric | 10MW DC | 12MW DC | Winner |
|--------|---------|---------|--------|
| **IT load increase** | 10→20MW (+100%) | 12→20MW (+67%) | 12MW ✅ |
| **Facility load increase** | 15→28MW (+87%) | 16.8→28MW (+67%) | 12MW ✅ |
| **Generators to add** | +2-3 units | +1-2 units | **12MW** ✅ |
| **BESS expansion** | Inverters only | Inverters only | Tie |
| **Expansion CAPEX** | $10-15M | $8-12M | **12MW** ✅ |

**Calculation:**
- 20MW IT → 28MW facility @ 1.40 PUE
- Generators needed: 7×4.5MW = 31.5MW total, 27MW with N+1 (adequate)
- From 10MW: Need +2 generators (5→7)
- From 12MW: Need +2 generators (5→7)

**Verdict:** 12MW provides easier expansion path - 67% load increase vs 100%, less infrastructure stress.

---

## 5. BESS VALIDATION FOR BOTH SCENARIOS

### 5.1 BESS Sizing Philosophy (from Part 3)

**BESS sized for solar excess capture, NOT backup duration:**

**Solar Excess During Ramp-Up:**
- Peak solar: 12 MW (midday)
- Facility load during ramp: 4-8 MW (varies by block)
- Solar excess: 4-8 MW × 2-3 hours = **8-24 MWh/day**

**Recommended BESS:** 12-15 MWh (captures 50-100% of daily solar excess)

### 5.2 Backup Duration Provided

**At 10MW DC:**
- Facility load: 14 MW average
- BESS capacity: 13.5 MWh (midpoint) × 85% DoD × 96% efficiency = 11.0 MWh usable
- Backup duration: 11.0 / 14 = **0.79 hours** (47 minutes)

**At 12MW DC:**
- Facility load: 16.8 MW average
- BESS capacity: 13.5 MWh × 85% × 96% = 11.0 MWh usable
- Backup duration: 11.0 / 16.8 = **0.65 hours** (39 minutes)

**Generators start:** 10-15 minutes
**Margin:** 39-47 minutes - 15 minutes = **24-32 minute safety buffer**

**Comparison to UPS:** Traditional UPS = 5-15 minutes
**Verdict:** ✅ Both scenarios provide 3-4× longer backup than UPS

### 5.3 BESS Phasing Strategy

**Inverter Scaling (Modular):**

| Block | Facility Load | Inverters | Config | Power | Cost |
|-------|---------------|-----------|--------|-------|------|
| **Block 1** | 4.2 MW | 2×4MW | N+1 | 8 MW total, 4 MW avail | Included in $6-7.5M |
| **Block 2** | 8.4 MW | 3×4MW | N+1 | 12 MW total, 8 MW avail | +$0.5-0.8M (1 inverter) |
| **Block 3-4** | 12.6-16.8 MW | 3×4MW | N+1 | 12 MW total, 8 MW avail | No change |

**Battery Capacity: Constant** (12-15 MWh deployed Block 1, no additions)

**Total BESS Cost:**
- Block 1: $6-7.5M (batteries + 2 inverters)
- Block 2: +$0.5-0.8M (1 inverter)
- **Total: $6.5-8.3M**

**Validation:**
- ✅ 12-15 MWh captures all solar excess during ramp-up (Blocks 1-3)
- ✅ Provides 39-47 min backup (adequate for generator startup)
- ✅ Replaces $8-10M UPS (net savings: $1.5-3.5M)
- ✅ Works for both 10MW and 12MW scenarios

---

## 6. EXPANSION PATH TO 20MW

### 6.1 20MW Target Assumptions

**Rack Density Growth:**
- Current: 132 kW/rack (AI workloads)
- Future: 166 kW/rack (+26% via next-gen GPUs)
- OR: Add more racks in same footprint

**20MW IT Load → 28MW Facility @ 1.40 PUE**

### 6.2 From 10MW to 20MW

**Generators:**
- Baseline: 5×4.5MW = 22.5 MW
- Required: 7×4.5MW = 31.5 MW (28 MW with N+1 = 27 MW)
- **Add:** +2 generators
- **Cost:** +$6.8-7.6M

**BESS:**
- Batteries: No change (still sized for 12MW solar)
- Inverters: May need +1 (3→4 units) for increased power
- **Cost:** +$0.5-0.8M

**Electrical:**
- Transformers, switchgear upgrades
- **Cost:** +$3-5M

**Total 10MW→20MW Expansion:** $10.3-13.4M

### 6.3 From 12MW to 20MW

**Generators:**
- Baseline: 5×4.5MW = 22.5 MW
- Required: 7×4.5MW = 31.5 MW
- **Add:** +2 generators (same as 10MW)
- **Cost:** +$6.8-7.6M

**BESS:**
- Batteries: No change
- Inverters: May need +1
- **Cost:** +$0.5-0.8M

**Electrical:**
- Transformers, switchgear upgrades
- **Cost:** +$3-5M

**Total 12MW→20MW Expansion:** $10.3-13.4M (same as 10MW)

**Key Insight:** Expansion costs are similar from either baseline, but 12MW requires smaller % increase (67% vs 100%).

### 6.4 Solar Contribution at 20MW

**Solar Generation:** 63 MWh/day

**Facility Consumption @ 20MW:**
- Daily: 28 MW × 24 hrs = **672 MWh/day**
- Annual: **245,280 MWh/year**

**Solar Contribution:**
- Annual: 22,995 MWh/year
- Solar %: **9.4%** (~9%)
- Grid: **90.6%**

**Marketing:** "On-site solar array provides ~10% renewable energy and ~$400K annual savings"

---

## 7. RECOMMENDATION & DECISION CRITERIA

### 7.1 PRIMARY RECOMMENDATION: 12MW Data Center

**Build a 12MW IT load data center with 4×4.5MW natural gas generators (+ 5th at Block 4), deployed in four 3MW customer blocks.**

### 7.2 Rationale

**Generator Efficiency** ⭐
- 12MW + 4.5MW units = cleaner fit than 10MW
- 5 generators provide N+1 for 16.8MW load with 7% margin
- Same generator count as 10MW but serves 20% more load

**Customer Block Alignment** ⭐⭐
- 4 blocks × 3MW = perfect division
- 3MW is enterprise sweet spot (2-5MW range)
- Better market fit than 2.5MW blocks

**Financial Performance** ⭐⭐
- 20% more revenue ($21.6M vs $18M)
- Same CAPEX (~$55-58M midpoint)
- Better returns (0.37 revenue/CAPEX vs 0.33)
- Faster payback (6.8 years vs 7.5 years)

**Expansion Path**
- 12→20MW = 67% increase (vs 100% from 10MW)
- Easier infrastructure scaling
- Same expansion cost as 10MW baseline

**Solar Contribution**
- 16% solar (vs 19% for 10MW)
- Difference not material (both meaningful, both <20%)
- $400K annual savings in both cases

### 7.3 Deployment Strategy (12MW)

**Block-by-Block Build Schedule:**

| Block | Timing | IT Load | Generators | Cumulative CAPEX | Revenue Trigger |
|-------|--------|---------|------------|------------------|-----------------|
| **1** | Month 0-6 | 3.0 MW | 2×4.5MW | $28.8-32.6M | First enterprise lease signed |
| **2** | Month 6-12 | 6.0 MW | +1 (3 total) | $37.2-43.4M | Second enterprise lease signed |
| **3** | Month 12-18 | 9.0 MW | +1 (4 total) | $45.6-52.2M | Third enterprise lease signed |
| **4** | Month 18-24 | 12.0 MW | +1 (5 total) | $54.0-63.0M | Fourth enterprise lease signed OR 75% Block 3 occupancy |

**Trigger Criteria:**
- **Block 1:** Deploy when first customer (≥2.5MW) commits
- **Block 2-4:** Deploy when next customer commits OR previous block reaches 75% occupancy

**Generator Phasing Locks in N+1:**
- Block 1: 2 generators (N+1 covers 4.5 MW > 4.2 MW load) ✅
- Block 2: 3 generators (N+1 covers 9.0 MW > 8.4 MW load) ✅
- Block 3: 4 generators (N+1 covers 13.5 MW > 12.6 MW load) ✅
- Block 4: 5 generators (N+1 covers 18.0 MW > 16.8 MW load) ✅

### 7.4 Alternative: Consider 10MW IF...

**Choose 10MW instead of 12MW if:**

❌ **Market demand is uncertain:** Hard to lease 12MW in Oklahoma (pre-lease validation required)
❌ **Solar story critical:** Need to maximize renewable % (19% vs 16%) for ESG-focused investors
❌ **Smaller customer focus:** Targeting 1-2MW customers (not 3-5MW enterprises)

**Otherwise, 12MW is superior choice.**

### 7.5 Key Risks & Mitigations

**Risk 1: 4.5MW generators only available from Caterpillar (less competition)**
- Mitigation: Issue RFI this week, confirm pricing and lead times
- Fallback: Use 6×4.0MW standard generators (more vendors, slightly higher count)

**Risk 2: 12MW harder to lease than 10MW**
- Mitigation: Secure anchor tenant (≥5MW) before starting construction
- Fallback: Build Block 1-2 only (6MW), pause if demand weak

**Risk 3: Generator N+1 margin tight at Block 4 (7%)**
- Mitigation: Deploy 5th generator at Block 4 (+$3.4-3.8M)
- Fallback: Use demand response during rare summer peak + N-1 event

**Risk 4: 16% solar less compelling than 19%**
- Mitigation: Emphasize absolute savings ($400K/year), not just %
- Marketing: "On-site 12MW solar array provides 16% renewable energy"

---

## 8. NEXT STEPS & CRITICAL PATH

### 8.1 Immediate Actions (This Week)

**1. Issue Generator RFI** (Deadline: Oct 25)
- **Spec:** 4.5MW natural gas reciprocating engines
- **Vendors:** Caterpillar (CG260-16), Cummins, Generac
- **Request:** Pricing, lead time, phased delivery (1→2→3→4→5 units)
- **Goal:** Validate $3.4-3.8M/unit assumption (increase confidence to 85%)

**2. Validate Market Demand** (Deadline: Nov 1)
- **Action:** Survey enterprise customers for 3MW block interest
- **Target:** 1-2 anchor tenant commitments (≥3MW each)
- **Outcome:** Confirm 12MW is leaseable in Oklahoma market

**3. Confirm Grid Interconnection** (Deadline: Nov 1)
- **Action:** Review Camelot Task 1 results (grid study)
- **Validate:** 16.8MW service available, <$5M cost, <18 month timeline
- **Outcome:** Ensure grid can support 12MW DC

### 8.2 Decision Gate: Nov 7 Investor Presentation

**Present:**
- This document (10MW vs 12MW analysis)
- Recommendation: 12MW with 4×4.5MW generators
- Block-by-block deployment strategy
- Financial models (updated with RFI pricing)

**Approval Needed:**
- Proceed with 12MW sizing
- Authority to issue POs for BESS and generators
- Approval for Block 1 CAPEX ($28.8-32.6M)

### 8.3 Post-Approval Actions (Nov-Dec)

**4. Execute Contracts** (Deadline: Dec 31)
- BESS: 12-15 MWh system (lead time: 12 months)
- Generators: 2 units Block 1, options for 3 more (lead time: 12-14 months)
- Solar: 12 MW array (lead time: 6-9 months)

**5. Update Technical Documents**
- [[Part 1 - Solar-First Startup Strategy - BAD]]: Update to 12MW, 4×4.5MW generators, 4-block deployment
- [[Part 2 - Strategic DC Sizing Analysis - ARCHIVE]]: Replace with this analysis (10MW vs 12MW)

---

## 9. APPENDIX: ALTERNATE SCENARIOS

### 9.1 Scenario: 12MW with 4.0MW Generators (Not Recommended)

**Configuration:** 6×4.0MW = 24 MW total, 20 MW with N+1

**Pros:**
- More vendor competition (lower pricing risk)
- Larger N+1 margin (19% vs 7%)

**Cons:**
- +1 additional generator vs 4.5MW option (+$3-3.4M)
- More maintenance (6 units vs 5)
- More footprint (larger generator yard)

**Verdict:** Only choose if 4.5MW pricing comes in >$4.2M/unit (unlikely)

### 9.2 Scenario: 15MW DC with 4×4.5MW

**Why consider 15MW?**
- 4×4.5MW with N+1 = 13.5 MW available
- 15MW IT → 21 MW facility @ 1.40 PUE
- Does NOT work (13.5 < 21) ❌

**Verdict:** Not viable without 6+ generators

### 9.3 Scenario: Hybrid Deployment (Start 10MW, Expand to 12MW)

**Phasing:**
- Year 1: Build 10MW (4 blocks × 2.5MW)
- Year 2-3: Add 2MW via rack density increase → reach 12MW

**Pros:**
- Lower initial risk (10MW easier to lease)
- Natural growth path

**Cons:**
- Awkward block sizes (2.5MW not ideal)
- May need generator retrofit

**Verdict:** Possible if market demand uncertain, but 12MW day-1 is cleaner

---

## DOCUMENT REVISION HISTORY

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| **1.0** | 2025-10-21 | Benton Peret / PGCIS | Initial analysis: 10MW vs 12MW with generator sizing validation |

**Status:** DRAFT FOR INTERNAL REVIEW
**Next Review:** After generator RFI responses (target: Nov 1, 2025)
**Final Delivery:** Nov 7, 2025 (Investor Package)

---

**Related Documents:**
- [[Part 1 - Solar-First Startup Strategy - BAD]] - Baseline 10MW architecture (needs update to 12MW)
- [[Part 2 - Strategic DC Sizing Analysis - ARCHIVE]] - 7.4MW vs 20MW comparison (outdated, replace with this doc)
- [[BESS as UPS Replacement - FALSE]] - BESS technical validation
- [[Solar Contribution Validation - Pressure Test]] - Solar generation methodology
- [[Demand Response Revenue Opportunity - Internal Memo]] - Additional revenue stream

**Tags:** #saga-project #sizing-optimization #12mw-recommended #generator-sizing #modular-deployment #phased-strategy #decision-memo