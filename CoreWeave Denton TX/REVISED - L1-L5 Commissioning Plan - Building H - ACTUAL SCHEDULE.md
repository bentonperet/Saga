# REVISED L1-L5 Commissioning Plan - Building H

## CoreWeave Denton South Data Center - ALIGNED TO ACTUAL PROJECT SCHEDULE

**Created:** 2025-11-19 (REVISED)
**Project:** CoreWeave Denton South Data Center - Building H
**Location:** 8151 Jim Christal Road, Denton, TX 76207
**Tags:** #commissioning #electrical #building-h #schedule-aligned

**CRITICAL:** This plan is aligned to the actual project schedule dated 2025-11-10.

---

## Executive Summary

This revised commissioning plan integrates L1-L5 commissioning activities with the actual Building H construction and startup schedule. **The key change is treating the February-March 2026 construction startup phase as formal L2/L3 commissioning**, reducing the standalone L4/L5 commissioning window to the scheduled 19 days (March 18 - April 13, 2026).

### Critical Schedule Milestones

| Milestone | Date | Type |
|-----------|------|------|
| Exterior Skids Started, Ready to Energize Interior | Feb 24, 2026 | Construction |
| Customer Early Access - Fiber Only | Mar 6, 2026 | Owner |
| H Interior Ready for L4 | Mar 17, 2026 | Construction |
| **Bldg H Cx Level 4 START** | **Mar 18, 2026** | **Commissioning** |
| Building H FULL Turnover | Apr 6, 2026 | Turnover |
| **Bldg H Cx Level 4 COMPLETE** | **Apr 6, 2026** | **Commissioning** |
| **Bldg H Cx Level 5 START** | **Apr 7, 2026** | **Commissioning** |
| GB200 Racks into Data Hall | Apr 7, 2026 | Customer |
| CDU Commissioning | Apr 8-10, 2026 | Customer |
| **Bldg H Cx Level 5 COMPLETE** | **Apr 13, 2026** | **Commissioning** |
| Network Provisioning Complete | Apr 21, 2026 | Customer |
| Node Provisioning Complete | Apr 29, 2026 | Customer |
| **Customer Handoff** | **Apr 30, 2026** | **Final** |

---

## Building H System Overview

**Power Blocks (per electrical one-lines):**
- **GPU Mechanical Blocks (MA):** 8 blocks - utility-fed, no generators
- **Mechanical Blocks (MB):** NOT in Building H (in separate buildings)
- **GPU Power Blocks (PA):** 18 blocks - utility-fed, no generators
- **IT Power Blocks (PB):** NOT in Building H (in separate buildings)
- **GPU Reserve Block (RA):** 1 block - redundancy for PA blocks

**Note:** Building H does NOT have on-site generators. Generator-backed systems are in other buildings (MB, PB blocks).

---

## Phase 1: L1 Factory Testing (Completed Before Delivery)

**Timeline:** Completed prior to equipment arrival on site

**SCOPE CLARIFICATION:** Factory witness testing is **NOT included** in our scope for this project. However, QA/QC review of all factory test deliverables will be part of our scope.

### Equipment Subject to Factory Testing (by Manufacturers/Others)

**Medium Voltage Transformers:**
- XFMR-MA-01H through MA-08H (8 units): 3000kVA, 34.5kV-415V
- XFMR-PA-01H through PA-18H (18 units): 3000kVA, 34.5kV-415V
- XFMR-RA-01H (1 unit): 3000kVA, 34.5kV-415V

**Main Switchboards:**
- SWBD-MA-01H through MA-08H (8 units): 4000A, 415/240V
- SWBD-PA-01H through PA-18H (18 units): 4000A, 415/240V
- SWBD-RA-01H (1 unit): 4000A, 415/240V

**UPS Systems:**
- MA blocks: 3 × 250kVA per block (24 units total)
- PA blocks: 2 × 1250kVA per block (36 units total)
- RA block: 2 × 1250kVA (2 units total)

**Static Transfer Switches:**
- PA blocks: 4 × 800A STS per block (72 units total)
- MA blocks: As shown on drawings

### L1 Deliverables Required for QA/QC Review (Due Before Equipment Installation)

**Our Scope:**
- QA/QC review of factory test reports per IEEE/NETA standards
- Verification of as-built drawings showing factory modifications
- Review of nameplate verification photographs
- Verification of shipping and handling documentation
- Review of warranty certificates

**Not in Our Scope:**
- Factory witness testing (attendance at manufacturer facilities)
- On-site factory acceptance testing coordination

---

## Phase 2: L2 Pre-Functional & Installation Verification

**Timeline:** November 2025 - February 2026 (integrated with construction)

**Strategy:** Complete all pre-functional verification **during construction** to minimize L4 commissioning scope.

