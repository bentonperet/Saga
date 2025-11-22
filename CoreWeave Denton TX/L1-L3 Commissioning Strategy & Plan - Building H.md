# L1-L3 Commissioning Strategy & Plan
## CoreWeave Denton South - Building H

**Created:** 2025-11-19
**Project:** CoreWeave Denton South Data Center
**Location:** 8151 Jim Christal Road, Denton, TX 76207
**Building:** Building H
**Tags:** #commissioning #electrical #data-center #L1-L3

---

## Executive Summary

This document outlines the Level 1 through Level 3 (L1-L3) commissioning strategy and detailed test plan for Building H electrical distribution systems at the CoreWeave Denton South data center. The facility features a complex 34.5kV medium-voltage distribution system serving multiple power blocks with diverse operational requirements.

### System Overview

**Building H Power Infrastructure:**
- **GPU Mechanical Blocks (MA):** 8 blocks (SWBD-MA-01H through MA-08H)
- **Mechanical Blocks (MB):** 3 blocks (SWBD-MB-01H through MB-03H) with generator backup
- **GPU Power Blocks (PA):** 18 blocks (SWBD-PA-01H through PA-18H)
- **IT Power Blocks (PB):** 6 blocks (SWBD-PB-01H through PB-06H) with generator backup
- **GPU Reserve Block (RA):** 1 block (SWBD-RA-01H)

**Key Electrical Parameters:**
- Primary Voltage: 34.5kV (Medium Voltage)
- Secondary Voltage: 415/240V, 3-phase, 4-wire
- UPS Systems: 250kVA to 1250kVA, lithium-ion battery backup (5 min EOL)
- Generators: 1250kW diesel generators (parallel operation for 2500kW)
- Main Transformers: 2550kVA to 3000kVA ONAN/ONAF

---

## 1. Commissioning Level Definitions

### Level 1 (L1) - Factory Testing
- **Scope:** QA/QC review of factory test deliverables (factory witness testing NOT in our scope)
- **Responsibility:** Equipment manufacturers conduct testing; CxA reviews deliverables
- **Deliverables:** Factory test reports, certifications, shipping documentation

### Level 2 (L2) - Installation Verification
- **Scope:** Field verification of installation, startup, and functional testing
- **Responsibility:** Installing contractor with CxA oversight
- **Deliverables:** Installation checklists, startup reports, functional test results

### Level 3 (L3) - Integrated Systems Testing
- **Scope:** Full system integration, performance verification, reliability testing
- **Responsibility:** Commissioning Authority with operations team training
- **Deliverables:** Integrated test reports, O&M manuals, training completion records

---

## 2. Commissioning Strategy by System Type

### 2.1 GPU Mechanical Blocks (SWBD-MA-01H through MA-08H)

**System Configuration:**
- 4000A main switchboard (415/240V)
- 3000kVA transformer (34.5kV-415V)
- Three 250kVA/250kW UPS units in parallel operation
- Lithium-ion battery systems (5-minute runtime)
- Three air-cooled chillers (ACC)
- Three chilled water pumps (75HP each) with VFDs
- Fan wall systems (6 fans per block)
- Static transfer switches (STS) for GPU power feeds

**Commissioning Phases:**

#### Phase 1: Pre-Energization (L2)
1. **Physical Inspection**
   - Verify transformer installation per nameplate and drawings
   - Inspect all breaker installations, ratings, and settings
   - Verify UPS equipment installation and battery connections
   - Check all cable terminations and torque values
   - Inspect grounding and bonding systems
   - Verify mechanical equipment installation (chillers, pumps, fans)

2. **Documentation Review**
   - Review transformer test reports (34.5kV-415V, 3000kVA)
   - Verify UPS factory acceptance test (FAT) reports
   - Check switchboard short-circuit test reports (100kAIC rating)
   - Review VFD factory settings and parameters
   - Confirm protective relay settings calculations

3. **Insulation Resistance Testing**
   - Medium-voltage cables: Minimum 100 MΩ at 2.5kV DC
   - Low-voltage feeders: Minimum 10 MΩ at 500V DC
   - UPS input/output circuits
   - Battery strings and DC distribution

#### Phase 2: Initial Energization (L2)
1. **Transformer Energization**
   - Verify transformer oil quality and levels
   - Perform transformer turns ratio testing
   - Measure primary and secondary voltages
   - Check phase rotation and voltage balance
   - Verify neutral-ground bonding

2. **Switchboard Energization**
   - Energize main switchboard (SWBD-MA-01H)
   - Verify voltage at main bus (415V ±5%)
   - Check power quality metering (PQM) functionality
   - Test surge protective devices (SPD)
   - Verify all circuit breaker operations

3. **UPS System Startup**
   - Perform UPS pre-startup inspections
   - Energize UPS input breakers (400A MIB)
   - Verify UPS normal mode operation
   - Test maintenance bypass operation
   - Verify parallel operation of three 250kVA units
   - Battery discharge test (verify 5-minute runtime at 100% load)

#### Phase 3: Load Testing (L2-L3)
1. **Mechanical Equipment Testing**
   - **Chillers (ACC-MA-01H-1/2/3):**
     - Verify 1200A feeder capacity
     - Test communication modules
     - Verify remote monitoring integration

   - **Chilled Water Pumps:**
     - VFD parameter verification
     - Motor rotation and current draw
     - Flow and pressure verification
     - Speed control testing

   - **Fan Walls:**
     - Individual fan motor testing (70A feeders)
     - Control sequence verification
     - Airflow measurements

2. **Static Transfer Switch Testing**
   - Load bank connection verification
   - Transfer time measurement (<10ms)
   - Preferred source priority
   - Retransfer delay settings
   - Multiple transfer/retransfer cycles

#### Phase 4: Integrated Systems Testing (L3)
1. **Full System Integration**
   - Simultaneous operation of all loads
   - UPS load sharing verification
   - Cooling system capacity verification
   - Power quality monitoring under full load

