📄 Reading markdown file...
🔍 Parsing markdown...
   Found 908 blocks
🔐 Authenticating with Google...
📝 Creating Google Doc...

✅ Document published successfully!

   Title: Attachment A - Commissioning_Plan_Outline_Template
   URL:   https://docs.google.com/document/d/1u_uMIMm7JZEi07qGQT_G3UJEMMMs_9nLyvt7HRhYbe4/edit

# DATA CENTER COMMISSIONING PLAN OUTLINE
## Generic Template for Proposal Attachment

**Created:** 2025-11-09
**Purpose:** Template outline for data center commissioning plan appendix
**Tags:** #commissioning #data-center #proposal #hut8

---

## DOCUMENT CONTROL

**Version:** [X.X]
**Date:** [Date]
**Project:** [Project Name]
**Prepared By:** [Company Name]
**Prepared For:** [Client Name]

---

## TABLE OF CONTENTS

1. Introduction
2. Project Description
3. Reference Documentation
4. Acronyms and Abbreviations
5. Commissioning Plan Objectives
6. Management Strategy
7. Commissioning Platform/Documentation System
8. Issue Resolution Process
9. Handover to Commissioning (H2C)
10. Commissioning Overview and Deliverables
11. Commissioning Levels (1-6)
12. Document Storage & Responsibility
13. Load Bank and Monitoring Plan
14. Firmware & Software Change Management
15. Additional Testing
16. Project Closeout
17. Commissioning Schedule
18. Reporting & Forecasting
19. Meetings
20. Roles & Responsibilities
21. Control Sequence/Sequence of Operations Review
22. Lessons Learned
23. Training Requirements
24. Safety
25. Commissioning Glossary
26. Annex Overview

---

## 1. INTRODUCTION

### 1.1 Purpose
The purpose of this Commissioning (Cx) Plan is to provide a comprehensive framework and structure for the commissioning process of [Project Name]. This plan establishes the methodology, responsibilities, and documentation requirements to ensure all facility systems are designed, installed, tested, operated, and maintained to meet the Owner's Project Requirements.

### 1.2 Living Document
This Commissioning Plan is a living document that will be continuously updated throughout all levels of commissioning. Updates will be communicated to all stakeholders and versioned appropriately.

### 1.3 Plan Alignment
This plan should be read in conjunction with:
- Project design documents
- Basis of Design (BOD)
- Owner's Project Requirements (OPR)
- Contract specifications
- Industry standards and applicable codes

### 1.4 Commissioning Authority
[Commissioning Authority Name] has been appointed as the independent Commissioning Authority (CxA) for this project. The CxA will lead, plan, schedule, and coordinate the commissioning team to implement this Commissioning Process.

### 1.5 Quality Assurance Focus
The commissioning process ensures:
- Equipment is constructed and installed correctly
- Systems operate per design intent
- The facility performs in accordance with client requirements
- Operations will not be compromised during normal or adverse conditions
- A reliable environment is provided for critical loads

---

## 2. PROJECT DESCRIPTION

### 2.1 Project Overview
[General description of the data center project, location, and purpose]

### 2.2 Facility Capacity
- **Total IT Load:** [XX MW]
- **Facility Size:** [Square footage]
- **Number of Data Halls:** [Number]
- **Redundancy Level:** [N, N+1, 2N, etc.]
- **Tier Classification:** [Tier I-IV]

### 2.3 Scope of Work
[Detailed description of project scope including:]

#### Infrastructure Components
- **Power Systems:**
  - Utility service capacity: [XX MVA]
  - Medium voltage distribution
  - Generator capacity and quantity
  - UPS systems capacity and configuration
  - Low voltage distribution
  - Power distribution units (PDUs)

- **Mechanical Systems:**
  - Cooling architecture (air-cooled, water-cooled, hybrid)
  - Chilled water plant capacity (if applicable)
  - CRAH/CRAC units quantity and capacity
  - Air handling systems
  - Pumping systems

- **Building Management Systems:**
  - BMS platform and scope
  - EPMS (Electrical Power Monitoring System)
  - Integration requirements

- **Support Systems:**
  - Fire detection and suppression
  - Security systems
  - Leak detection
  - Environmental monitoring

### 2.4 Project Phases
[Description of phased delivery approach, if applicable]

---

## 3. REFERENCE DOCUMENTATION

### 3.1 Industry Standards
All commissioning and testing activities shall comply with applicable standards including:

- **ASHRAE** – American Society of Heating, Refrigerating and Air-Conditioning Engineers
  - Guideline 0: The Commissioning Process
  - Guideline 1.1: HVAC&R Technical Requirements for The Commissioning Process
  - TC 9.9 Mission Critical Facilities

- **Electrical Standards:**
  - NFPA 70: National Electrical Code
  - IEEE Standards (as applicable)
  - NETA Standards for Acceptance Testing
  - Local electrical codes and regulations

- **Building Codes:**
  - Local building authorities having jurisdiction
  - International Building Code (IBC)
  - Life safety codes

- **Data Center Specific:**
  - Uptime Institute Tier Standards
  - TIA-942: Telecommunications Infrastructure Standard for Data Centers
  - EN 50600 (European Standard for Data Centres)

### 3.2 Project-Specific Documents
- Owner's Project Requirements (OPR)
- Basis of Design (BOD)
- Design drawings and specifications
- Equipment submittals and shop drawings
- Contract documents
- [Additional project-specific standards]

---

## 4. ACRONYMS AND ABBREVIATIONS

| Acronym | Definition |
|---------|------------|
| BOD | Basis of Design |
| BMS | Building Management System |
| CRAC | Computer Room Air Conditioner |
| CRAH | Computer Room Air Handler |
| Cx | Commissioning |
| CxA | Commissioning Authority/Agent |
| DCR | Daily Commissioning Report |
| EPMS | Electrical Power Monitoring System |
| FAT | Factory Acceptance Test |
| FPT | Functional Performance Test |
| FWT | Factory Witness Test |
| GC | General Contractor |
| H2C | Handover to Commissioning |
| HVAC | Heating, Ventilation & Air Conditioning |
| IRL | Issue Resolution Log |
| IST | Integrated Systems Test |
| ITIC/CBEMA | Information Technology Industry Council/Computer Business Equipment Manufacturers Association |
| LV | Low Voltage |
| MV | Medium Voltage |
| O&M | Operations and Maintenance |
| OPR | Owner's Project Requirements |
| PDU | Power Distribution Unit |
| PFT | Pre-Functional Test |
| PQM | Power Quality Meter |
| QA/QC | Quality Assurance/Quality Control |
| RFSU | Ready for Start-Up |
| SAI | Site Acceptance Inspection |
| SAT | Site Acceptance Test |
| SoO | Sequence of Operation |
| TAB | Test and Balance (Air & Water) |
| UPS | Uninterruptible Power Supply |

---

## 5. COMMISSIONING PLAN OBJECTIVES

### 5.1 Primary Objectives
The commissioning process shall achieve the following objectives:

1. **Design Verification**
   - Verify no mechanical and electrical coordination issues exist
   - Identify and eliminate single points of failure (SPoFs)
   - Review construction drawings, specifications, and submittals for compliance

2. **Installation Quality Assurance**
   - Ensure equipment and systems are installed properly
   - Verify adequate quality control through site observation
   - Document installation compliance with design intent

3. **Performance Validation**
   - Provide owner with high-level assurance that systems are installed and operating correctly
   - Verify compliance with design intent and contract documents
   - Document system performance against acceptance criteria

4. **Integrated Systems Testing**
   - Verify emergency and redundant systems operate as designed
   - Test interrelated systems in complex failure scenarios
   - Prove systems perform appropriately when called upon
   - Validate fail-safe operations

5. **Documentation & Knowledge Transfer**
   - Deliver comprehensive systems manual
   - Provide searchable reference of as-built documentation
   - Document O&M procedures and requirements
   - Train operations staff

### 5.2 Quality Focus
This commissioning process:
- Does not diminish designer or contractor responsibility
- Is not redundant testing or inspection
- Documents and validates design and construction efforts
- Ensures quality meets Owner's Project Requirements

### 5.3 Handover Criteria
The successful completion of Integrated Systems Testing (IST) shall:
- Act as verification of substantial completion
- Trigger contractual milestone achievements
- Enable transition to operational readiness phase

---

## 6. MANAGEMENT STRATEGY

### 6.1 Responsibility Matrix

| Phase/Activity | Manage Task | Support Task |
|----------------|-------------|--------------|
| **Level 0 – Design Reviews & Cx Plan** | CxA | GC / Owner |
| **Level 1 – Factory Tests & Equipment Delivery (Red Tag)** | GC | Vendors / CxA |
| **Level 2 – QA/QC (Yellow Tag)** | GC | Vendors / CxA |
| **Level 3 – Start-Ups (Green Tag)** | GC | Vendors / CxA |
| **Level 4 – FPT (Blue Tag)** | CxA | GC / Vendors |
| **Level 5 – IST (White Tag)** | CxA | GC / Vendors |
| **Level 0-3 Meetings (Design/Progress)** | GC | Vendors / CxA |
| **Level 4-5 Meetings** | CxA | GC / Vendors / Owner |
| **Cx Tagging L1-L3** | GC | Vendors |
| **Cx Tagging L4-L5** | CxA | GC |
| **O&M Production** | GC / Vendor | CxA / Owner / Design Team |
| **Training Plan** | GC | Design Team / CxA / Owner |
| **Standard Operating Procedures** | GC / Vendor | Design Team / CxA / Owner |
| **L1-L3 Test Script Development** | GC / Vendor | Design Team / CxA / Owner |
| **L4-L5 Test Script Development** | CxA | Owner / Design Team |
| **Weekly Cx Meetings** | CxA | Owner / GC / Vendors |
| **Customer Meetings** | Owner | CxA |

### 6.2 Collaboration Requirements
- All stakeholders shall contribute to test script development
- Client/customer shall have opportunity to comment on all procedures
- Client/customer shall have opportunity to witness all testing activities
- Minimum [X] weeks notice shall be provided for all major test events

---

## 7. COMMISSIONING PLATFORM/DOCUMENTATION SYSTEM

### 7.1 Platform Overview
[Name of commissioning management platform] will serve as the primary documentation and tracking system for commissioning activities across all levels (L1-L5).

### 7.2 Platform Capabilities
- Web-based and mobile application access
- Offline mode with synchronization capability
- Equipment and asset tracking
- Test procedure execution and documentation
- Issue tracking and resolution workflow
- Document storage and linking
- Progress reporting and dashboards
- Data export capabilities (Excel, PDF)

### 7.3 Platform Setup
- Platform configuration: CxA responsibility
- User access provisioning: All contractors, vendors, and stakeholders
- Equipment list import and management
- Tag checklist creation and assignment
- Workflow configuration per commissioning levels

### 7.4 Usage by Commissioning Level

**Levels 1-3 (GC Responsibility):**
- Equipment delivery documentation
- Red Tag (L1) checklist execution
- Yellow Tag (L2) pre-startup verification
- Green Tag (L3) startup and testing documentation
- Supporting document uploads (test reports, vendor documentation)
- Issue creation and tracking

**Levels 4-5 (CxA Responsibility):**
- Blue Tag (L4) functional performance test execution
- White Tag (L5) integrated systems test execution
- Test data collection and analysis
- Issue verification and closure
- Final documentation compilation

### 7.5 Document Types Stored
- Factory test reports and certifications
- Installation verification checklists
- Pre-startup inspection records
- Startup and commissioning reports
- Functional performance test results
- Integrated systems test results
- Power quality monitoring data
- Environmental monitoring data
- Calibration certificates
- As-built settings and configurations
- Issue logs with photographic evidence
- Meeting minutes and action items

---

## 8. ISSUE RESOLUTION PROCESS

### 8.1 Issue Management System
All commissioning issues shall be documented, tracked, and resolved through the commissioning platform issue resolution log (IRL).

### 8.2 Issue Documentation Requirements
When creating an issue, the following information shall be included:

**Issue Identification:**
- Descriptive title
- Issue category (design, installation, performance, documentation, safety)
- Photographs of the issue (when applicable)
- Test number or activity during which issue was observed
- System, subsystem, and equipment affected
- Equipment location and tag number
- Date and time of discovery
- Person identifying the issue

**Issue Description:**
- Detailed description of the problem
- Observed versus expected condition
- Reference to applicable standard, specification, or requirement
- Diagnostic information
- Recommended corrective action
- Assigned party responsible for resolution
- Target resolution date

### 8.3 Issue Resolution Documentation
When resolving an issue, the following shall be provided:

- Root cause analysis
- Diagnostic steps taken
- Description of corrective action implemented
- Photographs of completed work (when applicable)
- Impact on contract documents (if any)
- Verification that system is ready for retest (if applicable)
- Person(s) who completed the work
- Date of completion

### 8.4 Issue Priority Levels

**Priority 1 – Critical/Progress Limiting:**
- Safety hazard
- Prevents substantial completion
- Major system non-functionality
- Single point of failure identified
- Required resolution before proceeding

