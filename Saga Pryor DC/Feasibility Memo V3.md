
# Requirements & Feasibility Memo
## Saga Energy – Pryor Data Center

**Date:** October 15, 2025
**Prepared by:** PGCIS Program Management Team
**Project:** Saga Energy – Pryor Data Center (Mayes County, Oklahoma)
**Purpose:** Decision-grade memo for review and design scoping

Note: THIS DOCUMENT CAN BE UPDATED AS AN INVESTOR FRIENDLY LETTER TO HELP WITH THE COMMUNICATION AFTER THIS PROJECT.

---

## 1. EXECUTIVE SUMMARY
### Project Overview
* **Scale:** ~7.4 MW IT load (48 AI racks @ 132 kW + 48 network racks @ 22 kW). Initial facility load is ~10 MW at a target PUE of 1.2–1.3, with site planning for future scalability.
* **Availability Target:** Tier III–equivalent (N+1 redundancy across all critical power and cooling systems to ensure concurrent maintainability).
* **Site:** 121-acre parcel in Mayes County, OK; approximately 4 miles by road from Google’s Pryor campus (fiber route diversity to be confirmed).
* **Integrated Energy:** A 12 MW solar array plus a Battery Energy Storage System (BESS), owned by Saga Energy, will be integrated with the facility. The final interconnection approach (single vs. dual POI; behind-the-meter vs. export) will be determined via a utility study.

