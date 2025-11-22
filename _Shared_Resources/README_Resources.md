# Shared Resources

This folder contains cross-project knowledge that applies to all PGCIS engagements.

## Purpose

The Shared Resources library ensures:
- **Consistency** - All projects reference the same standards and guidelines
- **Efficiency** - No duplication of reference materials across projects
- **Quality** - Best practices and lessons learned inform every deliverable
- **Competitive Advantage** - Lessons learned from "uncovering what's hidden" are systematically captured

## Folder Structure

### Standards and Codes
**Folder:** `Standards_and_Codes/`
**Contents:** Reference documents for industry standards
- ASHRAE (90.1, 202, TC 9.9)
- NFPA (70 NEC, 72, 75)
- TIA (942 Data Center Standard)
- Uptime Institute (Tier I-IV requirements)
- ISO (27001, 50001)

**Use When:** Verifying design compliance, citing requirements in BOD documents

---

### Design Guidelines
**Folder:** `Design_Guidelines/`
**Contents:** PGCIS best practices for data center design
- Electrical Design Best Practices
- Mechanical Design Best Practices
- BIM LOD Requirements
- Redundancy Topologies
- Power Density Guidelines
- Cooling Strategy Selection
- Hyperscale AI Considerations (differentiator)

**Use When:** Starting design, conducting design reviews, advising clients on approach

---

### Calculation Tools
**Folder:** `Calculation_Tools/`
**Contents:** Excel/spreadsheet calculators for technical analysis
- **Electrical:** Load calculations, voltage drop, short circuit, generator sizing, UPS runtime, BESS sizing
- **Mechanical:** Cooling load, chiller sizing, airflow, pump sizing, PUE
- **Financial:** TCO, lifecycle cost, energy cost, ROI
- **Space Planning:** Equipment footprints, clearances, yard space

**Use When:** Sizing equipment, validating designs, developing cost estimates

---

### Equipment Libraries
**Folder:** `Equipment_Libraries/`
**Contents:** Specifications, comparisons, and vendor information
- Electrical Equipment (UPS, generators, switchgear, PDUs, BESS)
- Mechanical Equipment (chillers, CRAC/CRAH, cooling towers, pumps)
- Controls Equipment (BMS platforms, DCIM, PLCs)
- Vendor Database (approved vendors, performance tracking, lead times)

**Use When:** Selecting equipment, writing specifications, validating submittals

---

### Quality Checklists
**Folder:** `Quality_Checklists/`
**Contents:** Standardized review checklists
- BOD Review Checklist
- Design Review Checklists (30%, 60%, 90%, IFC)
- Construction QA Checklist
- Commissioning Readiness Checklist
- Substantial Completion Checklist

**Use When:** Conducting any design review, construction inspection, or quality verification

---

### Lessons Learned ⭐
**Folder:** `Lessons_Learned/`
**Contents:** PGCIS's competitive advantage - documented insights from "uncovering what's hidden"

**Organization:**
- **By Phase:** Design, Construction, Commissioning
- **By Issue Type:** Safety issues, quality issues, schedule issues, design errors, construction defects, operational risks
- **By Client Type:** Hyperscale cloud, hyperscale AI, colocation, investor

**Standard Format:** Each lesson includes:
- Issue description and root cause
- How PGCIS discovered it (what others missed)
- Impact (safety, quality, schedule, cost)
- Resolution and prevention methods
- Detection methods for future projects
- Applicable project types and keywords

**Use When:**
- Starting any new project (identify common risks)
- Conducting design reviews (check for known issues)
- Responding to RFPs (assess risk factors)
- Developing recommendations (apply past insights)

**CRITICAL:** Always search lessons learned when working on deliverables. This is what clients hire PGCIS for - our experience finding what others miss.

---

### Market Intelligence
**Folder:** `Market_Intelligence/`
**Contents:** Industry data and competitive analysis
- Energy Pricing (North America, EMEA, renewable incentives)
- Construction Costs (regional indices, equipment trends, labor rates)
- Competitive Intelligence (Cx firms comparison, win/loss analysis)
- Industry Trends (hyperscale AI, liquid cooling, sustainability, nuclear power)

**Use When:** Developing financial models, positioning proposals, advising on market conditions

---

### Workflows and Processes
**Folder:** `Workflows_and_Processes/`
**Contents:** Step-by-step guides for PGCIS processes
- How to Start New BOD Project
- How to Analyze RFP
- How to Develop Proposal
- How to Conduct Design Review
- How to Develop Cx Plan
- How to Build Financial Model
- How to Archive Completed Project
- How to Document Lessons Learned

**Use When:** Starting any new task, onboarding team members

---

## Using Shared Resources with Templates

**Integration Pattern:**
1. Copy template from `_Service_Line_Templates/`
2. Reference standards from `Standards_and_Codes/`
3. Apply guidelines from `Design_Guidelines/`
4. Use tools from `Calculation_Tools/`
5. Select equipment from `Equipment_Libraries/`
6. Follow checklists from `Quality_Checklists/`
7. **ALWAYS search `Lessons_Learned/` for relevant insights**
8. Reference market data from `Market_Intelligence/`
9. Follow workflows from `Workflows_and_Processes/`

## Maintenance

**Continuous Improvement:**
- Standards: Update when new versions published
- Guidelines: Evolve based on lessons learned
- Calculations: Verify formulas, add new tools as needed
- Equipment: Update specifications and costs quarterly
- Checklists: Add items based on lessons learned
- **Lessons Learned: Capture after every project (required)**
- Market Intelligence: Update quarterly
- Workflows: Refine based on team feedback

**Ownership:**
- All team members contribute lessons learned
- Erik and Muhammed approve guideline changes
- Equipment costs updated by project teams
- Market intelligence compiled monthly

---

**Related Resources:**
- [[_Service_Line_Templates/README|Service Line Templates]]
- [[PGCIS_Knowledge_Management_Strategy|Knowledge Management Strategy]]
- [[_Utilities/Project_Index_Dashboard|Active Projects Dashboard]]

**Tags:** #shared-resources #standards #lessons-learned #pgcis
