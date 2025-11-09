📄 Reading markdown file...
🔍 Parsing markdown...
   Found 85 blocks
🔐 Authenticating with Google...
📝 Creating Google Doc...

✅ Document published successfully!

   Title: RFI_001_Commissioning_Scope_Clarifications
   URL:   https://docs.google.com/document/d/1XqDgsE6KOlKDHoolbAXg0_GaVxKR1BH99N7vwSba-gM/edit

# REQUEST FOR INFORMATION (RFI)


**RFI Number:** RFI-001
**Project:** Riverbend Data Center Commissioning
**Client:** Hut 8
**Date Issued:** 2025-11-07
**Response Requested By:** [Date TBD]
**Submitted By:** [Your Company Name]
**Contact:** [Your Name, Email, Phone]

---

## PURPOSE

This Request for Information (RFI) is submitted to clarify commissioning scope, technical requirements, and commercial terms for the Riverbend Data Center Commissioning RFP dated October 2025. Responses to these questions are necessary to provide an accurate and complete proposal.

We respectfully request written responses to enable all proposers to work from consistent project information.

---

## SUMMARY OF CRITICAL QUESTIONS

| RFI #  | Topic            | Cost Impact | Schedule Impact    |
| ------ | ---------------- | ----------- | ------------------ |
| 001.01 | Switchyard Scope | $400K-$1.5M | CRITICAL PATH      |
| 001.02 | Controls Systems | $150K-$400K | IST schedule risk  |
| 001.03 | QA/QC Scope      | $100K-$2M+  | Early coordination |

**Total Potential Cost Variance from Critical Questions: $650K-$3.9M**

---

## CRITICAL QUESTIONS

The following 3 questions represent the highest priority items that significantly impact pricing, schedule, and technical approach. These questions address critical path dependencies and major cost drivers.

---

### RFI-001.01 - Switchyard Commissioning Scope and Timeline ⚠️ CRITICAL PATH

**RFP Reference:** Page 2, Ramp Schedule - Switchyard commissioning May 2026-July 2026; 300 MW available August 2026

**Question:**

**A.** What is the scope of switchyard commissioning? (check all that apply)
- [ ] Utility interconnection point and protective relaying
- [ ] Utility-owned equipment (coordinated witness/acceptance testing)
- [ ] Owner-owned switchyard equipment (transformers, switchgear, protection)
- [ ] 34.5kV primary distribution from switchyard to data halls
- [ ] Site substations and step-down transformers
- [ ] All of the above
- [ ] Other (please specify): _______________

**B.** What voltage level is the utility interconnection?
- Utility service voltage: _____ kV
- Metering point location: _______________
- Service type: [ ] Radial [ ] Loop [ ] Network [ ] Other: _____

**C.** What equipment is included in the switchyard commissioning? (check all that apply)
- [ ] Main utility transformers (qty: ____, voltage: ____ kV to ____ kV, capacity: ____ MVA)
- [ ] Utility breakers/reclosers
- [ ] Main switchgear/switchboards (34.5kV per equipment list - 12 total)
- [ ] Primary protective relaying and coordination
- [ ] SCADA/metering systems
- [ ] Arc flash studies validation
- [ ] Grounding system testing
- [ ] Other (please specify): _______________

**D.** Can you provide clearer design documents and drawings for switchyard commissioning scoping?

Facility and switchyard layout drawings:
- [ ] Yes, facility layout drawings available (current drawings difficult to interpret - clearer versions requested)
- [ ] Yes, switchyard layout drawings available
- [ ] Will be provided with RFI responses
- [ ] Not available at this time
- [ ] Other (please specify): _______________

Single-line diagrams and technical documentation:
- [ ] Yes, single-line diagrams for switchyard available
- [ ] Yes, one-line diagrams showing utility interconnection available
- [ ] Yes, utility interconnection agreement available
- [ ] Yes, protective relay coordination study available
- [ ] Yes, equipment specifications available
- [ ] Will be provided with RFI responses
- [ ] Not available to proposers
- [ ] Other (please specify): _______________

**E.** What is the CxA's responsibility for switchyard Levels 1-3 activities?
- [ ] Full execution of L1-3 (CxA performs all activities)
- [ ] Oversight only (GC/utility performs, CxA oversees)
- [ ] Hybrid (CxA performs some, oversees others - describe): _______________
- [ ] To be determined based on utility requirements
- [ ] Other (please specify): _______________