**Priority 2 – Retest Required by CxA:**
- System operates but not per specification
- Performance deficiency
- Requires CxA witnessing of correction
- May impact other systems

**Priority 3 – No Retest Required:**
- Documentation deficiency
- Minor deviation from specification
- Does not impact system operation
- Verification via photo or document review

### 8.5 Issue Workflow – Levels 1-3

1. **Issue Raised** → Documented in platform by GC, vendor, or CxA
2. **Assign** → Responsible party and priority assigned
3. **Due Date** → Completion target established
4. **Issue Open** → Active work to resolve
5. **Correction in Progress** → Status updates provided
6. **Ready for Verification** → Contractor indicates completion
7. **GC Review** → GC verifies completion and supporting evidence
8. **Issue Closed** → GC closes issue (or returns to "not fixed" status)

### 8.6 Issue Workflow – Levels 4-5

1. **Issue Raised** → Documented by CxA during testing
2. **Assign** → Responsible party and priority assigned
3. **Due Date** → Completion target established
4. **Issue Open** → Active work to resolve
5. **Correction in Progress** → Status updates provided
6. **Ready for Verification** → Contractor indicates completion
7. **GC Verify** → GC verifies and selects "GC Verified" status
8. **CxA Review** → CxA reviews completion and supporting evidence
9. **Issue Closed** → CxA closes issue (or returns to appropriate status)

### 8.7 Issue Tracking and Reporting
- Issues shall be reviewed at all commissioning meetings
- Issue aging reports shall be produced weekly
- Priority 1 issues shall be escalated to owner immediately
- Open issues preventing progress shall be highlighted on schedule
- Issue resolution rate shall be tracked as KPI
- All issues must be closed prior to final handover

---

## 9. HANDOVER TO COMMISSIONING (H2C)

### 9.1 H2C Definition and Significance
The "Handover to Commissioning" (H2C), also known as Green Tag Handover (GTH), represents a critical transition between the Construction Phase and the Acceptance Phase. This milestone signifies that:

- Systems commissioning is complete
- Equipment has been properly started up
- All inspections and tests are completed
- All issues are resolved and closed
- Documentation is submitted and complete
- System settings and parameters are verified

### 9.2 H2C Prerequisites

**Level 3 Completion:**
- All Level 3 commissioning successfully passed without deficiencies
- No open Priority 1 or Priority 2 issues
- All required documentation uploaded and verified

**System Configuration:**
- All systems configured for fully automatic operation
- All alarms and enunciations active and functional
- Control sequences verified and operational
- Set points established per design

**Testing Infrastructure:**
- Load banks in place and operational to test 100% capacity
- Safety facilities and procedures implemented
- Required support resources available (contractors, vendors)

**Monitoring Systems:**
- BMS/EPMS alarm-free (or open alarms justified and documented)
- All monitoring points verified and operational
- Approved monitoring points list issued to CxA
- Trending and data collection functional

**Documentation:**
- Level 3 documentation closed and available
- As-built drawings updated
- Equipment settings recorded
- O&M manuals submitted (draft)

**Testing Readiness:**
- Level 4 test scripts approved and ready for execution
- CxA training on monitoring systems completed (if required)
- Issue Resolution Log current with no major blockers
- Load bank plan approved
- Power quality monitoring plan approved

### 9.3 H2C Prerequisite Tracker
A formal prerequisite tracker shall be maintained showing:
- Prerequisite item description
- Responsible party
- Target completion date
- Actual completion date
- Status (pending, in progress, complete)
- Supporting documentation reference

### 9.4 H2C Meeting
A formal H2C meeting shall be conducted prior to commencing Level 4 activities:
- Review of prerequisite tracker
- Confirmation of system readiness
- Review of test schedule
- Confirmation of resource availability
- Review of open issues
- Approval to proceed with Level 4

### 9.5 Post-H2C Responsibilities

**General Contractor:**
- Load bank installation, movement, repairs, removal
- Fire watch during testing
- LOTO (Lockout/Tagout) and electrical switching support
- Construction power for test equipment
- Internet connectivity for testing
- Vendor and subcontractor coordination for issue resolution

**Equipment Vendors:**
- Equipment operation support during testing
- Equipment inspection support
- Issue resolution support for their equipment
- Technical expertise as needed

**Controls Vendors:**
- Access to control systems for monitoring
- Training for CxA on monitoring systems (if required)
- Trending and screenshot support from control systems
- Programming support for issue resolution
- System modification support (via change control)

**Commissioning Authority:**
- Test execution and coordination
- Issue identification and documentation
- Test data collection and analysis
- Progress reporting

### 9.6 Post-H2C Change Control
Following H2C:
- No changes to monitoring systems, software, or graphics without CxA approval
- Any changes require formal change request and review
- CxA determines if additional testing required
- Previous commissioning may be voided if changes made without approval

---

## 10. COMMISSIONING OVERVIEW AND DELIVERABLES

### 10.1 Project Organization Chart
[Organization chart showing relationships between:]
- Owner/Client
- End Customer (if different)
- General Contractor
- Commissioning Authority
- Design Team
- Major Vendors/Subcontractors
- Commissioning Team Members

### 10.2 Commissioning Equipment List
The approved equipment list includes all systems and equipment to be commissioned:

**Major Systems:**
- Utility service equipment
- Medium voltage switchgear and distribution
- Emergency generators
- Automatic transfer switches (ATS)
- UPS systems
- Low voltage switchgear and distribution
- Power distribution units (PDUs)
- Busway systems
- Chilled water plant equipment (if applicable)
- Cooling distribution equipment (pumps, piping)
- CRAH/CRAC units
- Air handling units
- Building management system
- Electrical power monitoring system
- Fire detection and suppression
- Leak detection systems
- Security systems
- Ancillary systems

[Reference to detailed equipment list in appendix]

### 10.3 CxA Organization Chart
[CxA team structure showing:]
- Project Manager
- Lead Electrical Commissioning Engineer
- Lead Mechanical Commissioning Engineer
- Supporting Commissioning Engineers
- Administrative Support

### 10.4 Commissioning Levels Summary (1-5)

| Level | Tag Color | Description | Responsible | Accountable |
|-------|-----------|-------------|-------------|-------------|
| **Level 1** | **Red** | Factory Testing & Equipment Installation - Equipment delivered with factory test documentation, installed per drawings without functional testing | Vendors | GC |
| **Level 2** | **Yellow** | Pre-Startup & Pre-Commissioning - Installation verified, pre-startup inspections complete, safe to energize | Vendors | GC |
| **Level 3** | **Green** | Energization, Start-Up & Commissioning - Equipment started up, load tested individually, vendor commissioning complete | Vendors | GC |
| **Level 4** | **Blue** | Functional Performance Testing - All modes of operation tested under load, system-level functionality verified | CxA | CxA |
| **Level 5** | **White** | Integrated Systems Test - Facility tested as complete system, redundancy and fail-safe operations verified | CxA | CxA |

### 10.5 Commissioning Tag/Placard
Physical equipment placards shall be installed on all commissioned equipment showing:

**Tag Format:**
- Equipment/System reference number
- Red section: "Not Ready for Start-Up" (Signature & Date)
- Yellow section: "Ready for Start-Up" (Signature & Date)
- Green section: "Ready for Level 4 FPT" (Signature & Date)
- Blue section: "Ready for IST" (Signature & Date)
- White section: "Cx Complete" (Signature & Date)

**Tag Requirements:**
- Durable, weatherproof material
- Minimum size: [specify dimensions]
- Location: Visible on equipment without obstruction
- Include company logos: Owner, GC, CxA
- Permanent attachment method

---

## 11. COMMISSIONING LEVELS

### 11.1 Level 1 – Factory Tests & Equipment Installation

#### 11.1.1 Level 1 Overview - RED TAG
Level 1 encompasses factory testing (FWT/FAT) and verification of proper equipment installation.

**Objective:** Verify equipment is manufactured correctly, tested at factory, shipped properly, and installed per design documents.

**Tag Status:** RED TAG - "Not Ready for Start-Up"

#### 11.1.2 Factory Witness Testing (FWT)

**FWT Scope:**
- Witness testing at manufacturer's facility
- Verification of equipment performance against specifications
- Documentation of test results
- Quality inspection of manufacturing

**FWT Process:**
1. **Script Development**
   - Vendor develops test procedure
   - GC reviews and comments
   - CxA reviews and comments
   - Client/customer reviews and comments
   - Final approval minimum [X] weeks before test date

2. **Test Logistics**
   - Minimum [X] weeks notice for FWT scheduling
   - Travel arrangements coordinated
   - Attendance confirmed (GC, CxA, Owner as desired)

3. **Pre-Test Meeting**
   - Review test procedure
   - Confirm equipment configuration
   - Review safety requirements
   - Establish roles and responsibilities

4. **Test Execution**
   - Conduct testing per approved procedure
   - Document all test results
   - Photograph equipment and test setup
   - Record any deviations or issues

5. **Documentation**
   - Manufacturer test report
   - Type test certificates
   - Calibration certificates
   - Equipment data sheets
   - Test measurements and recordings
   - Photographic documentation

6. **Post-Test Activities**
   - Post-test meeting to review results
   - Document issues in IRL
   - Combined FWT report issued by GC
   - Draft report to client/customer for comment
   - Final report approved

**FWT Requirements:**
- One FWT per equipment type/model
- Testing shall verify sequence of operations
- All operational modes tested (as applicable)
- Interface testing with control systems
- Factory environment simulations (where possible)
- Testing must be complete before shipping authorization

**Re-Testing:**
- CxA reserves right to reject equipment if issues not resolved
- Failed tests require three (3) successful consecutive re-tests
- Critical failures may require complete test sequence repetition

#### 11.1.3 Equipment Delivery and Installation

**Delivery Inspection:**
- Visual inspection upon arrival
- Verification against packing list
- Damage assessment and documentation
- Proper storage conditions verified
- Documentation package verified

**Installation Verification:**
- Installed per approved drawings
- Manufacturer clearances maintained
- Access for maintenance verified
- Ancillary equipment and connections complete
- Nameplate and labeling correct
- Equipment anchoring and seismic bracing (if required)
- Final finishes and touch-up complete

#### 11.1.4 Level 1 Documentation
- Factory test reports (one per equipment type)
- Delivery inspection reports (all equipment)
- Installation verification checklists (all equipment)
- Packing lists and shipping documentation
- Equipment certifications and warranties
- Calibration certificates
- Type test certificates
- Any deviations or non-conformances

#### 11.1.5 Red Tag Criteria
Red Tag shall be applied when:
- Factory testing successfully completed (if applicable)
- Equipment delivered to site without damage
- Installation complete per drawings and specifications
- Installation inspection checklist complete
- Required documentation uploaded to platform
- Visual inspection passed
- Equipment ready for pre-startup activities

---

### 11.2 Level 2 – Site Acceptance Inspection (SAI)

#### 11.2.1 Level 2 Overview - YELLOW TAG
Level 2 encompasses pre-startup inspections, dead testing, and verification that equipment is safe to energize.

**Objective:** Establish benchmark for quality control and provide auditable documentation of construction quality.

**Tag Status:** YELLOW TAG - "Ready for Start-Up"

#### 11.2.2 Level 2 Responsibilities
- **Manage:** General Contractor
- **Execute:** Vendors and installing contractors
- **Review:** CxA (periodic sample inspections)
- **Verify:** GC quality control team

#### 11.2.3 Pre-Startup Inspections

**Electrical Systems:**
- Insulation resistance testing (megger testing)
- Hi-pot testing (where applicable)
- Ground resistance testing
- Phasing and rotation verification
- Torque verification of electrical connections
- Breaker timing and trip testing
- Protection relay settings verification
- Cable tray and conduit installation inspection
- Grounding and bonding verification
- Arc flash labeling

**Mechanical Systems:**
- Hydrostatic testing of piping systems
- Pipe flushing and cleaning
- Water treatment and chemical balancing
- Ductwork cleaning and verification
- Duct leakage testing
- Refrigerant piping pressure testing
- Refrigerant charging (if applicable)
- Filter installation and verification
- Belt tension and alignment
- Vibration isolation verification

**Control Systems:**
- Point-to-point checkout of all I/O
- Control panel wiring verification
- Network communications verification
- Sensor calibration verification
- Control valve and damper stroking
- Safety interlocks verification
- Power supply verification for all controllers

#### 11.2.4 Vendor Pre-Startup Procedures
Each equipment vendor shall:
- Develop pre-startup checklist
- Submit checklist for GC/CxA review
- Execute checklist prior to energization
- Document all pre-startup activities
- Verify equipment ready for energization
- Upload documentation to platform
- Participate in pre-startup inspection

#### 11.2.5 Inspection Approach
- **No sampling** - Each piece of equipment receives full inspection
- Inspections completed before startup
- GC develops inspection checklists in collaboration with vendors
- Checklists address all safety and operational requirements
- Industry standards and manufacturer requirements incorporated

