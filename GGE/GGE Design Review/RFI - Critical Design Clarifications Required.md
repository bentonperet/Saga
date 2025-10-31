# REQUEST FOR INFORMATION (RFI)
## Biliki Data Center - Critical Design Clarifications Required

**Project:** Biliki Data Center, Tbilisi, Georgia
**Documents Reviewed:**
- GGE-CAS-DES-BOD-C02.pdf (Basis of Design, Rev C02)
- GE01-CAS-0004-CO6-C02.pdf (Mechanical Flow Diagram, Sheet 8)
- GE01-DES-PM00-OPR-0001_02_OPR_Change_Log (IFD)

**Date:** October 30, 2025
**Priority:** CRITICAL - Required before Uptime Institute Tier III Submission

---

## Executive Summary

The design review has identified **five (5) CRITICAL issues** that must be resolved before proceeding with Uptime Institute Tier III certification submission, equipment procurement, or construction commencement. These issues relate to fundamental electrical capacity and mechanical redundancy requirements for Tier III compliance.

**Status:** The OPR Change Log (IFD) addresses operational, security, and staffing matters but **does NOT resolve the critical electrical capacity and mechanical redundancy issues** identified below.

---

## CRITICAL ISSUES REQUIRING IMMEDIATE CLARIFICATION

### 1. POWER SOURCE CAPACITY MISMATCH (HIGHEST PRIORITY)

**Issue:**
The Basis of Design states:
- Primary power source: Mtkvari HPP = 3.7 MW
- Phase 2 IT load: 5.635 MW
- With PUE 1.5, total facility load = 8.45 MW

**Gap:** 8.45 MW required - 3.7 MW available = **4.75 MW shortfall**

**Questions:**
1. What is the capacity of the utility grid connection?
2. What is the power allocation strategy between HPP and utility grid for:
   - Phase 1 operation?
   - Phase 2 operation?
3. How is the "100% renewable baseline" claim justified if utility grid is required?
4. Can the facility operate on HPP alone, or is grid power mandatory for Phase 2?

**Required Documentation:**
- Utility service agreement showing contracted capacity
- Power source allocation diagram (HPP vs. grid by phase)
- Clarification memo addressing the 4.75 MW discrepancy

---

### 2. TRANSFORMER SIZING VERIFICATION

**Issue:**
Original design showed 3000 kVA transformers. OPR Change Log states "Transformer count reduced to align with actual IT load; future expansion space reserved" but provides **no new specifications**.

**2N Requirement:**
For Tier III compliance, each transformer must carry the full group load independently.

**Questions:**
1. How many transformers are in the revised design?
2. What is the capacity (kVA) of each transformer?
3. At full Phase 2 load (8.45 MW ÷ 0.95 power factor = 8.89 MVA), can a single transformer carry the full group load plus 25% margin?
4. What is the redundancy configuration (2N or N+1)?

**Required Documentation:**
- Updated electrical single-line diagram showing:
  - Transformer quantities and capacities
  - Redundancy topology (A/B distribution paths)
  - Load allocation per transformer group

---

### 3. GENERATOR SIZING VERIFICATION

**Issue:**
Original design: 4 × 2500 kVA generators
Minimum required for N+1 at full load: 3 × (8.89 MVA ÷ 3) = **3 × 3.0 MVA each**
Current capacity: 2500 kVA = 2.5 MVA = **insufficient**

**Questions:**
1. Has the generator sizing been revised? If so, what are the new specifications?
2. What is the redundancy configuration (N+1 or 2N)?
3. At full facility load (8.89 MVA), can the generators operate in N+1 configuration without overload?
4. What is the fuel consumption rate (L/h) for all generators at full load?

**Required Documentation:**
- Generator specification sheet (quantity, capacity, fuel consumption)
- Load calculation showing N+1 or 2N adequacy at full Phase 2 load

---

### 4. FUEL AUTONOMY CALCULATION ERROR

**Issue:**
BOD claims 72 hours of fuel autonomy with 20-ton fuel storage.

