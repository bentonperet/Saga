**Created:** 2025-10-23 10:20

# BASIS OF DESIGN - FIRE SUPPRESSION
## CSI Division 21
### Saga Energy – Pryor Data Center

**Parent Document:** [[_BOD - Exec Summary and TOC]]

---

## OVERVIEW

Fire protection designed to meet NFPA, IBC, and insurance requirements while protecting personnel, equipment, and minimizing business interruption.

**Design Philosophy:**
- Early detection in all critical areas
- Automatic suppression in data hall and electrical rooms
- Clear egress paths and emergency notification
- Equipment protection via clean agent systems (avoid water damage to IT equipment)

**Code Compliance:**
- NFPA 72 - National Fire Alarm and Signaling Code
- NFPA 75 - Fire Protection of Information Technology Equipment
- NFPA 2001 - Clean Agent Fire Extinguishing Systems
- NFPA 101 - Life Safety Code
- International Building Code (IBC)


---

## DATA HALL SUPPRESSION

### Hydraulic Calculation Basis

**Design Approach:**
- **Applicable Standard:** NFPA 13 - Standard for Installation of Sprinkler Systems
- **Occupancy Classification:** Ordinary Hazard Group 2 (OH-2) per NFPA 13
- **Design Density:** 0.20 gpm/SF over 1,500 SF design area (per NFPA 13 Table 11.2.3.1.2)
- **Hose Stream Allowance:** 250 GPM for 30 minutes (inside hose + exterior attack)
- **Water Supply Duration:** 60 minutes minimum
- **Hydraulic Calculation Method:** Computer-based calculation per NFPA 13 Section 23.4
- **Most Remote Area:** Calculated at furthest point from water supply (highest elevation, longest pipe run)

**Estimated Water Demand:**
- **Sprinkler Flow:** 0.20 gpm/SF × 1,500 SF = 300 GPM
- **Hose Stream:** 250 GPM
- **Total Demand:** 550 GPM @ 60-80 psi (TBD via detailed hydraulic calculation)
- **Duration:** 60 minutes = 33,000 gallons minimum storage requirement

### Pre-Action System (Recommended - Lower Cost)

**System Type:** Dual-interlock pre-action dry pipe system per NFPA 13

**Activation Sequence:**
1. **Stage 1 - Detection Alarm:** VESDA smoke detection activates → Pre-alarm in NOC, investigate
2. **Stage 2 - Pre-Action Valve Open:** VESDA alarm + sprinkler heat activation → Pre-action valve opens, pipe fills with water
3. **Stage 3 - Water Discharge:** Fused sprinkler head opens → Water discharges to fire

**Key Components:**
- **Pre-Action Valve:** Electric/pneumatic deluge valve with supervisory air pressure monitoring
- **Air Compressor:** Maintain 20-40 psi air pressure in dry pipe (monitor for leaks)
- **Sprinkler Heads:** Quick-response (QR) pendent heads, 155-165°F temperature rating
- **Pipe Material:** Schedule 40 black steel (dry pipe), CPVC or steel (wet pipe sections if any)
- **Control Panel:** Fire alarm integrated pre-action control panel

**Benefits:**
- Lower cost than clean agent ($300-500K vs $800K-1.3M for data hall)
- Dual-interlock prevents accidental water release (requires both detection + heat)
- Acceptable to most insurance carriers (FM Global approved)

### Clean Agent System (Alternative - Customer Preference)

**System Type:** Total flooding clean agent fire suppression per NFPA 2001

**Agent Options:**
- **FM-200 (HFC-227ea):** 7-8% design concentration, 10-second discharge
- **Novec 1230 (FK-5-1-12):** 4-6% design concentration, 10-second discharge, lower GWP

**Key Components:**
- **Agent Storage:** High-pressure cylinders (200-600 psi) in mechanical room or dedicated suppression room
- **Discharge Nozzles:** Ceiling-mounted nozzles, calculated spacing per NFPA 2001
- **Control Panel:** Dedicated clean agent control panel with manual abort
- **Activation:** Automatic via cross-zone smoke detection, 30-second pre-discharge alarm

**Cost Impact:** +$500K-800K vs pre-action sprinkler system

**Decision Criteria:** Customer preference and insurance requirements will dictate final selection. Pre-action is baseline; clean agent if customer requires water-free suppression.

---

## ELECTRICAL ENCLOSURES SUPPRESSION