2. **Failure Mode Testing**
   - UPS single module failure
   - Chiller failure scenarios (N+1 redundancy)
   - STS automatic transfer on UPS failure
   - Power quality disturbance response

---

### 2.2 Mechanical Blocks with Generator Backup (SWBD-MB-01H/02H/03H)

**System Configuration:**
- 4000A main switchboard (415/240V)
- 2550-3000kVA transformer (34.5kV-415V)
- Three 250kVA/250kW UPS units in parallel
- Two 1250kW diesel generators (parallel for 2500kW total)
- Power Switchgear (PSG) with ATS functionality
- Three chillers and three CHW pumps
- Fan wall systems (7 fans per block)

**Additional Commissioning Requirements:**

#### Generator System Testing (L2-L3)
1. **Pre-Start Inspections**
   - Verify fuel system installation and capacity
   - Check cooling system and radiator installation
   - Inspect exhaust system installation
   - Verify battery charger and starting batteries
   - Check control panel wiring and settings

2. **Generator Startup & Load Testing**
   - No-load operation and stability test (30 minutes)
   - Step-load testing: 25%, 50%, 75%, 100% load
   - Load bank testing at rated capacity (1250kW per generator)
   - Parallel operation testing (2500kW combined)
   - Voltage and frequency regulation verification (±5%, ±0.5Hz)
   - Transient response testing (sudden load application/rejection)

3. **Automatic Transfer Switch (ATS) Testing**
   - Normal to emergency transfer time (<10 seconds)
   - Utility restoration retransfer delay (30 minutes typical)
   - Transfer under various load conditions (0%, 50%, 100%)
   - Multiple transfer/retransfer cycles (minimum 10 cycles)
   - Generator synchronization and load sharing

4. **Generator-UPS Coordination**
   - Generator supplying UPS loads through bypass
   - UPS response to generator frequency variations
   - Load transition from utility to generator to UPS
   - Battery charging from generator source

---

### 2.3 GPU Power Blocks (SWBD-PA-01H through PA-18H)

**System Configuration:**
- 4000A main switchboard (415/240V)
- 3000kVA transformer (34.5kV-415V)
- Two 1250kVA/1250kW UPS units in parallel
- Four 800A static transfer switches (STS-PA-01H-1/2/3/4)
- Four 800A busway sections (BUS-PA-01H-1/2/3/4)
- Feeds to GPU racks via STS for high availability

**Critical Testing Requirements:**

#### GPU Power Continuity Testing (L3)
1. **STS Performance Verification**
   - Transfer time measurement with GPU load simulation
   - Voltage sag tolerance testing
   - Frequency deviation response
   - Multiple rapid transfers (stress testing)

2. **Load Bank Testing**
   - 800A per busway section verification
   - Voltage drop measurements at full load
   - Thermal imaging of connections under load
   - Power quality monitoring (THD, voltage regulation)

3. **Reserve Power Integration (SWBD-RA-01H)**
   - Bus-tie configuration to reserve block
   - Automatic load transfer scenarios
   - N+1 capacity verification across all GPU blocks

---

### 2.4 IT Power Blocks (SWBD-PB-01H through PB-06H)

