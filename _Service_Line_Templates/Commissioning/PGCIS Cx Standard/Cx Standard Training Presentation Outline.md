# PGCIS Commissioning Standard - Training Presentation Outline

**Purpose:** Comprehensive training outline for PGCIS commissioning methodology and standards
**Created:** 2025-11-20
**Status:** Active
**Tags:** #commissioning #training #pgcis #presentation #education

---

## Training Overview

**Target Audience:**
- New commissioning team members
- Project engineers and technicians
- Contractors and vendors requiring PGCIS methodology understanding
- Client representatives overseeing commissioning activities

**Duration:** 4-6 hours (full-day session with breaks)
**Format:** Interactive presentation with case studies, exercises, and Q&A
**Prerequisites:** Basic understanding of data center systems and electrical/mechanical fundamentals

---

## SECTION 1: INTRODUCTION & OVERVIEW (30 minutes)

### 1.1 Welcome and Introductions (5 min)
- Instructor introduction and credentials
- Participant introductions and experience levels
- Training objectives and agenda overview

### 1.2 What is Commissioning? (10 min)
**Slide Content:**
- Definition: "A quality-focused process for achieving, verifying, and documenting that the performance of facilities, systems, and assemblies meets defined objectives and criteria"
- Why commission data centers? (reliability, uptime, performance validation)
- Cost of poor commissioning vs. investment in quality process
- Industry statistics on commissioned vs. non-commissioned facilities

**Interactive Element:**
- Poll: "How many have worked on projects where lack of commissioning caused issues?"
- Brief discussion of real-world examples

### 1.3 PGCIS Commissioning Philosophy (15 min)
**Slide Content:**
- **100% sampling protocol** - test everything unless Owner approves exception
- **Progressive testing approach** - field device → equipment → system → integrated
- **Stop on non-compliance** - no "test through" failures
- **Documentation-driven** - if it's not documented, it didn't happen
- **Independent verification** - CxA as Owner's advocate

**Case Study:**
- Example project where 100% sampling revealed systematic issue that would have been missed with spot-checking

---

## SECTION 2: THE 5-LEVEL COMMISSIONING PROCESS (90 minutes)