### Outdoor Containerized Electrical Enclosures
- **System Type:** Integrated clean agent or pre-action suppression per enclosure (vendor-provided)
- **Quantity:** 12-16 outdoor electrical enclosures (phased deployment with UPS/switchgear)
- **Enclosure Size:** ~12 ft × 55 ft per enclosure {TBC}
- **Suppression Strategy:** Factory-integrated suppression system (clean agent preferred for electrical equipment protection)
- **Agent (if clean agent):** FM-200 or Novec 1230, designed per NFPA 2001
- **Activation:** Automatic via smoke/heat detection in enclosure, 30-second pre-discharge alarm, manual abort switch
- **Integration:** Suppression alarm signal transmitted to building FACP and BMS
- **Rationale:** Protects high-value UPS and electrical equipment; factory integration reduces field installation complexity


---

## MECHANICAL ROOMS {TBC}

- **System Type:** Wet pipe sprinkler system
- **Coverage:** Sprinkler heads per NFPA 13 spacing requirements
- **Equipment Protection:** Avoid sprinkler heads directly above sensitive controls (use sidewall heads where needed)

---

## OFFICE/NOC/SUPPORT SPACES

- **System Type:** Wet pipe sprinkler system
- **Coverage:** Standard commercial spacing per NFPA 13

---

## FIRE DETECTION & ALARM

### Detection System Specifications

**Data Hall - VESDA (Very Early Smoke Detection):**
- **Technology:** Aspirating smoke detection (ASD) per NFPA 72 Chapter 17
- **Sampling:** Air sampling pipe network with sampling holes at ceiling level (12-15 ft elevation)
- **Pipe Layout:** Grid pattern with sampling holes every 20-30 ft (manufacturer-specified spacing)
- **Sensitivity Levels:**
  - Alert: 0.005% obscuration/ft (pre-alarm, investigate)
  - Action 1: 0.015% obscuration/ft (alarm, notify NOC)
  - Action 2: 0.02% obscuration/ft (activate pre-action valve if heat detected)
  - Fire 1: 0.05% obscuration/ft (general alarm, evacuation)
- **Response Time:** <60 seconds from smoke entry to alarm
- **Integration:** Connected to FACP, initiates pre-action suppression sequence

**Electrical Enclosures:**
- **Detection:** Spot-type photoelectric smoke detectors + fixed-temperature heat detectors (135-155°F)
- **Spacing:** Per NFPA 72 (30 ft spacing for smooth ceiling)
- **Integration:** Linked to enclosure suppression system (if clean agent) and building FACP

**Mechanical Rooms & Support Spaces:**
- **Detection:** Spot-type photoelectric smoke detectors per NFPA 72
- **Spacing:** 30 ft on-center for smooth ceilings, 15 ft for irregular ceilings

### Fire Alarm Control Panel (FACP) Specifications

- **Type:** Addressable, networked fire alarm control panel per NFPA 72
- **Capacity:** 250-500 addressable points (Phase 1), expandable to 1,000+ (Ultimate)
- **Power Supply:** 120/240V primary with battery backup (24 hours standby, 5 minutes alarm)
- **Communication:** Ethernet/IP network for NOC integration, BACnet/IP to BMS
- **Remote Monitoring:** Cellular or IP dialer to off-site central station (UL listed monitoring service)
- **Notification Appliances:** Visual strobes + audible horns per NFPA 72 (15 candela @ 10 ft, 75-110 dBA)
- **Zoning:** Separate alarm zones for data hall, each electrical enclosure, mechanical rooms, support spaces
- **Annunciation:** Graphic annunciator panel in NOC showing active alarms by zone

### Suppression Activation Sequence (Pre-Action System)

1. **Pre-Alarm (VESDA Alert):** Investigate, no suppression action
2. **Alarm (VESDA Action 1 + Heat Detector):** Pre-action valve opens, pipe fills with water
3. **Discharge (Fused Sprinkler Head):** Sprinkler head fuses @ 155-165°F → water discharge
4. **Post-Discharge:** Flow switch confirms water flow → waterflow alarm to FACP and fire department

---

## EGRESS & LIFE SAFETY

### Occupancy Classification
- **Data Hall:** Group B (Business) per IBC Section 304
- **Office/NOC:** Group B (Business)
- **Occupant Load:** ~20-30 persons (varies by operational model)

