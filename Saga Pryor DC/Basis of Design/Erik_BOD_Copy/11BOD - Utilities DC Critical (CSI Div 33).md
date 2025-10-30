**Created:** 2025-10-23 11:00

# BASIS OF DESIGN - UTILITIES (DC CRITICAL)
## CSI Division 33
### Saga Energy – Pryor Data Center

**Parent Document:** [[Saga Pryor DC/Basis of Design/Erik_BOD_Copy/_BOD - Exec Summary and TOC]]
**Related:** [[Basis of Design - Part 1 Core Systems]]

---

## OVERVIEW

**Note on Separate Page:** Division 33 Utilities receives a dedicated page separate from Site & Infrastructure (Divs 31-32) due to the **critical importance** of utility systems for data center operations. Utility interconnection, capacity, and reliability are primary project risks and CAPEX drivers.

This page covers utility services essential for data center operation: electrical interconnection, natural gas, water/sewer. Standard site utilities (stormwater) are covered in [[Saga Pryor DC/Basis of Design/Erik_BOD_Copy/10BOD - Site and Infrastructure (CSI Divs 31-32)]].

---

## UTILITY INTERCONNECTION STRATEGY {TBC}

### High-Voltage Electrical Service

**Service Parameters:**
- **Utility Provider:** Oklahoma Gas & Electric (OG&E)
- **Voltage Level:** 138 kV transmission line (nearby line confirmed, exact interconnection point TBD)
- **On-Site Transformation:** Step-down to 13.8 kV medium voltage via utility-owned or customer-owned substation

### Substation Transformer Sizing - Updated Oct 2025

**Requirement (Without BESS):**
- Facility load: Up to ~15 MW (12 MW IT + mechanical/support, PUE 1.2-1.3)
- No BESS charging load (BESS-as-UPS and Economic BESS rejected)
- Total: **Up to ~15 MW**

**Substation Transformer Sizing:**
- **Recommended:** **15-20 MVA** (accommodate facility load + margin)
- **Configuration:** Single transformer or dual transformers in N+1 (if utility allows)

**Note:** Original estimate of 20-25 MVA included 12 MW BESS charging load. Without BESS, transformer can be sized for facility load only.

**Action Required:** Confirm substation transformer capacity requirements with utility during interconnection study.

### Point of Interconnection (POI) Strategy - Pending Decision

**Option 1: Single POI with Behind-the-Meter (BTM) Configuration (RECOMMENDED)**
- Solar + data center connect behind a single utility meter
- **Advantages:**
  - Simplified metering
  - Maximized solar utilization (self-consumption by data center)
- **Disadvantages:**
  - Utility may require additional study/upgrades

**Option 2: Dual POI Configuration (Fallback)**
- Data center connects at one POI (load only)
- Solar connects at separate POI (generation only)
- **Advantages:**
  - Simpler utility approval process
  - Follows traditional interconnection model
- **Disadvantages:**
  - Limits behind-the-meter solar optimization
  - More complex metering/billing

**Critical Path Action Required:**
Initiate formal interconnection request with OG&E immediately. This study will define:
- Available capacity at nearest substation
- Required utility upgrades (transformers, switchgear, protection)
- Interconnection costs and timeline
- Preferred POI configuration

**Cost Exposure:**
- Utility system upgrades: $2-5M (TBD via utility study)
- Interconnection study fees: $50-150K
- **Schedule risk: 6-18+ months if major upgrades required**

---

## NATURAL GAS SERVICE - UPDATED OCT 2025 {TBC}

### Primary Backup Power: Natural Gas Turbine(s)

**Service Requirements:**
- **Fuel Source:** Pipeline natural gas for turbine generators
- **Turbine Capacity:** ~4.3 MW per turbine
- **Demand:** ~500-700 CFH per turbine at full load
- **Peak Demand:** ~3,000-4,000 CFH (if multiple units running simultaneously)

**Gas Service Specifications:**
- **Pressure:** 5-10 psig at meter (typical utility delivery pressure)
- **Meter Size:** 6-8" meter for peak demand
- **Line Location:** Nearby natural gas line identified, capacity confirmation required

**Action Required:**
- Confirm natural gas service availability with Oklahoma Natural Gas (ONG) or local provider
- Request capacity study to verify adequate pipeline capacity
- Determine interconnection costs and timeline
- If insufficient capacity, evaluate dual-fuel strategy or diesel-only fallback

### Diesel Fuel Storage (Secondary Backup)

**Fuel Oil Storage (If Diesel Generators Selected):**
- **Type:** Double-wall sub-base tanks or above-ground storage tanks (AST)
- **Capacity:** 48-hour minimum runtime for diesel generators
- **Total Storage:** ~8,000 gallons aggregate (if multiple generators with sub-base tanks)
- **Regulatory:** EPA SPCC plan required if total storage >1,320 gallons

**Above-Ground Storage Tank (Alternative):**
- Centralized fuel farm with 10,000-20,000 gallon AST
- Day tanks at each generator (smaller sub-base tanks)
- Fuel transfer pumps from AST to day tanks
- Secondary containment: 110% of largest tank volume

**Regulatory Requirements:**
- EPA SPCC Plan (if fuel storage >1,320 gallons aggregate)
- Secondary containment per EPA and Oklahoma DEQ
- Spill kits and response equipment
- Annual tank inspections

---

## DOMESTIC WATER SERVICE {TBC}

### Water Demand
- **Domestic Use:** Restrooms, break room, showers
  - Estimated: ~500-1,000 gallons/day (5-10 staff on-site)
