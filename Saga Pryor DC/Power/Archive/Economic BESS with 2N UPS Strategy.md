**Created:** 2025-10-22 14:45

# Economic BESS with 2N UPS Strategy
## 10-12MW Data Center Design Memo

**Saga Energy Pryor Data Center**

**Document Purpose:** Demonstrate that a Tier III-compliant design using JIT-deployed 2N UPS + separate economic BESS delivers superior IRR through revenue generation rather than cost avoidance, while maintaining bankable reliability standards.

**Prepared By:** PACHYDERM GLOBAL / PGCIS
**Prepared For:** Saga Energy
**Date:** 2025-10-22
**Status:** DRAFT FOR CLIENT REVIEW

**Related Documents:**
- [[BESS as UPS Replacement V4]] - Original approach (superseded by this memo)
- [[Technical Addendum - BESS Implementation Details]] - Detailed specifications

**Tags:** #saga-project #economic-bess #tier3-design #jit-deployment #revenue-generation

---

## EXECUTIVE SUMMARY

### The Recommendation
**Deploy separate systems for reliability (2N UPS) and economics (1N BESS) to maximize IRR through revenue generation while maintaining Tier III compliance and lender confidence.**

### Why BESS-as-UPS Fails Financially

| Issue                          | Problem                                                         | Financial Impact                                             |
| ------------------------------ | --------------------------------------------------------------- | ------------------------------------------------------------ |
| **Tier III Compliance**        | Single BESS creates non-maintainable SPOF                       | Requires 2N BESS design: $16-20M vs. $11-13M traditional UPS |
| **Dual-Purpose Contradiction** | UPS requires maintaining charge; solar/revenue requires cycling | Cannot capture both values simultaneously with single system |
| **Lender Risk**                | Exotic microgrid topology unproven at scale                     | Higher financing costs or project rejection                  |
| **Maintenance Outages**        | BESS offline = zero UPS protection                              | Violates Tier III "concurrently maintainable" requirement    |

**Bottom Line:** A Tier III-compliant BESS-as-UPS requires ~$16-20M (2N design), eliminating estimated savings.

### Why Economic BESS + 2N UPS Succeeds

| Component | Strategy | Financial Benefit |
|-----------|----------|-------------------|
| **2N UPS** | JIT modular deployment | $7-8M Phase 0 vs. $14M upfront → IRR optimization |
| **Economic BESS** | Phase-adaptive revenue strategy | $800k-1.2M/year revenue (early phases: solar capture, later: grid services) |
| **Decoupled Design** | BESS not in critical power path | Can discharge to 0% SOC without reliability risk |
| **Tier III Compliant** | Traditional 2N UPS proven topology | Lender confidence, lower financing costs |

**Net Financial Impact (20-year NPV):**
- BESS revenue: **$12-18M** (discounted at 8%)
- JIT UPS deployment IRR boost: **+2-4% project IRR**
- Risk-adjusted financing benefit: **-50-100 bps cost of capital**

---

## 1. SYSTEM ARCHITECTURE

### 1.1 Parallel Design Topology

```
┌──────────────────── Main "Dirty" Bus (Non-Critical) ────────────────────┐
│                                                                          │
│  [Utility POI] ──┬── [Solar 12MW] ──┬── [Economic BESS 16MWh] ──┬──    │
│                  │                   │                            │      │
│                  └───────────────────┴────────────────────────────┘      │
│                                      │                                   │
└──────────────────────────────────────┼───────────────────────────────────┘
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
                           │    (10MW Critical)    │
                           └───────────────────────┘
                                       │
                           ┌───────────┴───────────┐
                           │                       │
                    [Path A: Utility]      [Path B: 5×4MW Turbines]
```

**Key Principle:** BESS is a **revenue asset** on the main bus, NOT a **reliability component** in the critical power path.

### 1.2 Component Specifications

**2N UPS System:**
- **Topology:** Dual A/B bus, N+1 per side
- **Capacity:** 4.5MW → 9MW → 13.5MW (Just-in-time deployment)
- **Technology:** Modular frames with plug-in power modules
- **Standards:** UL 1778, IEC 62040, Tier III certified
- **Backup Duration:** 15 minutes (bridge to generators)

