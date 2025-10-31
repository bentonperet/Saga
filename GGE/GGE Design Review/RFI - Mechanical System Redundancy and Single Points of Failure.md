# REQUEST FOR INFORMATION (RFI)
## Biliki Data Center - Mechanical System Redundancy and Single Points of Failure

**Created:** 2025-10-31 00:00
**Tags:** #gge #data-center #mechanical #rfi #tier-iii #spof
**Related:** [[Design Review Findings - Mechanical System Single Points of Failure]], [[RFI - Critical Design Clarifications Required]], [[GGE Design Review]]

**Project:** Biliki Data Center, Tbilisi, Georgia
**RFI Number:** GGE-RFI-MECH-002
**Document Reviewed:** GE01-CAS-0004-CO6-C02 (Mechanical Flow Diagram, Sheet 8, Rev C02, dated 27.10.2025)
**Date Issued:** October 31, 2025
**Priority:** **CRITICAL** - Required before Uptime Institute Tier III Design Submission
**Requested Response Date:** November 7, 2025

---

## RFI Summary

**Subject:** Mechanical cooling system drawing lacks sufficient detail to verify Tier III concurrent maintainability compliance, particularly regarding chilled water distribution redundancy.

**Issue:** The mechanical flow diagram GE01-CAS-0004-CO6-C02 is a schematic-level drawing that does not clearly show:
1. Whether redundant A/B chilled water distribution paths exist to IT spaces
2. Equipment specifications and capacities
3. Isolation valve locations and concurrent maintenance strategy
4. Expansion tank sizing basis

**Positive Finding:** CRV1 and CRV2 chiller plants ARE connected at utility level via "MAKEUP RING" and shared river water loop, providing system-level integration.

**Requested Action:**
1. Clarify whether redundant A/B chilled water distribution exists
2. Provide equipment specifications and redundancy configurations
3. Provide more detailed P&ID showing isolation valves and maintenance boundaries
4. Address five (5) identified single points of failure or clarify why they are not SPOFs

---

## Background: Tier III Concurrent Maintainability Requirements

Uptime Institute Tier III Certification requires:

> **"Concurrently Maintainable: Any single component in the distribution path can be removed from service for planned maintenance without impacting IT operations. This requires redundant distribution paths (A/B) and sufficient capacity in both paths."**

**Specific Requirements for Mechanical Systems:**
- **N+1 or 2N chiller configuration** with ability to maintain one chiller while maintaining full cooling capacity
- **Redundant chilled water distribution paths (A/B)** to all critical cooling equipment
- **Isolation valving** at strategic locations to allow component maintenance without system shutdown
- **Redundant pumps** in primary and secondary loops
- **Redundant auxiliary systems** (makeup water, expansion, degassing)

**Current Design Review Status:**
The schematic-level drawing (GE01-CAS-0004-CO6-C02) does not provide sufficient detail to verify these requirements. More detailed P&ID and equipment specifications are needed.

---

## CRITICAL CLARIFICATIONS REQUIRED

### CRITICAL ISSUE #1: Chilled Water Distribution Redundancy (A/B Paths to IT Spaces)

**Drawing Reference:** GE01-CAS-0004-CO6-C02, center section showing distribution piping

**Observation:**
The mechanical flow diagram shows DN250 distribution headers from each chiller plant to IT spaces:
- **CRV1** → Single visible DN250 header → V1, V2, V3, V4, V5 VIP rooms
- **CRV2** → Single visible DN250 header → E-A Enterprise, HB Hub computer rooms
- **No redundant parallel headers clearly shown**
- **No cross-tie visible** between CRV1 and CRV2 distribution headers

**Tier III Concern:**
If this represents truly single-path distribution (no A/B redundancy), it violates concurrent maintainability requirements. However, this may be a limitation of the schematic-level drawing detail.

**Questions:**

1. **Do redundant A/B chilled water distribution paths exist from each chiller plant to IT spaces?**
   - If YES: Please provide updated drawing or P&ID showing A/B path segregation
   - If NO: Is cross-tie planned between CRV1 and CRV2 distribution headers to allow back-feed?

2. **For the DN250 headers shown on the drawing:**
   - Does "DN250" represent a single pipe or dual parallel pipes (A/B)?
   - Are there actually two physical headers (supply A/B, return A/B) that are not distinguished on this schematic?

