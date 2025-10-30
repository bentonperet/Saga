**Created:** 2025-10-30
**Referenced from:** [[1BOD - General Requirements (CSI Div 01)]]

# APPENDIX A - ASSET NAMING AND TAGGING STANDARD
## SAGA DATA CENTERS GLOBAL NAMING CONVENTION

**Purpose:** Establish consistent, scalable naming standard for all SAGA data center facilities worldwide

**Scope:** Applies to all campuses, buildings, zones, equipment, cables, and customer spaces

---

## GEOGRAPHIC HIERARCHY

### Level 1: Campus Code (Airport IATA Code)
**Format:** `XXX` (3-letter airport code)

**Pryor, Oklahoma:**
- Nearest major airport: **Tulsa International (TUL)**
- Campus Code: **`TUL`**

**Examples of Future Campuses:**
- Dallas: `DFW` or `DAL`
- Phoenix: `PHX`
- Amsterdam: `AMS`
- Frankfurt: `FRA`
- Singapore: `SIN`
- London: `LHR`
- Tokyo: `NRT`

**Rationale:** IATA codes are globally recognized, unique, and immediately identify geographic location

---

### Level 2: Data Center Building Number
**Format:** `XXX-##` (Campus + Building Number)

**Pryor Campus:**
- First building: **`TUL-01`**
- Future expansion: `TUL-02`, `TUL-03`, etc.

**Numbering Rules:**
- Two digits support up to 99 buildings per campus
- Sequential numbering by construction order
- Skip numbers for cancelled projects (maintain chronology)

---

### Level 3: Floor Level
**Format:** `XXX-##-F#` (Campus + Building + Floor)

**Pryor Data Center (Multi-Level):**
- Ground floor: **`TUL-01-F1`**
- Mezzanine (NOC, offices): **`TUL-01-F2`**
- Upper level (gym): **`TUL-01-F3`**

**Future Multi-Story Buildings:**
- Basement: `F0` or `FB`
- Ground: `F1`
- Second floor: `F2`, etc.
- Penthouse: `FPH`

---

### Level 4: Zone/Area Type
**Format:** `XXX-##-F#-ZZZ` (Campus + Building + Floor + Zone Code)

**Zone Codes:**

| Code | Description | Example |
|------|-------------|---------|
| **DH#** | Data Hall | `DH1`, `DH2` |
| **EYN** | Equipment Yard - North | Mechanical yard |
| **EYS** | Equipment Yard - South | Electrical yard |
| **SUB** | Substation | 138 kV substation |
| **NOC** | Network Operations Center | - |
| **MDA** | Main Distribution Area | Telecom backbone |
| **MMR#** | Meet-Me Room | `MMR1` (east), `MMR2` (west) |
| **MPE#** | MPOE (Main Point of Entry) | `MPE1`, `MPE2` |
| **MER#** | Mechanical/Electrical Room | `MER1`, `MER2` |
| **CHY** | Chiller Yard | - |
| **GNY** | Generator Yard | - |
| **STG** | Staging Area | Loading dock |
| **SHL** | Storm Shelter | FEMA 361 shelter |
| **OFC** | Office Area | - |
| **BRK** | Break Room | - |
| **LDG** | Loading Dock | - |

**Pryor Examples:**
- **`TUL-01-F1-DH1`** = Data Hall 1 (ground floor)
- **`TUL-01-F1-DH2`** = Data Hall 2 (ground floor)
- **`TUL-01-F2-NOC`** = Network Operations Center (mezzanine)
- **`TUL-01-F1-EYN`** = North Equipment Yard (Mechanical)
- **`TUL-01-F1-EYS`** = South Equipment Yard (Electrical)
- **`TUL-01-F1-SUB`** = 138 kV Substation

---

## EQUIPMENT ASSET TAGGING

### Format: `XXX-##-F#-ZZZ-EEEEE-###`

**Components:**
- `XXX-##-F#-ZZZ` = Location (Campus-Building-Floor-Zone)
- `EEEEE` = Equipment Type Code (5 characters max)
- `###` = Sequential Unit Number (3 digits)