#### 11.2.6 CxA Sample Review
- CxA reviews completed inspections on sample basis
- CxA reserves right to conduct 100% verification if quality issues identified
- CxA may require re-inspection or additional testing
- CxA periodic site visits during Level 2 activities

#### 11.2.7 Level 2 Documentation
- Pre-startup inspection checklists (all equipment)
- Insulation resistance test reports
- Hi-pot test reports
- Ground resistance test reports
- Hydrostatic test reports
- Pipe flushing and cleaning reports
- Water treatment reports and chemical analysis
- Ductwork cleanliness certification
- Point-to-point checkout sheets
- Sensor calibration records
- Control valve stroke testing results
- Torque verification records
- Protection relay test reports
- Equipment settings record (as-found)

#### 11.2.8 Yellow Tag Criteria
Yellow Tag shall be applied when:
- Red Tag complete
- All electrical and mechanical inspections complete
- All dead testing complete and passed
- Vendor pre-startup procedures complete
- Equipment confirmed safe to energize
- All Level 2 documentation submitted and reviewed
- No open Priority 1 or 2 issues for that equipment
- Pre-energization meeting complete (for systems)

---

### 11.3 Level 3 – Energization, Start-Up & Commissioning

#### 11.3.1 Level 3 Overview - GREEN TAG
Level 3 encompasses energization, startup, individual equipment commissioning, and load testing.

**Objective:** Verify equipment operates correctly when energized and performs at rated capacity under load.

**Tag Status:** GREEN TAG - "Ready for Level 4 FPT"

#### 11.3.2 Level 3 Responsibilities
- **Manage:** General Contractor
- **Execute:** Vendors and installing contractors
- **Witness:** CxA (periodic inspections)
- **Support:** Controls vendors, equipment vendors

#### 11.3.3 Pre-Energization Activities

**Pre-Energization Meeting:**
- Review energization procedure and sequence
- Discuss safety procedures and requirements
- Review lockout/tagout (LOTO) procedures
- Confirm emergency shutdown procedures
- Verify required personnel present
- Review communication protocols
- Confirm first energization authority

**Pre-Energization Verification:**
- Yellow Tag in place
- Area clear of personnel and obstructions
- Safety barriers and signage in place
- Fire watch established (if required)
- Test equipment in place
- Monitoring equipment ready
- Emergency contact information posted

#### 11.3.4 Startup Procedures

**Initial Energization:**
- Follow manufacturer startup procedures
- Document voltage and current readings
- Monitor for abnormal conditions
- Verify rotation (rotating equipment)
- Check for proper operation of safeties
- Verify no unusual noise or vibration
- Thermal imaging (IR scan) of connections
- Document as-left settings

**Vendor Startup:**
- Manufacturer representative present (critical equipment)
- Startup per manufacturer procedures
- Functional checkout of all components
- Verification of control sequences
- Adjustment of settings as required
- Load testing (as applicable for Level 3)
- Performance verification
- Training for operations staff

**System Startup:**
- Individual equipment operational
- System-level startup procedures
- Verification of system sequences
- Interface testing between systems
- Alarm verification
- Load testing at system level
- Adjustment of setpoints

#### 11.3.5 Level 3 Testing

**Electrical System Testing:**
- Transformer energization and load testing
- Generator startup and load bank testing (up to rated capacity)
- ATS transfer testing (no-load transfers)
- UPS startup and load testing
- Switchgear energization and verification
- PDU testing and verification
- Breaker operation verification
- Power quality monitoring and recording
- EPMS verification (points, trending, alarming)

**Mechanical System Testing:**
- Chilled water plant startup and performance testing
- Pump startup and flow verification
- CRAH/CRAC startup and capacity testing
- Temperature and humidity control verification
- Airflow measurements and verification
- Test and balance (TAB) of air and water systems
- Control sequence verification
- BMS verification (points, trending, alarming)

**Control System Testing:**
- BMS/EPMS point verification (100% of points)
- Graphic verification
- Alarm verification and testing
- Trending verification
- Control sequence verification
- Setpoint verification
- Integration between systems verification

#### 11.3.6 Load Bank Testing - Level 3
- Individual equipment load tested to rated capacity
- Generator tested to 100% nameplate rating
- UPS tested to rated capacity on utility and generator
- Testing per manufacturer requirements
- Minimum [X] hours at full load
- Performance measurements recorded
- Thermal imaging during load test

#### 11.3.7 Test and Balance (TAB)
- Independent TAB contractor (or qualified vendor)
- Air and water system balancing
- Airflow measurements and adjustments
- Water flow measurements and adjustments
- Documentation per AABC or NEBB standards
- TAB report submitted and reviewed

#### 11.3.8 48-Hour Run Test
[If applicable - describe requirement for continuous run testing]

#### 11.3.9 Level 3 Documentation
- Startup reports (all equipment)
- Initial energization records
- Rotation verification
- Thermal imaging reports
- Load bank test reports
- Generator performance test results
- UPS performance test results
- ATS transfer test results
- Test and balance reports
- BMS/EPMS point verification reports
- Alarm verification reports
- Control sequence verification
- As-left equipment settings
- Training attendance records
- Vendor startup certifications

#### 11.3.10 Green Tag Criteria
Green Tag shall be applied when:
- Yellow Tag complete
- Equipment successfully energized without issues
- Vendor startup procedures complete
- Load testing complete and passed (where applicable)
- 48-hour run test complete and passed (if required)
- Test and balance complete (HVAC systems)
- Control system verification complete
- BMS/EPMS points verified
- Alarms verified operational
- All Level 3 documentation submitted
- No open Priority 1 or 2 issues
- Equipment operating in automatic mode
- Thermal imaging complete without issues

---

### 11.4 Level 4 – Functional Performance Testing (FPT)

#### 11.4.1 Level 4 Overview - BLUE TAG
Level 4 encompasses functional performance testing of all equipment under all modes of operation, including failure modes.

**Objective:** Verify systems function as designed under all normal and abnormal operating conditions.

**Tag Status:** BLUE TAG - "Ready for IST"

#### 11.4.2 Level 4 Responsibilities
- **Manage:** Commissioning Authority (CxA)
- **Execute:** CxA
- **Support:** GC, Vendors, Controls Vendors
- **Witness:** Owner, Customer (as desired)

#### 11.4.3 Level 4 Prerequisites (H2C Requirements)
[Reference Section 9 - Handover to Commissioning]

#### 11.4.4 Test Script Development

**Script Development Process:**
1. CxA develops draft test scripts
2. Scripts based on:
   - Sequence of Operations (SoO)
   - Design specifications
   - Manufacturer requirements
   - Industry standards
   - Owner requirements
   - Lessons learned from previous projects

3. Review and comment period:
   - Design team review
   - GC review
   - Vendor review
   - Owner/Customer review
   - Minimum [X] working days for review

4. Comments incorporated and script finalized
5. Final approval minimum [X] working days before testing

**Script Content:**
- Equipment/system identification
- Test prerequisites and setup requirements
- Test procedure step-by-step
- Expected results with acceptable tolerances
- Pass/fail criteria
- Data to be collected
- Monitoring points to observe
- Safety considerations
- Required support resources
- Estimated test duration

#### 11.4.5 Support Requirements During Level 4

**General Contractor:**
- Electrical switching per switching plans
- LOTO and isolation support
- Construction power for test equipment
- Internet connectivity
- Load bank installation and movement
- Fire watch (as required)
- Coordination of vendors and subcontractors

**Equipment Vendors:**
- Equipment operation as needed
- Equipment inspection support
- Technical expertise
- Issue resolution support

**Controls Vendors:**
- Access to control systems
- System monitoring support
- Trending and screenshots
- Programming support for issue resolution
- Simulation support (where possible)

#### 11.4.6 Testing Approach

**Equipment Level Testing:**
- Test each piece of equipment individually
- All operational modes tested
- Manual operation (where applicable)
- Automatic operation
- Maintenance mode
- All failure modes
- Alarm generation and annunciation
- Interface with monitoring systems
- Performance under load
- Capacity verification

**System Level Testing:**
- Equipment operating as integrated system
- System-level sequences verified
- Load sharing and staging
- Lead/lag operation
- System redundancy verification
- Failure response verification
- Recovery from failures
- Optimization sequences

#### 11.4.7 Test Execution Sequence

**Electrical Testing Sequence:**
1. Equipment settings verification
   - Protective relay settings vs. coordination study
   - Arc flash study verification
   - Equipment parameters vs. specifications

2. Alarm and EPMS verification
   - All alarm points tested
   - Alarm response verified
   - EPMS trending verified
   - Graphics verified

3. Medium voltage and generator systems
   - MV switchgear functional testing
   - Generator functional testing under load
   - ATS functional testing (loaded transfers)
   - Ring bus operation verification
   - Paralleling operation (if applicable)

4. UPS systems
   - UPS functional testing under load
   - UPS on utility power
   - UPS on generator power
   - Transfer testing (bypass, maintenance)
   - Battery autonomy verification
   - Power quality verification (ITIC/CBEMA compliance)

5. Low voltage distribution
   - LV switchgear functional testing
   - Distribution system verification
   - Busway system testing (if applicable)
   - PDU functional testing

6. Data hall power distribution
   - Branch circuit verification
   - Receptacle testing
   - PDU monitoring verification

**Mechanical Testing Sequence:**
1. BMS alarm verification
   - All alarm points tested
   - Alarm response verified
   - BMS trending verified
   - Graphics verified

2. Visual inspections and local testing
   - Equipment inspections
   - Local control verification
   - Safety verification

3. Chilled water system (if applicable)
   - Chiller functional testing
   - Pump operation and staging
   - Valve operation verification
   - Free cooling operation (if applicable)
   - System capacity verification

4. Cooling system functional testing
   - CRAH/CRAC functional testing under load
   - Capacity verification
   - Control verification (temperature, humidity)
   - Lead/lag and staging operation
   - Failure response and recovery

5. BMS system functionality
   - System-level sequences
   - Optimization sequences
   - Alarm response
   - Data trending and reporting

#### 11.4.8 Load Bank Strategy - Level 4
- Load banks placed per approved load bank plan
- Testing conducted in phases per test sequence
- Electrical systems typically tested first
- Mechanical systems tested with electrical systems operational
- Full facility load achieved during testing
- Load bank coordination meeting prior to testing

#### 11.4.9 Monitoring and Data Collection

**Power Quality Monitoring:**
- PQMs placed per approved PQM plan
- Monitoring during all major electrical tests
- Data collection for ITIC/CBEMA analysis
- Voltage, current, frequency, harmonics recorded
- Transfer events captured

**Environmental Monitoring:**
- Temperature and humidity data loggers
- Placement per approved monitoring plan
- Data collection during thermal load testing
- Verification of environmental stability

**System Monitoring:**
- BMS trending of all mechanical parameters
- EPMS trending of all electrical parameters
- Screenshots captured at key test points
- Baseline data established for operations

#### 11.4.10 Test Repetition Requirements
- Failed tests require investigation and correction
- Three (3) successful consecutive repetitions required after failure
- CxA determines scope of re-testing required
- Re-testing scheduled after issue resolution

#### 11.4.11 Pre-IST System Level Test
- Conducted after all equipment-level FPT complete
- Abbreviated IST to verify system readiness
- Internal verification before customer witnessing
- Identifies any final issues before formal IST

#### 11.4.12 Level 4 Documentation
- Functional performance test scripts (all equipment)
- Test execution records with results
- Power quality monitoring reports
- ITIC/CBEMA compliance analysis
- Environmental monitoring data
- Load bank test reports
- Thermal imaging reports (if conducted)
- BMS/EPMS screenshots and trend logs
- Issue Resolution Log
- Daily commissioning reports
- As-left settings record

#### 11.4.13 Blue Tag Criteria
Blue Tag shall be applied when:
- Green Tag complete
- All functional performance tests passed
- All operational modes tested successfully
- All failure modes tested successfully
- Performance verified under load
- System-level testing passed
- Pre-IST passed (if conducted)
- All Level 4 documentation submitted
- All Priority 1 and Priority 2 issues resolved
- Only minor punch-list items remain (Priority 3 or pushed to acceptance)
- Owner approval to proceed to Level 5

---

### 11.5 Level 5 – Integrated Systems Test (IST)

#### 11.5.1 Level 5 Overview - WHITE TAG
Level 5 encompasses integrated systems testing of the entire facility as a complete, operating system.

**Objective:** Verify the facility operates as designed with all systems working in coordination, including redundancy verification and fail-safe operations.

**Tag Status:** WHITE TAG - "Cx Complete"

#### 11.5.2 Level 5 Responsibilities
- **Manage:** Commissioning Authority (CxA)
- **Direct:** CxA
- **Execute:** CxA (hands-off test)
- **Support:** GC, Vendors, Controls Vendors
- **Witness:** Owner, Customer, Stakeholders

#### 11.5.3 IST Characteristics