**Rationale:** Switchyard commissioning is **CRITICAL PATH** for the entire project. Any switchyard delay cascades to all 6 data hall blocks and could jeopardize the entire project schedule. The 3-month window (May-July 2026) must accommodate utility schedules, weather, and acceptance testing during hurricane season. The RFP provides minimal detail about switchyard scope. Cost variance is **$400K-$1.5M (3-4x)** depending on scope interpretation. This is the highest-risk scope ambiguity in the RFP.

**Impact if Not Answered:** Unable to accurately price or schedule switchyard commissioning; potential 3-4x cost variance ($400K to $1.5M); critical path schedule risk; inadequate resources allocated for high-voltage testing and utility coordination; project delays cascade to all data hall blocks.

---

### RFI-001.02 - Controls and Monitoring Systems (BMS, EPMS, DCIM, SCADA)

**RFP Reference:** General commissioning scope; IST requirements

**Question:**

**A.** Can you confirm which monitoring and control systems will be used on this project?

This information is critical for planning integration testing and IST activities accurately.

- **BMS (Building Management System):** [ ] Yes [ ] No [ ] TBD
  - Vendor/System: _______________
  - Version: _______________
- **DCIM (Data Center Infrastructure Management):** [ ] Yes [ ] No [ ] TBD
  - Vendor/System: _______________
  - Version: _______________
- **EPMS (Electrical Power Monitoring System):** [ ] Yes [ ] No [ ] TBD
  - Vendor/System: _______________
  - Version: _______________
- **SCADA (Supervisory Control and Data Acquisition):** [ ] Yes [ ] No [ ] TBD
  - Vendor/System: _______________
  - Version: _______________
  - Application: [ ] Switchyard [ ] Data halls [ ] Both [ ] Other: _____

**B.** Who is responsible for BMS/EPMS/DCIM/SCADA programming and integration?
- [ ] Controls contractor (under GC)
- [ ] Equipment vendors (system-by-system)
- [ ] Owner IT/facilities team
- [ ] CxA oversight only (no direct programming)
- [ ] Other (please specify): _______________

**C.** What is the expected CxA role in controls commissioning?
- [ ] Functional testing of control sequences only
- [ ] Sequence of operations (SOO) development and verification
- [ ] Control system tuning and optimization
- [ ] Graphics and user interface review
- [ ] Integration testing between systems (BMS/EPMS/DCIM/SCADA)
- [ ] All of the above
- [ ] Other (please specify): _______________

**Rationale:** Controls system integration is critical for IST activities and represents significant scope variation depending on system complexity, vendor coordination requirements, and integration testing needs. Vendor and version information affects test procedure development and integration planning. Undefined control system scope could result in 20-40% variance in Level 5 (IST) labor and schedule.

**Impact if Not Answered:** Inability to accurately scope controls integration testing; potential schedule delays during IST phase; insufficient resources allocated for multi-system integration verification; cost variance of $150K-$400K depending on integration complexity.

---

### RFI-001.03 - QA/QC Scope Definition (Critical Infrastructure vs. General Construction)

**RFP Reference:** General project quality requirements

**Question:**

**A.** Does the separate QA/QC scope of work apply to:
- [ ] Critical infrastructure only (electrical power distribution, cooling systems, life safety systems, utility interconnection)
- [ ] Entire project (all systems, equipment, and construction activities)
- [ ] To be determined / proposer to recommend based on risk assessment
- [ ] Other (please specify): _______________

If critical infrastructure only, please confirm which systems are considered critical infrastructure:
- [ ] Utility interconnection and switchyard
- [ ] Primary electrical distribution (34.5kV, transformers, MV switchboards)
- [ ] Secondary electrical distribution (LV switchboards, UPS systems, batteries)
- [ ] Chiller plants and primary cooling distribution
- [ ] Data hall cooling systems (CDUs, CRAH units)
- [ ] Fire protection and life safety systems
- [ ] BMS/EPMS/DCIM control systems
- [ ] Emergency power systems (generators, if applicable)
- [ ] Other: _______________

**B.** When should QA/QC involvement begin to support commissioning activities?
- [ ] During design phase (constructability/commissionability review)
- [ ] At construction start (Level 1 documentation review)
- [ ] Prior to Level 2 activities (installation verification for first-of-a-kind systems)
- [ ] Prior to Level 3 activities (pre-functional testing)
- [ ] Level 4-5 only (functional and integrated testing)
- [ ] Other (please specify): _______________

