**Created:** 2025-10-29
**Updated from:** Pryor_Bod_EVS_Rev01.md

# BASIS OF DESIGN - FIRE SUPPRESSION
## CSI Division 21
### Pryor Data Center - PACHYDERM GLOBAL

**Parent Document:** [[Saga Pryor DC/Basis of Design/Erik_BOD_Updated/_BOD - Exec Summary and TOC]] 

---

## OVERVIEW

Fire protection systems protect personnel, IT equipment, and facility infrastructure while meeting NFPA, IBC, FM Global, and insurance requirements. Multi-layered approach includes early detection, automatic suppression, and clear egress paths.

**Design Philosophy:**
- **Very early detection:** VESDA (Very Early Smoke Detection Apparatus) in data halls
- **Zoned preaction sprinkler:** Primary suppression system for data halls
- **Life safety first:** Clear egress, emergency lighting, notification
- **Insurance compliance:** FM Global approval for premium reduction

---

## FIRE SUPPRESSION STRATEGY

### Data Hall 1 (10,000 SF White Space - Orange Zone CP 4)

**System Type: ZONED PREACTION SPRINKLER (Primary System)**

**Configuration:**
- **Type:** Zoned dual-interlock preaction system
- **Zones:** Multiple independent zones for targeted suppression control
- **Activation sequence:**
  1. VESDA detects smoke → pre-alarm (investigate)
  2. Second detection zone confirms → alarm
  3. Heat activation (sprinkler fusible link) → water release to specific zone only
- **Benefit:** Dry pipe until both smoke + heat detected; zoned activation limits water discharge area

**DDC Cabinet Integrated Suppression:**
- DDC cabinets include factory-integrated fire suppression
- Coordinates with building preaction system
- Provides additional protection at cabinet level

### Data Hall 2 (Future Fit-Out)

- Same system type as Data Hall 1
- Installed with shell or deferred to tenant fit-out

### E-Houses (Electrical Houses)

**2 × Outdoor E-Houses (Phase 1-4, one per 13.8 kV ring)**

**E-House Specifications:**
- **Dimensions:** Each 14' W × 260' L (3,640 SF)
- **Contents:** MV switchgear (RMUs), LV switchboards, IT UPS, Mechanical UPS, battery cabinets, distribution panels
- **Configuration:** E-House A (Ring A) and E-House B (Ring B)

**System Type:** Clean agent suppression per NFPA 2001

**Configuration:**
- Factory-installed clean agent (Novec 1230 or FM-200)
- Cylinder bank sized for 3,640 SF @ 14' ceiling height (~51,000 cubic feet per E-House)
- Zone coverage: Full E-House interior with uniform agent distribution
- Automatic discharge on smoke detection (cross-zoned with two independent detection circuits)
- Manual abort button (30-second delay before discharge)
- Pre-discharge alarms: Audible/visual with 30-second evacuation warning
- **Rationale:** Protects MV/LV electrical gear, UPS, switchboards, batteries without water damage or conductive residue
- **Red Zone - CP 5** security classification

**Detection:**
- Cross-zoned smoke detection (two independent detector zones required for discharge)
- Addressable smoke detectors throughout E-House
- Integration with facility fire alarm panel

**Cost:** Integrated in E-House package (~$80-120K per E-House, larger than typical due to 3,640 SF enclosure size)

### LV Transformer Yard

**11 × 3.5 MVA Outdoor Transformers (Phase 1-4)**

**Location:** Outdoor concrete pads with oil containment adjacent to E-Houses

**System Type:** Portable fire extinguishers

**Configuration:**
- Portable Class C electrical fire extinguishers at transformer yard (2 units minimum)
- No fixed fire suppression required for outdoor oil-filled transformers
- Oil containment per EPA SPCC requirements (110% of transformer oil volume)
- Spill response equipment and absorbent materials on-site

**Rationale:** Outdoor transformers have natural ventilation and heat dissipation; fixed suppression not required per NFPA 850

### Generator Enclosures
<!-- @claude - please write a 1-2 sentence statement about the enclosure required -->

---

## MECHANICAL ROOMS & CHILLER YARD

### Indoor Mechanical Spaces

**System Type:** Wet pipe sprinkler

