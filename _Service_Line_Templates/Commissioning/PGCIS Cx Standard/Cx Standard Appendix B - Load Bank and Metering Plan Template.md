# Appendix B - Load Bank and Metering Plan Template

**Document Type:** Template
**Version:** 1.0
**Created:** 2025-11-20
**Tags:** #commissioning #load-bank #metering #level4 #level5 #template

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

This Load Bank and Metering Plan defines the requirements for load bank equipment and test metering necessary to execute Level 4 Functional Performance Tests (FPT) and Level 5 Integrated System Tests (IST). This plan ensures:

- **Adequate load bank capacity** for all testing scenarios
- **Proper load bank placement** to simulate actual operating conditions
- **Appropriate test metering** to capture accurate performance data
- **Safe connections and operations** per manufacturer requirements and codes
- **Efficient testing execution** through pre-planned logistics

---

## Instructions for Use

<!-- @claude When customizing this template:
1. Replace all [BRACKETED PLACEHOLDERS] with project-specific information
2. Calculate load bank requirements based on actual equipment ratings
3. Coordinate with electrical one-line diagrams for connection points
4. Verify voltage and current ratings match equipment under test
5. Confirm load bank availability and delivery dates with GC/CM
6. Cross-reference with Testing Outline (Appendix A) for test sequencing
-->

### Step 1: Load Bank Sizing
For each piece of equipment requiring load testing:
1. Identify rated capacity (kW, kVA)
2. Determine test load levels (typically 25%, 50%, 75%, 100%, 110%)
3. Size load bank(s) to achieve maximum test load
4. Include reactive capability if testing at non-unity power factor

### Step 2: Connection Planning
For each load bank connection:
1. Identify voltage and phase configuration
2. Determine connection point (breaker, busway tap, etc.)
3. Specify cable size and length required
4. Verify available fault current and breaker coordination
5. Plan for physical placement and ventilation

### Step 3: Metering Requirements
For each test:
1. Determine parameters to be measured (V, A, kW, kVA, PF, THD, etc.)
2. Specify meter type and accuracy class
3. Identify metering connection points
4. Plan for data logging and synchronization

### Step 4: Safety Planning
1. Arc flash assessment for connection/disconnection activities
2. Lockout/tagout procedures
3. Qualified personnel requirements
4. Ventilation requirements for load banks

---

## Responsibilities

Per PGCIS Commissioning Standard Section 1.6:

### GC/CM Responsibilities:
- Provide all load banks and cabling per this plan
- Coordinate load bank delivery to site
- Provide qualified personnel for placement, connection, disconnection, and operation
- Provide all test metering equipment per this plan
- Ensure all equipment has valid calibration certificates

### CxA Responsibilities:
- Develop this Load Bank and Metering Plan
- Direct load bank placement and connection during testing
- Verify proper metering setup
- Monitor test data collection
- Review and validate metering reports

### Installing Contractor Responsibilities:
- Execute load bank connections per CxA direction
- Operate load banks during testing
- Collect and provide metering data
- Ensure safe operations throughout testing

---

## Load Bank Inventory Requirements

### Summary of Load Bank Requirements

| Load Bank Type | Quantity | Capacity Each | Total Capacity | Voltage | Phase | Notes |
|----------------|----------|---------------|----------------|---------|-------|-------|
| Resistive, [XXX]V, 3-phase | [X] | [XXX] kW | [XXX] kW | [XXX]V | 3-phase | For generator/UPS testing |
| Resistive, [XXX]V, 3-phase | [X] | [XXX] kW | [XXX] kW | [XXX]V | 3-phase | For transformer/distribution testing |
| Resistive/Reactive, [XXX]V, 3-phase | [X] | [XXX] kVA @ 0.8PF | [XXX] kVA | [XXX]V | 3-phase | For power factor testing |

**Total Load Bank Capacity Required:** [XXXX] kW / [XXXX] kVA

---

## Load Bank Specifications

### General Requirements

All load banks shall meet the following minimum specifications:

1. **Type:** Trailer-mounted or skid-mounted resistive load banks
2. **Cooling:** Forced air or liquid cooled
3. **Control:** Manual and/or automatic control
4. **Load Steps:** Minimum [XX]kW increments
5. **Accuracy:** ±5% of rated capacity
6. **Metering:** Integral metering (V, A, kW minimum)
7. **Protection:** Overcurrent, overvoltage, overtemperature
8. **Ventilation:** Adequate for indoor or outdoor operation as required
9. **Cables:** Appropriately sized camlock or other approved connectors
10. **Safety:** Emergency stop, clearly marked, proper grounding

### Resistive Load Banks

**Application:** Generator testing, UPS testing, transformer loading, general electrical distribution testing

**Specifications:**
- Power Factor: Unity (1.0)
- Load Steps: [XX]kW minimum increments
- Voltage Range: [XXX-XXX]V
- Frequency: [50/60]Hz
- Control: Local panel with kW setpoint control
- Metering: Digital display of voltage, current, kW

