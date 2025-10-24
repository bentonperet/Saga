**Created:** 2025-10-17 18:30

# BASIS OF DESIGN - PART 2: SUPPORTING SYSTEMS
## Saga Energy – Pryor Data Center
### Mayes County, Oklahoma

**Project Reference:** Schneider Electric EcoStruxure™ Reference Design 109 (RD109)
**Document Status:** DRAFT - Complete (Part 2 of 2)
**Prepared by:** PGCIS Program Management Team
**Date:** October 17, 2025
**Purpose:** Technical design foundation for investor package and downstream detailed design

**Related Documents:**
- [[Feasibility Memo V3]] - Strategic decisions and validation studies
- [[RD109_0.0_Table-Of-Contents_R10]] - Schneider Electric baseline reference design
- [[BESS as UPS Replacement - Feasibility Analysis V2]] - Power system optimization analysis
- [[_Project Plan]] - Project schedule and milestones
- [[Basis of Design - Part 1 Core Systems]] - Sections 1-6 (Project Overview, Site, Electrical, Renewable Energy, Mechanical, Plumbing)

---

## TABLE OF CONTENTS - PART 2

7. [FIRE PROTECTION & LIFE SAFETY](#7-fire-protection--life-safety)
8. [SECURITY & ACCESS CONTROL](#8-security--access-control)
9. [TELECOMMUNICATIONS & CONNECTIVITY](#9-telecommunications--connectivity)
10. [MONITORING, CONTROLS & AUTOMATION](#10-monitoring-controls--automation)
11. [OPERATIONS & MAINTENANCE STRATEGY](#11-operations--maintenance-strategy)
12. [SUSTAINABILITY & ENVIRONMENTAL](#12-sustainability--environmental)
13. [DEVIATIONS FROM RD109 BASELINE](#13-deviations-from-rd109-baseline)

**→ For Sections 1-6, see [[Basis of Design - Part 1 Core Systems]]**

---

# 7. FIRE PROTECTION & LIFE SAFETY

## 7.1 Fire Protection Overview

The fire protection system is designed to meet NFPA, IBC, and insurance requirements while protecting personnel, equipment, and minimizing business interruption.

**Design Philosophy:**
- **Early Detection:** Smoke and heat detection in all critical areas
- **Rapid Suppression:** Automatic suppression systems in data hall and electrical rooms
- **Personnel Safety:** Clear egress paths and emergency notification systems
- **Equipment Protection:** Clean agent systems to prevent water damage to IT equipment

**Code Compliance:**
- NFPA 72 - National Fire Alarm and Signaling Code
- NFPA 75 - Standard for the Fire Protection of Information Technology Equipment
- NFPA 2001 - Standard on Clean Agent Fire Extinguishing Systems
- NFPA 855 - Standard for the Installation of Stationary Energy Storage Systems (for BESS)
- NFPA 101 - Life Safety Code
- International Building Code (IBC) occupancy classification and construction type requirements

## 7.2 Fire Suppression Systems

**Data Hall Suppression:**
- **System Type:** Pre-action dry pipe sprinkler system OR clean agent gas suppression
- **Pre-Action Option (RECOMMENDED):**
  - Dual-interlock pre-action system (requires smoke detection + heat activation before water release)
  - Dry pipe eliminates risk of accidental water damage
  - ESFR (Early Suppression Fast Response) or standard sprinkler heads
  - Water supply: Fire pump + storage tank or municipal water service (TBD)
- **Clean Agent Option:**
  - FM-200 (HFC-227ea) or Novec 1230 (FK-5-1-12)
  - Agent concentration: Per NFPA 2001 for Class A/C fires
  - Agent discharge time: ≤10 seconds
  - Cost Impact: +$500K-800K vs. pre-action system

**Decision Required:** Align suppression system with customer preferences and insurance requirements. Pre-action is lower cost; clean agent preferred by some hyperscale customers.

**Electrical Rooms (UPS/BESS):**
- **System Type:** Clean agent gas suppression (FM-200 or Novec 1230)
- **Rationale:** Protects high-value electrical equipment without water damage risk
- **Coverage:** Full room flooding system with nozzle distribution per NFPA 2001
- **Integration:** Automatic activation on smoke detection; manual abort switch outside room

**Mechanical Rooms:**
- **System Type:** Wet pipe sprinkler system
- **Coverage:** Sprinkler heads per NFPA 13 spacing requirements
- **Equipment Protection:** Avoid sprinkler heads directly above sensitive controls (use sidewall heads)

**Office/NOC/Support Spaces:**
- **System Type:** Wet pipe sprinkler system
- **Coverage:** Standard commercial spacing per NFPA 13

**BESS Enclosure (If BESS-as-UPS Selected):**
- **System Type:** Specialized lithium-ion battery fire suppression per NFPA 855
- **Options:**
  - Water mist system (preferred for LFP chemistry)
  - Clean agent system with enhanced concentration
  - Hybrid system (detection + gas suppression + water backup)
- **Gas Detection:** Hydrogen, smoke, and CO detection with early warning alarms
- **Thermal Runaway Prevention:** Temperature monitoring, HVAC smoke evacuation, explosion venting
- **Automatic Activation:** Multi-criteria detection (heat + smoke + gas)

## 7.3 Fire Detection & Alarm Systems

**Detection Technology:**
- **Data Hall:** Very Early Smoke Detection Apparatus (VESDA) or aspirating smoke detection (ASD)
  - Air sampling holes above and below raised floor (if used) or at ceiling and floor level (if slab)
  - Sensitivity: Alert at 0.005% obscuration/ft, alarm at 0.02% obscuration/ft
  - Response time: <60 seconds for early detection
- **Electrical Rooms:** Spot-type smoke detectors + heat detectors
- **Mechanical Rooms:** Spot-type smoke and heat detectors
- **BESS Enclosure:** Multi-criteria detection (smoke + heat + gas + thermal imaging)
- **Support Spaces:** Spot-type smoke detectors per NFPA 72

**Fire Alarm Control Panel (FACP):**
- **Type:** Addressable, networked fire alarm system
- **Integration:** BMS integration for monitoring and control
- **Notification:** Visual and audible alarms (strobes + horns)
- **Remote Monitoring:** 24/7 NOC monitoring + off-site central station monitoring
- **Zones:** Separate zones for data hall, electrical rooms, mechanical rooms, support spaces

**Pre-Alarm Strategy:**
- **Alert Level:** Low-level smoke detection triggers alert (investigate, no evacuation)
- **Alarm Level:** Higher smoke level or heat detection triggers full alarm (evacuation, suppression activation)
- **Staged Response:** Allows time to investigate false alarms before full evacuation/suppression

## 7.4 Egress & Life Safety

**Occupancy Classification:**
- **Data Hall:** Group B (Business) per IBC Section 304
- **Office/NOC:** Group B (Business)
- **Occupant Load:** ~20-30 persons (varies by operational model)

**Egress Requirements:**
- **Exit Count:** Minimum 2 exits from data hall per IBC Section 1006
- **Exit Width:** 36" minimum per door, 44" preferred for equipment moves
- **Travel Distance:** ≤200 ft to nearest exit (unsprinklered), ≤300 ft (sprinklered) per IBC Table 1017.2
- **Exit Signs:** Illuminated exit signs at all egress doors
- **Emergency Lighting:** Battery-backed LED emergency lighting per NFPA 101
  - Illumination: 1 foot-candle average, 0.1 fc minimum
  - Duration: 90 minutes minimum battery backup

**Hot Aisle Containment Integration:**
- Containment doors must auto-release on fire alarm activation (magnetic hold-open with fail-safe release)
- Egress paths must not be blocked by containment structures

## 7.5 Fire Pump & Water Supply

**Water Supply Requirements (If Sprinkler System Selected):**
- **Demand Calculation:** Per NFPA 13 for data hall (most demanding area)
  - Estimated demand: 1,500-2,500 GPM @ 60-80 psi (TBD via hydraulic calculation)
- **Fire Pump:** Electric or diesel-driven fire pump sized to meet demand
- **Storage Tank:** 50,000-100,000 gallon on-site fire water storage tank (if municipal supply insufficient)
- **Backflow Prevention:** Double-check backflow preventer on fire service connection

**Municipal Water Dependency:**
If municipal water service is unavailable or insufficient:
- On-site storage tank + fire pump required
- Tank refilled periodically via water truck delivery
- Coordinate with Water & Wastewater Availability Study (Feasibility Memo Section 4.3)

---

# 8. SECURITY & ACCESS CONTROL

## 8.1 Security Overview

The security system provides multi-layered protection for critical infrastructure, customer equipment, and personnel safety.

**Security Objectives:**
1. **Perimeter Security:** Prevent unauthorized site access
2. **Building Access Control:** Restrict entry to authorized personnel only
3. **Customer Data Protection:** Isolate customer cages/suites in multi-tenant deployments
4. **Surveillance:** 24/7 video monitoring and recording
5. **Intrusion Detection:** Real-time alerting for security breaches

**Security Layers:**
- **Layer 1:** Site perimeter (fence, gates, barriers)
- **Layer 2:** Building perimeter (doors, windows, vehicle barriers)
- **Layer 3:** Internal access control (data hall, electrical rooms, NOC)
- **Layer 4:** Customer cage/suite access (individual customer spaces)

## 8.2 Perimeter Security

**Perimeter Fencing:**
- **Fence Type:** 8 ft chain-link with barbed wire or ornamental steel (per local zoning requirements)
- **Gates:** Automated sliding gate for vehicle access + pedestrian gate
- **Access Control:** Card reader or keypad at vehicle gate; intercom with NOC for visitor management
- **Clearance:** 10-20 ft clear zone inside fence (no obstructions for surveillance coverage)

**Vehicle Barriers:**
- **Crash-Rated Bollards:** K4 or K12 rated bollards at building entry points (protects against vehicle ramming)
- **Location:** Around critical equipment (generators, BESS enclosure, utility transformer)
- **Standards:** ASTM F2656 / DOS SD-STD-02.01 crash rating

**Perimeter Detection:**
- **Fence-Mounted Sensors:** Vibration or fiber optic intrusion detection on perimeter fence
- **Cameras:** Coverage of all fence sections, gates, and building perimeter (see Section 8.4)

## 8.3 Building Access Control

**Access Control System:**
- **Technology:** Proximity card or biometric (fingerprint/facial recognition) readers
- **Integration:** Networked access control system integrated with BMS/DCIM and video surveillance
- **Credential Management:** Centralized database for adding/removing user credentials
- **Audit Trail:** All access events logged with timestamp, user ID, and door location

**Access Levels:**
- **Level 1 (Facility Staff):** Full access to all areas except customer cages
- **Level 2 (Customer):** Access to assigned customer cage/suite only
- **Level 3 (Vendor/Contractor):** Escorted access, temporary credentials
- **Level 4 (Visitor):** Reception area only, must be escorted

**Critical Access Points:**
- **Building Entry:** Main entrance with reception desk + man-trap (double-door airlock with card reader)
- **Data Hall Entry:** Card reader + PIN or biometric (two-factor authentication)
- **Electrical Rooms:** Card reader (restricted to facility staff and authorized vendors)
- **Mechanical Rooms:** Card reader (restricted to facility staff and authorized vendors)
- **NOC:** Card reader (restricted to operations staff)

**Man-Trap Configuration:**
- **Purpose:** Prevents tailgating (unauthorized follow-in)
- **Operation:** Outer door must close and latch before inner door can open
- **Override:** Fire alarm triggers both doors to unlock (life safety compliance)

## 8.4 Video Surveillance (CCTV)

**Camera Coverage:**
- **Perimeter:** All fence lines, gates, and building exterior (360° coverage)
- **Building Entry Points:** All doors (exterior and data hall entry)
- **Data Hall:** Wide-angle cameras covering aisles (not directed into customer cages for privacy)
- **Equipment Yards:** Generator yard, chiller yard, BESS enclosure, transformer pad
- **Interior Critical Areas:** NOC, electrical rooms, mechanical rooms (entry points)

**Camera Specifications:**
- **Resolution:** 4MP or higher (1080p minimum)
- **Type:** IP cameras with PoE (Power over Ethernet)
- **Features:** Night vision (IR LEDs), motion detection, tamper detection
- **Frame Rate:** 15-30 fps (higher for critical areas like man-trap)

**Video Management System (VMS):**
- **Recording:** Network Video Recorder (NVR) with redundant storage
- **Retention:** 90 days minimum (180 days preferred for forensic analysis)
- **Storage Capacity:** ~50-100 TB (varies by camera count and retention period)
- **Remote Access:** NOC operators can view live/recorded video via secure network
- **Integration:** VMS integrated with access control (view video on access event triggers)

**Analytics:**
- Motion detection zones (reduce false alarms)
- Object left behind detection (unattended bag/package)
- Perimeter crossing detection (virtual tripwire)
- Facial recognition (optional, for high-security deployments)

## 8.5 Intrusion Detection

**Intrusion Detection System (IDS):**
- **Door Contacts:** Magnetic door contacts on all exterior doors and critical interior doors
- **Motion Sensors:** Passive infrared (PIR) motion detectors in unoccupied areas during off-hours
- **Glass Break Detectors:** Acoustic sensors on windows (if windows present)
- **Duress Buttons:** Panic buttons at reception desk and NOC for emergency situations

**Alarm Response:**
- **Local Alarm:** Audible alarm (can be silenced to avoid alerting intruder)
- **NOC Alert:** Immediate notification to NOC operators
- **Central Station Monitoring:** Alarm forwarded to off-site security monitoring center
- **Law Enforcement:** NOC or central station contacts local police for confirmed intrusions

**Integration with Fire Alarm:**
- Security system must not impede life safety egress (doors unlock on fire alarm)
- Dual alarms (fire + intrusion) require prioritization (fire alarm takes precedence)

## 8.6 Customer Cage Security

**Physical Separation:**
- **Cages:** Floor-to-ceiling steel mesh partitions (e.g., 8' or 10' height)
- **Doors:** Lockable cage doors with electronic access control
- **Roof:** Cage roof or ceiling-mounted mesh to prevent climbing over

**Access Control:**
- **Customer-Controlled Access:** Customers manage their own user credentials for cage access
- **Biometric Option:** Customer can deploy additional biometric readers at cage door
- **Audit Trail:** All cage access events logged and available to customer via DCIM portal

**Surveillance:**
- Cameras provide general data hall coverage but do not directly view inside customer cages (privacy)
- Customer may deploy their own cameras inside cage

---

# 9. TELECOMMUNICATIONS & CONNECTIVITY

## 9.1 Telecommunications Overview

The facility is designed to provide high-bandwidth, diverse, and redundant connectivity for customer workloads.

**Connectivity Objectives:**
1. **Carrier Diversity:** Multiple telecommunications carriers (ISPs, dark fiber, cloud on-ramps)
2. **Physical Path Diversity:** Redundant fiber entry points from different directions
3. **Low Latency:** Proximity to Google Pryor campus enables GCP (Google Cloud Platform) interconnection
4. **Scalability:** Meet-Me-Room (MMR) sized for 10+ carriers

**Connectivity Strategy:**
- **Carrier-Neutral:** Open access for all carriers (no exclusivity agreements)
- **Cross-Connect Model:** Customers order cross-connects from MMR to customer cages
- **Cloud On-Ramps:** Direct connections to GCP, AWS, Azure via carrier partners

## 9.2 Fiber Entry & Path Diversity
**Fiber Entry Points:**
- **Primary Entry:** Fiber entrance from north or east side of building
- **Secondary Entry (Diversity):** Fiber entrance from south or west side (opposite side of building)
- **Physical Separation:** Entry conduits separated by >100 ft and routed through different utility vaults

**Conduit Infrastructure:**
- **Conduit Size:** 4-6" conduits from property line to MMR
- **Quantity:** 4-6 conduits per entry point (redundancy + future capacity)
- **Material:** PVC or HDPE conduits with pull rope installed
- **Vault:** Telecommunications vault at property line for carrier hand-off

**Fiber Route Analysis:**
Camelot is conducting fiber route analysis (Task 3, expected delivery early November 2025) to:
- Identify existing fiber routes near site
- Map carrier availability (AT&T, Cox, Level3/CenturyLink, Zayo, etc.)
- Confirm physical diversity (separate routes for redundancy)
- Estimate connectivity installation timeline and costs

**Action Required:** Review Camelot fiber analysis and confirm carrier diversity strategy. Negotiate Service Level Agreements (SLAs) with minimum two carriers for redundancy.

## 9.3 Meet-Me-Room (MMR)
The MMR is the telecommunications hub where carrier circuits enter the facility and cross-connects are made to customer equipment.

**MMR Specifications:**
- **Size:** ~500 SF (accommodates 10-15 carrier racks + cross-connect panels)
- <!-- @claude for a 10MW DC, is this the right sizing? -->
- **Location:** Ground floor, near fiber entry points
- **Rack Space:** 10-15 racks (42U height) for carrier equipment
- **Power:** Dedicated electrical panel, dual-feed circuits (A+B power from UPS/BESS)
- **Cooling:** Dedicated CRAC or CRAH unit (carrier equipment generates heat)
- **Fire Suppression:** Pre-action sprinkler or clean agent (coordinate with data hall system)

**Cross-Connect Infrastructure:**
- **Fiber Cross-Connect Panels:** LC or MTP fiber patch panels
- **Copper Cross-Connect:** 110-block or patch panels (for legacy circuits)
- **Cable Management:** Overhead ladder rack or wire basket tray for cross-connect cabling
- **Labeling:** All cross-connects labeled with customer ID, circuit ID, and carrier

**Carrier Onboarding Process:**
1. Carrier installs equipment in MMR rack
2. Carrier pulls fiber from entry vault to MMR
3. Carrier terminates fiber on cross-connect panel
4. Customer orders cross-connect from MMR to customer cage
5. Facility staff install fiber cross-connect (patch cable)

## 9.4 Main Distribution Area (MDA) & Backbone
**Main Distribution Area (MDA):**
- **Size:** ~300 SF (separate from MMR, within data hall or adjacent)
- **Purpose:** Facility backbone equipment (core switches, firewalls, monitoring)
- **Rack Space:** 4-6 racks for facility network equipment

**Backbone Architecture:**
- **Facility Network:** Management network for BMS, DCIM, security, access control
- **Customer Network:** Physically isolated from facility network
- **Redundancy:** Dual fabric (A+B switches) for facility network
- **Bandwidth:** 10 Gbps or 40 Gbps backbone links

## 9.5 Google Cloud Platform (GCP) Interconnection

**Proximity Advantage:**
The data center is approximately 4 miles from Google Pryor campus, enabling low-latency direct interconnection to GCP.

**Interconnection Options:**
1. **Dedicated Interconnect:** Direct fiber connection from data center to Google Pryor campus
   - Bandwidth: 10 Gbps or 100 Gbps per circuit
   - Latency: <1 ms (sub-millisecond due to proximity)
   - Cost: ~$1,700/month per 10 Gbps circuit (Google pricing)
2. **Partner Interconnect:** Via carrier partners (e.g., Equinix, Megaport)
   - Bandwidth: 50 Mbps to 50 Gbps
   - Latency: <2 ms (depends on carrier routing)
   - Cost: Varies by partner

**Feasibility:**
- Confirm availability of dark fiber route from data center to Google Pryor campus (via Camelot fiber study)
- Negotiate with Google for Dedicated Interconnect colocation at Pryor campus
- If dark fiber not feasible, leverage Partner Interconnect via carrier presence in MMR

**Customer Value Proposition:**
- Low-latency GCP access (ideal for AI/ML workloads, real-time applications)
- Hybrid cloud deployments (on-prem + GCP seamlessly integrated)
- Reduced data egress costs (direct connection bypasses internet)

---

# 10. MONITORING, CONTROLS & AUTOMATION

## 10.1 Monitoring & Control Overview
An integrated monitoring and control system ensures reliable operations, rapid fault detection, and energy optimization.

**System Integration Architecture:**
- **Building Management System (BMS):** Controls HVAC, fire, security, lighting
- **Data Center Infrastructure Management (DCIM):** Monitors power, cooling, environmental conditions at rack level
- **Energy Management System (EMS):** Manages solar, BESS, microgrid operations (see Section 4.3)
- **Integration Layer:** BACnet, Modbus, or SNMP protocols enable cross-system communication

**Monitoring Objectives:**
1. **Operational Visibility:** Real-time dashboards for NOC operators
2. **Fault Detection:** Immediate alerting for off-normal conditions
3. **Energy Optimization:** Automated controls to minimize PUE
4. **Capacity Planning:** Trending data for rack power, cooling utilization, UPS/BESS SOC
5. **Customer Transparency:** Customer portal for viewing rack power, cooling, environmental data

## 10.2 Building Management System (BMS)

The BMS is the central control system for all non-IT building systems.

**BMS Scope:**
- **HVAC:** Chiller plant, pumps, DX units, CRAH units, CDUs
- **Electrical:** Generator status, UPS/BESS status, switchgear status (monitoring only, not control)
- **Fire Alarm:** Integration for monitoring (fire alarm panel retains control)
- **Security:** Access control and video surveillance integration
- **Lighting:** Occupancy-based lighting control in office/NOC areas
- **Environmental:** Temperature, humidity, leak detection sensors

**BMS Platform:**
- **Vendor:** Schneider Electric EcoStruxure (recommended for RD109 integration), Siemens Desigo, Johnson Controls Metasys
- **Architecture:** Networked controllers with web-based HMI (Human-Machine Interface)
- **Protocols:** BACnet/IP (primary), Modbus TCP (legacy equipment)

**BMS Control Strategies:**
- **Free Cooling Optimization:** Automatically switch chillers between free cooling, partial mechanical, and full mechanical modes based on outdoor temperature
- **Chilled Water Setpoint Reset:** Increase supply water temperature during low-load conditions (reduces chiller energy)
- **Pump VFD Control:** Modulate pump speed based on differential pressure setpoint (reduces pumping energy)
- **Equipment Rotation:** Rotate chillers, pumps, and CDUs to equalize runtime and wear

**Alarms & Notifications:**
- **Critical Alarms:** Immediate SMS/email to on-call engineer (e.g., chiller failure, high temperature in data hall)
- **Warning Alarms:** BMS dashboard notification (e.g., chiller approaching high head pressure)
- **Escalation:** If no acknowledgment within 15 minutes, escalate to backup on-call engineer

## 10.3 Data Center Infrastructure Management (DCIM)
DCIM provides granular monitoring and reporting at the rack and device level.

**DCIM Scope:**
- **Power Monitoring:** Real-time kW, kWh, voltage, current, power factor per rack (via RPP or rack PDU)
- **Cooling Monitoring:** Chilled water flow rate, supply/return temperature per rack (if RDHx deployed)
- **Environmental Monitoring:** Temperature and humidity sensors at rack level (top, middle, bottom of racks)
- **Asset Management:** Rack inventory, customer assignment, equipment serial numbers
- **Capacity Planning:** Power and cooling utilization trending, heatmaps, "what-if" scenario modeling

**DCIM Platform:**
- **Vendor:** Schneider Electric EcoStruxure IT (recommended), Nlyte, Sunbird
- **Integration:** Pulls data from BMS, UPS/BESS, rack PDUs, environmental sensors
- **Customer Portal:** Web portal for customers to view their rack power/cooling utilization

**Key DCIM Features:**
- **PUE Calculation:** Real-time PUE calculation (facility power / IT power) with trending
- **Capacity Alerts:** Warn when rack power approaches circuit breaker limits (e.g., >80% of rated capacity)
- **Thermal Mapping:** 3D thermal visualization of data hall (identify hot spots)
- **Change Management:** Workflow for tracking rack installations, moves, changes

## 10.4 Energy Management System (EMS)

The EMS is the control system for the solar + BESS + generator microgrid (see Section 4.3 for detailed requirements).

**EMS Scope:**
- **Microgrid Controller:** Coordinates utility, solar, BESS, generators, and data center load
- **BESS State Management:** Optimize charging/discharging to extend battery life
- **Generator Dispatch:** Auto-start generators when BESS SOC reaches threshold
- **Solar Curtailment:** Prevent reverse power flow to utility (if not permitted)
- **Predictive Analytics:** Solar forecasting, load prediction

**Integration with BMS/DCIM:**
- EMS provides real-time power flow data to BMS/DCIM (e.g., "Solar generating 8.2 MW, BESS discharging 1.5 MW")
- BMS can request load shedding from DCIM in emergency scenarios (e.g., if BESS SOC critical and generators fail to start)

## 10.5 Network Operations Center (NOC)

**NOC Functionality:**
- **Operator Workstations:** 2-3 workstations with dual monitors
- **Video Wall:** Large display showing BMS dashboards, DCIM capacity, video surveillance feeds
- **Staffing:** 24/7 staffing model or remote monitoring (see Section 11.2)
- **Responsibilities:**
  - Monitor alarms from BMS, DCIM, EMS, fire, security
  - Dispatch technicians for critical issues
  - Coordinate customer access and vendor access
  - Maintain shift logs and incident reports

**Remote Monitoring Option:**
- If 24/7 on-site NOC is not cost-effective initially, use remote monitoring service
- Remote NOC operators view BMS/DCIM dashboards from off-site location
- Local on-call technician responds to alarms within 30-60 minutes

---

# 11. OPERATIONS & MAINTENANCE STRATEGY

## 11.1 Operations Overview

The operations strategy ensures reliable uptime, rapid incident response, and continuous performance optimization.

**Operational Model Options:**
1. **Owner-Operated:** Saga Energy hires and manages facility operations staff
2. **Third-Party Operator:** Engage data center operations service provider (e.g., CBRE, JLL, Cushman & Wakefield)
3. **Hybrid Model:** Owner manages critical systems (power, cooling), third-party manages security and customer support

**Recommendation:** Start with hybrid model (minimize headcount while maintaining control of critical systems). Transition to owner-operated as customer count grows.

## 11.2 Staffing & Roles

**Minimum Staffing Plan (Hybrid Model):**
- **Facility Manager:** 1 FTE (full-time employee)
  - Responsibilities: Vendor management, customer relations, budget management, compliance
- **Chief Engineer:** 1 FTE
  - Responsibilities: Maintenance planning, troubleshooting, BMS/DCIM oversight, project management
- **Facility Technicians:** 2 FTE (rotating shifts for on-call coverage)
  - Responsibilities: Preventive maintenance, reactive maintenance, customer support (rack installations)
- **NOC Operators:** 0 FTE initially (remote monitoring service), scale to 3-4 FTE for 24/7 on-site NOC as customer count grows
- **Security:** 0 FTE (remote video monitoring + access control system), add on-site security if required by customer SLAs

**Total Headcount:** 4 FTE initially, scale to 8-10 FTE at full occupancy.

## 11.3 Preventive Maintenance (PM) Program

Preventive maintenance minimizes unplanned downtime and extends equipment life.

**PM Schedule:**

**Electrical Systems:**
- **Generators:** Monthly load test (30-60 minutes), annual full-load test (4-8 hours), oil sampling every 500 hours
- **UPS/BESS:** Quarterly battery health checks, annual BESS cell balancing (if applicable), inverter firmware updates
- **Transformers:** Annual thermographic scan, oil sampling (if liquid-filled), tightness checks
- **Switchgear:** Annual infrared scan, contact resistance testing every 3 years
- **Rack PDUs:** Annual visual inspection, firmware updates

**Mechanical Systems:**
- **Chillers:** Quarterly refrigerant level checks, annual compressor oil analysis, coil cleaning every 6 months
- **Pumps:** Quarterly vibration analysis, annual motor bearing lubrication, coupling alignment check
- **CDUs:** Monthly filter changes, quarterly leak checks, annual heat exchanger cleaning
- **CRAH Units:** Monthly filter changes, quarterly coil cleaning, annual fan bearing lubrication

**Fire & Life Safety:**
- **Fire Alarm:** Quarterly detector testing (smoke, heat, gas), annual full system functional test
- **Suppression:** Annual agent cylinder weighing (clean agent), quarterly valve inspections (sprinkler)
- **Emergency Lighting:** Monthly battery test, annual 90-minute discharge test

**Security & Building Systems:**
- **Access Control:** Quarterly credential audit (remove terminated users), annual door hardware check
- **CCTV:** Monthly camera cleaning, quarterly DVR/NVR storage health check
- **HVAC (Office):** Quarterly filter changes, annual coil cleaning

**PM Software:**
- Use Computerized Maintenance Management System (CMMS) to schedule and track PM tasks
- Recommended platforms: IBM Maximo, UpKeep, FacilityBot

## 11.4 Commissioning Plan

Commissioning validates that all systems perform as designed before customer occupancy.

**Commissioning Phases:**

**Phase 1: Factory Acceptance Testing (FAT):**
- Critical equipment tested at manufacturer's factory before shipment (e.g., chillers, generators, UPS, BESS)
- Witness tests: Startup, full-load operation, protective relay operation, communication protocols

**Phase 2: Installation & Startup:**
- Equipment installed per manufacturer specifications
- Startup assistance from manufacturer field service engineers
- Initial operational testing (e.g., run generators at 50% load, run chillers in free cooling mode)

**Phase 3: Integrated Systems Testing (IST):**
- Test interaction between systems (e.g., chiller failure triggers alarm in BMS, BMS sheds load in DCIM)
- Failure mode testing: Simulate single-point failures and verify N+1 redundancy operates as designed
  - Example: Disconnect one chiller, verify remaining chillers pick up load without temperature excursion
- Microgrid mode testing (if BESS-as-UPS selected):
  - Islanding test: Disconnect utility, verify BESS maintains power, generators start at low SOC threshold
  - Resynchronization test: Verify seamless transition from island mode back to grid-connected mode

**Phase 4: Performance Verification:**
- Measure actual PUE under various load conditions (25%, 50%, 75%, 100% IT load)
- Validate cooling capacity (operate at design IT load, measure data hall temperature/humidity)
- Confirm power quality (voltage regulation, frequency stability, harmonic distortion)

**Phase 5: Documentation & Training:**
- As-built drawings delivered by contractors
- O&M manuals compiled and organized
- Staff training on BMS, DCIM, generator operation, emergency procedures
- Customer training on access control, cage access, cross-connect procedures

**Commissioning Authority:**
- Engage independent commissioning agent (CA) to oversee commissioning process
- CA validates test procedures, witnesses tests, documents deficiencies, verifies corrections

## 11.5 Incident Response & Business Continuity

**Incident Classification:**
- **Severity 1 (Critical):** Data hall outage, fire, security breach - Immediate response
- **Severity 2 (High):** Single-point failure in redundant system (e.g., one UPS offline) - Response within 1 hour
- **Severity 3 (Medium):** Non-critical system failure (e.g., office HVAC) - Response within 4 hours
- **Severity 4 (Low):** Cosmetic or minor issues - Response within 24 hours

**Incident Response Procedures:**
1. **Detection:** BMS/DCIM alarm triggers NOC notification
2. **Assessment:** NOC operator reviews alarm, checks video surveillance, contacts on-site staff
3. **Escalation:** If Severity 1 or 2, page on-call engineer and facility manager
4. **Resolution:** Technician dispatched to site, troubleshoots issue, restores service
5. **Documentation:** Incident report created in CMMS with root cause analysis and corrective actions

**Emergency Procedures:**
- **Fire:** Follow NFPA 101 evacuation procedures, contact fire department, suppress fire with automatic system
- **Utility Outage:** BESS provides backup power, generators start after 4 hours (or immediately if BESS unavailable)
- **Cooling Failure:** Shed non-critical IT load if temperature rises above ASHRAE A1 limits, activate backup cooling (N+1 redundancy)
- **Security Breach:** Lock down facility, contact law enforcement, review video surveillance footage

**Business Continuity:**
- Maintain spare parts inventory for critical components (UPS batteries, chiller compressors, pump motors)
- Establish vendor service contracts with 4-hour or 24-hour response times (e.g., generator manufacturer, chiller OEM)
- Document recovery time objectives (RTO) and recovery point objectives (RPO) for each system

---

# 12. SUSTAINABILITY & ENVIRONMENTAL

## 12.1 Sustainability Overview

The facility is designed to minimize environmental impact while delivering high-performance infrastructure.

**Sustainability Pillars:**
1. **Renewable Energy:** On-site solar + BESS to maximize clean energy utilization
2. **Energy Efficiency:** Target PUE 1.2-1.3 through free cooling, efficient equipment, and optimized controls
3. **Water Conservation:** Zero water consumption for cooling (closed-loop air-cooled chillers)
4. **Site Stewardship:** Minimal site disturbance, native landscaping, stormwater management

**Alignment with Corporate Sustainability Goals:**
Saga Energy's renewable energy strategy positions this facility as a best-in-class sustainable data center, enabling customer carbon footprint reduction and ESG (Environmental, Social, Governance) reporting.

## 12.2 Renewable Energy & Carbon Reduction

**On-Site Solar Array:**
- **Capacity:** 12 MW DC solar PV array
- **Annual Generation:** ~19-24 GWh/year
- **Renewable Penetration:** 60-80% of annual data center energy consumption from on-site solar *(preliminary estimate pending Camelot net load analysis)*
- **Carbon Offset:** ~12,000-16,000 metric tons CO2e per year (vs. grid electricity at 800 kg CO2e/MWh SPP average)

**Battery Energy Storage System (BESS):**
- **Function:** Stores excess solar energy for nighttime use, reducing reliance on grid power
- **Chemistry:** Lithium Iron Phosphate (LFP) - safer and longer-lived than NMC chemistries
- **End-of-Life:** BESS recycling plan required (lithium recovery, second-life applications)

**Generator Emissions Reduction:**
- If natural gas turbines selected: 30-50% lower NOx and particulate emissions vs. diesel generators
- 87% reduction in annual generator runtime (vs. traditional UPS-only architecture) due to extended BESS backup duration

**Renewable Energy Certificates (RECs):**
- If utility net metering or front-of-meter solar configuration is selected, consider monetizing RECs
- RECs provide additional revenue stream (~$1-5/MWh depending on market)

## 12.3 Energy Efficiency & PUE Optimization

**Target PUE:** 1.2-1.3 (annual average)

**PUE Breakdown:**
- IT Load: 7.4 MW (denominator)
- Cooling Load: ~1.2-1.8 MW (varies by season)
- UPS/BESS Losses: ~0.2-0.4 MW (depends on architecture)
- Lighting & Support: ~0.2-0.3 MW
- Total Facility Load: ~9-9.5 MW
- PUE = 9.5 / 7.4 = 1.28

**Efficiency Strategies (Detailed in Section 5.8):**
1. Extended free cooling (Oct-Apr in Oklahoma climate)
2. Variable speed drives (VFDs) on all pumps and fans
3. High chilled water supply temperature (50°F vs. 45°F typical)
4. Hot aisle containment (prevents hot/cold air mixing)
5. LED lighting with occupancy sensors
6. BESS-as-UPS (eliminates 4-8% UPS conversion losses if selected)

**Continuous Optimization:**
- Monthly PUE reporting to track performance trends
- Annual retro-commissioning to identify efficiency degradation (e.g., fouled coils, pump wear)
- Benchmarking against Uptime Institute Global Data Center Survey (median PUE ~1.58; target <1.30)

## 12.4 Water Conservation

**DEVIATION: Zero Water Consumption for Cooling**

**RD109 Baseline:**
- Adiabatic fluid coolers consume water via evaporative pre-cooling
- Estimated water usage: 1-2 million gallons/year (TBD via detailed calculation)

**Saga Pryor Design:**
- Eliminate adiabatic fluid coolers (see Section 5.2)
- Air-cooled chillers with integrated free cooling (closed-loop, no evaporation)
- **Water Usage: ~0 gallons/year for cooling** (only domestic water for staff use)

**Benefits:**
- Eliminates water cost and supply risk (important in drought-prone regions)
- Strong sustainability narrative for investor presentations and customer proposals
- Reduces permitting complexity (no water rights or wastewater discharge permits)

**Comparison to Industry:**
- Traditional data centers: 1.8 liters of water per kWh (evaporative cooling)
- Saga Pryor: 0 liters per kWh (air-cooled only)
- Annual water savings: ~60-80 million liters (vs. evaporative cooling)

## 12.5 Site & Environmental Stewardship

**Site Development:**
- **Minimal Grading:** Site topography is relatively flat; minimize cut/fill operations
- **Native Landscaping:** Use native Oklahoma species for landscaping (drought-tolerant, low maintenance)
- **Stormwater Management:** Detention/retention ponds to prevent erosion and downstream flooding
- **Low-Impact Development (LID):** Permeable paving, bioswales, rain gardens where feasible

**Wetlands & Habitat:**
- **Pre-Construction Survey:** Water delineation study to identify wetlands or protected habitats
- **Avoidance:** Site data center and solar array to avoid wetland areas (if present)
- **Mitigation:** If wetland impacts unavoidable, purchase wetland mitigation credits per Oklahoma DEQ requirements

**Construction Waste:**
- **Recycling Goal:** 75% construction waste diverted from landfill (concrete, metal, wood, cardboard)
- **LEED Alignment:** Track waste diversion metrics for potential LEED documentation

**Operational Waste:**
- **E-Waste Recycling:** Decommissioned IT equipment recycled per R2 (Responsible Recycling) or e-Stewards standards
- **Battery Recycling:** UPS batteries and BESS cells recycled at end-of-life (lithium recovery)

## 12.6 Sustainability Certifications

**LEED (Leadership in Energy and Environmental Design):**
- **Target Certification:** LEED Silver or Gold (Data Centers category)
- **Key Credits:**
  - Energy Performance (EA Credit 1): PUE 1.2-1.3 qualifies for high points
  - Renewable Energy (EA Credit 2): On-site solar array (60-80% renewable penetration)
  - Water Efficiency (WE Credit 2): Zero water cooling system
  - Construction Waste Management (MR Credit 2): 75% waste diversion
- **Benefits:** Marketing differentiation, tenant attraction (ESG-focused customers), potential insurance/financing benefits
- **Cost:** LEED certification fees ~$25-50K, plus ~2-5% construction cost premium for documentation/compliance

**Energy Star for Data Centers:**
- **Eligibility:** PUE <1.5 qualifies for Energy Star certification
- **Process:** Annual benchmarking via Energy Star Portfolio Manager
- **Benefits:** Federal tax incentives (Section 179D deduction for energy-efficient commercial buildings)

**Other Certifications (Optional):**
- **Uptime Institute Tier Certification:** Tier III certification validates N+1 redundancy and concurrent maintainability (useful for customer confidence)
- **ISO 50001 (Energy Management):** Demonstrates commitment to continuous energy performance improvement

**Decision:** Recommend pursuing LEED Silver at minimum (strong ROI via marketing and customer attraction). Evaluate Uptime Tier III if hyperscale customers require third-party validation.

---

# 13. DEVIATIONS FROM RD109 BASELINE

## 13.1 Summary of Deviations

This section consolidates all deviations from the Schneider Electric RD109 Reference Design baseline, with technical rationale and cost/schedule impacts.

**Purpose of RD109 Baseline:**
The RD109 provides a validated, proven architecture for 7.4 MW data centers. Deviations are made to:
1. Optimize for Oklahoma climate (vs. Dallas baseline)
2. Integrate renewable energy and microgrid functionality
3. Reduce costs where RD109 is over-specified for this application
4. Align with Saga Energy business model (power pass-through pricing, colocation flexibility)

**Total Cost Impact of Deviations:** -$6M to -$10M net CAPEX savings (depends on final decisions)

## 13.2 Major Deviations

### Deviation 1: BESS-as-UPS Architecture (PENDING DECISION #5)

**RD109 Baseline:**
- 8× 1,500 kW Galaxy VX UPS units (N+1 redundancy in 2N configuration)
- 32× Lithium-ion battery cabinets (17 modules each) for IT load
- 2× 200 kW Galaxy VL UPS units + 2× battery cabinets for mechanical load
- Total UPS CAPEX: ~$8-10M

**Saga Pryor Design (If BESS-as-UPS Selected):**
- ❌ Eliminate all traditional UPS units and batteries
- ✅ **16 MW / 48 MWh BESS** with grid-forming inverters (N+1 configuration), phased deployment
  - Phase 1: 3×4MW inverters + full 48MWh battery (8MW available N+1)
  - Phase 2: 4th 4MW inverter (12MW available N+1)
- ✅ IEEE 2030.7/2030.8 compliant microgrid controller
- ✅ Dual-purpose function: Solar storage + UPS power conditioning

**Rationale:**
- BESS provides **Phase 1: 6 hours @ 8MW; Phase 2: 4.8 hours @ 10MW facility load** (vs. 10-15 minutes for traditional UPS)
- Eliminates redundant battery investment (one BESS serves both solar storage and backup power functions)
- Reduces generator runtime by 87% (lower fuel costs, emissions, maintenance)
- Phased deployment defers ~$2-3M CAPEX, aligns with facility lease-up

**Cost Impact:**
- **Phase 1 CAPEX:** $29.7-31.2M (supports ~75% occupancy)
- **Phase 2 Incremental:** +$2.8-3.5M (triggered at ~75% leased)
- **Total CAPEX Savings:** **-$7.3M to -$9.3M (-18% to -23%)** vs. traditional
- **OPEX Savings:** -$445K/year (no UPS maintenance + reduced generator runtime)
- **Cash Flow Benefit:** Defers $2-3M by 8-12 months

**Schedule Impact:** Neutral (BESS procurement ~12-16 weeks, similar to UPS lead times)

**Risk Mitigation:**
- Requires BESS vendor validation of grid-forming inverter capability meeting ITIC curve
- Insurance underwriters must approve BESS-only architecture
- Saga Energy commits to BESS-specific operations training

**Decision Required:** End of October 2025

### Deviation 2: Natural Gas Turbines as Primary Backup Power (PENDING DECISION #2)

**RD109 Baseline:**
- 4× 3,750 kVA diesel generators (IT load)
- 2× 1,705 kVA diesel generators (mechanical load)
- Double-wall sub-base fuel tanks (1,320 gallons each)

**Saga Pryor Design (If Natural Gas Turbines Selected):**
- ❌ Eliminate diesel generators and fuel tanks
- ✅ Natural gas turbines (sizing TBD - requires vendor engineering study)
- ✅ Pipeline natural gas service (capacity confirmation required)

**Rationale:**
- Unlimited runtime (no on-site fuel storage constraints)
- Lower emissions vs. diesel (NOx, particulates, CO2)
- No diesel fuel storage tanks (eliminates EPA SPCC plan, reduces environmental permitting)
- Lower fuel cost (~$4-6/MMBtu for natural gas vs. ~$3-4/gallon for diesel)

**Cost Impact:**
- Natural gas turbines: Similar CAPEX to diesel generators (~$1,000-1,500/kW installed)
- Fuel tank elimination: -$200-400K savings
- Natural gas service installation: +$100-300K (piping, meter, interconnection fees)
- **Net CAPEX Impact:** -$100K to -$300K savings

**Schedule Impact:** +2-4 weeks (natural gas service interconnection study and installation)

**Considerations:**
- Turbine redundancy strategy differs from reciprocating engines (research required)
- Natural gas service must be confirmed with Oklahoma Natural Gas or local provider
- Fallback: If natural gas unavailable, use diesel or natural gas reciprocating generators

**Decision Required:** After natural gas service confirmation (October 2025)

### Deviation 3: Elimination of Raised Floor

**RD109 Baseline:**
- Raised floor system (18-24" height) for underfloor cable and cooling distribution
- Cost: ~$0.9M to -$1.25M for 25,000 SF data hall

**Saga Pryor Design:**
- ❌ Eliminate raised floor
- ✅ Structural slab-on-grade with overhead cable distribution
- ✅ All power and cooling distributed via overhead cable tray, busway, and piping

**Rationale:**
- Cost savings: -$0.9M to -$1.25M
- Faster construction: -2 to -4 weeks
- Superior structural stability for high-density racks (132 kW/rack AI workloads)
- Simpler cleaning and maintenance (no underfloor plenum to clean)

**Cost Impact:**
- **CAPEX Savings:** -$0.9M to -$1.25M

**Schedule Impact:** -2 to -4 weeks (eliminates raised floor installation time)

**Trade-offs:**
- Overhead distribution requires higher ceiling height (16-18 ft vs. 12-14 ft typical)
- Visual aesthetics: Exposed cable tray and busway vs. clean underfloor distribution

**Decision:** Confirmed (slab-on-grade selected)

### Deviation 4: Elimination of Adiabatic Fluid Coolers

**RD109 Baseline:**
- 5× Guntner GFD V-Shape adiabatic fluid coolers (1,478 kW each)
- Function: Pre-cool outdoor air via evaporative assist before entering chillers
- Cost: ~$750K to -$1M

**Saga Pryor Design:**
- ❌ Eliminate adiabatic fluid coolers
- ✅ Air-cooled chillers with integrated free cooling only
- ✅ Closed-loop system (zero water consumption for cooling)

**Rationale:**
- Zero water consumption (strong sustainability story)
- Simpler operation and maintenance (no water treatment, nozzle cleaning)
- Reduced environmental permitting (no water rights or wastewater discharge)

**Cost Impact:**
- Eliminate adiabatic coolers: -$750K to -$1M
- Larger air-cooled chillers: +$900K to +$1.3M (5-10% upsizing for peak summer performance)
- **Net CAPEX Impact:** +$150K to +$450K

**PUE Impact:** +0.02 to +0.05 during peak summer months (minimal annual impact due to extended free cooling season)

**OPEX Impact:** -$15K to -$25K/year (water cost + treatment + maintenance savings)

**Decision:** Recommended (proceed unless PUE modeling shows unacceptable degradation)

### Deviation 5: Rear-Door Heat Exchangers (RDHx) for Air-Cooled Racks (PENDING DECISION)

**RD109 Baseline:**
- Fan walls at end of hot aisles for air-cooled rack cooling
- Zonal cooling approach (serves entire row or zone)

**Saga Pryor Design (If RDHx Selected):**
- ❌ Eliminate fan walls
- ✅ Rear-Door Heat Exchangers (RDHx) on each air-cooled rack
- ✅ Rack-based cooling approach (individual rack control)

**Rationale:**
- **Per-customer control:** Each customer suite has isolated cooling capacity
- **Flexible billing:** Measure chilled water flow per rack for accurate cost allocation
- **Mixed density support:** Handle varying rack densities in same row without airflow conflicts
- **Scalability:** Add RDHx only where needed (not entire data hall upfront)

**Cost Impact:**
- RDHx units: +$3K to +$5K per rack
- Total for 48 network racks: +$144K to +$240K
- Fan wall elimination: -$100K to -$200K
- **Net CAPEX Impact:** +$44K to +$140K

**Trade-offs:**
- Higher upfront cost per rack
- More chilled water connections (more leak detection points)
- Better suited for flexible colocation vs. single-tenant master lease

**Decision Required:** Align cooling strategy with Saga Energy sales and marketing model (October 20 Midpoint Review)

### Deviation 6: Tornado Hardening (Oklahoma-Specific)

**RD109 Baseline:**
- Standard IBC wind design (115 mph basic wind speed for Dallas)
- Standard PEMB construction

**Saga Pryor Design:**
- ✅ EF-2 tornado resistance (135 mph winds) for critical areas
- ✅ FM Global compliant roof/wall panels (FM 1-90 or 1-120 wind uplift rating)
- ✅ Missile impact protection (steel roof deck with impact-resistant insulation)

**Rationale:**
- Oklahoma tornado risk requires enhanced wind resistance
- Insurance underwriting typically mandates FM Global compliance for data centers

**Cost Impact:**
- **CAPEX Premium:** +$150 to +$250/SF building envelope (~$3.75M to $6.25M for 25,000 SF data hall + support spaces)

**Decision:** Required (non-negotiable for insurance and life safety)

### Deviation 7: Addition of Staging/Burn-In Area

**RD109 Baseline:**
- No dedicated staging or burn-in space

**Saga Pryor Design:**
- ✅ Add 2,000 SF staging & burn-in area
- ✅ Dedicated power circuits for equipment testing
- ✅ Separate entry from data hall (prevents contamination)

**Rationale:**
- Accelerates customer onboarding (pre-deploy and test equipment before data hall installation)
- Prevents data hall contamination (cardboard dust, packing materials)
- Supports maintenance/repair workflows (staging area for equipment swaps)

**Cost Impact:**
- **CAPEX Premium:** +$300K to +$400K (building area + MEP + power circuits)

**Decision:** Recommended (strong ROI via faster customer onboarding)

### Deviation 8: Addition of Shower & Locker Facilities

**RD109 Baseline:**
- Basic restroom facilities only

**Saga Pryor Design:**
- ✅ Add ~700 SF shower & locker room
- ✅ Supports 24/7 operations and emergency response

**Rationale:**
- Enables staff to work extended shifts during emergencies (power outage, cooling failure)
- Supports 24/7 NOC operations (if on-site NOC is deployed)
- Improves employee satisfaction (exercise during breaks, bike/run commutes)

**Cost Impact:**
- **CAPEX Premium:** +$140K to +$175K

**Decision:** Recommended if 24/7 on-site operations model is selected

## 13.3 Minor Deviations

**Climate Optimization:**
- Chiller sizing adjusted for Pryor, OK climate (95°F dry bulb / 78°F wet bulb vs. Dallas 100°F / 78°F)
- Extended free cooling season (~215 days/year in Pryor vs. ~180 days in Dallas)
- Impact: -5% chiller capacity requirement

**Transformer Sizing:**
- RD109 does not specify utility substation transformer sizing
- Saga Pryor requires 12-15 MVA transformer to accommodate data center load + BESS charging
- Impact: +$200K to +$500K (if customer-owned transformer)

**BESS Fire Protection (If BESS Selected):**
- RD109 does not include BESS (not part of baseline)
- Saga Pryor requires NFPA 855-compliant fire suppression for BESS enclosure
- Impact: +$150K to +$300K (water mist or enhanced clean agent system)

**Google GCP Interconnection:**
- RD109 does not specify specific cloud on-ramps
- Saga Pryor proximity to Google Pryor campus enables low-latency GCP Dedicated Interconnect
- Impact: +$50K to +$200K (dark fiber installation or carrier circuit costs)

## 13.4 Decisions Still Pending

| Decision # | Item | Target Date | Impact if Delayed |
|---|---|---|---|
| Decision #1 | Utility Interconnection Strategy (single vs. dual POI) | Oct 2025 | Schedule risk: +6-18 months if major utility upgrades required |
| Decision #2 | Generator Fuel Type (nat gas turbines, nat gas recip, diesel) | Oct 2025 | Cost impact: ±$100K-300K |
| Decision #4 | Raised Floor Elimination | CONFIRMED | N/A (decision made: slab-on-grade) |
| Decision #5 | BESS-as-UPS Architecture with Phased Deployment | End of Oct 2025 | Cost impact: ±$7.3-9.3M; phasing defers $2-3M |
| BESS Phase 2 Trigger | Deploy at 50%/60%/75% occupancy | Set trigger in lease-up plan | Cash flow: timing of Phase 2 CAPEX deployment |
| RDHx Decision | Fan Walls vs. Rear-Door Heat Exchangers | Oct 20 Midpoint Review | Cost impact: ±$44K-140K |

---

## DOCUMENT STATUS & NEXT STEPS

**Current Status:** DRAFT - Complete Basis of Design (Sections 1-13)

**Review Requested:** Confirm technical approach, level of detail, and outstanding decisions before finalizing

**Next Steps:**
1. **Oct 20 Midpoint Review:** Present BoD Sections 1-6 to Saga Energy team, confirm approach
2. **Oct 25 Final BoD Delivery:** Incorporate feedback from midpoint review, finalize Sections 7-13
3. **Pending Decisions Closeout:** Work with Saga Energy to close Decision #1, #2, #5 by end of October
4. **Engineering Consultant Handoff:** Provide final BoD to MEP engineer for detailed design (November)

**Outstanding Actions Required:**
- Camelot fiber route analysis (Task 3) - Expected early November
- Camelot net load analysis (Task 2) - Expected early November
- Natural gas service confirmation with Oklahoma Natural Gas
- Utility interconnection study with OG&E
- BESS vendor validation of grid-forming capability
- Insurance underwriter review of BESS-only architecture (if Option A selected)

**Target Completion:** October 25, 2025 (per Project Plan Week 4 milestone)

**Prepared by:** PGCIS Program Management Team
**Date:** October 17, 2025

---

**Tags:** #saga-project #basis-of-design #rd109 #data-center #electrical #mechanical #renewable-energy #bess #microgrid

**Related Documents:**
- [[Feasibility Memo V3]]
- [[_Project Plan]]
- [[RD109_0.0_Table-Of-Contents_R10]]
- [[BESS as UPS Replacement - Feasibility Analysis V2]]
- [[Component Pricing Deep Dive - BESS vs UPS]]
