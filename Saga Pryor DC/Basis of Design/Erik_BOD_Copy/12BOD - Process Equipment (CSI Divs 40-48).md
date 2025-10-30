**Created:** 2025-10-23 11:05

# BASIS OF DESIGN - PROCESS EQUIPMENT
## CSI Divisions 40-48
### Saga Energy – Pryor Data Center

**Parent Document:** [[Saga Pryor DC/Basis of Design/Erik_BOD_Copy/_BOD - Exec Summary and TOC]]
**Related:** [[Basis of Design - Part 1 Core Systems]] | [[Why BESS Should Not Be UPS]] | [[Excess Solar Monetization Strategy]]

---

## OVERVIEW

Process equipment includes solar array, generators, and microgrid control systems that integrate renewable energy with data center operations.

**Primary Divisions Covered:**
- **Division 40:** Process Integration (microgrid coordination)
- **Division 48:** Electrical Power Generation (solar, generators)

**Other Divisions (41-47, 49):** Not applicable to this project.

**BESS NOT INCLUDED:** Both BESS-as-UPS and Economic BESS evaluated and rejected. See [[Why BESS Should Not Be UPS]] for Tier III compliance analysis and [[Excess Solar Monetization Strategy]] for economic BESS NPV analysis (deeply negative).

---

## DIVISION 40 – PROCESS INTEGRATION

### Microgrid Integration Overview

The facility operates as a simplified microgrid coordinating:
- **Utility Grid:** Primary power source (138 kV interconnection)
- **Solar Array:** 12 MW DC on-site renewable generation
- **Generators:** Natural gas turbine(s) + diesel reciprocating for backup power
- **Data Center Load:** 12 MW IT + mechanical/support (~15 MW total facility load)

**No BESS:** BESS-as-UPS rejected due to Tier III violations. Economic BESS rejected due to negative NPV (-$5.3M to -$6.2M over 20 years).

### Microgrid Control System (EMS)

**Function:** Coordinates power flow between utility, solar, generators, and data center load

**Simplified Control Requirements:**
- Real-time power balancing (solar + utility = data center load)
- Generator dispatch on utility outage
- Solar curtailment if needed (no export or limited export capacity)
- Power quality monitoring (voltage, frequency, harmonics)

**No IEEE 2030.7/2030.8 Compliance Required:**
- BESS-as-UPS was the only driver for advanced microgrid protocols
- Without BESS, standard generator ATS and solar inverter controls sufficient
- Significant cost savings vs full microgrid controller

### Key Control Functions

**1. Generator Dispatch Logic**
- Auto-start generators on utility outage (standard ATS function)
- Load sharing between generators (if multiple units online)
- Generator paralleling with utility (if designed for peak shaving)

**2. Solar Management**
- Maximize solar self-consumption by data center
- Curtail solar if load drops below minimum and no export permitted
- Monitor inverter performance and fault conditions

**3. Power Quality Monitoring**
- Continuous monitoring of voltage, frequency, harmonics, power factor
- Fault detection and isolation
- Automatic protective relay coordination

**4. Predictive Analytics (Optional)**
- Solar generation forecasting (weather-based)
- Data center load prediction (historical patterns)
- Minimal value without BESS to optimize

**5. SCADA Integration**
- 24/7 remote monitoring and control
- Integration with BMS and DCIM
- Alarms and notifications for off-normal conditions

### Recommended EMS Platforms
- **Schneider Electric EcoStruxure Power Monitoring Expert:** Standard DC power monitoring (not full microgrid controller)
- **Siemens PowerManager:** Simplified alternative
- **Solar Inverter Built-In Controls:** May be sufficient for basic solar + grid coordination

**Cost:** $200-400K for simplified power monitoring system (vs $1.05-1.55M for full IEEE 2030.7/2030.8 microgrid controller)

**Detailed EMS specifications:** See [[Saga Pryor DC/Basis of Design/Erik_BOD_Copy/6BOD - Integrated Automation (CSI Div 25)]]

---

## DIVISION 48 – ELECTRICAL POWER GENERATION {TBC}

See here for more details: [[Solar Contribution Validation - Pressure Test]]

### Interconnection Approach

**Single POI (Behind-the-Meter) Configuration (RECOMMENDED):**
```
Utility 138kV
    ↓
[Substation Transformer 20-25 MVA]
    ↓
13.8kV Microgrid Bus
    ├── Data Center Load (~15 MW)
    ├── Solar Inverters (9-10 MW AC)
    └── BESS (16 MW total / 48 MWh, phased: 12MW→16MW)
```

**Advantages:**
- Solar energy consumed directly by data center (no export/import losses)
- BESS stores excess solar for nighttime use
- Simplified utility metering and billing
- Maximizes renewable energy utilization

**Action Required:** Camelot Task 2 (Net Load Analysis) will model both BTM and FTM configurations and provide revenue projections. Expected delivery early November 2025.

---

### Battery Energy Storage System (BESS) - REJECTED

