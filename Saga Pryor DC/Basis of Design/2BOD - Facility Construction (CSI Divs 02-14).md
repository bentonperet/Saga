

# BASIS OF DESIGN - FACILITY CONSTRUCTION
## CSI Divisions 02-14
### Pryor Data Center - PACHYDERM GLOBAL

**Parent Document:** [[Saga Pryor DC/Basis of Design/Erik_BOD_Updated/_BOD - Exec Summary and TOC]]  

---

## OVERVIEW

38,000 SF single-story precast concrete tilt-up building with FM 1-150 tornado-resistant roof, housing 20,000 SF of white space (two 10,000 SF data halls: DH-W and DH-E), 18,000 SF support spaces, and multi-level central spine.

**Key Features:**
- **Construction:** Precast concrete tilt-up walls (tornado resistance)
- **Roof:** FM 1-150 rating (150 mph 3-second gust, hail resistance)
- **Floor:** Slab-on-grade (raised floor: Not Applicable), sealed concrete
- **Ceiling height:** 30 ft clear in data halls (overhead MEP distribution)
- **Containment:** Not Applicable (DDC cabinets provide integrated cooling)
- **Storm shelter:** FEMA 361 compliant (EF5 protection)

---

## DIVISION 02 – EXISTING CONDITIONS

### Site Prep
- Demolition: None (greenfield site)
- Clearing & grubbing: Tree removal, topsoil strip and stockpile
- Erosion control: Silt fences, sediment basins per SWPPP

---

## DIVISION 03 – CONCRETE