3. **Isolation valve strategy:**
   - Where are isolation valves located to enable concurrent maintenance?
   - Can distribution piping sections be isolated without IT impact?
   - What is the maximum IT zone affected by any single isolation?

4. **Cross-tie between plants:**
   - Is cross-tie piping provided between CRV1 and CRV2 distribution headers?
   - If yes, what is the pipe size and capacity?
   - Can each chiller plant back up the other at full or partial capacity?

**Required Documentation:**
- ✅ **More detailed P&ID** showing:
  - A/B distribution path segregation (if exists)
  - Isolation valve locations with valve tag numbers
  - Cross-tie connections between plants (if exists)
  - Concurrent maintenance isolation boundaries
- ✅ **Written narrative** explaining concurrent maintenance strategy and demonstrating Tier III compliance
- ✅ **If single-path confirmed:** Provide justification or redesign plan

---

### CRITICAL ISSUE #2: Equipment Specifications Missing

**Drawing Reference:** GE01-CAS-0004-CO6-C02, entire drawing

**Observation:**
The schematic shows piping layout but **lacks all equipment specifications**:
- No chiller make, model, capacity, or quantity
- No pump specifications
- No heat exchanger capacities
- No system design temperatures or flow rates
- No control valve specifications

**Impact:**
Cannot verify:
- N+1 chiller redundancy adequacy
- Pump redundancy and capacity
- System capacity vs. IT cooling load
- Distribution pipe sizing adequacy
- Tier III compliance

**Questions:**

5. **Chiller Specifications (CRV1/CH/4 and CRV2/CH/4):**
   - How many chillers per chiller plant? (CRV1 and CRV2)
   - Cooling capacity per chiller (kW or refrigeration tons)?
   - Manufacturer, model, refrigerant type?
   - What is the redundancy configuration (N+1, N+2, 2N)?
   - Total installed cooling capacity vs. required IT cooling load?

6. **Pump Specifications:**
   - Primary chilled water pumps: Quantity, flow (L/s or GPM), head (m), motor power (kW)?
   - Secondary/distribution pumps: Specifications per loop?
   - Condenser water pumps (if applicable): Specifications?
   - What is the pump redundancy configuration (duty/standby, N+1)?

7. **Heat Exchanger Specifications:**
   - River water plate heat exchanger (PHE): Capacity (kW), approach temperature (ΔT), flow rates?
   - Ground thermal heat exchanger: Type, capacity, configuration?

8. **System Design Parameters:**
   - Chilled water supply/return temperatures (e.g., 12°C/18°C)?
   - Total system flow rate (L/s)?
   - Design heat rejection capacity (MW thermal)?
   - Free cooling operating range (river water temperature)?

**Required Documentation:**
- ✅ **Mechanical equipment schedule** with all specifications listed above
- ✅ **Load calculation** showing IT cooling load vs. installed chiller capacity
- ✅ **Pump head calculation** for distribution system pressure drop
- ✅ **Redundancy verification** demonstrating N+1 or 2N compliance
- ✅ **Heat balance diagram** showing cooling capacities and flows

---

## HIGH-PRIORITY CLARIFICATIONS REQUIRED

### Issue #3: Expansion Tank Sizing Verification

**Drawing Reference:** GE01-CAS-0004-CO6-C02, "Expansion Tank 0,5 t" symbols throughout

**Observation:**
Drawing shows multiple expansion tanks labeled **"0,5 t"** (500 liters / 132 gallons each).

**Sizing Concern:**
For a ~5.6 MW data center cooling system:
- Estimated total system volume: **100-150 m³**
- Thermal expansion (5°C to 40°C, 35°C ΔT): ~1.5% = **1.5-2.25 m³**
- Required expansion capacity with safety factor: **5-10 m³ total**
- Current capacity appears to be 6× 0.5t = **3.0 m³ (marginal, no redundancy)**

**Consequences if undersized:**
- Frequent pressure relief valve discharge
- Constant makeup water operation
- Pump cavitation risk
- Pressure fluctuations

**Questions:**

9. **What is the basis for expansion tank sizing?**
   - Total system volume (m³)?
   - Design temperature range (min/max °C)?
   - Calculated thermal expansion volume?

10. **How many 0.5 t expansion tanks are provided, and what is total expansion capacity?**

11. **Has this been verified by mechanical engineer as adequate for system volume and temperature range?**

12. **Are expansion tanks redundant (dual vessels with isolation valves for maintenance)?**

