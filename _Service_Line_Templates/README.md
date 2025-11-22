# Service Line Templates

This folder contains reusable templates for all PGCIS advisory service offerings.

## Purpose

Templates accelerate deliverable creation by providing proven structures, standardized content, and integration with Claude AI for rapid customization.

## How to Use Templates

1. **Identify the Service Line** - Match your engagement to one of the service offerings below
2. **Copy the Template Folder** - Copy the entire template folder to your project location
3. **Follow Quick Start Guide** - Each template has a Quick Start document explaining the workflow
4. **Customize for Project** - Update placeholders, add project-specific content
5. **Reference Shared Resources** - Link to standards, calculations, and lessons learned from `_Shared_Resources/`

## Available Templates

### BOD Development
**Folder:** `BOD_Development/`
**Use When:** Developing or reviewing Basis of Design documents for data center projects
**Contents:**
- CSI MasterFormat Template (13 division documents + executive summary)
- Technical Appendices (voltage selection, cooling strategy, generators, BESS, etc.)
- Quick Start guide for new BOD projects

**Time Savings:** 50% reduction (40 hours → 20 hours for first draft)

---

### Commissioning
**Folder:** `Commissioning/`
**Use When:** Responding to Cx RFPs or developing commissioning plans
**Contents:**
- RFP Analysis Framework (5-step structured analysis)
- Proposal Package (modular proposal sections)
- Commissioning Plan Templates (ASHRAE 202 aligned)
- Equipment Testing Procedures (30+ systems)
- Quick Start guides for RFP response and Cx plan development

**Time Savings:** 70% reduction for RFP response (60 hours → 20 hours)

---

### Operational Readiness
**Folder:** `Operational_Readiness/`
**Use When:** Developing or reviewing operational readiness plans
**Contents:**
- OR Plan Master Template
- Staffing Plan with 20+ job descriptions
- Training Program including Hyperscale AI curriculum
- Compliance Requirements checklists (Uptime, ISO, regulatory)
- Transition to Operations checklists

**Time Savings:** 60% reduction (estimated)

---

### Financial Modeling
**Folder:** `Financial_Modeling/`
**Use When:** Developing financial models, TCO analysis, or investment projections
**Contents:**
- CAPEX/OPEX model templates
- Equipment cost database (continuously updated)
- TCO analysis framework
- Sensitivity analysis templates

**Time Savings:** 40% reduction (30 hours → 18 hours)

---

### Go-to-Market Strategy
**Folder:** `GTM_Strategy/`
**Use When:** Developing market entry, sales, or marketing strategies
**Contents:**
- Market analysis template
- Competitive positioning template
- Sales strategy template
- Marketing plan template

---

### Investor Relations
**Folder:** `Investor_Relations/`
**Use When:** Creating investor presentations, executive summaries, or financial projections
**Contents:**
- Investor deck template
- Executive summary template
- Financial projections template
- Risk assessment template

**Time Savings:** 50% reduction (20 hours → 10 hours)

---

### Development Advisory
**Folder:** `Development_Advisory/`
**Use When:** Greenfield/brownfield development, feasibility studies, or due diligence
**Contents:**
- Feasibility study template
- Site selection criteria
- Due diligence checklist
- Repurposing analysis template
- Schedule development template
- Constructability review checklist
- Value engineering framework

**Time Savings:** 50% reduction (varies by engagement scope)

---

### Joint Venture Strategy
**Folder:** `Joint_Venture_Strategy/`
**Use When:** Developing joint venture structures or partnership strategies
**Contents:**
- JV structure analysis template
- Partner evaluation criteria
- Risk sharing framework

---

## Template Development Guidelines

When creating new templates or updating existing ones:

1. **Start with Best Example** - Use the best completed project as foundation
2. **Remove Project-Specific Content** - Replace with placeholders like `[PROJECT NAME]`
3. **Add Claude Instructions** - Use comments: `<!-- @claude Customize this section based on... -->`
4. **Include Metadata Header** - Date, status, tags, related documents
5. **Write README** - Explain when to use template and provide workflow
6. **Test Template** - Use on next project and track time savings
7. **Iterate** - Incorporate feedback and lessons learned

See `_Shared_Resources/Workflows_and_Processes/` for detailed template development process.

---

## Integration with Claude AI

These templates are optimized for use with Claude Code. Claude can:
- Copy templates to new project locations
- Populate project-specific metadata
- Search `_Shared_Resources/` for relevant standards and lessons learned
- Generate customized content based on project parameters
- Link to related documents automatically
- Apply lessons learned from past projects

To use with Claude, simply say: "Start a new [service line] project for [client/description]"

---

**Related Resources:**
- [[_Shared_Resources/README_Resources|Shared Resources]]
- [[_Utilities/Template_Usage_Guide|Template Usage Guide]]
- [[PGCIS_Knowledge_Management_Strategy|Knowledge Management Strategy]]

**Tags:** #templates #advisory-services #pgcis
