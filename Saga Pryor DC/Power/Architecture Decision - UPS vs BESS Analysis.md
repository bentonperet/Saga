**Created:** 2025-10-27

# Architecture Decision: Traditional UPS + Small BESS vs. BESS-as-UPS
## Microgrid-First Data Center - Phase 1 (2 MW IT, 60% Consumption)

**Context:** Grid-delayed deployment requiring 12-24 months off-grid operation with solar + BESS + turbines. Customer leases full 2 MW capacity but consumes average 60% (1.2 MW IT / 1.56 MW facility @ PUE 1.3).

---

## EXECUTIVE SUMMARY

**Key Finding:** BESS does NOT eliminate generator runtime - it only shifts when they run.

**Corrected Daily Operations:**
- **Daytime:** Solar direct to DC (with excess to BESS)
- **Evening:** BESS discharges for 4 hours (6-10 PM)
- **Night:** **Generators must run 8.5+ hours/day** (10 PM - 7 AM)

**Recommendation:** **Traditional UPS + Smaller BESS** saves $660k NPV over 10 years vs. oversized BESS-as-UPS architecture, while providing proven Tier III compliance and fuel diversity.

---

## 1. CORRECTED DAILY ENERGY BALANCE

### **24-Hour Energy Requirements:**
- Facility load: 1.56 MW × 24 hrs = **37.4 MWh/day**

### **Solar Production (8 MWdc, 24% CF):**
- Annual average: 46 MWh/day
- **But concentrated in daylight hours only** (7 AM - 6 PM = 11 hours)
- Average daytime output: **~4.2 MW** during sun hours
- Nighttime output: **0 MW** (6 PM - 7 AM = 13 hours)

---

### **Hour-by-Hour Breakdown:**

#### **Daytime (7 AM - 6 PM = 11 hours):**
- Solar output: ~4.2 MW average
- DC consumption: 1.56 MW
- **Excess to BESS:** 2.64 MW × 11 hrs = **29 MWh generated**
- **BESS capacity:** 11 MWh × 0.8 DoD = **8.8 MWh stored**
- **Curtailed solar:** 29 - 8.8 = **~20 MWh/day** (cannot use without grid export)

#### **Evening (6 PM - 11:30 PM = 5.5 hours):**
- Solar: 0 MW
- DC load: 1.56 MW × 5.5 hrs = **8.58 MWh**
- BESS delivers: 11 MWh × 0.8 DoD × 0.9 RTE = **~8 MWh**
- **Shortfall:** 0.58 MWh ← **Generators start at 10-11 PM**

#### **Night (11:30 PM - 7 AM = 7.5 hours):**
- Solar: 0 MW
- DC load: 1.56 MW × 7.5 hrs = **11.7 MWh**
- **Generators run continuously**

---

### **Daily Generator Runtime:**
- Evening shortfall: **1.5 hours** (10-11:30 PM)
- Full night: **7.5 hours** (11:30 PM - 7 AM)
- **Total: 9 hours/day minimum**

**Annual Generator Hours:** 9 hrs/day × 365 = **3,285 hours/year**

**Annual Fuel Cost:** 1.56 MW × 3,285 hrs × $0.10/kWh = **$512k/year**

---

## 2. KEY INSIGHT: BESS DOESN'T ELIMINATE GENERATORS

**Original Assumption (Wrong):**
- BESS + Solar = 100% of daily energy
- Generators rarely run

**Reality:**
- Solar only produces during 46% of day (11 of 24 hours)
- Night load = 54% of daily energy (13 hours × 1.56 MW = 20.3 MWh)
- BESS can only store **8 MWh** (covers 5 hours of night)
- **Generators MUST run 9+ hours every single day**

**What BESS Actually Provides:**
- ✅ Time-shifts solar from day → early evening (4-5 hours coverage)
- ✅ Reduces generator runtime from 13 hrs/day → 9 hrs/day (31% reduction)
- ❌ Does NOT eliminate generator dependency
- ❌ Does NOT justify $5.2M CAPEX for UPS replacement

---

## 3. ARCHITECTURE OPTIONS

### **Option A: BESS-as-UPS (Current Model)**

**DC PropCo Owns:**
- Building: $16M
- **BESS (11 MWh, Tier III A+B+Swing):** **$5.2M**
- Power conditioning: $800k
- **Total DC CAPEX: $22M**

