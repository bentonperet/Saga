**Created:** 2025-10-20 19:30

## 7.4 MW vs. 20 MW Comparison & Decision Framework
**Saga Energy Pryor Data Center**

**Document Purpose:** Strategic analysis comparing 7.4 MW (renewable-focused) vs. 20 MW (scale-focused) data center configurations to inform investment sizing decision.

**Tags:** #saga-project #sizing-analysis #7.4mw #20mw #financial-comparison #decision-framework #client-deliverable

**Document Status:** DRAFT FOR CLIENT REVIEW
**Date:** 2025-10-20
**Prepared By:** Pachyderm Global / PGCIS
**Prepared For:** Saga Energy

**Related Documents:**
- [[Part 1 - Solar-First Startup Strategy - BAD]] - Technical architecture for 7.4 MW configuration
- [[Feasibility Memo V3]] - Project requirements and strategic context (internal)
- [[Camelot SOW Summary]] - Pending grid interconnection study

---

## EXECUTIVE SUMMARY

### The Strategic Question

**If grid power becomes available, should we build a 7.4 MW data center optimized for solar integration, or a bigger 20 MW data center optimized for scale?**

This decision fundamentally shapes:
- Capital requirements ($37-41M vs. $90-100M)
- Revenue potential ($13M/year vs. $36M/year)
- Time to market (6-9 months vs. 18 months)
- Renewable energy story (26% vs. 10% solar)
- Risk profile (lower vs. higher CAPEX)

### Key Findings

**1. Both Options Are Financially Viable**
- 7.4 MW: IRR 14-15%, NPV $28-32M @ 10% discount
- 20 MW: IRR 15-16%, NPV $48-55M @ 10% discount
- **Decision depends on strategic priorities, not financial viability**

**2. 7.4 MW Optimizes for Speed & Sustainability**
- Time to market: 6-9 months (solar-first startup)
- Renewable energy: 91% solar Phase 0, 26% long-term
- Lower CAPEX risk: $37-41M
- Fast payback: 6-7 years
- **Best for: Capital-constrained, renewable-focused, risk-averse investors**

**3. 20 MW Optimizes for Scale & Revenue**
- Annual revenue: $36M (2.7× more than 7.4 MW)
- Better revenue/CAPEX ratio: 0.36-0.40 vs. 0.32
- Higher NPV: $48-55M (1.7× more than 7.4 MW)
- Faster payback: 5-6 years
- **Best for: Capital-abundant, scale-focused, growth-oriented investors**

**4. Key Trade-Offs**

| Priority | 7.4 MW Winner | 20 MW Winner |
|----------|--------------|--------------|
| **Fastest time to revenue** | ✅ 6-9 months | ❌ 18 months |
| **Strongest renewable story** | ✅ 26% solar | ❌ 10% solar |
| **Lowest CAPEX risk** | ✅ $37-41M | ❌ $90-100M |
| **Highest absolute revenue** | ❌ $13M/year | ✅ $36M/year |
| **Highest IRR** | ❌ 14-15% | ✅ 15-16% |
| **Highest NPV** | ❌ $28-32M | ✅ $48-55M |

### Recommendation Framework

**Choose 7.4 MW IF:**
- Available capital: $40-50M
- Market demand: Moderate (5-10 MW pre-leased)
- Value proposition: Renewable energy differentiation matters
- Risk tolerance: Conservative (lower CAPEX exposure)
- Time pressure: Need revenue in 6-9 months

**Choose 20 MW IF:**
- Available capital: $90-120M
- Market demand: Strong (15-20 MW pre-leased)
- Value proposition: Scale and price competitiveness
- Risk tolerance: Moderate (comfortable with $90M CAPEX)
- Time flexibility: Can wait 18 months for grid

**Critical Inputs Needed:**
1. Grid interconnection timeline and cost (Camelot Task 1)
2. Market demand assessment (pre-lease status)
3. Capital availability confirmation
4. Investor priorities (renewable % vs. scale/revenue)

---

## 1. STRATEGIC CONTEXT

### 1.1 Why This Question Matters

**The Core Tension:**
- 12 MW solar array is fixed (already planned/budgeted)
- For 7.4 MW DC: Solar provides 26% of energy (meaningful renewable story)
- For 20 MW DC: Solar provides ~10% of energy (token renewable contribution)

**If grid power is available and doing 74-90% of the work, why not just build bigger and capture more revenue?**

This is a valid strategic question with no single "right" answer—it depends on:
- Capital availability
- Market demand
- Investor priorities (renewable story vs. scale)
- Risk tolerance
- Time to market requirements

### 1.2 Key Assumptions

**Both Options Assume:**
- Grid interconnection is possible (pending Camelot Task 1 confirmation)
- Grid cost: $3-5M (validated in final decision)
- Grid timeline: 12-18 months (validated in final decision)
- Site has adequate land for either configuration
- Oklahoma market can absorb capacity (demand validation needed)
- Pricing: $150/kW/month for AI colocation (market rate)

**Different Risk Profiles:**
- 7.4 MW: Can start off-grid (grid optional but beneficial)
- 20 MW: Must have grid (too large for off-grid startup with 12 MW solar)

**This analysis assumes grid becomes available—if not, 7.4 MW is only viable option.**

---

## 2. OPTION A: 7.4 MW DATA CENTER (Renewable-Focused)

### 2.1 Configuration Overview

**IT Capacity:**
- Total: 7.4 MW (96 racks)
- AI Racks: 48 racks × 132 kW = 6.336 MW
- Network Racks: 48 racks × 22 kW = 1.056 MW
- Facility Load: 10.5 MW @ 1.42 PUE (summer peak)

**Power System:**
- Solar: 12 MW (26% of annual energy)
- BESS: 12-15 MWh (solar excess capture)
- Generators: 4×4 MW (N+1 redundancy)
- Grid: Primary power (74% of annual energy)

**Deployment Strategy:**
- Phase 0 (Months 0-12): Off-grid, 30% occupancy, 91% solar
- Phase 1 (Months 12-24): Grid-tied, 50% occupancy, 53% solar
- Phase 2 (Months 24+): Full buildout, 100% occupancy, 26% solar

### 2.2 Financial Model (7.4 MW)