### Foundation System
- **Type:** Spread footings below frost line (18-24")
- **Bearing:** TBD per geotech report
- **Data hall slab:** 6-8" reinforced concrete, 4,000 PSI, FF 50 / FL 40 flatness, densifier/sealer finish
- **AI rack floor load:** 750 PSF sustained (supports 3,500 lb racks like NVIDIA GB200 NVL72)

### Equipment Pad Foundations
- **Chillers, generators:** Individual isolated pads; vibration isolation if required
- **Transformers:** Oil containment per EPA SPCC

---

## DIVISION 04 – MASONRY
Not applicable (precast tilt-up construction, no CMU)

---

## DIVISION 05 – METALS

### Structural Steel Roof Framing
- **System:** Clear-span steel joists and beams; 28-30 ft clear height
- **Loading:** MEP equipment (cable tray, HVAC duct, lighting) + FM 1-150 wind/hail
- **Seismic:** IBC Seismic Design Category B (Oklahoma)

---

## DIVISION 06 – WOOD, PLASTICS, AND COMPOSITES
Minimal scope (office millwork, shelving)

---

## DIVISION 07 – THERMAL AND MOISTURE PROTECTION

### Precast Concrete Tilt-Up Walls

**Why Precast Tilt-Up (Not PEMB):**
- **Tornado resistance:** EF3+ wind speeds (precast withstands impacts better than metal)
- **Insurance:** 20-30% premium reduction vs. PEMB in tornado-prone regions {TBC}
- **Durability:** 50+ year lifespan, low maintenance
- **Fire resistance:** Non-combustible, 4-hour fire rating (if required)

**Panel Specifications:**
- **Thickness:** 8-10" precast concrete panels {TBC}
- **Insulation:** Rigid foam insulation sandwich (R-19 min)
- **Finish:** Architectural texture or smooth finish (exterior); painted drywall (interior)
- **Connections:** Steel embeds, welded/bolted to foundation and roof

**Cost Premium:**
- Precast tilt-up ~$25-40/SF more than PEMB {TBC}
- Total building envelope premium: ~$1.3-2.0M for 50,000 GSF {TBC}
- Offset by insurance savings (~$200-300K/year → 5-7 year payback) {TBC}

### Roof System (FM 1-150 Rating)

**FM 1-150 Compliance:**
- **Wind:** 150 mph 3-second gust (EF2-EF3 tornado resistance)
- **Hail:** Class 4 hail impact resistance (2" diameter ice balls)
- **Fire:** Class A roof assembly (non-combustible)

**Roof Assembly:**
- **Structural deck:** Steel roof deck (substrate for roofing assembly)
- **Insulation:** Polyisocyanurate or equivalent, mechanically fastened + adhered
- **Roofing membrane:** TPO or EPDM, fully adhered (final weather surface)
- **Compliance:** FM 1-150 standard for 150 mph wind, Class 4 hail, fire rating

**Roof Access:**
- **Location:** Via elevator and adjacent stairwell from central spine
- **Access door:** Weather-protected with overhang providing rain/hail/snow protection
- **Purpose:** Periodic roof inspections and maintenance
- **Code:** OSHA 1910.23 (guardrails/fall protection), IBC roof access requirements

**Roof-Mounted Equipment Protection:**
- Storm-rated stainless steel debris screen around perimeter
- Impact-resistant enclosures for all roof equipment (HVAC, exhaust fans, vent shafts)

**Roof Drainage:**
- Interior roof drains (6" diameter) at low points
- Overflow scuppers at roof edge (backup)
- Design for 100-year storm event per IBC

**Cost:**
- FM 1-150 premium: ~$8-12/SF vs. standard roof {TBC}
- Debris screen and equipment protection: ~$100-200K {TBC}
- Total roof premium: ~$500-800K for 50,000 GSF {TBC}

### Air and Vapor Barriers
- **Air barrier:** Self-adhered membrane at precast joints, penetrations
- **Vapor barrier:** Under slab; at wall insulation per climate
- **Target:** TBD but we want a tight envelope for PUE

---

## DIVISION 08 – OPENINGS

### Exterior Doors
- **Main entry:** Glazed aluminum storefront, double doors (6 ft clear) {TBC}
- **Loading dock:** Overhead sectional door (12 ft W × 14 ft H, insulated)
- **Emergency exits:** Steel doors with panic hardware (minimum 2 per data hall)
- **Fire rating:** 2-hour where required by IBC

### Security Mantrap (Main Building Entry)

**Location:** Main entrance to building

**Configuration:** Double-door airlock mantrap with single-person occupancy enforcement

**Access Control:**
- Outer door: Card reader (all authorized personnel)
- Inner door: Card reader + biometric MFA (Level 2+ clearance) {TBC}
- Interlocked operation (outer closes before inner opens)
- CCTV with facial recognition, fire override, integration with SCR

### Data Hall Doors
- **Large equipment doors:** At least two double doors per data hall with 10 ft H × 8 ft W minimum clear opening for large equipment moves (UPS modules, chillers, transformers)
- **Standard doors:** Other doors may be 4 ft single pedestrian doors
- **Hardware:** Card reader + biometric (two-factor authentication, MFA required)
- **Clearance:** Level 4 (Secure Operations) or higher for unescorted access
- **Vision panels:** Wire glass (optional for visibility)
- **Forced entry resistance (HR sites):** 15-minute rating for exterior doors
- **Integration:** Access events logged to DCIM for asset correlation

### Electrical and Mechanical Room Doors (Red Zone)
- **Width:** 3-4 ft single doors
- **Hardware:** Card reader + biometric (MFA)
- **Clearance:** Level 3 (Technical Staff) minimum, Level 5 for certain areas
- **Forced entry resistance (HR sites):** 15-minute rating for exterior doors
- **Emergency egress:** Panic hardware on interior side (life safety)

---

## DIVISION 09 – FINISHES

### Data Hall Finishes
- **Floor:** Sealed concrete (densifier + sealer), light gray
- **Walls:** Painted gypsum board over precast (interior side) or exposed precast
- **Ceiling:** Exposed structure and MEP (no suspended ceiling)
- **Paint:** Low-VOC, white or light colors (reflectivity)

---

## DIVISION 10 – SPECIALTIES
- Signage (wayfinding, room IDs, exit signs)
- Fire extinguisher cabinets (recessed)
- Toilet accessories (ADA-compliant)
- Whiteboards in conference rooms

---

## DIVISION 11 – EQUIPMENT
See CSI Div 23 (HVAC), 26 (Electrical), 27 (Telecom)

---

## DIVISION 12 – FURNISHINGS
Not in base building scope (owner-furnished)

---

## DIVISION 13 – SPECIAL CONSTRUCTION

### FEMA 361 Storm Shelter/Safe Room

**Purpose:** Protect personnel from EF5 tornadoes

**Specifications:**
- **Capacity:** 20 persons (staff + tenant personnel)
- **Type:** Prefabricated modular safe room
- **Location:** First floor, near center of building, adjacent to elevator serving Level 2 (Secure NOC) and Level 3 (Fitness Area/Tour Route)
- **Construction:** Prefabricated steel or reinforced concrete module (FEMA 361 compliant)
- **Door:** Blast-rated steel door, secure locking (opens outward per module design)
- **Ventilation:** Integrated HVAC/ventilation system with battery backup, HEPA filtration
- **Utilities:** Emergency lighting, communication equipment
- **Security during emergencies:** Auto-unlock on tornado warning or fire alarm

**Cost:** ~$75-150K (prefabricated module + installation){TBC}

**Compliance:**
- FEMA P-361 (Safe Rooms for Tornadoes and Hurricanes)
- ICC 500 (Standard for Storm Shelters)

**Benefits:**
- Life safety (primary)
- Insurance premium reduction {TBC}
- Faster installation vs. site-built
- Factory-tested and certified

---

### Security Control Room (SCR) (Red Zone - CP 5)

**Purpose:** 24/7 central monitoring for all security systems (Red Zone - CP 5)

**Physical Security:**
- Forced-entry resistant construction (15-minute rating minimum)
- Reinforced steel door with card + biometric MFA (Level 4/5 access only)
- Duress button for emergency escalation

**Systems:**
- Redundant security servers with automatic failover (99.982% availability)
- Dual power feeds (A/B paths) with UPS and generator backup
- Video wall for CCTV monitoring
- 90-day minimum data retention (camera footage, access logs)

**Environment:**
- Dedicated HVAC (68-75°F, 40-60% RH)
- Sized for 3-4 operator workstations plus equipment racks

**Staffing:**
- 24/7/365 operation with Level 4/5 clearance required

---

### Clean In/Clean Out (CICO) Checkpoint (Orange Zone - CP 4 Entry)

**Purpose:** Screen all equipment and materials entering/exiting data halls (Orange Zone - CP 4 Entry)

**Infrastructure:**
- Dedicated checkpoint with tailgate prevention
- Walk-through magnetometer with UPS backup
- Inspection tables for tool/equipment examination
- CCTV with facial recognition integrated to SCR

**Prohibited Items:**
- Personal mobile phones, cameras, unapproved wireless devices
- Unauthorized storage media (USB drives, external HDDs)

**Asset & Tool Control:**
- Pre-authorization via work order required
- Entry/exit inspection and logging
- 90-day audit trail retention

**Staffing:**
- Level 4 clearance security personnel during operational hours

---

## DIVISION 14 – CONVEYING EQUIPMENT

### Elevator
- **Type:** Hydraulic or traction elevator
- **Capacity:** 2,500-3,500 lb (12-16 persons)
- **Stops:** 4 stops (Level 1, Level 2, Level 3, Roof)
- **Purpose:** Access to Level 2 (Secure NOC), Level 3 (Fitness Area/Tour Route), and Roof (inspections/maintenance)
- **Roof access:** Weather-protected door with overhang for rain/hail/snow protection
- **Location:** Central spine, adjacent to storm shelter/safe room on Level 1
- **Code:** ASME A17.1, ADA-compliant, OSHA 1910.23 (roof access)
- **Cost:** ~$175-225K

---

## BUILDING LAYOUT (38,000 SF)

### Data Halls (20,000 SF - Orange Zone CP 4)
- **Data Hall West (DH-W):** 10,000 SF (Phase 1 operational) - Orange Zone CP 4
- **Data Hall East (DH-E):** 10,000 SF (powered shell, future fit-out) - Orange Zone CP 4
- **Ceiling height:** 30 ft clear
- **Layout:** Overhead power/cooling distribution (containment: Not Applicable - DDC cabinets)
- **Access:** 4 secure doors per hall accessible from perimeter corridor (card + biometric MFA required)

### East End Entry Zone (Ground Level)
**Main Entrance (Blue Zone - CP 2):**
- Lobby with luggage room, public restroom, Security Control Room (SCR - Red Zone)

**Secure Office Zone (Yellow Zone - CP 3, Post-Mantrap):**
- Conference room, restrooms, hoteling office area, soundproof call pods
- MPOE and MMR (Red Zone - fiber entrance and meet-me-room)

**Perimeter Corridor (Yellow Zone - CP 3):**
- Secure corridor with 4 access doors per data hall (Orange Zone entry)
- Access to indoor mechanical galleries and multi-level central spine

### West End Loading Zone (Ground Level)
**Loading Dock (Yellow Zone - CP 3):**
- 2-bay weather-protected loading area with Security Control Booth (SCB - Red Zone)
- Secure staging, storage, fire riser, internal restroom
- Second MPOE and MMR (redundant fiber entrance and meet-me-room - Red Zone)
- Delivery driver restroom (exterior access, view of security)

### Multi-Level Central Spine (3 Levels in Spine, 1 Level Elsewhere)

**Level 1 (Ground - Yellow Zone):**
- Prefabricated storm shelter (20 person, FEMA 361 compliant)
- Elevator/stairwell, restrooms, showers, break room, lounge

**Level 2 (Secure NOC - Red Zone):**
- Network Operations Center (~2,060 SF) with 24/7 operations

**Level 3 (Fitness/Tour Route - Yellow Zone):**
- Gym/fitness center, secure tour route with internal windows into critical areas
- Weather-protected balconies (north/south) for equipment yard viewing

**Roof Level:**
- Elevator/stairwell access with weather-protected door
- Storm-rated SS debris screen, protected roof equipment

### Support Spaces
- North/south mechanical pipe galleries (Red Zone - indoor maintenance)
- Power Delivery Modules (PDMs - Red Zone - outdoor electrical yard)
- IT storage and spare parts (Yellow Zone)

---

## KEY DESIGN DECISIONS

### Why Precast Tilt-Up (Not PEMB)?
- **Tornado risk:** Oklahoma is EF3-EF5 zone; precast provides superior impact/wind resistance
- **Insurance:** FM Global/insurance carriers require hardened construction in tornado regions
- **Long-term:** 50+ year lifespan, minimal maintenance vs. PEMB corrosion/repair

### Why FM 1-150 Roof?
- **Wind:** 150 mph 3-second gust exceeds most tornado wind speeds below EF3
- **Insurance:** Premium reduction offsets cost in 5-7 years
- **Customer confidence:** Tier III uptime requires robust envelope

### Why FEMA 361 Storm Shelter/Safe Room?
- **Life safety:** Oklahoma tornado fatalities; shelter protects staff/visitors during extreme events
- **Code:** May become required by local AHJ in tornado-prone areas
- **Insurance:** Demonstrates commitment to risk mitigation

---

## COST SUMMARY (PHASE 4 FULL BUILD-OUT)

### Direct Construction Costs

| System | Cost Estimate | Confidence | Notes |
|--------|---------------|------------|-------|
| **Foundation & Slab** | $2,280,000 | ±25% | 38,000 SF @ $60/SF; upgraded for 750 PSF AI rack loads, FF 50/FL 40 |
| **Precast Tilt-Up Walls** | $4,200,000 | ±25% | ~50,000 SF @ $84/SF; 8-10" insulated panels, tornado-rated construction |
| **Structural Steel Roof Frame** | $2,660,000 | ±23% | Enhanced clear-span joists/beams for 30 ft clear + FM 1-150 loads |
| **FM 1-150 Roof + Debris Protection** | $2,400,000 | ±25% | 50,000 SF @ $48/SF; TPO membrane, insulation, debris screen, enhanced fastening |
| **Multi-Level Central Spine Structure** | $3,500,000 | ±27% | 3-level structure (NOC level 2, fitness level 3, roof access), stairs, steel framing |
| **Elevator (4-stop with roof access)** | $600,000 | ±20% | Heavy-duty traction, 3,500 lb capacity, 4 stops including roof, weather protection |
| **Doors, Windows, Glazing** | $1,200,000 | ±30% | Security mantrap, 4 large equipment doors per hall (10'H × 8'W), standard doors, glazing |
| **Interior Finishes (Enhanced)** | $3,000,000 | ±27% | Data halls, offices, NOC, fitness area, break rooms, restrooms, sealed concrete, drywall, paint, acoustic ceilings |
| **Building HVAC (Office/Support)** | $1,500,000 | ±30% | Rooftop units for offices, NOC, support spaces (separate from data hall HVAC in Div 23) |
| **Plumbing (Domestic/Sanitary)** | $650,000 | ±27% | Restrooms, break rooms, showers, domestic water, sanitary drainage (data hall cooling in Div 23) |
| **FEMA 361 Storm Shelter** | $150,000 | ±25% | Prefab module, 20-person capacity, EF5-rated, HVAC, emergency lighting |
| **Subtotal (Direct Costs)** | **$22,140,000** | **±27%** | |

### Professional Services

| Item | Cost Estimate | Confidence | Notes |
|------|---------------|------------|-------|
| **Architectural & Engineering (7%)** | $1,550,000 | ±20% | Architect, structural, envelope consultant, specifications |
| **Subtotal** | **$23,690,000** | **±27%** | |
| **TOTAL BUILDING CONSTRUCTION** | **$23,690,000** | **±27%** | **Shell + core + interior fit-out (excludes MEP data hall systems in other divisions)** |

**Cost per SF:** $623/SF (38,000 SF building)
**Cost per kW (IT Load):** $1,077/kW (22 MW)
**Industry Benchmark:** $900-$1,400/kW for AI-ready, tornado-hardened facilities

**Note on Cost Increase:**
Previous estimate of $314/SF was significantly below market for tornado-hardened construction with multi-level spine and comprehensive interior fit-out. Industry standards for comparable facilities range $550-$700/SF in non-coastal markets.

---

## CODES AND STANDARDS
- **IBC 2021** (International Building Code), Oklahoma amendments
- **ASCE 7-16** (wind/seismic loads)
- **ACI 318** (concrete design)
- **AISC 360** (steel design)
- **NEC 2023** (duct bank installation per Articles 300.5 and 300.50)
- **FM 1-150** (roof wind uplift and hail resistance)
- **FEMA P-361** (safe rooms, missile impact resistance)
- **ICC 500** (storm shelters)
- **ASTM E1886/E1996** (hurricane debris impact testing)
- **OSHA 1910.23** (roof access, guardrails, fall protection)

---

**Tags:** #facility #construction #precast-tilt-up #fm-1-150 #tornado #storm-shelter 

**Next Steps:**
1. Coordinate with Insurance to confirm savings on walls, roof and safe room
2. Geotechnical report (bearing capacity, slab design, duct bank burial depth)
3. Electrical engineering (duct bank sizing, conduit quantity for 24 MW capacity)
4. Structural engineering (precast panel design, roof framing, duct bank coordination)
5. FM Global loss prevention review (roof/wall ratings)
6. Storm shelter/safe room design (FEMA 361 compliance)
7. Architectural drawings (floor plans, elevations, details, duct bank locations)

---

**Document Control:**
- **Source:** PGCIS Team
- **Date Updated:** October 29, 2025
- **Prepared by:** PGCIS Team
- **Key Updates:** Precast tilt-up rationale, FM 1-150 roof, FEMA 361 shelter/safe room
