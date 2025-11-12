**Created:** 2025-10-22 15:30

# Excess Solar Monetization Strategy
## Comparing Three Approaches for Phase 1-2 Solar Excess

**Saga Energy Pryor Data Center**

**Document Purpose:** Evaluate three distinct strategies for monetizing 7-8MW of excess solar capacity during Phase 1-2 buildout, comparing direct grid export, mobile edge computing, and battery energy storage based on risk-adjusted NPV and operational requirements.
****Assumes that grid power is available day 1

**Prepared By:** PACHYDERM GLOBAL / PGCIS
**Prepared For:** Saga Energy
**Date:** 2025-10-22
**Status:** DRAFT - REQUIRES ADDITIONAL RESEARCH

**Related Documents:**
- [[Why BESS Should Not Be UPS]] - Technical analysis of BESS-as-UPS failure modes

**Tags:** #saga-project #solar-monetization #mobile-edge #economic-bess #decision-framework

---
*We just assumed we needed a BESS, but as we started designing the land that would hold it, we took a minute to do an analysis on do we even need as BESS!*

## EXECUTIVE SUMMARY

### Why no BESS?
Financially, buying a BESS fails because of a fatal problem-solution mismatch:
- Fatal Flaw 1: The Short Window. We are trying to use a $10.8M long-term asset to solve a temporary 2-year revenue problem. As the math shows, that 2-year window _only_ provides $1.8M in present value. The project is financially underwater from day one.
- Fatal Flaw 2: Internal Competition. When the 2-year window closes, our BESS _tries_ to become a merchant asset. But, as Section 4.3.1 proves, its most valuable long-term revenue stream (Demand Response) is cannibalized by our own on-site generators.
### The Opportunity
Phase 1-2 deployment creates a temporary but significant revenue opportunity: 12MW solar array serving only 4-8.5MW facility load results in 7-8MW of excess capacity during peak solar hours.

As the facility scales, excess solar power diminishes or disappears entirely. The strategic question: **What is the highest-value use of this excess during the buildout window?**

### Three-Option Comparison

| Metric                     | Option A: Grid Export          | Option B: Mobile Edge                          | Option C: Economic BESS                               |
| -------------------------- | ------------------------------ | ---------------------------------------------- | ----------------------------------------------------- |
| **CAPEX**                  | $500k-1M                       | $150-300k (+ $0-5M interconnection)            | $10.8M                                                |
| **Phase 1-2 Revenue/Year** | $400-600k                      | $3-6M (lease) or $1-3M (rev share)             | $600k-1.4M (insufficient to recover CAPEX)            |
| **Phase 3-5 Revenue/Year** | $50-150k (minimal excess)      | $0 (vendor exits)                              | $700k/year (competed by generators)                   |
| **20-Year NPV @ 8%**       | **$0.8-1.5M**                  | **$4.7-7.5M (lease)** or **$3.3M (rev share)** | **-$5.3M to -$6.2M**  **(NEGATIVE - destroys value)** |
| **Capital Efficiency**     | 1-2× (NPV/CAPEX)               | **21-33× (lease)** or **15× (rev share)**      | **Negative (destroys value)**                         |
| **Revenue Volatility**     | Low                            | High (market-dependent)                        | N/A (not viable)                                      |
| **Operational Complexity** | Low                            | Medium-High                                    | High (moot - not recommended)                         |
| **Phase 3+ Transition**    | Seamless (just curtail export) | Vendor must exit site                          | **NOT VIABLE**                                        |

*Note: All NPV calculations use consistent 8% discount rate with year-by-year present value factors. Option B calculations corrected to reflect 24-month Phase 1-2 window (not 48 months).*

*Note on Option B Revenue: Phase 1 lease model assumes 6MW firm capacity × $65/kW/month × 12 months = $4.68M/year. This rate ($50-80/kW range) reflects market pricing from mobile compute vendors (Crusoe Energy, Lancium) who value solar-powered capacity for AI/mining workloads. Phase 2 drops to $2.34M/year as excess solar shrinks to 3MW.
- I forget the name of the vendor you all were considering for this, but seems like a good plan to avoid spending on BESS.

### Critical Unknowns (Research Required)

| Question                                                                                              | Impact                                                                                                                                                                                                                          | Timeline                              |
| ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| **Does interconnection agreement permit 6-8MW additional load (Option B) or 12MW export (Option A)?** | **CRITICAL - Must answer first.** If no, Option B requires 6-12 month utility study + potential $0-5M upgrade costs. Option A requires simpler export amendment (3-6 months). Delays revenue start, may kill Option B entirely. | **IMMEDIATE (Week 1 - call utility)** |
| **Are mobile compute vendors available/interested?**                                                  | **Likely yes** based on prior discussions. If terms are favorable ($50-80/kW lease rate), Option B delivers $8-15M NPV vs. $1.5-2.5M for Option A. BUT only pursue AFTER utility confirms interconnection feasibility.          | 2 weeks (RFI - AFTER utility OK)      |
| **Will lenders accept mobile compute revenue? (Or is project fully equity-funded?)**                  | If equity-funded, lender acceptance is moot—pursue highest NPV option (likely B). If debt-financed and lenders reject crypto/mining revenue, Option B becomes unavailable regardless of returns.                                | 4 weeks (lender discussion)           |