### Egress Requirements
- **Exit Count:** Minimum 2 exits from data hall per IBC Section 1006
- **Exit Width:** 36" minimum per door, 44" preferred for equipment moves
- **Travel Distance:** ≤200 ft to nearest exit (unsprinklered), ≤300 ft (sprinklered) per IBC Table 1017.2
- **Exit Signs:** Illuminated exit signs at all egress doors
- **Emergency Lighting:** Battery-backed LED fixtures per NFPA 101
  - Illumination: 1 foot-candle average, 0.1 fc minimum
  - Duration: 90 minutes minimum battery backup

### Hot Aisle Containment Integration
- **Door Release:** Containment doors auto-release on fire alarm (magnetic hold-open with fail-safe release)
- **Egress Paths:** Containment structures must not block egress

---

## FIRE PUMP & WATER SUPPLY

### Water Supply Design

**Demand Calculation:**
- **Design Basis:** Per NFPA 13 hydraulic calculation for data hall (most demanding area)
- **Estimated Demand:** 550 GPM @ 60-80 psi (300 GPM sprinklers + 250 GPM hose stream)
- **Duration:** 60 minutes = 33,000 gallons minimum
- **Final Demand:** TBD via detailed hydraulic calculation (may be higher based on actual building layout)

### Fire Pump & Storage Tank

**Fire Pump (Required if Municipal Pressure <80 psi):**
- **Type:** Electric motor-driven vertical turbine or horizontal split-case fire pump
- **Capacity:** Sized to meet calculated demand (estimated 550 GPM @ 80 psi)
- **Driver:** Electric motor preferred (480V, 3-phase), diesel backup optional
- **Redundancy:** Single fire pump is code-compliant (NFPA 20 does not require N+1 redundancy for fire pumps)
- **Controller:** UL-listed fire pump controller with automatic start on pressure drop
- **Location:** Dedicated fire pump room or outdoor pump house

**On-Site Fire Water Storage Tank:**
- **Requirement:** Required if municipal water supply is unavailable or insufficient flow/pressure
- **Size:** 50,000-75,000 gallons (33,000 gal demand + safety factor)
- **Type:** Welded steel or concrete tank, above-ground or underground
- **Refill:** Automatic refill from municipal water (if available) or periodic water truck delivery
- **Freeze Protection:** Buried below frost line or heated (if above-ground in cold climate)
- **Site-Specific Decision:** Coordinate with municipal water utility to confirm available flow and pressure. If municipal supply meets NFPA 13 demand (550 GPM @ 60-80 psi), on-site storage tank may not be required.

**Backflow Prevention:**
- **Type:** Double-check backflow preventer on fire service connection (per IPC and local code)
- **Size:** 4-6" based on fire service demand

### Municipal Water Coordination
- **Action Required:** Coordinate with Water & Wastewater Availability Study (see [[11BOD - Utilities DC Critical (CSI Div 33)]])
- **Fire Flow Test:** Request fire flow test from municipal utility to confirm available GPM and residual pressure
- **Decision Tree:**
  - **Municipal supply adequate:** Direct connection to municipal water (no storage tank required)
  - **Municipal supply inadequate:** On-site storage tank + fire pump required
  - **No municipal supply:** On-site storage tank + fire pump + periodic water truck refill

---

## KEY DESIGN CONSIDERATIONS

### Integration with Security
- Fire alarm system must not impede life safety egress
- All security doors unlock on fire alarm activation
- Dual alarms (fire + intrusion) prioritize fire alarm

### Insurance Requirements
- FM Global approval likely required for data center insurance
- Pre-action sprinkler or clean agent systems typically required by insurers
- UPS room fire protection must meet insurer standards (clean agent per NFPA 2001)

---

## COST IMPACTS & FINANCIAL ANALYSIS

**Cost Analysis Prompt for Future Detailed Work:**