### November 2025 - December 2025: Exterior Equipment Installation

**Activities (aligned to construction schedule):**

**H - Exterior Structure (Oct 24 - Dec 16, 2025):**
- Building steel erection: Oct 24 - Dec 2
- Roofing: Nov 12 - Dec 8
- IMP walls: Dec 3-16
- **Milestone: Exterior Roof and Façade Complete - Dec 16** ✓

**H - Exterior Equipment Yards (Oct 24 - Feb 24, 2026):**

**Week 1-4 (Nov 7 - Dec 8): Underground & Foundation Work**
- Mass excavation at chiller/electrical yards: Nov 7-22
- Civil/storm/water underground: Nov 24
- MV loop underground: Nov 25
- Telecomm underground: Nov 26 - Dec 4
- Generator laterals (if applicable): Dec 5-8

**L2 Commissioning Activities:**
- ✓ Verify underground installation per drawings
- ✓ Document as-built underground routing
- ✓ Megger test MV cables before termination
- ✓ Photograph all underground work before backfill

**Week 5-7 (Dec 9 - Dec 27): Equipment Setting**
- Form/pour equipment pads: Dec 9-13
- Cure pads: Dec 15-17
- Set MV transformers: Dec 18-27
- Set electrical skids/equipment/chillers: Dec 18 - Jan 17

**L2 Commissioning Activities:**
- ✓ Verify pad elevations and anchor bolt locations
- ✓ Inspect transformer installation (nameplate, clearances)
- ✓ Verify electrical skid installation per submittals
- ✓ Check chiller installation and supports
- ✓ Document equipment serial numbers and locations

**Week 8-10 (Dec 15 - Jan 29): Steel Structures**
- Form/pour steel bases: Dec 15-19
- Install conveyance steel: Jan 19-29

**L2 Commissioning Activities:**
- ✓ Verify structural steel installation
- ✓ Check cable tray and conduit support adequacy

### January 2026: Connections & Interior Build-Out

**H - Interior Construction (Nov 24, 2025 - Feb 28, 2026):**

**Week 1-2 (Jan 1-17): Gallery and BOH Equipment**
- Structural steel for conveyance complete
- Chilled water piping installation: Dec 5, 2025 - Jan 17
- Overhead electrical feeders: Dec 9, 2025 - Jan 6
- Equipment installation: Dec 9-13

**L2 Commissioning Activities:**
- ✓ Verify all cable/pipe penetrations fire-stopped
- ✓ Check cable tray fill ratios
- ✓ Verify separation between power and communications
- ✓ Inspect mechanical equipment installation

**Week 3-4 (Jan 8-29): Exterior Connections Complete**
- Pull/terminate MV loop cable: Jan 19-29
- Pull/terminate XFMR to skid cable: Jan 19-23
- Install chiller piping: Jan 30 - Feb 12
- Install cable buss: Jan 30 - Feb 7

**L2 Commissioning Activities:**
- ✓ Megger test all MV cables (min 100 MΩ @ 2.5kV)
- ✓ Megger test all LV feeders (min 10 MΩ @ 500V)
- ✓ Verify cable terminations and torque values
- ✓ Inspect all cable tags and identification
- ✓ Review protective relay settings vs. calculations

### February 2026: L2/L3 Integrated Startup & Commissioning

**CRITICAL CHANGE:** This period is formally designated as **L2/L3 Commissioning**, not just "construction startup."

#### Week 1 (Feb 2-8): Exterior Startup Preparation

**Construction Activities:**
- Install cable buss complete: Feb 7
- Install chiller piping complete: Feb 12

**L2/L3 Commissioning Activities:**
- Pre-energization meetings with contractors
- Safety briefings and arc flash training
- Final pre-functional checklists completed
- Test equipment staged and calibrated
- Load banks scheduled and delivered

**Deliverables:**
- Pre-functional checklists 100% complete
- Lockout/tagout procedures approved
- Energization permits obtained
- Test procedures approved

#### Week 2 (Feb 9-15): MV System Energization & Electrical Startup

**Construction Schedule:**
- **Energize MV Loop: Jan 24-26** (already complete)
- **Startup Electrical Skids: Feb 9-13**

**L2/L3 Commissioning Procedures:**

**Day 1-2 (Feb 9-10): MV Transformer Testing**
- Verify MV loop energization (done Jan 24-26)
- Transformer oil sampling and testing
- Transformer turns ratio verification
- Primary and secondary voltage measurements
- Phase rotation verification
- Neutral-ground bonding verification
- **Test Report: MV Transformer Commissioning**

**Day 3-5 (Feb 11-13): Electrical Skid Startup**
- Switchboard energization sequence
- Main breaker operation testing
- Verify voltage at all distribution points (415V ±5%)
- Power quality monitoring baseline
- Protective relay functional testing
- Ground fault system verification
- **Test Report: Electrical Distribution Startup**

