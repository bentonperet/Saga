**Created:** 2025-10-23 12:30

# FINANCIAL MODEL CHANGE LOG
## Saga Energy – Pryor Data Center

**Parent Document:** [[Saga Pryor DC/Basis of Design/Archive/Benton_BOD/_BOD - Exec Summary and TOC]]

---

## PURPOSE

This document tracks all design changes that require updates to the financial model. Each entry includes the change description, financial impact, and implementation status.

---

## MAJOR ARCHITECTURE CHANGES

### BESS-as-UPS Rejection (October 2025)

**Decision:** Reject BESS-as-UPS topology in favor of traditional N+1 modular UPS (dual paths)

**Technical Rationale:** [[Why BESS Should Not Be UPS]]
- Single BESS violates Tier III concurrent maintainability requirement
- Dual BESS would cost $18-22M (more expensive than traditional $11-13M N+1 UPS)
- Lacks lender acceptance and bankability for project finance

**Financial Model Updates Required:**

| Item | Old Value | New Value | Delta |
|---|---|---|---|
| UPS CAPEX (Phase 1) | $29.7-31.2M (BESS Phase 1) | $4.5M (6MW N+1 traditional UPS) | **-$25.2M to -$26.7M** |
| UPS CAPEX (Phases 2-5) | $2.8-3.5M (BESS Phase 2) | $21.8M (phased modules) | +$18.3-19.0M (but deferred) |
| UPS CAPEX (Total) | $32.5-34.7M (BESS total) | $26.3M (traditional UPS total) | **-$6.2M to -$8.4M** |
| Electrical Enclosures | N/A (BESS assumed outdoor) | Outdoor containerized (2-3 units) | +$1-2M {TBC} |
| Fire Suppression (electrical) | Included in BESS | Integrated in enclosures | +$200-400K {TBC} |
| Building Footprint Reduction | 6,000 SF indoor electrical rooms | Outdoor enclosures (no indoor space) | **-$0.9-1.5M** (6,000 SF savings) |
| **Phase 1 CAPEX Savings** | -- | -- | **-$22.7M Phase 1 cash preserved** |
| **Total CAPEX Savings** | -- | -- | **-$5.7M to -$8.9M (net)** |

**IRR Impact:**
- **Phase 1 CAPEX reduction:** -$21.8M deferred from Phase 1 to Phases 2-5
- **JIT deployment benefit:** Match UPS capacity to IT load growth, optimize cash flow timing
- **Expected IRR improvement:** TBD (awaiting financial model update)

**Implementation Status:** ✅ Design documents updated, financial model update pending

---

### Economic BESS Rejection (October 2025)

**Decision:** Reject Economic BESS (separate from UPS) due to deeply negative NPV

**Financial Analysis:** [[Excess Solar Monetization Strategy]]
- **NPV:** -$5.3M to -$6.2M over 20 years
- **Root Cause:** $10.8M CAPEX cannot be recovered from limited Phase 1-2 revenue window (2 years, $1.8M PV) combined with generator-competed Phase 3-20 revenue

**Financial Model Updates Required:**

| Item | Old Value (with BESS) | New Value (without BESS) | Delta |
|---|---|---|---|
| Economic BESS CAPEX | $10.8M | $0 | **-$10.8M** |
| BESS fire suppression | $150-300K | $0 | **-$150-300K** |
| Advanced microgrid controller | $1.05-1.55M | $0 | **-$1.05-1.55M** |
| Simplified EMS | $0 | $200-400K | +$200-400K |
| Substation transformer | 20-25 MVA ($500K-1M) | 15-20 MVA ($400-800K) | **-$100-200K** |
| **Total CAPEX Avoidance** | -- | -- | **-$11.9M to -$12.9M** |
| **NPV Impact** | -$5.3M to -$6.2M (BESS) | $0 (no BESS) | **+$5.3M to +$6.2M** |

**Revenue Impact:**
- **Lost BESS Revenue:** Phase 1-2 solar arbitrage ($1.8M PV over 2 years)
- **Maintained Revenue:** Generator demand response ($600k/year via OG&E Load Reduction Program)
- **Net Revenue Change:** -$1.8M PV over project life (but avoids -$5.3M to -$6.2M NPV)

**Implementation Status:** ✅ Design documents updated, financial model update pending

---

## CAPACITY & PHASING CHANGES

### IT Load Increase (October 2025)

**Change:** Initial IT load increased from 7.4 MW to 12 MW