---

## 1. PROJECT CONTEXT & PHASED DEPLOYMENT

### 1.1 Five-Phase Buildout Strategy (good for modeling)

| Phase | IT Load | Facility Load (PUE 1.35-1.42) | Solar Excess Available   | Buildout Timeline |
| ----- | ------- | ----------------------------- | ------------------------ | ----------------- |
| **1** | 3MW     | 4.0-4.3MW                     | **7.7-8MW** (peak hours) | Months 0-12       |
| **2** | 6MW     | 8.0-8.5MW                     | **3.5-4MW** (peak hours) | Months 12-24      |
| **3** | 9MW     | 12.0-12.8MW                   | **0-0.8MW** (minimal)    | Months 24-36      |
| **4** | 12MW    | 16.0-17.0MW                   | **0MW** (net consumer)   | Months 36-48      |
| **5** | 20MW    | 27.0-28.4MW                   | **0MW** (net consumer)   | Months 48-60+     |

**Key Insight:** The monetization opportunity is **front-loaded** in Phase 1-2 (18-24 months), then largely disappears as facility load grows.

**Key Insight 2: BESS vs. Generators for Long-Term Demand Response**
With potential natural gas turbine generators onsite (5×4MW N+1), we have an alternative to BESS for demand response participation in Phase 3-5. In this case generators are more cost-effective (no $10.8M CAPEX required).

---

## 2. OPTION A: DIRECT GRID EXPORT (WHOLESALE)

### 2.1 Description
Export excess solar directly to the grid via SPP wholesale market, selling at day-ahead or real-time pricing.

**System Requirements:**
- Grid interconnection sized for 12MW export (may already be planned)
- Minimal metering/control upgrades
- SPP market participation agreement (or utility buyback contract)

**Operating Mode:**
- **Phase 1-2:** Export 3.5-7.7MW during peak solar hours (11am-4pm)
- **Phase 3+:** Export diminishes to zero as facility load grows
- **No storage:** Direct solar → grid (cannot time-shift energy)

### 2.2 Financial Model

**CAPEX:**
- Interconnection upgrades (if needed): $300-500k
- Metering/controls: $100-200k
- SPP market registration/software: $50-100k
- **Total: $500k-1M**


**20-Year NPV Calculation (Base Case):**

The **$0.8M Net NPV** is derived from a 20-year present value of revenue of $1.55M (dominated by Phase 1-2 exports) less $750k in CAPEX.

**NPV Range:**
- **Conservative** (no Phase 3+ revenue): **$124k** (marginal)
- **Base Case** (moderate ongoing export): **$0.8M**
- **Optimistic** (extended buildout, high SPP prices): **$1.5M**

### 2.3 Pros and Cons

**Advantages:**
- **Lowest CAPEX:** $500k-1M vs. $10.8M for BESS
- **Reasonable capital efficiency:** 1.1× NPV/CAPEX ratio
- **Low operational complexity:** Set-and-forget system
- **Lender acceptance:** Proven, conservative revenue stream
- **No degradation:** Unlike batteries, no capacity fade

**Disadvantages:**
- **Lowest NPV and revenue:** $400-600k/year Phase 1-2 vs. $3-6M for mobile compute
- **No demand charge reduction:** Cannot time-shift energy to reduce peak grid usage
- **Curtailment risk:** Grid may reject excess during low-demand periods
- **Limited long-term value:** Revenue drops to $50-150k/year after Phase 2
- **Wholesale price volatility:** Can be negative during high-wind periods in SPP

---

## 3. OPTION B: MOBILE EDGE COMPUTING (LEASE/REVENUE SHARE)

### 3.1 Description
Partner with mobile data center vendors (e.g., Crusoe Energy, Lancium, Applied Digital) to deploy shipping containers with GPUs/ASICs on-site. Vendor consumes excess solar for AI compute, cryptocurrency mining, or grid balancing workloads.

**Two Business Models:**

**Model B1: Capacity Lease**
- Vendor pays fixed $/kW/month for power capacity
- Vendor owns compute economics (profit/loss)
- Saga receives predictable revenue regardless of market conditions

**Model B2: Revenue Share**
- Vendor pays % of compute revenue (mining proceeds, AI inference fees)
- Saga participates in upside (crypto bull markets, AI demand spikes)
- Revenue highly volatile based on market conditions

