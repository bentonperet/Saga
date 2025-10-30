**Created:** 2025-10-27

# Assessment: 60% Data Center Utilization Impact
## Microgrid + Data Center Financial Model

**Context:** Your updated model assumes **60% capacity utilization** on the 2 MW IT data center, while infrastructure is sized for 100% capacity.

---

## 1. LOAD PROFILE WITH 60% UTILIZATION

**Capacity vs. Actual:**
- **IT Capacity:** 2.0 MW
- **Utilization Factor:** 60%
- **Actual IT Load:** 1.2 MW (60% × 2.0 MW)
- **Facility Load @ PUE 1.3:** 1.56 MW (1.2 MW × 1.3)
- **Annual Consumption:** 13,666 MWh/year

**Infrastructure Sized For:**
- **BESS:** 2.6 MW / 10-12 MWh (100% capacity)
- **Turbines:** 4.5 MW total (3×1.5 MW, N+1)
- **Solar:** 8 MWdc (optimized for 75% solar fraction at 100% load)

---

## 2. ENERGY BALANCE AT 60% UTILIZATION

**Solar Performance (8 MWdc):**
- Annual Production: **16,819 MWh/year**
- Facility Consumption: **13,666 MWh/year**
- **Solar provides: 123% of facility energy** ✅

**Turbine Operation:**
- Turbines only needed: **Nighttime hours + cloudy days**
- Est. turbine generation: **3,153 MWh/year** (23% of energy vs. 25% at 100% util)
- **Pre-grid fuel cost: ~$315k/year**
  - vs. $587k at 100% utilization
  - **Fuel savings: $272k/year**

**Excess Solar:**
- **Peak daytime excess: ~6.4 MW** (8 MW solar - 1.56 MW load)
- **Annual excess energy: ~3,153 MWh** available for export/monetization
- Value @ $0.05/kWh export: **$158k/year**
- Value via mobile edge compute: **$3-4M/year** (if grid delayed)

---

## 3. FINANCIAL IMPACT

### 3.1 Data Center PropCo (Revenue Side)

**Rental Revenue @ 60% Utilization:**
- Occupied capacity: 1,200 kW (60% of 2,000 kW)
- Rental rate: $155/kW-month
- **Annual revenue: $2,232,000** (60% × $3,720,000)
- **Lost revenue vs. 100%: -$1,488,000/year**

**OPEX @ 60% Utilization:**
- Fixed costs: $720k/year (facility O&M, insurance, taxes - unchanged)
- Variable costs: ~60% of normal (utilities, minor maintenance)
- **Total OPEX: ~$750-850k/year**

**Data Center NOI:**
- Revenue: $2.23M
- OPEX: $0.80M
- **NOI: ~$1.43M/year** (vs. ~$3.0M at 100% utilization)
- **IRR impact: Likely drops from 14% to 8-10%**

---

### 3.2 Microgrid GenCo (Cost/Benefit)

**CAPEX (Unchanged):**
- Net CAPEX: **$16-18M** (after ITC)
- Must size for 100% capacity regardless of utilization

**OPEX Benefits:**
- **Lower fuel costs: $315k/year** (vs. $587k at 100% util)
- O&M: ~$130k/year (solar + BESS + turbines)
- **Total GenCo OPEX: $445k/year**

**Revenue Opportunities:**
- PPA from DC: $0.08/kWh × 13,666 MWh = **$1.09M/year**
- Excess solar export (if grid available): +$158k/year
- OR: Mobile edge lease (if grid delayed): +$3-4M/year
- Post-grid DR revenue: +$629k/year
- **Total revenue: $1.25M-$4.7M/year** (depending on strategy)

**GenCo NOI:**
- Best case (mobile edge pre-grid): $1.09M + $4M - $0.45M = **$4.64M/year**
- Base case (export only): $1.09M + $0.16M - $0.45M = **$0.80M/year**
- **IRR: 8-15%** (depends on grid timeline and excess solar monetization)

---

## 4. KEY INSIGHTS

### 4.1 The Good ✅

**1. Turbine Fuel Savings: $272k/year**
- Solar over-production means turbines rarely run pre-grid
- Post-grid, DR-only operation costs just $9k/year fuel

**2. Excess Solar Monetization Opportunity**
- **3,153 MWh/year** available for export or mobile edge
- If mobile edge: **$3-4M/year** for 12-24 months
- This could dramatically improve GenCo IRR

**3. Lower Operational Risk**
- BESS and turbines operating well below capacity
- Less wear and tear, longer equipment life
- More headroom for growth

**4. Easier Lease-Up**
- Start with 60% gives time to market and fill
- Lower risk than betting on 100% Day 1 occupancy
- Can grow into 100% as demand materializes

---

### 4.2 The Bad ❌

**1. Revenue Shortfall: -$1.5M/year**
- Data Center losing $1.5M/year vs. 100% occupancy
- Fixed CAPEX ($20.6M) spread over fewer tenants
- Debt service coverage ratio drops significantly

**2. Capital Inefficiency**
- Infrastructure built for 2.6 MW, using 1.56 MW
- **40% of CAPEX sitting idle:**
  - BESS: $4-5M unused capacity
  - Turbines: $1.8M unused capacity
  - Solar: Producing excess with no buyer (if grid delayed)

**3. Unit Economics Deteriorate**
- **Cost per occupied kW increases 67%:**
  - @ 100%: $10,316 CAPEX/kW
  - @ 60%: $17,193 CAPEX/kW
- **IRR drops 4-6 percentage points**

**4. Financing Risk**
- Lenders typically underwrite to 80-90% occupancy minimum
- 60% may trigger covenant violations or prevent debt financing
- May force higher equity requirement

---

### 4.3 The Critical Question 🤔

**Is 60% utilization:**