**Financial Model Updates Required:**

| Item | Old Value | New Value | Delta |
|---|---|---|---|
| Initial IT Load | 7.4 MW | 12 MW | +4.6 MW (+62%) |
| White Space (total) | 25,000 SF | 40,000 SF | +15,000 SF (+60%) |
| Phase 1 Fit-Out | 25,000 SF | 20,000 SF | -5,000 SF |
| Phase 2 Shell | 0 SF | 20,000 SF | +20,000 SF |
| Facility Load (PUE 1.2-1.3) | ~9 MW | ~15 MW | +6 MW |
| Substation Transformer | 15-20 MVA | 15-20 MVA | No change (without BESS) |

**Revenue Impact:**
- **Increased leasable capacity:** +4.6 MW IT load (+62% revenue potential)
- **Phased deployment flexibility:** Phase 2 shell space allows JIT fit-out as leased

**CAPEX Impact:**
- **Building envelope:** 40,000 SF (+15,000 SF @ $150-250/SF tornado premium) = +$2.25-3.75M
- **MEP systems:** Phased deployment reduces Phase 1 CAPEX (fit-out only 20,000 SF initially)

**Implementation Status:** ✅ Design documents updated, financial model update pending

---

## COOLING SYSTEM CHANGES

### Expanded Chiller Plant

**Change:** ~3 chillers (RD109 baseline) → ~16 chillers (1.5 MW each in modular 3 MW blocks)

**Rationale:**
- Support 12 MW initial load (vs 7.4 MW original)
- Modular 3 MW blocks align with customer flexibility strategy
- N+1 redundancy within each 3 MW block (3 chillers per block)

**Financial Model Updates Required:**

| Item | Old Value | New Value | Delta |
|---|---|---|---|
| Chiller Count | ~3 chillers | ~16 chillers | +13 chillers |
| Chiller Capacity | ~5 MW each | ~1.5 MW each | -- |
| Chiller Plant CAPEX | TBD | ~$8-12M (phased) | +$5-9M (estimate) |
| Chiller Yard Area | ~500 SF | ~2,000-2,500 SF | +1,500-2,000 SF |

**Implementation Status:** ✅ Design documents updated, financial model update pending

---

## GENERATOR STRATEGY CHANGES

### Generator Fuel Strategy (October 2025)

**Change:** Decision-based approach replaces single diesel strategy

**Rationale:**
- **Option A (Grid Day 1):** Diesel generators - lower CAPEX, rare runtime
- **Option B (No Grid Day 1):** Natural gas turbine - unlimited fuel for nightly operation
- **Decision Driver:** Grid availability at facility opening
- **Cost Analysis:** See [[Diesel vs NatGas Generator CAPEX]]

**Financial Model Updates Required:**

| Item | Option A (Diesel) | Option B (Nat Gas) | Delta vs Baseline |
|---|---|---|---|
| Generator Type | Diesel recip | NG turbines | -- |
| Generator Count | 5-6 units | 2-3 turbines + 1 diesel | -- |
| Generator CAPEX | ~$10-11M | ~$9-10M | Variable |
| Fuel Infrastructure | Diesel belly tanks/AST | NG pipeline connection | +$100-300K (Option B) |
| OPEX (fuel) | Higher $/runtime hr | Lower $/runtime hr | Depends on runtime |

**Implementation Status:** ✅ Design documents updated, financial model update pending

---

## RENEWABLE ENERGY CHANGES

### Solar Array Sizing (No Change)

**Status:** 12 MW DC solar array maintained from original design

**Configuration Changes:**
- Behind-the-meter (BTM) single POI confirmed
- No BESS for storage (60-80% renewable penetration without storage via direct consumption)

**Financial Model Updates Required:**

| Item | Old Value | New Value | Delta |
|---|---|---|---|
| Solar Capacity | 12 MW DC | 12 MW DC | No change |
| Annual Generation | 19-24 GWh/year | 19-24 GWh/year | No change |
| Renewable Penetration | 60-80% (with BESS) | 60-80% (without BESS) | No change |
| Solar CAPEX | ~$12-15M | ~$12-15M | No change |

**Revenue Impact:**
- **Phase 1-2 excess solar:** ~$1.8M PV over 2 years (lost without BESS)
- **Alternate monetization:** Mobile edge computing ($4.7-7.5M NPV) or direct grid export ($0.8-1.5M NPV)
- **Recommendation:** Pursue mobile edge computing if utility interconnection study confirms feasibility

