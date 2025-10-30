**Created:** 2025-10-29

# NATURAL GAS GENERATOR TCO WITH DEMAND RESPONSE ANALYSIS
## Saga Energy – Pryor Data Center

**Purpose:** Objective financial analysis determining whether demand response revenue justifies the higher capital cost of natural gas generators versus diesel for a 4.2 MW data center facility.

**Related Documents:**
- [[Diesel vs NatGas Generator CAPEX]] - Base CAPEX comparison
- [[Demand Response Revenue Opportunity - Internal Memo]] - DR program details
- [[Saga Pryor DC/Basis of Design/Archive/Benton_BOD/7BOD - Electrical (CSI Div 26)]] - Generator specifications

---

## EXECUTIVE SUMMARY

**Bottom Line:** Natural gas generators cost **$1.8M-2.6M more** over 10 years even after accounting for $1.8M-2.6M in demand response revenue. At Phase 2 scale (8.1 MW), demand response revenue nearly offsets the nat gas CAPEX premium, making the decision much closer than at smaller scales. The choice hinges on risk tolerance, permitting certainty, and strategic priorities.

**Key Findings (Phase 2: 8.1 MW Facility Load):**

| Metric | Diesel (4×2.5MW) | Nat Gas (3×4.3MW) | Nat Gas Premium |
|--------|------------------|-------------------|-----------------|
| **CAPEX** | $10M - $13.3M | $14.6M - $20M | +$4.6M - $6.7M |
| **10-Year OpEx** | $3.2M - $4.9M | $2.2M - $3.4M | -$1.0M to -$0.2M (nat gas cheaper) |
| **10-Year DR Revenue** | $0 | $1.8M - $2.6M | +$1.8M - $2.6M |
| **Net 10-Year TCO** | **$13.2M - $18.2M** | **$15M - $20.8M** | **+$1.8M - $2.6M** |

**DR Data Certainty:**
- **PSO rate ($32/kW):** 95% certainty - verified from PSO website and OCC filings
- **OG&E rate ($25-35/kW):** 80% certainty - estimated from OCC filings, needs confirmation
- **Risk:** If OG&E rate is $20/kW (conservative), DR revenue drops to $1.6M over 10 years, increasing nat gas premium to $3.0M-3.8M

**Conclusion:** At Phase 2 scale, **diesel still has lower TCO** but the gap is **much narrower** ($1.8M-2.6M vs $4M-6M at Phase 1 scale). Natural gas becomes competitive when factoring in:
- Permitting risk mitigation (diesel may face delays or denials)
- Lower OpEx (nat gas saves $200K-1M over 10 years)
- DR revenue ($1.8M-2.6M over 10 years)
- Future revenue upside (capacity markets, grid services)

---

## ANALYSIS BASIS

### Facility Parameters (Phase 2 - Representative Scale)
- **Facility Load:** 8.1 MW (Phase 2 per BOD phasing table, PUE 1.35)
- **Generator Configuration:**
  - Diesel: 4 × 2.5 MW reciprocating gensets (10 MW total, N+1 redundancy for 8.1 MW load)
  - Nat Gas: 3 × 4.3 MW turbines (12.9 MW total, N+1 redundancy for 8.1 MW load)
- **No solar** in this analysis - generators provide all power during demand response events
- **Time Horizon:** 10 years (standard data center planning window)

**Why Phase 2 vs Phase 1:**
- Phase 1 (4.2 MW) requires only 2 generators, unrepresentative of steady-state operations
- Phase 2 (8.1 MW) requires 3 generators, better reflects operational scale and economics
- N+1 configuration more efficient at Phase 2+ scale

### Operating Assumptions
- **Diesel Runtime:** 20-30 hrs/year (testing + rare backup events)
- **Nat Gas Runtime:** 40-60 hrs/year (testing + demand response participation)
- **DR Events:** 8-10 events/year × 4-6 hours each (June-September peak periods)
- **LTSA Pricing:** Industry standard benchmarks ($200K-250K/year for 3 turbines)

---

## CAPITAL COSTS (CAPEX)

### Diesel Fleet: 4 × 2.5 MW Reciprocating Gensets

