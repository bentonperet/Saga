# Hut 8 Riverbend Data Center Commissioning RFP Analysis

**Project:** Riverbend Data Center - Louisiana
**Client:** Hut 8
**Analysis Date:** 2025-11-07
**Analysis Status:** Complete - Ready for Proposal Development

---

## Document Overview

This folder contains a comprehensive analysis of the Hut 8 Riverbend Data Center Commissioning RFP, including scope breakdown, clarifying questions, and risk assessment to support proposal development.

### Documents in This Analysis

1. **[[01_Executive_Summary]]** - High-level project overview, timeline, and key requirements
2. **[[02_Scope_Analysis]]** - Detailed commissioning scope breakdown by level and system
3. **[[03_Clarifying_Questions]]** - Comprehensive list of questions to submit to client (77 questions organized by priority)
4. **[[04_Risk_Assessment]]** - Risk analysis and go/no-go decision criteria

---

## Quick Reference: Project Key Facts

| Parameter | Value |
|-----------|-------|
| **Total IT Capacity** | 224 MW (6 data halls + 1 network room) |
| **Utility Power** | 300 MW |
| **Phasing** | Six 36 MW blocks |
| **Switchyard Cx** | May 2026 - July 2026 |
| **Data Hall Cx** | August 2026 - February 2027 |
| **IST Duration Limit** | 6 weeks per 36 MW block |
| **Standards** | ASHRAE & NEBB |
| **Total Equipment Items** | ~5,000+ pieces |

---

## Critical Findings

### 🔴 CRITICAL ISSUES REQUIRING CLARIFICATION

1. **6-Week IST Constraint** - Potentially infeasible if applies to all of Levels 4-5 + IST
   - Industry standard: 10-16 weeks for 36 MW block
   - RFP requirement: 6 weeks maximum
   - **40-60% schedule compression**

2. **Level 1-3 Oversight Scope Ambiguous** - Could represent 10% to 70% of effort
   - Cost variance: $200K to $600K per block depending on interpretation
   - RFP uses term "oversight" without definition

3. **Switchyard Commissioning Scope Undefined** ⚠️ **CRITICAL PATH RISK**
   - RFP shows 12 MV switchboards + 138 RMUs but no main transformers or utility voltage
   - Cost variance: $400K to $1.5M (3-4x) depending on scope interpretation
   - **Any switchyard delay cascades to all 6 data hall blocks**
   - 3-month window during hurricane season with utility coordination requirements

### 🟡 HIGH-PRIORITY CONSIDERATIONS

- **Overlapping phases:** 3-4 blocks simultaneously active Oct-Dec 2026
- **Holiday period impacts:** Blocks 4-6 span Thanksgiving through New Year's
- **GC capability unknown:** Level 1-3 quality depends on GC experience
- **Equipment list subject to change:** Explicit RFP caveat
- **White space configuration TBD:** Three options provided, final selection unknown

---

## Risk Assessment Summary

**Overall Risk Rating:** ⚠️ **MEDIUM-HIGH** (manageable with proper contract protections)

**Top 5 Risks:**
1. 6-week IST timeline potentially infeasible
2. Level 1-3 oversight scope ambiguity (massive cost variance)
3. QA/QC scope completely undefined
4. Professional liability exposure due to schedule pressure
5. Overlapping commissioning phases create resource constraints

**Recommendation:** **PURSUE WITH CAUTION** - contingent on receiving satisfactory answers to critical clarifying questions

---

## Clarifying Questions Summary

**RFI Structure:** Streamlined to focus on highest-priority scope ambiguities
**Critical Questions:** 3 questions addressing major cost drivers and critical path
**Total Cost Variance from Critical Questions:** $650K-$3.9M

**SCOPE & PRICING ASSUMPTIONS (Not included in RFI):**