**Hands-Off Testing:**
- Systems operate under automatic control
- No manual intervention unless part of designed sequence
- Demonstrates operational readiness
- Manual transfers may be accommodated per owner request
- Operator response scenarios included where specified

**Full Facility Testing:**
- Entire facility under full IT load
- All systems operating simultaneously
- All redundancy verified
- Complex failure scenarios tested
- Recovery and return to normal verified

#### 11.5.4 IST Planning and Coordination

**IST Planning Meetings:**
- Regular meetings during Level 4 to plan IST
- Test scenarios identified and agreed
- Test configuration defined
- Roles and responsibilities confirmed
- Schedule established

**IST Summary Plan:**
- Description of all test scenarios
- Load bank placement and configuration
- Test equipment requirements (PQMs, data loggers, etc.)
- Data collection methodology
- BMS/EPMS monitoring strategy
- Safety procedures
- Communication protocols
- Contingency plans

**IST Script Development:**
1. CxA develops draft IST scripts
2. Based on:
   - Level 4 test results
   - Redundancy architecture
   - Failure mode analysis
   - Owner requirements
   - Customer requirements
   - Industry best practices

3. Review and comment period:
   - Owner/Customer extensive review
   - Design team review
   - GC review
   - Vendor review
   - Minimum [X] working days for review

4. Comments incorporated
5. Final approval minimum [X] working days before IST
6. IST presentation to all stakeholders

#### 11.5.5 IST Prerequisites

**System Readiness:**
- All Blue Tags in place
- All Level 4 testing complete
- Pre-IST passed successfully
- No open critical issues
- All systems in automatic mode
- Monitoring systems verified and ready

**Infrastructure Readiness:**
- Load banks in place per IST plan
- PQMs in place per monitoring plan
- Data loggers in place per monitoring plan
- Safety systems verified
- Communication systems tested
- Emergency procedures reviewed

**Personnel Readiness:**
- Contractor and vendor support confirmed
- Operator training complete
- CxA team briefed
- Owner/Customer attendance confirmed
- Roles and responsibilities understood

**Documentation Readiness:**
- IST scripts finalized and approved
- Data collection forms prepared
- Safety procedures documented
- Emergency contact list current
- Issue log ready for use

#### 11.5.6 IST Test Structure

**Typical IST Duration:**
- [X] days total
- Stage 1: Thermal ramp and electrical failures
- Stage 2: Mechanical system failures
- Daily testing schedule with breaks for review

**Stage 1 – Thermal Ramp & Electrical System Testing:**

*Thermal Ramp:*
- Stepwise increase of thermal load to 100% in data halls
- Verification of cooling system response
- Temperature and humidity stability verification
- Capacity verification at each load step
- Typical steps: 25%, 50%, 75%, 100%

*Electrical System Failure Testing:*
- Utility failure (transfer to generator)
- Generator failures with redundancy verification
- ATS failure scenarios
- UPS failures and bypass operations
- Parallel operation verification
- Bus transfer operations
- Multiple concurrent failures
- Recovery and restoration
- Power quality verification during all events

*Integrated Response:*
- Mechanical system response to electrical failures
- Cooling maintained during power transitions
- BMS/EPMS integration verified
- Alarms and notifications verified

**Stage 2 – Mechanical System Failure Testing:**

*Environmental Stability:*
- 100% thermal load maintained
- Cooling system at full operation
- Baseline stability demonstrated

*Mechanical Failures:*
- Individual CRAH/CRAC failures
- Multiple CRAH/CRAC failures
- Cooling redundancy verification (N+1, 2N, etc.)
- Chilled water system failures (if applicable)
- Pump failures
- Cooling tower/condenser failures (if applicable)
- Control system failures

*Verification:*
- Temperature and humidity stability maintained
- Recovery time within specifications
- Redundancy level demonstrated
- No single point of failure
- Return to normal operations verified

#### 11.5.7 Data Collection During IST

**Power Quality:**
- Continuous PQM monitoring
- Capture all transfer events
- Voltage, current, frequency recorded
- Harmonics analysis
- ITIC/CBEMA compliance verification
- Waveform captures of key events

**Environmental:**
- Continuous temperature and humidity monitoring
- Multiple locations per data hall
- Equipment inlet temperatures
- Room averages
- Maximum deviations recorded
- Recovery time measurements

**System Performance:**
- BMS trending of all key mechanical points
- EPMS trending of all key electrical points
- Equipment operating parameters
- System responses to failures
- Alarm sequences
- Return to normal sequences

**Photographic/Video:**
- Key test events photographed
- Control system screenshots
- Monitoring displays captured
- Video recording of critical sequences (optional)

#### 11.5.8 IST Testing Scenarios

**Typical Test Scenarios Include:**
1. Utility power failure (normal to generator transfer)
2. Return to utility (generator to normal transfer)
3. Generator failure (load transfer to remaining generators)
4. Generator maintenance mode operation
5. UPS failure and bypass transfer
6. UPS return from bypass
7. Multiple concurrent UPS failures
8. CRAH/CRAC failures (single and multiple)
9. Chilled water system failures (if applicable)
10. BMS/EPMS control system failures
11. Network communication failures
12. Multiple concurrent system failures
13. Recovery sequences for all failures

[Client/customer specific scenarios added as required]

#### 11.5.9 Daily IST Process

**Morning Meeting:**
- Review previous day results
- Discuss any issues or concerns
- Review day's test schedule
- Confirm roles and responsibilities
- Confirm system ready for testing
- Safety briefing

**Test Execution:**
- Execute per approved test scripts
- Real-time data collection
- Issue identification and documentation
- Verification of pass/fail criteria
- Adjustments as needed
- Safety monitoring

**End-of-Day Review:**
- Review day's test results
- Discuss any issues identified
- Plan for next day
- Update issue log
- Document preliminary findings

#### 11.5.10 Issue Management During IST
- Issues documented in real-time
- Priority assessment immediate
- Critical issues may pause testing
- Resolution coordinated with GC and vendors
- Verification of fixes before continuing
- Re-testing as required

#### 11.5.11 Post-IST Activities

**Final Facility Inspection:**
- CxA conducts walkthrough of entire facility
- Verify all equipment in correct operating state
- Verify no alarms present (or justified)
- Verify all systems in automatic mode
- Document final conditions

**Data Analysis:**
- Power quality data analysis
- Environmental data analysis
- System performance analysis
- ITIC/CBEMA compliance report
- Comparison to acceptance criteria

**IST Report:**
- Executive summary
- Test procedures and scenarios
- Results for each test
- Pass/fail assessment
- Data analysis
- Issues identified and resolved
- Outstanding issues (if any)
- Photographic documentation
- Recommendations

#### 11.5.12 Level 5 Documentation
- IST test scripts with results
- IST summary report
- Power quality monitoring report
- ITIC/CBEMA compliance analysis
- Environmental monitoring report
- BMS/EPMS trend logs
- Control system screenshots
- Photographic documentation
- Video recordings (if applicable)
- Final facility inspection report
- Issue Resolution Log final status
- Daily IST reports

#### 11.5.13 White Tag Criteria
White Tag shall be applied when:
- Blue Tag complete
- All IST scenarios executed successfully
- All systems demonstrated redundancy level
- No single points of failure identified
- Environmental stability maintained
- Power quality verified (ITIC/CBEMA compliant)
- All systems operate in automatic mode
- Final facility inspection passed
- All critical issues resolved
- IST report approved by owner
- Facility ready for operational handover

#### 11.5.14 Substantial Completion
Successful completion of Level 5 IST typically triggers:
- Substantial completion milestone
- Contractual payment milestone
- Transition to operational readiness phase
- Warranty period commencement
- [Other contractual obligations as defined]

---

### 11.6 Level 6 – Acceptance & Handover

#### 11.6.1 Level 6 Overview
Level 6 encompasses final documentation, training verification, and formal handover to operations.

**Objective:** Complete all commissioning documentation and deliverables, verify training completion, and formally hand over facility to owner.

#### 11.6.2 Final Commissioning Report

**Report Structure:**
1. **Executive Summary**
   - Project overview
   - Commissioning scope
   - Key findings
   - Overall assessment
   - Recommendations

2. **Project Information**
   - Participants and roles
   - Facility description
   - Systems commissioned
   - Commissioning schedule summary

3. **Commissioning Process Overview**
   - Testing and verification methods
   - Quality control processes
   - Deviations from standard process (if any)

4. **Equipment List**
   - Complete list of commissioned equipment
   - Equipment status (commissioned, tested, accepted)
   - Tag numbers and locations

5. **Testing Results Summary**
   - Level 1-5 completion status
   - Performance verification results
   - Capacity verification results
   - Acceptance criteria compliance

6. **As-Left Settings**
   - Electrical system settings
   - Mechanical system settings
   - Control system setpoints
   - Alarm setpoints
   - Baseline operational parameters

7. **Test Documentation**
   - Links to all test scripts and results
   - Factory test reports
   - Startup reports
   - Functional performance test results
   - Integrated systems test results
   - Power quality monitoring results
   - Environmental monitoring results

8. **Specialized Testing Results**
   - Electrical coordination/arc flash study (signed & stamped)
   - Primary/secondary injection testing
   - Thermal imaging results
   - ITIC/CBEMA compliance report
   - Test and balance reports
   - Calibration certificates

9. **Issues and Resolutions**
   - Summary of issues encountered
   - Resolution methods
   - Outstanding issues (if any)
   - Recommended future actions

10. **Training Summary**
    - Training sessions conducted
    - Attendance records
    - Training materials provided

11. **Recommendations**
    - Operational recommendations
    - Maintenance recommendations
    - Future commissioning activities
    - System optimization opportunities

12. **Appendices**
    - Detailed test results
    - BMS/EPMS screenshots
    - Power quality data
    - Environmental monitoring data
    - Photographic documentation
    - Equipment manuals references
    - Warranty information

#### 11.6.3 Operations and Maintenance (O&M) Manual Review

**O&M Development Process:**
1. O&M developed by GC and supply chain
2. Data collected via document management platform
3. Cx documents exported from commissioning platform
4. First Draft issued at substantial completion
   - Includes all L1-L3 commissioning documents
   - Submitted for review by CxA, Owner, Design Team
   - Comments compiled and addressed

5. Second Draft issued after IST completion
   - Includes all L4-L5 commissioning documents
   - Updated with as-built information
   - Submitted for final review
   - Comments addressed

6. Final Issue
   - Complete O&M manual
   - Hard copy and electronic versions
   - Issued within [X] business days after successful IST

**O&M Manual Contents:**
- Equipment manuals and documentation
- Warranty information
- As-built drawings
- Control sequences and narratives
- Setpoint schedules
- Preventive maintenance schedules
- Troubleshooting guides
- Parts lists and spare parts recommendations
- Emergency procedures
- Training materials
- Commissioning reports and test results
- As-left settings documentation

**CxA O&M Review:**
- Cross-check hard copy and electronic versions
- Verify completeness
- Verify accuracy of as-built information
- Verify inclusion of all commissioning documentation
- Final approval

#### 11.6.4 Training Verification
- Training plan executed per contract requirements
- Training attendance documented
- Training materials included in O&M manual
- Operator competency assessed
- Additional training needs identified

#### 11.6.5 Systems Manual
Comprehensive systems manual provided including:
- System descriptions and functions
- Operating procedures (normal and emergency)
- Maintenance procedures
- Troubleshooting guides
- Safety procedures
- Emergency contact information
- Vendor contact information
- Spare parts information

#### 11.6.6 Final Documentation Deliverables
- Final Commissioning Report
- O&M Manuals (hard copy and electronic)
- Systems Manual
- As-built drawings (electronic)
- Test and balance reports
- Electrical coordination/arc flash study (final, signed, stamped)
- Control sequences (final as-built)
- Training documentation
- Warranty documentation
- Certificate of Substantial Completion
- [Other contractual deliverables]

#### 11.6.7 Final Acceptance
- Final walkthrough and inspection
- Punch list review and completion
- Documentation review and acceptance
- Training completion verification
- Final payment processing
- Certificate of Occupancy (if applicable)
- Formal handover to operations

#### 11.6.8 Transition to Operations
- Operations team assumes responsibility
- Ongoing commissioning plan initiated (if applicable)
- Warranty period begins
- Preventive maintenance program begins
- CxA support during transition period (as contracted)

---

## 12. DOCUMENT STORAGE & RESPONSIBILITY

### 12.1 Document Repository
All project documents shall be stored in a centralized, cloud-based document management system accessible to all project stakeholders.

**Primary Platform:** [Platform Name - e.g., Asite, Procore, SharePoint, etc.]

### 12.2 Document Categories

**Design Documents:**
- Responsibility: Design Team/GC
- Basis of Design (BOD)
- Owner's Project Requirements (OPR)
- Design drawings (all disciplines)
- Technical specifications
- Design calculations
- Design review comments and responses
- RFIs and responses
- Change orders
- Addenda

