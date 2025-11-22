**Created:** 2025-10-21

# BESS as UPS Replacement Strategy
## 10-12MW Data Center Design Memo

**Saga Energy Pryor Data Center**

**Document Purpose:** Demonstrate that BESS sized for solar excess capture eliminates traditional UPS requirements, saving $11-15M in CAPEX while providing superior backup duration (~1 hours vs. 15 minutes).

**Prepared By:** PACHYDERM GLOBAL / PGCIS
**Prepared For:** Saga Energy (Executives, Vendors, Lenders)
**Date:** 2025-10-21
**Status:** DRAFT FOR CLIENT REVIEW

**Related Documents:**
- [[Part 1 - Solar-First Startup Strategy - BAD]] - Solar integration and phased deployment
- [[Technical Addendum - BESS Implementation Details - FALSE]] - Detailed specifications

**Tags:** #saga-project #bess-as-ups #cost-savings #grid-forming-inverters #client-deliverable

---

## EXECUTIVE SUMMARY

### Bottom Line
**BESS sized for solar excess capture eliminates the need for traditional UPS, saving $11-14M in CAPEX and enabling use of lower-cost turbine generators.**

### Key Findings

| Dimension       | Finding                                                                                           | Impact                                     |
| --------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| **Financial**   | Eliminate UPS system entirely ($11-13M)                                                           | **Primary savings source**                 |
| **Financial**   | If no grid connection for first 3MW, use turbine generators vs. faster diesel ($1M+ fuel savings) | **BESS allows large  startup window**      |
| **Technical**   | Grid-forming BESS meets all data center power quality standards                                   | **<50ms response, proven in production**   |
| **Operational** | 1+ hours backup vs. 15 minutes (UPS)                                                              | **4× safety margin for generator startup** |
| **Strategic**   | Single BESS serves dual purpose (solar storage + UPS)                                             | **Simpler, more efficient operations**     |

### The Core Value Proposition

**Traditional Approach:**
- Install separate UPS system for backup power: **$11-13M**
- Use fast-start diesel generators (10-15 min startup): **Higher cost**
- BESS sized for solar excess capture: **Similar to our approach**

**BESS-as-UPS Approach:**
- Grid-forming BESS sized for solar excess capture and UPS capabilities
- **No separate UPS needed: Save $11-13M**
- Longer backup window allows turbine generators: Save $1-2M
- Advanced microgrid controls needed: +$0.7M (vs. basic controls in traditional)

**Net Savings: $11-15M** (UPS elimination + turbine generators - advanced controls)
### Confidence Assessment

| Component                 | Estimate | Confidence | Path to 80%+                                                                 |
| ------------------------- | -------- | ---------- | ---------------------------------------------------------------------------- |
| **BESS (16 MWh)**         | $7-10M   | **65%**    | Published pricing: Tesla Megapack $540/kWh, Fluence $500-550/kWh (2024-2025) |
| **UPS Elimination**       | -$11-13M | **80%** ✅  | Industry standard: $700-800/kW for 16MW UPS                                  |
| **Turbine Generators**    | -$1-2M   | **70%**    | Turbines and natural gas fuel much cheaper than diesel                       |
| **Technical Feasibility** | Proven   | **85%** ✅  | Microsoft, X.ai, Switch, Quantum Loophole validate                           |
| **Net Savings**           | $11-15M  | **75%** ✅  | UPS pricing solid; generator delta needs RFI validation                      |

**BESS Cost Validation (without RFI):**
- Tesla Megapack 2 XL: $540/kWh list price (2024) → 16 MWh = $8.6M
- Fluence Gridstack Pro: $500-550/kWh (industry reports 2025) → 16 MWh = $8-8.8M
- Market trend: -30% pricing decline in 2024, continued decline expected


---

## 1. DESIGN RATIONALE

### 1.1 Why BESS Replaces Traditional UPS

Modern grid-forming BESS inverters perform ALL traditional UPS functions:

| Function             | Traditional UPS | Grid-Forming BESS         | Validation            |
| -------------------- | --------------- | ------------------------- | --------------------- |
| Voltage regulation   | ±1%             | ±1% (ANSI C84.1)          | **Equivalent**        |
| Frequency regulation | ±0.1 Hz         | ±0.1 Hz (IEEE 1547)       | **Equivalent**        |
| Response time        | 0-4ms           | <50ms (within ITIC curve) | **Acceptable for IT** |
| Harmonic distortion  | <3% THD         | <5% THD (IEEE 519)        | **Meets standards**   |
| Backup duration      | 5-15 minutes    | **1 hour**                | **4× longer**         |
| Transfer time        | 0ms (always on) |  0ms (grid-forming)       | **No transfer**       |

**Critical Insight:** Grid-forming BESS operates continuously as the power source—it doesn't "switch" during outages. There is zero transfer time because the BESS *is* the source.

## 2. BESS SIZING & COST COMPARISON

### 2.1 System Specifications

**Data Center:**
- IT Load: 10MW (full buildout)
- Facility Load: 4.5MW → 8MW → 13.5MW (phased growth)
- PUE: 1.35 average, 1.42 peak