*Scope Assumptions:*
- **QA/QC Services:** CxA will document assumptions, SOW, and manpower in proposal
- **Load Bank Provision:** Air and liquid load banks to be provided and operated by others; PGCIS provides load bank plan review and oversight only
- **Pressure Testing, Flush & Fill, and TAB:** Pressure testing, flush & fill, and test and balancing (TAB) of liquid/liquid and liquid/air equipment to be performed by others; PGCIS provides oversight and documentation review only
- **White Space Configuration:** CxA will base pricing on White Space Option 2 per RFP instruction
- **Level 4-5 Duration:** CxA will assume 6 weeks total duration per 36 MW block from start to finish: Level 4 (Functional Performance Testing, Heat Load Testing, System Level Testing) = 4-5 weeks, and Level 5 (Integrated Systems Testing) = 1-2 weeks, for a total of 6 weeks per RFP constraint
- **No Overlapping L4-L5 Phases:** CxA will assume that no two Level 4-5 commissioning phases overlap during the project duration. If overlapping L4-L5 phases are required, a change order may be necessary to provide additional resources
- **Level 1-3 Oversight:** CxA will assume moderate oversight (2-3 site visits per week, test procedure development, critical item witness) representing approximately 25-30% effort level
- **Contract Structure:** CxA will propose Time & Materials with Not-to-Exceed limit and unit pricing schedule
- **Payment Terms:** 20% mobilization upon contract execution; bi-weekly invoicing with Net 30-day payment terms

*Pricing Assumptions:*
- **Payment Terms:** 20% of total contract value due upon contract execution; invoices submitted bi-weekly with Net 30-day payment terms
- **Commissioning Continuity:** Level 4 and Level 5 commissioning will be contiguous; delays not related to CxA may require change order
- **Construction Delays:** Any construction-related delays or GC readiness issues unrelated to PGCIS may necessitate a change order
- **Work Hours:** Pricing based on 50-hour work week; hours over 50/week may require change order

### 3 Critical Questions That MUST Be Answered:

1. **RFI-001.01** ⚠️ - **Switchyard Commissioning Scope and Timeline (CRITICAL PATH)**
   - Cost variance: $400K-$1.5M (3-4x)
   - Schedule impact: Critical path for all 6 data hall blocks
   - Key unknowns: Utility voltage, main transformers, protective relaying scope, L1-3 responsibilities

2. **RFI-001.02** - **Controls and Monitoring Systems (BMS, EPMS, DCIM, SCADA)**
   - Cost variance: $150K-$400K
   - Schedule impact: IST phase schedule risk
   - Key unknowns: System vendors/versions, integration scope, CxA role in controls commissioning

3. **RFI-001.03** - **QA/QC Scope Definition (Critical Infrastructure vs. General Construction)**
   - Cost variance: $100K-$2M+ (3-10x)
   - Schedule impact: Early coordination for first-of-a-kind installations
   - Key unknowns: Critical infrastructure only vs. entire project, timing of QA/QC involvement, role definition

**See [[RFI_001_Detailed_Commissioning_Scope_Clarifications]] for formal RFI document**
**See [[Switchyard_Commissioning_Notes]] for detailed switchyard analysis**

---

## Estimated Pricing Ranges

### Base Commissioning Services (Levels 1-5 + IST)

| Scenario | Cost Range | Description |
|----------|------------|-------------|
| **Low** | $3.5M - $4.5M | Minimal Level 1-3 oversight, no major issues |
| **Medium** | $5.0M - $6.5M | Moderate oversight, normal project challenges |
| **High** | $7.0M - $9.0M | Extensive oversight, significant complications |

### Additional Costs (Separate Line Items)

| Item | Cost Range | Notes |
|------|------------|-------|
| **Equipment** | $1.0M - $1.8M | Load banks, test equipment (rental/purchase) |
| **QA/QC Option A** | $100K - $150K | Commissioning quality verification |
| **QA/QC Option B** | $300K - $500K | Construction quality oversight |
| **QA/QC Option C** | $1.0M - $2.0M | Comprehensive inspection program |

### Recommended Proposal Pricing

**Base Commissioning:** $5.5M - $6.0M
**Equipment Costs:** $1.2M
**QA/QC (Option A):** $150K
**TOTAL:** **$6.85M - $7.35M**

*Target margin: 20-25% (higher than standard due to risk level)*

---

## Scope Highlights

### Equipment to be Commissioned (Total Facility)

