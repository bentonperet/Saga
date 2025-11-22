# PGCIS Commissioning Standard

**Purpose:** Comprehensive commissioning specification standard for data center projects, establishing consistent quality control processes and documentation requirements across all PGCIS commissioning engagements.

**Created:** 2025-11-20
**Status:** Active
**Tags:** #commissioning #standard #pgcis #specification

---

## Overview

The PGCIS Commissioning Standard provides a complete master specification for general commissioning requirements on mission-critical facility projects. This standard defines:

- **5-Level Commissioning Process** (Level 1 - Level 5)
- **Roles & Responsibilities** for all commissioning team members
- **Documentation Requirements** at each commissioning level
- **Quality Assurance** processes and acceptance criteria
- **Testing Protocols** and procedures
- **Reporting Standards** and deliverables

---

## When to Use This Standard

Use this standard when:

1. **Developing Commissioning Specifications** for new data center projects
2. **Writing RFP Responses** that include commissioning scope
3. **Training Team Members** on commissioning processes and expectations
4. **Establishing Project Baselines** for commissioning activities
5. **Reviewing Contractor Submittals** for compliance with standards
6. **Resolving Disputes** by referencing specification requirements

---

## Document Structure

### Part 1 - GENERAL
- Summary and scope
- Related documents and references
- Comprehensive definitions (20+ key terms)
- Compensation provisions
- Commissioning team structure
- Detailed roles and responsibilities (10 parties)
- Submittal requirements (informational and closeout)
- Quality assurance requirements

### Part 2 - PRODUCTS
- Test equipment and instrumentation requirements
- Commissioning software specifications (CxAlloy)
- Proprietary test equipment guidelines
- Report format and organization standards

### Part 3 - EXECUTION
- Preparation requirements
- Level 2 and Level 3 documentation forms
- **Level 1:** Factory Witness Testing (FWT) / Factory Acceptance Test (FAT)
- **Level 2:** Pre-Start Up Documentation
- **Level 3:** Equipment Start-Up and Pre-Functional Testing (PFT)
- **Level 4:** Functional Performance Testing (FPT)
- **Level 5:** Integrated System Testing (IST)
- General execution requirements
- Testing protocols and procedures
- Scheduling requirements
- Commissioning reports
- Certificate of Construction Phase Commissioning Completion

---

## The 5-Level Commissioning Process

### Level 1 - Factory Witness Testing (FWT/FAT)
**Timeline:** Prior to equipment delivery
**Location:** Manufacturer facility
**Scope:** QA/QC review of factory test deliverables, witness testing (when specified)
**Key Activities:**
- Factory test procedure review and approval
- Witness testing attendance (when required by Owner)
- Equipment capacity, safety, and controls verification
- Issues log maintenance for factory deficiencies

**Deliverables:**
- Factory test reports per IEEE/NETA standards
- As-built drawings showing factory modifications
- Nameplate verification photographs
- Shipping and handling documentation
- Warranty certificates

---

### Level 2 - Pre-Start Up Documentation
**Timeline:** During equipment delivery and installation
**Location:** Project site
**Scope:** Installation verification and pre-energization inspections
**Key Activities:**
- Site arrival inspections with photographic documentation
- Equipment storage verification per manufacturer requirements
- Equipment model verification (make, model, serial number)
- Pre-installation physical condition checks
- Pre-installation component verification
- Pre-energization inspection (housekeeping, labeling, panel schedules)

**Deliverables:**
- Completed Level 2 documentation forms
- Delivery receipt checks with photos
- Equipment model verification records
- Installation compliance issue tracking
- System readiness evaluation summaries

---

### Level 3 - Equipment Start-Up and Pre-Functional Testing (PFT)
**Timeline:** Following installation, prior to Level 4
**Location:** Project site
**Scope:** Manufacturer startup, adjustment, and performance validation
**Key Activities:**
- Equipment startup per manufacturer procedures
- "As-left" equipment settings documentation
- Building Automation System (BAS) online verification
- Point-to-point verification (field device to BAS GUI)
- Field device calibration and verification
- Temporary Arc Flash labeling installation

**Deliverables:**
- Completed Level 3 startup documentation
- Equipment setpoint matrices with "as-left" values
- Point-to-point verification records
- BAS/EPMS online confirmation
- Level 1-3 Issues Log (closed)
- Certificate of Construction Completion

