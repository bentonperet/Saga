**Created:** 2025-10-23 13:00

# BASIS OF DESIGN - GENERAL REQUIREMENTS
## CSI Division 01
### Saga Energy – Pryor Data Center

**Parent Document:** [[_BOD - Exec Summary and TOC]]
**Related:** [[0BOD - Procurement and Contracting (CSI Div 00)]] | [[Basis of Design - Part 1 Core Systems]]

---

## OVERVIEW

**Division 01 is the Project's Operating System.** It establishes the administrative, procedural, and quality framework that governs all technical divisions (02-49). If Division 23 specifies "what" chiller to install, Division 01 defines "how" to manage its submittal, coordination, installation, testing, and commissioning.

**Critical Role for Data Centers:**
Division 01 translates high-level BOD goals (e.g., "Tier III Concurrent Maintainability") into contractual, actionable requirements. It defines hold points, testing protocols, and acceptance criteria that ensure the facility performs as designed.

**Key Sections:**
- **01 30 00:** Administrative Requirements (submittals, RFIs, coordination)
- **01 40 00:** Quality Requirements (QA/QC, testing, hold points, third-party verification)
- **01 50 00:** Temporary Facilities (site logistics, temporary power, security)
- **01 60 00:** Product Requirements (materials, certifications, data center-specific standards)
- **01 70 00:** Execution (BIM coordination, phasing, protection of work)
- **01 78 00:** Closeout Submittals (as-builts, O&M manuals, warranties)
- **01 79 00:** Demonstration and Training (owner operator training)
- **01 91 00:** Commissioning (FAT, SAT, IST, Tier III verification)

---

## 01 10 00 - PROJECT SUMMARY

### Work Sequence & Phasing

**Phase 1 Construction Sequence:**
1. Site prep, utilities, foundations (Months 1-4)
2. Structural steel, building envelope (Months 3-8)
3. MEP rough-in (overhead distribution, electrical rooms, chiller yard) (Months 6-14)
4. Equipment setting (UPS, generators, chillers) (Months 10-16)
5. Interior finishes, controls integration (Months 12-16)
6. Pre-functional testing (Months 15-17)
7. Integrated systems testing (IST) (Month 17)
8. 72-hour full-load test and acceptance (Month 18)

**Phase 2 Shell Fit-Out:** Triggered by 70-80% Phase 1 occupancy, 6-9 month duration

**Critical Path:** Utility interconnection (6-18 month lead time), UPS procurement (9-12 months)

---

## 01 31 00 - PROJECT MANAGEMENT & COORDINATION

### BIM Requirements

**Mandate:** Building Information Modeling (BIM) required for all M/E/P trades