**Implementation Status:** ✅ Design documents updated, financial model update pending

---

## ELECTRICAL DISTRIBUTION CHANGES

### JIT UPS Deployment Strategy (October 2025)

**Change:** Upfront full UPS deployment → Phased JIT deployment aligned with IT load growth

**Financial Model Updates Required:**

| Phase | Facility Load | UPS Capacity | UPS CAPEX | Cumulative CAPEX |
|---|---|---|---|---|
| **1** | 4.0-4.3 MW | 6MW (N+1) | $4.5M | $4.5M |
| **2** | 8.0-8.5 MW | Add 4MW modules | $3.0M | $7.5M |
| **3** | 12.0-12.8 MW | Add 5MW modules | $3.8M | $11.3M |
| **4** | 16.0-17.0 MW | Add 6MW modules | $4.5M | $15.8M |
| **5** | 27.0-28.4 MW | Add 14MW modules | $10.5M | $26.3M |

**IRR Impact:**
- **Phase 1 CAPEX:** $4.5M (vs $29.7-31.2M BESS Phase 1)
- **Cash flow optimization:** UPS CAPEX deferred until IT load (and revenue) materializes
- **Expected IRR improvement:** TBD (awaiting financial model update)

**Implementation Status:** ✅ Design documents updated, financial model update pending

---

## OUTSTANDING FINANCIAL MODEL DECISIONS

| Decision | Target Date | Financial Impact |
|---|---|---|
| Single-story vs two-story building | Nov 2025 | CAPEX ±$2-4M, footprint implications |
| UPS vendor selection | Nov 2025 | CAPEX ±$500K-1M, O&M cost differences |
| Final generator count (turbine + diesel mix) | Nov 2025 | CAPEX ±$500K-1M |
| Excess solar monetization strategy | Nov 2025 | Revenue $0.8-7.5M NPV (mobile edge vs export) |

---

## SUMMARY OF NET FINANCIAL IMPACTS

### Phase 1 CAPEX Changes

| Category | Change | Amount |
|---|---|---|
| UPS (BESS → traditional) | Phase 1 savings | **-$21.8M** |
| Economic BESS elimination | CAPEX avoidance | **-$10.8M** |
| Advanced EMS elimination | CAPEX avoidance | **-$0.85-1.15M** |
| Simplified EMS addition | New requirement | +$0.2-0.4M |
| Electrical enclosures | Outdoor containerized | +$1-2M {TBC} |
| Building footprint reduction | Outdoor vs indoor electrical | **-$0.9-1.5M** |
| Fire suppression (electrical) | Integrated in enclosures | +$0.2-0.4M {TBC} |
| Expanded chiller plant | +13 chillers | +$5-9M (estimate) |
| Larger building envelope | +15,000 SF | +$2.25-3.75M |
| Generator expansion | +1-2 units | +$0.8-1.8M |
| Natural gas service | New requirement | +$0.1-0.3M |
| Substation transformer | Smaller sizing | **-$0.1-0.2M** |
| **Total Phase 1 CAPEX Delta** | -- | **-$23M to -$29M (net savings)** |

### Total Project CAPEX Changes (All Phases)

| Category | Change | Amount |
|---|---|---|
| UPS (total all phases) | BESS → traditional | **-$6.2M to -$8.4M** |
| Economic BESS elimination | Total avoidance | **-$11.9M to -$12.9M** |
| Electrical enclosures | Outdoor vs indoor | **-$0.7M to -$1.3M** (net savings) |
| Other systems (net) | Chillers, generators, building | +$9-16M (estimate) |
| **Total Project CAPEX Delta** | -- | **-$9M to -$13M (net savings)** |

### NPV Changes

| Category | Change | Amount |
|---|---|---|
| Economic BESS NPV avoidance | Avoid negative NPV | **+$5.3M to +$6.2M** |
| Lost solar arbitrage revenue | Phase 1-2 window | -$1.8M PV |
| Demand response (generators) | Maintained revenue | $600k/year |
| **Net NPV Impact** | -- | **+$3.5M to +$4.4M** |

---

**Tags:** #saga-project #financial-model #capex #npv #irr #bess-rejection

**Next Steps:**
1. Update financial model with all CAPEX changes
2. Recalculate IRR based on JIT UPS deployment and deferred CAPEX
3. Model excess solar monetization scenarios (mobile edge computing vs direct export)
4. Validate generator demand response revenue assumptions with OG&E
5. Update proforma with revised CAPEX phasing schedule