**Submittals:**
- Responsibility: GC
- Equipment submittals
- Shop drawings
- Product data sheets
- Samples
- Coordination drawings
- Submittal review comments
- Approved submittals

**Commissioning Documents (Levels 1-3):**
- Responsibility: GC (execution), CxA (review)
- Storage Platform: Commissioning Platform
- Factory test reports
- Delivery inspection records
- Installation verification checklists
- Pre-startup inspection records
- Startup reports
- Load test reports
- Test and balance reports
- Vendor commissioning reports
- Supporting certifications and calibrations

**Commissioning Documents (Levels 4-5):**
- Responsibility: CxA
- Storage Platform: Commissioning Platform
- Functional performance test scripts and results
- Integrated systems test scripts and results
- Power quality monitoring reports
- Environmental monitoring data
- Daily commissioning reports
- Issue Resolution Log
- As-left settings documentation

**Control System Documentation:**
- Responsibility: Controls Vendor/GC
- Sequence of operations (final as-built)
- Control diagrams and schematics
- Points lists
- BMS/EPMS graphics
- Programming documentation
- Network architecture
- Alarm setpoints
- User manuals

**Operations Documentation:**
- Responsibility: GC (compilation), All Vendors (content)
- Equipment O&M manuals
- Systems manuals
- Training materials
- Preventive maintenance schedules
- Standard operating procedures
- Emergency procedures
- Spare parts lists

### 12.3 Document Control Procedures

**Version Control:**
- All documents shall be version controlled
- Revision history maintained
- Superseded versions archived (not deleted)
- Current version clearly identified

**Access Control:**
- Role-based access permissions
- Read/write permissions assigned appropriately
- Audit trail of document access and changes

**Document Review Workflow:**
- Formal review and approval workflow
- Comment tracking and resolution
- Approval signatures captured electronically
- Status tracking (draft, in review, approved, superseded)

### 12.4 Document Naming Conventions
[Specify project-specific document naming convention]

Example format:
`[Project Code]-[Discipline]-[Document Type]-[Number]-[Revision]`

### 12.5 Commissioning Platform Integration
- Commissioning platform shall link documents to specific equipment assets
- Supporting documents uploaded for each commissioning tag level
- Documents accessible via equipment tag number
- Export capability for archival purposes

### 12.6 Final Archival
- Complete project documentation archived at project completion
- Owner provided with complete electronic copy
- Backup archive maintained by CxA for [X] years
- Document retention per contractual requirements

---

## 13. LOAD BANK AND MONITORING PLAN

### 13.1 Purpose
The Load Bank and Monitoring Plan establishes the strategy for load testing and performance monitoring throughout commissioning Levels 3, 4, and 5.

### 13.2 Load Bank Plan Development

**Level 3 Load Bank Plan:**
- Responsibility: GC and commissioning team
- Review: CxA
- Purpose: Individual equipment load testing
- Load bank placement for:
  - Generator testing (100% nameplate capacity)
  - UPS testing (rated capacity)
  - Individual system testing

**Level 4 & 5 Load Bank Plan:**
- Responsibility: CxA
- Review: GC, Owner, Customer
- Purpose: Facility-level testing and IST
- Comprehensive plan addressing:
  - Full facility load requirements
  - Data hall load distribution
  - Connection points and power requirements
  - Load bank quantities and specifications
  - Safety considerations
  - Fire watch requirements
  - Movement and logistics

### 13.3 Load Bank Plan Contents

**Load Bank Specifications:**
- Total load capacity required: [XX MW]
- Load bank types and ratings
- Resistive vs. reactive load requirements
- Control capabilities (local, remote)
- Monitoring capabilities
- Safety features

**Load Bank Placement:**
- Data hall load distribution strategy
- Connection point locations (PDUs, busway, etc.)
- Power requirements at each location
- Cable routing and management
- Ventilation requirements
- Fire safety considerations

**Load Bank Connection Strategy:**
- Connection sequence and procedure
- Electrical connection details
- Safety procedures and LOTO
- Pre-connection verification checklist
- Disconnection procedures

**Load Testing Strategy:**
- Testing sequence for different commissioning levels
- Load increments and staging
- Test durations at each load level
- Coordination with cooling systems
- Coordination with power systems
- Data collection requirements

**Load Bank Logistics:**
- Delivery schedule
- Storage locations
- Movement procedures
- Equipment required for movement (forklifts, etc.)
- Labor requirements
- Return/removal schedule

**Safety Procedures:**
- Fire watch requirements
- Ventilation requirements
- Personnel safety (heat exposure)
- Electrical safety (connection/disconnection)
- Emergency procedures
- Site access control during testing

### 13.4 Power Quality Monitoring Plan

**Purpose:**
Establish monitoring strategy to verify:
- ITIC/CBEMA compliance
- Power quality during all operational scenarios
- Transfer event characteristics
- Harmonic distortion levels
- Voltage regulation

**PQM Placement Locations:**
- Utility service entrance
- Generator output
- ATS output
- UPS input
- UPS output
- Critical distribution points
- Data hall power distribution
- [Other strategic locations]

**PQM Configuration:**
- Monitoring parameters:
  - Voltage (RMS and waveform)
  - Current (RMS and waveform)
  - Frequency
  - Power factor
  - Total harmonic distortion (THD)
  - Individual harmonics
  - Transients and sags/swells
- Recording triggers:
  - Continuous recording
  - Event-based triggers
  - Manual triggers for specific tests
- Data storage and retrieval

**Data Collection Events:**
- All electrical commissioning tests
- Generator transfers
- UPS transfers
- Load step changes
- Failure mode testing
- Integrated systems test
- Recovery sequences

**Data Analysis:**
- ITIC/CBEMA curve compliance analysis
- Transfer time measurements
- Voltage deviation analysis
- Frequency deviation analysis
- Harmonic analysis
- Power quality report generation

### 13.5 Environmental Monitoring Plan

**Purpose:**
Verify environmental stability and cooling system performance during thermal load testing.

**Data Logger Placement:**
- Multiple locations per data hall:
  - Hot aisle locations
  - Cold aisle locations
  - Equipment inlet points
  - Return air locations
  - Room average reference points
- Cooling equipment locations:
  - CRAH/CRAC inlet/outlet
  - Supply air temperatures
  - Return air temperatures

**Monitoring Parameters:**
- Temperature
- Relative humidity
- Dew point
- Air pressure differential (if applicable)

**Data Collection Frequency:**
- Recording interval: [X] seconds/minutes
- Continuous recording during:
  - Level 3 thermal testing
  - Level 4 thermal testing
  - Level 5 IST thermal ramp
  - All mechanical failure testing

**Data Analysis:**
- Temperature stability verification
- Humidity stability verification
- Maximum temperature deviation
- Temperature recovery time
- Spatial temperature distribution
- Equipment inlet temperature compliance
- Room average compliance
- Environmental stability report

### 13.6 Load Bank and Monitoring Meeting
Prior to commencing load bank testing:
- Review load bank plan with all stakeholders
- Confirm load bank specifications and quantities
- Review placement and connection strategy
- Review safety procedures
- Confirm PQM and data logger placement
- Review data collection procedures
- Confirm roles and responsibilities
- Establish communication protocols

### 13.7 Load Bank and Monitoring Plan Documentation
- Load bank plan document with diagrams
- Load bank connection procedures
- PQM placement plan with diagram
- Data logger placement plan with diagram
- Data collection procedures
- Safety procedures
- Equipment specifications sheets

---

## 14. FIRMWARE & SOFTWARE CHANGE MANAGEMENT

### 14.1 Change Control Policy
All firmware and software changes during the commissioning process shall be managed through a formal change control procedure to ensure:
- Commissioning integrity is maintained
- Changes are documented and traceable
- Impact on testing is assessed
- Re-testing requirements are determined
- All stakeholders are informed

### 14.2 Equipment Firmware Changes

**Baseline Version:**
- Firmware version at Factory Acceptance Test (FAT/FWT) establishes baseline
- Baseline version should remain unchanged throughout commissioning
- Any proposed changes require formal change request

**Change Request Process:**
1. **Identification**
   - Issue identified requiring firmware update
   - Vendor proposes firmware change
   - Change request submitted to CxA

2. **Documentation**
   - Current firmware version
   - Proposed firmware version
   - Reason for change (bug fix, performance improvement, security patch)
   - Release notes detailing changes
   - Impact assessment on commissioned status
   - Affected equipment list

3. **Review**
   - CxA reviews change request
   - Owner/Customer notified
   - GC and relevant vendors consulted
   - Impact on commissioning schedule assessed

4. **Approval**
   - CxA determines re-testing requirements
   - Owner approval required for implementation
   - Implementation schedule established
   - Communication to all stakeholders

5. **Implementation**
   - Change implemented per approved procedure
   - Verification of successful update
   - Testing per CxA requirements
   - Documentation of new firmware version

6. **Verification**
   - Re-testing as determined by CxA
   - Verification of issue resolution
   - Confirmation no new issues introduced
   - Update of as-built documentation

### 14.3 BMS/EPMS Operating System and Software Changes

**Baseline Version:**
- Control system software version at H2C (Handover to Commissioning) establishes baseline
- Major software changes should be avoided after H2C
- Any changes require formal change request

**Change Request Process:**
[Same process as Equipment Firmware Changes above]

**Specific Considerations for Control Systems:**
- Impact on graphics and user interface
- Impact on point mappings
- Impact on trending and alarming
- Impact on integrations with other systems
- Database integrity verification
- Backup of current system before change
- Rollback plan if issues occur

### 14.4 Re-Testing Requirements

**CxA Determination:**
The CxA shall determine re-testing requirements based on:
- Scope of firmware/software changes
- Systems affected
- Control sequences affected
- Previous test results validity
- Risk to facility operations

**Potential Re-Testing:**
- Functional performance tests (partial or complete)
- Control sequence verification
- Alarm verification
- Integration testing
- Portions of IST (if after IST completion)

### 14.5 Emergency Changes
In the event of critical issues requiring immediate firmware/software changes:
- Document issue and urgency
- Verbal notification to CxA and Owner
- Implement change to resolve critical issue
- Follow formal change request process retroactively
- Conduct required re-testing as soon as possible

### 14.6 Post-Handover Changes
After facility handover:
- Owner assumes responsibility for firmware/software change management
- Vendor support may be engaged
- Ongoing commissioning process addresses changes (if implemented)
- Previous commissioning documentation updated as required

### 14.7 Documentation
All firmware/software changes shall be documented:
- Change request form
- Approval documentation
- Release notes and change logs
- Re-testing results
- Updated as-built documentation
- Version control record

---

## 15. ADDITIONAL TESTING

### 15.1 Purpose
This section addresses testing requirements beyond the standard commissioning scope that may be requested by the Owner, regulatory authorities, or identified as needed during the commissioning process.

### 15.2 Additional Testing Request Process

**Request Initiation:**
- Additional testing request submitted to CxA Project Manager
- Request includes:
  - Description of testing required
  - Objective and acceptance criteria
  - Systems/equipment involved
  - Regulatory requirement or business justification
  - Desired schedule

**CxA Review:**
- Technical feasibility assessment
- Resource requirements (personnel, equipment, time)
- Impact on commissioning schedule
- Safety considerations
- Required support from GC, vendors, or others

**Planning:**
- Test procedure development
- Monitoring requirements identified
- Data collection methodology established
- Success criteria defined
- Safety procedures developed

**Approval:**
- Test procedure reviewed by stakeholders
- Owner approval to proceed
- Schedule integration
- Budget impact assessed (if change order required)

**Execution:**
- Testing conducted per approved procedure
- Data collected and documented
- Results analyzed
- Report generated

### 15.3 Types of Additional Testing

**Examples may include:**
- Extended duration run tests
- Seismic qualification testing
- Acoustic testing
- Specific regulatory compliance testing
- Third-party witness testing
- Customer-specific acceptance criteria
- Environmental impact testing
- Specialized power quality testing
- Redundancy verification beyond standard scope

### 15.4 Documentation
- Additional test procedures
- Test execution records
- Test results and analysis
- Certification (if applicable)
- Incorporation into final commissioning report

---

## 16. PROJECT CLOSEOUT

### 16.1 Closeout Activities

The CxA shall support the Owner and project team in administrative closeout of the commissioning project to ensure all deliverables are completed in an acceptable and timely manner.

**Target Timeline:** Within [30] days post-IST completion

### 16.2 Final Documentation Compilation

**Commissioning Documentation:**
- Final Commissioning Report
- All test scripts and results (L1-L5)
- Issue Resolution Log (final)
- As-left settings documentation
- Power quality monitoring reports
- Environmental monitoring reports
- Training documentation
- Lessons learned documentation

**Supporting Documentation:**
- Factory test reports
- Startup reports
- Test and balance reports
- Electrical testing reports (primary/secondary injection, etc.)
- Arc flash/coordination study (final, signed, stamped)
- Thermal imaging reports
- Calibration certificates
- Warranties and certifications

