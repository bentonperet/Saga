# Appendix A - Testing Outline Template

**Document Type:** Template
**Version:** 1.0
**Created:** 2025-11-20
**Tags:** #commissioning #testing-outline #level4 #level5 #template

---

## Document Control

| Field | Value |
|-------|-------|
| Project Name | [PROJECT NAME] |
| Project Location | [CITY, STATE] |
| Owner | [OWNER NAME] |
| GC/CM | [CONTRACTOR NAME] |
| CxA | PGCIS / [CxA NAME] |
| AOR/EOR | [ENGINEER NAME] |
| Document Date | [DATE] |
| Revision | 1.0 |

---

## Purpose

This Testing Outline provides a high-level overview of all Level 4 Functional Performance Tests (FPT) and Level 5 Integrated System Tests (IST) to be performed during commissioning. This document:

- Identifies all equipment and systems requiring testing
- Defines test groupings and sequences
- Specifies required test equipment and instrumentation
- Establishes prerequisite dependencies between tests
- Provides estimated durations for scheduling

**Use this template to:**
1. Communicate testing scope to all commissioning team members
2. Coordinate resource requirements (personnel, equipment, load banks)
3. Integrate testing activities into master construction schedule
4. Track testing progress and completion status

---

## Instructions for Use

<!-- @claude When customizing this template:
1. Replace all [BRACKETED PLACEHOLDERS] with project-specific information
2. Add/remove equipment systems based on actual project scope
3. Adjust test durations based on equipment quantities and complexity
4. Update prerequisite dependencies based on project phasing
5. Coordinate with Load Bank and Metering Plan (Appendix B) for equipment requirements
-->

### Step 1: Equipment List Development
Work with GC/CM to develop complete equipment list from:
- Approved electrical one-line diagrams
- Mechanical drawings and schedules
- Controls drawings and points lists
- Equipment submittal register

### Step 2: Test Grouping
Group equipment into logical test sequences:
- By system (e.g., all UPS systems)
- By location (e.g., all Room 101 equipment)
- By discipline (electrical, mechanical, controls)
- By dependencies (upstream to downstream)

### Step 3: Resource Planning
For each test, identify:
- Required personnel (CxA, contractors, vendor techs)
- Test equipment and instrumentation
- Load banks and metering (reference Appendix B)
- Prerequisite tests that must pass first
- Estimated duration

### Step 4: Schedule Integration
Provide completed Testing Outline to GC/CM for integration into master construction schedule at least **40 working days** before Level 4 commencement.

---

## Testing Outline Format

### Test Identification
Each test shall be identified with unique ID:
- **Format:** `[Discipline]-[System]-[Equipment]-[Level]`
- **Examples:**
  - `ELEC-UPS-UPS-01-L4` (Electrical, UPS System, UPS-01, Level 4)
  - `MECH-CHW-PUMP-01-L4` (Mechanical, Chilled Water, Pump-01, Level 4)
  - `CTRL-BAS-INTEGRATION-L5` (Controls, BAS, Integrated System, Level 5)

---

## Project-Specific Testing Outline

<!-- @claude Customize the sections below based on actual project equipment and systems -->

---

## LEVEL 4 - FUNCTIONAL PERFORMANCE TESTS (FPT)

### Summary Statistics

| Category | Quantity | Estimated Duration |
|----------|----------|-------------------|
| Total Equipment Items | [XXX] | [XX] days |
| Electrical Systems | [XX] | [XX] days |
| Mechanical Systems | [XX] | [XX] days |
| Controls/BAS Points | [XXXX] | [XX] days |
| Fire/Life Safety | [XX] | [XX] days |

---

## 1. ELECTRICAL SYSTEMS - LEVEL 4

### 1.1 Medium Voltage Distribution

#### 1.1.1 Medium Voltage Switchgear

| Test ID | Equipment | Description | Prerequisites | Duration | Resources Required |
|---------|-----------|-------------|---------------|----------|-------------------|
| ELEC-MV-SWGR-01-L4 | [MV-SWGR-01] | MV switchgear functional test | L1-L3 complete, NETA testing complete | 4 hrs | CxA, Electrical contractor, Vendor tech |
| ELEC-MV-SWGR-02-L4 | [MV-SWGR-02] | MV switchgear functional test | L1-L3 complete, NETA testing complete | 4 hrs | CxA, Electrical contractor, Vendor tech |

**Test Equipment Required:**
- Power quality analyzer
- Clamp-on ammeters (True RMS, 1000A range)
- Digital multimeters (0.1% accuracy)
- Thermal imaging camera

**Key Test Activities:**
- Breaker operation verification (manual and electrical)
- Protective relay functional testing
- Interlocking verification
- Communication module testing (SCADA/EPMS)
- Power quality monitoring
- Thermal imaging at operating load

---

#### 1.1.2 Medium Voltage Transformers

| Test ID | Equipment | Description | Prerequisites | Duration | Resources Required |
|---------|-----------|-------------|---------------|----------|-------------------|
| ELEC-MV-XFMR-01-L4 | [XFMR-01] | MV transformer performance test | MV-SWGR-01 passed | 3 hrs | CxA, Electrical contractor |
| ELEC-MV-XFMR-02-L4 | [XFMR-02] | MV transformer performance test | MV-SWGR-02 passed | 3 hrs | CxA, Electrical contractor |

