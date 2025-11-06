
# BASIS OF DESIGN - GENERAL REQUIREMENTS
## CSI Division 01
### Pryor Data Center - PACHYDERM GLOBAL

**Parent Document:** [[Saga Pryor DC/Basis of Design/Erik_BOD_Updated/_BOD - Exec Summary and TOC]]


---

## 01 10 00 – SUMMARY


---

## 01 14 00 – WORK RESTRICTIONS


---

## 01 30 00 – ADMINISTRATIVE REQUIREMENTS


---

## 01 33 00 – SUBMITTALS


---

## 01 35 00 – SPECIAL PROCEDURES


---

## 01 40 00 – QUALITY REQUIREMENTS


---

## 01 42 00 – IDENTIFICATION AND NAMING STANDARDS

### Asset Naming Hierarchy

**Campus Code:** `TUL` (Tulsa International Airport - nearest major airport to Pryor, OK)

**Building Numbering:** `TUL-##`
- First building: `TUL-01`
- Future expansion: `TUL-02`, `TUL-03`, etc.

**Floor Designation:** `TUL-##-F#`
- Ground floor: `F1`
- Mezzanine: `F2`
- Upper level: `F3`

**Zone Codes:** `TUL-##-F#-ZZZ`
- Data halls: `DH1`, `DH2`
- Equipment yards: `EYN` (North/Mechanical), `EYS` (South/Electrical)
- Substation: `SUB`
- Network Operations Center: `NOC`
- Meet-Me Rooms: `MMR1`, `MMR2`
- Main Distribution Area: `MDA`

### Equipment Asset Tagging Format

**Full Asset ID:** `XXX-##-F#-ZZZ-EEEEE-###`

**Components:**
- Location: `XXX-##-F#-ZZZ` (Campus-Building-Floor-Zone)
- Equipment Type: `EEEEE` (5-character code)
- Unit Number: `###` (3-digit sequential)

**Key Equipment Type Codes:**
- Generators: `GEN`
- Transformers: `XFMR`
- UPS Modules: `UPS`
- Chillers: `CHLR`
- Pumps: `PUMP`
- CDUs: `CDU`
- Switchboards: `SWBD`
- Racks/Cabinets: `R###`

### Path and Loop Designation

**Electrical Paths (Dual Switchboards on Different MV Ring Segments):**
- Add suffix `-A` or `-B` for switchboard designation (SWBD-A on Ring A, SWBD-B on Ring B)
- Example: `TUL-01-F1-EYS-SWBD-A`, `TUL-01-F1-EYS-SWBD-B`
- Cabinet PDUs: `TUL-01-F1-DH1-PDU-R001-A`, `PDU-R001-B` (fed from different panels/switchboards)

**Mechanical Loops:**
- Add suffix `-L#` for Loop number
- Loop 1+2: Air cooling (shared plant)
- Loop 3: Direct-to-chip cooling
- Example: `TUL-01-F1-EYN-CHLR-L1-001`, `CHLR-L3-001`

### Physical Asset Labels

**Label Content:**
- QR code (machine-readable, links to DCIM asset record)
- Human-readable asset ID
- Equipment description and capacity
- Vendor serial number
- Commissioning date

**Label Material:**
- Outdoor equipment: Anodized aluminum (weather/UV resistant)
- Indoor equipment: Laminated polyester
- Engraving: Laser-engraved (permanent, no fade)

**Label Placement:**
- Primary: Front panel at eye level
- Backup: Rear/side panel (for large equipment)
- Cable entry points: Cable identification labels

### Cable and Conduit Marking

**Cable ID Format:** `[SOURCE]-[DEST]-[TYPE]-###`

Examples:
- Power cable: `SWBD-A-PANEL-DH1-PWR-001`
- MV cable: `RMU-001-XFMR-001-MV-001`
- Fiber: `MMR1-DH1-R001-FIBER-001`

**Labeling Frequency:**
- Every 10 ft along cable route
- At both termination points
- At all junction boxes and pull points

### DCIM/Asset Management Integration

**Required Asset Registry Fields:**
- Asset ID (per naming standard)
- Asset type and capacity
- Location (Campus-Building-Floor-Zone)
- Vendor, model, serial number
- Commissioning date, warranty expiration
- Path/Loop assignment
- BMS/EPMS point address
- Maintenance schedule links

**Database Population:** 
- All assets registered in DCIM before commissioning
- QR codes link directly to DCIM asset record
- Changes tracked with revision history

### Documentation Requirements

**Contractor Deliverables:**
- Asset tag schedule (Excel/CSV with all equipment IDs)
- As-built cable schedule (source-destination-ID for all cables)
- Physical labels installed and photographed
- DCIM database populated and verified

**Detailed Naming Standard:**
See [[Appendix - Asset Naming and Tagging Standard]] for complete rubric, equipment type codes, and examples.

---

## 01 43 00 – CODE COMPLIANCE


---

## 01 50 00 – TEMPORARY FACILITIES


---

## 01 60 00 – PRODUCT REQUIREMENTS


---

## 01 70 00 – EXECUTION AND CLOSEOUT


---

## 01 78 00 – CLOSEOUT SUBMITTALS


---

## 01 79 00 – DEMONSTRATION AND TRAINING


---

## 01 90 00 – COMMISSIONING

- Commissioning Agent (CxA): Independent 3rd party.
- Levels 1–5: Factory tests, delivery inspection, start-up, functional testing, IST.
- IST scenarios: Utility loss, chiller failure, UPS module failure, RMU switching, fire alarm.
- Performance targets: PUE TBD

---

## 01 91 00 – MONITORING & REPORTING


---

**Tags:** n/a

**Next Steps:**
1. Complete required sections

---

**Document Control:**
- **Source:** PGCIS Team
- **Date Updated:** November 5, 2025
- **Key Updates:** n/a