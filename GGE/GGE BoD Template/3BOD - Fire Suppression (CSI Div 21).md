**Created:** 2025-10-29
**Updated from:** Tbilisi_Bod_Rev01.md

# BASIS OF DESIGN - FIRE SUPPRESSION
## CSI Division 21
### Tbilisi Data Center - PACHYDERM GLOBAL

**Parent Document:** [[_BOD - Exec Summary and TOC]]

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
- **Sprinkler heads:** ESFR (Early Suppression Fast Response), K-25.2
- **Coverage:** Per NFPA 13 (130-200 SF per head for data center)
- **Water demand:** [ROM] 1,500-2,000 GPM @ 70 psi (full system)
- **Zoned demand:** Lower flow rate per zone activation (typical 500-800 GPM per zone)

**DDC Cabinet Integrated Suppression:**
- DDC cabinets include factory-integrated fire suppression
- Coordinates with building preaction system
- Provides additional protection at cabinet level

### Data Hall 2 (Future Fit-Out)

- Same system type as Data Hall 1
- Installed with shell or deferred to tenant fit-out

### Prefabricated Power Delivery Modules (PDMs)

**2 × Outdoor PDMs (Phase 1)**

**System Type:** Clean agent or other suppression per NFPA standards

**Configuration:**
- Factory-installed clean agent (FM-200, Novec 1230) or water mist per NFPA 2001/NFPA 750
- Cylinder bank sized for PDM enclosure volume
- Automatic discharge on smoke detection
- Manual abort button (30-second delay)
- **Rationale:** Protects UPS, switchboards, batteries without water damage
- **Red Zone - CP 5** security classification

**Cost:** Integrated in PDM package (~$50-100K per PDM)

### Generator Enclosures

**6 × Outdoor Generator Sets**

**System Type:** Portable fire extinguishers only

**Rationale:**
- Open-air enclosures with natural ventilation
- Diesel fuel fire risk (Class B)
- Fixed suppression not typically required for outdoor gen sets
- Portable extinguishers: 2 × 20 lb ABC per generator

**Optional:** Pre-engineered suppression system if required by AHJ or insurance
- Cost: +$25-50K per generator

---

## MECHANICAL ROOMS & CHILLER YARD

### Indoor Mechanical Spaces

**System Type:** Wet pipe sprinkler

**Configuration:**
- Standard NFPA 13 coverage
- Sprinkler heads: 130-200 SF per head
- Avoid heads directly above electrical panels (sidewall heads if needed)

### Outdoor Chiller Yard (~50,000 SF)

**System Type:** Portable fire extinguishers

**Rationale:**
- Open-air equipment (natural smoke/heat dissipation)
- Fixed suppression not required for outdoor chillers
- Extinguishers: 2 × 20 lb ABC per chiller plant zone

---

## OFFICE, NOC, SUPPORT SPACES

### System Type: WET PIPE SPRINKLER

**Coverage:**
- Standard commercial spacing per NFPA 13
- Light hazard occupancy (offices)
- Sprinkler heads: ~130 SF per head

**Special Areas:**

**Network Operations Center (NOC - Red Zone CP 5):**
- Consider preaction or clean agent if NOC contains critical equipment
- Standard wet pipe acceptable for office areas
- Raised floor: Not Applicable (slab-on-grade)

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
  - Holes every 10-15 ft along pipe
  - 4-6 sampling pipes per data hall
- **Sensitivity levels:**
  - Alert: 0.005% obscuration/ft (investigate, no evacuation)
  - Action: 0.015% obscuration/ft (pre-alarm, prepare suppression)
  - Fire 1: 0.03% obscuration/ft (alarm, evacuate, suppress)
  - Fire 2: 0.05% obscuration/ft (full alarm)
- **Response time:** <60 seconds from smoke event to alert
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
- Estimated demand: 1,500-2,000 GPM @ 70 psi for 2 hours
- Duration: ~180,000-240,000 gallons

### Fire Pump & Storage (If Municipal Service Inadequate)

**Fire Pump:**
- **Type:** Electric or diesel-driven (diesel preferred for reliability)
- **Capacity:** Sized to meet demand (1,500-2,000 GPM @ 70 psi)
- **Rating:** UL-listed per NFPA 20
- **Location:** Separate fire pump room (non-freezing)
- **Controller:** Automatic start on pressure drop

**Storage Tank:**
- **Capacity:** 250,000-300,000 gallons (includes hose stream allowance)
- **Type:** Bolted steel or welded steel, API 650
- **Location:** Outdoor, adjacent to fire pump room
- **Makeup:** Municipal water or periodic water delivery (if no utility)
- **Heating:** Tank heater if subject to freezing

**Cost:** ~$750K-1.5M (pump + tank + installation)

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
- Data hall travel distance: [ROM] <150 ft (compliant)

**Doors:**
- Panic hardware on exit doors (no keys required for egress)
- Magnetic hold-open with fire alarm release
- Self-closing on alarm

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
- **IBC 2021** (International Building Code), Georgia amendments
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

## COST SUMMARY

| System | Cost Estimate |
|--------|---------------|
| **Data Hall Preaction (10,000 SF)** | $300-500K |
| **Data Hall Clean Agent (Alternative)** | +$500-800K |
| **PDM Integrated Suppression (2 units)** | Included in PDM cost |
| **Wet Pipe (Support Spaces)** | $150-250K |
| **VESDA Detection (Data Halls)** | $100-200K |
| **Fire Alarm System (Addressable)** | $150-250K |
| **Fire Pump + Storage (If Needed)** | $750K-1.5M |
| **Portable Extinguishers** | $15-25K |
| **Total (Preaction Option)** | **$1.5-2.7M** |
| **Total (Clean Agent Option)** | **$2.0-3.5M** |

---

**Tags:** #Tbilisi-dc #fire-suppression #preaction #clean-agent #vesda #nfpa #tier-iii

**Next Steps:**
1. Coordinate with insurance broker for FM Global approval requirements
2. Fire water availability study (municipal service or on-site storage)
3. Hydraulic sprinkler calculations (if preaction selected)
4. Clean agent design calculations (if gas suppression selected)
5. VESDA sampling point layout and airflow modeling

---

**Document Control:**
- **Source:** Tbilisi_Bod_Rev01.md and Erik_BOD reference
- **Date Updated:** October 29, 2025
- **Prepared by:** EVS / PGCIS Team
- **Key Updates:** Preaction vs. clean agent analysis, VESDA specifications, FM Global compliance
