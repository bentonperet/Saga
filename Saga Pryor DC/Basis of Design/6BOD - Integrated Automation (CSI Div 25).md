**Created:** 2025-10-29
**Updated from:** Pryor_Bod_EVS_Rev01.md

# BASIS OF DESIGN - INTEGRATED AUTOMATION
## CSI Division 25
### Pryor Data Center - PACHYDERM GLOBAL

**Parent Document:** [[Saga Pryor DC/Basis of Design/Erik_BOD_Updated/_BOD - Exec Summary and TOC]]

---

## OVERVIEW

Integrated monitoring and control systems provide real-time visibility, automated optimization, and rapid fault response across electrical, mechanical, fire, and security systems. Microgrid controller coordinates 161kV utility, solar, BESS, and generators on common 13.8kV bus.

**System Integration Architecture:**
- **BMS (Building Management System):** HVAC, lighting, environmental control
- **EPMS (Electrical Power Monitoring System):** Utility, generators, UPS, transformers
- **Microgrid Controller:** Coordinates utility, solar, BESS, generators at 13.8kV
- **DCIM (Data Center Infrastructure Management):** Rack-level power, cooling, capacity
- **Fire Alarm System:** Life safety integration (monitoring only)
- **Access Control System:** Security integration

**Integration Layer:** BACnet/IP, Modbus TCP, OPC UA, SNMP

---

## BUILDING MANAGEMENT SYSTEM (BMS)

### System Scope

**HVAC Control & Monitoring:**
- 12 × air-cooled chillers (Loops 1+2+3)
- Chilled water pumps (primary + secondary)
- 60 × CDUs (Phase 2, direct-to-chip cooling)
- 30 × cabinet FCUs (fan speed, valve control)
- DOAS units (white space pressurization, humidity control)
- Rooftop units (office/support space comfort)

**Environmental Monitoring:**
- Temperature sensors: Data halls (16+ points), mechanical rooms, offices
- Humidity sensors: Data halls (8+ points), NOC
- Differential pressure: White space pressurization monitoring
- Leak detection: Data halls, mechanical rooms, CDU connections

**Lighting Control:**
- Occupancy-based dimming in offices, conference rooms
- Scheduled lighting in data halls (maintain minimum illumination 24/7)
- Emergency lighting status monitoring

**Integration Interfaces:**
- Fire alarm system (monitor status, trigger HVAC shutdown on alarm)
- Access control (door status, HVAC zone coordination)
- EPMS (utility status, generator run signals)

### BMS Platform

**Recommended Vendors:**
- Schneider Electric EcoStruxure Building Operation
- Siemens Desigo CC
- Johnson Controls Metasys

**Architecture:**
- **Head-end servers:** 2 × redundant servers (A/B, VM-based)
- **Field controllers:** DDC controllers at each major equipment piece
  - Chiller plant: 3 × plant controllers (Loops 1+2 shared, Loop 3 separate)
  - Data hall: 6 × zone controllers (environmental, FCUs, DOAS)
  - Support spaces: 4 × zone controllers (RTUs, lighting, misc)
- **Network:** Fiber backbone, copper to field devices
- **Protocols:** BACnet/IP (primary), Modbus TCP (legacy integration)
- **HMI:** Web-based graphical interface (HTML5, mobile-responsive)

### Control Strategies

**Free Cooling Optimization:**
- Monitor outdoor air temperature (OAT) continuously
- Mode 1: OAT <10°C → 100% free cooling (compressors off)
- Mode 2: OAT 10-15°C → Partial free cooling (part-load compressors)
- Mode 3: OAT >15°C → Full mechanical cooling
- Target: 3,500-4,000 hrs/year free cooling in Pryor, OK

**Chiller Sequencing:**
- Target 67% utilization per chiller for optimal efficiency
- Rotate chillers weekly to equalize runtime
- Stage chillers based on load (prevent short cycling)

**Pump VFD Control:**
- Modulate pump speed to maintain differential pressure setpoint
- ΔP setpoint: 15-20 psi at most remote cabinet/CDU
- Reduce pumping energy during part-load conditions

**Supply Water Temperature Reset:**
- Phase 1 (air cooling): 7-10°C supply, reset up during low load
- Phase 2 (Loop 3 D2C): 25°C supply, fixed (optimal for GPUs)

**White Space Environmental Control:**
- Maintain 18-27°C, 40-60% RH per ASHRAE A1
- DOAS modulates outdoor air dampers to maintain +0.02-0.05 in. w.g. pressure
- Humidification/dehumidification staged based on RH sensors

### Alarms & Notifications

**Critical Alarms (Immediate Response):**
- Chiller failure (redundancy loss)
- Data hall high temperature (>27°C)
- UPS on battery (utility loss)
- Fire alarm activation
- Leak detection
- **Notification:** SMS + email + audible alarm in NOC

