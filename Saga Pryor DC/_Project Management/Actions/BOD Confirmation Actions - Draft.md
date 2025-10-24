**Created:** 2025-10-23 11:15
**Updated:** 2025-10-23 11:45

# BOD Confirmation Actions - Draft for Review

**Purpose:** Key actions identified from review of Power and Basis of Design documentation that need to be completed to confirm the Basis of Design for Saga Pryor DC.

**Source Documents Reviewed:**
- Power folder: Solar validation, BESS analysis, mobile edge computing, excess solar monetization
- Basis of Design folder: Executive summary, Electrical (Div 26), HVAC (Div 23), Utilities (Div 33)
- Camelot SOW Summary: Market study, net load analysis, fiber drawings

**Status:** DRAFT - Please review and confirm before adding to Actions.csv

**Naming Convention:** `[Division]-[Number]: [Description]`
- Example: `33-001: Utility interconnection study`
- Division numbers follow CSI MasterFormat where applicable

---

## PRIORITY 1 - CRITICAL PATH ITEMS

### Utility Interconnection & Power (CSI Division 33)

**33-001: Comprehensive Utility Interconnection Study & Grid Power Validation**
- **Description:**
  - **PRIMARY QUESTION: Confirm grid power is available at the site** (138 kV service from OG&E)
  - Submit formal interconnection application to OG&E for 138 kV service (15-20 MVA substation transformer)
  - Validate interconnection agreement permits:
    - **Option A (Grid Export):** 12MW solar export capability during Phase 1-2
    - **Option B (Mobile Compute):** 6-8MW additional load for mobile edge computing
  - Identify required utility upgrades, costs, and timeline
  - Determine POI configuration (single behind-the-meter vs dual POI)
  - Confirm substation hosting capacity and transmission line voltage/capacity

- **Key Questions from Excess Solar Monetization Strategy:**
  1. Is grid power available at this site at all? (Foundational question)
  2. Does interconnection agreement permit 12MW export (Option A)?
  3. Does interconnection agreement permit 6-8MW additional load (Option B)?
  4. If no to either, what utility study timeline and upgrade costs ($0-5M range)?
  5. Which POI configuration (single BTM vs dual) is permitted/preferred?

- **Camelot Task 1 Coordination:**
  - Camelot's Market Study (Task 1 in SOW) covers: substation hosting capacity, nearby transmission lines with voltage, queue position recommendations
  - **Action:** Review Camelot Task 1 deliverable (expected early Nov 2025) to inform this interconnection application
  - **Questions for Camelot:**
    - Will substation capacity analysis identify specific upgrade costs for 12MW export or 6-8MW additional load?
    - Does transmission analysis include specific interconnection point recommendations?
    - Can you identify if existing interconnection agreements limit export or additional load?

- **Assigned To:** Saga (lead), coordinate with Camelot (Task 1 findings)
- **Dependencies:** None for application submittal - START IMMEDIATELY. Camelot Task 1 provides supporting data.
- **Impact:**
  - **CRITICAL:** Without grid power confirmation, entire project is at risk
  - $2-5M utility upgrade cost exposure (plus potential $0-5M for Option B mobile compute)
  - 6-18 month schedule risk if major upgrades required
  - Determines viability of Option A (grid export) and Option B (mobile compute) for solar monetization
- **Related Decisions:** Substation sizing, POI configuration, solar monetization strategy (Options A vs B vs neither)
- **Target Date:** Application submitted ASAP (Week 1), results in 6-12 months
- **Notes:** This is THE foundational critical path item. Must confirm grid power exists before all other design work proceeds.

---