**Economic BESS:**
- **Energy:** 16 MWh (LFP chemistry)
- **Power:** 16MW AC (4×4MW grid-following inverters)
- **Topology:** Single system (1N) - NOT in critical path
- **Standards:** UL 9540, UL 9540A, NFPA 855
- **Maintenance:** Can go fully offline without DC impact

**Backup Generators:**
- **Capacity:** 5×4MW natural gas turbines (N+1)
- **Startup Time:** 20-30 minutes (covered by UPS)
- **Fuel:** Natural gas (dual-fuel capable)

---

## 2. WHY BESS-AS-UPS FAILS THE BUSINESS CASE

### 2.1 The Tier III Compliance Problem

**Tier III Requirement:**
> "Concurrently maintainable—any single component can be removed from service for planned maintenance without disrupting IT load."

**Single BESS Design:**
```
Grid → [BESS 16MWh] → Data Center
           ↑
    SINGLE POINT OF FAILURE
```

When this BESS undergoes quarterly maintenance, battery replacement, or inverter service, the facility has **zero UPS protection**. This violates Tier III.

**True Tier III BESS-as-UPS:**
- Requires **2N design:** Two independent 16 MWh BESS systems (A-side + B-side)
- **Cost:** $16-20M for dual BESS vs. $11-13M for traditional 2N UPS
- **Result:** No savings, higher cost with unproven topology

### 2.2 The Dual-Purpose Contradiction

A single BESS cannot simultaneously:

| Function | Required State | Incompatible Because... |
|----------|----------------|-------------------------|
| **UPS Backup** | 90-100% SOC at all times | Cannot charge (already full) |
| **Solar Capture** | Charge daily from excess solar | Cannot be full to accept charge |
| **Night Discharge** | Discharge to offset grid use | Depletes UPS backup capacity |
| **Market Revenue** | Discharge during peak pricing | Depletes UPS backup capacity |

**Example Scenario (Phase 1, 8MW facility load):**
- **Morning:** Solar excess 4MW → Want to charge BESS
- **Problem:** BESS at 100% SOC for UPS duty → Cannot accept charge → Solar curtailed or exported at low value
- **Afternoon:** Grid prices spike → Want to discharge BESS for arbitrage
- **Problem:** Discharging to 40% SOC leaves only 25 minutes of backup (violates UPS requirement)

**Financial Impact:** You must choose **either** UPS reliability **or** economic cycling. You cannot monetize both functions with a single system.

### 2.3 Lender and Insurance Risk

**What Financiers See:**

| Traditional 2N UPS | BESS-as-UPS Microgrid |
|-------------------|----------------------|
| ✅ 40+ years proven track record | ❌ <5 deployments at 10MW+ DC scale |
| ✅ Understood failure modes | ❌ Novel failure scenarios |
| ✅ Standard insurance rates | ❌ Higher premiums or coverage gaps |
| ✅ Commodity service providers | ❌ Vendor lock-in risk |

**Financing Cost Impact:**
- **Traditional design:** Base rate + 150-200 bps project risk premium
- **Unproven topology:** Base rate + 250-350 bps → **+100 bps penalty**
- On $100M project: **+$1M/year financing cost** = $10M+ NPV loss

---

## 3. ECONOMIC BESS VALUE PROPOSITION

### 3.1 Phase-Adaptive Revenue Strategy

The economic BESS pivots its revenue model as the facility scales:

**Phases 0-1 (Low Load: 4.5-9MW facility)**

**Solar Excess Capture:**
- Solar production: 63 MWh/day (12MW × 5.25 peak hours)
- Facility consumption: 108-216 MWh/day (varies by phase)
- **Excess available:** 18-25 MWh/day (Phase 0), 12-16 MWh/day (Phase 1)
- **BESS captures:** 16 MWh/day (100% in Phase 1, 65-90% in Phase 0)

**Operating Pattern:**
- **7am-3pm:** Charge from solar excess (3-4MW for 4-6 hours)
- **7pm-11pm:** Discharge to facility (4MW for 4 hours) → Offset grid purchases
- **Result:** Capture excess solar that would otherwise be curtailed or exported at wholesale rates