**System Configuration:**
- 4000A main switchboard (415/240V)
- 2550-3000kVA transformer (34.5kV-415V)
- Two 1250kVA/1250kW UPS units in parallel
- Two 1250kW diesel generators (parallel for 2500kW)
- Ten 600A busway sections (BUS-PB-##H-1 through 10)
- DOAS (Dedicated Outdoor Air System) with humidification

**Specialized Testing:**

#### IT Load Distribution Testing (L3)
1. **Balanced Load Verification**
   - Load distribution across 10 busway sections
   - Voltage balance between phases (<2% deviation)
   - Neutral current monitoring
   - Harmonic distortion measurement (THD < 5%)

2. **HVAC Integration Testing**
   - DOAS startup and control sequence
   - Humidifier operation and control
   - 480V step-up transformer testing (XFMR-MECH-PB-##H)
   - Coordinated operation with IT cooling loads

---

## 3. Detailed Test Procedures

### 3.1 Medium Voltage Distribution Testing

#### MV Transformer Testing (L1/L2)
**Factory Tests (L1) - Review Only (NOT witness in our scope):**
- QA/QC review of factory test reports including:
  - Ratio test per IEEE C57.12.90
  - Polarity and phase relation tests
  - Resistance measurements (winding and insulation)
  - No-load loss and excitation current
  - Load loss and impedance voltage
  - Applied potential tests
  - Induced potential tests
  - Temperature rise tests

**Field Tests (L2):**
- Visual and mechanical inspection
- Insulation resistance (megger) test
- Turns ratio verification
- Polarity test
- Phase rotation verification
- Voltage regulation test under load
- Sound level measurement
- Thermal imaging under load

**Acceptance Criteria:**
- Voltage regulation: ±2.5% from no-load to full-load
- Impedance: 5.75% to 7.5% as specified
- Temperature rise: Within nameplate limits
- Sound level: <65 dBA at 10 feet

---

### 3.2 Low Voltage Switchgear Testing

#### Main Switchboard Testing (L2)
**Visual Inspection:**
- Verify nameplate ratings (4000A, 415/240V, 65-100kAIC)
- Check all breaker installations and ratings
- Inspect bus bar connections and supports
- Verify protective relay installations
- Check metering and instrumentation

**Electrical Tests:**
- Insulation resistance: >10 MΩ at 500V DC
- High-potential test: Per NETA standards
- Primary injection testing of main breakers
- Ground fault protection testing
- Protective relay calibration and settings verification
- Power quality meter commissioning

**Functional Tests:**
- Manual operation of all circuit breakers
- Electrical operation (close/trip) of all breakers
- Interlocking verification
- Communication module functionality (LSIG, RELT, TUM)
- Remote monitoring integration

**Load Tests:**
- Thermal scan at 50%, 75%, and 100% load
- Voltage drop measurements
- Current balance verification
- Power factor measurement

**Acceptance Criteria:**
- All breaker operations: <3 cycles
- Temperature rise: <30°C above ambient
- Voltage balance: Within ±2%
- Ground fault pickup: ±10% of setting

---

### 3.3 UPS System Testing

#### UPS Commissioning Procedure (L2/L3)

**Pre-Startup Inspection:**
1. Verify installation per manufacturer IOM
2. Check input/output/bypass connections
3. Inspect battery installation and connections
4. Verify control power and communications
5. Review factory settings and parameters

**Startup Sequence:**
1. **Static Bypass Mode Operation**
   - Close maintenance bypass breaker (MBB)
   - Verify bypass voltage (415V ±5%)
   - Transfer load to bypass
   - Verify load transfer completeness

2. **Normal Mode Operation**
   - Start UPS in normal mode
   - Verify rectifier operation
   - Check DC bus voltage
   - Monitor inverter output (415V ±2%, THD <3%)
   - Transfer load from bypass to inverter

3. **Battery Testing**
   - Verify battery voltage and temperature
   - Perform discharge test (5 minutes at 100% load minimum)
   - Measure autonomy time
   - Verify recharge characteristics
   - Test low battery alarm and shutdown

4. **Parallel Operation (for multi-module systems)**
   - Synchronize multiple UPS modules
   - Verify load sharing (±5% between modules)
   - Test single module failure scenario
   - Verify automatic load redistribution

**Performance Tests (L3):**
1. **Transfer Tests**
   - Normal to bypass transfer (<10ms)
   - Bypass to normal transfer
   - Transfer under 0%, 50%, 100% load
   - Multiple rapid transfers (10 cycles minimum)

2. **Load Step Response**
   - 0% to 100% load step
   - 100% to 0% load step
   - Monitor voltage regulation (±3%)
   - Monitor frequency stability (±0.5Hz)

3. **Overload Performance**
   - 110% load for 60 minutes
   - 125% load for 10 minutes
   - 150% load for 1 minute
   - Verify overload alarms and transfer to bypass

4. **Battery Autonomy Verification**
   - Full load discharge test
   - Measure actual runtime vs. specified (5 minutes minimum)
   - Monitor voltage sag characteristics
   - Verify low battery warning and shutdown points

**Acceptance Criteria:**
- Output voltage regulation: ±2% steady-state, ±5% transient
- Frequency regulation: ±0.5% steady-state
- Transfer time: <10ms (no dropout)
- THD: <3% with linear load, <5% with nonlinear load
- Efficiency: >95% at 50-100% load
- Battery runtime: ≥5 minutes at 100% load (EOL condition)
- Parallel load sharing: Within ±5%

---

### 3.4 Generator System Testing

#### Diesel Generator Commissioning (L2/L3)

**Pre-Start Inspection:**
1. Verify fuel system prime and leak-free operation
2. Check lubrication oil level and quality
3. Inspect cooling system and radiator
4. Verify battery charger operation and battery condition
5. Check exhaust system installation and support
6. Inspect vibration isolators and mounting
7. Review control panel settings and alarms

**Initial Startup (L2):**
1. **First Start (No Load)**
   - Manual start from control panel
   - Monitor cranking and starting
   - Verify oil pressure rise
   - Check coolant temperature rise
   - Monitor voltage and frequency stabilization
   - Run 30 minutes minimum
   - Verify auto-shutdown functions

2. **Automatic Start Test**
   - Simulate utility failure
   - Verify automatic start sequence
   - Measure time to rated voltage/frequency (<10 seconds)
   - Verify ready-to-load signal
   - Test multiple auto-start cycles

**Load Testing (L2/L3):**
1. **Single Generator Load Test**
   - Connect load bank
   - Apply 25% load for 30 minutes
   - Apply 50% load for 30 minutes
   - Apply 75% load for 30 minutes
   - Apply 100% load (1250kW) for 4 hours minimum
   - Apply 110% load for 2 hours

   **Monitor and Record:**
   - Voltage: 415V ±5%
   - Frequency: 50Hz ±0.5Hz
   - Voltage regulation during load steps
   - Exhaust temperature
   - Coolant temperature
   - Oil pressure
   - Fuel consumption

2. **Parallel Generator Operation**
   - Start both generators
   - Synchronize units
   - Close paralleling breakers
   - Verify load sharing (within ±5%)
   - Test load transfer between units
   - Total load test at 2500kW for 4 hours
   - Single generator failure simulation

3. **ATS Integration Testing**
   - Normal to emergency transfer (full load)
   - Emergency to normal transfer
   - Verify transfer delays and sequences
   - Test under various load conditions
   - Generator synchronization to utility (if applicable)

**Performance Verification (L3):**
1. **Transient Response**
   - Step load: 0% to 100% in one step
   - Step unload: 100% to 0% in one step
   - Measure voltage dip/rise (not to exceed ±20%)
   - Measure frequency dip/rise (not to exceed ±5%)
   - Verify recovery time (<5 seconds)

2. **Continuous Operation Test**
   - 24-hour test at 80% load minimum
   - 4-hour test at 100% load
   - Monitor all parameters continuously
   - Verify fuel consumption vs. manufacturer data
   - Thermal imaging of all connections
   - Vibration monitoring

**Acceptance Criteria:**
- Steady-state voltage: 415V ±5%
- Steady-state frequency: 50Hz ±0.5%
- Voltage regulation (0-100% load): ±10%
- Frequency regulation (0-100% load): ±5%
- Voltage transient recovery: <5 seconds to ±3%
- Parallel load sharing: Within ±5%
- Auto-start time: <10 seconds to ready-to-load
- Continuous operation: 24 hours without fault

---

### 3.5 Static Transfer Switch (STS) Testing

#### STS Performance Verification (L2/L3)

**Installation Verification (L2):**
1. Verify nameplate ratings (800A, 415V, 100% rated)
2. Check input source connections and phasing
3. Inspect output load connections
4. Verify control wiring and communication
5. Review factory settings

**Functional Testing (L2):**
1. **Preferred Source Selection**
   - Configure preferred source priority
   - Verify automatic return to preferred source
   - Test manual override capability
   - Verify source selection logic

2. **Transfer Performance**
   - Source 1 to Source 2 transfer
   - Source 2 to Source 1 transfer
   - Measure transfer time with oscilloscope
   - Monitor load dropout (should be zero)
   - Test at 0%, 50%, 100% load

3. **Transfer Initiation Conditions**
   - Voltage sag (test at various depths: 10%, 20%, 30%)
   - Voltage swell
   - Frequency deviation
   - Phase loss
   - Complete source failure

**Performance Testing (L3):**
1. **Transfer Time Verification**
   - Use oscilloscope to measure precise transfer time
   - Target: <10ms (typical: 4-6ms)
   - Verify no voltage dropout during transfer
   - Test with sensitive electronic loads

2. **Load Testing**
   - Test with GPU load simulators (if available)
   - Test with actual IT equipment (staged approach)
   - Verify no equipment disruption during transfer
   - Thermal imaging at full rated load

3. **Stress Testing**
   - Rapid multiple transfers (100 cycles)
   - Transfer with inrush loads
   - Transfer with maximum rated load
   - Simultaneous multiple STS transfers

**Acceptance Criteria:**
- Transfer time: <10ms break-before-make
- Voltage dropout during transfer: 0%
- Load carrying capacity: 100% of rating continuously
- Temperature rise: <40°C above ambient at full load
- Transfer cycles: 100 minimum without fault

---

### 3.6 Variable Frequency Drive (VFD) Testing

#### VFD Commissioning for Chilled Water Pumps (L2/L3)

**Installation Verification (L2):**
1. Verify VFD nameplate matches specification (75HP pumps)
2. Check input power connections (200A feeders)
3. Inspect output motor connections
4. Verify control wiring and communication
5. Review factory parameter settings

**Startup Procedure:**
1. **Pre-Start Checks**
   - Verify motor insulation resistance (>10 MΩ)
   - Check motor rotation (bump test)
   - Verify mechanical coupling alignment
   - Confirm pump isolation valves are in correct position

2. **Parameter Configuration**
   - Set motor nameplate parameters
   - Configure acceleration/deceleration ramps
   - Set minimum and maximum speed limits
   - Program PID control parameters (if applicable)
   - Configure protective functions

3. **Initial Operation**
   - Start at minimum speed
   - Verify correct rotation direction
   - Monitor motor current
   - Check for vibration and unusual noise
   - Gradually increase speed to maximum

**Performance Testing (L2/L3):**
1. **Speed Control Verification**
   - Test speed response to control signals
   - Verify minimum speed operation
   - Verify maximum speed operation
   - Test speed ramping (acceleration/deceleration)

2. **Motor Performance**
   - Record current at various speeds
   - Verify current limit functionality
   - Check power factor
   - Measure voltage and current balance (<5%)

3. **System Integration**
   - Test control from BMS/SCADA
   - Verify feedback signals (speed, status, alarms)
   - Test start/stop sequences
   - Verify interlocks with related equipment

**Acceptance Criteria:**
- Motor rotation: Correct direction
- Current balance: Within 5% between phases
- Speed range: 0-100% per specification
- Acceleration time: Per programmed ramp
- Control response: <2 seconds to command
- Communication: Successful integration with control system

---

## 4. Integration Testing (L3)

### 4.1 Normal Operations Testing

**Objective:** Verify all systems operate correctly under normal conditions with full load.

**Test Procedures:**

1. **Full Building Load Test**
   - Bring all power blocks online simultaneously
   - Verify MV distribution capacity (34.5kV system)
   - Monitor all transformer loading
   - Verify voltage regulation throughout facility (<3% deviation)
   - Thermal imaging of all major connections

2. **UPS System Integration**
   - All UPS systems operating in normal mode
   - Verify load sharing across parallel modules
   - Monitor harmonic distortion facility-wide
   - Verify battery charging from all sources

3. **Cooling System Integration**
   - All chillers operating (verify N+1 redundancy)
   - CHW pumps under VFD control
   - Fan walls providing required airflow
   - Temperature and humidity within setpoints

4. **Power Quality Monitoring**
   - Monitor THD at all major distribution points
   - Verify voltage regulation under full load
   - Check power factor (target >0.95)
   - Monitor neutral currents for imbalance

**Acceptance Criteria:**
- All equipment operating within nameplate ratings
- Voltage: 415V ±3% at all distribution points
- Frequency: 50Hz ±0.1%
- THD: <5% voltage, <20% current
- Temperature rise: <30°C above ambient
- Redundancy: N+1 verified for critical systems

---

### 4.2 Failure Mode Testing

**Objective:** Verify system resilience and automatic recovery from component failures.

**Test Scenarios:**

1. **Single UPS Module Failure (per power block)**
   - Simulate failure of one UPS module in parallel system
   - Verify automatic load transfer to remaining modules
   - Verify no load disruption
   - Confirm alarms and notifications
   - Test system recovery when failed module restored

2. **Primary Source Failure (Generator-backed blocks)**
   - Simulate utility failure (open main breaker)
   - Verify generator auto-start sequence
   - Verify ATS transfer to emergency power
   - Monitor UPS operation during transfer
   - Confirm load continuity
   - Test utility restoration and retransfer

3. **STS Source Transfer**
   - Simulate failure of primary UPS source
   - Verify automatic transfer to alternate source
   - Measure transfer time and load continuity
   - Verify return to preferred source
   - Test multiple transfer cycles

4. **Chiller Failure (N+1 Testing)**
   - Take one chiller offline
   - Verify remaining chillers absorb load
   - Monitor system temperatures
   - Verify alarm generation
   - Confirm adequate cooling capacity maintained

5. **Transformer Overload**
   - Gradually increase load beyond rated capacity
   - Verify overload alarms (at 80%, 90%, 100%)
   - Monitor temperature rise
   - Verify load shedding or transfer capabilities

**Documentation Requirements:**
- Record all alarm sequences and timing
- Document actual transfer times
- Capture system response characteristics
- Photograph or video critical sequences
- Record all parameter values during events

**Acceptance Criteria:**
- Zero load disruption during all automatic transfers
- Alarm notification within 5 seconds of event
- Automatic recovery successful in all scenarios
- N+1 redundancy maintained throughout
- All protection systems operate as designed

---

### 4.3 Operational Scenario Testing

**Objective:** Verify system performance under real-world operational scenarios.

**Test Scenarios:**

1. **Planned Maintenance Scenarios**
   - UPS module removal for service
   - Generator preventive maintenance
   - Chiller maintenance with system operating
   - Electrical switchgear inspection under load
   - Demonstrate maintenance bypass procedures

2. **Load Growth Scenarios**
   - Simulate 0% to 100% load ramp over 24 hours
   - Verify automatic equipment staging
   - Monitor efficiency at various load levels
   - Verify cooling system response

3. **Emergency Shutdown and Restart**
   - Execute emergency power-down (EPO) procedure
   - Verify all equipment shutdowns safely
   - Perform controlled restart sequence
   - Verify system integrity after restart
   - Document time required for full restoration

4. **Grid Disturbance Response**
   - Simulate voltage sag (70% of nominal)
   - Simulate voltage swell (120% of nominal)
   - Simulate frequency deviation (±2Hz)
   - Verify UPS and STS response
   - Test ride-through capability

**Acceptance Criteria:**
- Maintenance can be performed without system disruption
- Load changes tracked smoothly without alarms
- Emergency shutdown completes in <60 seconds
- Restart sequence completes in <30 minutes
- All protection systems respond appropriately

---

## 5. Test Equipment & Instrumentation Requirements

### 5.1 Required Test Equipment

**Electrical Testing:**
- Megohmmeter (insulation tester): 500V, 1000V, 2500V, 5000V ranges
- Digital multimeter (DMM): True RMS, 0.1% accuracy
- Clamp-on ammeter: 1000A range, True RMS
- Power quality analyzer: Class A per IEC 61000-4-30
- Ground resistance tester: 3-point and clamp-on types
- Phase rotation meter
- Primary injection test set: 0-4000A adjustable
- Relay test set: Multi-function protective relay tester
- Oscilloscope: 4-channel, 100MHz minimum, for STS testing
- Thermal imaging camera: -20°C to 350°C range
- Load banks:
  - 3000kW (minimum) for transformer/generator testing
  - 800kW (minimum) for UPS testing
  - Resistive and reactive (PF 0.8) capability

**Mechanical Testing:**
- Vibration analyzer
- Sound level meter
- Tachometer (for motor speed verification)
- Pressure gauges (for pump testing)
- Flow meters (ultrasonic type preferred)
- Temperature measurement devices (thermocouples, infrared)

**Documentation Equipment:**
- Digital cameras (for installation photos)
- Video camera (for sequence-of-operations recording)
- Laptop computers (for data logging and analysis)
- Label maker (for field verification)

### 5.2 Calibration Requirements

All test equipment must have valid calibration certificates:
- Calibration within 12 months of use
- NIST-traceable calibration
- Calibration certificates provided with test reports

---

## 6. Safety Requirements

### 6.1 General Safety

**Personal Protective Equipment (PPE):**
- Arc-rated clothing (minimum 40 cal/cm² for MV work)
- Electrical-rated gloves (Class 00, Class 0, Class 2, Class 4)
- Hard hats (Class E)
- Safety glasses with side shields
- Steel-toed boots (electrical hazard rated)
- Hearing protection

**Arc Flash Protection:**
- Arc flash hazard analysis completed for all equipment
- Arc flash labels affixed to all equipment
- Appropriate PPE selected based on incident energy
- Limited approach and restricted approach boundaries enforced

**Lockout/Tagout (LOTO):**
- Written LOTO procedures for all equipment
- Group lockout for all L3 testing involving multiple systems
- Energy verification before work begins
- Only authorized personnel remove locks

### 6.2 Work Permits

Required permits for commissioning activities:
- Hot work permits (for thermal imaging and connections)
- Confined space permits (if applicable)
- Electrical safety permits (for all energized work)
- Fall protection permits (for rooftop or elevated equipment)

### 6.3 Emergency Procedures

**Emergency Contacts:**
- Emergency Services: 911
- Facility Safety Manager: [To be determined]
- Electrical Contractor Emergency: [To be determined]
- Commissioning Authority: [To be determined]

**Emergency Response:**
- Emergency eyewash and shower locations identified
- First aid kits readily available
- Fire extinguishers located per NFPA 70E
- Emergency shutdown procedures posted at all major equipment
- Rescue plan for energized electrical work

---

## 7. Documentation & Deliverables

### 7.1 Pre-Commissioning Documentation

**Required Submittals:**
1. Equipment shop drawings and O&M manuals
2. Factory test reports for QA/QC review (transformers, switchgear, UPS, generators)
   - **Note:** Factory witness testing NOT in our scope; QA/QC review of deliverables IS in scope
3. Installation contractor quality control documentation
4. As-built drawings (redlines from construction)
5. Protective relay settings calculations and coordination study
6. Short-circuit and arc flash study
7. Battery sizing calculations
8. Generator load calculations and sizing verification

### 7.2 Commissioning Test Reports

**Format:**
Each test report shall include:
- Test identification and purpose
- Equipment identification and nameplate data
- Test date, time, and personnel
- Environmental conditions
- Test equipment used (with calibration dates)
- Test procedure and acceptance criteria
- Test results (tabular and graphical as appropriate)
- Deviations and deficiencies noted
- Photographs and thermal images
- Conclusions and recommendations
- Sign-off by contractor and CxA

**Test Report Organization:**
- Individual equipment test reports
- System-level test reports
- Integrated systems test reports
- Final commissioning summary report

### 7.3 Training Documentation

**Required Training:**
1. **Operations Training**
   - Normal operations procedures
   - Equipment startup and shutdown
   - Maintenance bypass procedures
   - Emergency procedures
   - Monitoring and alarm response

2. **Maintenance Training**
   - Preventive maintenance procedures
   - Troubleshooting techniques
   - Safety procedures
   - Spare parts identification

**Training Deliverables:**
- Training agendas and attendance rosters
- Training materials and presentations
- Hands-on demonstration records
- Competency verification tests
- Video recordings of key procedures

### 7.4 O&M Manual Contents

**Final O&M Manual shall include:**
1. Table of contents and organization guide
2. Warranty information for all equipment
3. Equipment cutsheets and submittals
4. Manufacturer O&M manuals
5. As-built drawings (electrical, mechanical, control)
6. Preventive maintenance schedules
7. Recommended spare parts lists
8. Safety procedures and arc flash labels
9. Commissioning test reports
10. Training materials
11. Sequence of operations narratives
12. Control system programming and graphics
13. Contact information for manufacturers and service providers

### 7.5 Final Acceptance Package

**Turnover Documentation:**
1. Certificate of Substantial Completion
2. Final Commissioning Report with Executive Summary
3. Deficiency List with resolution status
4. Warranty Start Date documentation
5. Operations and Maintenance Manuals (3 copies + electronic)
6. Training Completion Certificates
7. Spare Parts Inventory
8. Final As-Built Drawings (CAD files + PDFs)
9. Control System Programming Backup
10. Energy Baseline Data

---

## 8. Schedule & Milestones

### 8.1 Commissioning Phases Timeline

**Phase 1: Pre-Functional Testing (L2) - Weeks 1-4**
- Week 1-2: Installation verification and documentation review
- Week 3-4: Pre-energization testing (insulation resistance, continuity, etc.)

**Phase 2: Equipment Startup (L2) - Weeks 5-12**
- Week 5-6: MV transformer energization and testing
- Week 7-8: Switchgear energization and breaker testing
- Week 9-10: UPS startup and battery testing
- Week 11-12: Generator startup and initial load testing

**Phase 3: Functional Performance Testing (L2/L3) - Weeks 13-20**
- Week 13-14: Mechanical equipment startup (chillers, pumps, fans)
- Week 15-16: Static transfer switch testing
- Week 17-18: VFD and motor testing
- Week 19-20: Load bank testing of all power systems

**Phase 4: Integration Testing (L3) - Weeks 21-26**
- Week 21-22: Normal operations testing with full load
- Week 23-24: Failure mode testing
- Week 25-26: Operational scenario testing

**Phase 5: Training & Documentation - Weeks 27-30**
- Week 27-28: Operations and maintenance training
- Week 29-30: Final documentation and turnover

### 8.2 Critical Milestones

| Milestone | Target Date | Description |
|-----------|-------------|-------------|
| Commissioning Kickoff | Week 0 | CxA, contractor, owner meeting |
| Pre-functional Testing Complete | Week 4 | All installation verification complete |
| First Equipment Energized | Week 5 | First transformer energized |
| All UPS Systems Operational | Week 10 | All UPS online and tested |
| Generator Load Testing Complete | Week 12 | All generators tested to full load |
| First Power Block Fully Commissioned | Week 18 | One complete block through L3 |
| All Equipment Commissioned | Week 20 | All blocks through functional testing |
| Integration Testing Complete | Week 26 | All L3 testing complete |
| Training Complete | Week 28 | All operations staff trained |
| Final Turnover | Week 30 | Final acceptance and closeout |

### 8.3 Dependencies & Constraints

**Critical Dependencies:**
- Utility 34.5kV service availability
- Fuel delivery for generator testing
- Load bank availability and scheduling
- IT equipment availability for load simulation
- Weather (for outdoor generator testing)
- Facility occupancy restrictions

**Schedule Constraints:**
- Limited utility outage windows
- Seasonal temperature requirements for thermal testing
- Availability of specialized test equipment
- Coordination with data center construction schedule
- Client operational requirements

---

## 9. Roles & Responsibilities

### 9.1 Commissioning Team Structure

**Owner/Client Representatives:**
- Final approval of all testing and acceptance
- Coordination of facility access and scheduling
- Review of all commissioning documentation
- Participation in training sessions
- Sign-off on final acceptance

**Commissioning Authority (CxA):**
- Overall commissioning management and coordination
- Development of commissioning plan and procedures
- Witness and verification of all L2/L3 testing
- Review of factory test reports (L1)
- Review of contractor test results
- Deficiency tracking and resolution verification
- Training coordination and verification
- Final commissioning report preparation

**General Contractor:**
- Overall project coordination
- Schedule coordination for commissioning activities
- Safety program enforcement
- Access control and security

**Electrical Contractor:**
- Installation quality control
- Pre-functional checklists (L2)
- Equipment startup and initial testing
- Participation in functional and integrated testing
- Deficiency correction
- As-built documentation
- Operator training support

**Equipment Manufacturers/Vendors:**
- Factory testing (L1)
- Startup support and supervision
- Performance testing support
- Training for operations and maintenance
- Warranty documentation
- Technical support during commissioning

**Control System Integrator:**
- BMS/SCADA programming and configuration
- Control sequence verification
- Integration testing support
- Graphics and user interface development
- Operator training for control systems

### 9.2 Communication Protocol

**Regular Meetings:**
- Weekly commissioning progress meetings
- Daily tailboard safety meetings during active testing
- Issue resolution meetings (as needed)

**Reporting:**
- Weekly progress reports from CxA to owner
- Daily field reports during active commissioning
- Immediate notification of critical issues or safety concerns
- Test report distribution within 48 hours of test completion

**Documentation Distribution:**
- All test reports to owner and CxA
- Deficiency reports to responsible contractor
- Training materials to operations team
- Final documentation to owner in electronic and hard copy

---

## 10. Quality Assurance

### 10.1 Test Witnessing Requirements

**Factory Tests (L1) - QA/QC Review Only:**
- **Factory witness testing is NOT in our scope**
- Our scope includes QA/QC review of factory test deliverables for:
  - Transformers (2550-3000kVA)
  - Main switchgear (4000A)
  - UPS systems (250-1250kVA)
  - Generators (1250kW)
  - Static transfer switches (800A)

**Field Tests (L2/L3):**
- All critical tests witnessed by CxA:
  - First energization of all major equipment
  - UPS battery discharge tests
  - Generator load tests
  - Integration testing
  - Failure mode testing

### 10.2 Deficiency Management

**Deficiency Classification:**
- **Critical:** Safety hazard or prevents system operation
- **Major:** Impacts performance or reliability but allows operation
- **Minor:** Documentation or cosmetic issue

**Deficiency Process:**
1. Identify deficiency during testing or inspection
2. Document in deficiency log with photos
3. Assign responsibility for correction
4. Set correction deadline based on classification
5. Verify correction and document
6. Close deficiency in log

**Resolution Timeline:**
- Critical deficiencies: Immediate correction required before proceeding
- Major deficiencies: Correction within 48 hours
- Minor deficiencies: Correction before final turnover

### 10.3 Test Data Validation

**Data Review Process:**
1. Contractor performs test and records data
2. CxA witnesses test and independently verifies readings
3. CxA reviews test report within 48 hours
4. Discrepancies or failures addressed immediately
5. Re-testing performed if acceptance criteria not met
6. Final data incorporated into commissioning report

**Acceptance Criteria:**
- All parameters within manufacturer specifications
- All parameters within design specifications
- All safety systems functional as designed
- All redundancy proven operational

---

## 11. Specific Testing by Power Block Type

### 11.1 SWBD-MA-01H through MA-08H (GPU Mechanical Blocks)

**Configuration Summary:**
- Quantity: 8 blocks (typical)
- Main transformer: 3000kVA (34.5kV-415V)
- UPS: 3 × 250kVA/250kW in parallel
- Mechanical load: 3 chillers, 3 CHW pumps, fan wall (6 fans)
- Critical loads: Four 800A STS feeds to GPU racks

**Block-Specific Test Sequence:**
1. Transformer energization and ratio testing
2. Switchboard energization and breaker testing
3. UPS startup (3 modules) and parallel operation verification
4. Battery discharge test (5 minutes at full load)
5. Chiller startup and capacity verification (coordinated with chiller vendor)
6. CHW pump and VFD functional testing
7. Fan wall operation and control verification
8. STS performance testing with load bank
9. Integrated cooling system performance test
10. Failure mode testing (single UPS failure, single chiller failure)

**Special Considerations:**
- Critical GPU loads require zero-dropout STS transfers
- Thermal management critical for GPU operation
- Power quality monitoring essential (low THD required)

**Acceptance Criteria:**
- All STS transfers <10ms with no load interruption
- UPS parallel operation within ±5% load sharing
- Cooling system maintains design temperatures ±2°F
- Battery runtime ≥5 minutes at 100% load

---

### 11.2 SWBD-MB-01H/02H/03H (Mechanical Blocks with Generators)

**Configuration Summary:**
- Quantity: 3 blocks
- Main transformer: 2550-3000kVA (34.5kV-415V)
- UPS: 3 × 250kVA/250kW in parallel
- Generators: 2 × 1250kW diesel (2500kW combined)
- ATS: Integrated in power switchgear (PSG)
- Mechanical load: 3 chillers, 3 CHW pumps, fan wall (7 fans)

**Block-Specific Test Sequence:**
1. Transformer energization and testing
2. Switchboard and PSG testing
3. Generator pre-start inspection and first start
4. Generator no-load operation (30 minutes each)
5. Generator load bank testing (0-110% load)
6. Parallel generator operation and load sharing
7. ATS functional testing (utility to generator transfer)
8. UPS startup on utility and generator sources
9. Battery discharge test
10. Mechanical equipment startup
11. Integrated load test (building load + generators)
12. Failure mode testing:
    - Utility failure → generator transfer
    - Single generator failure in parallel operation
    - Generator to utility retransfer
    - UPS operation during transfers

**Special Considerations:**
- Generator sizing must account for UPS battery charging loads
- ATS settings must coordinate with UPS transfer times
- Generator synchronization and paralleling critical
- Extended generator runtime testing required (24 hours)

**Acceptance Criteria:**
- Generator voltage: 415V ±5% at all loads
- Generator frequency: 50Hz ±0.5% at all loads
- Parallel load sharing: within ±5%
- ATS transfer time: <10 seconds
- 24-hour continuous operation at 80% load
- UPS seamless operation during all transfers

---

### 11.3 SWBD-PA-01H through PA-18H (GPU Power Blocks)

**Configuration Summary:**
- Quantity: 18 blocks
- Main transformer: 3000kVA (34.5kV-415V)
- UPS: 2 × 1250kVA/1250kW in parallel
- Distribution: 4 × 800A STS with 800A busways
- Reserve power tie: SWBD-RA-01H provides N+1 capacity

**Block-Specific Test Sequence:**
1. Transformer energization and testing
2. Switchboard energization
3. UPS startup (2 × 1250kVA modules) and parallel operation
4. Battery discharge test at full load
5. STS installation verification (4 units per block)
6. Busway installation and connection verification
7. Load bank testing:
   - Each STS at 800A
   - Both UPS modules at full capacity
   - Voltage drop testing through distribution
8. STS transfer testing under load
9. Reserve power block interconnection testing
10. GPU load simulation testing (if equipment available)
11. Power quality monitoring (harmonics, voltage regulation)
12. Failure mode testing:
    - Single UPS module failure
    - STS source transfer
    - Reserve power block activation

**Special Considerations:**
- High harmonic content expected from GPU loads
- Extremely low voltage tolerance for GPU equipment
- Critical uptime requirement (dual source to all loads)
- Reserve block (SWBD-RA-01H) must be tested with multiple primary blocks

**Acceptance Criteria:**
- UPS output voltage: 415V ±2% (tighter than standard)
- UPS output frequency: 50Hz ±0.1Hz
- UPS parallel load sharing: within ±3%
- STS transfer time: <4ms (measured with oscilloscope)
- Voltage drop: <3% from UPS to end of busway at full load
- THD: <5% voltage, <20% current
- N+1 redundancy verified through reserve block testing

---

### 11.4 SWBD-PB-01H through PB-06H (IT Power Blocks with Generators)

**Configuration Summary:**
- Quantity: 6 blocks
- Main transformer: 2550-3000kVA (34.5kV-415V)
- UPS: 2 × 1250kVA/1250kW in parallel
- Generators: 2 × 1250kW diesel (2500kW combined)
- Distribution: 10 × 600A busways
- HVAC: DOAS with humidification (480V system)

**Block-Specific Test Sequence:**
1. Transformer energization and testing
2. Generator testing (per MB block procedures)
3. ATS functional testing
4. Switchboard energization
5. UPS startup and parallel operation
6. Battery discharge testing
7. 480V step-up transformer testing (XFMR-MECH-PB-##H)
8. DOAS startup and control verification
9. Humidifier operation testing
10. Busway testing (10 × 600A feeds)
11. Load distribution testing across 10 busways
12. Integrated testing with IT load simulation
13. Failure mode testing:
    - Utility to generator transfer with IT loads
    - UPS module failure
    - Generator failure in parallel operation

**Special Considerations:**
- IT loads require high power quality
- HVAC integration with IT environment critical
- Balanced load distribution across 10 busways
- Humidity control critical for IT equipment

**Acceptance Criteria:**
- UPS output: 415V ±2%, 50Hz ±0.1%
- Generator operation per MB block criteria
- DOAS maintains temperature ±2°F, humidity ±5% RH
- Load balance across busways: within ±10%
- Voltage balance between phases: <2%
- Neutral current: <20% of phase current at full load

---

### 11.5 SWBD-RA-01H (GPU Reserve Block)

**Configuration Summary:**
- Quantity: 1 block (reserve/redundancy for PA blocks)
- Main transformer: 3000kVA (34.5kV-415V)
- UPS: 2 × 1250kVA/1250kW in parallel
- Distribution: 4000A bus with connections to PA blocks
- Function: Provides N+1 redundancy for GPU power blocks

**Block-Specific Test Sequence:**
1. Transformer energization and testing
2. Switchboard energization
3. UPS startup and parallel operation
4. Battery discharge testing
5. Bus tie connections to SWBD-PA blocks verification
6. Load transfer testing:
   - Reserve block supplying PA-01H STS sources
   - Reserve block supplying PA-02H STS sources
   - Verify capacity to support any single PA block failure
7. Multiple block support testing (if design allows)
8. Integration with all PA blocks
9. Automatic switchover testing (if automatic transfer configured)
10. Manual transfer procedures verification

**Special Considerations:**
- Must demonstrate ability to support any PA block
- Critical for overall facility N+1 redundancy strategy
- May require testing with actual GPU loads
- Coordination with multiple PA blocks essential

**Acceptance Criteria:**
- Capable of supporting full load of any single PA block
- Transfer to reserve power with no load disruption
- UPS performance per PA block criteria
- All interconnection protection properly coordinated

---

## 12. Lessons Learned & Continuous Improvement

### 12.1 Post-Commissioning Review

**Final Review Meeting:**
- Conduct within 30 days of substantial completion
- Attendance: Owner, CxA, contractors, design team
- Review commissioning process effectiveness
- Discuss challenges and solutions
- Identify improvement opportunities

**Topics for Review:**
1. Schedule adherence and delays
2. Test procedure effectiveness
3. Equipment performance vs. expectations
4. Deficiency resolution process
5. Documentation quality and completeness
6. Training effectiveness
7. Safety performance

### 12.2 Performance Monitoring Plan

**First Year Monitoring:**
- Monthly performance data collection
- Quarterly performance reviews
- Annual recommissioning or performance verification
- Energy baseline establishment and monitoring
- Deficiency trend analysis

**Monitored Parameters:**
- Energy consumption (kWh) by system
- Power factor and power quality
- UPS efficiency and battery health
- Generator runtime and fuel consumption
- Cooling system efficiency (kW/ton)
- Temperature and humidity compliance
- Uptime and availability metrics
- Maintenance costs and frequencies

### 12.3 Documentation Updates

**Living Documents:**
- Operating procedures updated based on experience
- O&M manual revisions as needed
- Control sequences refined based on performance
- Training materials updated
- Preventive maintenance schedules adjusted

---

## 13. Appendices

### Appendix A: Test Forms & Checklists
*(To be developed during detailed planning phase)*
- Pre-functional checklists by equipment type
- Functional test forms
- Integrated systems test forms
- Deficiency log template
- Training attendance roster

### Appendix B: Acceptance Criteria Summary Tables
*(To be developed from specifications)*
- Equipment performance criteria
- System performance criteria
- Safety criteria
- Documentation requirements

### Appendix C: Safety Procedures
- Arc flash boundaries and PPE requirements
- LOTO procedures by equipment
- Confined space entry (if applicable)
- Hot work procedures
- Emergency response procedures

### Appendix D: Contact Information
- Owner representatives
- Design team contacts
- Commissioning Authority
- General contractor
- Electrical contractor
- Equipment manufacturers/vendors
- Utility contacts
- Emergency contacts

### Appendix E: Reference Standards
- NETA Acceptance Testing Specifications
- IEEE Standards (C57, 519, 1100, etc.)
- NFPA 70 (NEC) and NFPA 70E
- ASHRAE Guidelines
- Manufacturer specifications
- Project specifications

### Appendix F: Abbreviations & Definitions
- Technical abbreviations
- Commissioning terminology
- Equipment abbreviations from drawings

---

## Document Control

**Revision History:**

| Revision | Date | Description | Author |
|----------|------|-------------|--------|
| 0.1 | 2025-11-19 | Initial draft | CxA Team |

**Distribution List:**
- Owner: CoreWeave
- Commissioning Authority
- General Contractor
- Electrical Contractor
- Design Engineer: Telios, Inc.

**Document Approval:**

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Owner Representative |  |  |  |
| Commissioning Authority |  |  |  |
| Electrical Contractor |  |  |  |
| Design Engineer |  |  |  |

---

**End of Commissioning Plan**