**Test Equipment Required:**
- Power quality analyzer
- Infrared thermometer
- Sound level meter
- Voltage/current measurement devices

**Key Test Activities:**
- Voltage regulation under load
- Temperature rise monitoring
- Sound level measurement
- Power quality (harmonics, THD)
- Cooling system operation (fans, radiators)

---

### 1.2 Emergency Power Systems

#### 1.2.1 Diesel Generators

| Test ID | Equipment | Description | Prerequisites | Duration | Resources Required |
|---------|-----------|-------------|---------------|----------|-------------------|
| ELEC-GEN-01-L4 | [GEN-01] | Generator functional performance test | L3 complete, fuel available | 8 hrs | CxA, Electrical contractor, Vendor tech, GC/CM (fuel) |
| ELEC-GEN-02-L4 | [GEN-02] | Generator functional performance test | L3 complete, fuel available | 8 hrs | CxA, Electrical contractor, Vendor tech, GC/CM (fuel) |

**Load Bank Required:**
- Quantity: [X] x [XXXX]kW resistive load banks
- Reactive capability: 0.8 PF
- See Appendix B - Load Bank and Metering Plan

**Test Equipment Required:**
- Power quality analyzer
- Exhaust gas analyzer
- Vibration analyzer
- Sound level meter
- Fuel flow meter

**Key Test Activities:**
- Auto-start sequence verification
- Load acceptance testing (25%, 50%, 75%, 100%, 110%)
- Voltage and frequency regulation
- Transient response (load step changes)
- Parallel operation (if applicable)
- 4-hour continuous run at rated load
- Protective systems and alarms
- Cooling system performance

---

#### 1.2.2 Automatic Transfer Switches (ATS)

| Test ID | Equipment | Description | Prerequisites | Duration | Resources Required |
|---------|-----------|-------------|---------------|----------|-------------------|
| ELEC-ATS-01-L4 | [ATS-01] | ATS functional performance test | Generator tests passed | 4 hrs | CxA, Electrical contractor, Vendor tech |
| ELEC-ATS-02-L4 | [ATS-02] | ATS functional performance test | Generator tests passed | 4 hrs | CxA, Electrical contractor, Vendor tech |

**Test Equipment Required:**
- Oscilloscope (4-channel, 100MHz)
- Power quality analyzer
- Load bank (per Appendix B)

**Key Test Activities:**
- Normal to emergency transfer (with load)
- Transfer time measurement (<10 seconds)
- Emergency to normal retransfer
- Transfer delay settings verification
- In-phase monitor operation
- Multiple transfer cycles (minimum 10)
- Transfer under varying load conditions (0%, 50%, 100%)

---

### 1.3 Uninterruptible Power Systems (UPS)

#### 1.3.1 UPS Modules

| Test ID | Equipment | Description | Prerequisites | Duration | Resources Required |
|---------|-----------|-------------|---------------|----------|-------------------|
| ELEC-UPS-01-L4 | [UPS-01] | UPS functional performance test | L3 complete, battery charged | 6 hrs | CxA, Electrical contractor, Vendor tech |
| ELEC-UPS-02-L4 | [UPS-02] | UPS functional performance test | L3 complete, battery charged | 6 hrs | CxA, Electrical contractor, Vendor tech |

**Load Bank Required:**
- See Appendix B for specific sizing per UPS rating
- Resistive and reactive capability

**Test Equipment Required:**
- Power quality analyzer
- Battery analyzer
- Oscilloscope for transfer time measurement
- Thermal imaging camera

**Key Test Activities:**
- Normal mode operation verification
- Bypass mode operation
- Transfer tests (normal to bypass, bypass to normal)
- Transfer time measurement (<10ms)
- Load step response (0-100%, 100-0%)
- Overload performance (110%, 125%, 150%)
- Input power factor
- Output voltage regulation (±2%)
- Output frequency regulation (±0.5%)
- THD measurement (<3% with linear load)
- Efficiency at 25%, 50%, 75%, 100% load
- Parallel operation (if applicable)
  - Load sharing verification (±5%)
  - Single module failure simulation
  - Automatic load redistribution

---

#### 1.3.2 UPS Battery Systems

| Test ID | Equipment | Description | Prerequisites | Duration | Resources Required |
|---------|-----------|-------------|---------------|----------|-------------------|
| ELEC-BAT-01-L4 | [BATTERY-01] | Battery discharge test | UPS test passed | 8 hrs | CxA, Electrical contractor, Vendor tech |
| ELEC-BAT-02-L4 | [BATTERY-02] | Battery discharge test | UPS test passed | 8 hrs | CxA, Electrical contractor, Vendor tech |

**Load Bank Required:**
- 100% UPS rating for discharge test
- See Appendix B

**Key Test Activities:**
- Battery voltage and temperature verification
- Full load discharge test (to end-of-discharge voltage)
- Runtime measurement (verify ≥ design minutes at 100% load)
- Voltage sag characteristics
- Low battery alarm verification
- Automatic shutdown verification
- Recharge characteristics (time to 90%, time to 100%)
- Individual battery/string measurements

---