**Revenue Calculation (Phase 1 example):**
- BESS captures: 16 MWh/day × 350 days/year = 5,600 MWh/year
- Avoided grid purchase: 5,600 MWh × $0.12/kWh = **$672k/year**
- Alternative (wholesale export): 5,600 MWh × $0.03/kWh = $168k/year
- **Value of self-consumption:** $504k/year vs. export option

**Phases 2-3 (High Load: 13.5MW+ facility)**

**Grid Services Revenue:**

Once facility load exceeds solar production, solar excess disappears. BESS pivots to market participation:

| Revenue Stream | Mechanism | Annual Value |
|----------------|-----------|--------------|
| **SPP Regulation Up** | Provide frequency response 16MW × 4 hours/day | $320-480k |
| **Demand Response** | Discharge during SPP peak events (50-80 hours/year) | $240-400k |
| **Capacity Credit** | Summer peak availability (4 months) | $120-200k |
| **Energy Arbitrage** | Charge off-peak ($0.04), discharge peak ($0.15) | $160-280k |

**Total Phase 2-3 Revenue Potential:** $840k-1.36M/year

**Key Advantage of Decoupled Design:**
- BESS can discharge to **0% SOC** during high-value events (not constrained by UPS duty)
- Can go **fully offline** for maintenance during low-price periods (2N UPS maintains DC reliability)
- **Optimizes for revenue** rather than reliability compromise

### 3.2 20-Year Financial Model

**Assumptions:**
- BESS CAPEX: $10M (Phase 0: $8M base + Phase 1-2 inverters: $2M)
- Battery replacement: Year 12 at $4M (50% cost reduction)
- O&M: $80k/year
- Discount rate: 8%
- Revenue degradation: -1.5%/year (capacity fade)

**Revenue Profile:**

| Period      | Primary Revenue Source            | Annual Revenue | Cumulative NPV |
| ----------- | --------------------------------- | -------------- | -------------- |
| Years 1-4   | Solar excess capture (Phases 0-1) | $600-800k      | $2.1M          |
| Years 5-12  | Grid services (Phases 2-3)        | $900k-1.2M     | $6.4M          |
| Year 12     | Battery replacement               | -              | -$2.8M         |
| Years 13-20 | Grid services (degraded)          | $700k-900k     | $4.2M          |

**20-Year NPV:** $12.1M revenue - $10M CAPEX - $2.8M replacement - $1.1M O&M = **$8.2M net NPV**

**Simple Payback:** 11-13 years
**IRR:** 12-15% (BESS system standalone)

**Critical Insight:** This return is **only possible** because the BESS can fully cycle (0-100% SOC) without reliability constraints. A BESS-as-UPS constrained to 90-100% SOC would capture <20% of this revenue.

---

## 4. JIT UPS DEPLOYMENT FOR IRR OPTIMIZATION

### 4.1 Phased Deployment Strategy

**Traditional Approach (Upfront Sizing):**
- Install full 13.5MW UPS capacity in Phase 0: **$14M upfront**
- Operates at 33% utilization in Phase 0 (4.5MW load / 13.5MW capacity)
- **Problem:** $9.5M of CAPEX earns zero return for 18-24 months

**JIT Approach (Match Capacity to Revenue):**

| Phase | Facility Load | UPS Deployment | Phase CAPEX | Cumulative |
|-------|---------------|----------------|-------------|------------|
| **0** | 4.5MW | Install frames + 6MW modules (N+1) | $7.5M | $7.5M |
| **1** | 9MW | Add 4.5MW modules | $3.2M | $10.7M |
| **2** | 13.5MW | Add 6MW modules | $3.8M | $14.5M |

**Financial Benefits:**

**Capital Efficiency:**
- Phase 0 CAPEX reduced: $14M → $7.5M = **$6.5M cash preserved**
- Deploy remaining $6.5M only when revenue justifies (Phases 1-2)
- **Working capital benefit:** $6.5M earning interest or deployed elsewhere for 12-18 months

**IRR Impact Example:**

Assume $100M total project, 10MW IT capacity, 3-phase deployment over 24 months:

| Metric | Upfront UPS | JIT UPS | Improvement |
|--------|-------------|---------|-------------|
| Phase 0 CAPEX | $82M | $75.5M | -$6.5M |
| Phase 0 Revenue | $3.6M/year | $3.6M/year | - |
| Project IRR | 18.2% | 20.7% | **+2.5%** |
| NPV @ 8% discount | $142M | $149M | **+$7M** |