**Acceptance Criteria:**
- MV cables: IR ≥ 100 MΩ
- LV cables: IR ≥ 10 MΩ
- Voltage: 415V ±3%
- Voltage balance: <2% deviation
- All protective relays functional

#### Week 3 (Feb 16-22): Mechanical Systems Startup

**Construction Schedule:**
- **Flush/Fill Chiller Piping: Feb 13-24**

**L2/L3 Commissioning Procedures:**

**Day 1-3 (Feb 13-15): Chiller System Flush/Fill**
- System cleanliness verification
- Hydrostatic pressure testing
- Chemical treatment per specifications
- Flow and pressure measurements
- Glycol concentration verification (if applicable)
- **Test Report: Chilled Water System Flush/Fill**

**Day 4-5 (Feb 16-17): Chiller Startup Preparation**
- Chiller pre-start inspections
- Refrigerant charge verification
- Oil level and quality checks
- Control wiring verification

**Day 6-9 (Feb 18-22): Chiller Performance Testing**
- Individual chiller startup (3 per MA block)
- Capacity verification
- Efficiency measurements
- Control sequence verification
- Alarm and safety shutdown testing
- **Test Report: Chiller Commissioning**

**Acceptance Criteria:**
- System leak-free at test pressure
- Water quality per specifications
- Chillers operate at rated capacity
- All controls and safeties functional

#### Week 4 (Feb 23 - Mar 1): Interior Systems Preparation

**Construction Schedule:**
- **Milestone: Exterior Skids Started, Ready to Energize Interior - Feb 24** ✓
- **Interior STS Startup: Feb 25-28**

**L2/L3 Commissioning Procedures:**

**Day 1-2 (Feb 25-26): UPS System Startup**
- UPS pre-start inspections
- Battery string voltage verification
- Rectifier startup and operation
- Inverter startup and synchronization
- Bypass mode operation verification
- **Test Report: UPS Initial Startup**

**Day 3-4 (Feb 27-28): Static Transfer Switch Startup**
- STS installation verification
- Input source verification (dual UPS feeds)
- Control wiring and programming verification
- Manual transfer testing (no load)
- Preferred source priority verification
- **Test Report: STS Installation & Startup**

**Acceptance Criteria:**
- UPS output: 415V ±2%, <3% THD
- Battery voltage within spec
- STS transfers manually without fault

### March 2026: Final L2/L3 Startup & L4 Preparation

#### Week 1 (Mar 2-8): Data Hall Systems Startup

**Construction Schedule:**
- Flush & fill chiller lines: Feb 14 - Mar 3
- Pull busstaps: Feb 7 - Mar 6
- Terminate busstaps: Feb 23 - Mar 6
- **Milestone: Customer Early Access - Fiber Only - Mar 6** ✓

**L2/L3 Commissioning Procedures:**

**Day 1-2 (Mar 2-3): Data Hall Chiller System Final Testing**
- System balance and commissioning
- Temperature control verification
- Final flow measurements
- System integration testing
- **Test Report: Data Hall Chiller System**

**Day 3-5 (Mar 4-6): Electrical Distribution Final Verification**
- Busstap termination verification
- Busway megger testing
- Voltage drop measurements
- Thermal imaging of all connections (infrared)
- **Test Report: Distribution System Verification**

**Day 6 (Mar 6): Customer Fiber Access**
- Facility access procedures established
- Safety orientation for customer personnel
- Fiber pathways verified and accessible

#### Week 2 (Mar 9-15): Final Interior Startup

**Construction Schedule:**
- Startup bussway: Mar 7-9
- Startup fan walls: Mar 7-11
- Air-water test & balance: Mar 12-17
- **Milestone: DATA Hall Ready to Energize - Mar 6** ✓
- **Milestone: H Interior Ready for L4 - Mar 17** ✓

**L2/L3 Commissioning Procedures:**

**Day 1-3 (Mar 7-9): Bussway and Distribution Startup**
- Energize 4000A busways
- 800A STS busway energization
- Load bank connection and testing
- Voltage regulation under load
- **Test Report: Busway System Startup**

**Day 4-6 (Mar 9-11): Fan Wall Startup**
- Individual fan motor testing
- VFD programming verification
- Airflow measurements
- Control sequence testing
- **Test Report: Fan Wall Commissioning**

**Day 7-10 (Mar 12-15): Air-Water Test & Balance**
- Chilled water pump VFD testing
- System balance and flow verification
- Temperature control loop tuning
- Building pressure verification
- **Test Report: HVAC Test & Balance**