### 1.4 Power Distribution Units (PDU) / Switchboards

#### 1.4.1 Main Distribution Switchboards

| Test ID | Equipment | Description | Prerequisites | Duration | Resources Required |
|---------|-----------|-------------|---------------|----------|-------------------|
| ELEC-SWBD-01-L4 | [SWBD-01] | Switchboard functional test | Upstream source available | 4 hrs | CxA, Electrical contractor |
| ELEC-SWBD-02-L4 | [SWBD-02] | Switchboard functional test | Upstream source available | 4 hrs | CxA, Electrical contractor |

**Test Equipment Required:**
- Power quality analyzer
- Thermal imaging camera
- Clamp-on ammeters

**Key Test Activities:**
- All breaker operations (manual and electrical)
- Metering accuracy verification
- Interlocking verification
- Ground fault protection testing
- Power monitoring system integration
- Load testing with thermal imaging (50%, 75%, 100%)
- Voltage balance verification
- Neutral current monitoring

---

### 1.5 Static Transfer Switches (STS)

| Test ID | Equipment | Description | Prerequisites | Duration | Resources Required |
|---------|-----------|-------------|---------------|----------|-------------------|
| ELEC-STS-01-L4 | [STS-01] | STS functional performance test | Dual UPS sources available | 4 hrs | CxA, Electrical contractor, Vendor tech |
| ELEC-STS-02-L4 | [STS-02] | STS functional performance test | Dual UPS sources available | 4 hrs | CxA, Electrical contractor, Vendor tech |

**Load Bank Required:**
- 100% STS rating per unit
- See Appendix B

**Test Equipment Required:**
- Oscilloscope (for transfer time measurement)
- Power quality analyzer
- Thermal imaging camera

**Key Test Activities:**
- Preferred source selection verification
- Source 1 to Source 2 transfer time (<10ms, target <4ms)
- Source 2 to Source 1 transfer time
- Automatic return to preferred source
- Transfer initiation conditions testing:
  - Voltage sag (10%, 20%, 30%)
  - Frequency deviation (±2Hz)
  - Phase loss
  - Complete source failure
- Transfer under load (0%, 50%, 100%)
- Load capacity verification (100% rating)
- Thermal imaging at full load
- Multiple rapid transfer cycles (100 minimum)

---

### 1.6 Busway Systems

| Test ID | Equipment | Description | Prerequisites | Duration | Resources Required |
|---------|-----------|-------------|---------------|----------|-------------------|
| ELEC-BUS-01-L4 | [BUSWAY-01] | Busway system test | Upstream breakers operational | 3 hrs | CxA, Electrical contractor |
| ELEC-BUS-02-L4 | [BUSWAY-02] | Busway system test | Upstream breakers operational | 3 hrs | CxA, Electrical contractor |

**Load Bank Required:**
- Per busway rating
- See Appendix B

**Key Test Activities:**
- Voltage drop measurement (no load vs. full load)
- Tap box connection verification
- Thermal imaging of all joints and connections
- Load capacity verification
- Grounding verification

---

### 1.7 Power Monitoring / EPMS Integration

| Test ID | Equipment | Description | Prerequisites | Duration | Resources Required |
|---------|-----------|-------------|---------------|----------|-------------------|
| ELEC-EPMS-INTEGRATION-L4 | EPMS System | Power monitoring system integration test | All electrical equipment tested | 8 hrs | CxA, Controls contractor, EPMS vendor |

**Key Test Activities:**
- Point-to-point verification (all metered equipment to EPMS)
- Alarm verification and escalation
- Trend data accuracy
- Historical data logging
- Power quality data capture
- Energy consumption calculations
- PUE calculation accuracy
- Dashboard and graphics verification
- User access and permissions
- Report generation

---

## 2. MECHANICAL SYSTEMS - LEVEL 4

### 2.1 Chilled Water Systems

#### 2.1.1 Chillers

| Test ID | Equipment | Description | Prerequisites | Duration | Resources Required |
|---------|-----------|-------------|---------------|----------|-------------------|
| MECH-CHLR-01-L4 | [CHILLER-01] | Chiller functional performance test | L3 complete, CHW system filled | 6 hrs | CxA, Mechanical contractor, Vendor tech |
| MECH-CHLR-02-L4 | [CHILLER-02] | Chiller functional performance test | L3 complete, CHW system filled | 6 hrs | CxA, Mechanical contractor, Vendor tech |

**Test Equipment Required:**
- Ultrasonic flow meter
- Pressure gauges (calibrated)
- Temperature measurement devices
- Power quality analyzer (electrical consumption)

**Key Test Activities:**
- Capacity verification at design conditions
- Efficiency measurement (kW/ton)
- Entering/leaving water temperatures
- Flow rate verification
- Approach temperature verification
- Control sequence verification
- Staging and destaging
- Alarm testing (low flow, high pressure, etc.)
- Safety shutdown testing
- Remote monitoring integration
- N+1 redundancy verification (take one offline, verify others absorb load)

---

#### 2.1.2 Chilled Water Pumps