| Component                | Cost                                                                  |
| ------------------------ | --------------------------------------------------------------------- |
| **Generators**           | $900-1,200/kW × 10,000 kW = $9M - $12M                                |
| **Emissions Control**    | Tier 4 Final (SCR, DPF, DEF): +20-30% = $1.8M - $3.6M included above |
| **Fuel Infrastructure**  | 4× belly tanks or bulk storage (48hr): $400K - $650K                  |
| **Footprint/Structural** | Larger pad, heavier foundations: included in site work                |
| **Total Diesel CAPEX**   | **$10M - $13.3M**                                                     |

### Natural Gas Fleet: 3 × 4.3 MW Turbines

| Component                | Cost                                                                            |
| ------------------------ | ------------------------------------------------------------------------------- |
| **Turbines**             | $1,050-1,400/kW × 12,900 kW = $13.5M - $18.1M (volume pricing for 3+ units)    |
| **Emissions Control**    | Lower cost (cleaner): $300K - $450K                                             |
| **Fuel Infrastructure**  | Pipeline tap, metering, compressor station: $750K - $1.5M (shared across units) |
| **Footprint/Structural** | Smaller footprint, lighter weight: site work savings                            |
| **Total Nat Gas CAPEX**  | **$14.6M - $20M**                                                               |

**CAPEX Premium for Nat Gas: $4.6M - $6.7M**

