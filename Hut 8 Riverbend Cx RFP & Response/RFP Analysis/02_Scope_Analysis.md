# Hut 8 Riverbend - Detailed Scope Analysis

**Created:** 2025-11-07
**Tags:** #commissioning #scope #technical-analysis #hut8
**Related:** [[01_Executive_Summary]], [[03_Clarifying_Questions]]

---

## Commissioning Level Definitions

### Level 1: Documentation Review & Submittal Review
**Responsibility:** General Contractor performs, CxA oversees
**CxA Activities:**
- Review and approve commissioning plan from GC
- Review equipment submittals for compliance with design intent
- Review pre-installation documentation
- Verify factory test reports
- Review O&M manuals

**Estimated CxA Effort:** 10-15% of total Cx hours

---

### Level 2: Physical Verification & Installation QA
**Responsibility:** General Contractor performs, CxA oversees
**CxA Activities:**
- Site observation of equipment installation
- Verification of equipment nameplate data
- Confirmation of proper installation per manufacturer requirements
- Review installation checklists from GC
- Random spot-checks of installation quality

**Estimated CxA Effort:** 15-20% of total Cx hours

---

### Level 3: Pre-Functional Testing
**Responsibility:** General Contractor performs, CxA oversees
**CxA Activities:**
- Review pre-functional test procedures
- Witness critical start-up procedures
- Review test results and documentation
- Verify system readiness for functional testing
- Punch list development for deficiencies

**Estimated CxA Effort:** 20-25% of total Cx hours

---

### Level 4: Functional Performance Testing, Heat Load Testing & System Level Testing
**Responsibility:** CxA full execution
**CxA Activities:**
- Develop detailed functional test procedures for all systems
- Execute functional performance tests on all commissioned equipment
- Conduct heat load testing
- Perform electrical system level testing
- Perform mechanical system level testing
- Document performance against design criteria
- Coordinate with GC and subcontractors
- Deficiency tracking and re-testing
- Performance verification testing

**Critical Constraint:** Level 4 testing duration per RFP (see clarifications needed)

**Estimated CxA Effort:** 35-40% of total Cx hours

**Systems to be Functionally Tested (per 36 MW block):**

#### Electrical Distribution Systems
- 32 IT Transformers (34.5kV-480V, 2.5 MVA)
- 12 Mechanical Transformers (34.5kV-480V, 5 MVA)
- 23 Ring Main Units
- 2 MV Switchboards
- 32 LV Switchboards (IT) @ 4000A
- 12 LV Switchboards (Mech) @ 5000A
- 113 UPS modules (600kVA each)
- 351 Battery Cabinets

#### Mechanical Cooling Systems
- 27 Chillers (Vertiv OFC)
- 27 Buffer Tanks
- 190 CDUs (all halls)
- 36 CRAH Fan Walls (data halls)
- 11 CRAH Fan Walls (electrical rooms)

#### White Space Distribution (Option 2)
- 160 Rack Power Panels (1000/1200A)
- 7 Remote Distribution Panels (400A)
- 32 CDUs per hall
- 36 CRAH units per hall
- 11 Hot Aisle Containment systems

#### Control Systems & EPMS
- Building Management System integration
- EPMS (Electrical Power Monitoring System)
- Chiller plant controls
- UPS monitoring and controls
- Environmental monitoring systems

---

### Level 5: Integrated Systems Testing (IST)
**Responsibility:** CxA full execution
**CxA Activities:**
- Develop IST scenarios and test scripts
- Execute full-facility integrated tests across electrical and mechanical systems
- Verify system interactions and dependencies
- Test failure mode operations and redundancy
- Simulate emergency scenarios
- Coordinate load bank testing (full facility load)
- Validate automatic transfer schemes
- Test N+1 redundancy scenarios
- Document system performance under integrated operation

**Critical Constraint:** Must be completed within 6-week window per 36 MW block (includes Level 4)

**Estimated CxA Effort:** 15-20% of total Cx hours

**Key IST Scenarios:**

1. **Normal Operation Verification**
   - Full power path verification under load
   - Cooling system operation at design conditions
   - Control system integration validation

2. **Utility Failure Scenarios**
   - Utility loss and generator start
   - UPS transfer and operation
   - Generator load acceptance
   - Utility restoration and transfer back

3. **N+1 Redundancy Verification**
   - Single chiller failure
   - Single transformer failure
   - Single UPS module failure
   - Single generator failure (if applicable)

4. **Mechanical System Integration**
   - Chiller plant optimization
   - Free cooling operation
   - CDU operation and failover
   - CRAH fan wall control integration