### Resistive/Reactive Load Banks

**Application:** Power factor testing, UPS efficiency testing, generator transient response

**Specifications:**
- Power Factor Range: 0.6 to 1.0 (lagging)
- Resistive Capacity: [XXX] kW
- Reactive Capacity: [XXX] kVAR
- Load Steps: Independently adjustable kW and kVAR
- Control: Local panel with kW and kVAR setpoint controls
- Metering: Digital display of voltage, current, kW, kVAR, kVA, PF

---

## Test Equipment and Metering Requirements

### Power Quality Analyzers

**Quantity Required:** [X] units

**Specifications:**
- Compliance: Class A per IEC 61000-4-30
- Voltage Channels: 4 minimum (3-phase + neutral)
- Current Channels: 4 minimum
- Voltage Range: [XX]V to [XX]V
- Current Range: [XX]A to [XXXX]A (with appropriate CTs or clamps)
- Parameters Measured:
  - RMS voltage and current (all phases + neutral)
  - True power (kW), reactive power (kVAR), apparent power (kVA)
  - Power factor
  - Frequency
  - Total Harmonic Distortion (THD) - voltage and current
  - Individual harmonic content (up to 50th harmonic minimum)
  - Voltage unbalance
  - Current unbalance
  - Flicker
  - Transients and sags/swells
- Data Logging: Continuous logging with configurable intervals (1-second minimum)
- Data Storage: Sufficient for 24+ hours of continuous logging
- Data Export: CSV, Excel, PDF formats
- Display: Real-time waveform display
- Calibration: Valid calibration certificate (<12 months old, NIST traceable)

### Oscilloscope

**Quantity Required:** [X] unit(s)

**Application:** STS transfer time measurement, transient capture

**Specifications:**
- Channels: 4 minimum
- Bandwidth: 100MHz minimum
- Sample Rate: 1 GSa/s minimum
- Memory Depth: 10 Mpts minimum per channel
- Voltage Range: [XX]V to [XXX]V with appropriate voltage probes
- Trigger Modes: Edge, pulse, video
- Data Storage: USB or network transfer capability
- Calibration: Valid calibration certificate

### Clamp-On Ammeters

**Quantity Required:** [X] units (minimum 6 recommended)

**Specifications:**
- Type: True RMS AC
- Range: 1A to 1000A minimum
- Accuracy: ±2% of reading
- Display: Digital, 3½ or 4-digit
- Data Logging: Preferred (for long-duration monitoring)
- Calibration: Valid calibration certificate

### Digital Multimeters (DMM)

**Quantity Required:** [X] units (minimum 6 recommended)

**Specifications:**
- Type: True RMS
- DC Voltage: 0-1000V, ±0.1% accuracy
- AC Voltage: 0-750V, ±0.5% accuracy
- DC Current: 0-10A, ±0.5% accuracy
- AC Current: 0-10A, ±1% accuracy
- Resistance: 0-40MΩ
- Frequency: 1Hz to 100kHz
- Calibration: Valid calibration certificate

### Thermal Imaging Camera

**Quantity Required:** [X] unit(s)

**Specifications:**
- Temperature Range: -20°C to 350°C minimum
- Thermal Sensitivity: <0.1°C
- IR Resolution: 160x120 pixels minimum (320x240 preferred)
- Image Storage: Minimum 500 images
- Data Export: Thermal JPEG with embedded temperature data
- Analysis Software: Included
- Calibration: Valid calibration certificate

### Temperature Measurement Devices

**Quantity Required:** As needed for HVAC/mechanical testing

**Types:**
- Infrared thermometers
- Thermocouple probes (Type K or T)
- RTD sensors
- Wireless temperature sensors

**Specifications:**
- Range: -20°C to 150°C minimum
- Accuracy: ±0.5°C or better
- Data logging capability preferred
- Calibration: Valid calibration certificate

### Flow Meters

**Quantity Required:** As needed for chilled water testing

**Type:** Ultrasonic clamp-on or insertion type

**Specifications:**
- Pipe Size Range: [XX]" to [XX]"
- Flow Range: [XX] to [XXX] GPM
- Accuracy: ±2% of reading
- Display: Digital with totalizer
- Data logging capability
- Calibration: Valid calibration certificate

### Pressure Gauges

**Quantity Required:** As needed for mechanical testing

**Specifications:**
- Range: Appropriate for application (water, refrigerant, air)
- Accuracy: ±1% of full scale
- Display: Analog or digital
- Calibration: Valid calibration certificate

---

## Level 4 Testing - Load Bank and Metering Requirements by Test

<!-- @claude Customize this section based on actual project equipment per Testing Outline (Appendix A) -->

### Generator Testing

#### Test: Generator Load Bank Testing (Each Generator)

**Equipment Under Test:** [GEN-01, GEN-02, etc.]
**Test Reference:** [ELEC-GEN-XX-L4]