| Test ID | Equipment | Description | Prerequisites | Duration | Resources Required |
|---------|-----------|-------------|---------------|----------|-------------------|
| MECH-CHWP-01-L4 | [CHW-PUMP-01] | CHW pump functional test | CHW system ready | 3 hrs | CxA, Mechanical contractor |
| MECH-CHWP-02-L4 | [CHW-PUMP-02] | CHW pump functional test | CHW system ready | 3 hrs | CxA, Mechanical contractor |

**Test Equipment Required:**
- Ultrasonic flow meter
- Pressure gauges
- Vibration analyzer
- Power meter

**Key Test Activities:**
- Rotation direction verification
- Flow rate verification at various speeds
- Pressure rise verification
- VFD operation and control
- Speed control response
- Current draw at various speeds
- Power factor verification
- Vibration analysis
- Bearing temperature monitoring
- BAS integration verification

---

#### 2.1.3 Condenser Water Systems (if applicable)

| Test ID | Equipment | Description | Prerequisites | Duration | Resources Required |
|---------|-----------|-------------|---------------|----------|-------------------|
| MECH-CWT-01-L4 | [COOLING-TOWER-01] | Cooling tower functional test | CHW system operational | 4 hrs | CxA, Mechanical contractor, Vendor tech |

**Key Test Activities:**
- Fan operation and control
- Water distribution verification
- Basin heater operation
- Fill and drift eliminator inspection
- Makeup water control
- Blowdown control
- Water treatment system integration

---

### 2.2 Air Handling Systems

#### 2.2.1 Computer Room Air Handlers (CRAH) / Air Handling Units (AHU)

| Test ID | Equipment | Description | Prerequisites | Duration | Resources Required |
|---------|-----------|-------------|---------------|----------|-------------------|
| MECH-CRAH-01-L4 | [CRAH-01] | CRAH functional performance test | CHW available, power available | 4 hrs | CxA, Mechanical contractor |
| MECH-CRAH-02-L4 | [CRAH-02] | CRAH functional performance test | CHW available, power available | 4 hrs | CxA, Mechanical contractor |

**Test Equipment Required:**
- Anemometer / hot wire
- Temperature and humidity sensors
- Pressure gauges
- Sound level meter

**Key Test Activities:**
- Fan operation and VFD control
- Airflow measurement and verification
- Cooling capacity verification
- Temperature and humidity control
- Filter pressure drop measurement
- Control sequence verification
- Alarm testing
- BAS integration verification

---

#### 2.2.2 Fan Walls (if applicable)

| Test ID | Equipment | Description | Prerequisites | Duration | Resources Required |
|---------|-----------|-------------|---------------|----------|-------------------|
| MECH-FANWALL-01-L4 | [FAN-WALL-01] | Fan wall system functional test | Power available | 3 hrs | CxA, Mechanical contractor |

**Key Test Activities:**
- Individual fan motor testing
- VFD operation (all fans)
- Airflow measurement
- Fan staging and destaging
- Control sequence testing
- Redundancy verification (N+X)
- Alarm testing

---

### 2.3 Dedicated Outdoor Air Systems (DOAS) (if applicable)

| Test ID | Equipment | Description | Prerequisites | Duration | Resources Required |
|---------|-----------|-------------|---------------|----------|-------------------|
| MECH-DOAS-01-L4 | [DOAS-01] | DOAS functional performance test | All utilities available | 6 hrs | CxA, Mechanical contractor, Vendor tech |

**Key Test Activities:**
- Outdoor air damper operation
- Heating coil operation (if applicable)
- Cooling coil operation (if applicable)
- Humidification system operation
- Dehumidification operation
- Temperature control
- Humidity control
- Airflow verification
- Energy recovery wheel operation (if applicable)
- Control sequence verification

---

### 2.4 Liquid Cooling Systems (if applicable)

#### 2.4.1 Cooling Distribution Units (CDU)

| Test ID | Equipment | Description | Prerequisites | Duration | Resources Required |
|---------|-----------|-------------|---------------|----------|-------------------|
| MECH-CDU-01-L4 | [CDU-01] | CDU functional performance test | CHW available, facility CHW loop ready | 4 hrs | CxA, Mechanical contractor, Vendor tech |

**Key Test Activities:**
- Pump operation and control
- Heat exchanger performance
- Flow rate control
- Temperature control (facility water to rack)
- Leak detection system
- Alarms and safety systems
- Redundancy verification
- BAS integration

---

### 2.5 Fire Suppression Systems

#### 2.5.1 Pre-Action / Dry Pipe Systems

| Test ID | Equipment | Description | Prerequisites | Duration | Resources Required |
|---------|-----------|-------------|---------------|----------|-------------------|
| FIRE-PREACTION-01-L4 | [PREACTION-01] | Pre-action system functional test | System charged, detection operational | 4 hrs | CxA, Fire protection contractor, AHJ witness |

**Key Test Activities:**
- Detection system verification
- Cross-zone verification
- Pre-action valve operation
- Air compressor operation
- Low air pressure alarm
- Supervisory signal verification
- Waterflow alarm testing
- Integration with fire alarm system
- Manual release testing

---

#### 2.5.2 Clean Agent Systems (if applicable)

| Test ID | Equipment | Description | Prerequisites | Duration | Resources Required |
|---------|-----------|-------------|---------------|----------|-------------------|
| FIRE-CLEANAGENT-01-L4 | [CLEANAGENT-01] | Clean agent system functional test | System charged, detection operational | 4 hrs | CxA, Fire protection contractor, Vendor tech, AHJ witness |