---

### Level 4 - Functional Performance Testing (FPT)
**Timeline:** After Level 3 completion
**Location:** Project site
**Scope:** Individual equipment and system functional verification
**Key Activities:**
- CxA-directed functional performance testing
- Circuit breaker and relay settings verification
- Equipment-level testing per approved sequences of operations
- System-level integrated testing
- Load bank testing (per Load Bank and Metering Plan)
- Power quality monitoring and thermal imaging
- Issue tracking with priority classifications (Critical/High/Medium/Low)

**Deliverables:**
- Approved Level 4 test procedures
- Completed test data forms with signatures
- Circuit Breaker and Relay Settings Verification Checklists
- Level 4 Issues Log with resolutions
- Daily commissioning status reports
- Thermographic survey baseline reports

**Testing Philosophy:**
- **100% sampling protocol** - all equipment tested unless Owner approves exception
- Testing proceeds from field device → equipment → system levels
- Non-compliance stops testing until corrected
- Retest until acceptable results achieved

---

### Level 5 - Integrated System Testing (IST)
**Timeline:** After all Level 4 tests pass
**Location:** Project site
**Scope:** Facility-level integrated system validation
**Key Activities:**
- Site-level systems testing under various load conditions
- Automatic response verification (no active human intervention)
- Severe operating conditions validation
- Extended duration operation tests
- Deferred testing plan development (if needed)
- Permanent Arc Flash labeling installation

**Deliverables:**
- Approved Level 5 test procedures
- Completed integrated system test data
- Level 5 Issues Log with resolutions
- Final Commissioning Report (within 4 weeks)
- Certificate of Construction Phase Commissioning Completion (within 48 hours)
- Training completion verification

**Completion Criteria:**
- All Level 4 tests successfully passed
- BAS & EPMS fully operational
- All systems functioning per Owner's Requirements
- Issues resolved or deferred with Owner approval

---

## Key Features

### Comprehensive Roles & Responsibilities Matrix

The standard includes a detailed RACI matrix defining responsibilities for:
- General Contractor / Construction Manager (GC/CM)
- Installing Contractors
- Manufacturer(s)/Vendor(s)
- Third Party Electrical Testing Company (NETA certified)
- Commissioning Authority (CxA)
- Architect/Engineer of Record (AOR/EOR)
- Owner's Design Team
- Owner's Construction Management Team
- Owner's Facility Operations Team

### Quality Assurance Requirements

**CxA Qualifications:**
- 3+ similar projects of comparable scope and complexity
- Required certifications (BCA, ASHRAE, UW-Madison)

**Calibration Requirements:**
- All test equipment calibrated within 12 months
- NIST-traceable calibration certificates
- Permanent calibration tags

**NETA Testing:**
- Independent third-party electrical testing
- NETA certified company with 10+ years experience
- Testing per most recent NETA Acceptance Testing Standard

### Deficiency Classification System

**Critical:** Impacts overall building functionality, immediate resolution required
**High:** Impacts equipment/system functionality, 2-day resolution target
**Medium:** Impacts isolated equipment/system operation
**Low:** Does not affect critical system functionality

### Documentation & Reporting Standards

**Issues Log Requirements:**
- Equipment tag / system
- Date identified, identified by, responsible party
- Discipline, status, priority
- Root cause analysis
- Resolution documentation
- Supporting photos and data

**Test Report Standards:**
- As-tested system configuration
- Trend logs and power quality data
- Attendee lists
- Historical data from previous day
- Waveform data (when applicable)

---

## How to Use This Standard

### For Project-Specific Specifications

1. **Copy the master specification** to your project folder
2. **Customize the following sections:**
   - Section 1.2: Add project-specific related documents
   - Section 1.5: Identify specific team members and companies
   - Appendix A: Develop project-specific Testing Outline
   - Appendix B: Develop project-specific Load Bank and Metering Plan
3. **Review and modify:**
   - Timelines and durations to match project schedule
   - Specific equipment lists to match project scope
   - Testing requirements based on equipment complexity

### For RFP Responses