**Day 11-12 (Mar 16-17): Final L2/L3 Closeout**
- Deficiency punch list completion
- Final thermal imaging scan
- Power quality baseline documentation
- System readiness verification for L4
- **Deliverable: L2/L3 Commissioning Summary Report**

**Acceptance Criteria for L4 Readiness:**
- All systems operational
- All safety systems functional
- No critical deficiencies outstanding
- All L2/L3 test reports complete
- Training materials prepared

---

## Phase 3: L4 Performance Verification Commissioning

**Timeline:** March 18 - April 6, 2026 (**14 calendar days**)

**Objective:** Verify performance, reliability, and compliance with specifications through comprehensive load testing and integrated systems verification.

**Strategy:** Parallel testing teams working simultaneously across multiple systems to maximize efficiency.

### Week 1: Mar 18-24 (Days 1-7)

#### Testing Team Structure

**Team 1: Power Systems (Electrical Engineer + 2 Technicians)**
- UPS performance testing
- Battery discharge testing
- Electrical distribution verification

**Team 2: Mechanical Systems (Mechanical Engineer + 2 Technicians)**
- Chiller performance testing
- CHW pump and VFD verification
- HVAC systems performance

**Team 3: Integration/Controls (Controls Engineer + 2 Technicians)**
- STS performance testing
- BMS/SCADA integration
- Sequence of operations verification

#### Day 1 (Tuesday, Mar 18): Commissioning Kickoff

**Morning:**
- 8:00 AM: Commissioning kickoff meeting (all stakeholders)
- Safety briefing and arc flash requirements review
- Review test schedule and responsibilities
- Distribute test procedures and forms

**Afternoon:**
- Team assignments and equipment checkout
- Calibration certificate verification
- Test equipment setup and staging
- Preliminary system walkdown

**Deliverable:** Signed kickoff meeting minutes

#### Days 2-3 (Wednesday-Thursday, Mar 19-20): UPS Performance Testing

**Team 1 Focus:**

**All MA Blocks (8 blocks × 3 UPS each = 24 UPS units):**
**All PA Blocks (18 blocks × 2 UPS each = 36 UPS units):**
**RA Block (1 block × 2 UPS = 2 UPS units):**

**Testing approach:** Test multiple blocks in parallel

**Parallel UPS Operation Testing:**
- Load sharing verification (target ±5% between modules)
- Synchronization verification
- Single module failure simulation
- Automatic load redistribution testing

**Transfer Performance:**
- Normal to bypass transfer time (<10ms)
- Bypass to normal transfer
- Transfer under 0%, 50%, 100% load
- Multiple rapid transfer cycles (10 minimum)

**Load Step Response:**
- 0% to 100% load step
- 100% to 0% load step
- Voltage regulation verification (±3%)
- Frequency stability verification (±0.5Hz)

**Test Blocks:**
- Day 2 AM: MA-01H, MA-02H, PA-01H, PA-02H
- Day 2 PM: MA-03H, MA-04H, PA-03H, PA-04H
- Day 3 AM: MA-05H, MA-06H, PA-05H through PA-08H
- Day 3 PM: MA-07H, MA-08H, PA-09H through PA-12H, RA-01H

**Deliverable:** UPS Performance Test Reports (by block)

#### Days 2-3 (Mar 19-20): Battery Discharge Testing

**CONCURRENT with UPS testing:**

**Battery Autonomy Verification (All Blocks):**
- Full load discharge test
- Target: ≥5 minutes at 100% load (EOL condition)
- Monitor voltage sag characteristics
- Verify low battery warning timing
- Verify shutdown sequence

**Testing Strategy:**
- Use load banks for controlled discharge
- Stagger tests across blocks (avoid simultaneous battery drain)
- Document recharge characteristics

**Schedule:**
- Day 2: MA blocks (8 battery systems)
- Day 3 AM: PA blocks 1-9 (18 battery systems)
- Day 3 PM: PA blocks 10-18, RA block (20 battery systems)

**Acceptance Criteria:**
- Runtime ≥5 minutes at 100% load
- All alarms function correctly
- Automatic shutdown as designed
- Recharge within 8 hours to 90%

**Deliverable:** Battery Discharge Test Reports

#### Days 4-5 (Friday-Saturday, Mar 21-22): Static Transfer Switch Performance

**Team 3 Focus:**

**STS Performance Testing (PA Blocks: 72 STS units total):**

**Critical Test:** Transfer time verification with oscilloscope
- Target: <10ms break-before-make
- Typical: 4-6ms expected
- Zero voltage dropout requirement

**Testing per STS:**
- Source 1 to Source 2 transfer
- Source 2 to Source 1 transfer
- Test at 0%, 50%, 100% load (800A rated)
- Measure with calibrated oscilloscope