**Load Bank Requirements:**
| Load Bank | Capacity | Voltage | Connection Point | Cable Size | Cable Length | Load Levels to Test |
|-----------|----------|---------|------------------|------------|--------------|---------------------|
| LB-1 | [1500] kW | [480]V, 3-ph | Generator output terminal | [500] MCM (per phase) | [50] ft | 0%, 25%, 50%, 75%, 100%, 110% |

**Connection Configuration:**
- Voltage: [480]V, 3-phase, 4-wire
- Connection: Via camlock connectors or approved lugs
- Grounding: Connect load bank frame to equipment ground
- Protection: Generator breaker provides OCP

**Metering Requirements:**
| Parameter | Meter Type | Location | Connection | Sampling Rate |
|-----------|------------|----------|------------|---------------|
| Voltage (3-phase + N) | Power Quality Analyzer | Generator output terminals | Voltage probes | 1 second |
| Current (3-phase + N) | Power Quality Analyzer | Generator output | CTs or clamps | 1 second |
| kW, kVAR, kVA, PF | Power Quality Analyzer | Calculated from V & A | - | 1 second |
| THD (voltage & current) | Power Quality Analyzer | Calculated | - | 1 second |
| Frequency | Power Quality Analyzer | - | - | 1 second |
| Exhaust Temperature | Thermocouple | Exhaust stack | - | 10 seconds |
| Coolant Temperature | From generator control panel | - | - | Via SCADA/manual |
| Oil Pressure | From generator control panel | - | - | Via SCADA/manual |
| Fuel Consumption | Fuel flow meter or tank level | Fuel line or day tank | - | 1 minute |

**Test Procedure:**
1. Connect load bank to generator output (de-energized)
2. Connect metering per table above
3. Verify all connections and safety protocols
4. Start generator per normal procedure
5. Bring online and stabilize at no-load
6. Begin data logging
7. Apply load in increments: 0% → 25% → 50% → 75% → 100% → 110%
8. Hold each load level for minimum [30] minutes (100% load for [4] hours, 110% for [2] hours)
9. Monitor and record all parameters
10. Reduce load to zero
11. Shutdown generator per normal procedure
12. Disconnect load bank and metering (de-energized)

**Safety Considerations:**
- Arc flash hazard: [XX] cal/cm² per approved study
- PPE required: [Specify]
- LOTO procedures: [Reference MOP]
- Ventilation: Ensure adequate exhaust ventilation
- Fuel availability: Verify adequate fuel for duration of test

---

#### Test: Generator Parallel Operation Testing

**Equipment Under Test:** [GEN-01 & GEN-02 in parallel]
**Test Reference:** [ELEC-GEN-PARALLEL-L4]

**Load Bank Requirements:**
| Load Bank | Capacity | Voltage | Connection Point | Cable Size | Cable Length | Load Levels to Test |
|-----------|----------|---------|------------------|------------|--------------|---------------------|
| LB-1 & LB-2 Combined | [3000] kW total | [480]V, 3-ph | Paralleling bus | [750] MCM (per phase) | [75] ft | 0%, 50%, 100% combined |

**Metering Requirements:**
- Individual generator output metering (each generator)
- Paralleling bus metering (combined output)
- Load sharing verification (±5% between generators)

**Test Procedure:**
1. Start both generators
2. Synchronize generators
3. Close paralleling breakers
4. Apply load and verify load sharing
5. Test load transfers between units
6. Simulate single generator failure

---

### UPS System Testing

#### Test: UPS Functional Performance Testing (Each UPS)

**Equipment Under Test:** [UPS-01, UPS-02, etc.]
**Test Reference:** [ELEC-UPS-XX-L4]

**Load Bank Requirements:**
| Load Bank | Capacity | Voltage | Connection Point | Cable Size | Cable Length | Load Levels to Test |
|-----------|----------|---------|------------------|------------|--------------|---------------------|
| LB-3 | [250] kW (or UPS rating) | [480]V, 3-ph | UPS output distribution | [300] MCM | [25] ft | 0%, 25%, 50%, 75%, 100%, 110%, 125%, 150% |

**Resistive/Reactive Load Bank Recommended** for power factor and efficiency testing

**Metering Requirements:**
| Parameter | Meter Type | Location | Connection | Sampling Rate |
|-----------|------------|----------|------------|---------------|
| Input Voltage (3-phase) | Power Quality Analyzer | UPS input | Voltage probes | 0.1 second (for transfer tests) |
| Input Current (3-phase) | Power Quality Analyzer | UPS input | CTs or clamps | 0.1 second |
| Output Voltage (3-phase) | Power Quality Analyzer | UPS output | Voltage probes | 0.1 second |
| Output Current (3-phase) | Power Quality Analyzer | UPS output | CTs or clamps | 0.1 second |
| Input kW, PF | Power Quality Analyzer | Calculated | - | 1 second |
| Output kW, PF | Power Quality Analyzer | Calculated | - | 1 second |
| Efficiency | Calculated (Output kW / Input kW) | - | - | 1 second |
| THD (input & output) | Power Quality Analyzer | Calculated | - | 1 second |
| DC Bus Voltage | From UPS monitoring | - | - | Via UPS display/SCADA |
| Battery Voltage | From UPS monitoring or separate meter | - | - | 1 second |