**BESS-as-UPS: REJECTED**
- **Reason:** Violates Tier III concurrent maintainability requirement
- **Analysis:** Single BESS creates non-maintainable single point of failure. True 2N BESS would cost $18-22M (more than traditional $11-13M 2N UPS) and still lacks lender acceptance.
- **See:** [[Why BESS Should Not Be UPS]] for full technical analysis

**Economic BESS (Separate from UPS): REJECTED**
- **Reason:** Deeply negative NPV of -$5.3M to -$6.2M over 20 years
- **Root Cause:** $10.8M CAPEX cannot be recovered from limited Phase 1-2 revenue window (2 years, $1.8M PV) combined with generator-competed Phase 3-20 revenue
- **Analysis:**
  - Phase 1-2 window (2 years): Only $1.8M present value from solar arbitrage
  - Phase 3-20 revenue: Generators can provide demand response at $0 incremental CAPEX, eliminating $3.1M of BESS value
  - Result: Cannot achieve positive ROI under any scenario
- **See:** [[Excess Solar Monetization Strategy]] for full financial analysis

**Excess Solar Monetization Alternatives Evaluated:**
- **Option A: Direct Grid Export** - NPV $0.8-1.5M (marginal but positive)
- **Option B: Mobile Edge Computing** - NPV $4.7-7.5M (best option if interconnection study succeeds)
- **Option C: Economic BESS** - NPV -$5.3M to -$6.2M (NOT VIABLE)

**Recommendation:** Pursue Option B (mobile edge computing) if utility interconnection study confirms feasibility. Otherwise, pursue Option A (direct grid export) or curtail excess solar.

---

### Backup Power Generation {TBC}

**Dual-Fuel Generator Strategy (Updated Oct 2025):**

**Primary Backup: Natural Gas Turbine(s)**
- **Capacity:** ~4.3 MW per turbine
- **Fuel Source:** Pipeline natural gas (capacity confirmation required)
- **Advantages:**
  - High efficiency for backup power generation
  - Unlimited runtime (pipeline fuel)
  - Lower emissions vs diesel (NOx, particulates, CO2)

**Secondary Backup: Diesel Reciprocating Generators**
- **Configuration:** N+1 redundancy within diesel genset group
- **Fuel Storage:** Belly tanks or above-ground storage (48-hour minimum)
- **Advantages:**
  - Fuel diversity (independent of natural gas infrastructure)
  - Proven reliability, customer comfort
  - Backup if natural gas service fails

**Generator Count:**
- **IT Load Generators:** 4-5 generators (turbine + diesel recip mix, exact count TBD)
- **Mechanical Load Generators:** 1 generator (office/non-critical areas)
- **Total Generators:** ~5-6 units

**Reasoning for Dual Approach:**
- **Two types of reserve power required:** Cannot rely on single fuel source
- **Turbine benefits:** Lower emissions, unlimited runtime, higher efficiency
- **Diesel benefits:** Fuel independence, proven technology
- **Risk mitigation:** If natural gas service fails, diesel provides backup

**Generator Backup Duration:**
- Traditional 2N UPS provides 15 minutes backup (bridges to generator startup)
- Generators provide extended backup power (unlimited runtime with natural gas, 48+ hours with diesel)

**Detailed generator specifications:** See [[Saga Pryor DC/Basis of Design/Erik_BOD_Copy/7BOD - Electrical (CSI Div 26)]]

---

## FACILITY LOAD SIZING

### Total Facility Load Breakdown
- **IT Load:** 12 MW (updated from 7.4 MW)
- **Cooling Load:** 2.4-3.6 MW (calculated from PUE 1.2-1.3)
- **Auxiliary Systems:** 0.3-0.6 MW (lighting, BMS, pumps, fans)
- **Total Facility Load:** **~15 MW**

### Generator N+1 Redundancy Strategy
- **Phase 1:** 2× generators (N+1 for ~4MW load)
- **Phase 2-5:** Add generators as load increases (see table in [[Saga Pryor DC/Basis of Design/Erik_BOD_Copy/7BOD - Electrical (CSI Div 26)]])
- **Ultimate:** 8× generators total (N+1 for ~28MW ultimate load)

### Solar Array Match
- **Solar Capacity:** 12 MW DC (~9-10 MW AC)
- **Facility Load:** 15 MW (at full Phase 1-2 occupancy)
- **Solar Contribution:** 60-80% of annual energy consumption (with behind-the-meter configuration) {TBC}

**Action Required:**
1. Commission detailed electrical load study to validate 15MW total facility load (updated from 10MW)
2. Ensure generator sizing adequate for 15MW facility load (turbine + diesel recip mix)

---

## SOLAR INTERCONNECTION STRATEGY

**Behind-the-Meter (BTM) - RECOMMENDED:**
- Solar interconnects on customer side of utility meter
- All solar energy consumed by data center first; only net load seen by utility
- **Advantages:** Maximizes solar utilization, minimizes utility demand charges, simplifies billing
- **Disadvantages:** Foregoes potential revenue from grid export (minimal with no BESS to store excess)