### Strategic Context
This project is de-risked by several strategic advantages that strengthen investor confidence:
1.  **Proven Design Foundation:** The project will be based on Schneider Electric's RD109 reference design, providing a validated and reliable foundation for the core electrical and mechanical architecture.
2.  **Renewable Integration:** The 12 MW solar + BESS system provides a key sustainability differentiator and enables a potential behind-the-meter (BTM) power strategy (critical given grid interconnection timeline.
3.  **Financial Upside:** Shifting to a power pass-through pricing model removes commodity risk from the operator and is projected to lift the project IRR from **12.1% to 15-19%**.
4.  **Strategic Market Position:** The site's proximity to Google’s campus positions it to capture customers seeking low-latency interconnection, pending confirmation of carrier route diversity and Google Cloud Platform (GCP) onramp feasibility.

### Critical Path Decisions
Five key decisions must be resolved during the initial planning phase to maintain schedule:
1.  **Utility Interconnection Strategy:** Finalize the approach for interconnecting the ~7.4 MW data center load and the 12 MW solar plant with the utility grid.
2.  **Generator Fuel & Siting:** Determine the optimal fuel source (diesel vs. natural gas) and placement (indoor vs. outdoor), which impacts cost and the building envelope.
3.  **Power Pricing Model:** Formally confirm and adopt the power pass-through model to secure the projected IRR improvement.
4.  **Raised Floor Elimination:** Validate the use of overhead power and cooling distribution to reduce capital costs and accelerate the construction schedule.

### Validation Studies Status
Comprehensive due diligence is underway to resolve key feasibility questions.

**Reports Expected Early November (following mid-October site visit):**
* Critical Issues Analysis (Cultural/Ecological)
* Permitting Matrix
* ALTA/NSPS Land Survey
* Phase I Environmental Site Assessment (ESA)
* Water Delineation Study
* Desktop Geotechnical Analysis

**Additional Consultant Engaged For the Following:**
* SPP Oklahoma Market Study
* Net Load Analysis (Data Center + Solar)
* Fiber and Telecom Carrier Analysis

---

## 2. DESIGN FOUNDATION & VALIDATED ELEMENTS
### What's Already De-Risked
This project’s schedule and budget are significantly de-risked by using **Schneider Electric's RD109 reference design package**. This provides a  engineering baseline for all major systems, which PGCIS will optimize for this specific site and application.

**Electrical Architecture (PGCIS will validate and optimize):**
*Why It Matters: Reduces engineering time and procurement risk for major equipment.*
- 138 kV to 13.8 kV on-site substation | *Open question: Substation transformer capacity needs to be validated. A single transformer sized only for the initial load may be insufficient. Sizing should account for the full facility load, BESS charging, and future growth (e.g., 12-15 MVA or dual transformers for redundancy).*
- 4× 3750 kVA generators (fuel type to be confirmed in Decision #2) | *Open question: This N+1 configuration from RD109 is a baseline. The final size, quantity, and control strategy must be confirmed via a dynamic power/capacity study that models the interplay with the solar, BESS, and specific IT load profiles.*
	- INVESTIGATING TURBINE AND/OR GENERATORS
- 8× 1500 kW UPS + 2× 200 kW UPS (Li-ion batteries) | *Open question: What is the rationale for the extra 2× 200 kW UPS units? (e.g., for control systems, network rooms, or other auxiliary loads?)*
	- **BESS-AS-UPS CONFIRMED: 12MW/48MWh configuration provides $6.5-8.5M savings vs traditional UPS**
- Medium-voltage switchgear and OCP-compliant rack power distribution | *Open question: Why is OCP compliance specified for this project? (This is typical for hyperscale clients but may not be required for all enterprise colocation tenants.)*
	- TO-DO ASK YOUR CONSULTANT ON OCP REASONING

**Mechanical Architecture (PGCIS will validate and optimize):**
*Why It Matters: Establishes a clear path to achieving the target PUE with proven cooling technology.*
- 3× air-cooled chillers + 5× fluid coolers with adiabatic assist | *Open question: Have hybrid air-cooled chillers (with integrated free cooling capabilities) been evaluated as an alternative to fluid coolers?*
	- EVALUATING ALTERNATE CHILLERS
- 9× liquid-to-liquid CDUs (MCDU-50 equivalent) for AI rack cooling | *Open question: Do we include this now? or wait until we know the DC client compute type? (Pre-installing CDUs accelerates deployment for AI clients but adds upfront cost.)*
- Hot aisle containment with BMS/DCIM integration
- N+1 redundancy on all critical cooling components

**PGCIS Recommendation:** Consider **rear-door heat exchangers (RDHx)** for air-cooled racks instead of fan walls. Fan walls are effective for bulk cooling but limit flexibility in allocating cooling capacity to individual customers. RDHx offers per-rack cooling, enabling denser air-cooled deployments and greater customer configurability, which could be a key service differentiator.

**IT Space Configuration (Validated):**
*Why It Matters: Confirms the facility can support high-value, high-density AI workloads.*
- 25,000 SF data hall footprint / white space
- SF of Critical Spaces within building envelope
- 132 kW/rack power density capability for AI workloads
- Mix of air-cooled (network) and liquid-cooled (AI) deployment zones
- CURRENTLY INCLUDING ADDITIONAL REQUIRED ROOMS FOR A SMOOTHLY OPERATING DC. THESE ARE NOT IN THE SCHNEIDER DESIGNS AND WILL MAKE THE TOTAL BUILDING LARGER.

---

## 3. CRITICAL PATH DECISIONS

### Decision #1: Utility Interconnection Strategy
**Context:**
The project requires coordinating the ~7.4 MW data center load with the 12 MW solar/BESS plant, both of which are Saga Energy assets. This is a microgrid interconnection design question, not a standard utility service request.

**Owner Questions to Resolve (Week 1–2):**
- **POI Configuration:** Single Point of Interconnection (POI) where the solar/BESS and data center operate behind one utility meter, or a dual POI with separate utility meters for each.
- **Microgrid Control System:** Have you considered how the microgrid control system will work for this project?
- **Utility Capacity:** What is OG&E's capacity along the nearby transmission lines and are there required upgrades?

**Action Required:**
- Initiate a formal interconnection request with OG&E that includes both the generation (solar) and load (DC) profiles.
- Saga to discuss internally about the preferred controls, metering, and protection strategy for microgrid, etc.

**Cost Exposure:**
- Utility upgrades (if required): $2M-$5M {CONFIRM}
- Interconnection fees and studies: $200K-$500K {CONFIRM}
- Schedule delay impact: 6-12 months if not initiated immediately {CONFIRM}

**Recommendation:**
Pursue a **single POI with BTM supply** as the primary option to maximize operational and energy cost benefits. Maintain a **dual-POI** configuration as a fallback if the utility study reveals significant technical or tariff-related roadblocks.

### Decision #2: Additional Power Generation

**Context:** Placeholder section as we investigate options for turbine, generators, etc.

---

### Decision #3: Power Pricing Model Confirmation

**Context:**
Financial model analysis shows significant IRR improvement if power is passed through to customers at cost rather than bundled into colocation pricing.

**Current Model (Power in OpEx):**
- Data center pays for power (~$159M over 25 years) {CONFIRM}
- Power cost included in OpEx, reducing margins
- **Project IRR: 12.1%**

**Recommended Model (Power Pass-Through):**
- Customer pays for power directly at cost (zero markup)
- Power cost removed from OpEx
- **Project IRR: 15-19%** (+3-7 percentage points)

**Industry Context:**
Power pass-through is standard practice in wholesale colocation. It removes commodity price risk from the operator, allows customers to optimize their own power procurement, simplifies financial modeling, and improves project returns.

**Solar Integration/Microgrid Opportunity:**
If the power pass-through model is adopted AND solar provides behind-the-meter power, customers may receive discounted renewable power. This is a powerful competitive differentiator.

**Action Required:**
- Confirm with investors/operators that power pass-through pricing is the approved commercial model.
- Align the power pricing model with the utility interconnection strategy (Decision #1).

**Owner Decision Date:** Immediate priority

---

### Decision #4: Raised Floor Elimination
**Context:**
The current Basis of Design (BoD) specifies a 24" raised access floor (RAF). Modern AI data centers increasingly use overhead distribution on a structural slab to reduce cost, improve airflow for certain cooling designs, and accelerate construction.

**Overhead Distribution (Alternative) vs. Raised Floor (Current Spec):**
- With the specified hot aisle containment and CDU cooling, the primary function of a raised floor would be for cable management, not air distribution.
- Overhead distribution via cable trays is standard for modern hyperscale and AI facilities and is fully compatible with the RD109 cooling concept.
- The structural slab must be designed for direct equipment loading, which requires geotechnical validation.

**Savings Potential (Net of Alternates):**
- While a raised floor may cost **$80–$100/SF** installed, eliminating it requires adding robust overhead trays, lifts, and stands. The **net avoidable cost is estimated at $35–$50/SF**.
- For a 25,000 SF data hall, this represents a **$0.9M–$1.25M** capex reduction and a **2–4 week** schedule pull-in.

**Risk/Dependencies:**
- The structural engineer must validate that the slab-on-grade can support all equipment loads (pending the geotechnical report).
- The cooling concept (CDUs + containment/RDHx) must be confirmed to **not** require underfloor air distribution.
- A detailed overhead cable management plan is required to avoid operational clutter.

**Action Required:**
- BIM lead and structural engineer to validate slab loading capability (pending geotechnical report).
- Confirm the final cooling design does not require an underfloor plenum.
- Review with the operations team to confirm preference and maintenance procedures.

**Owner Decision Date:** Following geotechnical analysis
**Cost/Schedule Impact:** ~$900K-$1.25M savings; 2-4 week schedule improvement {CONFIRM}

---

### Decision #5: BESS as UPS Architecture (NEW OPPORTUNITY)

**Context:**
Given that Saga Energy already owns a 12 MW solar array + BESS for renewable integration, there is a significant architectural opportunity to use the BESS to ALSO serve as the data center UPS system, eliminating or reducing the need for traditional UPS equipment.



**Three Architectural Options:**
#### **Option 1: Traditional (Baseline - RD109)**
- **Architecture**: UPS + BESS operate independently
- **UPS**: 8×1500kW + 2×200kW Li-ion ($8-10M)
- **BESS**: **12MW/48MWh** for solar storage only (**$24M**)
- **Generators**: 4×3750kVA ($7M)
- **Microgrid Controls**: Basic ($0.8M)
- **Total Power CAPEX**: **$39.8-41.8M**
- **Backup Duration**: 5-15 min (UPS) + 4.8 hrs (BESS for solar) + unlimited (gensets)

#### **Option 2: Pure BESS-as-UPS with Phased Deployment - RECOMMENDED**
- **Architecture**: BESS does everything, no separate UPS; inverters deployed in 2 phases
- **Phase 1**: **12MW/48MWh** (3×4MW inverters + full battery) for solar + UPS function (**$21.7-23.2M**)
- **Phase 2**: Add 4th 4MW inverter when ~75% leased (**+$2.8-3.5M**)
- **Generators**: 4×3750kVA ($7M)
- **Microgrid Controls**: Advanced (**$1.5M**)
- **Phase 1 CAPEX**: **$29.7-31.2M** (supports ~75% occupancy)
- **Total Power CAPEX (Full Buildout)**: **$32.5-34.7M**
- **CAPEX Savings**: **-$7.3-9.3M (-18% to -23%)** vs. Traditional ✅
- **Deferred CAPEX**: **~$2-3M deferred 8-12 months** (improved cash flow)
- **Backup Duration**: **Phase 1: 6 hrs @ 8MW; Phase 2: 4.8 hrs @ 10MW facility load** + unlimited (gensets)


**Reference Document:**
See more here: [[BESS as UPS Replacement - Feasibility Analysis]] **← Document reflects updated 12MW/48MWh sizing based on 10MW facility load validation**

---

### **BESS Sizing Rationale (12MW/48MWh)**

The BESS has been sized to support the **complete facility load**, not just the IT load:

| Load Component | Power | Basis |
|---|---|---|
| IT Load | 7.4 MW | 48 AI racks @ 132kW + 48 network @ 22kW |
| Cooling Load | 1.8-2.6 MW | PUE 1.2-1.3 minus IT load |
| Auxiliary Systems | 0.2-0.4 MW | Lighting, BMS, pumps, fans |
| **Total Facility Load** | **~10 MW** | **Validated via electrical load study** |

**BESS Configuration:**
- **16MW/48MWh** (4×4MW grid-forming inverters, phased deployment: 3 initially, 4th at ~75% occupancy)
- **N+1 Redundancy:**
  - Phase 1: 8MW available power with one inverter down (3×4MW inverters)
  - Phase 2: 12MW available power with one inverter down (4×4MW inverters)
- **Solar Symmetry:** 12MW inverter capacity in Phase 1 matches 12MW solar array for optimal microgrid balance
- **Phased Deployment:** Defers ~$2-3M CAPEX, aligns with facility lease-up

**Previous 7MW Sizing Error:**
The initial 7MW sizing only considered the 7.4MW IT load and did not account for cooling or auxiliary loads, resulting in a 30% undersizing.

**Validation Required:**
- Detailed electrical load study to confirm 10MW total facility load
- Vendor RFIs for 16MW/48MWh phased deployment pricing validation
- Update financial model with revised costs and phased deployment cash flows

### 2.4 Phased Deployment Strategy

**Rationale:** The facility will lease gradually over 12-24 months. Deploying all BESS inverter capacity on day 1 would tie up capital before it's operationally needed.

**Approach:**
- **Phase 1 (Initial):** Deploy 3×4MW inverters + full 48MWh battery
  - Provides 8MW with N+1 redundancy
  - Supports ~75-80% occupancy
  - Cost: $29.7-31.2M

- **Phase 2 (~75% leased):** Add 4th 4MW inverter
  - Provides 12MW with N+1 redundancy
  - Supports 100% occupancy
  - Incremental cost: $2.8-3.5M

**Infrastructure Sizing:** All electrical infrastructure (transformer, switchgear, buswork, enclosure) sized for 4 inverters from day 1. Only the 4th inverter hardware is deferred.

**Financial Impact:**
- Defers ~$2-3M in CAPEX by 8-12 months
- Aligns capital deployment with revenue generation
- Maintains contractual option for 4th inverter at locked pricing

---

## 4. VALIDATION STUDIES & KNOWN GAPS
### Studies Currently Underway (Reports Available Early November)
A comprehensive site and environmental due diligence package is in progress. Reports are expected in **early November**, following a site visit scheduled for mid-to-late October.

| Study | Purpose | Key Question It Resolves | Risk If Delayed / Flawed |
|---|---|---|---|
| **Critical Issues Analysis** | Identify cultural (historic/tribal) & ecological (endangered species) constraints. | Are there permitting showstoppers or costly mitigation requirements? | 3-6 month permit delay; $200K-$1M mitigation cost. |
| **Permitting Matrix** | Map all federal, state, and local permit requirements and timelines. | What is our exact regulatory roadmap and timeline? | Missed permit deadlines; schedule delays; expedite fees. |
| **ALTA/NSPS Land Survey** | Confirm legal boundaries, easements, encroachments, and topography. | Is the site legally and physically suitable for the design? | Costly redesign; title insurance issues; legal disputes. |
| **Phase I ESA** | Assess for historical or current environmental contamination. | Are there hidden environmental liabilities or cleanup costs? | Unknown remediation costs ($1M+); lender financing issues. |
| **Water Delineation Study** | Identify wetlands, streams, or floodplains regulated by the Army Corps or EPA. | Does the site require a federal permitting? | 6-12 month federal permit delay; $500K-$2M mitigation. |
| **Desktop Geotechnical Analysis** | Provide a preliminary assessment of soil bearing capacity and foundation needs. | Can we use standard foundations or are expensive deep foundations needed? | $500K-$1M foundation redesign if poor soils are found. |

---

### Additional Studies Scheduled or In Progress

Three market and infrastructure studies are underway with completion expected in **early-to-mid November**.

| Study | Purpose | Key Question It Resolves | Impact on Project |
|---|---|---|---|
| **SPP Oklahoma Market Study** | Analyze Southwest Power Pool dynamics, pricing, and renewable integration rules. | What are the economics of our solar export and power procurement strategy? | Informs financial model; validates solar revenue assumptions. |
| **Net Load Analysis** | Model the combined electrical profile of the data center and the solar/BESS plant. | How will our microgrid interact with the utility grid? | Critical input for Decision #1; informs interconnection design. |
| **Fiber Analysis** | Assess fiber routes, carrier presence, diversity, and GCP onramp logistics. | Do we have cost-effective, diverse, high-capacity connectivity? | De-risks connectivity; validates a core part of the customer value prop. |

---

### Additional Validation Possibilities (Owner-Initiated)
Beyond the studies underway, the following owner-led actions should be initiated immediately.

**1. Utility Coordination (CRITICAL PATH)**
- **Action:** Initiate formal coordination with OG&E regarding the 138 kV interconnection.
- **Goal:** Obtain a formal capacity study, interconnection timeline, required upgrades, and a cost estimate. This is the longest lead-time risk on the project.
- **Cost:** $50K-$150K for utility study fees.
- **Risk if Skipped:** An unknown utility lead time (potentially 6-18+ months) could render the entire project schedule unachievable.

**2. Telecom Carrier Pre-Engagement**
- **Action:** Engage major carriers (AT&T, Lumen, Zayo) and the Google Cloud Interconnect team for preliminary design and timeline discussions.
- **Goal:** Get preliminary route options, construction timelines, and Meet-Me-Room requirements directly from the providers to validate the Fiber Analysis.
- **Cost:** None (pre-sales engagement).
- **Risk if Skipped:** Carrier build-out schedules could lag facility completion, delaying revenue.
- **Note:** This may be a natural next step of the Fiber study that's pending…

**3. Local Permitting Pre-Application Meeting**
- **Action:** Schedule an informal pre-application meeting with Mayes County planning, building, and fire officials.
- **Goal:** Build relationships and uncover any "unwritten rules," political sensitivities, or specific local concerns (e.g., tornado hardening, generator noise) before submitting formal applications.
- **Cost:** None.
- **Risk if Skipped:** Unexpected local requirements could emerge late in the design process, causing delays and costly rework.

**4. Water & Wastewater Availability Study**
- **Action:** Formally request an availability and pressure study from the local water and sewer authority.
- **Goal:** Confirm that sufficient water capacity and pressure exist for both the cooling systems (adiabatic coolers) and domestic use, and that adequate wastewater capacity is available.
- **Cost:** $5K-$15K for study fees.
- **Risk if Skipped:** Lack of water/sewer capacity could require expensive new utility extensions or a change in cooling technology.

---

## 5. LONG-LEAD EQUIPMENT & COMMITMENT TRIGGERS
### Equipment Lead Times (Rough Estimates)
The following table outlines provisional lead times for critical equipment based on current market conditions. These are the primary drivers for the overall project schedule and must be validated via formal Requests for Quotation (RFQs) during the planning phase.

| Equipment                                       | Provisional Lead Time | Cost/Schedule Impact if Slipped |
| ----------------------------------------------- | --------------------- | ------------------------------- |
| **138 kV / 13.8 kV Transformer (12–15 MVA)**    | 52–60 weeks           | +$1M; 9–12 mo delay             |
| **Generators 4× 3750 kVA (diesel / dual-fuel)** | 44–52 weeks           | +$0.5M–$1M; 6–9 mo delay        |
| **MV Switchgear (13.8 kV) & Protection**        | 36–44 weeks           | +$0.2M–$0.4M; 3–5 mo delay      |
| **UPS (8×1500 kW + 2×200 kW Li-ion)**           | 40–48 weeks           | +$0.4M–$0.6M; 4–6 mo delay      |
| **Air-cooled Chillers**                         | 40–44 weeks           | +$0.3M–$0.5M; 4–5 mo delay      |
| **Liquid-to-Liquid CDUs (~MCDU-50)**            | 36–40 weeks           | +$0.2M–$0.3M; 3–4 mo delay      |

> **Note on Cost and Lead Times:** Ranges reflect significant global supply chain constraints for electrical equipment. Final dates, costs, and slotting will be confirmed via competitive RFQs with a minimum of two vendors per category.

WE ARE INVESTIGATING TURBINE TIMELINES TO MAKE SURE IT'S A VALID OPTION

---

## 6. DESIGN OPTIMIZATION OPPORTUNITIES

### Opportunity #1: Staging, Assembly & Burn-in Area
**Current Design:**
A standard shipping/receiving area with a loading dock is planned for equipment delivery.

**Optimization:**
Add a dedicated **technical workspace (~2,000 SF)** adjacent to shipping/receiving for assembling, configuring, and testing customer equipment before it enters the data hall.

**Rationale:**
- **Reduces Contamination:** Prevents cardboard dust, packaging, and other contaminants from entering the clean data hall environment, which is a major cause of equipment failure.
- **Accelerates Customer Onboarding:** Allows for pre-staging and "burn-in" testing of racks in a controlled area, reducing the "time-to-revenue" for new customer deployments.
- **Improves Operations:** Provides a dedicated space for break-fix activities without disrupting the live data hall.

**Cost Impact:**
- Additional building area: ~$150-$200 per SF × 2,000 SF = **$300K-$400K**
- **Return on Investment:** Faster customer deployments and reduced operational risk.

**Action Required:**
- Confirm operational workflow with the Saga Energy operations team.
- Update BIM spatial program to include this dedicated workspace.

---

### Opportunity #2: Staff Amenities for 24/7 Operations
**Current Design:**
A standard break room and kitchen are included in the plan.

**Optimization:**
Add **showers, lockers, and laundry facilities** to fully support 24/7 shift operations and emergency response scenarios.

**Rationale:**
- **Supports 24/7 Operations:** Essential for staff working long shifts, particularly during maintenance windows or incident response.
- **Enhances Emergency Readiness:** Allows the facility to support staff on-site for extended periods during severe weather or other emergencies.

**Cost Impact:**
- Additional building area and MEP: ~$200-$250 per SF × ~700 SF = **$140K-$175K**

**Action Required:**
- Confirm with Saga Energy HR/operations team.
- Update BIM spatial program and coordinate plumbing rough-in.

---

### Opportunity #3: Evaluating Cooling for Customer Flexibility (RDHx)
**Current Design:**
The Schneider RD109 design uses a mix of liquid-cooling CDUs and fan walls for air cooling.

**Consideration:**
As noted in the BoD, fan walls are effective but inflexible. They serve large, shared zones, making it difficult to customize cooling for individual customers.

**Alternative (RDHx):**
- Deploy **Rear-door Heat Exchangers (RDHx)** for air-cooled racks (e.g., network gear). This provides rack-by-rack cooling control.
- Reserve **CDUs for high-density AI racks** as planned.
- This hybrid approach allows for precise allocation of cooling capacity based on each customer's specific needs.

**Recommendation:**
If the business model is **flexible colocation** with varied customer densities, the higher upfront cost of RDHx is likely justified by the greater service flexibility. If the facility will be master-leased to a single tenant with a uniform deployment, the fan wall approach is lower-cost and sufficient.

**Action Required:**
- PGCIS mechanical lead to model the PUE and cost trade-offs of both scenarios.
- Align the final decision with the Saga Energy sales and marketing strategy.

---

### Opportunity #4: Marketing a "Cloud-Ready" GCP Onramp
**Current Design:**
A Meet-Me-Room with diverse fiber entries is planned.

**Optimization:**
Proactively design and pre-provision for a **Google Cloud Platform (GCP) onramp**, leveraging the site's 4-mile proximity to Google's campus.

**Rationale:**
- **Strategic Differentiator:** Creates a powerful marketing message of a "Cloud-Ready" or "Cloud-Adjacent" facility, which is highly attractive to enterprise customers.
- **Low-Latency Connectivity:** Offers an "easy button" for customers to establish a direct, low-latency, high-bandwidth connection to GCP for hybrid cloud workloads.
- **Revenue Opportunity:** Can create a new revenue stream through interconnection and cross-connect services.

**Action Required:**
- Engage the Google Cloud Interconnect team for preliminary discussions.
- Ensure the ongoing fiber analysis study includes diverse, low-latency routes to the Google campus.
- Incorporate GCP onramp readiness into the Meet-Me-Room design and all marketing materials.


---

## 7. INVESTOR READINESS SUMMARY
*We can use this section for later comms, once we make the above decisions and whatever else we come up with in the review.
### Confidence Factors
This project is **investment-ready**, anchored by the following de-risked elements:
1.  **Proven Design Foundation:** The Schneider RD109 reference design provides a validated technical baseline, eliminating significant engineering risk and accelerating the design process.
2.  **Strategic Energy Integration:** The on-site 12 MW solar + BESS, developed and owned by Saga Energy, provides a powerful sustainability narrative and operational cost advantages.
3.  **Robust Financial Upside:** Projected IRR of XX% - Analysis shows the project remains viable even with moderate capex overruns or slower-than-projected customer ramp-up.
4.  **Clear Path to Validation:** All major feasibility questions are being addressed by a comprehensive set of due diligence studies that are already underway and have clear delivery dates.

---
### Bounded Risk Exposure

All identified risks have been quantified with clear cost exposure ranges and have active mitigation plans.

WE WILL REDO THIS SECTION AFTER WE'VE GONE FURTHER, THIS IS AN EXAMPLE OF INFO THAT MIGHT HELP INVESTORS MAKE DECISIONS.

| Risk Category                  | Potential Cost Exposure | Mitigation Plan                                                                                      |
| ------------------------------ | ----------------------- | ---------------------------------------------------------------------------------------------------- |
| **Utility Interconnection**    | $2M–$5M                 | Utility study being initiated to define costs/timeline.                                              |
| **Geotechnical / Foundation**  | $500K–$1M               | Geotechnical study to follow, allowing for early foundation design.                                  |
| **Environmental / Permitting** | $200K–$1M               | Phase I ESA and water delineation studies in progress to identify any mitigation needs early.        |
| **Generator Configuration**    | $300K–$800K             | Decision on fuel/siting is a near-term priority, allowing costs to be locked.                        |
| **Equipment Lead Times**       | Schedule Risk           | Procurement strategy focuses on identifying triggers for placing orders on longest-lead items first. |

**Total Bounded Risk Range:** The primary identified cost risks fall within a **$3M - $8M** range, representing a manageable contingency for a project of this scale. All risks have active studies or decision gates in place.Camelot 

---
## CONCLUSION

The Saga Energy Pryor Data Center project is founded on a de-risked design, a compelling strategic location, and a robust financial model. The integration of on-site solar and BESS provides a significant competitive advantage in a market increasingly focused on sustainability.

Comprehensive due diligence is underway to address all known risks, and clear decision criteria have been established to ensure the project proceeds on a sound footing.

Pachyderm will continue to validate the assumptions for the internal MEP components in the data center and build the architectural renders. 

---
**Document Status:** Draft for Internal PGCIS Review




Notes From working with Erik:
- Air cooled chiller with free cooling is recommended.
- RDhx inside to reject the heat to the exterior cooling system.
- There needs to be a climate review and cooling 
- Consult the psychometric chart of Pryor and make sure chiller performs well in zone.

Benton - to review RD109 and highlight the changes to the cooling system.

Example pic of this chart:
![[Pasted image 20251016160839.png]]