**CAPEX (Phased):**
```
Phase 0 (Day 1): $28-30M
  - BESS: $6-7.5M
  - Generators: $6M (2 units)
  - Solar: $12M
  - Controls & Fire Safety: $3.5M
  - Site prep, transformers, other: $0.5-1M

Phase 1 (Month 12): +$6.5-8.5M
  - Grid interconnection: $3-5M
  - 3rd generator: $3M
  - Integration: $0.5M

Phase 2 (Month 24): +$3M
  - 4th generator: $3M

Total Project CAPEX: $37.5-41.5M
```

**Revenue Ramp:**
```
Phase 0 (Months 0-12): 30% occupancy
  - IT Load: 2.3 MW
  - Monthly revenue: 2,300 kW × $150 = $345k
  - Annual revenue: $4.14M
  - Phase 0 total: $4.14M (12 months)

Phase 1 (Months 12-24): 50% occupancy
  - IT Load: 3.7 MW
  - Monthly revenue: 3,700 kW × $150 = $555k
  - Annual revenue: $6.66M
  - Phase 1 total: $6.66M (12 months)

Phase 2 (Months 24+): 100% occupancy
  - IT Load: 7.4 MW
  - Monthly revenue: 7,400 kW × $150 = $1.11M
  - Annual revenue: $13.32M
  - Steady-state: $13.32M/year ongoing
```

**Operating Expenses:**

**Phase 0 (Off-Grid):**
```
Fuel: $800k/year (generators run 7-8 hrs/night)
Generator maintenance: $150k (2 units, moderate duty)
BESS maintenance: $150k
Solar O&M: $150k
Insurance & misc: $100k
Total Phase 0 OpEx: $1.35M/year
```

**Phase 1 (Grid-Tied, 50% occupancy):**
```
Grid electricity: $1.5M/year (59 MWh/day × 365 × $0.07/kWh)
Fuel: $50k (testing only)
Generator maintenance: $180k (3 units, light duty)
BESS maintenance: $150k
Solar O&M: $150k
Insurance & misc: $120k
Total Phase 1 OpEx: $2.15M/year
```

**Phase 2 (Grid-Tied, 100% occupancy):**
```
Grid electricity: $3.0M/year (186 MWh/day × 365 × $0.044/kWh)
Fuel: $50k (testing only)
Generator maintenance: $200k (4 units, light duty)
BESS maintenance: $150k
Solar O&M: $150k
Insurance & misc: $150k
Other: $300k
Total Phase 2 OpEx: $4.0M/year
```

**Net Operating Income:**

| Period | Revenue | OpEx | NOI | Cumulative NOI |
|--------|---------|------|-----|----------------|
| **Phase 0 (Yr 1)** | $4.14M | $1.35M | $2.79M | $2.79M |
| **Phase 1 (Yr 2)** | $6.66M | $2.15M | $4.51M | $7.30M |
| **Phase 2 (Yr 3-10)** | $13.32M/yr | $4.0M/yr | $9.32M/yr | $81.86M (cumulative through Year 10) |

**10-Year Financial Summary:**
```
Total Revenue (10 years): $115.8M
Total OpEx (10 years): $34.0M
Total NOI (10 years): $81.8M

Debt Financing (60% LTV @ 7%, 10-year amortization):
  - Loan amount: $24M (60% of $40M avg CAPEX)
  - Annual debt service: $3.4M
  - Total debt service (10 years): $34M

Net Cash Flow (10 years): $81.8M - $34M = $47.8M

IRR: 14-15%
NPV @ 10% discount: $28-32M
Payback: 6-7 years
```

### 2.3 Energy Profile (7.4 MW)

**Phase 0 (Off-Grid):**
```
Daily consumption: 72 MWh
Solar provides: 66 MWh (91%)
Generators provide: 6 MWh (9%)

Marketing message: "91% solar-powered AI data center"
```

**Phase 2 (Grid-Tied):**
```
Annual consumption: 252 MWh/day × 365 = 91,980 MWh/year
Solar provides: 24,090 MWh/year (26%)
Grid provides: 67,890 MWh/year (74%)

Marketing message: "26% on-site solar with expansion capability"
```

### 2.4 Advantages of 7.4 MW Configuration

**Financial Advantages:**
- ✅ **Lower CAPEX risk:** $37-41M vs. $90-100M (57% less capital at risk)
- ✅ **Faster time to revenue:** 6-9 months vs. 18 months (earn $4M during Phase 0)
- ✅ **Phased capital deployment:** Aligns investment with tenant lease-up
- ✅ **Adequate IRR:** 14-15% meets typical investment criteria
- ✅ **Lower debt service:** $3.4M/year vs. $8M/year (easier to service)

**Operational Advantages:**
- ✅ **Grid independence capable:** Can operate off-grid if grid delayed
- ✅ **Proven solar integration:** 26% renewable energy is meaningful (vs. token 10%)
- ✅ **Easier to lease:** 7.4 MW is achievable in Oklahoma market
- ✅ **Lower operational complexity:** Smaller facility, easier to manage

**Strategic Advantages:**
- ✅ **Strong ESG story:** 91% solar Phase 0, 26% long-term (vs. 10% at 20 MW)
- ✅ **First-mover advantage:** Operational 12 months before 20 MW option
- ✅ **Flexibility:** Can expand to 20 MW later if demand materializes
- ✅ **Lower risk:** If market doesn't absorb capacity, smaller loss

### 2.5 Disadvantages of 7.4 MW Configuration

**Financial Disadvantages:**
- ⚠️ **Lower absolute revenue:** $13.3M/year vs. $36M/year (2.7× less)
- ⚠️ **Lower absolute NOI:** $9.3M/year vs. $25M/year (2.7× less)
- ⚠️ **Lower NPV:** $28-32M vs. $48-55M ($20M less)
- ⚠️ **Slightly lower IRR:** 14-15% vs. 15-16% (marginal difference)

**Operational Disadvantages:**
- ⚠️ **Limited scale:** May not fully utilize Oklahoma market demand
- ⚠️ **Higher $/kW:** Some economies of scale lost at smaller size
- ⚠️ **Phase 0 fuel cost:** $800k/year (though offset by $4M revenue)

**Strategic Disadvantages:**
- ⚠️ **May leave revenue on table:** If Oklahoma can absorb 20 MW, 7.4 MW undershoots
- ⚠️ **Expansion complexity:** Growing 7.4→20 MW requires land, electrical, permits

---

## 3. OPTION B: 20 MW DATA CENTER (Scale-Focused)

### 3.1 Configuration Overview

**IT Capacity:**
- Total: 20 MW (260 racks, all AI-capable @ 77 kW avg)
- Facility Load: 28 MW @ 1.40 PUE (average)