**Initiation Conditions Testing:**
- Voltage sag (10%, 20%, 30% depth)
- Frequency deviation (±2Hz)
- Complete source failure
- Phase loss

**Load Bank Testing:**
- Each STS tested to 800A capacity
- Thermal imaging at full load
- Voltage drop measurement (target <3%)

**Testing Schedule:**
- Day 4 AM: PA-01H through PA-04H (16 STS)
- Day 4 PM: PA-05H through PA-09H (20 STS)
- Day 5 AM: PA-10H through PA-14H (20 STS)
- Day 5 PM: PA-15H through PA-18H (16 STS)

**Acceptance Criteria:**
- Transfer time: <10ms
- Load carrying capacity: 100% of rating
- Temperature rise: <40°C above ambient
- 100 transfer cycles without fault

**Deliverable:** STS Performance Test Reports

#### Days 4-5 (Mar 21-22): Chiller Performance Testing

**Team 2 Focus:**

**Chiller Testing (MA Blocks: 3 chillers × 8 blocks = 24 chillers):**

**Performance Verification:**
- Capacity testing at design conditions
- Efficiency measurements (kW/ton)
- Control sequence verification
- Staging and destaging
- Alarm testing

**N+1 Redundancy Verification:**
- Take one chiller offline per block
- Verify remaining chillers absorb load
- Monitor system temperatures
- Verify adequate capacity maintained

**Testing Schedule:**
- Day 4: MA-01H through MA-04H (12 chillers)
- Day 5: MA-05H through MA-08H (12 chillers)

**Deliverable:** Chiller Performance Test Reports

### Week 2: Mar 25-31 (Days 8-14)

#### Days 8-10 (Tuesday-Thursday, Mar 25-27): Integrated Building Systems

**All Teams Coordinated:**

**Full Building Load Test:**
- Bring all MA blocks to full load simultaneously
- Bring all PA blocks to full load simultaneously
- Monitor MV distribution capacity
- Verify all transformers within thermal limits
- Power quality monitoring across facility

**Test Sequence:**
- Day 8 AM: Ramp all MA blocks 0% to 50% load
- Day 8 PM: Ramp all MA blocks 50% to 100% load
- Day 9 AM: Ramp all PA blocks 0% to 50% load
- Day 9 PM: Ramp all PA blocks 50% to 100% load
- Day 10: Full facility at 100% load (4+ hours)

**Monitoring Points:**
- MV transformer loading (all 27 transformers)
- Switchboard temperatures (thermal imaging)
- UPS efficiency under load
- Chiller system performance
- Building temperatures and humidity
- Power factor and harmonics (THD)

**Acceptance Criteria:**
- Voltage: 415V ±3% at all points
- Frequency: 50Hz ±0.1%
- THD: <5% voltage, <20% current
- All equipment within thermal limits
- Power factor: >0.95

**Deliverable:** Integrated Systems Performance Report

#### Days 8-10 (Mar 25-27): VFD and Motor Testing

**Team 2 Focus (concurrent with load testing):**

**CHW Pump VFD Testing (3 pumps × 8 MA blocks = 24 VFDs):**

**Performance Tests:**
- Speed range verification (0-100%)
- Current draw at various speeds
- Power factor verification
- Control response time (<2 seconds)
- BMS/SCADA integration verification

**Motor Performance:**
- Rotation direction verification
- Current balance (<5% between phases)
- Vibration analysis
- Bearing temperature monitoring

**Testing Schedule:**
- Parallel testing during building load test
- Verify VFD performance under actual load conditions

**Deliverable:** VFD/Motor Test Reports

#### Days 11-12 (Friday-Saturday, Mar 28-29): Protective Systems & Safety

**All Teams:**

**Protective Relay Testing:**
- Primary injection testing (spot-check)
- Trip time verification
- Coordination verification
- Communication module testing

**Ground Fault Testing:**
- Ground fault pickup verification
- Alarm verification
- Selective coordination verification

**Emergency Systems:**
- Emergency power-off (EPO) sequence
- Fire alarm interface testing (if applicable)
- Emergency lighting (if applicable)

**Deliverable:** Protective Systems Test Report

#### Days 13-14 (Sunday-Monday, Mar 30-31): Deficiency Resolution & Documentation

**All Teams:**

**Deficiency Closeout:**
- Review all open items
- Prioritize critical vs. minor issues
- Coordinate correction activities
- Re-test corrected items

**Documentation:**
- Compile all test reports
- Photograph all equipment nameplates
- Thermal imaging documentation
- Final punch list

**Deliverable:** Preliminary L4 Commissioning Report

### L4 Final Week: Apr 1-6 (Days 15-19)

#### Days 15-17 (Tuesday-Thursday, Apr 1-3): Performance Verification Completion