---

## EQUIPMENT TYPE CODES (COMPLETE LIST)

### **ELECTRICAL EQUIPMENT**

| Code | Description | Example | Notes |
|------|-------------|---------|-------|
| **XFMSU** | Substation Transformer (138kV/11kV) | `TUL-01-F1-SUB-XFMSU-001` | 2N redundancy: -001, -002 |
| **XFMR** | Power Transformer (11kV/480V) | `TUL-01-F1-EYS-XFMR-001` | Sequential 001-008 |
| **GEN** | Generator | `TUL-01-F1-EYS-GEN-001` through `GEN-006` | N+1 redundancy |
| **RMU** | Ring Main Unit (11 kV switchgear) | `TUL-01-F1-EYS-RMU-001` | Ring A: 001-003, Ring B: 004-006 |
| **SWBD** | Switchboard (480V) | `TUL-01-F1-EYS-SWBD-A`, `SWBD-B` | 2N: Path A/B |
| **UPS-IT** | IT UPS Module | `TUL-01-F1-EYS-UPS-IT-001-A` | Path A: 001-005, Path B: 001-005 |
| **UPS-MC** | Mechanical UPS Module | `TUL-01-F1-EYS-UPS-MC-001` | N+1: 001-020 |
| **BATT** | Battery Cabinet | `TUL-01-F1-EYS-BATT-001` | Grouped with UPS modules |
| **PANEL** | Distribution Panel | `TUL-01-F1-DH1-PANEL-001` | Per zone |
| **PDU** | Rack PDU | `TUL-01-F1-DH1-PDU-R001-A` | Rack 1, A-side |
| **ATS** | Automatic Transfer Switch | `TUL-01-F1-EYS-ATS-001` | - |
| **PDM** | Power Delivery Module | `TUL-01-F1-EYS-PDM-A`, `PDM-B` | 2N paths |
| **BRKR** | Circuit Breaker | `TUL-01-F1-EYS-BRKR-001` | Major breakers only |
| **METER** | Power Meter | `TUL-01-F1-EYS-METER-001` | Revenue/submetering |

### **MECHANICAL EQUIPMENT**

| Code | Description | Example | Notes |
|------|-------------|---------|-------|
| **CHLR** | Chiller | `TUL-01-F1-EYN-CHLR-L1-001` | Loop 1, Unit 1 |
| **PUMP** | Pump | `TUL-01-F1-EYN-PUMP-L1-P01` | L1=Loop, P=Primary |
| **CDU** | Coolant Distribution Unit | `TUL-01-F1-DH1-CDU-R001-A` | Cabinet 1, A-side |
| **FCU** | Fan Coil Unit (in-cabinet) | `TUL-01-F1-DH1-FCU-R001` | Cabinet 1 |
| **AHU** | Air Handling Unit | `TUL-01-F1-DH1-AHU-001` | - |
| **DOAS** | Dedicated Outdoor Air System | `TUL-01-F1-DH1-DOAS-001` | White space pressurization |
| **RTU** | Rooftop Unit | `TUL-01-F1-NOC-RTU-001` | Support spaces |
| **EXPTK** | Expansion Tank | `TUL-01-F1-EYN-EXPTK-L1-001` | Per loop |
| **VLVMX** | Mixing Valve | `TUL-01-F1-EYN-VLVMX-001` | - |
| **VLVBL** | Balancing Valve | `TUL-01-F1-EYN-VLVBL-001` | - |
| **STRN** | Strainer | `TUL-01-F1-EYN-STRN-001` | - |
| **AIRSEP** | Air Separator | `TUL-01-F1-EYN-AIRSEP-001` | - |

### **FIRE & LIFE SAFETY**