**Test Procedure:**
1. Connect load bank to UPS output (via UPS output distribution)
2. Connect metering at UPS input and output
3. Verify UPS in normal mode, battery charged
4. Begin data logging
5. Perform the following tests:
   - **Transfer Tests:**
     - Normal to bypass transfer (measure transfer time with oscilloscope - target <10ms)
     - Bypass to normal transfer
     - Test at 0%, 50%, 100% load
     - Multiple rapid transfers (10 minimum)
   - **Load Step Response:**
     - 0% to 100% load step (measure voltage regulation and recovery time)
     - 100% to 0% load step
   - **Steady State Operation:**
     - 25% load for [30] minutes - measure efficiency
     - 50% load for [30] minutes - measure efficiency
     - 75% load for [30] minutes - measure efficiency
     - 100% load for [30] minutes - measure efficiency, THD
   - **Overload Performance:**
     - 110% load for [60] minutes
     - 125% load for [10] minutes
     - 150% load for [1] minute or until UPS transfers to bypass
6. For parallel UPS systems:
   - Verify load sharing (±5%)
   - Simulate single module failure
   - Verify automatic load redistribution
7. Complete data logging
8. Reduce load to zero
9. Disconnect load bank

**Acceptance Criteria:**
- Transfer time: <10ms (no dropout)
- Output voltage regulation: ±2% steady-state, ±5% transient
- Frequency regulation: ±0.5%
- THD: <3% with linear load
- Efficiency: >95% at 50-100% load
- Parallel load sharing: Within ±5%

---

#### Test: UPS Battery Discharge Testing

**Equipment Under Test:** [BATTERY-01, BATTERY-02, etc.]
**Test Reference:** [ELEC-BAT-XX-L4]

**Load Bank Requirements:**
| Load Bank | Capacity | Voltage | Connection Point | Cable Size | Cable Length | Load Level |
|-----------|----------|---------|------------------|------------|--------------|-----------|
| LB-3 (same as UPS test) | [250] kW | [480]V, 3-ph | UPS output | [300] MCM | [25] ft | 100% of UPS rating |

**Metering Requirements:**
| Parameter | Meter Type | Location | Connection | Sampling Rate |
|-----------|------------|----------|------------|---------------|
| Battery String Voltage | DMM or Battery Analyzer | Battery terminals | Direct connection | 1 second |
| Battery String Current | Battery Analyzer or Shunt | Battery DC circuit | Shunt or clamp | 1 second |
| Individual Battery Voltages | Battery Analyzer (multi-channel) | Each battery | Direct probes | 10 seconds |
| Battery Temperature | Thermocouples | Representative batteries | - | 10 seconds |
| UPS Output Voltage | Power Quality Analyzer | UPS output | Voltage probes | 1 second |
| Load (kW) | Power Quality Analyzer | UPS output | From V & A | 1 second |
| Runtime | Timer / data logger timestamp | - | - | - |

**Test Procedure:**
1. Ensure UPS in normal mode, battery fully charged (float voltage achieved)
2. Connect 100% load via load bank
3. Connect all metering
4. Begin data logging
5. Transfer UPS to battery mode (simulate input power loss)
6. Monitor battery discharge:
   - String voltage sag characteristics
   - Current delivery
   - Individual battery voltages
   - Battery temperatures
   - Load continuity (should remain uninterrupted)
7. Continue discharge until one of the following:
   - Low battery shutdown voltage reached
   - Design runtime achieved ([XX] minutes at 100% load)
   - End-of-discharge voltage reached
8. Measure actual runtime achieved
9. Return UPS to normal mode (restore input power)
10. Monitor recharge characteristics:
    - Time to 90% charge
    - Time to 100% charge (float voltage)
    - Recharge current profile
11. Complete data logging

**Acceptance Criteria:**
- Runtime: ≥ [XX] minutes at 100% load (per design)
- Voltage: No individual battery drops below [XX]V
- Temperature: <10°C rise during discharge
- Load: Zero interruption during discharge
- Alarms: Low battery alarm at appropriate time
- Shutdown: Automatic controlled shutdown if end-of-discharge reached
- Recharge: 90% charge within [8] hours

---

### Transformer Loading Testing

#### Test: Transformer Performance Under Load

**Equipment Under Test:** [XFMR-01, XFMR-02, etc.]
**Test Reference:** [ELEC-MV-XFMR-XX-L4]

**Load Bank Requirements:**
| Load Bank | Capacity | Voltage | Connection Point | Cable Size | Cable Length | Load Levels to Test |
|-----------|----------|---------|------------------|------------|--------------|---------------------|
| LB-4 | [3000] kW (transformer rating) | [480]V, 3-ph | Secondary distribution | [750] MCM | [100] ft | 0%, 25%, 50%, 75%, 100% |