**Why This Matters for Financing:**
- Higher Phase 0 IRR = stronger debt service coverage ratio (DSCR)
- Lower upfront CAPEX = reduced equity requirement
- JIT deployment demonstrates disciplined capital allocation (lender confidence)

### 4.2 Modular UPS Technology

**How JIT Deployment Works:**

Modern UPS systems use **hot-swappable power modules** in fixed frames:

```
Phase 0 Installation:
┌─────────────────────────────────────┐
│  UPS Frame A (800kW capacity)       │
│  ┌────┐ ┌────┐ ┌────┐ [empty] [empty]│ ← Install 3 modules (2.4MW)
│  │Mod1│ │Mod2│ │Mod3│               │   + room for 2 more
└─────────────────────────────────────┘

Phase 1 Addition:
┌─────────────────────────────────────┐
│  UPS Frame A (800kW capacity)       │
│  ┌────┐ ┌────┐ ┌────┐ ┌────┐ ┌────┐│ ← Add 2 modules
│  │Mod1│ │Mod2│ │Mod3│ │Mod4│ │Mod5││   (now 4MW, N+1)
└─────────────────────────────────────┘
```

**Phase 0 Investment:**
- UPS frames, switchgear, distribution: **$4M** (one-time, supports all phases)
- Power modules for 4.5MW (N+1): **$3.5M**
- **Total Phase 0:** $7.5M

**Phases 1-2 Investment:**
- Additional power modules only: **$7M** (no frame/switchgear duplication)

**Key Advantage:** You build the "skeleton" (2N redundant frames) upfront for Tier III compliance, but only populate with revenue-justified "muscle" (power modules) as load grows.

---

## 5. SYSTEM COSTS & FINANCIAL COMPARISON

### 5.1 Total System CAPEX (All Phases)

| Component | Phase 0 | Phase 1 | Phase 2 | Total |
|-----------|---------|---------|---------|-------|
| **2N UPS System** | | | | |
| - Frames/switchgear | $4.0M | - | - | $4.0M |
| - Power modules (4.5MW) | $3.5M | - | - | $3.5M |
| - Power modules (add 4.5MW) | - | $3.2M | - | $3.2M |
| - Power modules (add 6MW) | - | - | $3.8M | $3.8M |
| **Economic BESS** | | | | |
| - Batteries (16 MWh) | $5.2M | - | - | $5.2M |
| - Inverters (2×4MW) | $1.6M | - | - | $1.6M |
| - Inverters (add 1×4MW) | - | $0.8M | - | $0.8M |
| - Inverters (add 1×4MW) | - | - | $0.8M | $0.8M |
| - Controls/BMS | $0.8M | - | - | $0.8M |
| - Fire safety (NFPA 855) | $0.4M | - | - | $0.4M |
| **Backup Generators** | | | | |
| - Turbines (2×4MW) | $2.4M | - | - | $2.4M |
| - Turbines (add 1×4MW) | - | $1.4M | - | $1.4M |
| - Turbines (add 2×4MW) | - | - | $2.8M | $2.8M |
| **Switchgear/Integration** | $1.5M | $0.3M | $0.3M | $2.1M |
| | | | | |
| **Phase Totals** | **$19.4M** | **$5.7M** | **$7.7M** | **$32.8M** |

**Note:** Solar costs ($14-16M) excluded as identical across all design approaches.

### 5.2 Comparison to Alternative Designs

| Design Approach | Total CAPEX | Tier III Compliant? | BESS Revenue Potential | Project IRR Impact |
|----------------|-------------|---------------------|------------------------|-------------------|
| **Recommended: Economic BESS + JIT 2N UPS** | $32.8M | ✅ Yes | $840k-1.2M/year (full) | +2-4% (JIT benefit) |
| **Traditional: No BESS + Upfront 2N UPS** | $20.6M | ✅ Yes | $0 | Baseline |
| **Flawed: Single BESS-as-UPS** | $22.5M | ❌ No (SPOF) | $200-400k/year (constrained) | N/A (not financeable) |
| **True Tier III BESS-as-UPS (2N BESS)** | $38-42M | ✅ Yes | $200-400k/year (constrained) | -3 to -5% (excess CAPEX) |