| Code | Description | Example | Notes |
|------|-------------|---------|-------|
| **FACP** | Fire Alarm Control Panel | `TUL-01-F1-NOC-FACP-001` | Primary panel |
| **VESDA** | VESDA Detector | `TUL-01-F1-DH1-VESDA-001` | Per zone |
| **SPRKL** | Sprinkler Riser | `TUL-01-F1-DH1-SPRKL-001` | - |
| **SUPPR** | Suppression System (Clean Agent) | `TUL-01-F1-DH1-SUPPR-001` | FM-200/Novec |
| **FEXT** | Fire Extinguisher | `TUL-01-F1-DH1-FEXT-001` | Portable units |
| **FPUMP** | Fire Pump | `TUL-01-F1-FP-FPUMP-001` | - |
| **EMRLT** | Emergency Light | `TUL-01-F1-DH1-EMRLT-001` | Battery-backed |

### **TELECOM & NETWORK**

| Code | Description | Example | Notes |
|------|-------------|---------|-------|
| **RACK** | Telecom/Network Rack | `TUL-01-F1-MMR1-RACK-001` | Carrier equipment |
| **CORE** | Core Switch | `TUL-01-F2-MDA-CORE-A`, `CORE-B` | Redundant pair |
| **FW** | Firewall | `TUL-01-F2-MDA-FW-001` | - |
| **PATCHP** | Fiber Patch Panel | `TUL-01-F1-MMR1-PATCHP-001` | - |
| **ROUTER** | Router | `TUL-01-F2-MDA-ROUTER-001` | - |

### **SECURITY**

| Code | Description | Example | Notes |
|------|-------------|---------|-------|
| **CAM** | Security Camera | `TUL-01-F1-DH1-CAM-001` | Per zone |
| **NVR** | Network Video Recorder | `TUL-01-F2-MDA-NVR-001` | Redundant pair |
| **ACSDR** | Access Control Door Reader | `TUL-01-F1-DH1-ACSDR-001` | Per door |
| **ACSCP** | Access Control Panel | `TUL-01-F2-MDA-ACSCP-001` | Central controller |
| **IDS** | Intrusion Detection Sensor | `TUL-01-F1-DH1-IDS-001` | Motion, glass break |
| **DRSN** | Door Sensor | `TUL-01-F1-DH1-DRSN-001` | Open/close monitoring |

### **BMS/CONTROLS**

| Code | Description | Example | Notes |
|------|-------------|---------|-------|
| **BMS** | BMS Server | `TUL-01-F2-NOC-BMS-001` | Redundant A/B |
| **DDC** | Direct Digital Controller | `TUL-01-F1-EYN-DDC-L1-001` | Per plant/zone |
| **EPMS** | Electrical Power Monitoring Server | `TUL-01-F2-NOC-EPMS-001` | SCADA |
| **DCIM** | DCIM Server | `TUL-01-F2-NOC-DCIM-001` | Asset management |
| **MGC** | Microgrid Controller | `TUL-01-F1-SUB-MGC-001` | IEEE 2030.7 |

---

## CUSTOMER SPACE NAMING

### Cabinets/Racks
**Format:** `XXX-##-F#-DH#-R###` (Campus-Building-Floor-DataHall-Rack)

**Pryor Examples:**
- **`TUL-01-F1-DH1-R001`** = Data Hall 1, Rack 001
- **`TUL-01-F1-DH1-R030`** = Data Hall 1, Rack 030
- **`TUL-01-F1-DH2-R001`** = Data Hall 2, Rack 001

**Rack Numbering Rules:**
- Sequential, left-to-right, front-to-back (when facing cold aisle)
- Start at `R001` in each data hall
- Three digits support up to 999 racks per hall

### Cages/Suites
**Format:** `XXX-##-F#-DH#-C##` (Campus-Building-Floor-DataHall-Cage)

**Examples:**
- **`TUL-01-F1-DH1-C01`** = Data Hall 1, Cage 01 (4-rack cage)
- **`TUL-01-F1-DH1-C02`** = Data Hall 1, Cage 02 (8-rack cage)

**Suites (Larger):**
**Format:** `XXX-##-F#-DH#-S##`

