**Created:** 2025-10-23 10:50

# BASIS OF DESIGN - ELECTRONIC SAFETY AND SECURITY
## CSI Division 28
### Saga Energy – Pryor Data Center

**Parent Document:** [[Saga Pryor DC/Basis of Design/Archive/Erik_BOD_Copy/_BOD - Exec Summary and TOC]]
**Related:** [[Basis of Design - Part 2 Supporting Systems]]

---

## OVERVIEW

Multi-layered security system protects critical infrastructure, customer equipment, and personnel. Integrated with BMS/DCIM for centralized monitoring and alarm response.


---

## SECURITY OBJECTIVES

1. **Perimeter Security:** Prevent unauthorized site access
2. **Building Access Control:** Restrict entry to authorized personnel only
3. **Customer Data Protection:** Isolate customer cages/suites in multi-tenant deployments
4. **Surveillance:** 24/7 video monitoring and recording
5. **Intrusion Detection:** Real-time alerting for security breaches

---

## SECURITY LAYERS

- **Layer 1:** Site perimeter (fence, gates, barriers)
- **Layer 2:** Building perimeter (doors, windows, vehicle barriers)
- **Layer 3:** Internal access control (data hall, electrical enclosures, NOC)
- **Layer 4:** Customer cage/suite access (individual customer spaces)
<!-- talk about construction-specific layers. Sometimes there will be construction workers in the envelope, think about how to represent this -->

---

## PERIMETER SECURITY

### Perimeter Fencing
- **Fence Type:** 8 ft chain-link with barbed wire or ornamental steel (per local zoning requirements)
- **Gates:**
  - Automated sliding gate for vehicle access
  - Pedestrian gate with card reader or keypad
- **Access Control:** Card reader or keypad at vehicle gate; intercom with NOC for visitor management
- **Clearance:** 10-20 ft clear zone inside fence (no obstructions for surveillance coverage)

### Vehicle Barriers
- **Crash-Rated Bollards:** K4 or K12 rated bollards at building entry points
- **Location:** Around critical equipment (generators, BESS enclosure, utility transformer)
- **Standards:** ASTM F2656 / DOS SD-STD-02.01 crash rating
- **Purpose:** Protects against vehicle ramming attacks

### Perimeter Detection
- **Fence-Mounted Sensors:** Vibration or fiber optic intrusion detection on perimeter fence
- **Cameras:** Coverage of all fence sections, gates, and building perimeter

---

## BUILDING ACCESS CONTROL

### Access Control System
- **Technology:** Proximity card or biometric (fingerprint/facial recognition) readers
- **Integration:** Networked access control system integrated with BMS/DCIM and video surveillance
- **Credential Management:** Centralized database for adding/removing user credentials
- **Audit Trail:** All access events logged with timestamp, user ID, and door location

### Access Levels
- **Level 1 (Facility Staff):** Full access to all areas except customer cages
- **Level 2 (Customer):** Access to assigned customer cage/suite only
- **Level 3 (Vendor/Contractor):** Escorted access, temporary credentials
- **Level 4 (Visitor):** Reception area only, must be escorted

### Critical Access Points

**Building Entry:**
- **Man-Trap:** Double-door airlock with card reader + PIN or biometric (two-factor authentication)
- **Operation:** Outer door must close and latch before inner door can open (prevents tailgating)
- **Fire Override:** Both doors unlock on fire alarm (life safety compliance)

**Data Hall Entry:**
- **Card Reader + PIN or Biometric:** Two-factor authentication required

**Electrical Enclosures:**
- **Card Reader:** Restricted to facility staff and authorized vendors

**Mechanical Rooms:**
- **Card Reader:** Restricted to facility staff and authorized vendors

**NOC:**
- **Card Reader:** Restricted to operations staff

**Meet-Me Rooms (MMRs):**
- **Highest Security Level:** Card reader + biometric recommended
- **Rationale:** Critical telecommunications infrastructure

---

## VIDEO SURVEILLANCE (CCTV)

### Camera Coverage
- **Perimeter:** All fence lines, gates, and building exterior (360° coverage)
- **Building Entry Points:** All doors (exterior and data hall entry)
- **Data Hall:** Wide-angle cameras covering aisles (not directed into customer cages for privacy)
- **Equipment Yards:** Generator yard, chiller yard, BESS enclosure, transformer pad
- **Interior Critical Areas:** NOC, electrical enclosures (entry points), mechanical rooms (entry points)