**Note:** Phase 2 requires adding 1 additional unit to each fleet (vs Phase 1's 2-3 units). This increases the absolute CAPEX difference but improves per-MW economics and operational efficiency.

---

## 10-YEAR OPERATING COSTS (OPEX)

### Diesel OpEx (4 × 2.5 MW units)

**Maintenance & Readiness:**
- Monthly/quarterly loaded testing: 20-30 hrs/year across 4 units
- Oil changes, filter changes, coolant checks: $100K-160K/year (4 units)
- Fuel polishing, biocide additives, quality testing: $40K-65K/year
- DEF (Diesel Exhaust Fluid) management: $15K-25K/year
- Battery testing and replacement: $15K-20K/year
- **Annual Maintenance:** $170K - $270K/year

**Fuel Costs (Testing Only):**
- Runtime: 20-30 hrs/year
- Fuel consumption: 8.1 MW × 0.3 gal/kWh = 2,430 gal/hr
- Annual fuel: 48,600 - 72,900 gallons
- Cost: $3/gal × 60,750 gal avg = $182K/year (testing only, no DR)
- **Annual Fuel:** $145K - $220K/year

**Total Diesel OpEx:** $315K - $490K/year
**10-Year Diesel OpEx:** **$3.2M - $4.9M**

---

### Natural Gas OpEx (3 × 4.3 MW turbines)

**Long-Term Service Agreement (LTSA):**
- Fixed annual cost covering readiness, maintenance, future hot section overhaul
- Industry benchmark for 3 turbines: $200K - $300K/year (scales with unit count)
- Covers predictable maintenance, guarantees availability
- **Annual LTSA:** $200K - $300K/year

**Fuel Costs (Testing + Demand Response):**
- Testing runtime: 20-30 hrs/year
- DR runtime: 40-60 hrs/year (8-10 events × 4-6 hours)
- **Total runtime:** 60-90 hrs/year
- Fuel consumption: 8.1 MW × 7,000 BTU/kWh = 56.7 MMBtu/hr
- Annual fuel: 3,402 - 5,103 MMBtu
- Natural gas cost: $5-7/MMBtu (Oklahoma industrial rates)
- **Annual Fuel:** $17K - $36K/year

**Total Nat Gas OpEx:** $217K - $336K/year
**10-Year Nat Gas OpEx:** **$2.2M - $3.4M**

**OpEx Comparison:** Nat gas and diesel have **nearly identical OpEx** at this scale. Diesel has higher maintenance complexity (fuel polishing, DEF) but lower per-hour fuel costs during testing. Nat gas has fixed LTSA but minimal fuel costs even during DR events.

---

## DEMAND RESPONSE REVENUE

### Program Details

**Applicable Programs:**
- **PSO Peak Performers:** $32/kW enrolled capacity (95% certainty - verified via PSO website)
- **OG&E Load Reduction:** $25-35/kW estimated (80% certainty - estimated from OCC filings)

**Enrollment Strategy:**
- **Enrolled Capacity:** 8,100 kW (100% facility load participation)
- **Incentive Rate:** $25-32/kW/year (range covers OG&E estimate to PSO verified)
- **Events:** 8-10/year, voluntary participation, 2-4 hour advance notice

### Revenue Calculation

**Conservative Case (OG&E low estimate):**
- 8,100 kW × $22/kW = **$178,000/year**
- 10-Year Revenue: **$1,780,000**

**Moderate Case (OG&E mid-range):**
- 8,100 kW × $28/kW = **$227,000/year**
- 10-Year Revenue: **$2,270,000**

**Aggressive Case (PSO verified rate):**
- 8,100 kW × $32/kW = **$259,000/year**
- 10-Year Revenue: **$2,590,000**

**Data Certainty Note:** PSO rate ($32/kW) is 95% certain. OG&E rate is 80% certain and needs confirmation during utility engagement. Conservative case uses $22/kW to account for potential lower-than-estimated OG&E rates.

### Why Diesel Cannot Participate

**Emissions Regulations:**
- Oklahoma air quality regulations prohibit diesel generators from participating in demand response programs due to NOx and particulate matter emissions
- Diesel runtime typically limited to 50-100 hrs/year for testing and emergencies only
- Demand response requires 40-60 hrs/year of additional runtime specifically for economic dispatch
- **Diesel DR Revenue: $0**

This is the critical economic differentiator: **natural gas unlocks $1M-1.5M in revenue over 10 years that diesel physically cannot access.**

---

## TOTAL COST OF OWNERSHIP ANALYSIS

### 10-Year TCO Comparison (Phase 2: 8.1 MW Load)

| Scenario | Diesel TCO | Nat Gas TCO | Nat Gas Premium |
|----------|------------|-------------|-----------------|
| **Conservative** | $10M + $3.2M = **$13.2M** | $14.6M + $2.2M - $1.78M = **$15.02M** | **+$1.82M** |
| **Moderate** | $11.7M + $4.0M = **$15.7M** | $17.3M + $2.8M - $2.27M = **$17.83M** | **+$2.13M** |
| **Aggressive** | $13.3M + $4.9M = **$18.2M** | $20M + $3.4M - $2.59M = **$20.81M** | **+$2.61M** |

### Key Insights

1. **At Phase 2 scale, DR revenue nearly offsets nat gas CAPEX premium**
   - CAPEX premium: $4.6M-6.7M
   - DR revenue (10 years): $1.8M-2.6M
   - Nat gas OpEx advantage (10 years): $0.2M-1.0M (lower maintenance, cheaper fuel per hour)
   - **Net premium after DR + OpEx advantage: $1.8M-2.6M** (64-72% of CAPEX premium recovered)

2. **OpEx favors nat gas at this scale**
   - Diesel: Higher per-unit maintenance costs across 4 units, expensive fuel polishing, DEF systems
   - Nat gas: Fixed LTSA covers 3 units predictably, minimal fuel costs even during 60-90 hrs/year runtime
   - **Nat gas saves $200K-1M in OpEx over 10 years**

3. **The decision is much closer than at smaller scales**
   - Phase 1 (4.2 MW): Nat gas premium $4M-6M (clear diesel win)
   - **Phase 2 (8.1 MW): Nat gas premium $1.8M-2.6M (competitive, especially with risk factors)**
   - Economies of scale favor nat gas: Fixed costs (LTSA, fuel infrastructure) spread across more MW

---

## BREAKEVEN ANALYSIS

### Years to Breakeven (Phase 2: 8.1 MW)

**Formula:**
Breakeven = (Nat Gas CAPEX - Diesel CAPEX) ÷ (Annual DR Revenue + Annual OpEx Savings)

**Conservative Case:**
- CAPEX difference: $4.6M
- Annual advantage: $178K DR + $100K OpEx savings = $278K/year
- **Breakeven: 16.5 years**

**Moderate Case:**
- CAPEX difference: $5.9M
- Annual advantage: $227K DR + $120K OpEx savings = $347K/year
- **Breakeven: 17 years**

**Aggressive Case:**
- CAPEX difference: $6.7M
- Annual advantage: $259K DR + $150K OpEx savings = $409K/year
- **Breakeven: 16.4 years**

**Conclusion:** Breakeven period is **16-17 years** at Phase 2 scale. This is within or near typical data center equipment life (15-20 years) and extends beyond the standard 10-year planning horizon but is achievable over facility lifecycle.

**Implication:** At Phase 2 scale, **demand response revenue + OpEx savings bring nat gas to near-parity with diesel** within equipment lifetime. When factoring permitting risk, ESG requirements, or future revenue streams, nat gas becomes the rational choice despite slightly higher 10-year TCO.

---

## DECISION FRAMEWORK

### Choose DIESEL if:

✅ **Primary goal is lowest 10-year TCO**
- Saves $4M-5.5M over 10 years vs nat gas with DR

✅ **Backup-only application with minimal runtime**
- <50 hrs/year runtime keeps diesel fuel management costs low

✅ **DR revenue not critical to business model**
- $100K-150K/year not material to project economics

✅ **Air permits achievable**
- Can secure permits for 7.5 MW diesel capacity in Oklahoma
- Willing to accept permitting timeline and restrictions

✅ **Financial optimization is the priority**
- Project evaluated purely on IRR, NPV, cash flow metrics

---

### Choose NATURAL GAS if:

✅ **Permitting certainty worth $4M-5.5M premium**
- Diesel permitting has significant risk (delays, denials, runtime restrictions)
- Nat gas permitting faster, more certain, fewer restrictions
- Value of risk mitigation exceeds TCO premium

✅ **DR revenue strategically valuable**
- $100K-150K/year supports operating budget or pass-through to customers
- Positions facility as grid-responsive, attractive to ESG-focused customers

✅ **Higher runtime expected (>100 hrs/year)**
- If generators run frequently (not just DR), fuel economics favor nat gas
- Natural gas $5-7/MMBtu vs diesel $3/gal makes nat gas cheaper per MWh at scale

✅ **ESG/environmental requirements matter**
- Project financing requires low-emissions backup power
- Customer requirements for green/sustainable operations
- Corporate ESG commitments

✅ **Future revenue streams anticipated**
- SPP capacity markets post-2028 could add $150K-300K/year
- Frequency regulation, voltage support, other grid services
- Upside optionality worth base case premium

✅ **Regulatory/permitting risk mitigation is the priority**
- Avoiding multi-year permitting battles worth premium
- Certainty of project timeline more valuable than lowest TCO

---

## SENSITIVITY CASES

### 1. Higher Runtime Scenario (>100 hrs/year)

If generators run more than 100 hrs/year (beyond just DR events), fuel economics shift dramatically:

**Diesel Fuel Cost:**
- 100 hrs/year × 4.2 MW × 0.3 gal/kWh × $3/gal = **$378K/year**

**Nat Gas Fuel Cost:**
- 100 hrs/year × 4.2 MW × 7,000 BTU/kWh × $6/MMBtu = **$18K/year**

**Fuel Savings: $360K/year for nat gas at 100+ hrs runtime**

At this runtime, nat gas breaks even on TCO within **15-20 years** due to fuel cost savings.

**Implication:** If grid reliability poor or other use cases drive >100 hrs/year runtime, nat gas becomes financially competitive.

---

### 2. Permitting Failure Risk

If diesel permitting has material risk of failure or multi-year delay:

**Expected Value Analysis:**
- Diesel TCO: $9.55M - $13.2M (if permitted)
- Probability of permit approval: 50-70% (depends on jurisdiction, air quality)
- Delay cost: $500K-1M/year for mobile generators or project delay
- Risk-adjusted diesel cost: $11M - $16M

**Nat Gas TCO:** $13.5M - $18.7M (higher certainty)

If diesel permitting risk >30%, expected value may favor nat gas despite higher base case TCO.

---

### 3. Future Revenue Streams (Post-2028)

If SPP capacity markets and ancillary services materialize as projected in DR memo:

**Additional Revenue:**
- Capacity market: $50-100/kW-year = $210K-420K/year (post-2028)
- Frequency regulation: $20K-50K/year
- Total future revenue: $230K-470K/year

**15-Year TCO with Future Revenue:**
- Nat Gas: $18.7M + ($1.9M × 5 years OpEx) - ($126K × 5 years DR) - ($350K × 5 years future revenue) = **$26.9M**
- Diesel: $13.2M + ($3.2M × 5 years OpEx) = **$29.2M**

At 15-20 year horizon with future revenue streams, nat gas becomes **TCO-competitive** with diesel.

---

## STRATEGIC RECOMMENDATION

### For Saga Pryor Data Center (Grid Power Available Day 1)

**Financial Analysis Conclusion:**
Natural gas generators have **$4M-5.5M higher 10-year TCO** than diesel even with demand response revenue. DR revenue ($1M-1.5M over 10 years) reduces but does not eliminate the cost premium.

**Recommended Approach:**

1. **If financial TCO is the primary decision driver:** Choose diesel generators
   - Clear $4M-5.5M savings over 10 years
   - Accept permitting risk and timeline
   - Forgo $1M-1.5M DR revenue opportunity

2. **If permitting certainty and operational flexibility matter:** Choose natural gas
   - Pay $4M-5.5M premium for permitting certainty
   - Capture $1M-1.5M DR revenue (net premium: $3M-4M)
   - Preserve optionality for future grid services revenue
   - Support ESG/environmental requirements

3. **Hybrid approach (worth considering):**
   - 1-2 natural gas turbines for primary backup + DR participation
   - 1-2 smaller diesel gensets for black start and fuel diversity
   - Balances cost, permitting, and operational flexibility
   - Total cost between pure diesel and pure nat gas options

### Key Questions for Decision-Making

1. **What is the realistic probability of diesel permitting approval in Mayes County, Oklahoma?**
   - If >80%: Diesel likely better choice
   - If <60%: Nat gas risk mitigation worth premium

2. **How important is $100K-150K/year DR revenue to project economics?**
   - Material to operating budget: Favors nat gas
   - Immaterial (<2% of revenue): Favors diesel

3. **What are customer ESG requirements?**
   - Strong ESG requirements: Nat gas required
   - No ESG constraints: Diesel acceptable

4. **What is the expected generator runtime beyond DR events?**
   - <50 hrs/year: Diesel lower TCO
   - >100 hrs/year: Nat gas competitive on fuel costs

---

## CONCLUSION

**The Honest Math:** Demand response revenue does **not** fully justify the natural gas generator premium from a pure 10-year TCO perspective. Diesel remains $4M-5.5M cheaper over 10 years despite nat gas capturing $1M-1.5M in DR revenue.

**The Strategic Reality:** The decision is not purely financial. Permitting risk, operational flexibility, ESG requirements, and future revenue optionality all favor natural gas despite the TCO premium.

**Final Recommendation:** For Saga Pryor DC with grid power available Day 1, conduct detailed permitting risk assessment. If diesel permitting confidence is >70-80%, diesel offers superior 10-year TCO. If permitting risk is >30%, natural gas premium is justified as risk mitigation, not pure financial optimization.

---

**Tags:** #saga-project #generators #demand-response #tco-analysis #diesel-vs-natgas #financial-analysis #permitting

**Related Documents:**
- [[Diesel vs NatGas Generator CAPEX]] - Base CAPEX comparison (keep as-is)
- [[Demand Response Revenue Opportunity - Internal Memo]] - DR program details
- [[Demand Response in a Regulated Power Market - Oklahoma V2]] - Full market analysis
- [[Saga Pryor DC/Basis of Design/Archive/Benton_BOD/7BOD - Electrical (CSI Div 26)]] - Generator specifications and deployment strategy
- [[Saga Pryor DC/Basis of Design/Archive/Benton_BOD/0BOD - Procurement and Contracting (CSI Div 00)]] - Phasing and procurement approach