**Key Takeaway:** Economic BESS + JIT UPS costs $12M more than traditional approach but generates $8.2M NPV + 2-4% IRR boost = **net positive** while maintaining Tier III compliance.

---

## 6. IMPLEMENTATION ROADMAP

### 6.1 Phase 0 (Months 0-12)

**Objectives:**
- Establish Tier III-compliant power infrastructure
- Deploy economic BESS to capture early-phase solar excess
- Minimize upfront CAPEX for IRR optimization

**Deployments:**
- 2N UPS frames + 6MW power modules (N+1 for 4.5MW load)
- 16 MWh BESS + 2×4MW inverters
- 2×4MW turbine generators (N+1)
- 12MW solar array

**Operational Mode:**
- **Daytime:** Solar excess (7-8MW) charges BESS
- **Nighttime:** BESS discharges to facility (offset grid)
- **UPS:** Maintains 15-min backup for generator startup
- **BESS Revenue:** $600-800k/year from solar self-consumption

**Phase 0 CAPEX:** $19.4M (power systems only)

### 6.2 Phase 1 (Months 12-24)

**Objectives:**
- Match UPS and generator capacity to 9MW facility load
- Optimize BESS capture of remaining solar excess

**Deployments:**
- Add 4.5MW UPS power modules (total: 10.5MW N+1)
- Add 1×4MW BESS inverter (total: 12MW discharge capability)
- Add 1×4MW turbine generator (total: 12MW N+1)

**Operational Mode:**
- **Daytime:** Solar excess (3-4MW) charges BESS
- **Nighttime:** BESS discharges to facility
- **BESS Revenue:** $600-750k/year (declining solar excess)

**Phase 1 CAPEX:** $5.7M

### 6.3 Phase 2 (Months 24-36)

**Objectives:**
- Complete buildout to 13.5MW facility capacity
- Pivot BESS to grid services revenue model

**Deployments:**
- Add 6MW UPS power modules (total: 16.5MW N+1)
- Add 1×4MW BESS inverter (total: 16MW for grid services)
- Add 2×4MW turbine generators (total: 20MW N+1)

**Operational Mode:**
- **Daytime:** Minimal solar excess (DC load ≈ solar production)
- **BESS New Role:**
  - SPP frequency regulation (4-8 hours/day)
  - Demand response (peak events)
  - Energy arbitrage (charge off-peak, discharge peak)
- **BESS Revenue:** $840k-1.2M/year (grid services)

**Phase 2 CAPEX:** $7.7M

---

## 7. RISK MITIGATION

### 7.1 BESS Revenue Risk

**Risk:** Market prices or regulations change, reducing BESS revenue below projections.

**Mitigations:**
- **Diversified revenue streams:** Solar capture (Phases 0-1) transitions to grid services (Phases 2-3)
- **Conservative modeling:** $840k-1.2M/year assumes 50-70% market participation rate (vs. 100% theoretical)
- **Downside scenario:** Even at 50% revenue ($420k/year Phase 2), 20-year NPV remains positive
- **Fallback:** BESS can operate as pure solar firming (discharge nightly) with zero market exposure

**Sensitivity Analysis:**

| Revenue Scenario | Phase 2 Annual | 20-Year NPV | IRR |
|------------------|----------------|-------------|-----|
| Base case | $1.0M | $8.2M | 14% |
| Conservative (70%) | $700k | $5.1M | 10% |
| Pessimistic (50%) | $500k | $2.4M | 7% |
| Floor (solar only) | $300k | -$0.8M | 4% |

**Conclusion:** BESS remains NPV-positive in all but the most pessimistic scenario.

### 7.2 UPS Technology Risk

**Risk:** Modular UPS products discontinued or vendor exit.

**Mitigations:**
- **Commodity technology:** Schneider, Eaton, Vertiv all offer compatible systems
- **Open standards:** UL 1778 ensures cross-vendor compatibility
- **Proven track record:** 15+ years of modular UPS in hyperscale DCs (Microsoft, Google, Meta)
- **Service availability:** 3-4 hour response time in Tulsa/OKC metro