**Key Test Activities:**
- Detection system verification
- Cross-zone verification
- Agent storage pressure verification
- Manual release testing (without discharge)
- Abort switch testing
- Pre-discharge alarm testing
- HVAC shutdown verification
- Door release verification
- Integration with fire alarm system

---

## 3. CONTROLS & MONITORING SYSTEMS - LEVEL 4

### 3.1 Building Automation System (BAS)

| Test ID | Equipment | Description | Prerequisites | Duration | Resources Required |
|---------|-----------|-------------|---------------|----------|-------------------|
| CTRL-BAS-INTEGRATION-L4 | BAS System | BAS integration functional test | All field devices installed and online | 16 hrs | CxA, Controls contractor, BAS vendor |

**Key Test Activities:**
- Point-to-point verification (100% of points)
  - From field device to local control panel
  - From local control panel to BAS server
  - From BAS server to graphical user interface
- Field device calibration verification
- Sensor accuracy verification (spot check with independent instruments)
- Actuator stroke testing
- Control loop tuning verification
- Sequence of operations verification (all modes)
- Alarm generation and escalation
- Trending and data logging
- Graphics and dashboards
- User access and permissions
- Report generation
- Network communications
- Integration with EPMS
- Integration with fire alarm (if applicable)

---

### 3.2 Fire Alarm System

| Test ID | Equipment | Description | Prerequisites | Duration | Resources Required |
|---------|-----------|-------------|---------------|----------|-------------------|
| FIRE-FAS-01-L4 | Fire Alarm System | Fire alarm system functional test | System installed and programmed | 8 hrs | CxA, Fire alarm contractor, AHJ witness |

**Key Test Activities:**
- Device testing (100% of devices)
  - Smoke detectors
  - Heat detectors
  - Manual pull stations
  - Notification appliances (strobes, horns)
- Zone verification
- Alarm sequence verification
- Supervisory signal verification
- Trouble signal verification
- Elevator recall testing
- Door release testing
- HVAC shutdown testing
- Integration with BAS
- Integration with suppression systems
- Remote monitoring verification
- Battery backup testing
- Authority Having Jurisdiction (AHJ) final inspection

---

### 3.3 Access Control / Security Systems (if in scope)

| Test ID | Equipment | Description | Prerequisites | Duration | Resources Required |
|---------|-----------|-------------|---------------|----------|-------------------|
| SEC-ACS-01-L4 | Access Control System | Access control system functional test | System installed and programmed | 6 hrs | CxA, Security contractor |

**Key Test Activities:**
- Card reader functionality (all readers)
- Door locking mechanisms
- Request-to-exit devices
- Door contact verification
- Forced door alarm testing
- Door held open alarm testing
- Access level verification
- Time zone verification
- Anti-passback testing (if applicable)
- Integration with video surveillance (if applicable)
- Remote monitoring and control

---

## 4. SPECIAL SYSTEMS - LEVEL 4 (if applicable)

### 4.1 Fuel Systems

| Test ID | Equipment | Description | Prerequisites | Duration | Resources Required |
|---------|-----------|-------------|---------------|----------|-------------------|
| FUEL-SYSTEM-01-L4 | Fuel System | Fuel system functional test | Tanks filled, generators operational | 4 hrs | CxA, Mechanical contractor, GC/CM |

**Key Test Activities:**
- Fuel transfer pump operation
- Day tank level control
- Day tank high/low level alarms
- Leak detection system
- Fuel quality verification
- Vent system verification
- Spill containment verification

---

### 4.2 Leak Detection Systems

| Test ID | Equipment | Description | Prerequisites | Duration | Resources Required |
|---------|-----------|-------------|---------------|----------|-------------------|
| LEAK-DETECTION-01-L4 | Leak Detection System | Leak detection system functional test | System installed and sensors placed | 3 hrs | CxA, Installing contractor |

**Key Test Activities:**
- Sensor testing (all zones)
- Alarm verification
- Panel operation
- Remote monitoring integration
- Battery backup testing

---

## LEVEL 5 - INTEGRATED SYSTEM TESTS (IST)

### Summary

| Category | Test Count | Estimated Duration |
|----------|-----------|-------------------|
| Total Integrated Tests | [XX] | [XX] days |
| Electrical Integration | [X] | [X] days |
| Mechanical Integration | [X] | [X] days |
| Full Facility Integration | [X] | [X] days |

---

## 5. ELECTRICAL INTEGRATION TESTS - LEVEL 5

### 5.1 Utility Failure and Generator Transfer

| Test ID | Description | Prerequisites | Duration | Resources Required |
|---------|-------------|---------------|----------|-------------------|
| IST-UTIL-FAIL-L5 | Utility failure simulation and automatic generator start/transfer | All L4 electrical tests passed | 8 hrs | CxA, GC/CM, Electrical contractor, Generator vendor, Owner ops team |

**Key Test Activities:**
- Simulate utility failure (open main breaker)
- Verify automatic generator start sequence
- Verify ATS transfer to emergency power
- Verify UPS operation during transfer (no disruption)
- Verify load continuity
- Monitor time to full transfer
- Simulate utility restoration
- Verify automatic retransfer to utility (after time delay)
- Monitor generator cooldown
- Verify all systems return to normal operation