- **Fire Suppression Fill:** One-time fill for sprinkler system (if wet pipe used)
  - Estimated: 5,000-10,000 gallons (one-time)
- **Cooling System Fill:** One-time fill for chilled water loop
  - Estimated: 5,000-8,000 gallons (closed-loop, minimal makeup)

### Service Requirements
- **Supply:** Municipal water or on-site well (TBD via site study)
- **Pressure:** 60-80 psi minimum at building entry point
- **Meter Size:** 2-3" meter (adequate for domestic flow + fire system fill)
- **Backflow Prevention:** Reduced pressure backflow preventer (RP) required by code

**Action Required:**
- Confirm water service availability via local water authority
- Request Water & Wastewater Availability Study to validate:
  - Service line capacity
  - Pressure at site
  - Connection fees and timeline

**Zero Water Cooling:** Note that cooling system requires zero ongoing water (closed-loop air-cooled chillers). Domestic water is only for staff use and one-time chilled water fill.

---

## SANITARY SEWER & WASTEWATER {TBC}

### Wastewater Flow
- **Domestic Wastewater:** ~500-1,000 gallons/day (restrooms, break room, showers)
- **Process Wastewater:** None (closed-loop cooling system, no blowdown or discharge)

### Service Requirements
- **Connection:** Municipal sanitary sewer or on-site septic system (TBD via site study)
- **Pipe Size:** 4-6" sanitary sewer lateral
- **Grease Trap:** Not required (break room sink only, no commercial kitchen)

**Action Required:**
- Confirm sanitary sewer availability and capacity via local wastewater authority
- If municipal sewer not available, design on-site septic system per Oklahoma DEQ requirements

---

## FIBER & TELECOMMUNICATIONS UTILITIES {TBC}

### Fiber Entry Infrastructure
- **Primary Entry:** North side of building
- **Secondary Entry (Diversity):** South side of building
- **Conduit:** 4-6" conduits (4-6 per entry point) from property line to MMRs
- **Vault:** Telecommunications vault at property line for carrier hand-off

### Fiber Route Analysis (In Progress)
**Camelot Task 3 (Expected Delivery: Early November 2025):**
- Identify existing fiber routes near site
- Map carrier availability
- Confirm physical diversity
- Estimate connectivity installation timeline and costs

**Detailed specifications:** See [[Saga Pryor DC/Basis of Design/Erik_BOD_Copy/8BOD - Communications (CSI Div 27)]]

---

## UTILITY COORDINATION & CRITICAL PATH

### High-Priority Actions

**1. Utility Interconnection Study (OG&E)**
- **Timeline:** Initiate immediately (6-18+ month lead time)
- **Cost Exposure:** $2-5M utility upgrades + $50-150K study fees
- **Schedule Risk:** Major upgrades can delay project by 6-18 months

**2. Natural Gas Service Confirmation (ONG)**
- **Timeline:** Initiate in October 2025
- **Cost Exposure:** $100-300K (piping, meter, interconnection)
- **Schedule Risk:** +2-4 weeks if service installation required

**3. Water & Wastewater Availability Study**
- **Timeline:** October-November 2025
- **Cost Exposure:** $50-200K (connection fees, if municipal service available)
- **Schedule Risk:** +4-8 weeks if on-site well/septic required

**4. Fiber Route Analysis (Camelot)**
- **Timeline:** Early November 2025
- **Cost Exposure:** $50-200K (dark fiber installation to Google Pryor)
- **Schedule Risk:** +8-12 weeks if new fiber route construction required

### Risk Mitigation
- **Utility Interconnection:** Largest schedule risk; initiate study immediately to identify required upgrades
- **Natural Gas:** If insufficient capacity, fall back to diesel-only or dual-fuel with on-site diesel storage
- **Water/Sewer:** If municipal unavailable, on-site well/septic is fallback (adds cost and schedule)
- **Fiber:** Multiple carrier options reduce single-carrier dependency

---

## COST IMPACTS

| Utility Service | Cost Estimate |
|---|---|
| Utility interconnection (138 kV) + substation upgrades | $2-5M (TBD via utility study) |
| Substation transformer (15-20 MVA) | $400-800K (if customer-owned) |
| Natural gas service connection | $100-300K |
| Diesel fuel storage (if needed) | $200-400K |
| Water service connection | $50-200K |
| Sanitary sewer connection | $50-200K |
| Fiber conduit infrastructure | $200-400K |
| **Total Utility Services** | ~$3.0-7.3M |

**Note:** Utility interconnection is largest cost variable (depends on OG&E study results).

**Cost Savings Without BESS:**
- Smaller substation transformer (15-20 MVA vs 20-25 MVA): **-$100-200K**

---

**Tags:** #saga-project #utilities #electrical-interconnection #natural-gas #water-sewer #csi-division-33

**Related Documents:**
- [[Saga Pryor DC/Basis of Design/Erik_BOD_Copy/_BOD - Exec Summary and TOC]] - Main title page
- [[Saga Pryor DC/Basis of Design/Erik_BOD_Copy/7BOD - Electrical (CSI Div 26)]] - Electrical distribution details
- [[Saga Pryor DC/Basis of Design/Erik_BOD_Copy/4BOD - Plumbing (CSI Div 22)]] - Water usage and treatment
- [[Saga Pryor DC/Basis of Design/Erik_BOD_Copy/8BOD - Communications (CSI Div 27)]] - Fiber infrastructure
- [[Architectural Meeting Changes by CSI Division]] - October 2025 updates