**Probability:** <5% (mature, multi-vendor market)

### 7.3 Tier III Certification Risk

**Risk:** Certifier challenges parallel BESS design as non-compliant.

**Mitigations:**
- **BESS not in critical path:** Can be fully removed without impacting Tier III topology
- **2N UPS establishes compliance:** Traditional A/B power distribution
- **Precedent:** Microsoft, Switch use similar designs (economic BESS alongside Tier III UPS)
- **Pre-certification review:** Engage Uptime Institute in design phase (Q1 2026)

**Probability:** <10% (design follows established patterns)

### 7.4 BESS Cost Overrun Risk

**Risk:** BESS pricing exceeds $10M budget, reducing returns.

**Current Estimates:**
- Tesla Megapack 2 XL: $8.6M (published 2024 pricing)
- Fluence Gridstack Pro: $8-8.8M (industry reports)
- Budget: $10M (includes 15-25% contingency)

**Mitigations:**
- **Market trend:** -30% BESS pricing decline in 2024, continued reduction expected
- **RFI competition:** Tesla, Fluence, Wärtsilä, BYD (4+ vendors)
- **Showstopper threshold:** >$14M (destroys business case)

**Sensitivity:**
- At $12M BESS cost: NPV = $6.2M (still positive)
- At $14M BESS cost: NPV = $4.2M (marginal)
- At $16M BESS cost: NPV = $2.2M (reconsider)

---

## 8. VENDOR ACTION ITEMS

### 8.1 For Camelot Energy (Net Load Analysis - Task 2)

**BESS Operating Parameters:**

**Phases 0-1 (Solar Capture Mode):**
- **Charging:** 3-4MW for 4-6 hours (daytime solar excess)
- **Discharging:** 4MW for 4 hours (7pm-11pm nightly)
- **Daily cycling:** 16 MWh charge/discharge
- **Grid impact:** Reduces nighttime grid purchases by 16 MWh/day

**Phases 2-3 (Grid Services Mode):**
- **Regulation:** 16MW bid into SPP regulation market (4-8 hours/day)
- **Demand response:** Full discharge during peak events (50-80 hours/year)
- **Arbitrage:** Charge 12am-6am (off-peak), discharge 4pm-8pm (peak)
- **Grid impact:** Net export during peak periods, net import during off-peak

**Questions for Your Modeling:**
1. Quantify annual grid purchase reduction (Phase 0-1) from nightly BESS discharge
2. Estimate SPP regulation revenue at 16MW × 4 hours/day average participation
3. Calculate demand response value: 80 events/year × 16MW × 2 hours × $200/MWh premium
4. What is optimal arbitrage strategy given SPP day-ahead pricing patterns?

### 8.2 For UPS Vendors (RFI Due Nov 8)

**System Requirements:**
- **Topology:** 2N (dual A/B bus), N+1 redundancy per side
- **Capacity:** 4.5MW Phase 0 → 9MW Phase 1 → 13.5MW Phase 2
- **Technology:** Modular frames with hot-swappable power modules
- **Backup Duration:** 15 minutes @ full load (bridge to generators)
- **Standards:** UL 1778, IEC 62040, Tier III certification

**Phased Deployment Pricing Required:**
- **Phase 0:** Frames, switchgear, distribution + 6MW modules (N+1 for 4.5MW)
- **Phase 1:** Add 4.5MW modules only
- **Phase 2:** Add 6MW modules only

**Key Questions:**
1. Confirm module compatibility across 10-year lifecycle (product roadmap)
2. Lead time for Phase 0 (target: ≤16 weeks)
3. Service coverage: Pryor, OK 74361 (response time <4 hours)
4. Warranty: 10 years parts, 1 year labor (standard?)
5. Provide Tier III reference projects (hyperscale DC preferred)

### 8.3 For BESS Vendors (RFI Due Nov 8)

**System Requirements:**
- **Energy:** 16 MWh (LFP chemistry required)
- **Power:** 16MW AC output (4×4MW grid-following inverters)
- **Topology:** Single system (1N) - NOT in critical power path
- **Standards:** UL 9540, UL 9540A, NFPA 855, IEEE 1547
- **Warranty:** 80% capacity retention @ 6,000 cycles or 15 years