**Warning Alarms (Investigation Required):**
- Equipment approaching setpoint limits
- Maintenance due (filter replacement, oil change)
- Low glycol level (makeup required)
- **Notification:** BMS dashboard + email

**Escalation:**
- If no acknowledgment within 15 minutes → escalate to backup on-call engineer
- If no acknowledgment within 30 minutes → escalate to manager

---

## ELECTRICAL POWER MONITORING SYSTEM (EPMS)

### System Scope

**Medium Voltage Monitoring (13.8kV):**
- 161kV/13.8kV substation transformers (2 × 25 MVA)
- 13.8kV dual ring bus (Ring A + Ring B)
- Ring main units (6 × RMUs, switching status)
- 13.8kV/480V transformers (8 × 3,500 kVA)

**Generator Monitoring:**
- 6 × 4.0 MW @ 13.8kV diesel generators
- Parameters: kW, kVA, voltage, frequency, fuel level, run hours
- Paralleling status, load sharing
- Fuel tank levels (with low-level alarms)

**Low Voltage Monitoring (480V):**
- Main switchboards (SWBD-A, SWBD-B)
- Distribution panels (IT, mechanical, UPS output)
- Branch circuits (major loads)

**IT UPS Monitoring:**
- Phase 1: 5-6 × 1,250 kVA IT UPS modules (N+1 architecture)
- Phase 2: 13-15 × 1,250 kVA IT UPS modules (N+1 architecture)
- Parameters: Input/output kW, battery voltage, runtime remaining, bypass status, module health
- Path redundancy: MV dual-ring provides path redundancy; N+1 UPS provides component redundancy

**Mechanical UPS Monitoring:**
- 20 × 250 kW mechanical UPS modules (N+1)
- Status, load, battery runtime

**Revenue Metering:**
- Utility import/export at 161kV (utility-owned)
- Solar production (13.8kV inverter output)
- BESS charge/discharge (if BESS deployed)

### EPMS Platform

**Recommended Vendors:**
- Schneider Electric PowerLogic / EcoStruxure Power Monitoring Expert
- Siemens SICAM / PowerManager
- GE Grid Solutions (if IEEE 2030.7/2030.8 microgrid controller required)

**Architecture:**
- **SCADA server:** 2 × redundant servers (A/B)
- **Power meters:** IEC 61850-compliant meters at all major points
  - 161kV substation: Utility-grade meters
  - 13.8kV ring bus: SEL or ABB relays with metering
  - 480V switchboards: Schneider PM8000 or equivalent
- **Network:** Fiber (redundant ring topology)
- **Protocols:** Modbus TCP, IEC 61850, DNP3

### Monitoring Functions

**Real-Time Power Flow:**
- Single-line diagram (SLD) showing power flow from 161kV → 13.8kV → 480V → IT load
- kW values at every major point (updated every 1-2 seconds)

**Load Trending:**
- Historical power consumption (hourly, daily, monthly)
- Peak demand tracking
- PUE calculation (facility power / IT power)

**Fault Detection:**
- Overcurrent, undervoltage, overvoltage, frequency deviation
- Arc flash detection (optional)
- Ground fault detection

**Generator Performance:**
- Fuel consumption tracking (gal/hr, gal/kWh)
- Runtime hours (maintenance scheduling)
- Load sharing accuracy (verify equal load distribution)


---

## DATA CENTER INFRASTRUCTURE MANAGEMENT (DCIM)

### System Scope

**Rack-Level Power Monitoring:**
- 30 cabinets × 2 PDUs = 60 intelligent PDUs
- Parameters: kW, kVA, voltage, current, power factor (per outlet or total)
- Remote switching capability (if smart PDUs)

**Rack-Level Cooling Monitoring:**
- Cabinet FCU status (fan speed, valve position, airflow)
- CDU status (Phase 2: flow rate, supply/return temp, pump speed)
- Temperature sensors: Rack inlet (cold aisle), outlet (hot aisle), rear door

**Environmental Sensors:**
- Temperature: 4-6 sensors per cabinet (top, middle, bottom × inlet/outlet)
- Humidity: 2 sensors per cabinet row
- Airflow: Differential pressure across containment

**Asset Management:**
- Rack inventory (server count, U-space utilization)
- Customer assignment (which racks belong to which customer)
- Equipment serial numbers, warranties, maintenance schedules

### DCIM Platform

**Recommended Vendors:**
- Schneider Electric EcoStruxure IT / StruxureWare
- Nlyte DCIM
- Sunbird DCIM

**Features:**
- **Real-time dashboards:** Power, cooling, environmental status
- **Capacity planning:** "What-if" modeling for new equipment deployments
- **Thermal mapping:** 3D visualization of data hall temperature distribution
- **PUE calculation:** Real-time and historical PUE trending
- **Customer portal:** Web interface for customers to view their rack metrics
- **Change management:** Workflow for tracking equipment moves/adds/changes