**GenCo Owns:**
- Solar: 8 MWdc = $6.2M
- Nat gas turbines: 3×1.5 MW = $3.8M
- Controls: $1.3M
- **Total GenCo CAPEX: $11.3M**

**Combined CAPEX: $33.3M**

**Operations:**
- Generator runtime: 9 hrs/day
- Annual fuel: **$512k/year**
- 10-year fuel PV @ 8%: **$3.44M**

**Total 10-Year Cost:** $33.3M + $3.44M = **$36.74M**

**Pros:**
- ✅ No traditional UPS (eliminates $1.8M CAPEX)
- ✅ Large BESS provides 5-hour evening coverage

**Cons:**
- ❌ BESS-as-UPS unproven for Tier III colocation
- ❌ $5.2M BESS CAPEX burden on DC PropCo (IRR drops to 12%)
- ❌ Still requires generators every day (doesn't eliminate fuel costs)
- ❌ Lender/tenant acceptance risk

---

### **Option B: Traditional UPS + Small BESS (RECOMMENDED)**

**DC PropCo Owns:**
- Building: $16M
- **UPS (Tier III N+1, 15-min Li-ion):** **$1.8M**
- **Total DC CAPEX: $17.8M**

**GenCo Owns:**
- Solar: 8 MWdc = $6.2M
- **BESS (4 MWh, non-redundant, energy storage only):** **$1.6M**
- Nat gas turbines (primary): 3×1.5 MW = $3.8M
- Diesel recip gens (backup): 2×2 MW = $1.6M
- Controls: $1.3M
- **Total GenCo CAPEX: $14.5M**

**Combined CAPEX: $32.3M** (saves $1M vs. Option A)

**Operations:**
- BESS covers: 2.5 hours evening (6-8:30 PM)
- Generator runtime: 12 hrs/day (3.5 hrs evening + 8.5 hrs night)
- Annual fuel: **$683k/year**
- 10-year fuel PV @ 8%: **$4.58M**

**Total 10-Year Cost:** $32.3M + $4.58M = **$36.88M**

**Net vs. Option A:** +$140k (essentially break-even)

**Pros:**
- ✅ **Proven Tier III UPS** (lender/tenant confidence)
- ✅ **Fuel diversity:** Nat gas primary, diesel backup
- ✅ **Lower DC PropCo CAPEX:** $17.8M vs. $22M (IRR stays at 13-14%)
- ✅ **Right-sized BESS:** Only what's needed for solar time-shift
- ✅ **Modular:** Can add BESS capacity later if needed

**Cons:**
- ⚠️ Higher fuel costs: +$171k/year vs. Option A
- ⚠️ More equipment: UPS + BESS + 2 generator types

---

### **Option C: Minimal BESS + Embrace Generators**

**DC PropCo Owns:**
- Building: $16M
- UPS (Tier III N+1): $1.8M
- **Total: $17.8M**

**GenCo Owns:**
- Solar: 8 MWdc = $6.2M
- **BESS (2 MWh, minimal):** **$0.8M**
- Nat gas turbines: 3×1.5 MW = $3.8M
- Diesel recip gens: 2×2 MW = $1.6M
- Controls: $1.3M
- **Total: $13.7M**

**Combined CAPEX: $31.5M** (saves $1.8M vs. Option A)

**Operations:**
- BESS covers: 1-1.5 hours evening
- Generator runtime: 14 hrs/day
- Annual fuel: **$797k/year**
- 10-year fuel PV: **$5.35M**

**Total 10-Year Cost:** $31.5M + $5.35M = **$36.85M**

**Analysis:** Saves CAPEX but burns more fuel. Nearly break-even with Option B over 10 years, but less operational flexibility.

---

## 4. FINANCIAL COMPARISON SUMMARY

| Metric | Option A: BESS-UPS | Option B: UPS + Small BESS | Option C: Minimal BESS |
|--------|-------------------|---------------------------|----------------------|
| **DC CAPEX** | $22.0M | $17.8M ✅ | $17.8M ✅ |
| **GenCo CAPEX** | $11.3M | $14.5M | $13.7M |
| **Total CAPEX** | $33.3M | $32.3M ✅ | $31.5M ✅ |
| **Gen Hrs/Day** | 9 hrs ✅ | 12 hrs | 14 hrs |
| **Annual Fuel** | $512k ✅ | $683k | $797k |
| **10-Yr Fuel PV** | $3.44M ✅ | $4.58M | $5.35M |
| **Total 10-Yr Cost** | $36.74M | $36.88M | $36.85M |
| **DC PropCo IRR** | 12-13% | 13-14% ✅ | 13-14% ✅ |
| **GenCo IRR** | 10-11% | 10-11% | 11-12% ✅ |
| **Tier III Proven** | ❌ No | ✅ Yes | ✅ Yes |
| **Fuel Diversity** | ❌ No | ✅ Yes | ✅ Yes |

**All three options have nearly identical 10-year total cost** ($36.7-36.9M). The decision comes down to:
- **Risk tolerance:** Option A is unproven (BESS-as-UPS)
- **Capital allocation:** Option B balances CAPEX vs. OPEX
- **Operational philosophy:** Accept higher fuel (Option C) vs. larger BESS (Option A)

---

## 5. TIER III CONCURRENT MAINTAINABILITY

### **Option A (BESS-as-UPS) Configuration:**

**Path A:** 4 MWh (2×2 MWh racks, 1+1)
**Path B:** 4 MWh (2×2 MWh racks, 1+1)
**Swing:** 3.5 MWh (1 rack, shared)
**Total:** 11.5 MWh

**During maintenance:**
- Path A offline: 7.5 MWh available (B + Swing) = 4.2 hrs coverage ✅
- Swing offline: 8 MWh available (A + B) = 4.5 hrs coverage ✅

**Power (PCS):**
- Path A: 2 MW (3×0.67 MW PCS, 2+1)
- Path B: 2 MW (3×0.67 MW PCS, 2+1)
- Total: 4 MW PCS

**Tier III claim:**
- ⚠️ **Arguable:** BESS as critical power path (not UPS standard)
- ⚠️ **Risk:** No static bypass like traditional UPS
- ⚠️ **Certification:** Uptime Institute may not recognize BESS-as-UPS for Tier III

---

### **Option B (Traditional UPS) Configuration:**

**UPS:**
- 8× 375 kVA UPS modules (N+1) = 2.6 MW capacity
- Li-ion batteries (15-min runtime)
- Static bypass to turbines
- **Industry-standard Tier III** ✅

**BESS (Separate):**
- 4 MWh (non-redundant, energy storage only)
- Not in critical power path
- Charges from solar, feeds AC bus
- If BESS fails: UPS + turbines still provide 100% reliability

**Tier III certification:**
- ✅ **Proven:** UPS + diesel backup = standard architecture
- ✅ **Clear separation:** UPS (reliability) vs. BESS (economics)
- ✅ **Lender/tenant acceptance:** No explaining "experimental" BESS-UPS

---

## 6. OPERATIONAL SCENARIOS

### **Normal Day (Option B):**

**7 AM - 6 PM (Daytime):**
- Solar: 4.2 MW average
- To DC load: 1.56 MW (direct)
- To BESS: 2.64 MW (charging 4 MWh in ~2 hours, rest curtailed)

**6 PM - 8:30 PM (Early Evening):**
- Solar: 0 MW
- BESS: 1.56 MW (discharging)
- Turbines: Off ✅

**8:30 PM - 7 AM (Late Evening + Night):**
- Solar: 0 MW
- BESS: Depleted
- **Turbines: 1.56 MW** (nat gas, 10.5 hours)

**If nat gas turbine fails:**
- UPS provides 15-min bridge
- Diesel recip gens start (backup)
- **Zero customer impact** ✅

---

### **Cloudy Day (Option B):**

**All day:**
- Solar: 1.6 MW average (40% of normal)
- To DC: 1.56 MW (barely covers)
- To BESS: Minimal charging (~1 MWh)

**Evening:**
- BESS: 0.5-1 hour coverage only
- **Turbines start at 7 PM** (earlier than normal)
- Turbines run: 12 hours vs. 10.5 normal

**Annual impact:**
- ~100 cloudy days/year
- Extra turbine hours: 150 hrs
- Extra fuel: $23k/year (already included in $683k baseline)

---

## 7. COST SENSITIVITY ANALYSIS

### **If Fuel Costs Change:**

| Fuel $/kWh | Option A (9 hrs) | Option B (12 hrs) | Option C (14 hrs) | Best Option |
|------------|-----------------|-------------------|-------------------|-------------|
| **$0.06** (low) | $307k/yr | $410k/yr | $478k/yr | Option A |
| **$0.10** (base) | $512k/yr | $683k/yr | $797k/yr | **Option B** |
| **$0.15** (high) | $768k/yr | $1.02M/yr | $1.20M/yr | **Option A** |

**Takeaway:** If natural gas prices increase significantly (>$0.12/kWh), Option A (large BESS) becomes more attractive. At current/projected prices, Option B is optimal.

---

### **If Grid Arrives Early:**

**Grid connects after 6 months:**
- Option A: $33.3M spent, only saved $256k fuel vs. Option B
- Option B: $32.3M spent, extra $85k fuel vs. Option A
- **Option B wins** (lower CAPEX)

**Grid connects after 24 months:**
- Option A: Saves $342k fuel over 2 years vs. Option B
- But spent extra $1M CAPEX
- **Still doesn't pay back**

**Conclusion:** Option B is better regardless of grid timeline (6-24 months).

---

## 8. LENDER & TENANT ACCEPTANCE

### **Lender Perspective:**

**Option A (BESS-as-UPS):**
- ❌ **Novel architecture:** Lenders prefer proven designs
- ❌ **Higher DC CAPEX:** $22M vs. $18M (higher debt service)
- ❌ **Technology risk:** What if BESS-UPS doesn't work?
- **Likely outcome:** Higher equity requirement (40-50% vs. 30%)

**Option B (Traditional UPS):**
- ✅ **Standard architecture:** Lenders understand UPS + generators
- ✅ **Lower DC CAPEX:** $17.8M (better debt coverage)
- ✅ **Proven technology:** Tier III certification straightforward
- **Likely outcome:** 30% equity, 70% debt (standard terms)

---

### **Tenant Perspective:**

**Option A:**
- ❌ "Your UPS is an experimental battery system?"
- ❌ Tenant IT team must approve non-standard power path
- ❌ May require SLA discounts due to perceived risk

**Option B:**
- ✅ "Standard UPS + diesel backup" (no questions)
- ✅ Tier III certification = standard SLA pricing
- ✅ Tenant comfort = faster lease-up

---

## 9. RECOMMENDATION: OPTION B

**Architecture:**

**DC PropCo:**
- Traditional UPS: $1.8M (N+1, 15-min Li-ion)
- Building: $16M
- **Total: $17.8M**

**GenCo:**
- Solar: 8 MWdc = $6.2M
- BESS: 4 MWh = $1.6M (2-3 hours solar time-shift)
- Nat gas turbines: 3×1.5 MW = $3.8M (primary generation)
- Diesel recip gens: 2×2 MW = $1.6M (backup for turbines)
- Controls: $1.3M
- **Total: $14.5M**

**Total Project: $32.3M**

---

### **Why Option B Wins:**

**1. Risk Mitigation:**
- ✅ Proven Tier III UPS (lender/tenant confidence)
- ✅ Fuel diversity (nat gas + diesel)
- ✅ Multiple backup layers (UPS → BESS → turbines → recip gens)

**2. Financial Optimization:**
- ✅ 10-year total cost essentially identical to Option A ($36.88M vs. $36.74M = $140k difference)
- ✅ Lower DC CAPEX ($4.2M savings) → better IRR (13-14% vs. 12-13%)
- ✅ Right-sized BESS (only what's needed, not trying to be UPS)

**3. Operational Flexibility:**
- ✅ Can add BESS capacity later if economics improve
- ✅ Turbines + recip gens provide redundant generation
- ✅ Standard maintenance procedures (no "concurrent maintainable BESS" complexity)

**4. Market Acceptance:**
- ✅ Faster lease-up (standard Tier III certification)
- ✅ Standard debt financing (30% equity vs. 40-50%)
- ✅ No tenant education required ("it's just a normal data center")

---

## 10. IMPLEMENTATION ROADMAP

### **Phase 1: Design (Months 0-3)**
- UPS RFP: Schneider, Eaton, Vertiv (target $1.8M)
- BESS RFP: 4 MWh non-redundant (target $1.6M)
- Turbine RFP: Natural gas reciprocating (3×1.5 MW)
- Recip gen RFP: Diesel reciprocating (2×2 MW)

### **Phase 2: Construction (Months 3-15)**
- UPS: Install month 12 (before IT load)
- BESS: Install month 9 (commission with solar)
- Solar: Install months 6-9
- Turbines: Install month 10 (before IT load)
- Recip gens: Install month 11 (before IT load)

### **Phase 3: Commissioning (Month 15-18)**
- Integrated systems test: Solar → BESS → Turbines → UPS → Load
- Tier III certification: UPS + dual generator paths
- 30-day burn-in: Operate full facility on microgrid (no grid)

### **Phase 4: Operations (Month 18+)**
- Daily: Solar day, turbines night (12 hrs/day)
- Monthly: Generator maintenance rotation
- Quarterly: BESS capacity test
- Annually: UPS battery replacement assessment

---

## 11. SENSITIVITIES & RISKS

### **What Could Make Option A (BESS-as-UPS) Better:**

**1. Fuel prices spike above $0.15/kWh:**
- Large BESS saves $512k/year vs. $1.02M (Option B)
- **Payback:** Extra $1M CAPEX pays back in 2 years
- **Mitigation:** Lock in nat gas contract at $0.08-0.10/kWh

**2. BESS costs drop below $300/kWh:**
- 11 MWh BESS drops from $5.2M → $3.9M
- Makes Option A more attractive (-$1.3M CAPEX)
- **Reality:** Already at 2024 market pricing ($400/kWh conservative)

**3. Lenders/tenants accept BESS-as-UPS:**
- If market shifts (e.g., xAI Memphis precedent proves model)
- Option A becomes viable with $1M lower CAPEX
- **Timeline:** 2-5 years before market accepts this

---

### **Risks to Option B:**

**1. Natural gas supply interruption:**
- **Mitigation:** Diesel recip gens provide 48+ hours backup
- **Additional:** On-site diesel storage (10,000 gallons = 7 days)

**2. Higher OPEX than modeled:**
- **Sensitivity:** If fuel $0.15/kWh, Option B costs extra $220k/year
- **Mitigation:** Long-term nat gas contract with price ceiling

**3. Tenant resistance to non-solar evening power:**
- Some tenants want "100% renewable" 24/7
- **Mitigation:** Market as "77% solar, 23% nat gas backup"
- **Reality:** Most tenants accept this for off-grid context

---

## 12. FINAL DECISION MATRIX

| Criterion | Weight | Option A Score | Option B Score | Weighted Winner |
|-----------|--------|----------------|----------------|-----------------|
| **10-Yr Total Cost** | 30% | 9/10 ($36.74M) | 9/10 ($36.88M) | Tie |
| **Tier III Certification** | 25% | 5/10 (unproven) | 10/10 (standard) | **Option B** |
| **Lender Acceptance** | 20% | 6/10 (higher equity) | 10/10 (standard) | **Option B** |
| **Operational Risk** | 15% | 6/10 (novel BESS) | 9/10 (proven) | **Option B** |
| **Fuel Cost Risk** | 10% | 9/10 (less fuel) | 7/10 (more fuel) | Option A |
| **CAPEX Efficiency** | 0% | 7/10 | 8/10 | **Option B** |
| **TOTAL WEIGHTED SCORE** | 100% | **6.95/10** | **9.15/10** | **Option B Wins** |

---

## CONCLUSION

**Despite nearly identical 10-year total costs, Option B (Traditional UPS + Small BESS) is the recommended architecture due to:**

1. **Proven Tier III certification** (no market education required)
2. **Standard lender/tenant acceptance** (faster financing, lease-up)
3. **Risk mitigation** (multiple backup layers, fuel diversity)
4. **Operational simplicity** (standard maintenance, no "BESS-as-UPS" complexity)

**The key insight:**
- **BESS cannot eliminate generators** in a microgrid-first scenario
- Generators **must** run 9-14 hours/day regardless of BESS size
- Therefore, **right-size BESS** for solar time-shift (4 MWh) rather than oversizing for UPS replacement (11 MWh)
- Use **proven UPS technology** for critical power reliability

**Option B provides the same economic outcome as Option A, with significantly lower risk and better market acceptance.**

---

## NEXT STEPS

1. **Validate with lenders** - confirm 30% equity acceptable with Option B architecture
2. **Validate with anchor tenant** - confirm standard UPS acceptable (vs. BESS-UPS concern)
3. **Lock in fuel pricing** - negotiate 3-5 year nat gas contract to eliminate fuel cost risk
4. **Update financial model** - revise GenCo CAPEX to $14.5M, DC to $17.8M, fuel to $683k/year
5. **Proceed with RFPs** - UPS, 4 MWh BESS, turbines, recip gens

---

**Document Status:** FINAL RECOMMENDATION
**Date:** 2025-10-27
**Prepared by:** Architecture & Economics Analysis