**C.** This project represents first-of-a-kind installations for several systems. Should QA/QC provide enhanced oversight for Level 2/Level 3 installation qualification activities?
- [ ] Yes, enhanced QA/QC for first installations with lessons-learned documentation
- [ ] Yes, but limited to critical infrastructure only
- [ ] No, standard commissioning oversight is sufficient
- [ ] To be determined based on GC capabilities
- [ ] Other (please specify): _______________

**D.** What is the expected QA/QC role during commissioning?
- [ ] Independent verification of CxA test results and documentation quality
- [ ] Witness testing of critical systems only
- [ ] Construction quality oversight (separate from commissioning verification)
- [ ] Both construction quality AND commissioning quality verification
- [ ] Other (please specify): _______________

**Rationale:** QA/QC scope definition (critical infrastructure vs. entire project) represents the largest cost variance in the RFP - potentially **3-10x difference ($100K to $2M+)**. Critical infrastructure QA/QC is a focused scope appropriate for commissioning quality verification. General construction QA/QC is a much broader scope encompassing all installation activities. Early QA/QC coordination for first-of-a-kind installations can prevent costly rework.

**Impact if Not Answered:** QA/QC scope ambiguity could result in massive cost variance ($100K to $2M+); unclear whether QA/QC is construction-focused or commissioning-focused; inadequate early coordination may miss critical installation issues; proposers unable to accurately price QA/QC services.

---

## HIGH PRIORITY QUESTIONS

The following questions significantly impact scope definition, technical approach, and cost but may have reasonable assumptions if not answered.

**[Note: Additional questions from original RFI would be listed here - preserving all other questions from the original document]**

---

## RFI RESPONSE REQUEST

We respectfully request written responses to the questions in this RFI, prioritizing the **3 Critical Questions:**
- **RFI-001.01:** Switchyard Commissioning Scope and Timeline ⚠️ **(CRITICAL PATH)**
- **RFI-001.02:** Controls and Monitoring Systems (BMS, EPMS, DCIM, SCADA)
- **RFI-001.03:** QA/QC Scope Definition (Critical Infrastructure vs. General Construction)

**Requested Response Timeline:**
- RFI response target date: _______________
- Proposal due date (confirmed): _______________

We appreciate Hut 8's consideration of these clarifications and look forward to submitting a comprehensive and competitive proposal for the Riverbend Data Center Commissioning project.

---

## CONTACT INFORMATION

**Submitted By:**
[Your Company Name]
[Address]
[City, State ZIP]

**Primary Contact:**
[Name, Title]
[Email]
[Phone]

**Date Submitted:** 2025-11-07

---

**END OF RFI-001**

*This RFI contains 3 CRITICAL priority questions that address the highest-risk scope ambiguities: (1) Switchyard scope and critical path, (2) Controls system integration, and (3) QA/QC scope definition. Additional supporting questions are available upon request.*

**SCOPE & PRICING ASSUMPTIONS (Questions Removed from RFI):**

**Scope Assumptions:**
- **QA/QC Services:** CxA will document assumptions, scope of work, and manpower requirements for QA/QC as a separate proposal section
- **Load Bank Provision:** Air and liquid load banks to be provided and operated by others; PGCIS will provide load bank plan review and oversight only
- **Pressure Testing, Flush & Fill, and TAB:** Pressure testing, flush & fill, and test and balancing (TAB) of liquid/liquid and liquid/air equipment to be performed by others; PGCIS will provide oversight and documentation review only
- **White Space Configuration:** CxA will base all pricing and planning on White Space Option 2 per RFP instruction
- **Level 4-5 Duration:** CxA will assume 6 weeks total duration per 36 MW block from start to finish: Level 4 (Functional Performance Testing, Heat Load Testing, System Level Testing) = 4-5 weeks, and Level 5 (Integrated Systems Testing) = 1-2 weeks
- **No Overlapping L4-L5 Phases:** CxA will assume that no two Level 4-5 commissioning phases overlap during the project duration. If overlapping L4-L5 phases are required, a change order may be necessary to provide additional resources

**Pricing Assumptions:**
- **Payment Terms:** 20% of total contract value due upon contract execution; invoices to be submitted bi-weekly with payment terms Net 30 days from date of invoice
- **Commissioning Continuity:** Pricing assumes that Level 4 and Level 5 commissioning will be contiguous (continuous without delays). Any delays not related to PGCIS (commissioning agent) may require a change order
- **Construction Delays:** Any construction-related delays or GC readiness issues unrelated to PGCIS may necessitate a change order
- **Work Hours:** Pricing is based on a 50-hour work week. Hours over 50 hours per week may require a change order