**Power Systems:**
- **Solar:** 12MW array (63 MWh/day production)
- **BESS:** 16 MWh with grid-forming inverters
- **Generators:** 5×4MW natural gas turbines (phased deployment) or potentially diesel generators - TBD

### 2.2 Why 16 MWh BESS is Optimal

**The Sizing Challenge:** As the data center grows, solar excess changes dramatically:

| Phase | IT Load | Facility Load | Solar Excess Available | BESS Captures | Backup Duration |
|-------|---------|---------------|----------------------|---------------|-----------------|
| **0** | 3MW | 4.5MW | 18-25 MWh/day | 65-90% (16 MWh) | 3.5 hours |
| **1** | 6MW | 8MW | 12-16 MWh/day | 100% (16 MWh) | 2.0 hours |
| **2** | 10MW | 13.5MW | 3-8 MWh/day | 100% (16 MWh) | 1.2 hours |

**Why 16 MWh Works Across All Phases:**
1. **Phase 1 (4.5MW facility):** Captures most solar excess without oversizing for capacity that becomes obsolete
2. **Phase 2 (8MW facility):** Sweet spot - captures 100% of available solar excess
3. **Phase 3 (13.5MW facility):** Minimal solar excess, but BESS provides 1.2 hours backup (4× turbine startup time)

**What We're NOT Doing:**
- **Oversizing to 25-30 MWh** for Phase 1 → Wastes $4-7M on capacity unused in Phases 1-2
- **Undersizing to 10 MWh** → Misses 40-50% of solar value in early phases

**ROI Advantage:** Lower CAPEX ($8M for 16 MWh) vs. oversizing for early phase solar capture ($12-15M for 25-30 MWh).

### 2.3 BESS-as-UPS System Costs (Phased Deployment)

**Our System Costs:**

| Component | Phase 0 | Phase 1 | Phase 2 | Notes |
|-----------|---------|---------|---------|-------|
| **BESS** | $8M (16 MWh + 2×4MW inv) | +$1M (add 1×4MW inv) | +$1M (add 1×4MW inv) | **Battery capacity constant**, inverters scale |
| **Advanced Controls** | $1.5M | - | - | IEEE 2030.7/8 microgrid |
| **Fire Safety** | $2M | - | - | NFPA 855 for 4 containers |
| **Switchgear** | $1M | - | - | BESS inverter integration |
| **Turbine Generators** | $2.5M (2×4MW) | +$1.5M (1×4MW) | +$2M (2×4MW) | Natural gas, 20-30min startup |
| **TOTAL** | **$15M** | **+$2.5M** | **+$3M** | **Cumulative: $20.5M** |

**Grid-Forming BESS Premium:**
A traditional BESS (same 16 MWh, grid-following) would require the same batteries, inverters, fire safety, and switchgear. The only incremental cost for grid-forming capability is:
- **Advanced Controls:** $1.5M vs. $0.8M basic = **+$0.7M premium**

This $0.7M premium enables UPS replacement, saving $11-13M.

### 2.4 UPS Savings by Phase