**Configuration:**
- Standard NFPA 13 coverage
- Avoid heads directly above electrical panels (sidewall heads if needed)

### Outdoor Chiller Yard

**System Type:** Portable fire extinguishers

**Rationale:**
- Open-air equipment (natural smoke/heat dissipation)
- Fixed suppression not required for outdoor chillers

---

## OFFICE, NOC, SUPPORT SPACES

### System Type: WET PIPE SPRINKLER

**Coverage:**
- Standard commercial spacing per NFPA 13
- Light hazard occupancy (offices)

**Special Areas:**

**Network Operations Center (NOC - Red Zone CP 5):**
- Consider preaction or clean agent if NOC contains critical equipment
- Standard wet pipe acceptable for office areas

**MPOE/MMR (Fiber Entrance Rooms - Red Zone CP 5):**
- Preaction dry pipe or clean agent (protects carrier equipment)
- Coordinate with carrier requirements
- Critical telecommunications infrastructure protection

**Storm Shelter/Safe Room (FEMA 361 Compliant Prefabricated Module):**
- Integrated fire suppression per module manufacturer (typically wet pipe or clean agent)
- 20 person capacity, Level 1 location
- Emergency lighting and signage per FEMA P-361

---

## FIRE DETECTION & ALARM SYSTEM

### Detection Technology by Zone

**Data Halls (Critical Detection):**
- **Type:** VESDA (Very Early Smoke Detection Apparatus) or equivalent ASD
- **Sampling points:** Air sampling pipes at ceiling level
- **Sensitivity levels:** Multi-stage alarming (alert, action, fire alarm levels)
- **Integration:** BMS, DCIM, fire alarm panel

**PDMs (Electrical Rooms):**
- Spot-type photoelectric smoke detectors (addressable)
- Heat detectors (rate-of-rise + fixed temp 135°F)
- Integration with clean agent suppression system

**Mechanical Rooms:**
- Spot-type smoke detectors (every 500 SF)
- Heat detectors (135°F fixed temp)

**Office/NOC/Support Spaces:**
- Spot-type smoke detectors per NFPA 72
- Spacing: Every 500-900 SF depending on ceiling height
- Duct smoke detectors in HVAC supply/return

**Generator Yard:**
- Heat detectors in enclosed gen set housings (if applicable)
- No detection required for open-air enclosures

### Fire Alarm Control Panel (FACP)

**System Configuration:**
- **Type:** Addressable, intelligent fire alarm system
- **Manufacturer:** [TBD - e.g., Notifier, Simplex, Edwards]
- **Network:** Fiber backbone, redundant pathways
- **Zones:** Separate addressable zones for each major area
- **Annunciation:** Remote annunciators at NOC, main entrance, loading dock

**Integration:**
- **BMS:** Status monitoring, alarm forwarding
- **Access control:** Unlock all doors on alarm
- **HVAC:** Shutdown air handlers, close smoke dampers
- **Suppression systems:** Trigger preaction/clean agent discharge

**Remote Monitoring:**
- Central station monitoring (UL-listed service)
- Direct dial to fire department (if permitted by AHJ)
- NOC 24/7 monitoring with alarm escalation procedures

### Notification Appliances

**Audible:**
- Horns/speakers at 90 dB minimum (15 dB above ambient)
- Voice evacuation capability (EVAC panels)
- Distinct tones for alert vs. alarm

**Visual:**
- Strobes per NFPA 72 (ADA compliant)
- Red strobes in all occupied areas
- Minimum 75 candela in public areas

---

## FIRE WATER SUPPLY

### Municipal Water Connection

**If Available:**
- 8-12" fire service connection (separate from domestic)
- Underground loop with PIV (post indicator valve) and FDC (fire department connection)
- Backflow preventer: Double-check valve assembly
- Hydrant spacing: ~300 ft around perimeter

**Demand Calculation:**
- Design basis: ESFR sprinklers in data hall (most demanding)
- Demand and duration per NFPA 13 hydraulic calculations

### Fire Pump & Storage (If Municipal Service Inadequate)

