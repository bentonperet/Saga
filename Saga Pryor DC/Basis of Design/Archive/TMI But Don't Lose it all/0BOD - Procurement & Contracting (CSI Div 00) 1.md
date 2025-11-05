**Created:** 2025-10-29
**Updated from:** Pryor_Bod_EVS_Rev01.md + Erik_BOD references

# BASIS OF DESIGN - PROCUREMENT & CONTRACTING
## CSI Division 00
### Pryor Data Center - PACHYDERM GLOBAL

**Parent Document:** [[Saga Pryor DC/Basis of Design/Erik_BOD_Updated/_BOD - Exec Summary and TOC]]

---

*Note: We generated this full doc quickly, but haven't fully validated this section as it wasn't in scope. We've left it as part of the template, but you'll need to delete or rework all of this! Assume that all specific information, numbers, costs, and lead times are wrong until otherwise proven.*

## OVERVIEW

CSI Division 00 establishes the contract strategy, procurement approach, and delivery methods for the Pryor Data Center project. This division defines how the project will be organized, procured, and executed to meet schedule, budget, and performance requirements while minimizing risk.

**Key Objectives:**
- **Delivery method:** Select optimal project delivery approach (Design-Build, CMAR, etc.)
- **Procurement strategy:** Balance competitive pricing with proven Tier III vendors
- **Risk allocation:** Clear contractual roles for design, construction, commissioning, and performance
- **Schedule optimization:** Parallel design, procurement, and construction to meet 24-month timeline
- **Quality assurance:** Vendor pre-qualification and performance guarantees

---

## 0.01 PROJECT DELIVERY METHOD

### Recommended Delivery Method: **Design-Build (DB)**

**Rationale:**
- **Single-point responsibility:** One contract for design and construction reduces owner risk
- **Schedule compression:** Overlap design, procurement, and construction (fast-track)
- **Integrated team:** Design-builder coordinates architect, MEP engineer, and trades
- **Performance guarantees:** PUE, uptime, capacity targets contractually enforceable
- **Cost certainty:** Guaranteed Maximum Price (GMP) locked after design development

### Design-Build Team Structure

```
Owner (SAGA)
        |
  Design-Builder (Prime Contractor)
        |
    ┌───┴────┬────────────┬────────────┬─────────────┐
Architect  MEP Eng  Struct Eng  Commissioning  Construction Mgr
                                    (CxA)
                                      |
                            ┌─────────┴──────────┐
                      Subcontractors    Vendors
                    (Electrical, Mech,  (Generators,
                     Precast, Roofing)   UPS, Chillers)
```

**Design-Builder Responsibilities:**
- Design coordination (architectural, structural, MEP, fire protection)
- Permitting and utility coordination
- Equipment procurement (long-lead items: switchgear, UPS, generators, chillers)
- Construction execution (site work, building shell, MEP installation)
- Commissioning coordination (CxA oversight, factory tests, IST)
- Performance guarantees (PUE, uptime, capacity)
- Warranty and post-occupancy support

**Owner Responsibilities:**
- Define Owner's Project Requirements (OPR) and success criteria
- Site acquisition and financing
- Utility coordination (high-voltage service, telecom fiber)
- Review and approve design at milestones (30%, 65%, 95%, 100%)
- Engage independent commissioning authority (CxA)
- Final acceptance and facility operations

---

## 0.02 PROCUREMENT STRATEGY

### Phased Procurement Approach

**Phase 1: Design-Builder Selection (RFP Process)**
- **RFQ (Request for Qualifications):** Pre-qualify 3-5 design-build teams based on:
- **RFP (Request for Proposal):** Issue to pre-qualified teams

**Phase 2: Long-Lead Equipment Procurement** {lead times are wrong}
- **Critical path items** (order during design development, 4-6 months into project):
  - Medium-voltage switchgear (20-32 weeks lead time)
  - UPS systems (16-24 weeks)
  - Generators (16-20 weeks)
  - Chillers (12-16 weeks)
  - Transformers (12-16 weeks)

- **Procurement approach:**
  - **Design-assist:** Major vendors (e.g., Schneider, Caterpillar, Carrier) provide input during design
  - **Performance specifications:** Define output requirements (kW, efficiency, redundancy) vs. prescriptive specs
  - **Sole-source justification:** For standardized equipment or proven integrations (e.g., UPS + EPMS from same vendor)
  - **Competitive bidding:** Where multiple vendors meet Tier III requirements (e.g., chillers, cooling towers)

**Phase 3: Subcontractor Procurement**
- **Bid packages** issued after 95% design:
  - Site work (grading, utilities, paving)
  - Precast tilt-up panels (fabrication + erection)
  - Roofing (FM 1-150 system)
  - Electrical (conduit, wire, terminations, testing)
  - Mechanical (piping, ductwork, TAB)
  - Fire protection (sprinkler, pre-action, fire alarm)
  - Low-voltage (BMS, access control, CCTV)