1. **Reference this standard** to demonstrate PGCIS methodology
2. **Extract relevant sections** for proposal technical approach:
   - Commissioning process overview (5 levels)
   - Roles and responsibilities summary
   - Quality assurance approach
   - Deliverables and reporting
3. **Customize timelines** based on RFP-specific schedule
4. **Highlight differentiators:**
   - 100% sampling protocol
   - CxAlloy commissioning software
   - Comprehensive deficiency classification
   - 48-hour completion letter turnaround

### For Training

1. **Use as training manual** for new commissioning team members
2. **Key training topics:**
   - 5-level commissioning process flow
   - Roles and responsibilities by party
   - Documentation requirements at each level
   - Issues log maintenance and resolution
   - Quality assurance and acceptance criteria
3. **Conduct table-top exercises** using standard as reference

### With Claude AI

This standard is optimized for use with Claude Code:

```plaintext
"Create a Level 4 test procedure for [equipment type] based on PGCIS Cx Standard"
"Generate a commissioning schedule for [project] using PGCIS 5-level process"
"Review this contractor submittal against PGCIS Cx Standard requirements"
```

---

## Integration with Other Templates

### Works With:
- **Commissioning Plan Templates** (Cx_Plan_Templates folder)
- **Equipment Testing Procedures** (Equipment_Testing folder)
- **RFP Response Framework** (RFP_Response folder)
- **BOD Development Templates** (for design review)

### Feeds Into:
- Project-specific commissioning specifications
- Contractor scopes of work
- RFP technical proposals
- Commissioning plan documents
- Training materials

---

## Frequently Asked Questions

### Q: Is factory witness testing always required?
**A:** No. Level 1 scope varies by project. Standard supports:
- Factory Acceptance Testing (FAT) by manufacturer without witness
- Factory Witness Testing (FWT) when Owner requires attendance
- QA/QC review of factory test reports (always in CxA scope)

### Q: Can we modify the 5-level structure?
**A:** The 5-level framework is core to PGCIS methodology. However:
- Specific activities within each level can be customized
- Timelines and durations are project-specific
- Testing sampling can be adjusted with Owner approval (default is 100%)

### Q: What commissioning software is required?
**A:** CxAlloy is the PGCIS standard platform. Key requirements:
- Web-accessible with user permissions
- Real-time progress tracking
- Equipment list and deficiency log management
- Checklist and test script execution
- File sharing and design review hosting

### Q: How are Level 4 and Level 5 different?
**A:**
- **Level 4 (FPT):** Tests individual equipment and systems against sequences of operations
- **Level 5 (IST):** Tests integrated facility-level operation under various conditions

Level 5 cannot begin until all Level 4 tests pass.

### Q: What if testing cannot be completed on schedule?
**A:** Standard includes provisions for:
- **Seasonal/Deferred Tests:** Approved tests completed after Cx completion when conditions allow
- **Delayed Tests:** Tests delayed due to correctable issues, completed when resolved

All require Owner approval and documented schedule.

---

## Maintenance and Updates

### Version Control
- Current Version: 1.0 (2025-11-20)
- Review cycle: Annually or after major project lessons learned
- Update authority: PGCIS Technical Director

### How to Propose Changes
1. Document proposed change with justification
2. Reference specific section(s) affected
3. Submit via GitHub issue or direct to Technical Director
4. Include lessons learned or project examples supporting change

### Change Log
Future versions will maintain a change log in this section documenting:
- Version number and date
- Sections modified
- Rationale for changes
- Effective date for new projects

---

## Related Documents

- [[PGCIS Commissioning Standard - Master Specification]]
- [[Cx Standard Appendix A - Testing Outline Template]]
- [[Cx Standard Appendix B - Load Bank and Metering Plan Template]]
- [[Equipment Testing Procedures Index]]
- [[Commissioning Plan Templates]]
- [[PGCIS Knowledge Management Strategy]]

---

## Support and Questions

For questions about this standard:
- **Technical Questions:** Contact PGCIS Technical Director
- **Project Application:** Consult with assigned Commissioning Authority
- **Training Requests:** Contact PGCIS Training Coordinator

---

**Last Updated:** 2025-11-20
**Document Owner:** PGCIS Technical Team
**Tags:** #commissioning #standard #pgcis #documentation #quality-assurance