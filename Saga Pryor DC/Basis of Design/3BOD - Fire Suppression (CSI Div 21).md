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

### System Options

**Pre-Action Dry Pipe (RECOMMENDED)**
- **Type:** Dual-interlock pre-action system
- **Activation:** Requires smoke detection + heat activation before water release
- **Benefit:** Eliminates risk of accidental water damage (dry pipe until both conditions met)
- **Sprinkler Type:** ESFR (Early Suppression Fast Response) or standard heads
- **Water Supply:** Fire pump + storage tank or municipal service (TBD)

**Clean Agent Gas (Alternative)**
- **Agent:** FM-200 (HFC-227ea) or Novec 1230 (FK-5-1-12)
- **Concentration:** Per NFPA 2001 for Class A/C fires
- **Discharge Time:** ≤10 seconds
- **Cost Impact:** +$500K-800K vs pre-action system
- **Use Case:** If customer prefers gas suppression (some hyperscale operators require this)

**Decision:** Align with customer preferences and insurance requirements. Pre-action is lower cost; clean agent preferred by some operators.

---

## ELECTRICAL ENCLOSURES

### Outdoor Containerized Electrical Enclosures
- **System Type:** Integrated fire suppression within containers (clean agent or pre-action)
- **Quantity:** 2-3 outdoor electrical enclosures (A-side, B-side, +1 optional for dual path UPS)
- **Size:** ~12 ft × 55 ft per enclosure {TBC}
- **Rationale:** Protects high-value UPS and electrical equipment without water damage risk
- **Coverage:** Integrated suppression system per enclosure, designed per NFPA 2001
- **Integration:** Automatic activation on smoke detection; manual abort capability

**Alignment with Oct 2025 Meeting:**
- October architectural meeting recommended outdoor containerized electrical enclosures
- Fire suppression integrated into containerized enclosure design
- Cost: ~$100-200K per enclosure {TBC} vs ~$200-400K for indoor room suppression

---

## MECHANICAL ROOMS

- **System Type:** Wet pipe sprinkler system
- **Coverage:** Sprinkler heads per NFPA 13 spacing requirements
- **Equipment Protection:** Avoid sprinkler heads directly above sensitive controls (use sidewall heads where needed)

---

## BESS ENCLOSURE - NOT APPLICABLE

**BESS REJECTED:**
- **BESS-as-UPS:** Violates Tier III concurrent maintainability requirement (see [[Why BESS Should Not Be UPS]])
- **Economic BESS:** Deeply negative NPV of -$5.3M to -$6.2M over 20 years (see [[Excess Solar Monetization Strategy]])

**NFPA 855 Requirements:** No longer applicable to this project

**Cost Savings:** -$150-300K (NFPA 855 fire suppression system not required)

---

## OFFICE/NOC/SUPPORT SPACES

- **System Type:** Wet pipe sprinkler system
- **Coverage:** Standard commercial spacing per NFPA 13

---

## FIRE DETECTION & ALARM

### Detection Technology by Zone

**Data Hall**
- **Type:** VESDA (Very Early Smoke Detection Apparatus) or aspirating smoke detection (ASD)
- **Sampling:** Air sampling holes at ceiling and floor level (no raised floor)
- **Sensitivity:** Alert at 0.005% obscuration/ft, alarm at 0.02% obscuration/ft
- **Response Time:** <60 seconds for early detection

**Electrical Rooms**
- **Type:** Spot-type smoke detectors + heat detectors
- **Integration:** Linked to clean agent suppression system in UPS rooms

**Mechanical Rooms**
- **Type:** Spot-type smoke and heat detectors

**Support Spaces**
- **Type:** Spot-type smoke detectors per NFPA 72

### Fire Alarm Control Panel (FACP)
- **Type:** Addressable, networked fire alarm system
- **Integration:** BMS integration for monitoring and control
- **Notification:** Visual and audible alarms (strobes + horns)
- **Remote Monitoring:** 24/7 NOC monitoring + off-site central station monitoring
- **Zones:** Separate zones for data hall, electrical rooms, mechanical rooms, support spaces

### Pre-Alarm Strategy
- **Alert Level:** Low-level smoke detection triggers alert (investigate, no evacuation)
- **Alarm Level:** Higher smoke or heat detection triggers full alarm (evacuation, suppression activation)
- **Staged Response:** Allows time to investigate false alarms before full evacuation/suppression

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

### Water Supply (If Sprinkler System Selected)

**Demand Calculation:**
- **Design Basis:** Per NFPA 13 for data hall (most demanding area)
- **Estimated Demand:** 1,500-2,500 GPM @ 60-80 psi (TBD via hydraulic calculation)

**Fire Pump:**
- **Type:** Electric or diesel-driven fire pump sized to meet demand
- **Redundancy:** Single pump acceptable (fire pump itself is not N+1 redundant)

**Storage Tank:**
- **Size:** 50,000-100,000 gallon on-site fire water storage tank
- **Use Case:** If municipal supply insufficient or unavailable
- **Refill:** Periodic water truck delivery (if no municipal service)

**Backflow Prevention:**
- **Type:** Double-check backflow preventer on fire service connection

### Municipal Water Dependency
- **Coordinate with Water & Wastewater Availability Study** (see Division 33 Utilities)
- If municipal water unavailable: On-site storage + fire pump required

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

## COST IMPACTS

| System | Cost Estimate |
|---|---|
| Data hall pre-action sprinkler | Baseline (~$300-500K) |
| Data hall clean agent (alternative) | +$500-800K |
| Outdoor electrical enclosure suppression (2-3 units) | ~$200-400K {TBC} |
| Fire alarm system (addressable, networked) | ~$150-250K |
| Fire pump + storage tank (if needed) | +$500K-1M |
| **Total Fire Suppression** | ~$1.15-2.95M {TBC} |

**Cost Savings Without BESS:**
- Avoided NFPA 855 fire suppression: **-$150-300K**

---

**Tags:** #saga-project #fire-suppression #nfpa-855 #life-safety #csi-division-21

**Related Documents:**
- [[_BOD - Exec Summary and TOC]] - Main title page
- [[7BOD - Electrical (CSI Div 26)]] - Electrical enclosure details
- [[12BOD - Process Equipment (CSI Divs 40-48)]] - BESS specifications