**Rationale:** Data center has massive, parallel systems (36" chilled water pipes, multiple busways, overhead cable trays) competing for limited space. BIM clash detection is essential to avoid field conflicts.

**Level of Detail (LOD) Requirements:**
- **LOD 300:** Design development (major equipment and routing)
- **LOD 350:** Shop drawings and coordination drawings
- **LOD 400:** As-built documentation

**BIM Coordination Meetings:**
- **Frequency:** Weekly during construction, biweekly during design
- **Participants:** GC, M/E/P subcontractors, owner's representative, engineer
- **Deliverables:** Clash detection reports, resolution documentation, coordinated models

**Coordination Zones:**
- Above 12 ft elevation: Busway, cable tray, HVAC ductwork, sprinkler piping
- Below 12 ft elevation: Chilled water piping, conduit, fire alarm, access clearances

### RFI Procedures

**Submittal:** Written RFIs via project management software (Procore, e-Builder, etc.)
**Response Time:** Owner/engineer to respond within 7 business days
**Critical RFIs:** Flagged for 3-day response (hold points, safety issues)

---

## 01 30 00 - ADMINISTRATIVE REQUIREMENTS

### Submittal Requirements

### Design Phase Submittals

**Basis of Design (BOD) Documents:**
- Equipment schedules with capacities, redundancy configuration
- Single-line electrical diagrams (2N UPS topology)
- Mechanical flow diagrams (chilled water, cooling distribution)
- Control sequences and BMS integration points

**Design Reviews:**
- 30% design review: Concept validation, major equipment selection
- 60% design review: Coordination review, value engineering
- 90% design review: Final design verification, constructability review

### Construction Phase Submittals

**Shop Drawings:**
- UPS: Single-line diagrams, module configurations, phasing plan
- Generators: Load sharing logic, fuel systems, ATS coordination
- Chillers: Piping and controls diagrams, free cooling sequences
- Electrical Distribution: Busway layouts, panel schedules, grounding
- Fire Suppression: Hydraulic calculations, sprinkler layouts, detection zones

**Product Data:**
- Manufacturer cut sheets for all major equipment
- Performance data (UPS efficiency curves, chiller performance maps)
- Warranty terms and service agreements

**Sample Submittals:**
- Finishes, flooring, paint colors (owner approval required)
- Cable tray, conduit, pipe materials

**Submittal Review Timeline:**
- Contractor submits → Owner/Engineer review (14 days) → Resubmit if required (7 days)
- No fabrication or installation prior to submittal approval

---

## 01 40 00 - QUALITY REQUIREMENTS

### Hold Points

**Concept:** Hold points are mandatory inspection/approval stages where work must stop until owner/engineer verification is complete. Critical for data center quality assurance.

**Required Hold Points:**
1. **Foundation Pour:** Rebar placement, grounding grid installation, anchor bolt verification
2. **Structural Steel Erection:** Base plates, critical connections, seismic bracing
3. **Electrical Gear FAT:** UPS, generators, switchgear (witness testing at factory)
4. **NETA Acceptance Testing:** All electrical distribution equipment before energization
5. **UPS Installation:** Rigging, placement, connections, grounding verification
6. **Chiller Installation:** Piping connections, refrigerant charge, control wiring
7. **Pre-Functional Testing Completion:** All systems tested individually before IST
8. **Integrated Systems Testing (IST):** Full facility testing before owner acceptance

**Documentation:** Hold point sign-off forms required from owner's representative before proceeding.

### Third-Party Testing & Inspection

**NETA Acceptance Testing (Electrical):**
- **Scope:** All electrical distribution equipment (switchgear, UPS, generators, busway, panels)
- **Standards:** ANSI/NETA ATS (Acceptance Testing Specifications)
- **Tests:** Insulation resistance, contact resistance, protective relay calibration, load bank testing
- **Deliverable:** NETA test report with certified engineer seal

**TAB (Testing, Adjusting, Balancing):**
- **Scope:** All HVAC systems (chillers, pumps, CDUs, airflow)
- **Standards:** AABC or NEBB certification required
- **Deliverable:** Final TAB report with measured vs design performance

**Fire Alarm & Suppression:**
- **Scope:** Detection, notification, suppression activation
- **Inspector:** State-certified fire protection inspector
- **Deliverable:** Fire marshal approval and certificate of occupancy

### Mock-Ups

**Purpose:** Physical mock-ups verify constructability and quality standards before full-scale execution.

**Required Mock-Ups:**
1. **Overhead Coordination:** Full-scale mock-up of busway, cable tray, ductwork, piping, and sprinkler coordination at typical data hall bay
2. **Penetrations:** Fire-rated wall/floor penetrations with proper firestopping
3. **Equipment Access:** Verify maintenance clearances for UPS, generators, chillers

**Approval:** Owner/engineer approval required before proceeding with production work.

### Manufacturer Certifications

**UPS Systems:**
- Factory acceptance testing (FAT) at manufacturer facility
- Witness testing by owner's representative
- Tier III compliance documentation

**Generators:**
- Load bank testing at 100%, 110% rated load
- Paralleling and load sharing verification
- Fuel system pressure testing

**Chillers:**
- Factory run testing (performance verification)
- Refrigerant leak testing
- Free cooling mode functional testing

### Field Quality Control

**Welding:**
- Certified welders (AWS D1.1 qualification)
- Visual inspection + NDT (non-destructive testing) for structural welds

**Electrical:**
- Torque verification on all connections (torque wrench with calibration certificate)
- Insulation resistance (megger) testing before energization
- Infrared thermography after energization (identify hot spots)

**Mechanical:**
- Hydrostatic testing of chilled water piping (1.5× operating pressure, 2-hour hold)
- Refrigerant leak testing (nitrogen pressure test + electronic leak detection)
- Balance and test of HVAC systems (TAB report by certified agency)

---

## 01 50 00 - TEMPORARY FACILITIES & CONTROLS

### Site Logistics

**Construction Office:** On-site trailer for general contractor (minimum 500 SF)
**Staging Areas:** Designated laydown areas for materials and equipment
**Security Fencing:** 8 ft chain-link perimeter fencing with controlled access gates

### Temporary Utilities

**Temporary Power:**
- Construction power service (separate from permanent service)
- Load center with GFCI protection for all receptacles
- Lighting for night work and security

**Temporary Water:**
- Potable water for construction use
- Hydrostatic testing supply for mechanical systems

**Site Security:**
- 24/7 surveillance cameras at entry points and material staging areas
- Sign-in/sign-out logs for all personnel
- Badge access for sensitive areas (electrical rooms, IT spaces)

### Protection of Work

**Equipment Protection:**
- Weather protection for stored electrical equipment (generators, UPS, switchgear)
- Environmental controls for installed equipment during construction
- Dust barriers during fit-out phases (critical for data halls)

---

## 01 60 00 - PRODUCT REQUIREMENTS

### Data Center-Specific Standards

**Uptime Institute Standards:**
- Tier III topology requirements (concurrent maintainability)
- Documentation standards for Tier certification

**ASHRAE Standards:**
- TC 9.9: Data center thermal guidelines (64-78°F, 40-60% RH)
- 90.1: Energy efficiency for HVAC and lighting systems

**TIA Standards:**
- TIA-942: Data center infrastructure standards
- TIA-568: Structured cabling standards

### Material Requirements

**Electrical Equipment:**
- UL listing required for all electrical distribution equipment
- NEMA ratings appropriate for environment (NEMA 1 indoor, NEMA 3R outdoor)
- Seismic certification per IBC requirements for seismic zone

**Mechanical Equipment:**
- AHRI certification for chillers and CDUs
- ETL or UL listing for pumps and fans
- FM-approved fire suppression components

**Fire Protection:**
- UL/FM-listed fire alarm and detection equipment
- NFPA-compliant suppression systems

---

## 01 70 00 - EXECUTION

### Phased Execution

**Phase 1 Priority:**
- Core infrastructure (electrical distribution, mechanical systems)
- Data hall shell and critical MEP systems
- White space fit-out for initial 20,000 SF

**Phase 2+ Expansion:**
- Just-in-time (JIT) deployment of additional UPS capacity
- Additional white space fit-out as leased
- Modular chiller blocks added per load requirements

### Cutting and Patching

**Coordination Required:**
- No cutting of structural members without engineer approval
- Fire-rated assemblies: Restore rating with approved firestopping systems
- MEP penetrations: Coordinate with BIM model before cutting

### Protection of Installed Work

**Critical Equipment Protection:**
- Dust barriers during adjacent construction (protect installed IT equipment)
- HVAC filtration during construction (prevent contamination of data halls)
- Access restrictions to energized electrical rooms

### Progress Cleaning

**Requirements:**
- Daily cleanup of construction debris
- Final cleaning before equipment installation
- Pre-commissioning cleaning (remove all dust, debris from mechanical/electrical systems)

---

## 01 91 00 - COMMISSIONING

### Pre-Functional Testing

**Electrical Systems:**
- **UPS:** Load bank testing at 25%, 50%, 75%, 100%, 110% rated load
- **UPS Bypass:** Manual and automatic bypass operation verification
- **Generators:** No-load, 25%, 50%, 75%, 100% load testing
- **Generator ATS:** Automatic transfer from utility to generator (<15 seconds)
- **Busway:** Continuity, insulation resistance, torque verification

**Mechanical Systems:**
- **Chillers:** Full-load performance testing at design conditions
- **Free Cooling:** Verify automatic mode transitions (free → partial → mechanical)
- **Pumps:** VFD operation, pressure setpoint control
- **CDUs:** Flow rate verification, temperature control testing
- **RDHx:** Rack-level cooling verification (supply/return delta-T)

**Controls & Monitoring:**
- **BMS:** Point-to-point verification (sensors, actuators, alarms)
- **DCIM:** Power monitoring accuracy, trending, reporting
- **EMS:** Solar + generator + utility coordination testing
- **Fire Alarm:** Detector response, alarm notification, suppression activation

### Integrated Systems Testing (IST)

**Purpose:** Verify interaction between electrical, mechanical, controls, fire, and security systems

**IST Scenarios:**

**Scenario 1: Utility Outage (Grid Failure)**
- **Sequence:** Utility power lost → UPS maintains load → Generators start → ATS transfers to generators
- **Verification:** Zero interruption to IT load, generator startup <15 seconds
- **Duration:** Sustained generator operation for 4 hours minimum

**Scenario 2: UPS Failure (Single Module)**
- **Sequence:** UPS module taken offline (simulated failure) → Remaining modules pick up load
- **Verification:** No interruption to IT load, automatic load redistribution
- **Concurrent Maintainability:** Verify module can be serviced while system operates

**Scenario 3: Chiller Failure (N+1 Verification)**
- **Sequence:** Single chiller taken offline → Remaining chillers pick up load
- **Verification:** Data hall temperature remains within limits (<78°F)
- **Duration:** Sustained operation at design load for 2 hours minimum

**Scenario 4: Fire Alarm Activation**
- **Sequence:** Fire alarm triggered → Suppression system activation → HVAC shutdown (if required) → Security doors unlock
- **Verification:** Life safety systems respond correctly, no compromise to IT operations

**Scenario 5: Solar + Generator Coordination**
- **Sequence:** Solar generation fluctuates → Utility import adjusts automatically → Generator starts during utility outage while solar active
- **Verification:** Seamless transitions, no reverse power flow

**IST Acceptance Criteria:**
- All scenarios pass without IT load interruption
- All redundancy verified (N+1 operation demonstrated)
- All alarms and notifications function correctly
- Systems return to normal operation automatically

### 72-Hour Full-Load Test

**Scope:** Operate facility at full design load for 72 continuous hours

**Test Conditions:**
- IT load: Full rated capacity (simulated with load banks if not fully leased)
- HVAC: Design outdoor conditions (or simulated)
- Generators: Minimum 4-hour sustained run during test period
- Monitoring: Continuous data logging of all critical parameters

**Acceptance Criteria:**
- PUE ≤ 1.3 at full load (target 1.2-1.3)
- Data hall temperature: 64-78°F (ASHRAE A1 envelope)
- Data hall humidity: 40-60% RH
- No equipment failures or alarms
- All systems operate within design parameters

### Commissioning Authority (CxA)

**Role:** Independent third-party verification of systems performance and Tier III compliance

**CxA Responsibilities:**
- Review design documents for Tier III compliance
- Witness factory acceptance testing (FAT) for major equipment
- Develop and execute commissioning test procedures
- Observe and document all pre-functional and IST testing
- Prepare final commissioning report with Tier III verification

**Commissioning Report Contents:**
- Executive summary of Tier III compliance verification
- Test procedures and results for all systems
- Deficiency list and resolution status
- O&M manual review and acceptance
- Training completion documentation

### Tier III Verification

**Concurrent Maintainability Verification:**
- [ ] 2N UPS topology with A/B power paths demonstrated
- [ ] All IT equipment dual-corded to separate power paths
- [ ] N+1 redundancy on all other critical systems verified
- [ ] Isolation valves on all mechanical systems functional
- [ ] Manual bypass capability on UPS systems tested
- [ ] Generator paralleling capability verified

**Documentation:**
- Single-line diagrams showing redundant power paths
- Maintenance procedures demonstrating concurrent maintainability
- Test results proving systems operate during maintenance events

**Uptime Institute Certification (Optional):**
Pursue formal certification if required by customers or financing (adds $200-300K to project cost)

---

## 01 78 00 - CLOSEOUT SUBMITTALS

### Operation & Maintenance (O&M) Manuals

**Equipment Manuals:**
- Manufacturer operation and maintenance instructions
- Parts lists and recommended spare parts inventory (initial procurement quantities)
- Warranty information and service contact details
- Troubleshooting guides and fault code references

**System Manuals:**
- Start-up and shutdown procedures
- Emergency procedures (utility outage, fire, equipment failure)
- Calibration and testing procedures

**As-Built Drawings:**
- CAD files in owner's standard format
- PDF files for all disciplines (electrical, mechanical, civil, structural)
- Redlined marked-up drawings showing all field changes

**Controls Documentation:**
- BMS programming and control sequences
- DCIM configuration and user guides
- EMS logic diagrams (solar + generator coordination)
- Setpoints and alarm thresholds

**Format:**
- Hard copy binders: 3 complete sets
- Digital format: PDF files organized by system
- Cloud access: O&M portal for 24/7 remote access

### Warranty Documentation

**Standard Warranties:**
- General construction: 1 year from substantial completion
- Roofing: 20-year manufacturer warranty
- UPS: 1 year parts and labor, 10-year battery warranty
- Generators: 1 year or 2,000 hours parts and labor
- Chillers: 1 year parts and labor, 5-year compressor warranty
- Switchgear/Distribution: 1 year parts and labor

**Extended Warranty Evaluation:**
Contractor to provide pricing for extended warranty options (5-year, 10-year) for owner evaluation

### Equipment Records

**Required Information:**
- Serial numbers, model numbers, installation dates
- Warranty start dates and expiration dates
- FAT/SAT test results and commissioning data
- Service history during construction/commissioning period

### Project Closeout Checklist

- [ ] All punch list items completed
- [ ] All systems commissioned and accepted
- [ ] O&M manuals delivered (hard copy + digital)
- [ ] As-built drawings delivered
- [ ] Training completed for all operators
- [ ] Initial spare parts delivered and inventoried
- [ ] Warranties activated and documented
- [ ] Final payment released
- [ ] Certificate of occupancy obtained

---

## 01 79 00 - DEMONSTRATION AND TRAINING

### Owner Operator Training

**Training Requirements:**
- On-site training: 40 hours minimum (1 week)
- Hands-on operation with all systems
- Video recordings of critical procedures
- Written training materials provided with O&M manuals

**Training Topics by System:**

**Electrical Systems:**
- UPS: Normal operation, monitoring, alarm response, manual bypass procedures, battery maintenance
- Generators: Startup, paralleling, load sharing, fuel system operation, ATS operation
- Distribution: Switchgear operation, breaker racking, safety procedures

**Mechanical Systems:**
- Chillers: Operation and mode transitions (free cooling), BMS interface, control sequences
- Pumps/CDUs: VFD operation, setpoint adjustments, troubleshooting
- Water Systems: Treatment procedures, makeup operation

**Controls & Monitoring:**
- BMS: Interface navigation, alarm response, setpoint changes
- DCIM: Power monitoring, capacity planning, reporting
- EMS: Solar + generator coordination, energy optimization

**Fire & Life Safety:**
- Fire alarm panel operation
- Suppression system manual activation/abort procedures
- Pre-action system valve operation
- Evacuation procedures

**Training Documentation:**
- Attendance logs with operator signatures
- Training completion certificates
- Video library of critical procedures for future reference

---

**Tags:** #saga-project #commissioning #testing #quality-control #csi-division-01

**Related Documents:**
- [[_BOD - Exec Summary and TOC]] - Main title page
- [[0BOD - Procurement and Contracting (CSI Div 00)]] - Contracting strategy
- [[7BOD - Electrical (CSI Div 26)]] - UPS and generator testing requirements
- [[5BOD - HVAC (CSI Div 23)]] - Chiller commissioning requirements
- [[6BOD - Integrated Automation (CSI Div 25)]] - BMS and DCIM commissioning