5. **Load Bank Testing**
   - UPS capacity verification
   - Generator load acceptance
   - Parallel operation testing
   - Full load sustained operation

6. **Emergency Scenarios**
   - EPO (Emergency Power Off) testing
   - Fire alarm integration
   - Life safety systems coordination

---

## Equipment-Specific Commissioning Requirements

### Medium Voltage Systems (34.5kV)

**Ring Main Units (138 total, ~23 per block)**
- Insulation resistance testing
- Contact resistance measurements
- Protection relay settings verification
- Interlocking verification
- Arc flash calculations validation
- Operational testing (switching sequences)

**MV Switchboards (12 total, 2 per block)**
- High-potential testing
- Primary injection testing of protective relays
- Control power verification
- Metering accuracy verification
- Communication system testing

**MV Transformers (276 total, 44 per block)**
- Turns ratio testing
- Insulation resistance (Megger)
- Power factor/tan delta testing
- Oil quality analysis (if oil-filled)
- Temperature monitoring verification
- Cooling system testing
- Tap changer operation (if applicable)
- Parallel operation verification

---

### Low Voltage Systems (480V)

**LV Switchboards (276 total, 44 per block)**
- Insulation resistance testing
- Protective device settings verification
- Selective coordination validation
- Ground fault testing
- Arc flash labeling verification
- Metering and monitoring verification
- Load balance testing

**UPS Systems (676 total, 113 per block)**
- Acceptance testing per manufacturer specs
- Battery discharge testing
- Transfer time verification
- Parallel redundancy operation
- Static switch testing
- Bypass operation testing
- Efficiency measurements
- Harmonic distortion testing
- Communication and monitoring verification

**Battery Systems (2,104 cabinets, 351 per block)**
- Cell-by-cell voltage testing
- String resistance measurements
- Float voltage verification
- Equalize charge testing
- Temperature monitoring verification
- BMS (Battery Management System) testing
- Load test per IEEE standards

---

### Rack Power Distribution

**Rack Power Panels (960 total, 160 per block for Option 2)**
- Circuit breaker testing
- Ground continuity verification
- Voltage verification at all outlets
- Load balance testing
- Monitoring system integration
- Remote switching operation (if applicable)

**Remote Distribution Panels (40 total, 7 per block for Option 2)**
- Similar testing as Rack Power Panels
- Communication system verification
- Power metering accuracy

---

### Mechanical Cooling Systems

**Chillers (162 total, 27 per block)**
- Factory test report review
- Refrigerant leak testing
- Compressor operation verification
- Condenser performance testing
- Evaporator performance testing
- Control system integration
- Capacity verification via load testing
- Efficiency measurements
- Setpoint verification
- Free cooling operation (if applicable)
- Lead-lag sequencing
- Alarm and safety testing

**Buffer Tanks (162 total, 27 per block)**
- Leak testing
- Level sensor calibration
- Temperature sensor verification
- Isolation valve testing
- Drain and fill procedures

**Cooling Distribution Units - CDU (190 total)**
- Flow rate verification
- Pressure drop testing
- Temperature control verification
- Pump performance testing
- Manifold distribution verification
- Leak detection system testing
- Control system integration
- Rack-level distribution verification

**CRAH Fan Walls (278 total: 214 data hall + 64 electrical room)**
- Airflow measurement and verification
- Fan speed control testing
- Filter pressure drop monitoring
- Temperature and humidity sensor calibration
- Control system integration
- Variable frequency drive (VFD) testing
- Alarm testing
- Lead-lag operation
- Emergency shutdown testing

---

### White Space Systems

**Hot Aisle Containment (65 units for Option 2)**
- Physical installation verification
- Door operation and sealing
- Structural integrity
- Fire damper integration
- Monitoring system integration

---

## Phasing Analysis

### Switchyard Phase (May 2026 - July 2026)

**Systems Commissioned:**
- Utility interconnection equipment
- Main switchyard
- Incoming 34.5kV distribution
- Full 300 MW capacity verification

**Key Activities:**
- Utility coordination and approval
- High voltage testing
- Protection coordination studies validation
- Energization procedures

**Estimated Duration:** 3 months

---

### Data Hall Blocks (August 2026 - February 2027)

**Block 1 (Data Hall 1): Aug 2026 - Sep 2026**
- First deployment - learning curve anticipated
- Establish testing procedures and documentation templates
- Peak staffing required for template development

**Block 2 (Data Hall 2): Sep 2026 - Oct 2026**
- Overlaps with Block 1 completion
- Process refinement
- Efficiency gains expected

**Block 3 (Data Hall 3): Oct 2026 - Nov 2026**
- Three halls potentially active simultaneously
- Maximum staffing requirement period