**Metering Requirements:**
| Parameter | Meter Type | Location | Connection | Sampling Rate |
|-----------|------------|----------|------------|---------------|
| Primary Voltage | Power Quality Analyzer (MV capable) | Transformer primary | Voltage probes (appropriate for MV) | 1 second |
| Primary Current | Power Quality Analyzer | Transformer primary | CTs | 1 second |
| Secondary Voltage | Power Quality Analyzer | Transformer secondary | Voltage probes | 1 second |
| Secondary Current | Power Quality Analyzer | Transformer secondary | CTs or clamps | 1 second |
| Power (primary & secondary) | Power Quality Analyzer | Calculated | - | 1 second |
| Power Factor | Power Quality Analyzer | Calculated | - | 1 second |
| THD | Power Quality Analyzer | Calculated | - | 1 second |
| Temperature (top oil, windings if available) | Thermocouples or Infrared | Transformer tank, gauges | - | 1 minute |
| Cooling System Operation | Visual / SCADA | Fans, pumps (if applicable) | - | Per system |

**Test Procedure:**
1. Verify transformer energized and in service
2. Connect load bank to secondary distribution
3. Connect all metering (primary and secondary)
4. Begin data logging at no load
5. Apply load in steps: 0% → 25% → 50% → 75% → 100%
6. Hold each load level for minimum [30] minutes
7. At each load level, record:
   - Primary voltage, current, kW
   - Secondary voltage, current, kW
   - Voltage regulation (compare secondary voltage no-load vs. loaded)
   - Temperature rise
   - Cooling system operation (fans, pumps)
   - Sound level
8. Perform thermal imaging of secondary connections at 100% load
9. Calculate:
   - Losses (primary kW - secondary kW)
   - Efficiency
   - Voltage regulation
10. Reduce load to zero
11. Disconnect load bank

**Acceptance Criteria:**
- Voltage regulation: Within ±2.5% (no-load to full-load)
- Temperature rise: Within nameplate limits
- Sound level: <65 dBA at 10 feet
- Efficiency: Per manufacturer specification
- No hot spots on thermal imaging

---

### Static Transfer Switch (STS) Testing

#### Test: STS Performance and Transfer Time

**Equipment Under Test:** [STS-01, STS-02, etc.]
**Test Reference:** [ELEC-STS-XX-L4]

**Load Bank Requirements:**
| Load Bank | Capacity | Voltage | Connection Point | Cable Size | Cable Length | Load Levels to Test |
|-----------|----------|---------|------------------|------------|--------------|---------------------|
| LB-5 | [800] kW (STS rating) | [480]V, 3-ph | STS output | [400] MCM | [20] ft | 0%, 50%, 100% |

**Metering Requirements:**
| Parameter | Meter Type | Location | Connection | Sampling Rate |
|-----------|------------|----------|------------|---------------|
| Source 1 Voltage | Oscilloscope + PQ Analyzer | STS Source 1 input | Voltage probes | 1 µs (oscilloscope for transfer) |
| Source 2 Voltage | Oscilloscope + PQ Analyzer | STS Source 2 input | Voltage probes | 1 µs (oscilloscope for transfer) |
| Output Voltage | Oscilloscope + PQ Analyzer | STS output | Voltage probes | 1 µs (oscilloscope for transfer) |
| Output Current | Power Quality Analyzer | STS output | CTs or clamps | 1 second |
| Transfer Time | Oscilloscope (4-channel) | All 3 voltages + trigger | Probes | Continuous capture |

**Critical Measurement:** Transfer time must be measured with calibrated oscilloscope capable of capturing <1ms events.

**Test Procedure:**
1. Verify both UPS sources available and within tolerance
2. Connect load bank to STS output
3. Connect oscilloscope to capture:
   - Channel 1: Source 1 voltage
   - Channel 2: Source 2 voltage
   - Channel 3: Output voltage
   - Channel 4: Trigger (use voltage drop on output as trigger)
4. Set oscilloscope trigger to capture transfer event
5. Connect power quality analyzer for steady-state monitoring
6. Begin testing:
   - **Manual Transfers (No Load):**
     - Source 1 to Source 2
     - Source 2 to Source 1
     - Capture transfer time with oscilloscope
   - **Automatic Transfers Under Load (50% load):**
     - Simulate source 1 failure (voltage sag, frequency deviation, phase loss)
     - Capture automatic transfer time
     - Verify transfer to source 2
     - Verify automatic retransfer to preferred source
   - **Load Transfer Tests:**
     - Transfer at 0% load
     - Transfer at 50% load
     - Transfer at 100% load
     - Measure transfer time for each
   - **Transfer Initiation Condition Tests:**
     - Voltage sag (10%, 20%, 30% undervoltage)
     - Voltage swell (110%, 120%)
     - Frequency deviation (±1Hz, ±2Hz)
     - Phase loss
     - Complete source failure
   - **Rapid Transfer Cycling:**
     - Perform 100 transfer cycles
     - Verify no faults or failures