**System Requirements:**
- 7-8MW power distribution to vendor containers (200-400 ft from substation)
- Vendor provides containers, compute hardware, internet connectivity
- Contract terms: 18-36 month initial term with exit provisions for Phase 3 expansion

### 3.2 Financial Model

#### Model B1: Capacity Lease (Lower Risk)

**CAPEX:**
- Power distribution to container pad: $100-200k (reduced from $200-400k due to existing generator yard infrastructure)
- Site prep (grading, fencing): $50-100k (leveraging existing yard space and security)
- **Total: $150-300k** (conservative estimate assuming connection points already available in gen yard)

**Revenue (Phase 1):**
- Leasable capacity: 7.7MW (peak excess) → Conservative: 6MW firm
- Lease rate: $50-80/kW/month (market range for solar-powered compute)
- **Annual revenue: 6,000 kW × $65/kW × 12 = $4.68M/year**

**Revenue (Phase 2):**
- Leasable capacity: 3.5MW → Conservative: 3MW firm
- **Annual revenue: 3,000 kW × $65/kW × 12 = $2.34M/year**

**Revenue (Phase 3+):**
- Vendor exits (no excess solar available)
- **Annual revenue: $0**

**20-Year NPV Calculation (Base Case):**

The **$6.12M Net NPV** is derived from a 2-year present value of revenue of $6.34M (from the 24-month Phase 1-2 window) less $225k in CAPEX.

**Sensitivity (Lease Rate Variation):**
- Low case ($50/kW): $6.12M × (50/65) = **$4.71M NPV**
- Base case ($65/kW): **$6.12M NPV**
- High case ($80/kW): $6.12M × (80/65) = **$7.53M NPV**

#### Model B2: Revenue Share (Higher Risk/Reward)

**CAPEX:** Same as B1 ($150-300k)

**Revenue (Phase 1-2):**
- Vendor share: 50-70% (vendor keeps majority to cover hardware/ops)
- Saga share: 30-50%
- **If** vendor generates $8M/year gross → Saga receives $2.4-4M/year
- **If** crypto bear market → Saga receives $400k-1M/year
- **Expected value:** $1.5-2.5M/year (high variance, market-dependent)

**20-Year NPV Calculation (Corrected @ 8% Discount Rate):**

**Expected Revenue Scenario (Midpoint):**
- Year 1 (Phase 1): $2.0M × 0.926 = $1.85M
- Year 2 (Phase 2): $2.0M × 0.857 = $1.71M

**Total Revenue NPV: $3.56M**
**Less CAPEX: -$225k**
**Net NPV: $3.34M** (with ±$1.5M variance based on crypto/AI market conditions)

**Note:** Previous calculation incorrectly assumed 4-year window. Corrected to 2-year Phase 1-2 opportunity.

### 3.3 Pros and Cons

**Advantages:**
- ✅ **Highest revenue potential:** $3-6M/year in Phase 1-2 (5-10× other options)
- **Minimal CAPEX:** $300-600k vs. $10.8M for BESS
- **Capital efficiency:** 15-30× NPV/CAPEX ratio
- **Fast deployment:** 3-6 months from contract to revenue (vs. 12-18 months for BESS)
- **No degradation risk:** Vendor replaces/maintains hardware
- **Flexible exit:** Vendor removes containers for Phase 3 expansion

**Disadvantages:**
- **Site conflicts:** Requires 8-12 high-density containers (40-ft modules, ~1 acre footprint) in generator yard—minimal spatial impact but must coordinate with Phase 3 construction timeline
- **Interconnection study required:** Adding 6-8MW load triggers utility study (6-12 month timeline, potential upgrade costs $0-2M+ unknown until study complete)
- **Lender skepticism:** Crypto/mining revenue may be unacceptable for project finance
- **Revenue volatility:** Model B2 highly dependent on crypto/AI market conditions
- **Vendor risk:** Bankruptcy, contract breach, operational failures
- **No long-term value:** Revenue ends when vendor exits (Phase 3)

### 3.4 Critical Risk: Utility Interconnection Study

**MAJOR MISSING ASSUMPTION:** The financial model assumes mobile compute can connect to the site with minimal delay. This is **unlikely to be true**.

**The Problem:**
- **Current interconnection agreement:** Designed for 12MW solar source + phased 20MW data center load
- **Mobile compute adds:** 6-8MW NEW load in Phase 1 (not part of original plan)
- **Utility perspective:** This changes load flow, fault currents, protection coordination across the network
- **Result:** Triggers mandatory interconnection study with OG&E/GRDA and SPP