**O&M Documentation:**
- Operations and Maintenance Manuals (final)
- Systems Manuals
- As-built drawings (electronic)
- Control sequences (final)
- Equipment manuals
- Preventive maintenance schedules
- Training materials

### 16.3 Documentation Review and Acceptance

**Owner Review:**
- Owner reviews all documentation for completeness
- Comments or deficiencies identified
- CxA addresses comments
- Final acceptance documented

**Documentation Delivery:**
- Electronic copies of all documents
- Hard copies as specified in contract
- Organized per agreed structure
- Searchable PDF format
- Indexed for easy reference

### 16.4 Final Acceptance Walkthrough
- Final facility inspection
- Verification of all systems operational
- Verification of no outstanding critical issues
- Punch list review and status
- Acceptance documentation signed

### 16.5 Knowledge Transfer
- Final training sessions (if required)
- Operator questions addressed
- System optimization recommendations provided
- Ongoing commissioning recommendations (if applicable)

### 16.6 Financial Closeout
- Final invoicing
- Lien releases
- Warranty documentation
- Closeout of any retainage

### 16.7 Transition to Operations
- Formal handover to operations team
- Ongoing commissioning plan initiated (if contracted)
- CxA support period defined (if applicable)
- Escalation procedures for issues
- Vendor contact information provided

### 16.8 Project Archival
- Complete project documentation archived
- Retention period defined
- Backup copies maintained
- Access procedures established for future reference

---

## 17. COMMISSIONING SCHEDULE

### 17.1 Schedule Development

**Responsibility:**
- **Levels 1-3:** GC develops detailed schedule
- **Levels 4-5:** CxA develops schedule, GC incorporates into master schedule
- **Coordination:** Joint development and regular updates

**Schedule Characteristics:**
- Living document, updated throughout project
- Integrated with construction schedule
- Includes all commissioning milestones and activities
- Shows dependencies and critical path
- Resource loaded (personnel requirements)

### 17.2 Key Milestones

**For Each Major Commissioning Asset:**
- **Red Tag (Level 1)**
  - Factory testing complete
  - Equipment delivery
  - Installation complete
  - Documentation review and approval

- **Yellow Tag (Level 2)**
  - QA/QC inspections complete
  - Pre-startup procedures complete
  - Equipment ready for energization

- **Green Tag (Level 3)**
  - Equipment energized
  - Startup and commissioning complete
  - Load bank testing complete (where applicable)
  - EPMS/BMS SAT complete
  - Thermographic inspections complete

- **Blue Tag (Level 4)**
  - Functional performance testing complete
  - All operational modes verified

- **White Tag (Level 5)**
  - Integrated systems testing complete
  - Facility acceptance

### 17.3 Schedule Durations and Lead Times

**Review Periods:**
- Level 1-3 test script review: Minimum [10] working days
- Level 4 test script review: Minimum [10] working days
- Level 5 IST script review: Minimum [5] working days
- Level 5 IST script final approval: Minimum [5] working days before IST

**Testing Durations:**
- Pre-IST: Minimum [2] days
- IST: Minimum [1] week (facility dependent)
- Load bank mobilization and setup: [X] days
- [Other key activity durations]

**Phased Approach:**
- Construction completed in phases to enable commissioning
- Level 4 testing of early phases while construction continues
- All phases complete before Level 5 IST
- Coordination between construction and commissioning activities

### 17.4 Schedule Coordination and Review

**Initial Schedule Development:**
1. CxA meets with project team to review commissioning requirements
2. Initial commissioning schedule developed and incorporated into construction documents
3. Schedule lists equipment and milestones required for each commissioning level
4. Team reviews and agrees on baseline schedule

**Ongoing Schedule Management:**
- Regular review at commissioning meetings
- Updates based on progress and changes
- Variance analysis (planned vs. actual)
- Look-ahead planning
- Critical path monitoring
- Resource leveling

**Schedule Reporting:**
- 2-week look-ahead schedule minimum
- Planned vs. actual tag dates tracked
- Run rate analysis
- Slippage identification and mitigation
- Regular schedule updates to stakeholders

### 17.5 Load Bank Schedule
- Load bank procurement and delivery schedule
- Mobilization and installation schedule
- Testing schedule by system and level
- Demobilization schedule
- Coordination with facility testing sequence

### 17.6 Critical Dependencies
- Design completion and approvals
- Long-lead equipment delivery
- Construction substantial completion
- Utility service availability
- Personnel availability (vendors, specialists)
- Load bank availability
- Testing equipment availability

### 17.7 Schedule Contingencies
- Float analysis
- Risk assessment
- Mitigation strategies
- Weather delays (if applicable)
- Issue resolution time allowances

---

## 18. REPORTING & FORECASTING

### 18.1 Weekly Commissioning Reports (Levels 1-3)

**Frequency:** Weekly during construction and Levels 1-3 commissioning

**Distribution:** Owner, Customer, GC, CxA, Key Stakeholders

**Platform:** Uploaded to document management platform

**Report Contents:**
1. **Executive Summary**
   - Overall project status
   - Key accomplishments this week
   - Key activities planned for next week
   - Critical issues or concerns

2. **Weekly Activities**
   - Commissioning activities completed
   - Tests witnessed
   - Site visits conducted
   - Meetings attended

3. **Project Resources**
   - CxA personnel on site
   - Planned resource allocation
   - Vendor/contractor activities

4. **Deliverable Status**
   - CxA deliverable tracker
   - Upcoming deliverable due dates
   - Submitted documents pending review

5. **Tagging Status**
   - Red Tag status (count and percentage)
   - Yellow Tag status (count and percentage)
   - Green Tag status (count and percentage)
   - Progress charts/graphs
   - Comparison to baseline schedule

6. **Risk Register**
   - Current risks identified
   - Risk mitigation actions
   - Risk status (open, mitigated, closed)

7. **Issue Resolution Log Summary**
   - New issues this week
   - Issues resolved this week
   - Open issue count by priority
   - Aging issues requiring attention
   - Top priority issues

8. **Factory Acceptance Test (FAT) Tracker**
   - FATs scheduled
   - FATs completed
   - FAT results summary
   - Upcoming FATs

9. **Document Status Tracker**
   - Documents received
   - Documents under review
   - Documents requiring resubmission
   - Outstanding document requests

10. **RFI Summary** (if applicable)
    - RFIs submitted
    - RFIs answered
    - Open RFIs
    - RFI impact on commissioning

11. **Look-Ahead Program**
    - 2-week detailed look-ahead
    - Key activities and milestones
    - Resource requirements
    - Coordination requirements

### 18.2 Daily Commissioning Reports (Levels 4-5)

**Frequency:** Daily during active Level 4 and Level 5 testing

**Distribution:** Owner, Customer, GC, CxA, Active Vendors/Contractors

**Platform:** Uploaded to document management platform

**Report Contents:**
1. **Daily Summary**
   - Date and weather conditions (if applicable)
   - Personnel on site
   - Overall status (on schedule, delayed, etc.)

2. **Testing Activities**
   - Systems/equipment tested
   - Tests completed
   - Test results summary (pass/fail)
   - Tests in progress

3. **Issues**
   - New issues identified
   - Issue descriptions and priorities
   - Issues resolved
   - Issues pending resolution
   - Impact on schedule

4. **Data Collection**
   - Monitoring activities
   - Data collected
   - Preliminary findings

5. **Tomorrow's Plan**
   - Planned testing activities
   - Required support
   - Critical path items

6. **Safety**
   - Safety incidents (if any)
   - Safety observations
   - Corrective actions

### 18.3 Two-Week Look-Ahead and Planned vs. Actual

**Responsibility:**
- Levels 1-3: GC and commissioning team
- Levels 4-5: CxA

**Purpose:**
- Detailed short-term planning
- Resource coordination
- Progress measurement
- Early identification of delays

**Look-Ahead Contents:**
- Equipment/systems scheduled for commissioning
- Specific activities and tests
- Planned tag dates (Red, Yellow, Green, Blue, White)
- Resource requirements
- Dependencies
- Risk factors

**Planned vs. Actual Tracking:**
- Planned tag date for each equipment/system
- Actual tag date achieved
- Variance (days early/late)
- Run rate calculation
- Trend analysis
- Mitigation actions for delays

**Progress Measurement:**
- Percentage complete by tag level
- Percentage complete overall
- Planned progress vs. actual progress
- Forecast completion dates
- Schedule variance

### 18.4 Monthly Executive Reports (If Required)
- High-level summary for executive stakeholders
- Major accomplishments
- Schedule status
- Budget status (if applicable)
- Key issues and risks
- Upcoming milestones
- Forecast to completion

### 18.5 Forecasting
- Regular updates to completion forecast
- Based on run rate and progress
- Consideration of known risks and issues
- Resource availability
- Weather impacts (if applicable)
- Scenario analysis (best case, likely case, worst case)

---

## 19. MEETINGS

### 19.1 Commissioning Kickoff Meeting

**Timing:** Early in project, during design or early construction

**Participants:** Owner, Customer, GC, CxA, Design Team, Key Vendors

**Purpose:**
- Introduce commissioning team and process
- Review commissioning plan
- Clarify roles and responsibilities
- Review schedule and milestones
- Discuss Owner's Project Requirements
- Address questions and concerns

**Agenda:**
- Introductions
- Commissioning process overview
- Commissioning plan review
- Roles and responsibilities
- Schedule and milestones
- Communication protocols
- Documentation requirements
- Action items and next steps

### 19.2 Design Review Meetings (Level 0)

**Frequency:** As needed during design phase

**Participants:** CxA, Design Team, Owner, GC (if onboard)

**Purpose:**
- Review design documents for commissionability
- Identify potential single points of failure
- Review sequences of operation
- Verify alignment with OPR and BOD
- Address design coordination issues

### 19.3 Weekly Progress Meetings (Levels 1-3)

**Frequency:** Weekly during construction and Levels 1-3

**Participants:** GC, CxA, Vendors (as needed), Owner (as desired)

**Format:** On-site or virtual (e.g., Microsoft Teams)

**Purpose:**
- Review weekly progress
- Discuss commissioning activities completed and planned
- Review Issue Resolution Log
- Address coordination issues
- Review schedule and forecast
- Discuss risks and mitigation
- Plan upcoming activities

**Agenda:**
- Review of previous meeting action items
- Progress update by commissioning level
- Issue Resolution Log review
- Schedule review and look-ahead
- Risk and concern discussion
- Vendor/contractor updates
- Action items and responsibilities

### 19.4 Daily Level 4 Commissioning Meetings

**Frequency:** Daily during Level 4 testing

**Participants:** CxA, GC, Vendors/Contractors (as needed), Owner (as desired)

**Format:** On-site

**Purpose:**
- Review previous day's testing results
- Discuss issues identified and resolution status
- Review day's testing plan
- Coordinate resources and support
- Address safety considerations
- Adjust schedule as needed

**Agenda:**
- Previous day's results summary
- Issue Resolution Log review
- Priority issues requiring immediate attention
- Today's testing plan
- Resource and support confirmation
- Safety briefing
- Schedule update

**Timing:** Morning meeting before testing begins

### 19.5 Daily Level 5 IST Meetings

**Frequency:** Daily during IST

**Participants:** CxA, GC, Vendors/Contractors, Owner, Customer, Stakeholders

**Format:** On-site

**Purpose:**
- Review previous day's IST results
- Discuss any issues or concerns
- Review day's IST test plan
- Confirm all systems ready for testing
- Coordinate resources
- Safety briefing
- Address any questions

**Agenda:**
- Previous day's IST summary
- Test results review
- Issue discussion
- Today's IST schedule and scenarios
- System readiness confirmation
- Roles and responsibilities review
- Safety briefing
- Q&A

**Timing:** Morning meeting before IST execution

### 19.6 Weekly Remote Status Meetings (During Level 4)

**Frequency:** Weekly during Level 4 (in addition to daily on-site meetings)

**Participants:** CxA, Owner, Customer (if remote), GC, Key Stakeholders

**Format:** Virtual (e.g., Microsoft Teams)

**Purpose:**
- Provide status updates to remote stakeholders
- Review weekly progress
- Discuss major accomplishments
- Address concerns or issues
- Review forecast and schedule

### 19.7 H2C (Handover to Commissioning) Meeting

**Timing:** Prior to commencing Level 4 activities

**Participants:** CxA, GC, Vendors, Owner, Customer

**Purpose:**
- Review H2C prerequisite tracker
- Confirm system readiness for Level 4
- Review Level 4 test schedule
- Confirm resource availability and roles
- Review open issues
- Approve transition to Level 4

### 19.8 Pre-IST Planning Meetings

**Frequency:** Regular meetings during Level 4 to plan IST

**Participants:** CxA, GC, Vendors, Owner, Customer

**Purpose:**
- Develop IST test scenarios
- Define test configuration
- Review load bank and monitoring plans
- Establish roles and responsibilities
- Review safety procedures
- Coordinate logistics

### 19.9 IST Presentation Meeting

**Timing:** Prior to IST execution (after script approval)