**Fire Pump:**
- **Type:** Electric or diesel-driven (diesel preferred for reliability)
- **Capacity:** Sized per NFPA 13 hydraulic demand calculations
- **Rating:** UL-listed per NFPA 20
- **Location:** Separate fire pump room (non-freezing)
- **Controller:** Automatic start on pressure drop

**Storage Tank:**
- **Capacity:** Per NFPA 13 demand calculations (includes hose stream allowance)
- **Type:** Bolted steel or welded steel, API 650
- **Location:** Outdoor, adjacent to fire pump room
- **Makeup:** Municipal water or periodic water delivery (if no utility)
- **Heating:** Tank heater if subject to freezing


---

## EGRESS & LIFE SAFETY

### Occupancy & Load
**Data Halls:**
- Classification: Group B (Business) per IBC Section 304
- Occupant load: ~10 persons (one person per 100 SF gross)

**Support Spaces:**
- Offices, NOC, break rooms: Group B
- Total facility load: 20-30 persons

### Egress Requirements

**Exit Count:**
- Minimum 2 exits from each data hall (IBC Section 1006)
- Exits remotely located (diagonal separation)

**Exit Width:**
- Minimum 36" clear width per IBC
- Preferred 44" (allows equipment carts)

**Travel Distance:**
- Maximum 200 ft to nearest exit (unsprinklered areas)
- Maximum 300 ft (sprinklered areas) per IBC Table 1017.2
- Data hall travel distance: TBD

**Doors:**
- Panic hardware on exit doors (no keys required for egress)
- Magnetic hold-open with fire alarm release

### Containment

**Containment:** Not Applicable (DDC cabinets provide integrated cooling - no hot/cold aisle containment required)

### Emergency Lighting

**Coverage:**
- All egress paths, stairwells, data halls
- Battery-backed LED fixtures (90-minute runtime minimum)
- Illumination: 1 fc average, 0.1 fc minimum per NFPA 101

**Exit Signs:**
- Illuminated LED exit signs (battery-backed)
- Red or green letters (AHJ preference)
- Maximum 100 ft spacing in corridors

---

## PORTABLE FIRE EXTINGUISHERS

### Distribution

**Class A/C (Offices, Data Halls):**
- Type: ABC dry chemical or clean agent (Halotron for data halls)
- Size: 10-20 lb
- Spacing: Maximum 75 ft travel distance per NFPA 10

**Class B (Generator Yard, Mechanical):**
- Type: ABC dry chemical or Purple K
- Size: 20 lb
- Spacing: Maximum 50 ft travel distance

**Special Locations:**
- Data hall entrances: 2 × 20 lb Halotron
- Generator sets: 2 × 20 lb ABC per generator
- Mechanical rooms: 2 × 20 lb ABC per room

### Mounting & Signage

- Wall-mounted brackets (5 ft AFF to handle)
- Signage: "FIRE EXTINGUISHER" with directional arrow
- Inspections: Annual inspection, 6-year maintenance, 12-year hydrostatic test

---

## CODES AND STANDARDS

- **NFPA 13** (Installation of Sprinkler Systems)
- **NFPA 72** (National Fire Alarm and Signaling Code)
- **NFPA 75** (Fire Protection of Information Technology Equipment)
- **NFPA 2001** (Clean Agent Fire Extinguishing Systems)
- **NFPA 101** (Life Safety Code)
- **NFPA 20** (Installation of Stationary Pumps for Fire Protection)
- **IBC 2021** (International Building Code), Oklahoma amendments
- **FM Global Data Sheet 5-4** (Transformers)
- **FM Global Data Sheet 5-32** (General Storage)

---

## INSURANCE & FM GLOBAL APPROVAL

### FM Global Requirements (Data Center)

**Suppression:**
- Preaction dry pipe or clean agent in data halls
- ESFR sprinklers (if wet/preaction)
- Clean agent in UPS/electrical rooms

**Detection:**
- VESDA or equivalent very early smoke detection
- Dual-stage alarming (alert + alarm)

**Egress:**
- Clear exit paths, emergency lighting, notification

**Testing:**
- Quarterly fire alarm testing
- Annual sprinkler flow testing
- VESDA calibration every 6-12 months

**Benefits of Compliance:**
- 20-30% insurance premium reduction
- Faster claim processing
- Risk engineering support from FM Global