```
FIRE SUPPRESSION SYSTEMS COST ESTIMATION PROMPT

Using the specifications throughout this BOD, perform a comprehensive cost analysis
for the fire suppression and life safety systems including:

1. SYSTEM COST BREAKDOWN
   - Data hall pre-action sprinkler system (piping, heads, pre-action valve, air compressor)
   - Data hall clean agent system (if selected): agent, cylinders, nozzles, control panel
   - Electrical enclosure suppression (12-16 units, factory-integrated or field-installed)
   - VESDA/ASD system for data hall (sampling pipes, detector units, control modules)
   - Fire alarm control panel (FACP) and addressable devices
   - Notification appliances (strobes, horns)
   - Fire pump (if required based on municipal water pressure test)
   - Fire water storage tank (if required based on municipal water availability)
   - Installation labor, commissioning, and witness testing

2. VENDOR CONFIDENCE LEVELS & JUSTIFICATION
   Assign confidence level (High/Medium/Low) with percentage and justification:
   - High (80-95%): Recent vendor quote, comparable project within 12 months
   - Medium (60-80%): Industry pricing guide with regional adjustment, general vendor feedback
   - Low (40-60%): Preliminary estimate, pending detailed design or site-specific factors

3. SITE-SPECIFIC COST DRIVERS
   - Municipal water availability (impacts fire pump and storage tank requirements)
   - Insurance carrier requirements (may mandate clean agent vs pre-action)
   - FM Global or other insurer-specific requirements
   - Local fire marshal jurisdiction requirements

4. ALTERNATIVE DESIGN COST COMPARISON
   - Pre-action sprinkler (baseline) vs clean agent (data hall)
   - Municipal water connection vs on-site storage tank + fire pump
   - Factory-integrated electrical enclosure suppression vs field-installed

5. CODE COMPLIANCE & PERMITTING COSTS
   - NFPA hydraulic calculation engineering
   - Fire marshal plan review and approval fees
   - Inspection and testing costs (hydrostatic, flow test, VESDA calibration)

OUTPUT FORMAT:
- Detailed cost breakdown table by system with confidence % for each line item
- Justification for confidence level (quote source, comparable project, estimate basis)
- Highlight site-specific costs pending utility coordination
- Executive summary of total fire suppression CAPEX with overall confidence level
```

**Placeholder Cost Summary (Detailed Analysis Required):**

| System | Estimated Cost Range | Confidence | Notes |
|---|---|---|---|
| Data hall pre-action sprinkler (20,000 SF) | $300-500K | 65% (Medium) | Based on $15-25/SF for pre-action system, requires hydraulic calc |
| Data hall clean agent (alternative) | +$500-800K | 60% (Medium) | Clean agent adds $25-40/SF vs pre-action, customer preference |
| Electrical enclosure suppression (12-16 units) | $200-400K | 55% (Low) | Factory-integrated cost TBD, assume $15-25K per enclosure |
| VESDA/ASD detection system (data hall) | $75-125K | 70% (Medium) | Based on $4-6/SF for aspirating detection coverage |
| Fire alarm control panel & devices | $150-250K | 70% (Medium) | Addressable FACP + devices + notification appliances |
| Fire pump (if required) | $100-200K | 65% (Medium) | 550 GPM @ 80 psi electric fire pump, controller, piping |
| Fire water storage tank (if required) | $200-400K | 60% (Medium) | 50,000-75,000 gal tank, foundation, piping; site-specific |
| **Total Fire Suppression (Pre-Action)** | **$1.03-1.88M** | **65% (Medium)** | Baseline with pre-action; excludes storage tank if municipal water adequate |
| **Total Fire Suppression (Clean Agent)** | **$1.53-2.68M** | **60% (Medium)** | With clean agent upgrade for data hall |

**Key Assumptions Requiring Validation:**
- Municipal water supply provides adequate flow/pressure (eliminates storage tank requirement)
- Pre-action sprinkler acceptable to insurance carrier (lower cost than clean agent)
- Electrical enclosure suppression is factory-integrated (reduces field installation cost)

**Note:** Detailed cost validation to be completed per prompt above. Cost estimates are preliminary and subject to change based on detailed hydraulic calculations, insurance requirements, and municipal water availability study.

---

**Tags:** #saga-project #fire-suppression #nfpa-855 #life-safety #csi-division-21

**Related Documents:**
- [[_BOD - Exec Summary and TOC]] - Main title page and facility overview
- [[7BOD - Electrical (CSI Div 26)]] - Electrical enclosure details, outdoor containerized equipment
- [[4BOD - Plumbing (CSI Div 22)]] - Domestic water service, fire water supply coordination
- [[6BOD - Integrated Automation (CSI Div 25)]] - FACP integration with BMS, alarm monitoring
- [[9BOD - Electronic Safety and Security (CSI Div 28)]] - Security door releases on fire alarm
- [[2BOD - Facility Construction (CSI Divs 02-14)]] - Egress requirements, door hardware
- [[11BOD - Utilities DC Critical (CSI Div 33)]] - Municipal water availability for fire suppression
- [[Architectural Meeting Changes by CSI Division]] - October 2025 updates