**Interconnection Study Timeline:**
1. **Submit application:** Includes vendor specs, load profile, connection point
2. **Utility review:** 30-60 days to assign study scope
3. **System Impact Study:** 90-180 days to model new load on grid
4. **Facilities Study (if needed):** Additional 60-120 days if upgrades required
5. **Interconnection Agreement amendment:** 30-60 days negotiation

**Total Timeline: 6-12+ months** from application to permission to energize

**Potential Costs (Unknown Until Study Complete):**
- **Best case:** No upgrades required, study fees only ($10-50k)
- **Moderate case:** Transformer upgrade, relay coordination ($200-500k)
- **Worst case:** Substation upgrades, transmission line reinforcement ($1-5M+)
- **Critical:** These costs are **100% unknown** until utility completes study

**Impact on Financial Model:**
- **Revenue start date:** Month 6-12 (not Month 0-3 as assumed)
- **CAPEX:** $150-300k + $10k-5M (utility upgrades, wide range)
- **NPV sensitivity:** Each 6-month delay reduces NPV by ~$1.5M (lost revenue)

**What This Means:**
- **Action Item #1:** Contact utility IMMEDIATELY to confirm interconnection study requirements
- **Vendor RFI timing:** Cannot issue until utility confirms study scope and timeline
- **Contract structure:** Vendor must accept delayed interconnection (force majeure clause)

**Best Case Scenario:**
- Utility confirms existing IA already contemplated "behind-the-meter load flexibility"
- Study expedited (4-6 months), no material upgrades required ($50k study fees)
- **NPV impact:** -$500k to -$1M (6-month delay + study costs)

**Worst Case Scenario:**
- Utility requires full System Impact Study + Facilities Study (12-18 months)
- Identifies $2M+ in transformer/protection upgrades
- **Result:** Option B becomes uneconomic or infeasible (better to just do Option A or C)

### 3.5 Best Fit Scenarios

**Choose Option B if:**
1. Utility interconnection study confirms <$500k upgrade costs and <9-month timeline
2. Lenders accept lease revenue in DSCR calculations
3. Qualified vendors available (Crusoe, Lancium) at $50-80/kW rates
4. Site accommodates 8-12 containers without Phase 3 conflicts

**Do NOT pursue Option B if:**
- Interconnection study reveals >$1M upgrade costs (erodes NPV advantage)
- Study timeline >12 months (misses most of Phase 1-2 revenue window)
- Utility rejects interconnection modification outright

**Requires further diligence (BEFORE vendor RFI):**
1. **Utility interconnection study inquiry** (highest priority - Week 1)
2. Lender feedback on revenue acceptability
3. RFI to 3-5 mobile compute vendors (only AFTER utility confirms feasibility)

---


---

## 5. RISK-ADJUSTED COMPARISON

### 5.1 Financial Summary (Corrected NPV Calculations - All Options)

| Metric                | Option A: Export     | Option B: Mobile (Lease)                      | Option B: Mobile (Rev Share)            | Option C: BESS (w/ demand)    | Option C: BESS (no demand)    |
| --------------------- | -------------------- | --------------------------------------------- | --------------------------------------- | ----------------------------- | ----------------------------- |
| **CAPEX**             | $750k                | $225k (+ $0-5M interconnection unknown)       | $225k (+ $0-5M interconnection unknown) | $10.8M                        | $10.8M                        |
| **NPV**               | **$0.8M**            | **$6.12M** (base case)                        | **$3.34M**                              | **-$5.26M** ❌                 | **-$6.18M** ❌                 |
| **NPV/CAPEX**         | **1.1×**             | **27×** (base case)                           | **15×**                                 | **Negative (destroys value)** | **Negative (destroys value)** |
| **IRR**               | 25-35%               | **180%** (2-year window)                      | **110%**                                | **Negative**                  | **Negative**                  |
| **Payback**           | 2-3 years            | <1 year                                       | 1-2 years                               | **Never**                     | **Never**                     |
| **Revenue Duration**  | 20 years (declining) | 2 years (Phase 1-2 only)                      | 2 years (Phase 1-2 only)                | 20 years (insufficient)       | 20 years (insufficient)       |
| **Revenue Certainty** | High                 | High (lease)                                  | Low (market)                            | N/A (not viable)              | N/A (not viable)              |
| **Recommendation**    | Marginal fallback    | **BEST OPTION** (if interconnection succeeds) | MODERATE RISK/REWARD                    | ❌ **NOT VIABLE**              | ❌ **NOT VIABLE**              |


---

## 6. RECOMMENDATIONS BY SCENARIO

#### Scenario 1: Mobile Compute Interconnection Feasible
**RECOMMEND: Option B (Mobile Edge Lease Model)**

**Rationale:**
- Highest NPV by far: **$6.1M** (vs. $0.8M for export, -$5.3M for BESS)
- **7-8× better than Option A**
- Best capital efficiency: 27× NPV/CAPEX (vs. 1.1× for A)
- Fastest payback: <12 months
- Only option that captures full Phase 1-2 excess solar value