- **Subcontractor pre-qualification:**
  - Prior data center or mission-critical experience
  - NETA certification (electrical testing)
  - AABC/NEBB certification (test & balance)
  - Financial stability and bonding capacity

---

## 0.03 CONTRACT TYPES & STRUCTURE

### Design-Build Prime Contract

**Contract Type: Guaranteed Maximum Price (GMP)**

**Structure:**
- **Preconstruction phase:** Cost-plus-fee (design development, value engineering, GMP negotiation)
- **Construction phase:** GMP with shared savings
  - Owner: 50% of savings below GMP
  - Design-builder: 50% of savings below GMP
- **Schedule incentive:** $10K/day bonus for early Substantial Completion (max 30 days)
- **Schedule penalty:** $10K/day liquidated damages for late Substantial Completion (after float exhausted)

**Payment Structure:**
- **Monthly pay applications:** AIA G702/G703 format
- **Retainage:** 10% until Substantial Completion; 5% until Final Completion
- **Milestone payments:**
  - 5% - Design completion (100% CD)
  - 15% - Foundation and precast erection
  - 30% - Building shell and roof watertight
  - 30% - MEP rough-in and equipment installation
  - 15% - Commissioning and Substantial Completion
  - 5% - Final Completion and closeout

**Performance Guarantees:**
- **PUE:** ≤ 1.4 at 50% IT load; ≤ 1.3 at 80% IT load (measured per Uptime Institute methodology)
- **Uptime:** Tier III concurrently maintainable (no single point of failure)
- **Capacity:** 3 MW Phase 1 IT load; 12 MW total infrastructure capacity
- **Schedule:** Substantial Completion within 20 months of NTP (excluding force majeure)

**Penalties for Non-Performance:**
- **PUE miss:** $50K penalty for every 0.1 PUE above target (measured over 3 months post-occupancy)
- **Capacity shortfall:** $100K penalty if system cannot support guaranteed IT load
- **Uptime failure:** $500K penalty if Tier III certification cannot be achieved

---

## 0.04 VENDOR SELECTION CRITERIA

### Tier 1 Vendor Requirements

To minimize risk and ensure long-term supportability, all critical systems must be sourced from **Tier 1 vendors** meeting the following criteria:

| Criterion | Requirement |
|-----------|-------------|
| **Market presence** | 10+ years in data center industry |
| **Installed base** | 50+ Tier III or higher facilities |
| **Financial stability** | Investment-grade credit rating or private equity backing |
| **Service network** | 24/7 support with <4 hour response time in U.S. |
| **Parts availability** | Guaranteed spare parts for 15+ years |
| **Warranty** | Minimum 2 years parts and labor (standard); extended options available |
| **Interoperability** | Open protocols (Modbus, BACnet, SNMP) for BMS/DCIM integration |

### Pre-Qualified Vendor List (Examples)

**Electrical:**
- **Medium-voltage switchgear:** ABB, Siemens, Schneider Electric, Eaton
- **Transformers:** ABB, Siemens, Prolec GE, Hammond
- **Generators:** Caterpillar, Cummins, Kohler, MTU
- **UPS systems:** Schneider Electric (Galaxy VS, Trinergy), Vertiv (Liebert EXL), Eaton (93PM)
- **EPMS:** Schneider Electric (Struxureware, EcoStruxure), Vertiv (Trellis)

**Mechanical:**
- **Chillers:** Carrier, Trane, Daikin, Johnson Controls (York)
- **CRAC/CRAH units:** Vertiv (Liebert), Schneider Electric (APC), Stulz, Munters
- **Cooling towers:** Baltimore Aircoil, Evapco, SPX Cooling
- **Pumps:** Grundfos, Armstrong, Bell & Gossett
- **BMS:** Johnson Controls (Metasys), Siemens (Desigo), Schneider Electric (EcoStruxure)

**Fire Protection:**
- **Pre-action systems:** Victaulic, Tyco, Viking
- **Fire alarm:** Notifier, Simplex, Edwards

**Low-Voltage:**
- **Access control:** HID Global, Lenel (S2), Genetec
- **CCTV:** Axis, Hanwha, Genetec (VMS)

### Vendor Evaluation Process

**Step 1: Technical Compliance**
- Review submittals against performance specifications
- Verify redundancy, efficiency, and integration requirements
- Confirm seismic and environmental ratings (Oklahoma wind/tornado loads)

**Step 2: Reference Checks**
- Contact 3 references for similar Tier III projects
- Assess reliability, support responsiveness, and warranty fulfillment