**Recommended Action:**
- Recalculate expansion requirements per ASHRAE/EN 12828 guidelines
- Likely need to upsize to **5-10 m³ total** with redundancy

**Required Documentation:**
- ✅ **Expansion tank sizing calculation** showing:
  - System volume determination
  - Expansion volume calculation
  - Selected tank size and quantity
  - Pre-charge pressure calculation
  - Manufacturer specifications for selected vessels

---

### Issue #4: Water Storage Function and Autonomy Clarification

**Drawing Reference:** GE01-CAS-0004-CO6-C02, bottom corners showing water storage tanks

**Observation:**
Substantial water storage shown:
- **Left side (CRV1):** "Water storage 50 m³ - A1" + "Water storage 50 m³ - B1" = 100 m³
- **Right side (CRV2):** Two "Water storage 125 m³" = 250 m³
- **Total:** 350 m³ (92,000 gallons)

**Critical Questions:**

13. **What is the primary function of these water storage tanks?**
    - Makeup water storage for closed-loop system replenishment?
    - Emergency condenser water supply during river water system outage?
    - Both functions combined?

14. **If emergency condenser water supply, what is the design autonomy?**
    - At full cooling load (8.4 MW heat rejection), typical condenser flow ≈ 1,620 m³/hr
    - 350 m³ storage ÷ 1,620 m³/hr = **13 minutes runtime**
    - Is 13 minutes acceptable, or is different load assumption used?
    - Typically 2-4 hours minimum is recommended for emergency cooling

15. **What is the backup strategy if river water system becomes unavailable?**
    - Municipal water connection?
    - Stored water for limited runtime?
    - Partial IT load shedding?
    - Facility shutdown procedures?

16. **Are water storage tanks redundant?**
    - Duty/standby configuration?
    - Can one tank be isolated for cleaning/maintenance?
    - Isolation valves provided?
    - Automatic switchover capability?

**Required Documentation:**
- ✅ **Water storage design basis memo** clarifying:
  - Tank purpose and function
  - Sizing rationale and autonomy calculations
  - Backup cooling strategy during river water outage
  - Redundancy and maintenance isolation approach
- ✅ **Emergency cooling contingency plan** if river water unavailable

---

### Issue #5: Makeup Water System Configuration

**Drawing Reference:** GE01-CAS-0004-CO6-C02, bottom sections labeled "Makeup water A" and "Makeup water B"

**Observation:**
Drawing shows "MAKEUP RING" label, indicating makeup water systems are interconnected (positive finding).

**Questions:**

17. **Makeup water pump configuration:**
    - Are makeup water pumps redundant (dual pumps per system or shared)?
    - What is the pump redundancy configuration (duty/standby, N+1)?
    - Automatic switchover provided?

18. **Makeup water source:**
    - Potable water connection?
    - Stored water tanks?
    - Dual sources for redundancy?

19. **Makeup water treatment:**
    - Water treatment system required?
    - Filtration, softening, chemical treatment?
    - Treatment system redundancy?

20. **Does "MAKEUP RING" provide full redundancy?**
    - Can makeup system A supply CRV2 loop if makeup system B fails?
    - Are isolation/control valves provided for cross-feed?

**Required Documentation:**
- ✅ **Makeup water system P&ID** showing pump configuration, controls, and redundancy
- ✅ **Design narrative** explaining makeup water philosophy and "MAKEUP RING" implementation

---

### Issue #6: Degassing System Redundancy

**Drawing Reference:** GE01-CAS-0004-CO6-C02, "DC Degassing line" shown in legend

**Observation:**
Drawing indicates degassing systems ("DC" lines) but does not show redundancy.

**Function:** Critical for preventing air accumulation, pump cavitation, heat transfer degradation, and corrosion.

**Questions:**

21. **Are degassing systems redundant (dual units with isolation valving)?**

22. **Can degassing units be maintained without shutting down the cooling loop?**

23. **Are automatic air vents provided at high points throughout system as backup?**

24. **What type of degassing system is used?**
    - Vacuum degasser?
    - Air separator with compression tank?
    - Microbubble air eliminator?

**Required Documentation:**
- ✅ **Degassing system specifications** including:
  - Type and manufacturer
  - Capacity and flow rate
  - Redundancy configuration
  - Maintenance isolation strategy

---

### Issue #7: Seismic Design for Zone VIII