**Acceptance Criteria:**
- Generator auto-start: <10 seconds
- ATS transfer: <10 seconds
- Zero UPS load disruption
- All critical loads maintained
- Clean retransfer to utility
- No alarms or faults

---

### 5.2 UPS Redundancy and Failure Scenarios

| Test ID | Description | Prerequisites | Duration | Resources Required |
|---------|-------------|---------------|----------|-------------------|
| IST-UPS-REDUNDANCY-L5 | UPS module failure simulation in N+1 configuration | All UPS L4 tests passed | 6 hrs | CxA, Electrical contractor, UPS vendor |

**Key Test Activities:**
- Simulate single UPS module failure in parallel system
- Verify automatic load transfer to remaining modules
- Verify zero load disruption
- Verify alarms and notifications
- Monitor system performance under degraded condition
- Verify automatic recovery when module restored
- Test with varying load conditions

**Acceptance Criteria:**
- Zero voltage dropout during failure
- Automatic load sharing within 5 seconds
- All alarms function correctly
- Load sustained by remaining modules
- Clean recovery to normal operation

---

### 5.3 STS Automatic Source Transfer Under Load

| Test ID | Description | Prerequisites | Duration | Resources Required |
|---------|-------------|---------------|----------|-------------------|
| IST-STS-TRANSFER-L5 | STS automatic transfer simulation with critical loads | All STS L4 tests passed | 6 hrs | CxA, Electrical contractor, STS vendor |

**Key Test Activities:**
- Simulate primary UPS source failure
- Verify automatic STS transfer to alternate source
- Measure transfer time with oscilloscope (<10ms)
- Verify zero load disruption
- Test with varying load conditions (25%, 50%, 75%, 100%)
- Verify automatic return to preferred source
- Test multiple rapid transfer cycles
- Simulate various failure modes (voltage sag, frequency deviation, phase loss)

**Acceptance Criteria:**
- Transfer time: <10ms (target <4ms)
- Zero voltage dropout
- All loads remain operational
- Automatic return to preferred source
- No false transfers

---

### 5.4 Full Facility Load Test

| Test ID | Description | Prerequisites | Duration | Resources Required |
|---------|-------------|---------------|----------|-------------------|
| IST-FULL-LOAD-L5 | Full facility electrical load test at design capacity | All electrical L4 tests passed | 24 hrs | CxA, GC/CM, All electrical contractors, All vendors |

**Load Banks Required:**
- See Appendix B for complete facility loading plan
- Coordinate placement to simulate actual load distribution

**Key Test Activities:**
- Ramp all systems to design load over 4-hour period
- Maintain design load for minimum 4 hours
- Monitor all electrical distribution equipment:
  - MV transformers (loading, temperatures)
  - Switchboards (loading, temperatures, voltage drop)
  - UPS systems (efficiency, temperature, harmonics)
  - Generators (if online - fuel consumption, temperatures)
  - All distribution busway (voltage drop, temperatures)
- Power quality monitoring at all major distribution points
- Thermal imaging of all connections under load
- PUE calculation at full load
- Verify all cooling systems respond appropriately

**Acceptance Criteria:**
- Voltage: ±3% at all distribution points
- Frequency: 50/60Hz ±0.1%
- THD: <5% voltage, <20% current
- All equipment within thermal limits (no hotspots >40°C above ambient)
- Power factor: >0.95
- No alarms or faults
- PUE within design parameters

---

## 6. MECHANICAL INTEGRATION TESTS - LEVEL 5

### 6.1 Chilled Water System N+1 Redundancy

| Test ID | Description | Prerequisites | Duration | Resources Required |
|---------|-------------|---------------|----------|-------------------|
| IST-CHW-REDUNDANCY-L5 | Chiller N+1 redundancy verification under load | All chiller L4 tests passed, electrical full load test | 8 hrs | CxA, Mechanical contractor, Chiller vendor |

**Key Test Activities:**
- Bring facility to full cooling load
- Take one chiller offline (simulate failure)
- Verify remaining chillers automatically absorb load
- Monitor space temperatures (should remain within ±5°F of setpoint)
- Verify adequate capacity maintained
- Document recovery time
- Repeat for each chiller in system
- Verify automatic staging/destaging

**Acceptance Criteria:**
- Temperature excursion: <5°F from setpoint
- Automatic staging of remaining chillers
- No alarms or shutdowns
- Return to normal within 15 minutes
- N+1 capacity demonstrated

---

### 6.2 HVAC Control Sequence Verification

| Test ID | Description | Prerequisites | Duration | Resources Required |
|---------|-------------|---------------|----------|-------------------|
| IST-HVAC-CONTROL-L5 | HVAC control sequences under varying load conditions | All mechanical L4 tests passed | 16 hrs | CxA, Mechanical contractor, Controls contractor |

**Key Test Activities:**
- Test control sequences at various cooling loads (25%, 50%, 75%, 100%)
- Verify equipment staging/destaging per sequences
- Verify temperature control loop performance
- Verify humidity control (if applicable)
- Verify economizer operation (if applicable)
- Verify building pressure control
- Verify airflow tracking (supply vs. return)
- Simulate failure scenarios:
  - CRAH/AHU failure
  - Fan failure
  - Valve failure
  - Sensor failure