7. Thermal imaging at 100% load
8. Document all transfer times (target <10ms, typical 4-6ms)

**Acceptance Criteria:**
- Transfer time: <10ms (target <4ms) break-before-make
- Voltage dropout during transfer: 0% (no interruption)
- Load carrying capacity: 100% of rating continuously
- Temperature rise: <40°C above ambient at full load
- 100 transfer cycles: No faults or failures
- All initiation conditions: Correct response

---

## Level 5 Testing - Integrated Load Bank Requirements

### Full Facility Load Test

#### Test: 24-Hour Full Facility Operational Test

**Test Reference:** [IST-FACILITY-OPS-L5]

**Load Bank Requirements - Distributed Loading:**

| Location | Load Bank | Capacity | Voltage | Connection Point | Purpose | Duration |
|----------|-----------|----------|---------|------------------|---------|----------|
| Data Hall - Row 1 | LB-10 through LB-15 | [6] x [200] kW | [208]V | Rack PDUs | Simulate IT load | 24+ hours |
| Data Hall - Row 2 | LB-16 through LB-21 | [6] x [200] kW | [208]V | Rack PDUs | Simulate IT load | 24+ hours |
| Mechanical Room | LB-4 | [500] kW | [480]V | Mechanical loads bus | Simulate mechanical loads | 24+ hours |
| UPS Systems | LB-3, LB-5 | [2] x [250] kW | [480]V | UPS outputs | UPS load testing | 24+ hours |

**Total Facility Load:** [XXXX] kW (approximately [XX]% of design capacity)

**Load Distribution Strategy:**
- Distribute load banks throughout facility to simulate actual load distribution
- Place load banks in racks to simulate IT equipment heat generation
- Include mechanical loads (pumps, fans operating)
- Include lighting and auxiliary loads

**Metering Requirements - Facility-Wide:**

**Primary Metering Points:**
| Location | Parameters | Meter Type | Purpose | Sampling Rate |
|----------|------------|------------|---------|---------------|
| Utility Service Entrance | V, A, kW, kVAR, kVA, PF, THD | Power Quality Analyzer | Total facility consumption | 1 second |
| Each MV Transformer Secondary | V, A, kW, THD, Temperature | Power Quality Analyzer + Thermal | Transformer loading | 1 second |
| Each UPS Output | V, A, kW, Efficiency, THD | Power Quality Analyzer | UPS performance | 1 second |
| Each Generator (if running) | V, A, kW, PF, Fuel Flow | PQ Analyzer + Fuel Meter | Generator performance | 1 second |
| Chilled Water Supply/Return | Temperature, Flow, Pressure | Temp sensors, Flow meter | Cooling system performance | 10 seconds |
| Data Hall Environment | Temperature (multiple points), Humidity, Pressure | Environmental sensors | Environmental conditions | 1 minute |

**Data Collection:**
- All meters time-synchronized
- Continuous 24-hour data logging
- Data exported hourly for review
- Real-time dashboards for monitoring

**Calculated Metrics:**
- Power Usage Effectiveness (PUE) = Total Facility Power / IT Equipment Power
- Cooling Efficiency (kW/ton)
- UPS Efficiency at actual load
- Generator fuel consumption rate (if running)
- Electrical distribution losses

**Test Procedure:**
1. Plan load bank placement throughout facility
2. Install and connect all load banks (de-energized)
3. Install all metering points per table above
4. Verify all metering operational and time-synchronized
5. Conduct pre-test walkthrough and safety briefing
6. Begin 24-hour test:
   - **Hour 0-4:** Gradual load ramp 0% to 100% design load
   - **Hour 4-24:** Maintain stable 100% load
   - Monitor continuously:
     - All electrical parameters
     - All mechanical parameters (temperatures, flows, pressures)
     - All environmental parameters
     - Alarms and events
   - Document:
     - PUE at various load levels
     - Cooling system efficiency
     - UPS efficiency
     - Any alarms or anomalies
7. **Hour 24-28:** Gradual load reduction to zero
8. Complete data logging and export all data
9. Disconnect and remove load banks
10. Analyze data and generate comprehensive report

**Acceptance Criteria:**
- 24 hours continuous operation with zero critical alarms
- Voltage: ±3% at all distribution points throughout test
- Frequency: ±0.1%
- THD: <5% voltage, <20% current
- All equipment temperatures within design limits
- PUE: Within [XX]% of design target
- All monitoring and control systems functional throughout
- Environmental conditions maintained (temperature, humidity)

---

### Heat Rise Testing (Data Hall with Temporary Containment)

#### Test: Data Hall Heat Rise Test

**Test Reference:** [IST-HEAT-RISE-L5]

**Load Bank Requirements - Rack Distribution:**