**Step 3: Total Cost of Ownership (TCO)**
- **Capital cost:** Equipment purchase price + installation
- **Operating cost:** Energy consumption (15-year NPV at $0.08/kWh)
- **Maintenance cost:** Annual service contracts + parts replacement
- **Downtime risk cost:** Probability of failure × revenue impact

**Step 4: Factory Acceptance Test (FAT)**
- Witness testing at manufacturer facility (for UPS, generators, switchgear, chillers)
- Verify performance, redundancy failover, and control integration
- Document test results for commissioning phase

---

## 0.05 CONTRACT DOCUMENTS

### Design-Build Agreement

**Base contract:**
- AIA A141 (Standard Form of Agreement Between Owner and Design-Builder) with modifications for:
  - Performance guarantees (PUE, uptime, capacity)
  - Liquidated damages and schedule incentives
  - Commissioning requirements (independent CxA, IST)

**Exhibits:**
- **Exhibit A:** Owner's Project Requirements (OPR)
- **Exhibit B:** Basis of Design (this document)
- **Exhibit C:** Site survey and geotechnical report
- **Exhibit D:** Utility coordination letters
- **Exhibit E:** Design milestones and deliverables schedule

### General Conditions

**AIA A201 (General Conditions of the Contract for Construction)** with supplements:
- **Insurance requirements:**
  - General liability: $2M per occurrence / $5M aggregate
  - Builder's risk: All-risk coverage for full project value
  - Professional liability (design team): $2M minimum
  - Workers' compensation: Statutory limits
  - Delay in startup (DSU): Optional coverage for revenue loss

- **Bonds:**
  - Bid bond: 10% of bid price
  - Performance bond: 100% of contract value
  - Payment bond: 100% of contract value

- **Warranty period:**
  - Standard: 1 year from Substantial Completion
  - Extended warranties: Per equipment manufacturer (UPS, generators, chillers, roof)

### Technical Specifications

**CSI MasterFormat organization:**
- Division 00: Procurement and Contracting (this document)
- Division 01: General Requirements (submittals, commissioning, closeout)
- Divisions 02-14: Facility Construction (site, building, finishes)
- Divisions 21-28: MEP Systems (fire protection, plumbing, HVAC, electrical, controls)
- Divisions 31-32: Site & Infrastructure (earthwork, utilities)
- Division 33: Communications (fiber, telecom pathways)

**Specification format:**
- **Part 1:** General (scope, references, submittals, quality assurance)
- **Part 2:** Products (manufacturers, materials, equipment, performance criteria)
- **Part 3:** Execution (installation, testing, commissioning, closeout)

---

## 0.06 RISK ALLOCATION

### Design-Build Risk Matrix