**Final Testing:**
- Any re-tests from corrected deficiencies
- Final full-load test (24-hour duration if possible)
- Final power quality survey
- Final thermal imaging scan

**Deliverable:** Final Test Data

#### Days 18-19 (Friday-Saturday, Apr 4-5): L4 Closeout & Turnover Preparation

**Day 18 (Apr 4):**
- Final deficiency review
- Acceptance criteria verification
- Documentation review and completion
- Training material preparation

**Day 19 (Apr 5):**
- Turnover documentation package assembly
- Final walkthrough with owner
- System demonstration to operations team
- L4 completion certification

**Sunday, April 6, 2026:**
- **Milestone: Building H FULL Turnover** ✓
- **Milestone: Bldg H Cx Level 4 COMPLETE** ✓

**Deliverables:**
- Final L4 Commissioning Report
- All test reports compiled
- Deficiency log with resolutions
- As-built drawings marked up
- Training completion records (preliminary)
- Turnover certificate

---

## Phase 4: L5 Integrated Performance & Reliability Testing

**Timeline:** April 7-13, 2026 (**5 calendar days**)

**CRITICAL CONSTRAINT:** Overlaps with customer GB200 rack installation and CDU commissioning.

**Strategy:** Focus on critical failure modes and system reliability. Coordinate testing to avoid disruption of customer activities.

### Coordination Protocol with Customer Activities

**Customer Activities During L5:**
- Apr 7: GB200 racks begin installation
- Apr 8-10: CDU commissioning
- Apr 8-21: Network provisioning
- Apr 15-29: Node provisioning

**Testing Approach:**
- **Daytime (8 AM - 5 PM):** Non-disruptive monitoring and minor tests
- **Evening (6 PM - 10 PM):** Coordinated tests with customer notification
- **Night (10 PM - 6 AM):** Disruptive failure mode tests (if approved)
- **Pre-coordinated blackout windows:** Agreed times for planned outages

**Communication Protocol:**
- Daily coordination meeting at 7:00 AM
- 24-hour advance notice for any planned power interruption
- Customer approval required for disruptive testing
- Real-time notification of any unplanned events

### Week 1 (Apr 7-13): Critical Failure Mode Testing

#### Day 1 (Monday, Apr 7): UPS Failure Scenarios

**MORNING (8:00 AM - 12:00 PM):**
- Coordination meeting with customer
- Review testing plan and schedule
- Identify customer-approved test windows

**EVENING (7:00 PM - 10:00 PM):**
**Test: Single UPS Module Failure (MA Blocks)**
- Simulate failure of one 250kVA module in 3-module parallel system
- Verify automatic load transfer to remaining modules
- Monitor load continuity (no disruption)
- Verify alarms and notifications
- Test system recovery

**Test Blocks:**
- MA-01H, MA-03H, MA-05H, MA-07H (sample testing)

**Acceptance Criteria:**
- Zero load disruption
- Alarm within 5 seconds
- Automatic load redistribution
- Successful recovery when module restored

**Deliverable:** UPS Redundancy Test Report

#### Day 2 (Tuesday, Apr 8): STS Automatic Transfer Testing

**CRITICAL:** Customer CDU commissioning begins today - coordinate carefully

**MORNING (8:00 AM - 12:00 PM):**
- Observation mode: Monitor customer CDU commissioning
- No disruptive testing

**EVENING (7:00 PM - 11:00 PM):**
**Test: STS Automatic Source Transfer Under Load**
- Simulate primary UPS source failure
- Verify automatic transfer to alternate source
- Measure transfer time and load continuity
- Verify return to preferred source
- Multiple transfer cycles

**Test Sample:**
- PA-02H, PA-06H, PA-10H, PA-14H, PA-18H (5 blocks, 20 STS units)

**Acceptance Criteria:**
- Transfer time: <10ms
- Zero load dropout
- All loads remain operational
- Automatic return to preferred source

**Deliverable:** STS Reliability Test Report

#### Day 3 (Wednesday, Apr 9): Cooling System Redundancy

**DAYTIME (8:00 AM - 5:00 PM):**
**Test: Chiller N+1 Redundancy Verification**
- Take one chiller offline per block (planned)
- Monitor system response
- Verify remaining chillers absorb load
- Check space temperatures remain within limits
- Document recovery time

**Test Blocks:**
- All MA blocks (8 blocks tested sequentially)

**Acceptance Criteria:**
- Temperature excursion: <5°F from setpoint
- Automatic staging of remaining chillers
- No alarms or shutdowns
- Return to normal within 15 minutes

**Deliverable:** Cooling Redundancy Test Report

#### Day 4 (Thursday, Apr 10): Power Quality & Harmonics

**DAYTIME:**
**Test: Comprehensive Power Quality Survey**
- 24-hour power quality monitoring
- Harmonic analysis across all distribution
- Voltage and frequency stability
- Neutral current monitoring
- Transient capture and analysis