### 2.1 Process Overview (10 min)
**Slide Content:**
- Visual diagram showing all 5 levels in project timeline
- Progressive nature of commissioning (can't skip levels)
- Relationship between design, construction, and commissioning phases

**Handout:**
- [[Cx Standard Quick Reference Guide - One-Page Summary]] for participants

### 2.2 Level 1 - Factory Witness Testing / Factory Acceptance Testing (15 min)

**Slide Content:**
- **Timeline:** Before equipment delivery
- **Location:** Manufacturer facility (or site for modular equipment)
- **Scope:** Factory test review, witness testing (when specified), QA/QC verification

**Key Activities:**
- Factory test procedure review and approval process
- Witness testing attendance criteria and protocols
- Equipment capacity, safety, and controls verification
- Issues log maintenance for factory deficiencies

**Scope Variations:**
- FAT only (manufacturer tests, CxA reviews reports)
- FWT (CxA attends manufacturer testing)
- Site acceptance testing (modular equipment)

**Deliverables Review:**
- Factory test reports per IEEE/NETA standards
- As-built drawings showing factory modifications
- Nameplate verification photographs
- Shipping and handling documentation
- Warranty certificates

**Discussion Questions:**
- When should an Owner require factory witness testing vs. report review only?
- What are red flags in factory test reports?

**Exercise (10 min):**
- Review sample factory test report
- Identify 3 deficiencies in the report
- Group discussion of findings

### 2.3 Level 2 - Pre-Start Up Documentation (15 min)

**Slide Content:**
- **Timeline:** During equipment delivery and installation
- **Location:** Project site
- **Scope:** Installation verification and pre-energization inspections

**Key Activities:**
- Site arrival inspections with photographic documentation
- Equipment storage verification per manufacturer requirements
- Equipment model verification (make, model, serial number)
- Pre-installation physical condition checks
- Pre-installation component verification
- Pre-energization inspection (housekeeping, labeling, panel schedules)

**Why L2 Matters:**
- Catch shipping damage before it's hidden by installation
- Verify correct equipment ordered and delivered
- Ensure proper storage to maintain warranties
- Identify installation issues before energization

**Deliverables Review:**
- Completed Level 2 documentation forms
- Delivery receipt checks with photos
- Equipment model verification records
- Installation compliance issue tracking

**Common L2 Issues:**
- Equipment stored outdoors (moisture damage)
- Wrong model/specifications delivered
- Shipping damage not documented
- Incomplete labeling or panel schedules

**Video/Photos (5 min):**
- Examples of good vs. poor equipment storage
- Shipping damage examples
- Pre-energization inspection findings

### 2.4 Level 3 - Equipment Start-Up and Pre-Functional Testing (20 min)

**Slide Content:**
- **Timeline:** Following installation, prior to Level 4
- **Location:** Project site
- **Scope:** Manufacturer startup, adjustment, and performance validation

**Key Activities:**
- Equipment startup per manufacturer procedures
- "As-left" equipment settings documentation
- Building Automation System (BAS) online verification
- Point-to-point verification (field device to BAS GUI)
- Field device calibration and verification
- Temporary Arc Flash labeling installation

**Manufacturer Startup Requirements:**
- Must be performed by qualified manufacturer representative
- All manufacturer checklists completed
- Settings documented in setpoint matrices
- Startup report signed off

**Point-to-Point Verification Process:**
- What is point-to-point? (verifying each sensor/device communicates to BAS)
- Methodology: physically stimulate device, verify BAS response
- Documentation requirements
- Common issues and troubleshooting

**Deliverables Review:**
- Completed Level 3 startup documentation
- Equipment setpoint matrices with "as-left" values
- Point-to-point verification records
- BAS/EPMS online confirmation
- **Level 1-3 Issues Log (CLOSED)** ← Critical for L4 readiness

**Exercise (10 min):**
- Point-to-point verification simulation
- Given a temperature sensor scenario, walk through verification steps
- Document results on sample form

### 2.5 Level 4 - Functional Performance Testing (20 min)

**Slide Content:**
- **Timeline:** After Level 3 completion
- **Location:** Project site
- **Scope:** Individual equipment and system functional verification

**Key Activities:**
- CxA-directed functional performance testing
- Circuit breaker and relay settings verification
- Equipment-level testing per approved sequences of operations
- System-level integrated testing
- Load bank testing (per Load Bank and Metering Plan)
- Power quality monitoring and thermal imaging
- Issue tracking with priority classifications

**Testing Philosophy:**
- Test what is written (sequences of operations)
- Test normal operation first, then abnormal/fault conditions
- Document everything - pass or fail
- Retest until acceptable

**Test Procedure Development:**
- Starting with sequence of operations
- Creating step-by-step test procedures
- Review and approval process
- Field execution requirements

**Load Bank Testing:**
- Why load bank test? (verify capacity, heat rejection, efficiency)
- Load bank types and capabilities
- Connection planning and safety
- Test duration and data collection

**Deliverables Review:**
- Approved Level 4 test procedures
- Completed test data forms with signatures
- Circuit Breaker and Relay Settings Verification Checklists
- Level 4 Issues Log with resolutions
- Daily commissioning status reports
- Thermographic survey baseline reports

**Case Study (5 min):**
- Real project where L4 testing revealed major design flaw
- Discussion of how testing methodology caught the issue
- Financial impact of finding issue before occupancy

### 2.6 Level 5 - Integrated System Testing (20 min)

**Slide Content:**
- **Timeline:** After all Level 4 tests pass
- **Location:** Project site
- **Scope:** Facility-level integrated system validation

**Key Activities:**
- Site-level systems testing under various load conditions
- Automatic response verification (no active human intervention)
- Severe operating conditions validation
- Extended duration operation tests
- Deferred testing plan development (if needed)
- Permanent Arc Flash labeling installation

**L4 vs. L5 - What's the Difference?**
- **L4:** Individual equipment and systems tested in isolation
- **L5:** Integrated facility operation tested as a whole
- **Example:** L4 tests generator starts and runs; L5 tests entire facility response to utility failure

**Typical L5 Tests (Data Center):**
- Utility failure simulation → generator start/transfer → return to normal
- Generator failure → load transfer to redundant path
- Chiller failure → lead-lag sequencing and backup activation
- Fire alarm integration → HVAC shutdown and smoke control
- Multiple simultaneous failures (N+1 validation)

**Completion Criteria:**
- All Level 4 tests successfully passed
- BAS & EPMS fully operational with trending
- All systems functioning per Owner's Requirements
- All Critical and High priority issues resolved
- Medium/Low issues resolved or deferred with Owner approval

**Deliverables Review:**
- Approved Level 5 test procedures
- Completed integrated system test data
- Level 5 Issues Log with resolutions
- **Final Commissioning Report** (within 4 weeks)
- **Certificate of Construction Phase Commissioning Completion** (within 48 hours)
- Training completion verification

**Video (5 min):**
- Time-lapse of actual L5 integrated system test
- Utility failure → generator start → facility response
- Discussion of what to observe during IST

---

## SECTION 3: ROLES & RESPONSIBILITIES (30 minutes)

### 3.1 Commissioning Team Structure (10 min)

**Slide Content:**
- Owner's representative
- Commissioning Authority (CxA)
- Design team (Architect/Engineer of Record)
- General Contractor / Construction Manager
- Installing contractors (electrical, mechanical, controls)
- Equipment manufacturers and vendors
- Third-party testing agencies (NETA)
- Facility operations team

**Organizational Chart:**
- Visual showing reporting relationships
- Authority levels for decision-making

### 3.2 RACI Matrix Deep Dive (20 min)

**Slide Content:**
- **R** = Responsible (does the work)
- **A** = Accountable (final authority and ownership)
- **C** = Consulted (provides input before action)
- **I** = Informed (notified after action)

**Key Responsibility Areas:**
- Owner's Project Requirements and BOD development
- Commissioning Plan development
- Test procedure development and approval
- Test execution and documentation
- Issue resolution and tracking
- Final acceptance and certification

**Interactive Exercise (15 min):**
- Scenario: "Equipment fails Level 4 test - who does what?"
- Participants assign RACI roles for each action
- Discussion of correct assignments and why

**Common Responsibility Confusion:**
- Who develops test procedures? (CxA develops, Owner approves, contractors consult)
- Who fixes deficiencies? (Contractor responsible, CxA verifies, Owner accepts)
- Who determines test success/failure? (CxA documents, Owner accepts)

---

## SECTION 4: DOCUMENTATION REQUIREMENTS (30 minutes)

### 4.1 Documentation Philosophy (5 min)

**Slide Content:**
- "If it's not documented, it didn't happen"
- Legal and liability protection
- Knowledge transfer to operations team
- Future troubleshooting and maintenance reference
- Warranty and insurance requirements

### 4.2 CxAlloy Platform Overview (10 min)

**Slide Content:**
- Web-accessible commissioning management platform
- Real-time progress tracking and reporting
- Equipment list and deficiency log management
- Checklist and test script execution
- File sharing and design review hosting
- User permissions and access control

**Live Demo (if available):**
- Navigate through CxAlloy interface
- Show equipment tracking
- Demonstrate issues log functionality
- Review reporting capabilities

**Alternative:** Screenshots and walkthrough if live demo not available

### 4.3 Issues Log Management (15 min)

**Slide Content:**
- Purpose: Track all deficiencies from identification through resolution
- Required information:
  - Equipment tag / system identification
  - Date identified and identified by
  - Responsible party for resolution
  - Discipline (electrical, mechanical, controls, etc.)
  - Priority classification (Critical, High, Medium, Low)
  - Description and root cause analysis
  - Resolution documentation
  - Supporting photos and data

**Priority Classification System:**
| Priority | Definition | Resolution Target | Example |
|----------|-----------|-------------------|---------|
| Critical | Impacts overall building functionality | Immediate | Life safety system failure |
| High | Impacts equipment/system functionality | 2 days | Generator fails to start |
| Medium | Impacts isolated equipment operation | 1 week | Single pump vibration |
| Low | Does not affect critical functionality | Prior to L5 | Minor labeling error |

**Issue Resolution Process:**
1. Issue identified and logged
2. Priority assigned
3. Responsible party notified
4. Root cause analysis performed
5. Corrective action implemented
6. Verification testing performed
7. Issue closed with documentation

**Exercise (10 min):**
- Participants receive 5 sample deficiencies
- Assign priority classifications
- Discuss reasoning and consensus

### 4.4 Test Documentation Standards (10 min)

**Slide Content:**
- Test procedure requirements (approved before execution)
- Test data form completion (no blank fields)
- Signature requirements (all parties present)
- Photographic evidence requirements
- Trend log and power quality data
- Retest documentation

**Examples:**
- Show completed test form (good example)
- Show incomplete test form (bad example)
- Discuss consequences of poor documentation

---

## SECTION 5: QUALITY ASSURANCE (20 minutes)

### 5.1 CxA Qualifications (5 min)

**Slide Content:**
- Minimum project experience requirements (3+ similar projects)
- Required certifications:
  - Building Commissioning Authority (BCA)
  - ASHRAE Building Commissioning Professional (BCxP)
  - University of Wisconsin - Madison Certification
- Industry memberships and continuing education

### 5.2 Test Equipment Requirements (10 min)

**Slide Content:**
- Calibration requirements (12-month maximum, NIST-traceable)
- Permanent calibration tags and certificates
- Equipment categories:
  - Power quality analyzers (Class A per IEC 61000-4-30)
  - Multimeters (True RMS, CAT III/IV rated)
  - Load banks (resistive, sized appropriately)
  - Thermal imaging cameras (minimum specifications)
  - Metering equipment (revenue-grade accuracy)

**Why Calibration Matters:**
- Measurement accuracy and reliability
- Legal defensibility of test results
- Insurance and warranty requirements

### 5.3 NETA Testing Requirements (5 min)

**Slide Content:**
- Independent third-party electrical testing
- NETA certified company with 10+ years experience
- Testing per most recent NETA Acceptance Testing Standard
- Coordination with CxA Level 4 testing
- Report review and acceptance criteria

---

## SECTION 6: PRACTICAL APPLICATION (60 minutes)

### 6.1 Case Study 1: Successful Commissioning Project (15 min)

**Presentation:**
- Project overview (size, complexity, timeline)
- Commissioning challenges encountered
- How 5-level process identified and resolved issues
- Final outcomes and client satisfaction
- Lessons learned

**Discussion:**
- What made this project successful?
- How did commissioning add value?

### 6.2 Case Study 2: Lessons Learned from Problematic Project (15 min)

**Presentation:**
- Project overview
- What went wrong and why
- Impact of commissioning issues on project
- How issues were resolved
- Changes implemented for future projects

**Discussion:**
- Red flags that should have been caught earlier
- Importance of following the process

### 6.3 Table-Top Exercise: Plan a Commissioning Approach (30 min)

**Scenario Provided:**
- New 5MW data center project
- Project schedule and key milestones
- Equipment list (generators, UPS, chillers, etc.)
- Current project status (30% design complete)

**Exercise Instructions:**
- Small groups (3-4 people)
- Develop high-level commissioning plan using 5-level process
- Identify key milestones and deliverables
- Present 5-minute summary to class

**Deliverable:**
- Simple commissioning schedule showing L1-L5
- Key equipment to be commissioned
- Testing priorities

**Group Presentations and Feedback:**
- Each group presents approach
- Instructor provides feedback
- Class discussion of different approaches

---

## SECTION 7: SPECIAL TOPICS (30 minutes)

### 7.1 Arc Flash Labeling Requirements (10 min)

**Slide Content:**
- NFPA 70E requirements
- Temporary labeling during commissioning
- Permanent labeling after L5 completion
- Incident energy calculations
- PPE requirements

### 7.2 Load Bank Testing Deep Dive (10 min)

**Slide Content:**
- Load bank types (resistive, reactive, combined)
- Sizing and connection planning
- Safety protocols and permits
- Test duration and data collection requirements
- Common issues and troubleshooting

**Reference Material:**
- [[Cx Standard Appendix B - Load Bank and Metering Plan Template]]

### 7.3 Seasonal and Deferred Testing (10 min)

**Slide Content:**
- When is deferred testing appropriate?
- Owner approval requirements
- Documentation and scheduling
- Completion tracking and verification
- Impact on Certificate of Completion

**Examples:**
- Cooling system capacity testing in winter
- Heating system testing in summer
- Free cooling economizer testing (seasonal conditions)

---

## SECTION 8: TOOLS AND TEMPLATES (15 minutes)

### 8.1 PGCIS Standard Documents Overview (10 min)

**Documents Review:**
- [[PGCIS Commissioning Standard - Master Specification]]
- [[Cx Standard README]] - User guide for the standard
- [[Cx Standard Appendix A - Testing Outline Template]]
- [[Cx Standard Appendix B - Load Bank and Metering Plan Template]]
- [[Cx Standard Level 1-5 Documentation Summary Checklists Template]]
- [[Cx Standard Quick Reference Guide - One-Page Summary]]

**How to Use Templates:**
- When to use each template
- Customization for specific projects
- Integration with CxAlloy platform

### 8.2 AI-Assisted Commissioning with Claude (5 min)

**Slide Content:**
- Using Claude Code with PGCIS templates
- Example prompts:
  - "Create a Level 4 test procedure for UPS system based on PGCIS Cx Standard"
  - "Generate a commissioning schedule for [project] using PGCIS 5-level process"
  - "Review this contractor submittal against PGCIS Cx Standard requirements"
- Benefits of AI-assisted documentation
- Limitations and review requirements

---

## SECTION 9: Q&A AND WRAP-UP (30 minutes)

### 9.1 Open Q&A (20 min)

**Format:**
- Open floor for any questions
- Instructor addresses common concerns
- Sharing of participant experiences

### 9.2 Key Takeaways (5 min)

**Summary Slide:**
- 5-level commissioning process is systematic and progressive
- Documentation is critical - "if it's not documented, it didn't happen"
- 100% sampling protocol ensures quality
- Roles and responsibilities must be clear
- Testing doesn't stop until acceptable results achieved
- Final acceptance requires all issues resolved or deferred with approval

### 9.3 Resources and Next Steps (5 min)

**Slide Content:**
- Access to PGCIS Commissioning Standard documents
- CxAlloy training and access
- Recommended reading and certifications
- Continuing education opportunities
- Contact information for technical support

### 9.4 Training Evaluation (5 min)

**Feedback Form:**
- Training content and delivery evaluation
- Suggestions for improvement
- Additional topics desired
- Self-assessment of learning outcomes

---

## APPENDIX: PRESENTATION DEVELOPMENT GUIDELINES

### Visual Design Recommendations

**Slide Design:**
- Use PGCIS branding and color scheme
- Limit text per slide (6×6 rule: max 6 bullets, 6 words per bullet)
- High-quality images and diagrams
- Consistent font and formatting

**Effective Visuals:**
- Process flow diagrams
- Before/after photos
- Equipment identification photos
- Sample documents and forms
- Video clips of testing activities

### Handouts and Materials

**Participant Packet:**
- Training agenda and objectives
- [[Cx Standard Quick Reference Guide - One-Page Summary]] (laminated)
- Sample test procedures
- Sample issues log
- Exercise worksheets
- Resource list and contacts

**Digital Resources:**
- USB drive or shared folder with all PGCIS templates
- Sample project documentation
- Reference standards and codes (where permitted)
- CxAlloy quick start guide

### Interactive Elements

**Engagement Strategies:**
- Live polling (if technology available)
- Small group discussions
- Hands-on exercises
- Real equipment demonstrations (if possible)
- Video case studies
- Q&A throughout (not just at end)

### Instructor Preparation

**Pre-Training:**
- Review all PGCIS standard documents
- Prepare case studies from actual projects
- Test all technology (projector, videos, demos)
- Prepare backup materials (printed slides in case of tech failure)
- Arrive early to set up and test equipment

**During Training:**
- Encourage questions throughout
- Monitor participant engagement
- Adjust pace based on comprehension
- Use real-world examples liberally
- Take breaks every 60-90 minutes

**Post-Training:**
- Distribute evaluation forms
- Provide contact information for follow-up questions
- Share presentation materials digitally
- Schedule follow-up coaching sessions (if requested)

---

## TRAINING VARIATIONS

### Half-Day Overview (3 hours)
Condense to essentials:
- Introduction and overview (20 min)
- 5-level process summary (60 min)
- Roles and documentation (30 min)
- Case study (20 min)
- Q&A (20 min)

### Advanced Workshop (2 days)
Expand with:
- Detailed test procedure development workshop
- CxAlloy hands-on training
- Extended case studies and exercises
- Field trip to active commissioning site
- Test equipment hands-on practice

### Contractor Orientation (1 hour)
Focus on:
- What is commissioning and why it matters
- Contractor responsibilities in 5-level process
- Documentation requirements
- Issues resolution process
- Q&A

### Client/Owner Overview (1 hour)
Focus on:
- Value proposition of commissioning
- Owner responsibilities and approvals
- What to expect at each level
- Deliverables and timelines
- ROI and risk mitigation

---

**Related Documents:**
[[PGCIS Commissioning Standard - Master Specification]] | [[Cx Standard README]] | [[Cx Standard Quick Reference Guide - One-Page Summary]] | [[Cx Standard Appendix A - Testing Outline Template]] | [[Cx Standard Appendix B - Load Bank and Metering Plan Template]] | [[Cx Standard Level 1-5 Documentation Summary Checklists Template]]

---

**Document Version:** 1.0
**Last Updated:** 2025-11-20
**Maintained By:** PGCIS Technical Training Team
**Review Cycle:** Annually or after major training session feedback