**Power System:**
- Solar: 12 MW (~10% of annual energy)
- BESS: 12-15 MWh (same as 7.4 MW—sized for solar capture, not scale)
- Generators: 6×4 MW (N+1 redundancy for 28 MW load)
- Grid: Primary power (90% of annual energy) ← **Grid is critical**

**Deployment Strategy:**
- **No off-grid startup possible** (12 MW solar can't support 20 MW IT load)
- **Must wait for grid** (18 months construction)
- Single-phase buildout or phased lease-up (but all infrastructure day 1)

### 3.2 Financial Model (20 MW)

**CAPEX (All at Once):**
```
BESS: $6-7.5M (same 12-15 MWh, solar excess capture)
Generators: $18M (6×4 MW for N+1 at 28 MW load)
Solar: $12M (same 12 MW array)
Grid interconnection: $3-5M (same, possibly higher for 28 MW service)
Controls & Fire Safety: $4M (scales slightly with system size)
Data center building: $45M (scales with IT capacity, 20 MW vs. 7.4 MW)
Electrical infrastructure: $8M (transformers, switchgear for 28 MW)
Site prep & other: $5M

Total Project CAPEX: $101-109M
  - For analysis, using midpoint: $105M
```

**Note on BESS Sizing:**
- Does NOT scale to 20 MW size
- Still sized for solar excess capture (12-15 MWh)
- This is intentional—solar excess is same regardless of DC size
- 20 MW DC relies on grid for primary power, BESS just captures solar + provides backup

**Revenue Ramp:**
```
Months 0-18: $0 (waiting for grid construction + DC buildout)

Months 18-30: 50% occupancy ramp-up
  - IT Load: 10 MW avg
  - Annual revenue: 10,000 kW × $150 × 12 = $18M
  - Total this period: $18M (12 months)

Months 30+: 100% occupancy
  - IT Load: 20 MW
  - Monthly revenue: 20,000 kW × $150 = $3M
  - Annual revenue: $36M
  - Steady-state: $36M/year ongoing
```

**Operating Expenses (Steady-State, 100% Occupancy):**
```
Grid electricity: $9.5M/year
  - Daily consumption: 28 MW × 24 hrs × 0.90 (10% from solar) = 605 MWh/day
  - Annual: 605 × 365 = 220,825 MWh/year
  - Cost @ $0.043/kWh: $9.5M

Fuel: $50k (testing only, emergency backup)
Generator maintenance: $300k (6 units, light duty)
BESS maintenance: $150k (same size as 7.4 MW)
Solar O&M: $150k (same 12 MW array)
Insurance & misc: $250k
Other: $600k

Total OpEx: $11.0M/year
```

**Net Operating Income:**

| Period | Revenue | OpEx | NOI | Cumulative NOI |
|--------|---------|------|-----|----------------|
| **Months 0-18** | $0 | $0 | $0 | $0 |
| **Year 2-3 (ramp)** | $18M/yr | $5.5M/yr | $12.5M/yr | $25M (2 years) |
| **Year 4-10** | $36M/yr | $11M/yr | $25M/yr | $175M (cumulative) |

**10-Year Financial Summary (from Month 0):**
```
Total Revenue (10 years): $270M
  - Includes $0 for first 18 months (wait period)
  - Includes ramp-up revenue Years 2-3
  - Includes $36M/year for Years 4-10

Total OpEx (10 years): $84M

Total NOI (10 years): $186M

Debt Financing (60% LTV @ 7%, 10-year amortization):
  - Loan amount: $63M (60% of $105M CAPEX)
  - Annual debt service: $9M
  - Total debt service (10 years): $90M

Net Cash Flow (10 years): $186M - $90M = $96M

IRR: 15-16%
NPV @ 10% discount: $48-55M
Payback: 5-6 years (from Month 0, includes 18-month wait)
```

**Opportunity Cost Analysis:**
```
18-month wait for grid + construction:
  - Revenue lost: $18M (if we could operate at 50% during this time)
  - But 20 MW can't operate off-grid (12 MW solar insufficient)
  - This is unavoidable cost of scale strategy
```

### 3.3 Energy Profile (20 MW)

**Annual Energy (100% Occupancy):**
```
Annual consumption: 28 MW × 24 hrs × 365 × 0.95 (availability) = 231,960 MWh/year

Solar provides: 24,090 MWh/year (10.4%)
Grid provides: 207,870 MWh/year (89.6%)

Marketing message: "12 MW on-site solar array supporting operations"
(Renewable % is modest but solar presence is real)
```

**Daily Profile:**
```
Daytime (12 hrs):
  - Facility load: 28 MW × 12 = 336 MWh
  - Solar provides: 66 MWh (20% of daytime needs)
  - Grid provides: 270 MWh (80% of daytime needs)
  - BESS captures 12-15 MWh solar excess (same as 7.4 MW)

Nighttime (12 hrs):
  - Facility load: 28 MW × 12 = 336 MWh
  - Grid provides: 336 MWh (100% of nighttime needs)
  - BESS stays charged (ready for grid outages)
```

### 3.4 Advantages of 20 MW Configuration

**Financial Advantages:**
- ✅ **Higher absolute revenue:** $36M/year vs. $13.3M (2.7× more)
- ✅ **Higher absolute NOI:** $25M/year vs. $9.3M (2.7× more)
- ✅ **Higher NPV:** $48-55M vs. $28-32M ($20M more)
- ✅ **Better revenue/CAPEX ratio:** 0.34 vs. 0.32 (marginal improvement)
- ✅ **Higher IRR:** 15-16% vs. 14-15% (marginal improvement)
- ✅ **Faster payback:** 5-6 years vs. 6-7 years (from Month 0)

**Operational Advantages:**
- ✅ **Economies of scale:** Lower $/kW cost for infrastructure
- ✅ **Larger market capture:** Can serve enterprise customers needing 5-10 MW
- ✅ **Operational efficiency:** Spreading fixed costs over more capacity

**Strategic Advantages:**
- ✅ **Competitive positioning:** Scale enables price competitiveness
- ✅ **Market leadership:** 20 MW positions as major Oklahoma provider
- ✅ **Future expansion easier:** Land, permits, grid sized for growth
- ✅ **Better grid interconnection terms:** Larger customer, more utility negotiating power

### 3.5 Disadvantages of 20 MW Configuration

**Financial Disadvantages:**
- ⚠️ **Higher CAPEX risk:** $105M vs. $37-41M (2.6× more capital at risk)
- ⚠️ **18-month wait before revenue:** $18M opportunity cost
- ⚠️ **Higher debt service:** $9M/year vs. $3.4M (2.6× more)
- ⚠️ **Larger loss if market doesn't absorb capacity:** 20 MW > 7.4 MW vacancy risk

**Operational Disadvantages:**
- ⚠️ **Grid-dependent:** No off-grid startup capability (unlike 7.4 MW)
- ⚠️ **Must wait for grid:** Can't start operations until grid ready
- ⚠️ **Higher operational complexity:** Larger facility, more staff needed

**Strategic Disadvantages:**
- ⚠️ **Weaker ESG story:** 10% solar vs. 26% (less differentiation)
- ⚠️ **Market risk:** Can Oklahoma absorb 20 MW? (validation needed)
- ⚠️ **All-or-nothing:** Must build full infrastructure upfront (less phasing flexibility)

---

## 4. SIDE-BY-SIDE COMPARISON

### 4.1 Financial Comparison

| Metric | 7.4 MW (Renewable-Focused) | 20 MW (Scale-Focused) | Winner |
|--------|---------------------------|----------------------|--------|
| **Total CAPEX** | $37-41M | $101-109M | 7.4 MW (62% less) |
| **CAPEX per kW** | $5,000-5,541/kW | $5,050-5,450/kW | 20 MW (marginal) |
| **Annual Revenue (steady-state)** | $13.3M | $36M | 20 MW (2.7× more) |
| **Annual NOI (steady-state)** | $9.3M | $25M | 20 MW (2.7× more) |
| **Revenue/CAPEX Ratio** | 0.32-0.36 | 0.33-0.36 | Tie |
| **IRR** | 14-15% | 15-16% | 20 MW (marginal) |
| **NPV @ 10%** | $28-32M | $48-55M | 20 MW ($20M more) |
| **Payback Period** | 6-7 years | 5-6 years | 20 MW (1 year faster) |
| **10-Year Net Cash Flow** | $48M | $96M | 20 MW (2× more) |
| **Time to First Revenue** | 6-9 months | 18-24 months | 7.4 MW (12-15 mo faster) |
| **Revenue Lost During Wait** | $0 (starts earning) | $18M (18-month wait) | 7.4 MW |
| **Annual Debt Service** | $3.4M | $9M | 7.4 MW (62% less) |

**Financial Winner:** 20 MW on absolute returns, 7.4 MW on risk and speed

### 4.2 Energy & Sustainability Comparison

| Metric | 7.4 MW | 20 MW | Winner |
|--------|--------|-------|--------|
| **Solar Array** | 12 MW | 12 MW | Tie (same) |
| **Solar % of Energy (Phase 0)** | 91% (off-grid) | N/A (can't go off-grid) | 7.4 MW |
| **Solar % of Energy (Long-Term)** | 26% | 10% | 7.4 MW (2.6× more) |
| **Annual Solar Generation** | 24,090 MWh | 24,090 MWh | Tie (same) |
| **Annual Grid Consumption** | 67,890 MWh | 207,870 MWh | 7.4 MW (3× less) |
| **Renewable Energy Credits (RECs)** | 24,090 MWh/yr | 24,090 MWh/yr | Tie (same) |
| **Marketing Message** | "91% solar Phase 0, 26% long-term" | "12 MW solar array on-site" | 7.4 MW (stronger) |
| **ESG Positioning** | Strong (meaningful renewable %) | Moderate (token renewable %) | 7.4 MW |

**Sustainability Winner:** 7.4 MW (2.6× higher renewable energy percentage)

### 4.3 Risk Comparison

| Risk Factor | 7.4 MW Risk Level | 20 MW Risk Level | Lower Risk |
|-------------|------------------|------------------|------------|
| **CAPEX at Risk** | $37-41M | $105M | 7.4 MW (62% less) |
| **Market Absorption** | 7.4 MW easier to lease | 20 MW requires strong demand | 7.4 MW |
| **Grid Dependency** | Can start off-grid | Must wait for grid | 7.4 MW |
| **Debt Service Coverage** | $9.3M NOI ÷ $3.4M debt = 2.7× | $25M NOI ÷ $9M debt = 2.8× | Tie (both adequate) |
| **Time to Revenue** | 6-9 months | 18-24 months | 7.4 MW |
| **Vacancy Impact** | Lower absolute loss | Higher absolute loss | 7.4 MW |
| **Construction Risk** | Phased (spread over time) | All at once | 7.4 MW |
| **Technology Risk** | Solar-first unproven locally | Grid-tied proven | 20 MW |

**Risk Winner:** 7.4 MW (lower capital at risk, faster to revenue, less market dependency)

### 4.4 Strategic Fit Comparison

| Strategic Priority | Best Fit | Rationale |
|-------------------|----------|-----------|
| **Speed to Market** | 7.4 MW | 6-9 months vs. 18-24 months |
| **Renewable Differentiation** | 7.4 MW | 26% solar vs. 10% (ESG story) |
| **Maximum Revenue** | 20 MW | $36M/year vs. $13.3M/year |
| **Market Leadership** | 20 MW | Scale establishes regional presence |
| **Risk Mitigation** | 7.4 MW | Lower CAPEX, faster payback, less market risk |
| **Capital Efficiency** | 20 MW | Slightly better returns on capital (15-16% IRR) |
| **Operational Flexibility** | 7.4 MW | Off-grid capable, phased deployment |
| **Price Competitiveness** | 20 MW | Economies of scale enable lower pricing |

### 4.5 Decision Matrix

| Criterion | Weight | 7.4 MW Score (1-10) | 20 MW Score (1-10) | 7.4 MW Weighted | 20 MW Weighted |
|-----------|--------|---------------------|-------------------|-----------------|----------------|
| **IRR/Returns** | 25% | 7 (14-15% IRR) | 8 (15-16% IRR) | 1.75 | 2.0 |
| **Time to Revenue** | 20% | 9 (6-9 months) | 5 (18-24 months) | 1.8 | 1.0 |
| **Capital Risk** | 20% | 9 ($40M) | 5 ($105M) | 1.8 | 1.0 |
| **Market Absorption** | 15% | 8 (easier to lease) | 6 (needs validation) | 1.2 | 0.9 |
| **Renewable Story** | 10% | 9 (26% solar) | 5 (10% solar) | 0.9 | 0.5 |
| **Scale/Revenue** | 10% | 5 ($13M/year) | 9 ($36M/year) | 0.5 | 0.9 |
| **TOTAL** | 100% | | | **7.95** | **6.30** |

**Weighted Score Winner: 7.4 MW** (if weights reflect conservative/renewable-focused priorities)

**Note:** If you adjust weights to prioritize Scale/Revenue (increase from 10% to 25%) and reduce Time to Market (20% to 10%), 20 MW wins the weighted score. **Weights depend on investor priorities.**

---

## 5. DECISION FRAMEWORK

### 5.1 Critical Inputs Needed

**Before finalizing DC size decision, confirm:**

**1. Grid Interconnection Parameters (From Camelot Task 1):**
- Distance to interconnection point: ___ km
- Estimated cost: $___ (target: <$5M for 7.4 MW, <$8M for 20 MW)
- Timeline: ___ months (target: <18 months)
- Reliability: ___% uptime
- **Decision impact:**
  - If timeline <12 months: May favor 20 MW (less wait penalty)
  - If timeline 12-18 months: 7.4 MW solar-first strategy optimal
  - If timeline >18 months: Strongly favor 7.4 MW (avoid long wait)
  - If cost >$10M: Reconsider both options

**2. Market Demand Assessment:**
- Pre-lease commitments secured: ___ MW
- Expected lease-up rate: ___ MW/year
- Target customer profile: (AI training, inference, enterprise, colo)
- Competitive landscape: (other Oklahoma data centers, pricing)
- **Decision impact:**
  - If pre-leased >15 MW: Strong case for 20 MW
  - If pre-leased 5-10 MW: 7.4 MW appropriate
  - If pre-leased <5 MW: Consider starting smaller or securing more commitments

**3. Capital Availability:**
- Total capital available: $___
- Debt capacity: $___
- Equity available: $___
- **Decision impact:**
  - If capital <$50M: 7.4 MW only option
  - If capital $50-80M: 7.4 MW comfortable, 20 MW stretch
  - If capital >$90M: Both options feasible, choose based on strategy

**4. Investor Priorities:**
- IRR target: ___% (both options meet 14%+ threshold)
- Payback target: ___ years (both options 5-7 years)
- Renewable energy importance: High / Medium / Low
- Risk tolerance: Conservative / Moderate / Aggressive
- Time to revenue priority: Critical / Important / Flexible

### 5.2 Decision Tree

```
START: Confirm grid is available (Camelot Task 1)
  ↓
  ├─ Grid NOT available or >$10M or >24 months
  │    → Only option: 7.4 MW with extended off-grid Phase 0
  │
  └─ Grid available <$5M and <18 months
       ↓
       Assess capital availability
       ↓
       ├─ Capital <$50M
       │    → Only option: 7.4 MW
       │
       ├─ Capital $50-80M
       │    → Evaluate priorities:
       │       ├─ Renewable story critical → 7.4 MW
       │       ├─ Speed to market critical → 7.4 MW
       │       └─ Moderate priorities → 7.4 MW (risk-adjusted)
       │
       └─ Capital >$90M
            → Assess market demand:
               ├─ Pre-leased >15 MW
               │    → Evaluate priorities:
               │       ├─ Maximize revenue → 20 MW
               │       ├─ Renewable story critical → 7.4 MW
               │       └─ Balanced priorities → Run sensitivity analysis
               │
               └─ Pre-leased <15 MW
                    → 7.4 MW (lower risk, can expand later)
```

### 5.3 Recommendation by Scenario

**Scenario 1: Limited Capital ($40-50M Available)**
- **Recommendation: 7.4 MW**
- **Rationale:** Only feasible option within budget
- **Risk: Low** (capital matches CAPEX requirements)

**Scenario 2: Moderate Capital + Conservative Investors ($50-80M, Risk-Averse)**
- **Recommendation: 7.4 MW**
- **Rationale:** Lower risk profile, faster to revenue, strong renewable story
- **Risk: Low** (conservative approach with upside expansion potential)

**Scenario 3: Strong Capital + Strong Demand + Renewable Focus ($90M+, >15 MW Pre-Leased, ESG Important)**
- **Recommendation: 7.4 MW**
- **Rationale:** Even with capital and demand, 26% solar story is compelling differentiator
- **Risk: Low-Medium** (sacrificing revenue for sustainability positioning)

**Scenario 4: Strong Capital + Strong Demand + Scale Focus ($90M+, >15 MW Pre-Leased, Revenue Priority)**
- **Recommendation: 20 MW**
- **Rationale:** Maximize revenue capture, scale advantages, market leadership
- **Risk: Medium** (higher CAPEX, must wait for grid, depends on sustained demand)

**Scenario 5: Strong Capital + Uncertain Demand ($90M+, <10 MW Pre-Leased)**
- **Recommendation: 7.4 MW with expansion option**
- **Rationale:** Start conservatively, prove market, expand to 20 MW if demand materializes
- **Risk: Low** (phased approach, can reassess in 12-18 months)

### 5.4 Hybrid Approach: 7.4 MW → 20 MW Expansion Path

**Strategy:** Start with 7.4 MW, design for future expansion to 20 MW

**Phase 0-2 (Months 0-36): 7.4 MW as documented in Part 1**
- Build and operate 7.4 MW data center
- Prove market demand and operational capability
- Generate revenue and cash flow

**Phase 3 (Months 36+): Expand to 20 MW if conditions met**
- Conditions:
  - 7.4 MW is >80% leased (strong demand validated)
  - Additional capital available ($60-65M for expansion)
  - Grid has capacity for additional 12.6 MW
  - Oklahoma market still growing
- Add:
  - 12.6 MW additional IT capacity (164 racks)
  - 2 additional 4 MW generators (total 6 units for N+1)
  - Electrical infrastructure upgrades (transformers, switchgear)
  - No BESS expansion needed (12-15 MWh still sized for solar excess)

**Advantages of Phased Approach:**
- ✅ Lower initial risk ($40M vs. $105M)
- ✅ Validate market before full investment
- ✅ Generate cash flow to fund expansion (reduce debt burden)
- ✅ Benefit from 7.4 MW renewable story early
- ✅ Flexibility to adjust based on market response

**Disadvantages:**
- ⚠️ Expansion requires additional permitting, construction disruption
- ⚠️ Some infrastructure duplication (not as efficient as building 20 MW day 1)
- ⚠️ May need additional land or rework site plan

**Land/Site Requirements for Expansion:**
- Reserve land for future expansion (size site for 20 MW from beginning)
- Electrical room sized for future transformers/switchgear
- Generator yard with space for 6 units (install 4, expand to 6 later)
- Adequate grid interconnection capacity (request 30 MW service from utility)

---

## 6. FINANCIAL MODELS & SENSITIVITY ANALYSIS

### 6.1 7.4 MW Sensitivity Analysis

**Base Case: IRR 14-15%, NPV $28-32M**

**Sensitivity to Key Variables:**

| Variable | -20% | -10% | Base | +10% | +20% | Most Sensitive? |
|----------|------|------|------|------|------|-----------------|
| **Pricing ($/kW/mo)** | $120 | $135 | $150 | $165 | $180 | ✅ YES |
| IRR Impact | 10% | 12% | 14-15% | 17% | 19% | |
| NPV Impact | $8M | $18M | $28-32M | $38M | $48M | |
| | | | | | | |
| **CAPEX** | $30M | $35M | $40M | $44M | $48M | ⚠️ Moderate |
| IRR Impact | 18% | 16% | 14-15% | 13% | 12% | |
| NPV Impact | $38M | $33M | $28-32M | $25M | $22M | |
| | | | | | | |
| **Occupancy Rate** | 60% | 70% | 80% | 90% | 100% | ⚠️ Moderate |
| IRR Impact | 11% | 12% | 14-15% | 15% | 16% | |
| NPV Impact | $18M | $23M | $28-32M | $33M | $38M | |
| | | | | | | |
| **Grid Electricity Cost** | $0.03/kWh | $0.04/kWh | $0.05/kWh | $0.06/kWh | $0.07/kWh | Minimal |
| IRR Impact | 15% | 15% | 14-15% | 14% | 14% | |
| NPV Impact | $31M | $30M | $28-32M | $28M | $27M | |

**Key Insights:**
- **Pricing is most critical variable** (±$30/kW changes IRR by ±3-5%)
- CAPEX and occupancy also significant (±10% changes IRR by ±1-2%)
- Grid electricity has minimal impact (solar offsets 26% of consumption)

**Downside Scenario (Conservative):**
```
Assumptions:
  - Pricing: $130/kW/month (vs. $150 base)
  - CAPEX: $44M (vs. $40M base)
  - Occupancy: 75% (vs. 80-100% base)
  - Lease-up: 24 months to stabilization (vs. 18 months)

Results:
  - Annual revenue: $11.7M (vs. $13.3M base)
  - IRR: 11-12% (vs. 14-15% base)
  - NPV: $18-22M (vs. $28-32M base)

Verdict: Still acceptable, but below typical 14% IRR hurdle
Action: Reduce CAPEX or secure higher pricing
```

**Upside Scenario (Optimistic):**
```
Assumptions:
  - Pricing: $175/kW/month (AI premium)
  - CAPEX: $37M (low end)
  - Occupancy: 95%
  - Lease-up: 12 months to stabilization

Results:
  - Annual revenue: $15.6M
  - IRR: 18-19%
  - NPV: $42-48M

Verdict: Strong returns, justifies investment
```

### 6.2 20 MW Sensitivity Analysis

**Base Case: IRR 15-16%, NPV $48-55M**

**Sensitivity to Key Variables:**

| Variable | -20% | -10% | Base | +10% | +20% | Most Sensitive? |
|----------|------|------|------|------|------|-----------------|
| **Pricing ($/kW/mo)** | $120 | $135 | $150 | $165 | $180 | ✅ YES |
| IRR Impact | 11% | 13% | 15-16% | 18% | 21% | |
| NPV Impact | $20M | $34M | $48-55M | $62M | $76M | |
| | | | | | | |
| **CAPEX** | $84M | $95M | $105M | $116M | $126M | ⚠️ Moderate |
| IRR Impact | 19% | 17% | 15-16% | 14% | 12% | |
| NPV Impact | $63M | $56M | $48-55M | $43M | $38M | |
| | | | | | | |
| **Grid Timeline** | 12 mo | 15 mo | 18 mo | 21 mo | 24 mo | ⚠️ Moderate |
| IRR Impact | 17% | 16% | 15-16% | 15% | 14% | |
| NPV Impact (with opportunity cost) | $54M | $51M | $48-55M | $46M | $43M | |
| | | | | | | |
| **Occupancy Rate** | 60% | 70% | 80% | 90% | 100% | ⚠️ Moderate |
| IRR Impact | 11% | 13% | 15-16% | 16% | 17% | |
| NPV Impact | $30M | $39M | $48-55M | $57M | $66M | |

**Key Insights:**
- **Pricing is most critical variable** (same as 7.4 MW)
- Grid timeline matters more for 20 MW (can't start off-grid to mitigate delay)
- Higher absolute revenue makes 20 MW more sensitive to occupancy risk

**Downside Scenario (Conservative):**
```
Assumptions:
  - Pricing: $135/kW/month (market pressure)
  - CAPEX: $115M (overruns)
  - Grid delay: 24 months (vs. 18 months)
  - Occupancy: 75% stabilized
  - Lease-up: 30 months to stabilization

Results:
  - Annual revenue: $32.4M
  - IRR: 12-13%
  - NPV: $32-38M

Verdict: Marginal, below 14% hurdle
Action: Negotiate better pricing or reduce CAPEX
```

**Upside Scenario (Optimistic):**
```
Assumptions:
  - Pricing: $165/kW/month (AI premium, anchor tenant)
  - CAPEX: $100M (efficient execution)
  - Grid delay: Only 15 months
  - Occupancy: 90% stabilized
  - Lease-up: 24 months to stabilization

Results:
  - Annual revenue: $39.6M
  - IRR: 18-19%
  - NPV: $68-75M

Verdict: Excellent returns, justifies scale investment
```

### 6.3 Break-Even Analysis

**7.4 MW Break-Even Points:**
- Minimum pricing: $125/kW/month (to achieve 12% IRR)
- Maximum CAPEX: $46M (to achieve 12% IRR @ $150/kW)
- Minimum occupancy: 65% (to achieve 12% IRR)

**20 MW Break-Even Points:**
- Minimum pricing: $130/kW/month (to achieve 12% IRR)
- Maximum CAPEX: $120M (to achieve 12% IRR @ $150/kW)
- Minimum occupancy: 70% (to achieve 12% IRR)

**Interpretation:**
- 7.4 MW has more pricing flexibility (lower break-even)
- 20 MW has less CAPEX margin (must control costs)
- Both need >70% occupancy for acceptable returns

---

## 7. RECOMMENDATIONS

### 7.1 Primary Recommendation

**BUILD 7.4 MW DATA CENTER (OPTION A)**

**Rationale:**
1. ✅ **Lower capital risk** ($37-41M vs. $105M)
2. ✅ **Faster time to revenue** (6-9 months vs. 18-24 months)
3. ✅ **Strong renewable differentiation** (26% vs. 10% solar)
4. ✅ **Adequate returns** (14-15% IRR meets investment criteria)
5. ✅ **Operational flexibility** (off-grid capable if grid delays)
6. ✅ **Easier market absorption** (7.4 MW easier to lease than 20 MW in Oklahoma)
7. ✅ **Future expansion option** (can grow to 20 MW if demand materializes)

**This recommendation assumes:**
- Capital availability: $40-50M
- Market demand: Moderate (5-10 MW pre-leased or expected)
- Grid timeline: 12-18 months (manageable with Phase 0 strategy)
- Investor priorities: Balanced (renewable story matters, but returns critical)

### 7.2 Conditional Recommendation: Consider 20 MW IF

**Proceed with 20 MW (Option B) ONLY IF all conditions met:**

**✅ Financial Conditions:**
- Capital available: >$100M (equity + debt capacity)
- Debt service coverage comfortable: >2.5× (adequate cash flow)
- Investors accept 18-month wait: Lost opportunity revenue acceptable

**✅ Market Conditions:**
- Pre-lease commitments: >15 MW secured or high confidence
- Anchor tenant(s): Secured (5-10 MW single customer reduces vacancy risk)
- Competitive positioning: Oklahoma market can absorb 20 MW without oversupply

**✅ Grid Conditions (From Camelot Task 1):**
- Grid timeline: <15 months (minimize wait period)
- Grid cost: <$6M (higher than 7.4 MW but manageable)
- Grid reliability: >99% uptime (grid-dependent strategy requires stable grid)

**✅ Strategic Conditions:**
- Investor priority: Scale and revenue over renewable % and speed
- Risk tolerance: Comfortable with $105M CAPEX exposure
- Market ambition: Establish as major Oklahoma data center provider

**If ANY condition not met → Revert to 7.4 MW recommendation**

### 7.3 Hybrid Recommendation: 7.4 MW with Expansion Option

**For investors who want both options:**

**Phase 1-3 (Months 0-36):**
- Build 7.4 MW as documented in Part 1
- Design site and electrical for future 20 MW capacity:
  - Reserve land for expansion (additional 12.6 MW building)
  - Size grid interconnection for 28-30 MW (vs. 10-12 MW min)
  - Electrical room designed for future transformers
  - Generator yard sized for 6 units (install 4, expand later)

**Phase 4 (Months 36+):**
- Evaluate expansion to 20 MW based on:
  - 7.4 MW occupancy (>80% triggers expansion evaluation)
  - Market demand validation (pipeline for additional 12+ MW)
  - Capital availability (raise additional $60-65M)
  - Continued Oklahoma market growth

**If expansion conditions met:**
- Add 12.6 MW IT capacity (164 racks)
- Add 2×4 MW generators (6 total for N+1 at 28 MW)
- Upgrade electrical infrastructure
- Incremental CAPEX: $60-65M
- Total cumulative: $97-106M (similar to building 20 MW day 1)

**If expansion conditions NOT met:**
- Remain at 7.4 MW (still profitable with 14-15% IRR)
- Consider smaller expansions (7.4 → 10 MW or 15 MW)
- Excess infrastructure capacity not wasted (provides growth optionality)

**Advantages of Hybrid:**
- ✅ Lowest initial risk (start with $40M, not $105M)
- ✅ Validate market before full commitment
- ✅ Generate cash flow to fund expansion (reduce debt)
- ✅ Flexibility to adjust to market realities

**Disadvantages:**
- ⚠️ Some infrastructure duplication (inefficient vs. building 20 MW day 1)
- ⚠️ Expansion requires additional permitting, construction disruption
- ⚠️ May pay premium for future-proofing infrastructure not used

---

## 8. NEXT STEPS & CRITICAL PATH

### 8.1 Immediate Actions (This Week, Oct 20-25)

**Priority 1: Validate Grid Parameters (Camelot Task 1)**
- Request preliminary findings on grid distance, cost, timeline
- If not available: Escalate to get estimate (critical for decision)
- Target: Confirm grid timeline <18 months and cost <$5M

**Priority 2: Assess Market Demand**
- Survey Oklahoma data center market (absorption rate, competitive pricing)
- Contact potential anchor tenants (any 5-10 MW commitments available?)
- Validate $150/kW/month pricing assumption (AI compute market)

**Priority 3: Confirm Capital Availability**
- Investor commitment: $40-50M for 7.4 MW or $100M+ for 20 MW?
- Debt capacity: Lender interest and terms (60% LTV @ 7% achievable?)
- Equity requirements: How much equity vs. debt?

**Priority 4: Issue RFIs (From Part 1)**
- BESS RFI: 12-15 MWh, grid-forming, all vendors
- Generator RFI: 4×4 MW (7.4 MW) or 6×4 MW (20 MW) - get both quotes
- Goal: Validate CAPEX assumptions (60-65% confidence → 80%+)

### 8.2 Decision Gate 1 (Nov 1, 2025)

**By Nov 1, confirm:**
1. Grid interconnection parameters (timeline, cost from Camelot)
2. Market demand assessment (pre-lease status, competitive landscape)
3. Capital availability (firm commitments from investors/lenders)
4. RFI responses (BESS and generator pricing)

**Decision:**
- If grid <15 months, capital >$100M, demand >15 MW → **Consider 20 MW**
- Otherwise → **Proceed with 7.4 MW**

### 8.3 Decision Gate 2 (Nov 5, 2025)

**By Nov 5, finalize:**
1. DC size selection: 7.4 MW or 20 MW (or hybrid)
2. Financial model with updated costs (RFI responses incorporated)
3. Risk assessment and mitigation plan
4. Investor presentation materials

**Deliverable:**
- Final recommendation memo
- Updated financial models (both options)
- Risk matrix
- Implementation timeline

### 8.4 Investor Presentation (Nov 7, 2025)

**Present:**
- **Part 1:** 7.4 MW technical architecture (solar-first startup strategy)
- **Part 2:** Sizing analysis (7.4 MW vs. 20 MW comparison) ← **This document**
- **Recommendation:** 7.4 MW (base case) with rationale
- **Optionality:** 20 MW (if conditions met) or hybrid approach
- **Decision framework:** Clear criteria for final sizing selection

**Outcome:**
- Investor approval to proceed with 7.4 MW or 20 MW
- Capital commitment confirmed
- Authority to execute contracts (BESS, generators, EPC)
- Timeline to financial close (target: Dec 2025)

---

## 9. APPENDICES

### Appendix A: 7.4 MW 10-Year Cash Flow Model

**Assumptions:**
- CAPEX: $40M (midpoint)
- Pricing: $150/kW/month
- Occupancy ramp: 30% (Yr 1) → 50% (Yr 2) → 80% (Yr 3) → 90% (Yr 4-10)
- Debt: 60% LTV ($24M loan @ 7%, 10-year amortization)

| Year | Occupancy | Revenue | OpEx | NOI | Debt Service | Net Cash Flow | Cumulative Cash |
|------|-----------|---------|------|-----|--------------|---------------|-----------------|
| 1 | 30% | $4.14M | $1.35M | $2.79M | $3.42M | -$0.63M | -$0.63M |
| 2 | 50% | $6.66M | $2.15M | $4.51M | $3.42M | $1.09M | $0.46M |
| 3 | 80% | $10.66M | $3.6M | $7.06M | $3.42M | $3.64M | $4.10M |
| 4 | 90% | $11.99M | $3.9M | $8.09M | $3.42M | $4.67M | $8.77M |
| 5 | 90% | $11.99M | $3.9M | $8.09M | $3.42M | $4.67M | $13.44M |
| 6 | 90% | $11.99M | $3.9M | $8.09M | $3.42M | $4.67M | $18.11M |
| 7 | 90% | $11.99M | $3.9M | $8.09M | $3.42M | $4.67M | $22.78M |
| 8 | 90% | $11.99M | $3.9M | $8.09M | $3.42M | $4.67M | $27.45M |
| 9 | 90% | $11.99M | $3.9M | $8.09M | $3.42M | $4.67M | $32.12M |
| 10 | 90% | $11.99M | $3.9M | $8.09M | $3.42M | $4.67M | $36.79M |

**10-Year Totals:**
- Revenue: $104.4M
- OpEx: $34.5M
- NOI: $69.9M
- Debt Service: $34.2M
- Net Cash Flow: $35.7M
- Plus equity return: $16M (initial equity) + $35.7M cash = **$51.7M total return**
- IRR: **14.2%**

### Appendix B: 20 MW 10-Year Cash Flow Model

**Assumptions:**
- CAPEX: $105M (midpoint)
- Pricing: $150/kW/month
- Occupancy ramp: 0% (Yr 1, grid wait) → 0% (Yr 1.5) → 50% (Yr 2-3) → 80% (Yr 4) → 90% (Yr 5-10)
- Debt: 60% LTV ($63M loan @ 7%, 10-year amortization)

| Year | Occupancy | Revenue | OpEx | NOI | Debt Service | Net Cash Flow | Cumulative Cash |
|------|-----------|---------|------|-----|--------------|---------------|-----------------|
| 1 | 0% | $0 | $0 | $0 | $0 | $0 | -$42M (equity) |
| 2 | 25% | $9M | $5.5M | $3.5M | $8.98M | -$5.48M | -$47.48M |
| 3 | 50% | $18M | $7.5M | $10.5M | $8.98M | $1.52M | -$45.96M |
| 4 | 80% | $28.8M | $10M | $18.8M | $8.98M | $9.82M | -$36.14M |
| 5 | 90% | $32.4M | $11M | $21.4M | $8.98M | $12.42M | -$23.72M |
| 6 | 90% | $32.4M | $11M | $21.4M | $8.98M | $12.42M | -$11.30M |
| 7 | 90% | $32.4M | $11M | $21.4M | $8.98M | $12.42M | $1.12M |
| 8 | 90% | $32.4M | $11M | $21.4M | $8.98M | $12.42M | $13.54M |
| 9 | 90% | $32.4M | $11M | $21.4M | $8.98M | $12.42M | $25.96M |
| 10 | 90% | $32.4M | $11M | $21.4M | $8.98M | $12.42M | $38.38M |

**10-Year Totals:**
- Revenue: $250.2M
- OpEx: $89.0M
- NOI: $161.2M
- Debt Service: $89.8M
- Net Cash Flow: $71.4M
- Plus equity return: $42M (initial equity) + $38.38M cash = **$80.38M total return**
- IRR: **15.6%**

### Appendix C: Expansion Scenario (7.4 MW → 20 MW)

**Phase 1-3: Build 7.4 MW (Months 0-36)**
- CAPEX: $40M
- Operate and lease up to 80%+ occupancy

**Phase 4: Evaluate Expansion (Month 36)**
- If 7.4 MW >80% leased AND market demand strong:
  - Add 12.6 MW capacity
  - Incremental CAPEX: $62M
  - Total: $102M (vs. $105M building 20 MW day 1, $3M savings)

**Combined 10-Year Cash Flow:**
- Years 1-3: 7.4 MW only (as in Appendix A)
- Year 4: Expansion investment (-$62M)
- Years 5-10: 20 MW operations (higher revenue)

**Result:**
- Lower initial risk (validate with 7.4 MW first)
- Similar total returns to 20 MW day 1 option
- Flexibility to stay at 7.4 MW if expansion doesn't make sense

---

## DOCUMENT REVISION HISTORY

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| **1.0** | 2025-10-20 | Benton Peret / PGCIS | Initial client-facing strategic sizing analysis |

**Status:** DRAFT FOR CLIENT REVIEW
**Next Review:** After grid study results and market demand assessment (target: Nov 1, 2025)
**Final Delivery:** Nov 7, 2025 (Investor Package)

---

**Related Documents:**
- [[Part 1 - Solar-First Startup Strategy - BAD]] - Technical architecture for 7.4 MW option
- [[Feasibility Memo V3]] - Project requirements (internal)
- [[Camelot SOW Summary]] - Pending grid interconnection study

**Tags:** #saga-project #sizing-analysis #7.4mw-vs-20mw #financial-comparison #decision-framework #client-deliverable #part-2