**Drawing Reference:** Related to entire mechanical system, but not shown on schematic

**Background:**
Basis of Design states project site is **Seismic Zone VIII with PGA 0.25-0.27 g** (moderate-high seismic hazard). Mechanical schematic shows no seismic design features.

**Tier III Concern:**
Seismic event could cause:
- Rigid piping failure at equipment connections → flooding
- Pipe separation → loss of cooling
- Equipment toppling
- Loss of concurrent maintainability

**Questions:**

25. **Have seismic design criteria been developed for mechanical systems per Zone VIII requirements?**

26. **Will detailed mechanical drawings show:**
    - Flexible pipe connections at all rotating equipment (pumps, chillers)?
    - Seismic bracing for distribution piping per ASCE 7-16?
    - Seismic separation joints where piping crosses building expansion joints?
    - Equipment anchorage details per IBC Chapter 13?

27. **Has seismic analysis been performed for:**
    - Chiller anchorage and center of gravity?
    - Large-bore distribution piping (DN250) support and sway bracing?
    - Water storage tank anchorage and sloshing analysis?

**Recommended Actions:**
- Develop seismic design criteria document for Zone VIII mechanical systems
- Add seismic details to P&ID and installation drawings
- Specify flexible connections at all equipment
- Detail seismic bracing for piping per ASCE 7 Chapter 13
- Include seismic review in commissioning scope

**Required Documentation:**
- ✅ **Seismic design criteria document** for mechanical systems
- ✅ **Updated mechanical drawings** showing seismic details and bracing
- ⚠️ **Third-party seismic peer review** (recommended for Tier III in Zone VIII seismic zone)

---

## SUMMARY OF REQUESTED INFORMATION

### Critical Priority (Required Before Tier III Design Submission)

| Item | Question(s) | Required Documentation |
|------|-------------|----------------------|
| **1. Distribution Redundancy** | Q1-Q4 | Detailed P&ID showing A/B paths (if exist), isolation valves, cross-tie; concurrent maintenance narrative |
| **2. Equipment Specifications** | Q5-Q8 | Equipment schedule with chiller/pump/HX specs, load calculation, redundancy verification |

### High Priority (Required Before Construction Drawings)

| Item | Question(s) | Required Documentation |
|------|-------------|----------------------|
| **3. Expansion Tank Sizing** | Q9-Q12 | Expansion tank sizing calculation, verification, updated specifications |
| **4. Water Storage Function** | Q13-Q16 | Design basis memo, autonomy calculation, emergency cooling plan |
| **5. Makeup Water System** | Q17-Q20 | Makeup water P&ID showing pumps, controls, ring configuration |
| **6. Degassing Redundancy** | Q21-Q24 | Degassing system specs with redundancy details |
| **7. Seismic Design** | Q25-Q27 | Seismic criteria document, updated drawings with seismic details |

---

## TIER III CERTIFICATION IMPACT

**Current Status:** Cannot verify Tier III mechanical system compliance due to insufficient detail on schematic-level drawing GE01-CAS-0004-CO6-C02.

**Positive Finding:**
✅ CRV1 and CRV2 chiller plants ARE connected at utility level ("MAKEUP RING", river water loop) - demonstrates system-level integration

**Critical Uncertainties:**
❓ Chilled water distribution redundancy (A/B paths to IT spaces)
❓ Equipment specifications and N+1 chiller verification
❓ Isolation valve strategy for concurrent maintenance
❓ Expansion tank adequacy
❓ Water storage function and emergency cooling autonomy

**Confirmed Deficiency:**
❌ Expansion tanks appear undersized (3.0 m³ vs. 5-10 m³ required)

**Required for Tier III Approval:**
1. Confirmation that redundant A/B distribution paths exist (or will be added)
2. Detailed P&ID showing isolation valve locations and concurrent maintenance boundaries
3. Equipment specifications confirming N+1 redundancy
4. Expansion tank sizing verification and upsize if needed
5. Clarification of water storage function and emergency cooling strategy

**Timeline Impact:**
- **If A/B redundancy exists:** 1-2 weeks to update drawings and provide documentation
- **If A/B redundancy does NOT exist:** 3-4 weeks for distribution redesign + 1-2 weeks review
- Critical path for Tier III submission

---

## RECOMMENDED ACTIONS