**A. A conservative Phase 1 ramp-up assumption?**
- Build capacity, lease up over 12-18 months
- Grow from 60% → 80% → 100%
- **If this: Model should show graduated revenue growth**

**B. A permanent steady-state assumption?**
- Only 60% of market demand long-term
- Excess capacity never fills
- **If this: Need to right-size infrastructure or exit**

---

## 5. SCENARIO COMPARISON

| Metric | 60% Utilization | 100% Utilization | Delta |
|--------|----------------|------------------|-------|
| **DC Revenue** | $2.23M/year | $3.72M/year | -$1.49M |
| **GenCo Fuel** | $315k/year | $587k/year | +$272k |
| **Excess Solar** | 3,153 MWh | 0 MWh | +3,153 MWh |
| **GenCo Monetization** | $158k-$4M | $0 | +$158k-$4M |
| **DC NOI** | $1.43M | $3.0M | -$1.57M |
| **GenCo NOI** | $0.8-4.6M | $0.7-1.3M | +$0.1-3.3M |
| **Combined NOI** | $2.2-6.0M | $3.7-4.3M | -$1.5M to +$1.7M |
| **DC IRR** | ~8-10% | ~14% | -4 to -6% |
| **GenCo IRR** | 8-15% | 11% | -3% to +4% |

**Net Impact:**
- **If mobile edge works:** Combined project NPV **improves** by $3-5M
- **If only grid export:** Combined project NPV **decreases** by $8-10M

---

## 6. RECOMMENDATIONS

### 6.1 If 60% Is Temporary (Lease-Up Period):

**✅ Model as graduated revenue ramp:**
- Year 1: 40% occupied → 60% → 80%
- Year 2: 80% → 90% → 100%
- Calculate blended IRR across lease-up period

**✅ Monetize excess solar during ramp:**
- Mobile edge compute lease: $3-4M/year for months 0-18
- Exit mobile edge as DC occupancy grows to 80%+
- **This turns 60% utilization into an advantage**

**✅ Pre-lease before construction:**
- Target 60-70% pre-leased before breaking ground
- Reduces risk, improves lender confidence
- Industry standard for spec data centers

---

### 6.2 If 60% Is Permanent (Demand Cap):

**❌ DO NOT BUILD as currently sized.**

**Consider:**
- **Option A:** Right-size to 1.2 MW IT capacity (60% of 2 MW)
  - CAPEX savings: $6-8M (smaller BESS, turbines, building)
  - Better capital efficiency: $8,600/kW vs. $17,193/kW
  
- **Option B:** Build for 1.5 MW with expansion option
  - Modular BESS (add strings later)
  - Add 2nd turbine when needed
  - Defer $3-5M CAPEX until demand materializes

- **Option C:** Find anchor tenant for full 2 MW
  - Sign 10-year lease for 1.5-2 MW before construction
  - Eliminates lease-up risk
  - Unlocks debt financing

---

### 6.3 If 60% Reflects Grid-Delayed Strategy:

**✅ This makes strategic sense:**
- Build for future 100% but operate at 60% until grid arrives
- Excess solar = revenue via mobile edge ($3-4M/year)
- GenCo economics actually **improve** during grid delay
- **After grid arrives + DC lease-up, project converges to 100% case**

**Action:**
- **Model two phases:**
  - **Phase 1 (0-24 months):** 60% DC occupancy, no grid, mobile edge revenue
  - **Phase 2 (24+ months):** 80-100% DC occupancy, grid connected, DR revenue
- Calculate **blended IRR** across both phases

---

## 7. BOTTOM LINE ASSESSMENT

### With 60% Utilization:

**Data Center PropCo:**
- **Weakened economics:** IRR drops from 14% to 8-10%
- **Financing risk:** May not meet lender DSC thresholds
- **Recommendation:** Pre-lease to 70%+ OR right-size infrastructure

**Microgrid GenCo:**
- **Improved economics IF excess solar monetized** via mobile edge
- **Worse economics IF only grid export** (loses $1-2M NPV)
- **Recommendation:** Pursue mobile edge aggressively for grid-delay period

**Combined Project:**
- **Best case (mobile edge):** NPV +$3-5M vs. 100% utilization
- **Base case (grid export):** NPV -$8-10M vs. 100% utilization
- **Critical dependency:** Grid timeline + mobile edge contract

---

## 8. NEXT STEPS

**1. Clarify Utilization Assumption (URGENT):**
- Is 60% a ramp-up curve or permanent state?
- If ramp-up, model monthly/quarterly growth to 100%
- If permanent, right-size infrastructure or find anchor tenant

**2. Validate Mobile Edge Opportunity:**
- Contact Crusoe Energy, Lancium, Applied Digital
- Request term sheet for 6 MW capacity lease
- **If yes: Project economics dramatically improve**
- **If no: Consider delaying project until grid available**

**3. Update Financial Model:**
- Add lease-up scenario (40% → 100% over 18 months)
- Add mobile edge revenue during grid delay
- Calculate scenario-weighted IRR

**4. Stress Test Financing:**
- Can lenders accept 60% occupancy?
- What equity % required if 60% permanent?
- **Likely need 40-50% equity vs. 30% at 100% occupancy**

---

**CRITICAL QUESTION FOR YOU:**

**Is the 60% utilization factor modeling:**
- **(A) A conservative lease-up assumption** (will grow to 100% over time)?
- **(B) Long-term demand cap** (market only supports 1.2 MW)?
- **(C) Grid-delay strategy** (operate partial until grid + lease up)?

**The answer completely changes the project viability.**

- If **(A):** Model is too conservative - add growth curve
- If **(B):** Infrastructure is oversized - need to redesign
- If **(C):** Economics improve with mobile edge - pursue aggressively

**Which scenario are you modeling?**