**Monitoring Points:**
- All 27 switchboards
- All UPS outputs
- Critical load connections

**Acceptance Criteria:**
- THD voltage: <5%
- THD current: <20%
- Voltage: 415V ±3%
- Neutral current: <20% of phase current

**Deliverable:** Power Quality Analysis Report

#### Day 5-7 (Friday-Sunday, Apr 11-13): Final Reliability & Operational Testing

**Day 5 (Apr 11): Operational Scenario Testing**

**Planned Maintenance Simulation:**
- UPS module maintenance bypass procedure
- Switchgear inspection under load procedure
- Chiller maintenance with system operating
- Demonstrate safe isolation procedures

**Emergency Scenarios:**
- Emergency power-down (EPO) sequence
- Simulated utility disturbance response
- Load shedding cascade (if designed)

**Day 6 (Apr 12): Documentation & Training**

**Operator Training:**
- Normal operations procedures
- Maintenance bypass procedures
- Emergency response procedures
- Alarm investigation and response
- BMS/SCADA navigation

**Training Deliverables:**
- Training attendance rosters
- Competency verification tests
- Video recordings of key procedures

**Day 7 (Sunday, Apr 13): L5 Closeout**

**Final Activities:**
- Compile all L5 test reports
- Final deficiency review
- Complete training records
- Prepare final commissioning summary
- L5 completion certification

**Monday, April 13, 2026:**
- **Milestone: Bldg H Cx Level 5 COMPLETE** ✓

**Deliverables:**
- Final L5 Commissioning Report
- All failure mode test reports
- Training completion certificates
- Operations and maintenance manuals
- Final deficiency log (with resolutions)
- Final as-built drawings
- Warranty documentation
- Final commissioning summary report

---

## Customer Handoff Period (Apr 15-30, 2026)

**Commissioning Authority Role:**
- Available for technical support
- Monitor system performance
- Respond to deficiency items
- Support customer activities as needed

**Customer Activities:**
- Node provisioning: Apr 15-29
- Final acceptance testing

**April 30, 2026:**
- **CUSTOMER HANDOFF** ✓
- Final acceptance certificate
- Warranty period begins

---

## Post-Handoff Activities (May 2026)

**Week 1-2 (May 1-15):**
- Final documentation delivery
- Outstanding deficiency resolution
- Post-occupancy performance monitoring
- Final training sessions (if needed)

**Deliverables:**
- Final O&M manuals (3 copies + electronic)
- Final as-built CAD drawings
- Spare parts inventory and locations
- Warranty contact information
- Commissioning closeout report

---

## Schedule Summary Table

| Phase | Duration | Start | End | Key Activities |
|-------|----------|-------|-----|----------------|
| **L1 Factory Testing** | Pre-delivery | N/A | Nov 2025 | Equipment FAT witness |
| **L2 Pre-Functional** | 12 weeks | Nov 7, 2025 | Feb 8, 2026 | Installation verification during construction |
| **L2/L3 Startup** | 6 weeks | Feb 9, 2026 | Mar 17, 2026 | Formal startup = commissioning |
| **L4 Performance Cx** | **14 days** | Mar 18, 2026 | Apr 6, 2026 | Load testing, verification |
| **L5 Reliability Cx** | **5 days** | Apr 7, 2026 | Apr 13, 2026 | Failure modes, training |
| **Customer Handoff Period** | 17 days | Apr 13, 2026 | Apr 30, 2026 | Support customer activities |
| **Post-Handoff Closeout** | 15 days | May 1, 2026 | May 15, 2026 | Final documentation |

**Total Commissioning Duration:** ~27 weeks (but only 19 days of dedicated L4/L5 commissioning)

---

## Critical Success Factors

### 1. Construction Schedule Adherence
- **Zero tolerance for delays past March 17, 2026**
- Weekly schedule monitoring starting December 2025
- Proactive issue resolution during construction

### 2. L2/L3 Integration with Construction
- **Treat startup as commissioning, not just construction**
- CxA witness all startup activities
- Formal test procedures and reports for all startups
- This approach "banks" 6 weeks of commissioning credit

### 3. Parallel Testing Approach (L4)
- **Multiple teams working simultaneously**
- Test equipment pre-staged and calibrated
- Test procedures pre-approved
- Contractor support coordinated in advance

### 4. Customer Coordination (L5)
- **Daily coordination meetings Apr 7-13**
- Pre-approved test windows
- Minimize disruption to rack installation
- Flexible approach (defer non-critical tests if needed)

### 5. Documentation Discipline
- **Test reports completed within 24 hours**
- Running deficiency log updated daily
- Progressive documentation (not batch at end)
- Final deliverables ready by May 15