**Participants:** CxA, Owner, Customer, GC, Vendors, All Stakeholders

**Format:** Formal presentation

**Purpose:**
- Present final IST plan and scripts
- Review test scenarios and objectives
- Present load bank and monitoring strategy
- Explain data collection methodology
- Review safety procedures
- Address stakeholder questions
- Confirm attendance and roles

### 19.10 Post-IST Closeout Meeting

**Timing:** Shortly after IST completion

**Participants:** CxA, Owner, Customer, GC, Vendors

**Purpose:**
- Review IST results summary
- Discuss preliminary findings
- Review outstanding issues
- Discuss closeout activities and timeline
- Plan final documentation delivery
- Address warranty and training items

### 19.11 Meeting Documentation
- Meeting minutes for all formal meetings
- Action item tracking with responsible parties and due dates
- Distribution to all participants
- Storage in document management platform

### 19.12 Ad-Hoc Meetings
- Technical coordination meetings as needed
- Issue resolution meetings for critical items
- Vendor-specific meetings
- Safety meetings
- Training sessions

---

## 20. ROLES & RESPONSIBILITIES

### 20.1 Owner / Client

**Primary Responsibilities:**
- Define Owner's Project Requirements (OPR)
- Final decision-maker on all unresolved issues
- Approve major commissioning decisions and changes
- Active participation in commissioning process
- Provide input and guidance on interpreting requirements
- Review and approve commissioning deliverables
- Attend key commissioning milestones (FAT, IST, etc.)
- Support transition to operations

**Commissioning-Specific:**
- Review and approve Commissioning Plan
- Participate in commissioning kickoff
- Attend major test witnessing (as desired)
- Review and approve test scripts (Level 4 and 5)
- Provide staff for training and knowledge transfer
- Accept final commissioning documentation

### 20.2 End Customer (If Different from Owner)

**Primary Responsibilities:**
- Provide input on project requirements (as applicable)
- Review commissioning procedures and test scripts
- Witness commissioning activities (as desired)
- Provide feedback on operational readiness

**Note:** Communication with customer handled through Owner. Customer involvement at Owner's discretion.

### 20.3 Commissioning Authority (CxA)

**Primary Responsibilities:**
- Lead and coordinate the commissioning process
- Develop and maintain Commissioning Plan
- Facilitate commissioning team collaboration
- Ensure commissioning objectives are met

**Specific Duties:**
- **Planning:**
  - Develop commissioning plan and schedule (L4-5)
  - Develop test scripts for Level 4 and Level 5
  - Develop load bank and monitoring plans
  - Facilitate commissioning meetings

- **Review:**
  - Review design documents for commissionability
  - Review sequences of operation
  - Review Level 1-3 test scripts and procedures
  - Review Level 1-3 commissioning documentation (sample basis)
  - Review O&M manuals and training materials

- **Execution:**
  - Direct Level 4 functional performance testing
  - Direct Level 5 integrated systems testing
  - Witness critical Level 1-3 activities (periodic)
  - Manage commissioning platform for L4-5
  - Document all testing activities
  - Manage Issue Resolution Log for L4-5

- **Reporting:**
  - Provide weekly commissioning reports
  - Provide daily commissioning reports during L4-5
  - Develop Final Commissioning Report
  - Provide analysis of test data
  - Report issues and progress to Owner

- **Quality Assurance:**
  - Verify commissioning quality and completeness
  - Ensure documentation meets requirements
  - Validate system performance
  - Verify training completion

### 20.4 General Contractor (GC)

**Primary Responsibilities:**
- Manage overall construction process
- Execute commissioning process Levels 0-3
- Support commissioning process Levels 4-5
- Coordinate vendors and subcontractors

**Specific Duties:**
- **Planning:**
  - Develop detailed commissioning schedule (L1-3)
  - Develop Level 1-3 test procedures and checklists
  - Coordinate commissioning activities with construction

- **Execution:**
  - Manage factory testing (FWT/FAT)
  - Manage Level 1 equipment installation verification
  - Manage Level 2 pre-startup inspections and testing
  - Manage Level 3 startup and commissioning
  - Manage commissioning platform for L1-3
  - Coordinate vendor and subcontractor commissioning activities

- **Support for L4-5:**
  - LOTO and electrical switching support
  - Load bank installation and movement
  - Construction power and utilities
  - Vendor and subcontractor coordination for testing support
  - Issue resolution coordination

- **Documentation:**
  - Compile and submit all L1-3 commissioning documentation
  - Develop O&M manuals
  - Coordinate training materials development
  - Provide as-built drawings
  - Manage document submittals and approvals

- **Quality Control:**
  - Implement QA/QC program
  - Verify contractor work quality
  - Manage construction issues and punch list
  - Close Level 1-3 commissioning issues

### 20.5 Design Team / Engineer of Record

**Primary Responsibilities:**
- Develop constructible, commissionable design
- Support commissioning process with technical expertise
- Address design-related issues

**Specific Duties:**
- **Design Phase:**
  - Develop Basis of Design (BOD)
  - Incorporate Owner's Project Requirements
  - Develop sequences of operation
  - Attend design review meetings
  - Address CxA design comments
  - Incorporate commissionability into design

- **Construction Phase:**
  - Respond to RFIs related to design intent
  - Review submittals for design compliance
  - Participate in commissioning meetings as needed
  - Support issue resolution for design-related items

- **Testing Phase:**
  - Review test scripts and procedures
  - Attend critical testing as needed
  - Provide technical guidance during commissioning
  - Verify design intent is achieved

- **Closeout:**
  - Support O&M manual development
  - Review final commissioning report
  - Provide design documentation for as-builts

### 20.6 Equipment Vendors / Manufacturers

**Primary Responsibilities:**
- Provide equipment per specifications
- Conduct factory testing
- Support installation and startup
- Provide technical expertise

**Specific Duties:**
- **Pre-Construction:**
  - Provide equipment submittals and shop drawings
  - Develop factory test procedures
  - Conduct factory acceptance testing (FAT/FWT)
  - Provide FAT documentation

- **Construction:**
  - Support installation (as specified)
  - Provide installation guidance
  - Review installation for compliance

- **Startup (Level 3):**
  - Develop startup procedures
  - Conduct equipment startup
  - Provide manufacturer's representative (as specified)
  - Perform initial equipment commissioning
  - Provide startup training
  - Provide startup documentation

- **Testing (Level 4-5):**
  - Support functional performance testing
  - Operate equipment during testing (as needed)
  - Provide technical expertise
  - Support issue resolution for equipment-related items
  - Attend testing as requested

- **Closeout:**
  - Provide O&M manuals and documentation
  - Provide training (as specified)
  - Provide as-built equipment information
  - Provide warranty documentation

### 20.7 Installing Contractors / Subcontractors

**Primary Responsibilities:**
- Install equipment and systems per drawings and specifications
- Conduct pre-startup testing
- Support commissioning activities

**Specific Duties:**
- **Construction:**
  - Install equipment and systems
  - Conduct installation QA/QC
  - Complete construction checklists
  - Coordinate with other trades

- **Level 2:**
  - Conduct pre-startup inspections
  - Perform pre-functional testing (insulation resistance, etc.)
  - Complete pre-startup checklists
  - Verify readiness for energization

- **Level 3:**
  - Support equipment startup
  - Conduct initial testing and adjustments
  - Complete startup checklists
  - Verify system operation

- **Level 4-5:**
  - Provide personnel support for testing
  - Execute corrective actions for issues
  - Support issue resolution

- **Closeout:**
  - Provide as-built information
  - Support training (as specified)
  - Provide documentation

### 20.8 Controls Contractors (BMS/EPMS)

**Primary Responsibilities:**
- Install and program control systems
- Verify control sequences
- Support commissioning and testing

**Specific Duties:**
- **Construction:**
  - Install control panels and field devices
  - Install network infrastructure
  - Develop control graphics

- **Programming:**
  - Program control sequences
  - Configure alarms and setpoints
  - Configure trending and reporting
  - Integrate systems

- **Level 2:**
  - Conduct point-to-point checkout
  - Verify sensor calibrations
  - Verify network communications

- **Level 3:**
  - Verify control sequences during startup
  - Adjust and optimize controls
  - Verify graphics and trending

- **Level 4-5:**
  - Provide access to control systems for monitoring
  - Provide training to CxA on control system (if required)
  - Provide trending and screenshot support
  - Support testing with simulations (where possible)
  - Support issue resolution

- **Closeout:**
  - Provide as-built control documentation
  - Provide operator training
  - Provide programming documentation

### 20.9 Test and Balance (TAB) Contractor

**Primary Responsibilities:**
- Balance air and water systems
- Verify system flows and performance
- Provide TAB documentation

**Specific Duties:**
- Conduct air system TAB
- Conduct water system TAB (if applicable)
- Document all measurements and adjustments
- Provide TAB report per industry standards (AABC, NEBB, etc.)
- Support commissioning with flow verification

---

## 21. CONTROL SEQUENCE / SEQUENCE OF OPERATIONS REVIEW

### 21.1 Purpose
Control sequences (Sequence of Operations - SoO) define how systems are intended to operate under all conditions. These are critical documents for:
- Design verification
- Programming of control systems
- Development of test procedures
- Operational training
- Troubleshooting

### 21.2 Sequence of Operations Development

**Responsibility:**
- Developed by: Design Engineer / Controls Engineer
- Reviewed by: CxA, GC, Owner, Vendors

**Content Requirements:**
Each sequence of operations shall include:
- System description and components
- Normal operating sequences
- Startup sequences
- Shutdown sequences
- Seasonal operation modes (if applicable)
- Manual operation modes
- Maintenance mode operation
- Failure mode responses
- Safety sequences and interlocks
- Alarm conditions and responses
- Control setpoints and ranges
- Equipment staging and lead/lag operation
- Integration with other systems
- Energy optimization sequences

### 21.3 Review Process

**Initial Review - Design Phase:**
1. **SoO Submission**
   - Design team develops SoO for all systems
   - Submitted to CxA for review
   - Timeline: [X] weeks before programming begins

2. **CxA Review**
   - Technical accuracy
   - Completeness
   - Alignment with BOD and OPR
   - Commissionability
   - Testability
   - Identification of potential issues:
     - Ambiguities
     - Conflicts between systems
     - Single points of failure
     - Safety concerns
     - Energy efficiency opportunities

3. **Comment Resolution**
   - CxA provides comments via design review log
   - Design team addresses comments
   - Revised SoO submitted
   - Iterative process until approval

4. **Stakeholder Review**
   - Owner review and comment
   - GC review
   - Controls contractor review
   - Vendor review (for equipment-specific sequences)

5. **Final Approval**
   - All comments addressed
   - Final SoO approved by Owner and CxA
   - Basis for control system programming
   - Basis for test script development

**Update Review - Construction Phase:**
- SoO updated as design develops or changes occur
- Change control process for revisions
- Re-review and approval of changes
- Version control maintained

**As-Built Review - Commissioning Phase:**
- Verification that programmed sequences match approved SoO
- Testing confirms sequences operate as documented
- Updates to SoO based on field adjustments
- Final as-built SoO incorporated into O&M manual

### 21.4 Documentation Requirements

**Minimum Documentation:**
- Narrative description of sequences
- Sequence flow diagrams or logic diagrams
- Setpoint schedules
- Alarm conditions
- Interlock descriptions
- Equipment lists affected by sequence

**Equipment Requiring SoO:**
All equipment with automation or control interfaces, including but not limited to:
- HVAC equipment (CRAH, CRAC, AHU, chillers, pumps, cooling towers)
- Electrical equipment (generators, ATS, UPS, switchgear with automation)
- Building management system
- Electrical power monitoring system
- Fire suppression system (integration)
- Leak detection system
- Security system (integration)
- Any ancillary systems with automation

### 21.5 Use in Commissioning

**Test Script Development:**
- Level 1-3 test scripts reference SoO
- Level 4-5 test scripts directly test SoO compliance
- Each step of sequence verified during testing

**Performance Verification:**
- Actual operation compared to documented SoO
- Deviations documented as issues
- Field optimization documented and SoO updated

**Training:**
- SoO used as basis for operator training
- Understanding of sequences critical for operations
- Troubleshooting based on sequence knowledge

### 21.6 Critical Importance
The quality and accuracy of sequences of operations is critical to successful commissioning. Incomplete, ambiguous, or incorrect sequences result in:
- Programming errors
- Failed commissioning tests
- Rework and delays
- Operational issues
- Safety concerns

Therefore, thorough review and approval of SoO is a priority commissioning activity.

---

## 22. LESSONS LEARNED

### 22.1 Purpose
Capture knowledge gained during the commissioning process to:
- Improve future projects
- Avoid repeating mistakes
- Share best practices
- Enhance commissioning processes
- Provide value to Owner and industry

### 22.2 Lessons Learned Process

**Ongoing Collection:**
- Lessons learned log maintained throughout project lifecycle
- Input from all commissioning team members
- Documented as they occur (not just at end of project)
- Categorized for easy reference