**Outdoor Gray Space:**
- 276 Transformers (34.5kV-480V, 2.5-5 MVA)
- 138 Ring Main Units (34.5kV)
- 12 MV Switchboards (34.5kV)
- 162 Chillers (Vertiv OFC)
- 162 Buffer Tanks

**Indoor Gray Space:**
- 276 LV Switchboards (4000-5000A)
- 676 UPS Units (Vertiv APM2 600kVA)
- 2,104 Battery Cabinets (Vertiv LI5-LI7)
- 64 CRAH Fan Walls (Electrical Rooms)

**White Space (Option 2 - Most Extensive):**
- 65 Hot Aisle Containment Units
- 960 Rack Power Panels (1000/1200A)
- 40 Remote Distribution Panels (400A)
- 190 Cooling Distribution Units (Vertiv XDU 2300)
- 214 CRAH Fan Walls (Data Halls)

---

## Commissioning Level Breakdown

| Level | Performer | CxA Role | Estimated % of Total Effort |
|-------|-----------|----------|---------------------------|
| **Level 1** | GC | Oversight | 10-15% |
| **Level 2** | GC | Oversight | 15-20% |
| **Level 3** | GC | Oversight | 20-25% |
| **Level 4** | CxA | Full execution | 30-35% |
| **Level 5 (IST)** | CxA | Full execution | 15-20% |

**Level Definitions:**
- Level 3 = Pre-Functional Testing
- Level 4 = Functional Performance Testing, Heat Load Testing, System Level Testing (Electrical & Mechanical)
- Level 5 = Integrated Systems Testing

**Key Clarification Needed:** "Oversight" definition significantly impacts Levels 1-3 effort

---

## Project Timeline & Phasing

### Phase 0: Switchyard (May 2026 - July 2026)
- 300 MW utility interconnection commissioning
- Critical path for all subsequent data hall work

### Phase 1-6: Data Halls (August 2026 - February 2027)

| Block | Data Hall | Cx Start | Cx Complete | Duration | IT Load |
|-------|-----------|----------|-------------|----------|---------|
| 1 | DH-1 | Aug 2026 | Sep 2026 | 2 months | 36 MW |
| 2 | DH-2 | Sep 2026 | Oct 2026 | 2 months | 36 MW |
| 3 | DH-3 | Oct 2026 | Nov 2026 | 2 months | 36 MW |
| 4 | DH-4 | Nov 2026 | Dec 2026 | 2 months | 36 MW |
| 5 | DH-5 | Dec 2026 | Jan 2027 | 2 months | 36 MW |
| 6 | DH-6 | Jan 2027 | Feb 2027 | 2 months | 36 MW |