- Verify BAS responses to all scenarios

**Acceptance Criteria:**
- Temperature maintained within ±2°F of setpoint
- Humidity maintained within ±5% RH of setpoint (if applicable)
- Proper equipment staging/destaging
- All alarms function correctly
- Automatic recovery from failure scenarios

---

### 6.3 Room/Data Hall Heat Rise Test (if applicable)

| Test ID | Description | Prerequisites | Duration | Resources Required |
|---------|-------------|---------------|----------|-------------------|
| IST-HEAT-RISE-L5 | Data hall heat rise test with temporary containment | All mechanical tests passed, temporary containment installed | 24 hrs | CxA, GC/CM, Mechanical contractor, Controls contractor |

**Load Banks Required:**
- Distributed per rack locations to simulate actual IT load
- See Appendix B

**Test Equipment Required:**
- Multiple temperature sensors (rack inlet, rack outlet, room ambient)
- Humidity sensors
- Pressure sensors (room, hot aisle, cold aisle if contained)
- Airflow measurement devices

**Key Test Activities:**
- Install temporary containment per GC/CM plan
- Place load banks in racks to simulate IT load distribution
- Ramp load to design density over 4 hours
- Monitor for minimum 4 hours at full load (prefer 24 hours):
  - Rack inlet temperatures
  - Rack outlet temperatures
  - Hot aisle / cold aisle temperatures (if applicable)
  - Room ambient temperature
  - Humidity
  - Airflow rates
  - Cooling equipment operation
- Calculate return temperature index (RTI)
- Calculate supply heat index (SHI)
- Verify no hot spots
- Verify adequate airflow distribution

**Acceptance Criteria:**
- Rack inlet temperature: Within ASHRAE recommended range (18-27°C / 64-81°F)
- Temperature variation: <5°F between racks
- Humidity: 40-60% RH (or per design)
- No hot spots >5°F above design
- RTI and SHI within acceptable ranges
- Cooling system capacity demonstrated

---

## 7. FULL FACILITY INTEGRATED TESTS - LEVEL 5

### 7.1 Full Facility Operational Readiness Test

| Test ID | Description | Prerequisites | Duration | Resources Required |
|---------|-------------|---------------|----------|-------------------|
| IST-FACILITY-OPS-L5 | 24-hour full facility operational test | ALL L4 tests passed, ALL preliminary L5 tests passed | 24+ hrs | CxA, GC/CM, All contractors, All vendors, Owner ops team |

**Key Test Activities:**
- Operate facility at design capacity for 24 hours continuous
- Monitor all systems continuously:
  - Electrical (voltages, currents, power quality, temperatures)
  - Mechanical (temperatures, pressures, flows, efficiency)
  - Controls (setpoints, sequences, alarms)
  - Fire/life safety (supervisory signals)
- Verify all automatic control sequences
- Verify all monitoring and alarming
- Document system performance:
  - PUE calculation
  - Energy consumption
  - Cooling efficiency (kW/ton)
  - Generator fuel consumption (if running)
  - Water consumption
- Owner operations team shadowing and familiarization

**Acceptance Criteria:**
- 24 hours continuous operation with zero critical alarms
- All systems within design parameters
- PUE within design target
- All monitoring and control systems functional
- Owner operations team trained and comfortable

---

### 7.2 Operational Scenario Testing

| Test ID | Description | Prerequisites | Duration | Resources Required |
|---------|-------------|---------------|----------|-------------------|
| IST-OPS-SCENARIOS-L5 | Operational and emergency scenario testing | Full facility operational test passed | 8 hrs | CxA, GC/CM, All contractors, Owner ops team |

**Scenarios to Test:**

**Scenario 1: Planned Maintenance Simulation**
- UPS module removal for service (maintenance bypass)
- Generator preventive maintenance
- Chiller maintenance with system operating
- Electrical switchgear inspection under load

**Scenario 2: Emergency Shutdown and Restart**
- Execute emergency power-off (EPO) procedure
- Verify all equipment shutdowns safely and in correct sequence
- Perform controlled restart sequence
- Verify system integrity after restart
- Document time required for full restoration

**Scenario 3: Grid Disturbance Simulation**
- Voltage sag (70% of nominal)
- Voltage swell (120% of nominal)
- Frequency deviation (±2Hz)
- Verify UPS and STS ride-through
- Verify generator start (if disturbance persists)

**Scenario 4: Load Growth / Ramp**
- Simulate gradual load ramp 0% to 100% over 4 hours
- Verify automatic equipment staging
- Monitor efficiency at various load levels
- Verify cooling system response

**Acceptance Criteria:**
- Maintenance can be performed without system disruption
- EPO completes in <60 seconds
- Restart sequence completes successfully
- All protection systems respond appropriately
- Load changes tracked smoothly without alarms

---

### 7.3 Deferred / Seasonal Testing (if applicable)

| Test ID | Description | Prerequisites | Target Date | Resources Required |
|---------|-------------|---------------|-------------|-------------------|
| IST-SEASONAL-[XX]-L5 | [Describe seasonal test] | [Prerequisites] | [Season/Date] | [Resources] |

