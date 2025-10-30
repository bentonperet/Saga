**Created:** 2025-10-23 10:35

# BASIS OF DESIGN - INTEGRATED AUTOMATION
## CSI Division 25
### Saga Energy – Pryor Data Center

**Parent Document:** [[Saga Pryor DC/Basis of Design/Benton_BOD/_BOD - Exec Summary and TOC]]
**Related:** [[Basis of Design - Part 2 Supporting Systems]] | [[Saga Pryor DC/Basis of Design/Benton_BOD/12BOD - Process Equipment (CSI Divs 40-48)]]

---

## OVERVIEW

Integrated monitoring and control systems ensure reliable operations, rapid fault detection, and energy optimization across the facility and microgrid.

**System Integration Architecture:**
- **Building Management System (BMS):** HVAC, fire, security, lighting control
- **Data Center Infrastructure Management (DCIM):** Power/cooling monitoring at rack level
- **Energy Management System (EMS):** Simplified power monitoring for solar + generator coordination
- **Integration Layer:** BACnet, Modbus, SNMP protocols for cross-system communication

**Note:** BESS-as-UPS rejected (Tier III violation). Economic BESS rejected (negative NPV). See [[Why BESS Should Not Be UPS]] and [[Excess Solar Monetization Strategy]] for details.

---

## BUILDING MANAGEMENT SYSTEM (BMS) {TBC}

### System Scope
- **HVAC:** Chiller plant, pumps, DX units, AHUs, CDUs
- **Electrical:** Generator status, UPS status, switchgear monitoring (monitoring only, not control)
- **Fire Alarm:** Integration for monitoring (fire alarm panel retains primary control)
- **Security:** Access control and video surveillance integration
- **Lighting:** Occupancy-based lighting in office/NOC areas
- **Environmental:** Temperature, humidity, leak detection sensors

### BMS Platform
- **Recommended Vendor:** Schneider Electric EcoStruxure (integrates with RD109 baseline equipment)
- **Alternatives:** Siemens Desigo, Johnson Controls Metasys
- **Architecture:** Networked controllers with web-based HMI (Human-Machine Interface)
- **Protocols:** BACnet/IP (primary), Modbus TCP (legacy equipment)

### Control Strategies

**Free Cooling Optimization:**
- Automatically switch chillers between free cooling, partial mechanical, and full mechanical modes based on outdoor temperature

**Chilled Water Setpoint Reset:**
- Increase supply water temperature during low-load conditions (reduces chiller energy)

**Pump VFD Control:**
- Modulate pump speed based on differential pressure setpoint (reduces pumping energy)

**Equipment Rotation:**
- Rotate chillers, pumps, and CDUs to equalize runtime and wear

### Alarms & Notifications
- **Critical Alarms:** Immediate SMS/email to on-call engineer (e.g., chiller failure, high data hall temperature)
- **Warning Alarms:** BMS dashboard notification (e.g., chiller approaching high head pressure)
- **Escalation:** If no acknowledgment within 15 minutes, escalate to backup on-call engineer

---

## DATA CENTER INFRASTRUCTURE MANAGEMENT (DCIM)

### System Scope
- **Power Monitoring:** Real-time kW, kWh, voltage, current, power factor per rack (via RPP or rack PDU)
- **Cooling Monitoring:** Chilled water flow rate, supply/return temperature per rack (if RDHx deployed)
- **Environmental Monitoring:** Temperature and humidity sensors at rack level (top, middle, bottom)
- **Asset Management:** Rack inventory, customer assignment, equipment serial numbers
- **Capacity Planning:** Power/cooling utilization trending, heatmaps, "what-if" scenario modeling

### DCIM Platform
- **Recommended Vendor:** Schneider Electric EcoStruxure IT
- **Alternatives:** Nlyte, Sunbird
- **Integration:** Pulls data from BMS, UPS, rack PDUs, environmental sensors
- **Customer Portal:** Web portal for customers to view their rack power/cooling utilization

### Key DCIM Features

**PUE Calculation:**
- Real-time PUE calculation (facility power / IT power) with trending
- Monthly reporting per The Green Grid guidelines

**Capacity Alerts:**
- Warn when rack power approaches circuit breaker limits (e.g., >80% of rated capacity)

**Thermal Mapping:**
- 3D thermal visualization of data hall (identify hot spots)

**Change Management:**
- Workflow for tracking rack installations, moves, changes

---

## ENERGY MANAGEMENT SYSTEM (EMS)

### Simplified Power Monitoring System

**EMS Scope (Without BESS):**
- **Power Monitoring:** Real-time power flow between utility, solar, generators, and data center load
- **Generator Dispatch:** Auto-start generators on utility outage (standard ATS function)
- **Solar Management:** Maximize solar self-consumption, curtail if needed
- **Power Quality Monitoring:** Voltage, frequency, harmonics, power factor
- **SCADA Integration:** 24/7 remote monitoring and control

**No IEEE 2030.7/2030.8 Compliance Required:**
- BESS-as-UPS was the only driver for advanced microgrid protocols
- Without BESS, standard generator ATS and solar inverter controls are sufficient
- Significant cost savings vs full microgrid controller

**Detailed requirements:** See [[Saga Pryor DC/Basis of Design/Benton_BOD/12BOD - Process Equipment (CSI Divs 40-48)]]

### Key Control Functions

**1. Generator Dispatch Logic:**
- Auto-start generators on utility outage (standard ATS function)
- Load sharing between generators (if multiple units online)
- Generator paralleling with utility (if designed for peak shaving)