**Categories:**
- Design phase lessons
- Construction coordination
- Equipment selection and procurement
- Testing procedures and methodologies
- Issue resolution approaches
- Schedule and planning
- Communication and coordination
- Documentation and reporting
- Training and knowledge transfer
- Technology and tools

**Data Collection:**
- What worked well (best practices)
- What didn't work well (areas for improvement)
- Root cause of issues
- Solutions implemented
- Recommendations for future projects

### 22.3 Lessons Learned Session

**Timing:** After IST completion, during closeout phase

**Participants:** All key commissioning team members
- CxA
- Owner/Customer
- GC
- Design Team
- Key Vendors
- Controls Contractors

**Format:**
- Facilitated session (1-2 hours)
- Open discussion
- Non-attribution to encourage honesty
- Focus on process improvement, not blame

**Topics:**
- Overall commissioning process effectiveness
- Schedule and planning accuracy
- Quality of documentation and submittals
- Effectiveness of communication and coordination
- Design constructibility and commissionability
- Equipment performance vs. expectations
- Testing procedures effectiveness
- Issue resolution process
- Tool and technology effectiveness
- Training adequacy

### 22.4 Documentation

**Lessons Learned Report:**
- Summary of key lessons in each category
- Specific examples and recommendations
- Included in Final Commissioning Report appendix
- Provided to Owner for future reference

**Continuous Improvement:**
- CxA incorporates lessons into future commissioning plans
- Owner incorporates into project requirements
- Industry sharing (as appropriate and approved)

---

## 23. TRAINING REQUIREMENTS

### 23.1 Training Objectives
- Ensure operations staff can operate facility safely and effectively
- Transfer knowledge from design and commissioning teams
- Provide understanding of systems and sequences
- Enable troubleshooting and optimization
- Support operational excellence

### 23.2 Training Plan Development

**Responsibility:** GC develops training plan, CxA reviews

**Training Plan Contents:**
- Training objectives
- Training topics and content outline
- Target audience (operations, maintenance, management)
- Delivery method (classroom, hands-on, combination)
- Duration and schedule
- Trainer qualifications
- Training materials and aids
- Evaluation method
- Documentation requirements

**Training Plan Approval:**
- Submitted to CxA and Owner for review
- Comments addressed
- Final approval before implementation

### 23.3 Training Content

**Systems Training:**
- System descriptions and components
- System operation (normal and emergency)
- Sequences of operation
- Control systems operation
- Monitoring and alarming
- Performance expectations
- Common issues and troubleshooting

**Equipment Training:**
- Equipment operation
- Control interfaces
- Maintenance requirements
- Safety procedures
- Manufacturer-specific training (as required)

**Emergency Procedures:**
- Emergency shutdown procedures
- Emergency power operation
- Evacuation procedures
- Emergency contact protocols
- Incident reporting

**Maintenance Training:**
- Preventive maintenance procedures
- Predictive maintenance approaches
- Parts and consumables
- Documentation and record keeping
- Vendor support resources

### 23.4 Training Delivery

**Timing:**
- Initial training: During Level 3 startup activities
- Comprehensive training: After Level 4 testing complete
- Final training: Before or shortly after IST
- Additional sessions as needed

**Trainers:**
- Equipment vendors (for equipment-specific training)
- Controls vendors (for BMS/EPMS training)
- Commissioning team (for systems and operations)
- Specialized trainers (as needed)

**Methods:**
- Classroom instruction
- Hands-on equipment operation
- Control system demonstration and practice
- Scenario-based training
- Mock emergency drills

### 23.5 Training Documentation

**During Training:**
- Attendance records (sign-in sheets)
- Training agenda and schedule
- Training materials used
- Evaluation forms/tests (if applicable)
- Questions and answers log

**Training Materials:**
- Training presentations
- Handouts and reference materials
- Operating procedures
- Troubleshooting guides
- Contact information
- System diagrams and drawings

**Post-Training:**
- Training completion certificates
- Evaluation summaries
- Recommendations for additional training
- Incorporation of materials into O&M manual

### 23.6 Training Verification

**CxA Review:**
- Attendance at key training sessions (as specified)
- Review of training materials
- Verification training covered required topics
- Assessment of training effectiveness
- Identification of gaps or additional needs

**Operator Competency:**
- Evaluation of operator understanding
- Hands-on demonstration of key operations
- Additional training as needed

### 23.7 Ongoing Training
- Recommendations for refresher training
- New hire training procedures
- Ongoing vendor training support
- Annual or periodic training updates

---

## 24. SAFETY

### 24.1 Safety Policy
Safety is the highest priority during all commissioning activities. All commissioning team members shall:
- Comply with all applicable safety regulations and codes
- Follow site-specific safety requirements
- Participate in safety briefings and training
- Report unsafe conditions immediately
- Have authority to stop work for safety concerns

### 24.2 Safety Plan Reference
The CxA shall develop and maintain a comprehensive Health and Safety Plan that details:
- Safety rules and procedures
- Site-specific safety requirements
- Personal protective equipment (PPE) requirements
- Hazard identification and mitigation
- Emergency procedures
- Incident reporting
- Safety training requirements
- Day-to-day safety management

**Reference:** [Link to separate Safety Plan document]

### 24.3 Key Safety Considerations for Commissioning

**Electrical Safety:**
- Lockout/Tagout (LOTO) procedures strictly enforced
- Arc flash PPE requirements
- Qualified personnel only for electrical work
- Energized work permits (if required)
- Electrical switching procedures and approvals
- Proper use of electrical test equipment
- Grounding and bonding verification

**Mechanical Safety:**
- Rotating equipment guarding
- Hot surface protection
- Pressurized system safety
- Confined space entry procedures (if applicable)
- Fall protection (if applicable)
- Heavy equipment and rigging safety

**Load Bank Testing Safety:**
- Heat exposure management
- Adequate ventilation
- Fire watch requirements
- Load bank connection/disconnection safety
- Cable management and tripping hazards
- Access control during testing

**Chemical Safety:**
- Water treatment chemical handling
- Refrigerant safety
- Material Safety Data Sheets (MSDS/SDS) available
- Proper storage and handling

**Testing-Specific Safety:**
- Pre-test safety briefings
- Test area access control
- Communication protocols during testing
- Emergency shutdown procedures
- First aid availability
- Emergency contact information posted

### 24.4 Safety Meetings and Briefings
- Site safety orientation for all personnel
- Daily safety briefings during active testing
- Pre-test safety briefings for each major test
- Weekly safety topics at commissioning meetings
- Incident investigation and lessons learned

### 24.5 Incident Reporting
- All incidents, near-misses, and safety concerns reported immediately
- Incident investigation conducted
- Corrective actions implemented
- Incident reports documented
- Lessons learned shared

---

## 25. COMMISSIONING GLOSSARY

| Term | Definition |
|------|------------|
| **Acceptance** | Formal action taken by authorized person to declare that some aspect of project meets defined requirements, permitting subsequent activities to proceed |
| **As-Built** | Documentation reflecting actual installed conditions, including any changes from original design |
| **Basis of Design (BOD)** | Document recording concepts, calculations, decisions, and product selections used to meet Owner's Project Requirements and satisfy applicable standards |
| **Blue Tag** | Level 4 commissioning tag indicating functional performance testing complete and equipment ready for integrated systems testing |
| **Commissioning (Cx)** | Quality-focused process for enhancing project delivery by verifying and documenting that facility and systems are designed, installed, tested, operated, and maintained to meet Owner's Project Requirements |
| **Commissioning Authority (CxA)** | Entity identified by Owner who leads, plans, schedules, and coordinates commissioning team to implement commissioning process |
| **Commissioning Plan** | Document outlining organization, schedule, resource allocation, and documentation requirements of commissioning process |
| **Contract Documents** | Documents governing responsibilities and relationships between parties, including agreements, drawings, specifications, and change orders |
| **Factory Acceptance Test (FAT)** | Testing conducted at manufacturer's facility to verify equipment performance before shipment |
| **Functional Performance Test (FPT)** | Level 4 testing to verify equipment and systems function as designed under all modes of operation |
| **Green Tag** | Level 3 commissioning tag indicating equipment energized, started up, and ready for functional performance testing |
| **Handover to Commissioning (H2C)** | Critical transition from construction phase to acceptance phase, signifying completion of Level 3 and readiness for Level 4 |
| **Integrated Systems Test (IST)** | Level 5 testing of facility as complete system to verify proper operation, redundancy, and fail-safe operations |
| **Issue Resolution Log (IRL)** | Formal ongoing record of problems or concerns and their resolution during commissioning process |
| **ITIC/CBEMA Curve** | Power quality standard curve showing acceptable voltage and frequency ranges for IT equipment |
| **Lockout/Tagout (LOTO)** | Safety procedure to ensure equipment is properly isolated from energy sources during maintenance or testing |
| **Operation and Maintenance (O&M) Manual** | Comprehensive manual providing information for operating and maintaining facility systems and equipment |
| **Owner's Project Requirements (OPR)** | Written document detailing functional requirements and expectations for how project will be used and operated |
| **Power Quality Meter (PQM)** | Device to measure and record electrical parameters including voltage, current, harmonics, and transients |
| **Pre-Functional Test (PFT)** | Level 3 testing conducted by vendor/contractor during startup to verify basic equipment operation |
| **Red Tag** | Level 1 commissioning tag indicating equipment factory tested, delivered, and installed but not ready for startup |
| **Sequence of Operation (SoO)** | Detailed description of how system or equipment operates under all conditions |
| **Single Point of Failure (SPoF)** | Component or system whose failure would cause entire system or facility to fail |
| **Site Acceptance Inspection (SAI)** | Level 2 inspection to verify equipment properly installed and safe to energize |
| **Substantial Completion** | Project stage where work or designated portion is sufficiently complete for Owner to occupy or use, typically triggered by successful IST |
| **Test and Balance (TAB)** | Process of adjusting air and water systems to achieve design flow rates |
| **White Tag** | Level 5 commissioning tag indicating integrated systems testing complete and commissioning verification complete |
| **Yellow Tag** | Level 2 commissioning tag indicating pre-startup inspections complete and equipment ready for energization |

---

## 26. ANNEX OVERVIEW

The following annexes provide detailed supporting information for this Commissioning Plan:

### Annex A – Equipment List
- Complete list of all equipment to be commissioned
- Equipment tag numbers and descriptions
- System assignments
- Commissioning levels applicable to each equipment type

### Annex B – Commissioning Team Organization Charts
- Project organization chart
- Commissioning Authority organization chart
- Contact information for all team members

### Annex C – Level 1-3 Equipment Tag Checklists
- Red Tag checklists by equipment type
- Yellow Tag checklists by equipment type
- Green Tag checklists by equipment type

### Annex D – Level 4-5 Test Script Index
- List of all functional performance test scripts
- List of all integrated systems test scripts
- Test script numbering and organization

### Annex E – Forms and Templates
- Issue Resolution Log form
- Meeting minutes template
- Daily commissioning report template
- Weekly commissioning report template
- Test data collection forms

### Annex F – Schedule
- High-level commissioning schedule
- Milestone dates
- Critical path activities

### Annex G – Reference Standards and Codes
- Complete list of applicable standards
- Complete list of applicable codes
- Industry best practices references

### Annex H – Load Bank and Monitoring Plan
- Detailed load bank placement drawings
- PQM placement plan
- Environmental monitoring plan
- Testing sequence and strategy

### Annex I – Safety Plan
- Comprehensive Health and Safety Plan
- Site-specific safety requirements
- Emergency procedures

### Annex J – Training Plan
- Detailed training schedule
- Training content outlines
- Training materials list

---

## DOCUMENT APPROVAL

This Commissioning Plan has been reviewed and approved by the following:

**Commissioning Authority:**

Name: ________________________
Title: ________________________
Signature: ____________________
Date: ________________________

**Owner:**

Name: ________________________
Title: ________________________
Signature: ____________________
Date: ________________________

**General Contractor:**

Name: ________________________
Title: ________________________
Signature: ____________________
Date: ________________________

---

## REVISION HISTORY

| Revision | Date | Description of Changes | Prepared By | Approved By |
|----------|------|------------------------|-------------|-------------|
| 0.1 | [Date] | Initial Draft | [Name] | - |
| 1.0 | [Date] | First Issue for Review | [Name] | [Name] |
| 2.0 | [Date] | Final Issue | [Name] | [Name] |

---

**END OF COMMISSIONING PLAN OUTLINE TEMPLATE**

---

**Notes for Use:**

1. This template is generic and should be customized for specific project requirements
2. All bracketed items [ ] should be replaced with project-specific information
3. Sections may be expanded, condensed, or reordered based on project needs
4. Annexes should be developed as separate documents and referenced
5. The plan should be treated as a living document and updated throughout the project
6. Ensure all regulatory and contractual requirements are incorporated
7. Obtain stakeholder input and approval before finalizing
8. Maintain version control throughout project lifecycle