**Peak Overlap Period:** October - December 2026 (3-4 blocks active)
**Holiday Impact:** Blocks 4, 5, 6 (Thanksgiving - New Year's)

---

## Deliverables Required in Proposal

Per RFP Section "Deliverables," proposals must include:

1. ✅ **Schedule Estimate** - Duration and sequencing by phase
2. ✅ **Manpower Plan** - Staffing requirements and duration by phase
3. ✅ **Cost Proposal** - Level and phase-based breakdown
   - Equipment purchase/rental costs (separate)
   - QA/QC efforts (separate if not standard)
4. ✅ **Relevant Experience** - Large data center and hyperscale facility projects

---

## Next Steps for Proposal Development

### IMMEDIATE ACTIONS (Before Pricing)

1. **Submit Clarifying Questions** to Hut 8 via designated RFP contact
   - Prioritize the 9 critical questions
   - Request responses within 1 week to allow adequate proposal time

2. **Review Basis of Design (BOD) Document** (referenced as attachment in RFP)
   - Request access if not already provided
   - Extract performance criteria and technical requirements

3. **Request Additional RFP Information:**
   - Equipment List (referenced but not fully detailed in RFP)
   - Ramp Schedule (referenced but only summary shown)
   - Single-line diagrams if available
   - Design drawings (30%/60%/90% level)

### PROPOSAL PREPARATION (After Clarifications)

4. **Develop Detailed Schedule** (Deliverable #1)
   - Gantt chart showing all phases and commissioning levels
   - Critical path identification
   - Resource loading by phase

5. **Create Staffing/Manpower Plan** (Deliverable #2)
   - Organization chart
   - Role definitions and responsibilities
   - Labor hours by role and phase
   - Peak staffing periods identified

6. **Prepare Cost Breakdown** (Deliverable #3)
   - Level-by-level pricing matrix
   - Phase-by-phase pricing
   - Equipment costs (separate section)
   - QA/QC options (separate section)
   - Unit pricing schedule for flexibility

7. **Compile Relevant Experience** (Deliverable #4)
   - Hyperscale data center projects (100+ MW)
   - Commissioning experience summary
   - Key personnel resumes and certifications
   - Client references

8. **Develop Technical Approach**
   - Commissioning methodology
   - Quality control procedures
   - Testing equipment and capabilities
   - Risk mitigation strategies

9. **Draft Proposal Narrative**
   - Executive summary
   - Understanding of project requirements
   - Qualifications and experience
   - Technical approach and methodology
   - Schedule and staffing approach
   - Cost proposal with assumptions

10. **Include Assumptions and Clarifications Section**
    - Clearly state all assumptions made in absence of clarifications
    - List scope inclusions and exclusions
    - Define terms (especially "oversight" and "QA/QC")
    - Reference RFP sections and interpretations

### PROPOSAL REVIEW & SUBMISSION

11. **Internal Review Process**
    - Technical review (commissioning discipline leads)
    - Commercial review (contracts/legal)
    - Pricing review (estimating/finance)
    - Executive approval

12. **Finalize and Submit**
    - Format per RFP requirements
    - Proof for accuracy and completeness
    - Submit by deadline with all required forms

---

## Key Assumptions for Proposal (If Clarifications Not Received)

If clarifying questions are not answered before proposal due date, recommend including these assumptions:

### Schedule Assumptions:
- 6-week IST duration applies to Level 4 functional testing only, not combined Levels 4-5-IST
- Level 1-3 commissioning performed by GC will be substantially complete before Level 4 start
- Weather delays beyond 5 cumulative days per phase will result in schedule extension
- Holiday shutdowns (if required) will extend schedule accordingly

### Scope Assumptions:
- Level 1-3 "oversight" = 25-30% effort level (site visits 2-3 days/week during GC commissioning)
- CxA develops test procedures for all levels; GC executes Level 1-3 under CxA review
- QA/QC services = commissioning quality verification only (test procedure validation, documentation review, results verification)
- White Space Option 2 is basis of pricing; other options available via unit price adjustments
- Equipment list per RFP is baseline; changes >10% trigger change order process

### Equipment Assumptions:
- CxA provides all commissioning test equipment except load banks
- Load banks priced separately as optional service; Owner may elect to provide
- Test equipment is adequate for scheduled activities; extended duration rentals are Owner cost

### Commercial Assumptions:
- Contract structure: Not-to-exceed Time & Materials with unit pricing schedule
- Payment terms: Monthly progress payments, net 30 days, 5% retainage
- Professional liability capped at lesser of contract value or insurance limits ($5M)
- Standard of care applies; no guarantee of system performance

---

## Document References

**RFP Source Document:**
`C:\Users\eriks\Documents\Obsidian\Hut 8 Riverbend Cx RFP & Response\RFP from Hut 8\Riverbend RFP - Data Center Commissioning.pdf`

**Related Documents:**
- Basis of Design (BOD) - *Requested, not yet received*
- Equipment List - *Partial list in RFP page 5*
- Ramp Schedule - *Summary table in RFP page 2*

---

## Contact Information for Questions

**RFP Questions Contact:** *To be determined from RFP or via Q7.3*

**Internal Project Team:**
- Proposal Manager: *[Assign]*
- Technical Lead: *[Assign]*
- Estimating Lead: *[Assign]*
- Contracts/Legal Review: *[Assign]*

---

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-11-07 | Claude Code Analysis | Initial comprehensive RFP analysis |

---

**Analysis Classification:** CONFIDENTIAL - Internal Use Only

**Recommendation:** PURSUE WITH CAUTION - Submit clarifying questions immediately and await responses before finalizing proposal pricing and scope.