**2. Solar Management:**
- Maximize solar self-consumption by data center
- Curtail solar if load drops below minimum and no export permitted
- Monitor inverter performance and fault conditions

**3. Power Quality Monitoring:**
- Continuous monitoring of voltage, frequency, harmonics, power factor
- Fault detection and isolation
- Automatic protective relay coordination

**4. Predictive Analytics (Optional):**
- Solar generation forecasting (weather-based)
- Data center load prediction (historical patterns)
- Minimal value without BESS to optimize

**5. SCADA Integration:**
- 24/7 remote monitoring and control
- Integration with BMS and DCIM
- Alarms and notifications for off-normal conditions

### Recommended EMS Platforms
- **Schneider Electric EcoStruxure Power Monitoring Expert** - Standard DC power monitoring (not full microgrid controller)
- **Siemens PowerManager** - Simplified alternative
- **Solar Inverter Built-In Controls** - May be sufficient for basic solar + grid coordination

**Cost:** $200-400K for simplified power monitoring system (vs $1.05-1.55M for full IEEE 2030.7/2030.8 microgrid controller)

**Cost Savings:** -$850K to -$1.15M by not requiring advanced microgrid controller

### Integration with BMS/DCIM
- EMS provides real-time power flow data to BMS/DCIM (e.g., "Solar generating 8.2 MW, utility importing 7.5 MW")
- BMS can request load shedding from DCIM in emergency scenarios (e.g., if generators fail to start during utility outage)

---

## NETWORK OPERATIONS CENTER (NOC)

### NOC Functionality
- **Operator Workstations:** 2-3 workstations with dual monitors
- **Video Wall:** Large display showing BMS dashboards, DCIM capacity, video surveillance feeds
- **Staffing:** 24/7 staffing model or remote monitoring (TBD based on operational model)
- **Responsibilities:**
  - Monitor alarms from BMS, DCIM, EMS, fire, security
  - Dispatch technicians for critical issues
  - Coordinate customer access and vendor access
  - Maintain shift logs and incident reports

### Remote Monitoring Option
- If 24/7 on-site NOC not cost-effective initially, use remote monitoring service
- Remote NOC operators view BMS/DCIM dashboards from off-site location
- Local on-call technician responds to alarms within 30-60 minutes

---

## INTEGRATION PROTOCOLS & STANDARDS

### Communication Protocols
- **BACnet/IP:** Primary protocol for BMS devices
- **Modbus TCP:** Legacy equipment integration
- **SNMP:** Network equipment monitoring
- **OPC UA:** Industrial automation and microgrid control

### Cybersecurity
- **Network Segmentation:** Separate facility network from customer IT network
- **Firewall Protection:** Perimeter firewalls for BMS/DCIM/EMS networks
- **Access Control:** Role-based access control (RBAC) for operator interfaces
- **Encryption:** TLS/SSL encryption for all remote access

---

## MONITORING OBJECTIVES

**1. Operational Visibility:**
- Real-time dashboards for NOC operators
- Historical trending for performance analysis

**2. Fault Detection:**
- Immediate alerting for off-normal conditions
- Automated escalation if no operator response

**3. Energy Optimization:**
- Automated controls to minimize PUE
- Continuous commissioning to identify efficiency degradation

**4. Capacity Planning:**
- Trending data for rack power, cooling utilization, solar generation
- Predictive analytics for capacity expansion planning

**5. Customer Transparency:**
- Customer portal for viewing rack power, cooling, environmental data
- Detailed billing reports (power consumption, cooling usage)

---

## COMMISSIONING & TESTING

### Integrated Systems Testing (IST)
- Test interaction between BMS, DCIM, and EMS
- Failure mode testing: Simulate single-point failures and verify N+1 redundancy
- Example: Disconnect one chiller, verify remaining chillers pick up load without temperature excursion

### Generator Failover Testing
- **Utility Loss Test:** Disconnect utility, verify generators start and pick up load within design timeframe (15-second transfer window covered by UPS)
- **Load Sharing Test:** Verify multiple generators share load properly when running in parallel
- **Resynchronization Test:** Verify seamless transition back to utility power when restored

---

## COST IMPACTS {TBC}

| System | Cost Estimate |
|---|---|
| BMS (Schneider EcoStruxure or equivalent) | ~$500K-1M |
| DCIM (EcoStruxure IT or equivalent) | ~$300-500K |
| Simplified EMS (power monitoring system) | ~$200-400K |
| NOC fit-out (workstations, video wall, furniture) | ~$200-400K |
| Integration and commissioning | ~$200-400K |
| **Total Integrated Automation** | ~$1.4-2.7M |

**Cost Savings Without BESS:**
- Avoided advanced microgrid controller: **-$850K to -$1.15M**
- Reduced commissioning scope: **-$100K**

---

**Tags:** #saga-project #bms #dcim #ems #microgrid-controls #csi-division-25

**Related Documents:**
- [[Saga Pryor DC/Basis of Design/Benton_BOD/_BOD - Exec Summary and TOC]] - Main title page
- [[Saga Pryor DC/Basis of Design/Benton_BOD/5BOD - HVAC (CSI Div 23)]] - HVAC control sequences
- [[Saga Pryor DC/Basis of Design/Benton_BOD/7BOD - Electrical (CSI Div 26)]] - Electrical monitoring
- [[Saga Pryor DC/Basis of Design/Benton_BOD/12BOD - Process Equipment (CSI Divs 40-48)]] - Microgrid integration details