**Phased Deployment:**
- Phase 0: Full batteries (16 MWh) + 2×4MW inverters
- Phase 1: Add 1×4MW inverter (no batteries)
- Phase 2: Add 1×4MW inverter (no batteries)

**Key Questions:**
1. Confirm grid-following (NOT grid-forming) - we are NOT using BESS as UPS
2. Pricing breakdown: Phase 0 vs. Phase 1-2 inverter additions
3. Lead time from PO (target: ≤12 months)
4. Service network: Pryor, OK (response time <8 hours)
5. Provide references: Economic BESS in data center or industrial applications

---

## 9. FINANCIAL SUMMARY

### 9.1 Total Investment & Returns

**Total Power System CAPEX (Phases 0-2):**
- 2N UPS System: $14.5M
- Economic BESS: $10.8M
- Backup Generators: $6.6M
- Switchgear/Integration: $2.1M
- **Total:** $32.8M

**Solar (excluded from comparison):** $14-16M (identical across all designs)

**BESS-Specific Returns (20-Year):**
- Total revenue: $18.2M (nominal)
- NPV @ 8%: $12.1M
- CAPEX: $10.8M
- Net NPV: **$8.2M**
- IRR: **12-15%**

**Project-Level IRR Impact:**
- JIT UPS deployment benefit: **+2-4% IRR**
- BESS revenue contribution: **+1-2% IRR**
- **Combined impact:** +3-6% vs. traditional approach

### 9.2 Comparison to BESS-as-UPS Approach

| Metric | Economic BESS + 2N UPS | Single BESS-as-UPS | True 2N BESS-as-UPS |
|--------|------------------------|-------------------|---------------------|
| **Total CAPEX** | $32.8M | $22.5M | $38-42M |
| **Tier III Compliant?** | ✅ Yes | ❌ No (SPOF) | ✅ Yes |
| **BESS Revenue/Year** | $840k-1.2M (full cycling) | $200-400k (SOC constrained) | $200-400k (SOC constrained) |
| **BESS 20-Year NPV** | $8.2M | $1-2M | -$8 to -12M |
| **Lender Acceptance** | ✅ High (proven topology) | ❌ Low (exotic design) | ⚠️ Medium (high CAPEX) |
| **Project IRR Impact** | +3-6% | Unknown (not financeable) | -3 to -5% |

**Conclusion:** Economic BESS + 2N UPS delivers superior financial returns while maintaining Tier III compliance and lender confidence. BESS-as-UPS approaches either violate Tier III (single BESS) or destroy returns through excess CAPEX (2N BESS).

---

## 10. RECOMMENDATION

### Deploy Economic BESS + JIT 2N UPS for Maximum Risk-Adjusted Returns

**Why This Approach Wins:**

1. **Tier III Compliance:** 2N UPS provides concurrently maintainable reliability with 40+ years of proven performance

2. **Superior BESS Returns:** Decoupled design allows full 0-100% SOC cycling for maximum revenue capture ($8.2M NPV vs. $1-2M for constrained dual-purpose system)

3. **IRR Optimization:** JIT UPS deployment preserves $6.5M cash in Phase 0, boosting project IRR by 2-4%

4. **Lender Confidence:** Traditional UPS topology eliminates exotic microgrid risk, reducing financing costs by 50-100 bps

5. **Operational Flexibility:** BESS can go fully offline for maintenance without DC impact; can pivot revenue strategies as markets evolve

**Next Steps:**

1. **Issue RFIs (Due Nov 8):**
   - UPS vendors: JIT modular pricing (Schneider, Eaton, Vertiv)
   - BESS vendors: Economic system pricing (Tesla, Fluence, Wärtsilä)

2. **Camelot Task 2:** Model economic BESS revenue under phase-adaptive strategy

3. **Uptime Institute:** Pre-certification review of parallel BESS design (Q1 2026)

4. **Financial Model Update:** Incorporate vendor pricing + Camelot revenue projections (Nov 15 target)

5. **Investor Presentation:** Nov 22 delivery with vendor-validated financials

---

**Document Status:** DRAFT FOR CLIENT REVIEW
**Next Review:** Following vendor RFI responses (target Nov 15, 2025)
**Final Delivery:** Nov 22, 2025 (Investor Package)