**Note:** Deferred tests require Owner approval and documented schedule per PGCIS Cx Standard Section 3.5.C.

---

## Testing Equipment Summary

### Required Test Equipment and Instrumentation

Based on the testing outlined above, the following test equipment shall be provided and maintained per PGCIS Cx Standard Section 2.1:

#### Electrical Testing Equipment
- [ ] Megohmmeter (5kV range for MV testing)
- [ ] Power quality analyzer (Class A, IEC 61000-4-30)
- [ ] Clamp-on ammeters (1000A range, True RMS) - minimum 6 units
- [ ] Digital multimeters (0.1% accuracy) - minimum 6 units
- [ ] Oscilloscope (4-channel, 100MHz minimum)
- [ ] Primary injection test set (0-4000A)
- [ ] Relay test set
- [ ] Thermal imaging camera (-20°C to 350°C range)
- [ ] Battery analyzer
- [ ] Insulation resistance tester

#### Mechanical Testing Equipment
- [ ] Ultrasonic flow meters
- [ ] Pressure gauges (calibrated)
- [ ] Temperature measurement devices (thermocouples, infrared)
- [ ] Vibration analyzer
- [ ] Sound level meter
- [ ] Anemometer / hot wire
- [ ] Humidity sensors

#### Load Banks
See Appendix B - Load Bank and Metering Plan for complete specifications

#### Calibration Requirements
- All equipment calibrated within 12 months of use
- NIST-traceable calibration
- Calibration certificates provided with test reports

---

## Testing Schedule Integration

### Critical Path Milestones

The following milestones must be integrated into the master construction schedule:

| Milestone | Target Date | Prerequisites |
|-----------|-------------|---------------|
| All Level 1-3 Documentation Complete | [DATE] | All equipment installed and started |
| Level 4 Commissioning Kickoff | [DATE] | L1-3 complete, CxA on-site |
| Electrical Systems L4 Complete | [DATE] | All electrical equipment tested |
| Mechanical Systems L4 Complete | [DATE] | All mechanical equipment tested |
| Controls/BAS L4 Complete | [DATE] | All points verified |
| All L4 Testing Complete | [DATE] | All deficiencies resolved |
| Level 5 Commissioning Start | [DATE] | All L4 passed, Owner approval |
| Full Facility Load Test | [DATE] | All systems operational |
| All L5 Testing Complete | [DATE] | All integrated tests passed |
| Certificate of Cx Completion | [DATE] | Final report submitted |

---

## Coordination Requirements

### Daily Level 4/5 Coordination Meetings
- **Time:** [TIME] daily
- **Location:** [LOCATION]
- **Attendees:** CxA, GC/CM, Installing Contractors, Vendors (as needed), Owner

### Weekly Coordination Meetings
- **Time:** [TIME] weekly
- **Location:** [LOCATION]
- **Attendees:** All commissioning team members per PGCIS Cx Standard

### Two-Week Look-Ahead Schedule
- Issued by CxA every Friday
- Details specific tests scheduled for next 2 weeks
- Identifies required personnel, equipment, and load banks

---

## Testing Completion Tracking

### Completion Status

| System Category | Total Tests | Completed | Pass | Fail | Deferred | % Complete |
|-----------------|-------------|-----------|------|------|----------|-----------|
| MV Distribution | [XX] | 0 | 0 | 0 | 0 | 0% |
| Generators | [XX] | 0 | 0 | 0 | 0 | 0% |
| UPS Systems | [XX] | 0 | 0 | 0 | 0 | 0% |
| STS Systems | [XX] | 0 | 0 | 0 | 0 | 0% |
| Switchboards | [XX] | 0 | 0 | 0 | 0 | 0% |
| Chillers | [XX] | 0 | 0 | 0 | 0 | 0% |
| CHW Pumps | [XX] | 0 | 0 | 0 | 0 | 0% |
| Air Handling | [XX] | 0 | 0 | 0 | 0 | 0% |
| BAS/Controls | [XX] | 0 | 0 | 0 | 0 | 0% |
| Fire/Life Safety | [XX] | 0 | 0 | 0 | 0 | 0% |
| **TOTAL L4** | **[XXX]** | **0** | **0** | **0** | **0** | **0%** |
| **TOTAL L5** | **[XX]** | **0** | **0** | **0** | **0** | **0%** |
| **GRAND TOTAL** | **[XXX]** | **0** | **0** | **0** | **0** | **0%** |

---

## Document Approvals

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Owner |  |  |  |
| Commissioning Authority |  |  |  |
| AOR/EOR |  |  |  |
| GC/CM |  |  |  |

---

## Revision History

| Revision | Date | Description | Author |
|----------|------|-------------|--------|
| 1.0 | [DATE] | Initial Testing Outline | [AUTHOR] |

---

**Related Documents:**
- [[PGCIS Commissioning Standard - Master Specification]]
- [[Appendix B - Load Bank and Metering Plan]]
- [[Commissioning Plan]]
- [[Level 4 Test Procedures]]
- [[Level 5 Test Procedures]]

**Tags:** #testing-outline #commissioning #level4 #level5 #schedule #pgcis