**Front-of-Meter (FTM) - Alternative:**
- Solar interconnects on utility side of meter (separate metering)
- Solar can export to grid when data center load is low
- **Advantages:** Potential revenue from excess solar export (Phase 1-2 only)
- **Disadvantages:** Complex metering, limited export revenue without BESS storage

**Decision:** BTM configuration recommended for simplicity. Excess solar in Phase 1-2 can be curtailed or exported if minimal grid export capacity available.

**Excess Solar Monetization:** See BESS - REJECTED section above for evaluation of mobile edge computing vs direct grid export options.

---

## DEMAND RESPONSE PARTICIPATION (GENERATORS) {TBC}

**Demand Response via Generators:**
- **OG&E Load Reduction Program:** $25-35/kW/year for 6-10 curtailment events/year
- **Implementation:** Island data center on generators during utility peak demand events
- **Revenue Potential:** 20,000 kW × $30/kW/year = $600k/year
- **CAPEX:** $0 (generators already required for Tier III backup)
- **Advantage:** Provides revenue without requiring $10.8M BESS investment
- **Note:** This was key factor in rejecting Economic BESS (generators compete for same revenue at $0 incremental cost)

**Implementation:**
- Coordinate with OG&E to enroll in Load Reduction Program
- Test islanding capabilities during commissioning
- Automate response to utility curtailment signals

---

## PHASED DEPLOYMENT INFRASTRUCTURE

### Phase 1 (Build Day One)
- **Solar Array:** Full 12 MW DC installation
- **Generators:** Phase 1 generators (2× units, N+1 for initial load)
- **EMS:** Simplified power monitoring system ($200-400K)
- **UPS:** 2N frames with Phase 1 modules (see [[Saga Pryor DC/Basis of Design/Erik_BOD_Copy/7BOD - Electrical (CSI Div 26)]])

### Phase 2-5 (Triggered by IT Load Growth)
- **Generators:** Add generators as load increases (phased per load growth)
- **UPS:** Add UPS modules to existing frames
- **Solar:** Potential expansion if demand justifies (site has capacity for +10-15 MW)

### Procurement Strategy
- Execute solar EPC contract for Phase 1 array
- Execute generator contract with modular expansion options
- Coordinate with UPS vendor for phased module additions
- Consider future solar expansion if Phase 1-2 excess solar successfully monetized

---

## SUSTAINABILITY & CARBON REDUCTION

### Renewable Energy Contribution
- **On-Site Solar:** 12 MW DC (~19-24 GWh/year)
- **Renewable Penetration:** 60-80% of annual data center energy from on-site solar (behind-the-meter self-consumption)
- **Carbon Offset:** ~12,000-16,000 metric tons CO2e per year (vs grid electricity at 800 kg CO2e/MWh SPP average)
- **Note:** High renewable penetration achieved without BESS through optimized behind-the-meter configuration

### Generator Emissions Reduction
- Natural gas turbines: 30-50% lower NOx and particulate emissions vs diesel-only
- Infrequent generator runtime (backup use only) minimizes emissions
- Total emissions significantly lower than diesel-only backup approach

---

## COST IMPACTS

| System                                     | Cost Estimate |
| ------------------------------------------ | ------------- |
| Generator systems (turbine + diesel recip) | ~$3-5M        |
| Simplified power monitoring system (EMS)   | $200-400K     |
| **Total Process Equipment (Phase 1)**      | ???           |

**BESS NOT INCLUDED:**
- BESS-as-UPS: $29.7-31.2M Phase 1 (REJECTED - Tier III violation)
- Economic BESS: $10.8M (REJECTED - NPV -$5.3M to -$6.2M)
- Advanced microgrid controller: $1.05-1.55M (NOT REQUIRED without BESS)
- BESS fire suppression: $150-300K (NOT REQUIRED without BESS)

**Cost Savings:**
- Simplified EMS vs full microgrid controller: **-$850K to -$1.15M**
- Total avoided BESS-related CAPEX: **~$40-45M** (including Economic BESS and advanced controls)

---

**Tags:** #saga-project #solar #bess #generators #microgrid #renewable-energy #csi-divisions-40-48

**Related Documents:**
- [[Saga Pryor DC/Basis of Design/Erik_BOD_Copy/_BOD - Exec Summary and TOC]] - Main title page
- [[BESS as UPS Replacement - Feasibility Analysis V2]] - Detailed BESS analysis
- [[Saga Pryor DC/Basis of Design/Erik_BOD_Copy/7BOD - Electrical (CSI Div 26)]] - Electrical integration details
- [[Saga Pryor DC/Basis of Design/Erik_BOD_Copy/6BOD - Integrated Automation (CSI Div 25)]] - Microgrid control system (EMS)
- [[Saga Pryor DC/Basis of Design/Erik_BOD_Copy/11BOD - Utilities DC Critical (CSI Div 33)]] - Utility interconnection strategy
- [[Architectural Meeting Changes by CSI Division]] - October 2025 updates
