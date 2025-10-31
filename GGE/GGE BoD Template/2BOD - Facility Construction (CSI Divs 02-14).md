**Created:** 2025-10-29
**Updated from:** Tbilisi_Bod_Rev01.md + Erik_BOD references

# BASIS OF DESIGN - FACILITY CONSTRUCTION📄 Reading markdown file...
🔍 Parsing markdown...
   Found 207 blocks
🔐 Authenticating with Google...📄 Reading markdown file...
🔍 Parsing markdown...
   Found 208 blocks
🔐 Authenticating with Google...
📝 Creating Google Doc...

✅ Document published successfully!

   Title: 2BOD - Facility Construction (CSI Divs 02-14)
   URL:   https://docs.google.com/document/d/1N2R3Y5WCPaKgS-DXX_0AV5DwFKA2ftX6LiTEQbsmkWw/edit


📝 Creating Google Doc...

## CSI Divisions 02-14
### Tbilisi Data Center - PACHYDERM GLOBAL

**Parent Document:** [[_BOD - Exec Summary and TOC]]

---

## OVERVIEW

50,000 GSF single-story precast concrete tilt-up building with FM 1-150 tornado-resistant roof, housing 20,000 SF of white space (two 10,000 SF data halls), 30,000 SF support spaces, and multi-level central spine.