| Rack Location | Load Bank | Capacity | Voltage | Purpose |
|---------------|-----------|----------|---------|---------|
| Row 1, Rack 1 | LB-R1-1 | [10] kW | [208]V | Simulate server load |
| Row 1, Rack 2 | LB-R1-2 | [10] kW | [208]V | Simulate server load |
| [Continue for all racks] | [...] | [...] | [...] | [...] |

**Total Heat Load:** [XXX] kW distributed across [XX] racks

**Placement Strategy:**
- Load banks placed in racks to simulate actual IT equipment
- Heat output directed into hot aisle (if contained) or per actual configuration
- Load density per rack matches design ([XX] kW/rack)
- Distribution matches planned IT deployment

**Metering Requirements - Thermal Monitoring:**

| Parameter | Measurement Points | Instrument Type | Sampling Rate |
|-----------|-------------------|-----------------|---------------|
| Rack Inlet Temperature | Front of each rack (cold aisle) | Calibrated thermocouples | 1 minute |
| Rack Outlet Temperature | Rear of each rack (hot aisle) | Calibrated thermocouples | 1 minute |
| Cold Aisle Temperature | Top, middle, bottom of aisle (multiple locations) | Thermocouples / wireless sensors | 1 minute |
| Hot Aisle Temperature (if contained) | Top, middle, bottom of aisle | Thermocouples / wireless sensors | 1 minute |
| CRAH Supply Air Temperature | At each CRAH discharge | Thermocouples | 1 minute |
| CRAH Return Air Temperature | At each CRAH return | Thermocouples | 1 minute |
| Room Ambient Temperature | Multiple locations throughout space | Wireless sensors | 1 minute |
| Humidity | Cold aisle, hot aisle, room ambient | Calibrated humidity sensors | 1 minute |
| Pressure | Cold aisle, hot aisle, room (if contained) | Differential pressure sensors | 1 minute |
| Airflow | At each CRAH, at containment (if applicable) | Anemometer / hot wire | 5 minutes |

**Minimum Temperature Sensors Required:** [XXX] sensors

**Test Procedure:**
1. Install temporary containment per GC/CM plan (if applicable)
2. Place load banks in racks per distribution plan
3. Install all temperature, humidity, and pressure sensors
4. Verify all sensors operational and data logging
5. Verify all cooling systems operational (CRAHs, chillers, pumps)
6. Begin test:
   - **Hour 0:** Start data logging with no load
   - **Hour 0-2:** Ramp load 0% to 100% in [10]% increments
   - **Hour 2-26:** Hold at 100% load
   - Monitor continuously:
     - All rack inlet/outlet temperatures
     - Cold aisle / hot aisle temperatures
     - Room ambient conditions
     - CRAH performance
     - Cooling system operation
   - Document:
     - Maximum/minimum/average temperatures
     - Temperature stratification (top vs. bottom)
     - Hot spots
     - Return Temperature Index (RTI) = (Tr - Ts) / (Tre - Ts)
       - Tr = Rack return temperature
       - Ts = CRAH supply temperature
       - Tre = Rack return temperature (theoretical)
     - Supply Heat Index (SHI)
7. **Hour 26-28:** Ramp load to zero
8. Complete data logging
9. Remove load banks and temporary containment
10. Analyze data and generate heat rise report

**Acceptance Criteria:**
- Rack inlet temperature: 18-27°C (64-81°F) per ASHRAE recommended
- Rack inlet temperature variation: <5°F between racks
- Humidity: 40-60% RH (or per design)
- No hot spots >5°F above design
- RTI: Within acceptable range (typically >0.8)
- SHI: Within acceptable range
- Cooling system capacity demonstrated at design load
- Temperature stratification within acceptable limits

---

## Cable and Connection Requirements

### Load Bank Cabling

For all load bank connections, provide appropriately sized cables:

**Cable Sizing Table:**

| Load Bank Capacity | Voltage | Current (approx) | Recommended Cable Size (per phase) | Type | Length |
|--------------------|---------|------------------|-------------------------------------|------|--------|
| Up to 100 kW | 208V 3-ph | 278A | 300 MCM | THHN/THWN or SO cord | As required |
| 100-250 kW | 208V 3-ph | 695A | 500 MCM | THHN/THWN or SO cord | As required |
| 100-300 kW | 480V 3-ph | 361A | 350 MCM | THHN/THWN or SO cord | As required |
| 300-600 kW | 480V 3-ph | 722A | 600 MCM | THHN/THWN or SO cord | As required |
| 600-1000 kW | 480V 3-ph | 1203A | 1000 MCM or parallel runs | THHN/THWN or SO cord | As required |
| 1000-1500 kW | 480V 3-ph | 1804A | Parallel 750 MCM | THHN/THWN or SO cord | As required |

**Cable Requirements:**
- Rated for 90°C minimum
- Appropriately sized for voltage drop (<3% recommended)
- Grounding conductor included (sized per NEC)
- Flexible cord type acceptable for temporary connections
- Camlock or approved connectors
- Clearly labeled