**Block 4 (Data Hall 4): Nov 2026 - Dec 2026**
- Holiday period considerations
- Staffing availability challenges

**Block 5 (Data Hall 5): Dec 2026 - Jan 2027**
- Year-end/New Year impacts
- Weather considerations (Louisiana)

**Block 6 (Data Hall 6): Jan 2027 - Feb 2027**
- Final block
- Lessons learned application
- Project closeout preparation

---

## Testing Equipment Requirements

### Electrical Testing Equipment
- Megohmmeter (insulation resistance tester) - high voltage capable
- Micro-ohmmeter (contact/bond resistance)
- Power quality analyzer (3-phase)
- Multimeters (multiple)
- Clamp-on ammeters (multiple)
- Infrared cameras (thermography)
- Ground resistance tester
- Relay test sets (protective relay testing)
- High-potential test set
- Battery load test equipment
- Harmonic analyzer
- Load banks (coordinate capacity requirements)

### Mechanical Testing Equipment
- Airflow measurement stations (multiple)
- Pressure gauges and manometers
- Temperature and humidity sensors (calibrated)
- Ultrasonic flow meters
- Refrigerant leak detectors
- Vibration analysis equipment
- Sound level meters
- Psychrometers
- Strobe tachometers

### Documentation Equipment
- Thermal imaging camera
- Digital cameras
- Tablets/laptops for data collection
- Barcode/QR code scanners (asset tracking)

---

## Coordination Requirements

### With General Contractor
- Daily progress meetings during Level 4-5
- Weekly look-ahead schedule coordination
- Deficiency tracking and closeout
- Safety coordination
- Access and logistics coordination

### With Equipment Vendors
- Factory test witness coordination
- Start-up support scheduling
- Warranty activation documentation
- Technical support during testing

### With Owner (Hut 8)
- Weekly progress reporting
- Milestone approvals
- Test witness coordination for key systems
- Documentation delivery schedule

### With Design Team
- Performance criteria clarification
- Design intent verification
- Change order impact assessment

### With Utility
- Switchyard energization coordination
- Load profile coordination
- Emergency procedures alignment

---

## Documentation Deliverables

### Phase-Specific Deliverables

**Planning Phase:**
- Commissioning Plan
- Test procedure library
- Schedule and milestones
- Staffing plan
- Equipment procurement list

**Execution Phase (per block):**
- Weekly progress reports
- Test reports (all levels)
- Deficiency logs and tracking
- RFI log related to commissioning
- Photographic documentation
- Meeting minutes

**Closeout Phase (per block):**
- Final commissioning report
- Systems manual compilation
- Training documentation
- Warranty activation documentation
- As-built test results compilation
- Lessons learned documentation

**Project Closeout:**
- Master commissioning report (all blocks)
- Executive summary
- Outstanding items log
- Operations and maintenance recommendations
- Warranty tracking documentation

---

## Quality Control & Oversight

### GC Oversight Requirements (Levels 1-3)

**Documentation Review:**
- Submittal review logs
- Installation checklist verification
- Pre-functional test procedure review
- Test result validation
- Deficiency tracking

**Site Presence:**
- Periodic site visits during Levels 1-3
- Critical installation witness points
- Start-up procedure witnessing
- Random quality audits

**Estimated Site Presence:** 2-3 days per week during GC Levels 1-3

### CxA Direct Execution (Levels 4-5)

**Site Presence:**
- Full-time presence during functional testing
- Full-time presence during IST
- Off-hours testing coordination as required

**Estimated Site Presence:** 5-6 days per week during Levels 4-5

---

## Risk Factors & Mitigation

### Schedule Risks
- **Risk:** 6-week IST window is aggressive for 36 MW block
- **Mitigation:** Pre-developed test procedures, adequate staffing, equipment pre-positioned

### Overlapping Phases Risk
- **Risk:** Multiple blocks in commissioning simultaneously
- **Mitigation:** Dedicated teams per block, clear role definitions

### Equipment Availability Risk
- **Risk:** Test equipment scheduling conflicts
- **Mitigation:** Adequate equipment inventory, rental backup plans

### GC Coordination Risk
- **Risk:** GC delays in Levels 1-3 impact Level 4 schedule
- **Mitigation:** Early engagement, clear requirements communication, penalty clauses

### Design Changes Risk
- **Risk:** Equipment list subject to change per final engineering
- **Mitigation:** Change order process, scope flexibility in contract

### Weather Risk
- **Risk:** Louisiana weather impacts outdoor testing
- **Mitigation:** Weather contingency in schedule, flexible testing sequences