**Examples:**
- **`TUL-01-F1-DH1-S01`** = Data Hall 1, Suite 01 (12-rack suite)

---

## ELECTRICAL PATH DESIGNATION (2N ARCHITECTURE)

### Path A vs. Path B
All dual-fed equipment includes path suffix:

**Switchboards:**
- `TUL-01-F1-EYS-SWBD-A` (Path A)
- `TUL-01-F1-EYS-SWBD-B` (Path B)

**UPS Modules:**
- `TUL-01-F1-EYS-UPS-IT-001-A` (Path A, Module 1)
- `TUL-01-F1-EYS-UPS-IT-002-A` (Path A, Module 2)
- `TUL-01-F1-EYS-UPS-IT-001-B` (Path B, Module 1)
- `TUL-01-F1-EYS-UPS-IT-002-B` (Path B, Module 2)

**Cabinet PDUs:**
- `TUL-01-F1-DH1-PDU-R001-A` (Rack 1, A-side)
- `TUL-01-F1-DH1-PDU-R001-B` (Rack 1, B-side)

**Distribution Panels:**
- `TUL-01-F1-DH1-PANEL-A` (Path A distribution)
- `TUL-01-F1-DH1-PANEL-B` (Path B distribution)

---

## MECHANICAL LOOP DESIGNATION