**Immediate (This Week):**
1. Convene design team meeting to review RFI and clarifications needed
2. Confirm whether A/B distribution paths exist but are not shown on schematic
3. Identify who will provide responses to each question (equipment engineer, mechanical engineer, design manager)

**Short-Term (Within 2 Weeks):**
4. Provide written responses to all 27 questions in this RFI
5. Issue updated P&ID or flow diagram showing:
   - A/B distribution paths (if exist)
   - Equipment specifications and capacities
   - Isolation valve locations
   - Concurrent maintenance boundaries
6. Provide equipment schedules and specifications
7. Perform expansion tank sizing calculation

**Before Tier III Submission (Within 4 Weeks):**
8. Issue complete set of mechanical drawings demonstrating Tier III compliance:
   - Detailed P&ID with valve tags
   - Equipment schedules
   - Isolation valve schedule
   - Concurrent maintenance narrative
9. Provide all required documentation listed in this RFI
10. Conduct internal design review to verify Tier III compliance
11. Consider third-party peer review before Uptime Institute submission

---

## REFERENCES

- **Uptime Institute Tier Standard: Topology (ANSI/TIA-942)** - Concurrent maintainability requirements
- **ASHRAE TC 9.9** - Mission Critical Facilities, Data Centers, Technology Spaces
- **ASHRAE Handbook - HVAC Systems and Equipment, Chapter 13** - Expansion tanks and air elimination
- **ISO/IEC 22237-3** - Data centre facilities and infrastructures - Part 3: Building construction
- **EN 12828** - Heating systems in buildings - Design for water-based heating systems
- **ASCE 7-16, Chapter 13** - Seismic Design Requirements for Nonstructural Components
- **IBC 2021, Chapter 16** - Structural Design (including seismic)
- **Eurocode 8** - Design of structures for earthquake resistance
- **ASME B31.9** - Building Services Piping

---

## CONTACT INFORMATION

**RFI Issued By:**
Design Review Team
Biliki Data Center Project
Email: [To be completed]
Phone: [To be completed]

**RFI Directed To:**
CAS GmbH - Mechanical Engineering Team
Project: GEO01 - Biliki Data Center
Attention: Mechanical Engineer of Record / Project Manager

**Requested Response Date:** November 7, 2025
**Response Method:** Written responses to all questions + updated drawings and documentation

**Please respond to all questions and provide requested documentation by the response date to maintain Tier III submission schedule.**

---

## RFI TRACKING

**RFI Number:** GGE-RFI-MECH-002
**Date Issued:** October 31, 2025
**Priority:** CRITICAL
**Status:** OPEN - Awaiting Response
**Related RFIs:**
- GGE-RFI-ELEC-001 (Electrical Capacity and Transformer/Generator Sizing)
- GGE-RFI-MECH-001 (if exists - previous mechanical RFIs)

**Related Documents:**
- [[Design Review Findings - Mechanical System Single Points of Failure]]
- [[Design Review Findings - Biliki Data Center]]
- [[RFI - Critical Design Clarifications Required]]
- GE01-CAS-0004-CO6-C02 (Mechanical Flow Diagram under review)
- GGE-CAS-DES-BOD-C02 (Basis of Design)

---

## RESPONSE INSTRUCTIONS

**Please provide:**

1. **Written responses** to Questions 1-27 in this RFI
2. **Updated mechanical drawings:**
   - Detailed P&ID showing A/B distribution (if exists), isolation valves with tags
   - Or confirmation that schematic-level drawing will be followed by detailed P&ID later
3. **Equipment schedules and specifications:**
   - Chiller schedule (qty, capacity, make/model, redundancy)
   - Pump schedule (qty, flow, head, power, redundancy)
   - Heat exchanger schedule
   - Expansion tank schedule
   - Water storage tank schedule
4. **Calculations:**
   - Expansion tank sizing calculation
   - Water storage autonomy calculation (if emergency cooling function)
   - Load calculation (cooling capacity vs. required load)
5. **Design memos/narratives:**
   - Concurrent maintenance strategy
   - Water storage function and emergency cooling plan
   - Makeup water ring configuration
   - Seismic design approach

**Response Format Options:**
- Email with attached PDF documents
- Design review meeting with presentation (followed by written summary)
- Updated drawing package with cover letter addressing each question

**Follow-Up:**
Design review team is available for clarification meeting if needed before formal response.

---

**Thank you for your prompt attention to these critical design review questions. Clarification of these items is essential for Tier III certification path forward.**