### Camera Specifications
- **Resolution:** 4MP or higher (1080p minimum)
- **Type:** IP cameras with PoE (Power over Ethernet)
- **Features:** Night vision (IR LEDs), motion detection, tamper detection
- **Frame Rate:** 15-30 fps (higher for critical areas like man-trap)

### Video Management System (VMS)
- **Recording:** Network Video Recorder (NVR) with redundant storage
- **Retention:** 90 days minimum (180 days preferred for forensic analysis)
- **Storage Capacity:** ~50-100 TB (varies by camera count and retention period)
- **Remote Access:** NOC operators can view live/recorded video via secure network
- **Integration:** VMS integrated with access control (view video on access event triggers)

### Analytics
- Motion detection zones (reduce false alarms)
- Object left behind detection (unattended bag/package)
- Perimeter crossing detection (virtual tripwire)
- Facial recognition (optional, for high-security deployments)

---

## INTRUSION DETECTION SYSTEM (IDS)

### Detection Devices
- **Door Contacts:** Magnetic door contacts on all exterior doors and critical interior doors
- **Motion Sensors:** Passive infrared (PIR) motion detectors in unoccupied areas during off-hours
- **Glass Break Detectors:** Acoustic sensors on windows (if windows present)
- **Duress Buttons:** Panic buttons at reception desk and NOC for emergency situations

### Alarm Response
- **Local Alarm:** Audible alarm (can be silenced to avoid alerting intruder)
- **NOC Alert:** Immediate notification to NOC operators
- **Central Station Monitoring:** Alarm forwarded to off-site security monitoring center
- **Law Enforcement:** NOC or central station contacts local police for confirmed intrusions

### Integration with Fire Alarm
- Security system must not impede life safety egress (doors unlock on fire alarm)
- Dual alarms (fire + intrusion) require prioritization (fire alarm takes precedence)

---

## CUSTOMER CAGE SECURITY

### Physical Separation
- **Cages:** Floor-to-ceiling steel mesh partitions (8' or 10' height)
- **Doors:** Lockable cage doors with electronic access control
- **Roof:** Cage roof or ceiling-mounted mesh to prevent climbing over

### Access Control
- **Customer-Controlled Access:** Customers manage their own user credentials for cage access
- **Biometric Option:** Customer can deploy additional biometric readers at cage door
- **Audit Trail:** All cage access events logged and available to customer via DCIM portal

### Surveillance
- Cameras provide general data hall coverage but do not directly view inside customer cages (privacy)
- Customer may deploy their own cameras inside cage

---

## INTEGRATION WITH BMS/DCIM

### Centralized Monitoring
- All security systems (access control, CCTV, intrusion detection) integrated with BMS/DCIM
- Single-pane-of-glass view for NOC operators
- Alarms displayed on NOC video wall and operator workstations

### Automated Responses
- **Access Event + Video:** VMS automatically displays camera feed when access event occurs (e.g., door opened)
- **Alarm Escalation:** If intrusion alarm not acknowledged within 15 minutes, escalate to backup on-call
- **Fire Alarm Override:** All security doors unlock on fire alarm activation (life safety priority)

---

## COST IMPACTS

| System | Cost Estimate |
|---|---|
| Perimeter fencing (8 ft chain-link, gates) | ~$200-400K |
| Vehicle barriers (crash-rated bollards) | ~$100-200K |
| Access control system (card readers, controllers) | ~$150-300K |
| Video surveillance (cameras, NVR, storage) | ~$200-400K |
| Intrusion detection system (sensors, control panel) | ~$75-150K |
| Customer cage infrastructure (mesh partitions, doors) | ~$100-200K |
| Integration with BMS/DCIM | ~$50-100K |
| **Total Security Systems** | ~$875K-1.75M |

---

**Tags:** #saga-project #security #access-control #cctv #intrusion-detection #csi-division-28

**Related Documents:**
- [[Saga Pryor DC/Basis of Design/Archive/Erik_BOD_Copy/_BOD - Exec Summary and TOC]] - Main title page
- [[Saga Pryor DC/Basis of Design/Archive/Erik_BOD_Copy/8BOD - Communications (CSI Div 27)]] - Network infrastructure for IP cameras
- [[Saga Pryor DC/Basis of Design/Archive/Erik_BOD_Copy/6BOD - Integrated Automation (CSI Div 25)]] - BMS/DCIM integration
- [[Saga Pryor DC/Basis of Design/Archive/Erik_BOD_Copy/3BOD - Fire Suppression (CSI Div 21)]] - Fire alarm integration with security