**Calculation:**
- 20 tons diesel ≈ 23,500 liters (at 0.85 kg/L)
- Generator fuel consumption at full load ≈ 0.3 L/kWh × 8.89 MW = 2667 L/h
- Actual runtime = 23,500 L ÷ 2667 L/h = **8.8 hours (not 72 hours)**
- Even with N+1 operation (3 of 4 generators): 23,500 L ÷ 2000 L/h = **11.75 hours**

**For 72 hours at N+1 configuration:**
Required fuel = 2000 L/h × 72h = **144,000 liters (169 tons)**

**Questions:**
1. What is the actual full-load fuel consumption rate (L/h)?
2. Is the 20-ton storage capacity correct, or has it been increased?
3. If 20 tons is correct, what is the actual runtime at full load in N+1 configuration?
4. If 72-hour target remains, what fuel storage capacity is required?

**Required Documentation:**
- Fuel consumption calculation at full facility load
- Fuel storage capacity verification or revision
- Corrected runtime claim based on actual storage and consumption

---

### 5. NO REDUNDANT COOLING PATHS (MECHANICAL DIAGRAM)

**Issue:**
Drawing GE01-CAS-0004-CO6 shows single cooling path to each IT space. Tier III requires concurrent maintainability: any single cooling component must be serviceable without IT impact.

**Tier III Requirement:**
Each critical space must have **two independent cooling paths (A/B)** with isolation valves.

**OPR Change Log states:** "Chiller Redundancy Clarification: Revised to reflect N+1 scalable to 2N"
**However:** The mechanical flow diagram has not been revised to show redundant distribution paths.

**Questions:**
1. Will the mechanical distribution be redesigned to provide redundant A/B cooling paths to each IT space?
2. Where will isolation valves be located to enable concurrent maintainability?
3. What are the chiller capacities and N+1 configuration details?

**Required Documentation:**
- **Updated mechanical flow diagram** showing:
  - Redundant A/B cooling paths to all IT spaces
  - Isolation valve locations and numbering
  - Equipment specifications (chillers, pumps, heat exchangers)
  - Demonstration that either path can be isolated without IT impact

---

## ADDITIONAL HIGH-PRIORITY CLARIFICATIONS

### 6. UPS Battery Runtime Specification Clarification
- **Current spec:** 10-15 minutes
- **Question:** At what load condition was this runtime calculated?
- **Required:** Confirmation that 10-15 minutes is at full Phase 2 IT load (5.635 MW)

### 7. Seismic Design Criteria
- **Current status:** Not specified
- **Required:** IBC 2021 or Eurocode 8 seismic design criteria for Zone 7 (high seismic risk)

### 8. River Water Cooling Risk Assessment
- **Current status:** Not addressed
- **Required:** Risk assessment for Mtkvari River water intake (flooding, debris, temperature variation, drought)

---

## RECOMMENDED ACTIONS

**Before Uptime Institute Tier III Submission:**

1. **Provide updated electrical single-line diagram** addressing items #1, #2, and #3
2. **Provide updated mechanical flow diagram** addressing item #5
3. **Provide fuel autonomy calculation memo** addressing item #4
4. **Provide power source clarification memo** addressing item #1
5. **Confirm UPS battery runtime** specification (item #6)

**Before Construction:**

6. Provide seismic design criteria documentation (item #7)
7. Provide river water system risk assessment (item #8)

---

## CONCLUSION

The design review confirms that the Biliki Data Center project has made excellent progress on operational, security, staffing, and compliance aspects. However, **five critical electrical and mechanical capacity issues remain unresolved** and must be addressed before:

1. Uptime Institute design document submission
2. Equipment procurement (transformers, generators, chillers)
3. Construction commencement

**We respectfully request CAS GmbH provide the clarifications and updated documentation outlined above at your earliest convenience.**

---

**Prepared by:** Design Review Team
**Date:** October 30, 2025
**Contact:** [To be completed]