**Implementation:**
1. **Week 1:** Contact utility to confirm interconnection study requirements (**CRITICAL PATH**)
2. **Weeks 2-4:** Submit interconnection application, begin vendor RFI process
3. **Months 6-12:** Complete utility study, finalize vendor contract
4. **Months 12-24:** Mobile compute operational (if study successful)

**Success Criteria:**
- Utility interconnection study <$500k upgrade costs
- Study timeline <9 months (permits revenue start by Month 9-12)
- Vendor lease rate >$50/kW/month
- Lenders accept lease revenue in DSCR calculations

**Note:** NPV corrected from $12.2M to $6.1M to reflect accurate 24-month Phase 1-2 window. Recommendation unchanged - Option B remains clearly superior.

---

#### Scenario 2: Mobile Compute Interconnection Fails
**RECOMMEND: Option A (Direct Grid Export)**

**Rationale:**
- **Only remaining viable option** with positive NPV (**$0.8M**)
- BESS NPV is **deeply negative** (-$5.3M to -$6.2M) - not a viable alternative
- Low operational complexity, proven revenue model
- Only positive-NPV option when mobile compute unavailable (1.1× NPV/CAPEX vs. BESS negative)
- Conservative, lender-friendly approach

**Implementation:**
- Complete interconnection upgrades for export (Months 0-6)
- Register for SPP wholesale market participation
- Begin exports when Phase 1 operational (Month 12+)
- Revenue $400-600k/year for Phase 1-2, declining in Phase 3+

**When This Applies:**
- Utility interconnection study reveals >$1M upgrade costs for mobile compute
- Study timeline >12 months (misses Phase 1-2 window)
- No qualified mobile compute vendors available
- Lenders reject mobile compute revenue

**Important Note:** Option A delivers marginal returns ($0.8M NPV). If interconnection fails, consider whether excess solar monetization complexity is justified for <$1M value creation. May be simpler to curtail excess and focus resources elsewhere.

**NPV Sensitivity:**
- Conservative case (no Phase 3+ revenue): **$124k** (barely positive)
- Base case (moderate Phase 3+ export): **$0.8M**
- Optimistic case (extended buildout, high SPP prices): **$1.5M**

---

#### What About BESS (Option C)?

**NOT RECOMMENDED under any scenario.**

**Why BESS Fails:**
1. **Negative NPV:** -$5.26M (with demand charges) or -$6.18M (without) over 20 years
2. **Cannot recover CAPEX:** $10.8M investment + $1.6M battery replacement exceeds all revenue
3. **Short value window:** Phase 1-2 lasts only 2 years (~$1.8M PV), insufficient for $10.8M CAPEX
4. **Generator competition:** Eliminates $3.1M of Phase 3-20 revenue value
5. **Poor capital allocation:** Every dollar spent on BESS is better spent on Option A or saved

**Do NOT pursue BESS regardless of:**
- Demand charge availability
- SPP grid services market rates
- Lender appetite
- Phase 3+ strategic considerations

**Honest Assessment:** The corrected financial analysis shows BESS destroys shareholder value in this application. The 2-year Phase 1-2 window is too short to justify $10.8M CAPEX, and Phase 3-20 revenue is competed by generators and insufficient to close the gap.

---



---
# Appendix

### 3.4 OPTION B: MOBILE EDGE COMPUTING Risk Mitigation Strategies

**Lender Acceptance:**
- Structure as **non-recourse revenue** (excluded from debt service coverage)
- Use lease model (B1) instead of revenue share (B2) for predictability
- Provide vendor financials and market references (Crusoe has raised $500M+, works with major utilities)

**Vendor Risk:**
- Performance bond or LOC equal to 6 months lease payments
- Monthly payment terms (not quarterly/annual)
- Right to replace vendor with 90-day notice

**Site Conflicts:**
- Master plan showing container locations do NOT interfere with Phase 3-4 infrastructure
- Contract provisions for phased removal (50% containers exit by Month 18, 100% by Month 30)

**Revenue Volatility (Model B2 only):**
- Minimum revenue floor in contract ($50/kW or 30% of historical average)
- Quarterly true-up to ensure downside protection

---

## 4. OPTION C: ECONOMIC BESS (STORAGE + GRID SERVICES)

### 4.1 Description
Deploy a 16 MWh battery energy storage system (BESS) that operates **independently from critical power infrastructure**.

**Timeline Alignment:** BESS has 12-18 month lead time from order to commissioning. If ordered at project start (Month 0), system becomes operational Month 12-18 — **aligning with Phase 1 facility commissioning**. The facility itself requires 12-18 months construction before generating solar excess.

**Phase-Adaptive Revenue Strategy:**