### Connection Hardware

**Camlock Connectors:**
- Appropriately rated for current and voltage
- Standard color coding (if applicable)
- Positive locking mechanism

**Lugs:**
- Compression type, UL listed
- Properly sized for cable and termination point
- Torqued to manufacturer specifications

---

## Safety Requirements

### General Safety

1. **Arc Flash Protection:**
   - Arc flash assessment performed for all connection points
   - Appropriate PPE worn during connection/disconnection
   - Only qualified personnel perform connections

2. **Lockout/Tagout:**
   - All connections made in de-energized state when possible
   - LOTO procedures followed per project requirements
   - Energized work permits obtained when required

3. **Ventilation:**
   - Load banks placed in well-ventilated areas
   - Exhaust heat properly managed
   - Indoor use: verify adequate ventilation (load banks generate significant heat)
   - Outdoor use: protect from weather

4. **Fire Safety:**
   - Load banks placed on non-combustible surfaces
   - Minimum clearances maintained per manufacturer
   - Fire extinguishers readily available
   - Smoke detectors/fire alarm not inhibited

5. **Electrical Safety:**
   - All connections inspected before energization
   - Ground connections verified
   - Cables protected from damage
   - Overcurrent protection coordinated

6. **Personnel Safety:**
   - Barriers or rope-off around energized load banks
   - Warning signs posted
   - Only authorized personnel in area during testing
   - Communication protocols established (CxA, operators, contractors)

---

## Load Bank Logistics

### Delivery and Placement

**Delivery Schedule:**
- Load banks to be delivered minimum [7] days prior to Level 4 commencement
- Coordinate delivery with GC/CM site access requirements
- Verify unloading equipment available (forklift, crane, etc.)

**Placement Considerations:**
- Accessibility for connection and operation
- Proximity to connection points (minimize cable runs)
- Ventilation requirements
- Noise considerations
- Floor loading capacity (trailer-mounted load banks are heavy)
- Protection from weather (if outdoors)

**Storage:**
- Covered storage when not in use
- Security (load banks are expensive equipment)
- Protection from damage

### Operation

**Qualified Operators:**
- Installing contractor to provide qualified personnel
- Operators trained on specific load bank models
- Understanding of electrical safety
- Communication with CxA during testing

**Operating Procedures:**
- Follow manufacturer operating instructions
- Start at zero load, ramp gradually
- Monitor load bank temperatures
- Monitor electrical parameters
- Do not exceed rated capacity
- Emergency shutdown procedures established

---

## Data Management

### Data Collection

**Real-Time Monitoring:**
- All meters displayed on CxA laptop/monitoring station
- Alerts for out-of-range conditions
- Screen captures of key events

**Data Logging:**
- Continuous logging throughout tests
- Time-synchronized across all meters
- Configurable sampling rates per meter type

**Data Storage:**
- Primary: On meter internal memory
- Backup: Export to CxA laptop hourly
- Cloud backup: Upload daily (if connectivity available)

### Data Reporting

**Raw Data:**
- Export in CSV format for post-processing
- Include timestamp for all data points
- Preserve original data files

**Processed Data:**
- Graphs and charts generated in Excel or analysis software
- Overlay multiple parameters on common timeline
- Annotate with test events and observations

**Test Reports:**
- Include representative data plots in test reports
- Highlight any anomalies or out-of-tolerance conditions
- Compare actual vs. acceptance criteria
- Raw data files attached or referenced

---

## Coordination with Testing Outline

This Load Bank and Metering Plan must be coordinated with:

**Appendix A - Testing Outline:**
- Test sequence and schedule
- Equipment to be tested
- Test durations

**Level 4 Test Procedures:**
- Specific test steps referencing load bank connections
- Data collection requirements
- Acceptance criteria

**Master Construction Schedule:**
- Load bank delivery dates
- Testing windows
- Personnel availability

---

## Plan Approval and Updates

### Approval Process

This plan must be reviewed and approved by:

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Owner |  |  |  |
| Commissioning Authority |  |  |  |
| GC/CM |  |  |  |
| Electrical Contractor |  |  |  |

### Updates and Revisions

This plan may be revised as needed during the commissioning process:

- Changes to equipment ratings
- Additional tests identified
- Schedule adjustments
- Load bank availability changes

All revisions must be documented and re-approved.

---

## Revision History

| Revision | Date | Description | Author |
|----------|------|-------------|--------|
| 1.0 | [DATE] | Initial Load Bank and Metering Plan | [AUTHOR] |

---

## Related Documents

- [[PGCIS Commissioning Standard - Master Specification]]
- [[Appendix A - Testing Outline]]
- [[Commissioning Plan]]
- [[Level 4 Test Procedures]]
- [[Level 5 Test Procedures]]
- [[Electrical One-Line Diagrams]]
- [[Equipment Submittal Register]]

---

**Tags:** #load-bank #metering #testing #commissioning #level4 #level5 #pgcis