| Risk Category | Owner | Design-Builder | Mitigation |
|---------------|-------|----------------|------------|
| **Site conditions (geotech)** | Owner | — | Geotech report provided; differing site conditions clause allows cost/schedule adjustment |
| **Design errors** | — | Design-Builder | Professional liability insurance; design review at milestones |
| **Construction defects** | — | Design-Builder | Performance bond; 1-year warranty; commissioning verification |
| **Equipment performance** | — | Design-Builder | Performance guarantees (PUE, capacity); factory acceptance tests |
| **Schedule delays (contractor)** | — | Design-Builder | Liquidated damages; critical path management |
| **Schedule delays (owner decisions)** | Owner | — | Timely review of submittals/RFIs; change order process |
| **Utility coordination** | Shared | Shared | Owner coordinates utility service; design-builder designs interconnect |
| **Permit delays (AHJ)** | Shared | Shared | Early engagement with AHJ; design-builder manages permit applications |
| **Force majeure** | Shared | Shared | Schedule extension (no damages); insurance (builder's risk) |
| **Commissioning failures** | — | Design-Builder | Re-test at contractor expense; IST must pass before Substantial Completion |

---

## 0.07 SCHEDULE & MILESTONES

### Project Timeline (24-Month Fast-Track)

| Phase | Duration | Key Deliverables | Procurement Actions |
|-------|----------|------------------|---------------------|
| **Design-Builder Selection** | 2 months | Award DB contract | Issue RFQ/RFP; evaluate proposals |
| **Schematic Design (SD)** | 1 month | 30% design review | Engage long-lead vendors for design-assist |
| **Design Development (DD)** | 2 months | 65% design; GMP negotiation | Order switchgear, UPS, generators, chillers |
| **Construction Documents (CD)** | 2 months | 100% permit drawings | Issue subcontractor bid packages |
| **Permitting** | 2 months | Building permit, utility approvals | Continue equipment fabrication |
| **Site Work** | 3 months | Grading, utilities, foundations | Mobilize site contractor |
| **Building Shell** | 4 months | Precast erection, roof, watertight | Fabricate precast panels (overlaps with CD) |
| **MEP Rough-In** | 5 months | Electrical/mechanical infrastructure | Deliver switchgear, UPS, generators, chillers |
| **MEP Final & Startup** | 3 months | Equipment installation, startup | Factory technicians on-site |
| **Commissioning** | 3 months | Functional tests, IST, load bank tests | Independent CxA oversight |
| **Substantial Completion** | Month 20 | CO issued, owner occupancy | Punchlist <50 items |
| **Final Completion** | Month 22 | Punchlist closed, as-builts delivered | Final payment, warranty start |

**Critical Path:**
1. Utility service installation (12-18 months; must start early)
2. Long-lead equipment (switchgear, UPS, generators, chillers)
3. Building shell watertight (before MEP equipment installation)
4. Commissioning IST (final gate before Substantial Completion)

---

## 0.10 SPECIAL CONTRACT PROVISIONS

### Performance Guarantees

**PUE Guarantee:**
- **Measurement period:** 3 consecutive months post-occupancy at 50% and 80% IT load
- **Target:** PUE ≤ 1.4 at 50% load; ≤ 1.3 at 80% load
- **Penalty:** $50K per 0.1 PUE above target (max $200K)
- **Exclusions:** PUE adjusted for weather extremes (>99th percentile) and IT equipment inefficiency

**Uptime Guarantee:**
- **Tier III certification:** Design-builder responsible for achieving Uptime Institute Tier III (TCCF + TCOS)
- **Penalty:** $500K if certification cannot be achieved due to design or construction defects
- **Exclusions:** Owner-driven scope changes, utility failures beyond design criteria

**Capacity Guarantee:**
- **Phase 1:** 3 MW IT load with N+1 mechanical, 2N electrical
- **Penalty:** $100K if system cannot support 3 MW under all failure scenarios
- **Verification:** Load bank testing during commissioning

### Early Completion Incentive

**Bonus structure:**
- $10K per calendar day for Substantial Completion ahead of schedule
- Maximum 30 days early (max bonus: $300K)
- Conditions:
  - All systems commissioned and passing IST
  - Punchlist <50 items (no critical items)
  - CO issued by AHJ

### Liquidated Damages

**Schedule:**
- $10K per calendar day for late Substantial Completion (after schedule float exhausted)
- No cap on liquidated damages

**Performance:**
- PUE: $50K per 0.1 above target (max $200K)
- Capacity: $100K if IT load capacity not met
- Tier III: $500K if certification cannot be achieved

**Process:**
- Owner deducts liquidated damages from final payment
- Design-builder may dispute through contract dispute resolution process

---

## 0.11 DISPUTE RESOLUTION

### Tiered Dispute Resolution Process

**Level 1: Project Team (0-15 days)**
- Issue raised at weekly OAC meeting
- Project managers negotiate resolution

**Level 2: Senior Management (15-30 days)**
- Escalate to owner VP and design-builder senior VP
- Mediation facilitated by CxA or independent party

**Level 3: Mediation (30-60 days)**
- Engage professional mediator (AAA or JAMS)
- Non-binding mediation; costs split 50/50

**Level 4: Arbitration (60-90 days)**
- Binding arbitration per AIA A141
- Single arbitrator for disputes <$500K; panel of 3 for >$500K
- Arbitration conducted in Tulsa, Oklahoma

**Level 5: Litigation (>90 days)**
- Only if arbitration fails or is declined
- Jurisdiction: Rogers County, Oklahoma
- Costs: Prevailing party recovers attorney fees

---

## 0.12 INSURANCE & BONDING

### Required Insurance

| Type | Limit | Holder | Notes |
|------|-------|--------|-------|
| **General Liability** | $2M / $5M | Design-builder | Occurrence basis; owner as additional insured |
| **Builder's Risk** | Full project value | Owner or DB | All-risk; includes wind, hail, flood |
| **Professional Liability (E&O)** | $2M | Design team | Claims-made; 3-year tail coverage |
| **Workers' Compensation** | Statutory | Design-builder | All trades and subcontractors |
| **Auto Liability** | $1M | Design-builder | Company vehicles |
| **Umbrella/Excess** | $10M | Design-builder | Over general liability |
| **Delay in Startup (DSU)** | $5M (optional) | Owner | Revenue loss if CO delayed >30 days |

### Required Bonds

| Type | Amount | Holder | Purpose |
|------|--------|--------|---------|
| **Bid Bond** | 10% of bid | Owner | Guarantees bidder will sign contract if awarded |
| **Performance Bond** | 100% of GMP | Owner | Guarantees completion per contract |
| **Payment Bond** | 100% of GMP | Owner + Subs | Guarantees payment to subcontractors and suppliers |
| **Warranty Bond** | 50% of GMP | Owner | Guarantees warranty obligations (optional) |

**Surety Requirements:**
- A.M. Best rating: A- or better
- Treasury-listed surety company

---