---

## COST SUMMARY (PHASE 4 FULL BUILD-OUT)

### Executive Summary

| System                               | Subtotal       | Confidence | Notes                                                |
| ------------------------------------ | -------------- | ---------- | ---------------------------------------------------- |
| **Data Hall Preaction Sprinkler**    | $1,200,000     | ±20%       | 20,000 SF @ $60/SF, ESFR heads, 6 zones, enhanced coverage |
| **VESDA Detection System**           | $480,000       | ±15%       | Both data halls + support spaces, 40 sampling points, redundant panels |
| **Fire Alarm System (Comprehensive)** | $1,200,000    | ±20%       | Dual redundant panels, 350 detectors, 150 notification devices, 38,000 SF, full integration |
| **Wet Pipe Sprinkler (Support)**     | $680,000       | ±20%       | 18,000 SF office/mechanical spaces @ $38/SF          |
| **E-House Clean Agent Suppression**  | $240,000       | ±20%       | 2 × E-Houses (3,640 SF each), Novec 1230, cross-zoned detection |
| **Fire Water Service & Distribution** | $450,000      | ±15%       | Municipal connection, fire pump, hydrants, backflow, underground distribution |
| **Portable Extinguishers & Cabinets** | $55,000       | ±10%       | 75 units, various types, recessed cabinets, signage, annual inspection |
| **Emergency Lighting & Egress**      | $550,000       | ±20%       | 38,000 SF facility, generator-backed, LED fixtures, photoluminescent signage |
| **Testing & Commissioning**          | $350,000       | ±15%       | Full system acceptance, integrated testing, NFPA compliance, training |
| **Subtotal (Direct Costs)**          | **$5,205,000** |            |                                                      |
| **Design/Engineering (10%)**         | $520,500       |            | Fire protection engineering, hydraulic calcs, NFPA review, shop drawings |
| **Contingency (15%)**                | $858,825       |            | Phase 4 design stage allowance                       |
| **TOTAL PROJECT COST**               | **$6,584,325** |            | **Range: $5.6M - $7.6M**                             |

**Cost per kW (IT Load):** $299/kW (22 MW)
**Industry Benchmark:** $150-$300/kW for Tier III fire protection


---

### Pricing Assumptions & Methodology

**Unit Costs Basis:**
- RS Means 2024/2025 Cost Data
- Data center quality standards (exceeds commercial grade)
- Prevailing wage labor rates (union likely for project scale)

**Quantity Calculation Methods:**
- **Sprinkler heads:** NFPA 13 spacing for ESFR (100 SF/head @ 30 ft ceiling)
- **Piping:** 0.65 LF/SF for data hall preaction, 0.40 LF/SF for support wet pipe
- **VESDA sampling:** 1 point per 1,000 SF (conservative data center standard)
- **Fire alarm devices:** NFPA 72 spacing (smoke: 500-900 SF, strobe: 2,500 SF)
- **Emergency lighting:** 1 fixture per 500-750 SF based on egress paths

**Items Excluded from This Estimate:**
- E-house clean agent suppression (included in E-house package cost, not priced separately)
- DDC cabinet integrated suppression (included in DDC cabinet cost)
- Storm shelter suppression (included in prefab module cost)
- Annual operating costs (central station monitoring: ~$3,500/year, inspections: ~$8,000/year)

**Major Cost Drivers:**
- Municipal water availability eliminates $750K-1.5M fire pump/storage cost
- VESDA detection adds ~$165K vs. standard smoke detection (~$40K) = $125K premium for FM Global compliance
- Preaction system adds ~$90K vs. wet pipe (6 zones @ $15K each) = acceptable for water damage risk mitigation


---

**Next Steps:**
1. Coordinate with insurance broker for fire safety requirements
2. Fire water availability study (municipal service or on-site storage)
3. Hydraulic sprinkler calculations (if preaction selected)
4. Clean agent design calculations (if gas suppression selected)
5. VESDA sampling point layout and airflow modeling

---

**Document Control:**
- **Source:** Erik_BOD reference
- **Date Updated:** October 29, 2025
- **Key Updates:** Preaction vs. clean agent analysis, VESDA specifications, FM Global compliance