### Loop Numbering (Phase-Specific)
- **Loop 1:** Air cooling, Loop 1 coil (Coil #1 in cabinet FCUs)
- **Loop 2:** Air cooling, Loop 2 coil (Coil #2 in cabinet FCUs)
- **Loop 3:** Direct-to-chip cooling (D2C)

**Chillers:**
- `TUL-01-F1-EYN-CHLR-L1-001` (Loop 1, Chiller 1)
- `TUL-01-F1-EYN-CHLR-L1-002` (Loop 1, Chiller 2)
- `TUL-01-F1-EYN-CHLR-L1-003` (Loop 1, Chiller 3)
- `TUL-01-F1-EYN-CHLR-L1-004` (Loop 1, Chiller 4)
- `TUL-01-F1-EYN-CHLR-L3-001` through `L3-008` (Loop 3, Phase 2)

**Pumps:**
- `TUL-01-F1-EYN-PUMP-L1-P01` (Loop 1, Primary Pump 1)
- `TUL-01-F1-EYN-PUMP-L1-S01` (Loop 1, Secondary Pump 1)

---

## GENERATOR & TRANSFORMER NUMBERING

### Generators (Sequential by Installation)
- `TUL-01-F1-EYS-GEN-001` through `GEN-006`
- **Phase 1:** `GEN-001`, `GEN-002`, `GEN-003`
- **Phase 2:** `GEN-004`, `GEN-005`, `GEN-006`

**Rationale:** Sequential numbering regardless of ring assignment (simplifies identification)

### Transformers (11kV/480V)
- `TUL-01-F1-EYS-XFMR-001` through `XFMR-008`
- **Phase 1:** `XFMR-001`, `XFMR-002`, `XFMR-003`
- **Phase 2:** `XFMR-004` through `XFMR-008`

### Ring Main Units (11 kV)
- **Ring A:** `TUL-01-F1-EYS-RMU-001`, `RMU-002`, `RMU-003`
- **Ring B:** `TUL-01-F1-EYS-RMU-004`, `RMU-005`, `RMU-006`

**Rationale:** Ring assignment embedded in sequential numbering (001-003 = Ring A, 004-006 = Ring B)

---

## PHYSICAL ASSET LABELS

### Label Format (QR Code + Human-Readable)

```
┌─────────────────────────────┐
│  [QR CODE]                  │
│                             │
│  TUL-01-F1-EYS-GEN-001      │
│  Generator #1 (Path A)      │
│  4.0 MW @ 11 kV             │
│  Serial: [VENDOR-SN]        │
│  Commissioned: [DATE]       │
└─────────────────────────────┘
```

**Label Specifications:**
- **Size:** 4" × 6" minimum (larger for big equipment)
- **QR Code:** Links to DCIM asset record (dynamic URL)
- **Font:** Sans-serif, minimum 12pt for human-readable text
- **Colors:** Black text on white/silver background (high contrast)

**Label Placement:**
- **Primary label:** Front panel, eye level (5-6 ft AFF)
- **Backup label:** Rear or side panel (for large equipment)
- **Cable entry:** Small labels at cable/conduit entry points

**Label Material:**
- **Outdoor equipment:** Anodized aluminum, UV-resistant
- **Indoor equipment:** Laminated polyester (3M or equivalent)
- **Method:** Laser-engraved (permanent, no fade, chemical resistant)

---

## CABLE & CONDUIT TAGGING

### Cable ID Format
**Format:** `[SOURCE]-[DEST]-[TYPE]-###`

**Examples:**
- `SWBD-A-PANEL-DH1-PWR-001` (Power cable from SWBD-A to DH1 panel)
- `RMU-001-XFMR-001-MV-001` (MV cable from RMU-001 to XFMR-001)
- `MMR1-DH1-R001-FIBER-001` (Fiber from MMR1 to Rack 001)
- `XFMR-001-SWBD-A-LV-001` (LV cable from XFMR-001 to SWBD-A)

**Cable Type Codes:**
- `PWR` = Power cable (480V or below)
- `MV` = Medium voltage cable (11 kV)
- `FIBER` = Fiber optic
- `CAT6` = Category 6 copper
- `CTRL` = Control wiring
- `INST` = Instrumentation

**Cable Labels:**
- **Frequency:** Every 10 ft + at terminations (both ends)
- **Material:** Vinyl wrap-around labels or heat-shrink sleeves
- **Color coding:** Optional by voltage level (red=480V, yellow=11kV, blue=fiber)

---

## DATABASE/DCIM INTEGRATION

### Asset Registry Fields (Required)

| Field | Example | Notes |
|-------|---------|-------|
| **Asset ID** | `TUL-01-F1-EYS-GEN-001` | Primary key |
| **Asset Type** | Generator | From equipment type code |
| **Location** | TUL-01-F1-EYS | Zone assignment |
| **Vendor** | Caterpillar | Manufacturer |
| **Model** | 3516E | Model number |
| **Serial Number** | CAT12345XYZ | Vendor SN |
| **Capacity** | 4.0 MW @ 11 kV | Nameplate rating |
| **Commissioned Date** | 2026-06-15 | ISO 8601 format |
| **Warranty Expiration** | 2031-06-15 | - |
| **Maintenance Schedule** | [Link] | PM schedule reference |
| **Path/Loop** | Ring A | Redundancy group |
| **BMS Point** | GEN-001-STATUS | Control system address |
| **Drawing Reference** | E-401, Sheet 12 | As-built drawing |
| **Photo** | [Link to image] | Equipment photo |

### QR Code Implementation
- **URL Format:** `https://dcim.sagadata.com/asset/TUL-01-F1-EYS-GEN-001`
- **Dynamic link:** Redirects to current DCIM record (survives DCIM platform changes)
- **Mobile-friendly:** Accessible via smartphone for field technicians

---

## EXAMPLE: COMPLETE PRYOR DATA CENTER ASSET LIST (SAMPLE)

### Electrical Equipment (Sample)

| Asset ID | Description | Location | Path/Ring |
|----------|-------------|----------|-----------|
| `TUL-01-F1-SUB-XFMSU-001` | 138kV/11kV Transformer A | Substation | 2N-A |
| `TUL-01-F1-SUB-XFMSU-002` | 138kV/11kV Transformer B | Substation | 2N-B |
| `TUL-01-F1-EYS-GEN-001` | Generator 1, 4.0 MW | Electrical Yard South | Ring A |
| `TUL-01-F1-EYS-GEN-002` | Generator 2, 4.0 MW | Electrical Yard South | Ring A |
| `TUL-01-F1-EYS-GEN-003` | Generator 3, 4.0 MW | Electrical Yard South | Ring B |
| `TUL-01-F1-EYS-RMU-001` | Ring Main Unit 1 | Electrical Yard South | Ring A |
| `TUL-01-F1-EYS-XFMR-001` | 11kV/480V Transformer 1, 3.5 MVA | Electrical Yard South | Ring A |
| `TUL-01-F1-EYS-SWBD-A` | Switchboard Path A | Electrical Yard South | Path A |
| `TUL-01-F1-EYS-UPS-IT-001-A` | IT UPS Module 1, Path A | Electrical Yard South | Path A |

### Mechanical Equipment (Sample)

| Asset ID | Description | Location | Loop |
|----------|-------------|----------|------|
| `TUL-01-F1-EYN-CHLR-L1-001` | Chiller L1-1, 1,500 kW | Equipment Yard North | Loop 1+2 |
| `TUL-01-F1-EYN-CHLR-L1-002` | Chiller L1-2, 1,500 kW | Equipment Yard North | Loop 1+2 |
| `TUL-01-F1-EYN-PUMP-L1-P01` | Primary Pump L1-P1 | Equipment Yard North | Loop 1 |
| `TUL-01-F1-DH1-FCU-R001` | Cabinet FCU, Rack 1 | Data Hall 1 | Loop 1+2 |
| `TUL-01-F1-DH1-CDU-R001-A` | CDU Rack 1, A-side | Data Hall 1 | Loop 3 |

### Customer Racks (Sample)

| Asset ID | Description | Customer |
|----------|-------------|----------|
| `TUL-01-F1-DH1-R001` | Rack 001 | Customer A |
| `TUL-01-F1-DH1-R002` | Rack 002 | Customer A |
| `TUL-01-F1-DH1-R003` | Rack 003 | Customer B |

---

## SUMMARY RUBRIC

| Level | Format | Example | Description |
|-------|--------|---------|-------------|
| **Campus** | `XXX` | `TUL` | Airport IATA code |
| **Building** | `XXX-##` | `TUL-01` | Campus + Building # |
| **Floor** | `XXX-##-F#` | `TUL-01-F1` | Building + Floor |
| **Zone** | `XXX-##-F#-ZZZ` | `TUL-01-F1-DH1` | Zone/Area code |
| **Equipment** | `XXX-##-F#-ZZZ-EEEEE-###` | `TUL-01-F1-EYS-GEN-001` | Full asset ID |
| **Rack** | `XXX-##-F#-DH#-R###` | `TUL-01-F1-DH1-R001` | Cabinet location |
| **Path** | Add `-A` or `-B` | `SWBD-A`, `PDU-R001-B` | Electrical path |
| **Loop** | Add `-L#` | `CHLR-L1-001` | Mechanical loop |
| **Cable** | `SRC-DST-TYPE-###` | `SWBD-A-PANEL-PWR-001` | Cable ID |

---

## BENEFITS OF THIS STANDARD

**Scalability:**
- Supports global expansion (unlimited campuses, 99 buildings/campus)
- Accommodates multi-story, multi-hall, multi-customer deployments

**Parseability:**
- Machine-readable (DCIM, BMS, CMMS integration)
- Structured format enables automated validation and reporting

**Human-Friendly:**
- Intuitive hierarchy (location → equipment → unit)
- Self-documenting (asset ID reveals location and type)

**Future-Proof:**
- Three-digit equipment numbers (001-999) support large deployments
- Flexible zone codes accommodate new facility types

**Operational Efficiency:**
- Technicians locate equipment quickly (even without DCIM access)
- Reduces errors in maintenance work orders and incident response
- Simplifies spare parts inventory management (standardized equipment)

---

**Document Control:**
- **Revision:** 01
- **Date:** October 30, 2025
- **Prepared by:** EVS / PGCIS Team
- **Approved by:** [Pending]
- **Next Review:** Annual or upon facility expansion

---

**Tags:** #naming-standard #asset-tagging #dcim #operations #standards