**33-002: Confirm Natural Gas Service Capacity for Turbine Generators**
- **Description:** Contact Oklahoma Natural Gas (or local provider) to confirm pipeline capacity for 3,000-4,000 CFH peak demand (multiple turbines). Verify pressure (5-10 psig), meter sizing (6-8"), and interconnection timeline.
- **Assigned To:** Saga
- **Dependencies:** A-002 (existing action)
- **Impact:** If insufficient capacity, must fall back to diesel-only or evaluate dual-fuel strategy
- **Related Decisions:** Generator fuel strategy (turbine vs diesel mix)
- **Notes:** Already tracked as A-002 in existing actions (due 10/18/25). Critical for confirming generator fuel strategy and generator count.

---

**33-003: Determine Preferred POI Configuration (Single vs Dual)**
- **Description:** Based on utility interconnection study results (33-001), confirm whether single behind-the-meter POI (solar + DC) or dual POI configuration is preferred. Single POI maximizes solar utilization but may require additional utility upgrades.
- **Assigned To:** Saga
- **Dependencies:** 33-001 (utility interconnection study results)
- **Impact:** Affects solar self-consumption optimization, metering complexity, and potentially utility upgrade costs
- **Related Decisions:** Solar monetization strategy

---

## PRIORITY 2 - MAJOR DESIGN DECISIONS

### Electrical Systems (CSI Division 26)

**26-001: Confirm UPS Equipment Specifications and Pricing**
- **Description:** Select traditional 2N modular UPS equipment specifications for Phase 1 deployment (6MW N+1, $4.5M). Lock pricing for future phase expansions (ultimate 28MW). Confirm modular frame sizing and spare parts compatibility. This is for design and cost estimating, not vendor selection/procurement. We can likely use the existing schneider estimates, but should confirm.
- **Assigned To:** PGCIS
- **Dependencies:** None
- **Impact:** $4.5M Phase 1 CAPEX estimate accuracy, Class 3 cost estimate (+/- 15-20%)
- **Related Decisions:** UPS topology confirmed (traditional 2N, BESS-as-UPS rejected)
- **Target Date:** November 2025

---

**26-002: Confirm Final Generator Configuration (Turbine + Diesel Mix)**
- **Description:** Based on natural gas service confirmation (33-002), finalize generator count and fuel mix. Current plan: 4-5 generators total (natural gas turbine + diesel recip mix, N+1 redundancy). Customers may prefer diesel for fuel diversity if concerned about natural gas supply interruption risk.
- **Assigned To:** PGCIS/Saga
- **Dependencies:** 33-002 (natural gas capacity confirmation), A-011 (turbine lead time research)
- **Impact:** $2.4M Phase 1 CAPEX, ±$500K-1M based on turbine vs diesel mix {TBC}
- **Related Decisions:** Fuel diversity strategy, emissions compliance, customer comfort/marketing
- **Target Date:** November 2025

---

**26-003: Validate Substation Transformer Sizing (15-20 MVA)**
- **Description:** Confirm 15-20 MVA sizing is adequate for facility load without BESS (12 MW IT + mechanical/support, PUE 1.2-1.3 = ~15 MW peak). Original 20-25 MVA estimate included BESS charging load (now eliminated).
- **Assigned To:** PGCIS
- **Dependencies:** A-024 (existing action - validate transformer sizing), 33-001 (utility study)
- **Impact:** $400-800K if customer-owned substation transformer, ±$100-200K based on sizing
- **Related Decisions:** BESS rejection (no BESS charging load to accommodate)
- **Notes:** Already tracked as A-024 in existing actions.

---

**26-004: Confirm Electrical Room Configuration (Indoor vs Outdoor)**
- **Description:** BOD shows reversion to traditional indoor electrical rooms (6,000 SF total, 2× 3,000 SF) to house 2N UPS systems. October architectural meeting discussed outdoor containerized enclosures. Confirm final approach and resolve discrepancy.
- **Assigned To:** PGCIS
- **Dependencies:** 26-001 (UPS equipment specifications)
- **Impact:** Building footprint, fire suppression cost ($2-3M for indoor rooms), UPS equipment protection
- **Related Decisions:** Traditional UPS requires indoor housing (outdoor only viable with BESS-as-UPS)
- **Target Date:** November 2025

---

### Mechanical Systems (CSI Division 23)

**23-001: Finalize Chiller Plant Sizing (~16 Chillers @ 1.5 MW)**
- **Description:** Confirm chiller count and sizing for 12 MW initial (20-24 MW ultimate) capacity. Current plan: ~16 chillers in modular 3 MW blocks (3 chillers per block = N+1 redundancy). Validate against PUE target (1.2-1.3) and Oklahoma climate.
- **Assigned To:** Erik/PGCIS
- **Dependencies:** A-032, A-034 (existing actions - cooling strategy evaluation)
- **Impact:** $8-12M phased chiller CAPEX
- **Related Decisions:** Air-cooled with free cooling confirmed, adiabatic coolers eliminated
- **Target Date:** October-November 2025
- **Notes:** Related to existing actions A-032 (cooling strategy) and A-034 (CapEx comparison).

---

**23-002: Confirm RDHx Deployment Scope (Network Racks)**
- **Description:** Validate rear-door heat exchanger (RDHx) deployment for ~48 network racks (up to 22 kW/rack air-cooled). Confirm cost delta ($3-5K per RDHx unit = $144-240K total) is acceptable vs fan wall elimination.
- **Assigned To:** PGCIS
- **Dependencies:** A-032 (cooling strategy evaluation)
- **Impact:** +$144-240K CAPEX, but provides per-customer control and flexible billing
- **Related Decisions:** Fan walls eliminated, RDHx confirmed as primary air-cooling approach
- **Target Date:** October-November 2025
- **Notes:** Related to existing action A-032.

---

**23-003: Validate CDU Sizing for Liquid-Cooled AI Racks**
- **Description:** Confirm 9× MCDU-50 equivalent units (or similar) are adequate for 48 AI racks (up to 132 kW/rack liquid-cooled). Validate chilled water manifold distribution and leak detection strategy.
- **Assigned To:** PGCIS
- **Dependencies:** A-019, A-047 (existing actions - RDHx analysis and deployment)
- **Impact:** $500K-1M CDU CAPEX
- **Related Decisions:** Direct-to-chip vs rear-door liquid coil options for customers
- **Target Date:** November 2025
- **Notes:** Related to existing actions A-019 and A-047.

---

**23-004: Confirm Rooftop AHU Configuration for Data Hall Humidity Control**
- **Description:** Validate rooftop AHU sizing for 40,000 SF data hall (20,000 SF Phase 1 fitted, 20,000 SF Phase 2 shell). Confirm N+1 redundancy and integration with RDHx/CDU cooling strategy (AHUs handle humidity + over-pressurization, not IT heat rejection).
- **Assigned To:** PGCIS
- **Dependencies:** 23-001 (chiller plant sizing)
- **Impact:** $300-500K CAPEX
- **Related Decisions:** Deviation from RD109 (adds comfort cooling not in baseline)
- **Target Date:** November 2025

---

### Building & Site (CSI Divisions 02-14, 31-32)

**02-001: Confirm Building Test Fit on Site and Equipment Yard Locations**
- **Description:** Test fit building configuration on the 121-acre site to determine optimal orientation. Once building is placed, determine which side is appropriate for generator yard (north/south/east/west) and which side for chiller yard. Consider factors: property lines, access roads, future expansion areas, sound attenuation, prevailing winds.
- **Assigned To:** Julia (Architect)
- **Dependencies:** 26-002 (final generator count), 23-001 (chiller count)
- **Impact:** Site layout, equipment access, sound attenuation requirements, future phase expansion planning
- **Related Decisions:** Electrical/mechanical separation strategy, generator yard clearances, chiller yard airflow
- **Target Date:** November 2025
- **Notes:** Replaces previous action B-003 (assumed north side for generators). Need to validate building placement first.

---

**02-002: Validate Slab-on-Grade Foundation Design for Equipment Loads**
- **Description:** Review geotechnical analysis to confirm slab-on-grade can support equipment loads (chillers, transformers, generators) without raised floor. Raised floor eliminated from design.
- **Assigned To:** PGCIS
- **Dependencies:** A-043 (existing action - validate slab-on-grade), A-018 (geotech review complete)
- **Impact:** Foundation design, cost
- **Related Decisions:** No raised floor (structural slab + overhead distribution confirmed)
- **Notes:** Already tracked as A-043 in existing actions.

---

## PRIORITY 3 - TECHNICAL VALIDATIONS

### Utilities & Interconnection (CSI Division 33)

**33-004: Complete Water & Wastewater Availability Study**
- **Description:** Confirm municipal water service availability (500-1,000 gal/day domestic use) and sanitary sewer capacity. If municipal unavailable, evaluate on-site well/septic system design per Oklahoma DEQ requirements.
- **Assigned To:** Saga
- **Dependencies:** None
- **Impact:** $50-200K connection fees (municipal) or $100-300K (on-site well/septic)
- **Related Decisions:** Zero water cooling strategy (no ongoing water for cooling, only domestic)
- **Target Date:** October-November 2025

---

**33-005: Confirm Diesel Fuel Storage Strategy (If Diesel Generators Selected)**
- **Description:** Finalize diesel fuel storage approach: sub-base belly tanks vs centralized above-ground storage tank (AST). Confirm 48-hour minimum runtime capacity and EPA SPCC plan requirements (if >1,320 gallons total).
- **Assigned To:** PGCIS/Saga
- **Dependencies:** 26-002 (final generator configuration)
- **Impact:** $200-400K fuel storage CAPEX, regulatory compliance (EPA SPCC)
- **Related Decisions:** Dual-fuel strategy (turbine + diesel)
- **Target Date:** November 2025

---

### Fiber & Connectivity (CSI Division 27)

**27-001: Review Camelot Fiber Study Results and Coordinate with Aaron's Google Outreach**
- **Description:**
  - **Camelot Task 3 (Fiber Drawings, T&M):** Review fiber design drawings for routing to site when delivered
  - **Aaron's Google Outreach:** Coordinate with Aaron who is contacting Google regarding GCP Dedicated Interconnect feasibility
  - Confirm diverse fiber routes, carrier availability, and physical diversity
  - Validate dark fiber connectivity to Google Pryor campus (~4 miles, <1ms latency target)

- **Questions for Camelot (Task 3):**
  - What level of detail is included in fiber design drawings?
  - Will drawings show diverse route options to Google campus (4 miles)?
  - Does analysis cover GCP on-ramp infrastructure requirements?
  - Estimated hours/cost for fiber design work (T&M basis)?

- **Assigned To:** Benton/PGCIS (Camelot coordination), Aaron (Google contact)
- **Dependencies:** A-040 (receive Camelot studies), A-020 (GCP on-ramp feasibility - Aaron's action)
- **Impact:** Fiber infrastructure costs ($200-400K), GCP Dedicated Interconnect feasibility (competitive differentiator)
- **Related Decisions:** Dual MMR strategy (north/south for diverse fiber paths)
- **Target Date:** November 2025
- **Notes:**
  - Camelot Task 1 includes "proximity to fiber" analysis in market study
  - Camelot Task 3 provides fiber design drawings on T&M basis
  - Aaron is separate point of contact for Google GCP interconnect discussions
  - Already partially tracked as A-040 (Camelot studies) and A-020 (GCP feasibility)

---

## PRIORITY 4 - COST ESTIMATING & FINANCIAL MODEL

### Cost Validation (CSI Division 00 - General Requirements)

**00-001: Update Total Project CAPEX Range (Phase 1 and Ultimate)**
- **Description:**
  - Review cost tables at the end of each BOD division page
  - Consolidate all BOD updates into revised total project cost estimate
  - Provide Phase 1 CAPEX (initial 12 MW deployment) and ultimate CAPEX (20-24 MW with all phases)
  - Update financial model with revised assumptions (traditional UPS phasing, chiller expansion, BESS elimination savings, etc.)
  - Accuracy: Class 3 (+/- 15-20%)

- **Assigned To:** PGCIS cost estimating team
- **Dependencies:** All design decisions from Priority 2 actions (26-001 through 02-001)
- **Impact:** Financial model baseline, investor materials, IRR calculations, lender presentations
- **Target Date:** November 2025
- **Notes:** This consolidates previous F-001, F-002, F-003, F-004 into single comprehensive cost update action.

---



---

## CAMELOT SOW COORDINATION SUMMARY

**Key Camelot Deliverables and PGCIS Actions:**

### Task 1: SPP Oklahoma Market Study ($9,500, 3 weeks)
**Camelot Provides:**
- Substation hosting capacity near site
- Nearby transmission lines with voltage information
- Interconnect queue position recommendations
- Proximity to fiber and water
- Fuel mix at interconnecting substation

**PGCIS Actions:**
- Use for 33-001 (utility interconnection study) - informs application and identifies constraints
- Cross-check substation capacity findings with OG&E interconnection study results
- Validate fiber proximity findings with 27-001 (fiber routing)

### Task 2: Net Load Analysis (3 weeks)
**Camelot Provides:**
- BESS revenue stack analysis (Day-Ahead, Real-Time, Regulation, Reserve, Spinning)
- 12x24 heatmap load profiles
- 8760 hourly dispatch and performance results
- PV+S (Solar + Storage) load coverage metrics

**PGCIS Actions:**
- NOTE: Economic BESS already rejected (negative NPV per Excess Solar Monetization Strategy)
- Use net load analysis to validate solar contribution calculations (cross-check with Solar Contribution Validation document)
- Confirm facility load profiles used in analysis align with PUE assumptions (1.2-1.3)
- Archive BESS revenue findings as reference (not pursued, but useful for future consideration)

### Task 3: Ad Hoc Services (T&M)
**Camelot Provides:**
- Fiber design drawings (T&M basis)

**PGCIS Actions:**
- Use for 27-001 (fiber routing to site and Google campus)
- Coordinate with Aaron's Google GCP outreach
- Clarify T&M scope and budget with Camelot before proceeding

---

## SUMMARY OF ACTIONS BY DIVISION

**Total New Actions: 18** (using CSI division naming convention)

### Utilities & Power (CSI Div 33) - 5 actions
- 33-001: Comprehensive utility interconnection study & grid power validation ⭐ CRITICAL
- 33-002: Confirm natural gas capacity (existing as A-002)
- 33-003: Determine POI configuration
- 33-004: Water/wastewater availability study
- 33-005: Diesel fuel storage strategy

### Electrical Systems (CSI Div 26) - 4 actions
- 26-001: Confirm UPS equipment specifications and pricing
- 26-002: Confirm final generator configuration
- 26-003: Validate substation transformer sizing (existing as A-024)
- 26-004: Electrical room configuration (indoor vs outdoor)

### Mechanical Systems (CSI Div 23) - 4 actions
- 23-001: Finalize chiller plant sizing
- 23-002: Confirm RDHx deployment scope
- 23-003: Validate CDU sizing
- 23-004: Confirm rooftop AHU configuration

### Building & Site (CSI Divs 02-14, 31-32) - 2 actions
- 02-001: Confirm building test fit and equipment yard locations
- 02-002: Validate slab-on-grade design (existing as A-043)

### Connectivity (CSI Div 27) - 1 action
- 27-001: Review Camelot fiber study & coordinate Aaron's Google outreach (existing as A-040, A-020)

### Cost & Financial (CSI Div 00) - 1 action
- 00-001: Update total project CAPEX range (consolidated cost update)

### Documentation (CSI Div 01) - 1 action
- 01-001: Finalize BOD documents for MEP handoff

---

## CROSS-REFERENCE TO EXISTING ACTIONS

**Actions ALREADY TRACKED in Actions.csv:**
- A-002 (natural gas service) = 33-002
- A-024 (substation transformer sizing) = 26-003
- A-043 (slab-on-grade validation) = 02-002
- A-018 (geotech review) = 02-002 dependency
- A-032 (cooling strategy evaluation) = 23-001, 23-002 related
- A-034 (CapEx comparison for cooling) = 23-001 related
- A-019 (RDHx vs fan walls CapEx) = 23-002, 23-003 related
- A-047 (RDHx deployment) = 23-002, 23-003 related
- A-040 (Camelot studies) = 27-001
- A-020 (Camelot GCP analysis) = 27-001 (Aaron contact)

**NEW ACTIONS (not in existing Actions.csv):**
- 33-001: Comprehensive utility interconnection study ⭐ MOST CRITICAL
- 33-003: Determine POI configuration
- 33-004: Water/wastewater availability study
- 33-005: Diesel fuel storage strategy
- 26-001: UPS equipment specifications
- 26-002: Final generator configuration
- 26-004: Electrical room configuration
- 23-004: Rooftop AHU configuration
- 02-001: Building test fit and equipment yards
- 00-001: Update total project CAPEX (consolidated)
- 01-001: Finalize BOD for MEP handoff

---

## RECOMMENDED NEXT STEPS

1. **IMMEDIATE (Week 1):** Initiate 33-001 (utility interconnection study) - THE foundational critical path item
2. **Review Camelot Task 1 findings** (expected early Nov) to inform 33-001 application
3. **Confirm which new actions** should be added to Actions.csv
4. **Assign target dates** for all new actions
5. **Update Actions.csv** with confirmed new actions using CSI division naming convention

---

**Tags:** #saga-project #action-items #bod-confirmation #utility-interconnection #design-decisions #camelot-coordination

**Related Documents:**
- [[Action Items.csv]] - Existing action tracking
- [[_BOD - Exec Summary and TOC]] - Basis of Design overview
- [[Why BESS Should Not Be UPS]] - Technical analysis supporting design decisions
- [[Excess Solar Monetization Strategy]] - Economic analysis supporting design decisions
- [[Camelot SOW Summary]] - Consultant scope and deliverables