---

## Risk Mitigation Summary

| Risk | Mitigation |
|------|------------|
| **Construction delays past Mar 17** | Weekly monitoring, proactive issue resolution, punch list during construction |
| **Insufficient L4 time (14 days)** | L2/L3 startup credit, parallel testing, pre-functional during construction |
| **Customer activity conflicts (L5)** | Daily coordination, night/weekend testing, deferral of non-critical tests |
| **Equipment failures during Cx** | Factory test verification, spare parts on-site, manufacturer support on call |
| **Training time not scheduled** | Integrate training with testing, post-handoff sessions if needed |

---

## Roles & Responsibilities (Aligned to Actual Schedule)

### November 2025 - February 2026: L2 Pre-Functional

**General Contractor:**
- Coordinate access for CxA inspections
- Provide construction schedule updates weekly
- Support pre-functional checklist completion

**Electrical Contractor:**
- Complete installation per drawings
- Execute pre-functional checklists
- Prepare for energization activities

**Commissioning Authority:**
- Conduct spot-check inspections
- Review contractor pre-functional checklists
- Identify deficiencies for correction

### February 9 - March 17, 2026: L2/L3 Startup

**Equipment Manufacturers:**
- Provide startup technicians for initial energization
- Witness testing and provide factory support
- Training for operations staff

**Contractors:**
- Execute startup procedures
- Perform functional testing
- Document results per CxA requirements

**Commissioning Authority:**
- Witness all startups
- Verify test procedures and results
- Document as L2/L3 commissioning
- Issue startup/commissioning reports

### March 18 - April 6, 2026: L4 Performance Commissioning

**Commissioning Authority:**
- Lead all L4 testing
- Coordinate test teams
- Verify performance against specifications
- Issue L4 commissioning reports

**Contractors:**
- Support testing activities
- Provide operators for equipment
- Correct deficiencies as identified

**Owner:**
- Review test results
- Accept/reject equipment performance
- Approve turnover

### April 7-13, 2026: L5 Reliability Commissioning

**Commissioning Authority:**
- Coordinate testing with customer activities
- Execute failure mode testing
- Conduct operator training
- Issue final commissioning report

**Owner/Customer:**
- Approve test windows
- Participate in coordination meetings
- Receive operations training

---

## Deliverables Schedule

| Deliverable | Due Date | Responsibility |
|-------------|----------|----------------|
| Pre-Functional Checklists Complete | Feb 8, 2026 | Contractor/CxA |
| L2/L3 Startup Reports | Mar 17, 2026 | CxA |
| L2/L3 Summary Report | Mar 17, 2026 | CxA |
| L4 Test Reports (daily during L4) | Mar 18 - Apr 6 | CxA |
| L4 Commissioning Report | Apr 6, 2026 | CxA |
| Building H Turnover Package | Apr 6, 2026 | CxA/Contractor |
| L5 Test Reports | Apr 7-13, 2026 | CxA |
| Training Completion Records | Apr 13, 2026 | CxA |
| L5 Commissioning Report | Apr 13, 2026 | CxA |
| Final Commissioning Summary | Apr 30, 2026 | CxA |
| Final O&M Manuals | May 15, 2026 | CxA/Contractor |
| Final As-Built Drawings | May 15, 2026 | Contractor/Engineer |

---

## Appendix: Test Equipment Requirements

**Required On-Site by March 18, 2026:**

### Electrical Testing Equipment
- Megohmmeter (5kV range for MV testing)
- Power quality analyzer (Class A, IEC 61000-4-30)
- Clamp-on ammeters (1000A range, True RMS) - minimum 6 units
- Digital multimeters (0.1% accuracy) - minimum 6 units
- Oscilloscope (4-channel, 100MHz) for STS transfer time measurement
- Primary injection test set (0-4000A) for protective relay testing
- Thermal imaging camera (-20°C to 350°C range)
- Load banks:
  - 3000kW resistive (for full building load testing)
  - 800kW resistive (for STS and busway testing)
  - Reactive capability (0.8 PF)

### Mechanical Testing Equipment
- Ultrasonic flow meters
- Pressure gauges (calibrated)
- Temperature measurement devices
- Vibration analyzer

### All Equipment Requirements
- Valid calibration certificates (<12 months old)
- NIST-traceable
- Certificates provided with test reports

---

**Document Control:**

| Revision | Date | Description | Author |
|----------|------|-------------|--------|
| 1.0 | 2025-11-19 | Revised plan aligned to actual project schedule | CxA Team |

**Approval:**

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Owner Representative |  |  |  |
| Commissioning Authority |  |  |  |
| General Contractor |  |  |  |
| Electrical Contractor |  |  |  |

---

**END OF REVISED COMMISSIONING PLAN**