### Key Metrics

**Power Usage Effectiveness (PUE):**
- PUE = Total Facility Power / IT Power
- Target: Phase 1 = 1.35, Phase 2 = 1.25
- Calculated every 5 minutes, trended over time

**Capacity Utilization:**
- IT power: Actual kW / Available kW (%)
- Cooling: Actual kW cooling load / Available kW cooling capacity (%)
- Floor space: Occupied cabinets / Total cabinet positions (%)

**Thermal Performance:**
- Rack inlet temp distribution (ensure <27°C per ASHRAE A1)
- Hot spots identification (racks exceeding setpoint)

---

## NETWORK OPERATIONS CENTER (NOC)

### Purpose

24/7 monitoring and control hub for facility operations. NOC operators monitor BMS, EPMS, DCIM, fire, security systems and dispatch technicians for alarms.

### NOC Configuration

**Location:** Level 2, central spine (secure access)

**Equipment:**
- 2-3 × operator workstations (dual monitors each)
- Video wall: 3×3 or 4×2 LED display (55-65" panels)
- Displays: BMS dashboards, EPMS single-line, DCIM capacity, CCTV feeds
- Workstation PCs: Access to all monitoring systems
- Printers: Log printing, alarm reports

**Staffing Options:**
1. **24/7 on-site:** 3 shifts × 2 operators = 6 FTEs
2. **Remote monitoring:** Off-site NOC, local on-call technician
3. **Hybrid:** On-site during business hours, remote nights/weekends

### NOC Responsibilities

**Monitoring:**
- Watch for alarms from all integrated systems
- Acknowledge alarms, log details
- Monitor trends (power, cooling, environmental)

**Response:**
- Dispatch on-call technicians for critical alarms
- Coordinate with utility, fire department, security as needed
- Execute emergency procedures (facility shutdown, evacuation)

**Coordination:**
- Customer access requests (escort, remote hands)
- Vendor access (maintenance, deliveries)
- Shift handoff logs

---

## INTEGRATION PROTOCOLS & CYBERSECURITY

### Communication Protocols

**BACnet/IP:**
- BMS devices (chillers, pumps, FCUs, sensors)
- Native BACnet controllers preferred (no gateways)

**Modbus TCP:**
- Legacy equipment integration (older UPS, generators)
- Power meters (if not IEC 61850)

**IEC 61850:**
- Medium voltage switchgear, relays, RMUs
- Microgrid controller communication

**SNMP:**
- Network equipment (switches, routers)
- UPS monitoring (if BACnet not available)

**OPC UA:**
- Industrial automation, SCADA
- Microgrid controller integration with EPMS/BMS

### Network Architecture

**Segmentation:**
- **IT Network:** Customer servers, internet gateway (isolated)
- **Facility Network:** BMS, EPMS, DCIM, fire, security
- **Management Network:** NOC workstations, admin access
- **Firewall:** Between IT and Facility networks (strict rules)

**Redundancy:**
- Fiber ring topology (dual path)
- Redundant core switches (A/B)
- UPS-backed network equipment

### Cybersecurity

**Access Control:**
- Role-based access control (RBAC) for all systems
- Multi-factor authentication (MFA) for remote access
- Password policies (complexity, rotation)

**Encryption:**
- TLS/SSL for all web interfaces
- VPN for remote access

**Monitoring:**
- Intrusion detection system (IDS) on facility network
- Log aggregation and SIEM (if required by customer)

**Patching:**
- Regular security updates for BMS/EPMS/DCIM servers
- Tested in non-production environment before deployment


---

## COST SUMMARY

| System                                        | Cost Estimate |
| --------------------------------------------- | ------------- |
| **BMS (HVAC, Lighting, Environmental)**       | $600-900K     |
| **EPMS (Power Monitoring, SCADA)**            | $400-600K     |
| **DCIM (Rack-Level Monitoring)**              | $300-500K     |
| **NOC Fit-Out (Workstations, Video Wall)**    | $200-400K     |
| **Integration & Engineering**                 | $300-500K     |
| **Total Integrated Automation**               | **$3.0-4.8M** |

---

**Tags:** #pryor-dc #bms #epms #microgrid-controller #dcim #noc #ieee-2030

**Next Steps:**
1. Select BMS/EPMS/DCIM platforms (coordinate with equipment vendors)
2. Design facility network architecture (fiber routing, switch locations)
3. Cybersecurity assessment and hardening plan
4. Commissioning plan with IST scenarios

---

**Document Control:**
- **Source:** Pryor_Bod_EVS_Rev01.md and Erik_BOD reference
- **Date Updated:** October 29, 2025
- **Prepared by:** EVS / PGCIS Team
- **Key Updates:** Microgrid controller integration, 161kV/13.8kV coordination, IEEE 2030.7 compliance