**Key Features:**
- **Construction:** Precast concrete tilt-up walls (tornado resistance)
- **Roof:** FM 1-150 rating (150 mph 3-second gust, hail resistance)
- **Floor:** Slab-on-grade (raised floor: Not Applicable), sealed concrete
- **Ceiling height:** 28-30 ft data halls (overhead MEP distribution)
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
- **Type:** Spread footings on native soil (pending geotech)
- **Depth:** Below frost line (Georgia: ~18-24")
- **Bearing:** [TBD per geotech report, assume 3,000 psf min]
- **Slab-on-grade:** 6-8" reinforced concrete, 4,000 psi, WWF or fiber mesh
- **Subbase:** 6" aggregate; vapor barrier per ASHRAE 62.1

### Under-Building Electrical Duct Banks

**Purpose:** Provide protected, optimal electrical pathways between north and south equipment yards

**Configuration:**
- **Quantity:** Minimum 8 large duct banks installed beneath building prior to foundation pour
- **Routing:** North-south pathway providing shortest route between equipment yards
- **Entry points:** Minimum 2 entry points per duct bank at north and south ends of each data hall area
  - Data Hall 1 (East): 4 entry points (2 north, 2 south)
  - Data Hall 2 (West): 4 entry points (2 north, 2 south)
- **Capacity:** Sized to accommodate conduits and cables for 24 MW total power capacity
  - 12 MW per side (East and West)
  - Future expansion capability to full 24 MW master plan

**Design Specifications:**
- **Duct bank construction:** PVC-coated steel or HDPE conduit encased in concrete
- **Conduit sizing:** [TBD based on 13.8 kV or 480V distribution voltage and cable type]
  - Typical: 4-6" conduits for MV feeders (13.8 kV)
  - Multiple conduits per duct bank for redundancy and capacity
- **Concrete encasement:** 6" minimum on all sides per NEC 300.5 and 300.50
- **Burial depth:** Minimum 30" below finished grade; coordinate with foundation depth
- **Spacing:** Adequate separation between duct banks for thermal management and maintenance access
- **Pull boxes:** Located at strategic points for cable installation and maintenance
- **Entry risers:** Sealed penetrations through foundation with fire-stop and waterproofing

**Coordination:**
- Install duct banks prior to foundation/slab pour
- Coordinate with structural engineer for foundation loads and reinforcement
- Coordinate with electrical engineer for conduit sizing and quantity
- Survey and document duct bank locations for as-built drawings

**Rationale:**
- **Protection:** Concrete-encased duct banks protect cables from environmental damage and mechanical impact
- **Shortest path:** Direct north-south routing minimizes voltage drop and cable costs
- **Future-proof:** Sized for full 24 MW capacity supports master plan expansion
- **Reliability:** Multiple duct banks provide redundancy and diverse pathways

**Cost:** ~$300-500K (duct banks, concrete encasement, excavation, coordination)

### Data Hall Slab
- **Flatness:** FF 50 / FL 40 minimum (forklift traffic, server racks)
- **Finish:** Power-troweled, densifier/sealer (dust-proof, cleanable)
- **Color:** Light gray or epoxy coating (optional for reflectivity)
- **Joints:** Saw-cut control joints @15 ft o.c.; sealed

### AI Rack Floor Load Design Criteria
- **Live Load:** 750 PSF sustained (accommodates AI/HPC racks up to 3,500 lbs)
- **Slab Thickness:** 8-10" reinforced concrete (final thickness per geotechnical report)
- **Concrete Strength:** 4,000 PSI minimum
- **Reinforcement:** #4 rebar @ 12" o.c. each way, OR welded wire fabric (WWF) 6×6 W2.9×W2.9
- **Subbase:** 6" compacted aggregate base, 95% compaction (ASTM D698)
- **Flatness:** FF 50 / FL 40 (laser-level tolerance for rack alignment)
- **Joints:** Saw-cut control joints @ 15 ft o.c., sealed with polyurethane sealant
- **Finish:** Power-troweled, densifier/sealer (dust-proof, cleanable)
- **Load Cases:** Supports 3,500 lb racks like NVIDIA GB200 NVL72, forklift wheel loads up to 8,000 lbs
- **Future-proof:** Designed for AI/HPC rack configurations expected through 2030+

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
- **Seismic:** IBC Seismic Design Category B (Georgia)
- **Columns:** Minimize in data halls; 50-60 ft grid typical

### Cable Tray and Support Steel
- **Overhead:** Unistrut or equivalent trapeze hangers; seismic bracing
- **Capacity:** Sized for power + fiber cable fills + 25% spare
- **Height:** 12-14 ft above finished floor (AFF) typical

---

## DIVISION 06 – WOOD, PLASTICS, AND COMPOSITES
Minimal scope (office millwork, shelving)

---

## DIVISION 07 – THERMAL AND MOISTURE PROTECTION

### Precast Concrete Tilt-Up Walls

**Why Precast Tilt-Up (Not PEMB):**
- **Tornado resistance:** EF3+ wind speeds (precast withstands impacts better than metal)
- **Insurance:** 20-30% premium reduction vs. PEMB in tornado-prone regions
- **Durability:** 50+ year lifespan, low maintenance
- **Fire resistance:** Non-combustible, 4-hour fire rating (if required)

**Panel Specifications:**
- **Thickness:** 8-10" precast concrete panels
- **Insulation:** Rigid foam insulation sandwich (R-19 min)
- **Finish:** Architectural texture or smooth finish (exterior); painted drywall (interior)
- **Connections:** Steel embeds, welded/bolted to foundation and roof

**Cost Premium:**
- Precast tilt-up ~$25-40/SF more than PEMB
- Total building envelope premium: ~$1.3-2.0M for 50,000 GSF
- Offset by insurance savings (~$200-300K/year → 5-7 year payback)

### Roof System (FM 1-150 Rating)

**FM 1-150 Compliance:**
- **Wind:** 150 mph 3-second gust (EF2-EF3 tornado resistance)
- **Hail:** Class 4 hail impact resistance (2" diameter ice balls)
- **Fire:** Class A roof assembly (non-combustible)

**Roof Assembly:**
- **Deck:** 22-gauge steel roof deck, welded to joists
- **Insulation:** Polyisocyanurate (polyiso), R-30 min, mechanically fastened + adhered
- **Membrane:** TPO or EPDM, fully adhered (not mechanically fastened), min 80 mil
- **Attachment:** Enhanced deck attachment per FM 1-150 standard

**Roof Access:**
- **Location:** Via elevator and adjacent stairwell from central spine
- **Access door:** Weather-protected with overhang providing rain/hail/snow protection
- **Purpose:** Periodic roof inspections and maintenance
- **Code:** OSHA 1910.23 (guardrails/fall protection), IBC roof access requirements

**Roof-Mounted Equipment Protection:**
- **Perimeter protection:** Storm-rated heavy-duty stainless steel debris screen around roof perimeter
  - **Purpose:** Absorb, deflect, or shred flying debris during storm events
  - **Standards:** FEMA P-361 (missile impact resistance), ICC 500, ASTM E1886/E1996 (hurricane debris impact)
  - **Design:** Engineered to withstand 150 mph winds with 15 lb 2×4 timber projectile at 100 mph
- **Equipment protection:** Each roof-mounted unit (HVAC, AHU, DAHU, exhaust fans, vent shafts) protected with:
  - Impact-resistant enclosures or screens
  - Hail guards (mesh or louver design) for intake/exhaust openings
  - Secure mounting per ASCE 7-16 wind loads and FM 1-150
  - Equipment rated for Class 4 hail impact (2" diameter)
- **Rationale:** Minimize damage from hail, falling debris, and windborne projectiles during tornado/severe storm events

**Roof Drainage:**
- Interior roof drains (6" diameter) at low points
- Overflow scuppers at roof edge (backup)
- Design for 100-year storm event per IBC

**Cost:**
- FM 1-150 premium: ~$8-12/SF vs. standard roof
- Debris screen and equipment protection: ~$100-200K
- Total roof premium: ~$500-800K for 50,000 GSF

### Air and Vapor Barriers
- **Air barrier:** Self-adhered membrane at precast joints, penetrations
- **Vapor barrier:** Under slab (6 mil poly); at wall insulation per climate
- **Target:** <0.25 CFM/SF @ 0.3" w.g. (tight envelope for PUE)

---

## DIVISION 08 – OPENINGS

### Exterior Doors
- **Main entry:** Glazed aluminum storefront, double doors (6 ft clear)
- **Loading dock:** Overhead sectional door (12 ft W × 14 ft H, insulated)
- **Emergency exits:** Steel doors with panic hardware (minimum 2 per data hall)
- **Fire rating:** 2-hour where required by IBC

### Security Mantrap (Main Building Entry)

**Location:** Main entrance to building

**Configuration:** Full control glass security mantrap with double-door airlock

**Operation - Single Person Entry Rule:**
- Only one authorized person permitted within mantrap vestibule at any time
- Inner door remains locked until outer door fully closed and credentials verified

**Access Control:**
- **Outer door:** Card reader (all authorized personnel, visitors with escort)
- **Inner door:** Card reader + biometric MFA (Level 2+ clearance required)
- **Interlock:** Outer must close before inner opens
- **Surveillance:** CCTV cameras with 125 PPFW (Pixels Per Face Width) for positive identification
- **Fire override:** Both doors unlock on fire alarm
- **Delayed egress system:** Local alarm for tailgating deterrence

**Mantrap Requirements:**
- Single-person occupancy enforcement (sensors + visual verification)
- Video recording of all authentication events
- Integration with Security Control Room (SCR) for alarm response
- Intercom for SCR communication on authentication failures

**Facilities Access:**
- Main visitor waiting area (Blue Zone)
- Restrooms and locker connection
- Reception desk for visitor check-in

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

### Windows
- **Office areas (Yellow Zone):** Glazed aluminum windows, low-E glass
- **Data halls (Orange Zone):** No windows (security, environmental control)
- **SCR (Red Zone):** Ballistic-rated or no windows (per risk assessment)

---

## DIVISION 09 – FINISHES

### Data Hall Finishes
- **Floor:** Sealed concrete (densifier + sealer), light gray
- **Walls:** Painted gypsum board over precast (interior side) or exposed precast
- **Ceiling:** Exposed structure and MEP (no suspended ceiling)
- **Paint:** Low-VOC, white or light colors (reflectivity)

### Support Spaces
- **Offices/NOC:** VCT flooring, painted gypsum walls, ACT ceilings
- **Restrooms:** Ceramic tile floors, FRP wall panels
- **Mechanical rooms:** Sealed concrete floors, painted walls
- **Corridors:** VCT or polished concrete; gypsum walls with corner guards

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
- **Normal access:** Card reader (Level 1-2 clearance)

**Cost:** ~$75-150K (prefabricated module + installation)

**Compliance:**
- FEMA P-361 (Safe Rooms for Tornadoes and Hurricanes)
- ICC 500 (Standard for Storm Shelters)

**Benefits:**
- Life safety (primary)
- Insurance premium reduction
- Faster installation vs. site-built
- Factory-tested and certified

---

### Security Control Room (SCR) (Red Zone - CP 5)

**Purpose:** Primary central monitoring station for all electronic security systems, providing 24/7 continuous security oversight.

**Dimensions:**
- Minimum 12 ft × 24 ft (3.65 m × 7.3 m)
- Sized for 3-4 operator workstations plus equipment racks

**Physical Security:**
- **Walls:** Forced-entry or ballistic resistance per risk level
  - **HR sites (Tbilisi DC):** 15-minute forced entry resistance minimum
  - Optional: Ballistic-rated construction
- **Door:** Reinforced steel door with card + biometric (MFA)
  - Access: Level 4 (Secure Operations) or Level 5 only
- **Transaction Window:**
  - **HR sites:** Solid with transaction drawer (not open 4×6 in. opening)
  - Ballistic-rated glass (optional)
- **Interior:** Duress button installed for emergency escalation

**Workstation Security:**
- Clear screen policy enforcement
- Automatic screen lock after maximum 15 minutes of inactivity
- Dual monitors per workstation (minimum)
- Video wall for CCTV grid display

**System Redundancy and High Availability (99.982% Target):**
- **Redundant Security Servers:**
  - Surveillance servers/recorders in active-active or active-passive configuration
  - Storage Area Networks (SAN) with data integrity during failover
- **Redundant Network Infrastructure:**
  - Dual switches and diverse paths for dedicated security systems network
  - Network components in separate cabinets with diverse power feeds
- **Redundant Access Control Servers:** Automatic failover capabilities
- **Diverse Power Sources:** All redundant components powered from different PDUs
- **Continuous Monitoring:** System health monitoring with automated alerts

**Power:**
- All security equipment (panels, racks, workstations) on emergency power
- UPS battery bridge (minimum 15 minutes full load)
- Generator backup for extended outages
- Dual power feeds from separate PDUs (A/B paths)

**Data Integrity and Retention:**
- Historical security data (camera footage, access logs, IDS events) stored minimum 90 days
- Redundant storage architecture ensures data integrity during failover events
- Secure backup to off-site location or cloud (encrypted)

**HVAC:**
- Dedicated HVAC system with N+1 redundancy
- Temperature: 68-75°F (20-24°C)
- Humidity: 40-60% RH
- Independent control from building HVAC

**Staffing:**
- 24/7/365 continuous operation
- Minimum 1 operator on duty at all times
- 2 operators during peak hours (recommended)
- Level 4 or Level 5 security clearance required

**Cost:** ~$400-700K (room construction, redundant systems, furniture, video wall)

---

### Clean In/Clean Out (CICO) Checkpoint (Orange Zone - CP 4 Entry)

**Purpose:** Ensure no unauthorized equipment, materials, or data are brought into or removed from data halls (Orange Zone).

**Location:**
- Dedicated checkpoint at main data hall entrance
- Single main entrance for normal Orange Zone ingress/egress
- Adjacent to Blue Zone or Yellow Zone transition

**Space Requirements:**
- Minimum 300-500 SF
- Adequate space for:
  - Security officer station
  - Item inspection tables (minimum 2 tables, 6 ft × 3 ft each)
  - Full-height magnetometer walkthrough
  - Handheld screening device storage
  - Queuing area for personnel

**Infrastructure:**
- **Tailgate Prevention:** Optical sensors or weight-based technology at entrance
- **Inspection Tables:** Dedicated examination surfaces for tools and equipment
- **Magnetometer:** Full-height walk-through metal detector
  - UPS-backed power supply
  - Sensitivity adjustable for different screening levels
- **Handheld Scanners:** Storage and charging station for handheld metal detectors/wands
- **CCTV Coverage:**
  - **Critical Point Identification standard:** 125 PPFW resolution
  - Coverage of all inspection tables
  - Coverage of personnel screening point
  - Integration with SCR for live monitoring
- **Power:** All screening equipment on UPS-backed power (minimum 30-minute runtime)

**Prohibited Items:**
- Personal mobile phones (must be secured in Blue Zone lockers)
- Cameras (personal or professional)
- Unapproved wireless devices
- Unauthorized storage media (USB drives, external HDDs)
- Defined list maintained and displayed at checkpoint

**Asset & Tool Control Procedure:**
1. **Pre-Authorization:** All tools/equipment/removable media pre-authorized via ticketed work order
2. **Entry Inspection:** Items presented to security, verified against work order
3. **Entry Logging:** Each item logged (description, serial#, individual, work order#, time)
4. **Visual Inspection:** Security inspects all tools, equipment, containers
5. **Exit Inspection:** Mandatory presentation of all items upon exit
6. **Exit Logging:** Exit log updated (time, clearance confirmation)
7. **Audit Trail:** Complete entry/exit records retained minimum 90 days

**Staffing:**
- Manned by dedicated security personnel during all data hall operational hours
- Level 4 (Secure Operations) clearance required
- Training on screening procedures, prohibited items, work order verification

**Integration:**
- Access control system: Level 4+ clearance required for CICO passage
- BMS: Environmental monitoring (temperature, humidity)
- DCIM: Work order verification and asset tracking integration
- SCR: Direct video feed and alarm escalation

**Cost:** ~$150-300K (construction, equipment, screening technology, CCTV)

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

## BUILDING LAYOUT (50,000 GSF)

### Data Halls (20,000 SF - Orange Zone CP 4)
- **Data Hall 1 (East):** 9,980 SF (Phase 1 operational) - Orange Zone CP 4
- **Data Hall 2 (West):** 9,980 SF (powered shell, future fit-out) - Orange Zone CP 4
- **Ceiling height:** 28-30 ft clear
- **Layout:** Overhead power/cooling distribution (containment: Not Applicable - DDC cabinets)
- **Access:** 4 secure doors per hall accessible from perimeter corridor (card + biometric MFA required)

### East End Entry Zone (Ground Level)
**Main Entrance (Blue Zone - CP 2):**
- Entrance lobby with luggage room
- Restroom (public)
- Security Control Room (SCR - Red Zone CP 5) for tenant/staff/visitor check-in

**Secure Office Zone (Yellow Zone - CP 3, Post-Mantrap):**
- Mantrap entry (control point)
- Group conference room
- 2 × restrooms
- Small shared hoteling office area
- 2 × soundproof focus/call pods
- Small seating area
- Fire riser room
- **MPOE (Red Zone - CP 5):** Fiber entrance room (critical telecommunications infrastructure)
- **MMR (Red Zone - CP 5):** Meet-me-room for cross-connects (carrier-neutral infrastructure)

**Perimeter Corridor (Yellow Zone - CP 3):**
- Secure perimeter corridor providing access to secure data hall access points and secure indoor mechanical gallery maintenance areas
- 4 secure access doors per data hall (Orange Zone - CP 4 entry)
- Access to multi-level central spine

### West End Loading Zone (Ground Level)
**Loading Dock (Yellow Zone - CP 3):**
- 2-bay loading dock (weather-protected, outdoor and covered)
- Security Control Booth (SCB - Red Zone - CP 5)
- Secure staging area
- Secure storage
- Janitor closet
- Fire riser room
- **MPOE (Red Zone - CP 5):** Fiber entrance room, second/redundant
- **MMR (Red Zone - CP 5):** Meet-me-room, second/redundant
- Restroom (internal)
- Dedicated delivery driver restroom (accessible only from outside at NW corner, within view of security booth - Blue Zone)

### Multi-Level Central Spine (3 Levels)

**Level 1 (Ground - Yellow Zone CP 3):**
- Prefabricated storm shelter/safe room (20 person capacity - Blue Zone during emergency)
- Elevator and adjacent stairwell
- Redundant restrooms
- Redundant showers (men's and women's)
- Break room with eating area
- Lounge area
- Gaming area/room (TBD)

**Level 2 (Secure NOC - Red Zone CP 5):**
- Network Operations Center (NOC, ~2,060 SF) - 24/7 operations
- Private NOC area
- NOC landing area with restroom/janitor

**Level 3 (Fitness Area/Tour Route - Yellow Zone CP 3 with Orange/Red viewing):**
- Gym/fitness center (Yellow Zone)
- **Secure tour route (Yellow Zone CP 3)** with internal windows into critical areas (Orange/Red viewing only)
- Weather-protected balconies (north and south) for bird's eye view of equipment yards (Violet Zone viewing)
- Tour route accessible to Level 3+ clearance personnel for routine site walks

**Roof Level:**
- Roof access via elevator and adjacent stairwell
- Weather-protected access door with overhang
- Storm-rated stainless steel debris screen around perimeter
- Protected roof-mounted equipment (HVAC, AHU, DAHU, exhaust fans, vent shafts)

### Support Spaces
- **Mechanical pipe galleries (Red Zone - CP 5):** North and south sides indoor maintenance areas
- **Power Delivery Modules (PDMs - Red Zone - CP 5):** Located outside in electrical equipment yard (Violet Zone perimeter)
- **IT storage and spare parts (Yellow Zone - CP 3)**
- **Secure perimeter corridor (Yellow Zone - CP 3)** for data hall and mechanical gallery access

---

## KEY DESIGN DECISIONS

### Why Precast Tilt-Up (Not PEMB)?
- **Tornado risk:** Georgia is EF3-EF5 zone; precast provides superior impact/wind resistance
- **Insurance:** FM Global/insurance carriers require hardened construction in tornado regions
- **Long-term:** 50+ year lifespan, minimal maintenance vs. PEMB corrosion/repair

### Why FM 1-150 Roof?
- **Wind:** 150 mph 3-second gust exceeds most tornado wind speeds below EF3
- **Insurance:** Premium reduction offsets cost in 5-7 years
- **Customer confidence:** Tier III uptime requires robust envelope

### Why FEMA 361 Storm Shelter/Safe Room?
- **Life safety:** Georgia tornado fatalities; shelter protects staff/visitors during extreme events
- **Code:** May become required by local AHJ in tornado-prone areas
- **Insurance:** Demonstrates commitment to risk mitigation

---

## COST SUMMARY (ROM)

|| System | Cost Estimate |
||--------|---------------|
|| **Foundation & Slab** | $1.5-2.5M |
|| **Under-Building Electrical Duct Banks** | $0.3-0.5M |
| **Precast Tilt-Up Walls** | $2.5-4.0M |
| **Structural Steel Roof Frame** | $1.5-2.5M |
|| **FM 1-150 Roof + Debris Protection** | $1.6-2.7M |
|| **Elevator (4-stop with roof access)** | $0.175-0.225M |
| **Doors, Windows, Glazing** | $0.5-1.0M |
| **Interior Finishes** | $1.5-2.5M |
|| **FEMA 361 Storm Shelter/Safe Room** | $0.075-0.15M |
|| **Total Building Construction (shell + core)** | **$9.7-16.3M** |

**Cost per SF:** ~$194-326/SF (higher than typical DC due to tornado hardening and infrastructure)

---

## CODES AND STANDARDS
- **IBC 2021** (International Building Code), Georgia amendments
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

**Tags:** #facility #construction #precast-tilt-up #fm-1-150 #tornado #storm-shelter #csi-02-14

**Next Steps:**
1. Geotechnical report (bearing capacity, slab design, duct bank burial depth)
2. Electrical engineering (duct bank sizing, conduit quantity for 24 MW capacity)
3. Structural engineering (precast panel design, roof framing, duct bank coordination)
4. FM Global loss prevention review (roof/wall ratings)
5. Storm shelter/safe room design (FEMA 361 compliance)
6. Architectural drawings (floor plans, elevations, details, duct bank locations)

---

**Document Control:**
- **Source:** Tbilisi_Bod_Rev01.md, Erik_BOD references
- **Date Updated:** October 29, 2025
- **Prepared by:** EVS / PGCIS Team
- **Key Updates:** Precast tilt-up rationale, FM 1-150 roof, FEMA 361 shelter/safe room, 50,000 GSF layout