**Traditional UPS System Costs (What We're Avoiding):**

| Phase | Facility Load | Traditional UPS Cost (Cumulative) |
|-------|---------------|-----------------------------------|
| **0** | 4.5MW | $3.5-4M |
| **1** | 8MW | $6-7M |
| **2** | 13.5MW | $11-13M |

**Additional Savings:**
- **Turbine generators** (vs. diesel): -$1-2M (slower startup OK with 1.2hr backup)
- **Switchgear simplification:** -$1M (no UPS layer complexity) - however, we'll provide line diagram details with space to at UPS units to meet customer demands, if they require them. This will reduce these savings some, and we've removed from net savings below.

**Net Savings at Phase 2:** ~$11-15M
- UPS elimination: $11-13M
- Turbine vs. diesel: $1-2M (verification required)
- Less: Microgrid premium: -$0.7M
- **Total: $11.3-14.3M savings**

### 2.5 Key Takeaways

**16 MWh BESS Optimizes Across Growth:**
- Right-sized for Phase 1 sweet spot (100% solar capture)
- Acceptable capture in Phase 0 (65-90%) without expensive oversizing
- Provides adequate UPS backup in Phase 2 (1.2 hours = 4× generator startup time)
- Lower upfront CAPEX enables better project IRR

**Grid-Forming BESS Saves $11-15M:**
- Eliminates $11-13M traditional UPS system
- Enables cheaper turbine generators (+$1-2M savings)
- Simplifies switchgear (+$1M savings)
- Only $0.7M premium for grid-forming controls
- **Net savings: $11-14M** with superior backup duration (1hr vs. 15min)


---

## 3. CRITICAL INFORMATION FOR VENDORS

### 3.1 For Camelot Energy (Net Load Analysis - Task 2)

**⚠️ CRITICAL:** BESS operates in **dual-purpose mode**—this MUST be reflected in your net load modeling.

**Daytime Operation (Solar Excess Capture):**
- Solar generation: 12MW
- Facility load: 13.5MW (average across phases, varies by season) - ****assuming grid power is available
- **BESS charging:** Varies by phase - 0-3MW for 4-8 hours (3-16 MWh/day depending on facility load)
- **Purpose:** Capture solar excess during early phases when DC load is ramping up, and store energy for nighttime discharge. The 1-hour backup capacity provides sufficient buffer time for turbine generators (20-30 min startup) during grid outages. *Or plenty of time for diesel if market research required onsite diesel as an alternate backup fuel.*

**Night/Outage Operation (UPS Function):**
- Facility load: 13.5-14.2MW (varies by season, PUE 1.35-1.42)
- **BESS discharging:** 13.5MW for 1.2 hours
- **Purpose:** Provide UPS-equivalent backup until grid use or generators start (if early phases are behind-the-meter)

**Implications for Your Analysis:**
1. **Revenue Opportunity:** BESS cannot participate in SPP markets during UPS duty (must maintain 90-100% SOC for reliability)
2. **Load Coverage:** Model shows BESS covering 1+ hours of full facility load

**Questions for Your Modeling:**
- Can you quantify revenue opportunity if BESS participates in SPP markets during grid-connected Phase 1+? Also assume we'll have generation capability.
- What's the optimal SOC strategy to balance revenue generation potential vs. backup reliability?

### 3.2 For BESS Vendors (RFI Due Oct 25)

**System Requirements:**
- **Energy:** 16 MWh (LFP chemistry required)
- **Power:** 16MW AC output (4×4MW inverters, phased deployment)
- **Inverter Type:** **Grid-forming (NOT grid-following)** - CRITICAL for UPS replacement
- **Redundancy:** N+1 configuration (lose 1 inverter, maintain operation)
- **Standards:** UL 9540, UL 9540A, NFPA 855, IEEE 2030.7/8
- **Response Time:** <50ms (ITIC compliant)

**Phased Deployment:**
- Phase 0: Full batteries (16 MWh) + 2×4MW inverters
- Phase 1: Add 1×4MW inverter only (NO additional batteries)
- Phase 2: Add 1×4MW inverter only (NO additional batteries)

**Key Questions:**
1. Confirm grid-forming inverter capability (spec sheet + data center references)
2. Pricing for phased deployment (separate Phase 0, Phase 1, Phase 2 costs)
3. Lead time from PO (target: ≤12 months)
4. Service network coverage (Pryor, OK 74361 - response time <4 hours)
5. Warranty: 80% capacity retention at 6,000 cycles or 15 years

---

## 4. RISK MITIGATION & NEXT STEPS

### 4.1 Top 3 Risks

**Risk 1: BESS Costs Exceed Estimates (65% confidence)**
- **Impact:** Savings reduced but still significant
- **Mitigation:** Published pricing validates $7-10M range; Tesla $8.6M, Fluence $8-8.8M; RFI confirms final pricing
- **Showstopper:** >$13M for 16 MWh BESS (destroys business case)

**Risk 2: Lender/Insurance Skepticism**
- **Impact:** Project financing delayed
- **Mitigation:** Independent engineering review (Schneider, Black & Veatch); reference projects (Microsoft, Switch, Quantum Loophole)
- **Fallback:** Add small $0.2M UPS as "safety net" (still save $11M+)

**Risk 3: BESS Lead Time >12 Months**
- **Impact:** Revenue delayed, financing costs increase
- **Mitigation:** Order by Q1 2026; include liquidated damages; Tesla 15-18mo, Fluence/Wärtsilä faster

### 4.2 Immediate Actions (Critical Path)

**This Week (Oct 21-25):**
1. **Issue BESS RFI** to Tesla, Fluence, Wärtsilä (16 MWh, grid-forming, N+1) - Target: ≤$10M
2. **Confirm with Camelot:** Task 2 must model dual-purpose BESS operation (solar capture + UPS function)

**Next Week (Oct 27-Nov 1):**
4. **Update financial models** with vendor-validated costs
5. **Prepare investor presentation** (exec summary, cost comparison, risk matrix)


---

## APPENDIX: QUICK REFERENCE

### Phased Deployment (3MW IT Blocks)

| Phase | IT Load | Facility Load | BESS | Inverters | Generators (Turbine) | Backup Duration | Backup CAPEX |
|-------|---------|---------------|------|-----------|---------------------|-----------------|--------------|
| **0** | 3.3MW | 4.5MW | 16 MWh | 2×4MW | 2×4MW | 3.5 hrs | $14-17M |
| **1** | 6.6MW | 9MW | 16 MWh | 3×4MW | 3×4MW | 1.8 hrs | $16-19.5M |
| **2** | 10MW | 13.5MW | 16 MWh | 4×4MW | 5×4MW | 1.2 hrs | $19-23.5M |

**Note:** Backup CAPEX includes BESS, turbine generators, advanced controls, fire safety, and switchgear. Solar costs ($14-16M) are excluded as they are identical in both traditional and BESS-as-UPS approaches.
****This is one option, we still need to consider diesel generation for various reasons

---

**Document Status:** DRAFT FOR CLIENT REVIEW
**Next Review:** Following vendor RFI responses (target Nov 1, 2025)
**Final Delivery:** Nov 7, 2025 (Investor Package)