**Phase 1 (Months 12-24):**
- **Daytime:** Charge BESS from solar excess (7-8MW for 2-5 hours)
- **Evening:** Discharge BESS to facility (4-8pm peak demand window)
- **Value:** Avoid grid purchases during peak pricing OR reduce demand charges

**Phase 2 (Months 24-36):**
- **Daytime:** Charge BESS from solar excess (3-4MW for 2-3 hours)
- **Evening:** Discharge BESS to facility during peak hours
- **Value:** Peak shaving + demand charge reduction (if applicable)

**Phase 3-5 (No Excess Solar):**
- **Pivot to grid services:** SPP frequency regulation, demand response, energy arbitrage
- **Not constrained by UPS duty:** Can discharge to 0% SOC for maximum revenue
- **Maintained by 2N UPS:** Facility reliability independent of BESS availability

### 4.2 Financial Model

**CAPEX:**
- Batteries (16 MWh LFP): $5.2M ($325/kWh, declining trend)
- Inverters (4×4MW grid-following): $2.4M ($150/kW)
- Controls/BMS: $800k
- Fire safety (NFPA 855): $400k
- Integration/switchgear: $1.0M
- **Phase 1 Total: $9.8M**
- **Phase 2-5 Additions (inverters): +$1M** (Optional: Add inverters to increase discharge rate for grid services. Phase 1-2 solar charging only needs 2×4MW = 8MW. Phase 3-5 grid services benefit from full 16MW discharge capability for regulation/DR markets. Can defer this $1M if Phase 3+ revenue doesn't materialize.)
- **Total CAPEX: $9.8M (Phase 1-2 only) or $10.8M (if adding Phase 3+ grid services capability)**

**Revenue Model (Two Scenarios):**

#### Scenario C1: With Demand Charges (BEST CASE)

**Phase 1 Revenue:**
- **Solar arbitrage:** 16 MWh/day × 350 days × $0.08/kWh net value = $448k/year
- **Demand charge reduction:** 4MW peak shaving × $15/kW × 12 months = $720k/year
- **Total: $1.17M/year**

**Phase 2 Revenue:**
- **Solar arbitrage:** 12 MWh/day × 350 days × $0.08/kWh = $336k/year
- **Demand charge reduction:** 3MW peak shaving × $15/kW × 12 months = $540k/year
- **Total: $876k/year**

**Phase 3-5 Revenue:**
- **SPP regulation:** 16MW × 4 hours/day × 350 days × $7/MW = $157k/year
- **Demand response:** 60 events/year × 16MW × 2 hours × $200/MWh = $384k/year
- **Energy arbitrage:** 16 MWh × 250 days × $0.08/kWh spread = $320k/year
- **Capacity credit:** 16MW × $15/kW/year = $240k/year
- **Total: $1.1M/year**

**20-Year NPV Calculation (Corrected with Proper Discount Factors @ 8%):**

**Present Value Factors:**
- Year 1: 1/(1.08)^1 = 0.926
- Year 2: 1/(1.08)^2 = 0.857
- Years 3-12 annuity factor: 5.753 (10-year annuity discounted to Year 0)
- Year 12 (battery replacement): 0.397
- Years 13-20 annuity factor: 2.282 (8-year annuity discounted to Year 0)

**Revenue Present Value:**
- Year 1: $1.17M × 0.926 = $1.083M
- Year 2: $876k × 0.857 = $0.751M
- Years 3-12: $1.1M × 5.753 = $6.328M
- Battery replacement (Year 12): -$4M × 0.397 = -$1.588M
- Years 13-20: $900k × 2.282 = $2.054M

**Total Revenue NPV: $1.083M + $0.751M + $6.328M - $1.588M + $2.054M = $8.628M**

**Less CAPEX: -$10.8M**

**Net NPV (before generator competition adjustment): -$2.17M (NEGATIVE)**

**Generator Competition Impact:**
As noted in Section 4.3.1, generators can provide demand response at $0 incremental CAPEX, eliminating $384k/year of BESS revenue in Years 3-20.

- Lost demand response revenue: $384k/year × 8.035 (Years 3-20 annuity factor) = -$3.09M

**Adjusted Net NPV: -$2.17M - $3.09M = -$5.26M (DEEPLY NEGATIVE)**

**CONCLUSION:** Even with demand charges, Option C destroys value. The $10.8M CAPEX cannot be justified by the limited Phase 1-2 revenue window (2 years, $1.8M PV) combined with generator-competed Phase 3-20 revenue. In the absence of demand charges (energy-only rates), the financial model is even worse, with a projected NPV of -$6.2M.
### 4.3 Critical Dependency: Demand Charges vs. Demand Response

**IMPORTANT DISTINCTION:** There are TWO types of "demand" programs with different economics:

**1. Demand Charges - PEAK SHAVING (Monthly Billing Component):**
- Utility charges $/kW/month based on your peak demand during billing period
- Example: $15/kW × 13.5MW peak = $202.5k/month = **$2.4M/year**
- BESS can reduce this by discharging during facility peak hours (4-8pm daily)
- **Value to BESS:** $360k-960k/year savings (by reducing peak by 3-4MW)
- **Status:** Unknown if OG&E commercial rates include this (needs research)

**2. Demand Response (Revenue Program):**
- Utility PAYS you $/kW/year to reduce load during grid peak events (6-10 events/year)
- Example: $25-35/kW/year × 6MW enrolled = **$150-210k/year** (per internal memo)
- Can use BESS OR generators to island during events
- **Value to BESS:** $150-300k/year (but generators can provide same value at lower cost)
- **Status:** Confirmed available from OG&E Load Reduction Program

**CORRECTED ANALYSIS:** Even with demand charges, BESS is not viable.

**With Demand Charges ($10-20/kW monthly):**
- BESS daily peak shaving provides $720k/year (Phase 1) + $540k/year (Phase 2)
- Combined with solar arbitrage: $1.17M/year Phase 1, $876k/year Phase 2
- **Corrected NPV: -$5.26M** (NEGATIVE - does NOT justify $10.8M CAPEX)

**Without Demand Charges (energy-only rates):**
- BESS limited to solar arbitrage ($400-600k/year Phase 1-2)
- **Corrected NPV: -$6.18M** (CATASTROPHICALLY NEGATIVE)

**ROOT CAUSE OF FAILURE:**
1. **High CAPEX burden:** $10.8M upfront + $1.6M battery replacement (Year 12) = $12.4M total
2. **Short high-value window:** Phase 1-2 lasts only 2 years (present value ~$1.8M)
3. **Generator competition:** Eliminates $3.1M of Phase 3-20 revenue (demand response)
4. **Long payback impossible:** Even best-case revenue can't recover costs over 20 years

**CONCLUSION:** Option C is NOT VIABLE regardless of demand charge availability. The corrected financial analysis shows BESS destroys value in all scenarios.

**ACTION REQUIRED (DOWNGRADED):** Demand charge research is now moot - BESS fails economically even with favorable rate structure.

### 4.3.1 Generator Competition for Phase 3-5 Revenue

**ADDITIONAL ISSUE:** Even if BESS were operational on time, Phase 3-5 grid services revenue faces competition from generators.

**The Problem:**
The data center will have 5×4MW N+1 natural gas turbine generators onsite (see Section 7.3). These generators can participate in OG&E demand response programs **at zero incremental CAPEX**:

**Generator Demand Response Capability:**
- **OG&E Load Reduction Program:** Pays $25-35/kW/year for 6-10 curtailment events/year
- **Available capacity:** 20MW (N+1 configuration = 4 active turbines during events)
- **Revenue potential:** 20,000 kW × $30/kW/year = $600k/year
- **CAPEX:** $0 (generators already required for Tier III compliance)
- **Operational cost:** $50-75k/year (fuel, maintenance during events)
- **Net revenue:** $525-550k/year

**BESS Demand Response Revenue (from Section 4.2):**
- OG&E demand response: $384k/year (16MW × $200/MWh × 60 events × 2 hrs)
- But this requires $10.8M CAPEX + operational complexity

**Impact on BESS Business Case:**
The claimed $1.1M/year Phase 3-5 BESS revenue includes:
- SPP regulation: $157k/year
- **Demand response: $384k/year** ← Generators can provide this at $0 CAPEX
- Energy arbitrage: $320k/year
- Capacity credit: $240k/year

**Adjusted BESS Unique Value (Phase 3-5):**
- Remove demand response (generators provide this): -$384k/year
- **Remaining BESS-specific revenue: $717k/year** (regulation + arbitrage + capacity)
- This is **35% lower** than claimed $1.1M/year

**NPV Impact (already incorporated in Section 4.2 calculations):**
- Generator demand response eliminates: $384k/year × 8.035 (Years 3-20) = **-$3.09M**
- This adjustment is **already included** in the corrected NPV calculation above
- Without generator competition, NPV would be -$2.17M (still negative)
- With generator competition, NPV is -$5.26M (deeply negative)

**Conclusion:**
Generator competition worsens an already-failing business case. Even without generator competition, BESS NPV would still be negative (-$2.17M). The fundamental problem is that $10.8M CAPEX cannot be recovered from 2 years of Phase 1-2 solar arbitrage revenue combined with limited Phase 3-20 grid services.

### 4.4 Pros and Cons

**Advantages:**
- **Long-term revenue potential:** BESS could theoretically generate $700k/year in Phase 3-5 (grid services less generator competition)
- **Operational flexibility:** Can pivot strategies as markets evolve (solar → arbitrage → regulation)
- **No vendor dependence:** Owned asset, not reliant on third-party performance

**Disadvantages:**
- ❌ **FATAL: Negative NPV in all scenarios:** -$5.26M (with demand charges) or -$6.18M (without)
- ❌ **Highest CAPEX:** $10.8M vs. $150-300k for Option B or $500k-1M for Option A
- ❌ **Catastrophic capital efficiency:** Destroys value in all scenarios
- ❌ **Short value window:** Phase 1-2 lasts only 2 years (~$1.8M PV), insufficient to recover $10.8M+ investment
- **Battery degradation:** 80% capacity at Year 12 → $4M replacement cost (adds to losses)
- **Operational complexity:** High (battery management, market participation, maintenance)
- **Generator competition:** Eliminates $3.1M of Phase 3-20 revenue (35% of total value proposition)
- **No path to profitability:** Even optimistic assumptions show negative returns over 20 years

**RECOMMENDATION: DO NOT PURSUE Option C under any circumstances.** The corrected financial analysis shows BESS cannot recover its CAPEX from the limited Phase 1-2 revenue opportunity, even with favorable demand charge rates and optimistic Phase 3-5 grid services assumptions.

## 7. RELIABILITY INFRASTRUCTURE (UNCHANGED ACROSS ALL OPTIONS)

**CRITICAL:** Regardless of which monetization option is selected (A, B, or C), the facility reliability infrastructure remains identical. This section is **independent** of the solar excess strategy.

### 7.1 2N UPS System (Tier III Compliance)

**All three monetization options require the same 2N UPS architecture:**

```
┌──────────────────── Main "Dirty" Bus ────────────────────┐
│                                                            │
│  [Utility] ──┬── [Solar 12MW] ──┬── [Option A/B/C] ──┬── │
│              │                   │                     │   │
│              └───────────────────┴─────────────────────┘   │
│                                  │                         │
└──────────────────────────────────┼─────────────────────────┘
                                   │
                                   ▼
                        ┌──────────────────────┐
                        │   2N UPS System      │
                        │  (A-Side / B-Side)   │
                        │   Tier III Compliant │
                        └──────────┬───────────┘
                                   │
                                   ▼
                       ┌───────────────────────┐
                       │  Data Center IT Load  │
                       └───────────────────────┘
                                   │
                       ┌───────────┴───────────┐
                       │                       │
                [Path A: Utility]      [Path B: Generators]
```

**Key Principle:**
- **Options A, B, C connect to main bus** (non-critical power path)
- **2N UPS creates critical A/B paths** for IT loads
- Failure of export system, mobile compute, or BESS does NOT impact DC reliability

### 7.2 JIT UPS Deployment Strategy

**Phased Deployment (Matches IT Load Growth):**

| Phase | Facility Load | UPS Capacity Deployed | UPS CAPEX | Cumulative UPS Cost |
|-------|---------------|----------------------|-----------|---------------------|
| **1** | 4.0-4.3MW | 6MW (N+1) | $4.5M | $4.5M |
| **2** | 8.0-8.5MW | Add 4MW modules | $3.0M | $7.5M |
| **3** | 12.0-12.8MW | Add 5MW modules | $3.8M | $11.3M |
| **4** | 16.0-17.0MW | Add 6MW modules | $4.5M | $15.8M |
| **5** | 27.0-28.4MW | Add 14MW modules | $10.5M | $26.3M |

**JIT Benefits:**
- **Phase 1 CAPEX reduction:** $4.5M vs. $26.3M upfront (preserves $21.8M cash)
- **IRR optimization:** Deploy capacity only when revenue justifies
- **Risk mitigation:** Avoid overbuilding for uncertain Phase 5 timeline

**Technology:**
- Modular UPS frames with hot-swappable power modules
- Phase 1: Install 2N frames ($2M) + 6MW modules ($2.5M)
- Phases 2-5: Add modules only (no frame/switchgear duplication)

### 7.3 Backup Generators

**N+1 Natural Gas Turbines (Phased Deployment):**

| Phase | Generator Capacity | CAPEX | Cumulative Cost |
|-------|-------------------|-------|-----------------|
| **1** | 2×4MW (N+1) | $2.4M | $2.4M |
| **2** | 3×4MW (N+1) | $1.4M | $3.8M |
| **3** | 4×4MW (N+1) | $1.4M | $5.2M |
| **4** | 5×4MW (N+1) | $1.4M | $6.6M |
| **5** | 8×4MW (N+1) | $4.2M | $10.8M |

**Specifications:**
- Natural gas turbines (20-30 min startup)
- UPS provides 15-min backup (bridges to generator startup)
- N+1 redundancy (lose one unit, maintain full capacity)
