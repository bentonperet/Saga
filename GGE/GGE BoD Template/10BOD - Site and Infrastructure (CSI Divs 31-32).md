**Created:** 2025-10-29
**Updated from:** Pryor_Bod_EVS_Rev01.md + Erik_BOD references

# BASIS OF DESIGN - SITE AND INFRASTRUCTURE
## CSI Divisions 31-32
### Pryor Data Center - PACHYDERM GLOBAL

**Parent Document:** [[_BOD - Exec Summary and TOC]]

---

## DIVISION 31 – EARTHWORK

### Site Characteristics
- **Parcel:** ~120 acres (master plan)
- **Topography:** Slightly rolling; balanced cut/fill expected
- **Flood/Tornado:** Outside FEMA floodplain; high tornado risk (EF3+ region)
- **Soils:** TBD by geotechnical; design for frost depth per Oklahoma code

### Required Surveys and Studies
- ALTA/NSPS land survey (boundaries, easements, topo)
- Geotechnical investigation (bearing, CBR, slab support)
- Phase I ESA; wetlands/waters delineation if applicable
- Utility locates and capacity confirmations (water, sewer, gas, fiber)

### Site Grading and Pads
- **Building pad:** 50,000 GSF building (precast tilt-up) + aprons
- **Electrical yard:** ~100,000 SF (345 kV substation, MV gear, generator yard)
- **Mechanical yard:** ~50,000 SF (air-cooled chillers, pumps, headers)
- **Solar array area:** Allocate 10–20 acres adjacent (phased build)
- **BESS yard:** Allow 6–10 container positions (future-ready)

### Subgrade and Earthwork
- Over-excavate poor soils; import select fill (per Geo report)
- Proof-roll building pad; 95% compaction (ASTM D698 unless D1557 required)
- Underground utility trenches: sand bedding, warning tape, marker posts

---

## DIVISION 32 – EXTERIOR IMPROVEMENTS

### 345 kV Substation Yard (Customer-Owned)
- **Footprint:** ~35,000–50,000 SF fenced yard
- **Equipment:** 345 kV switchyard, 2 × 25 MVA 345kV/13.8kV transformers (2N), protection & control house
- **Grounding:** Copper grid per IEEE 80; step/touch potential analysis
- **Oil containment:** Transformer spill containment per EPA SPCC
- **Security:** 8–10 ft fence + barbed wire, cameras, access control

### Medium-Voltage (13.8 kV) Distribution
- Dual-ring MV ductbanks encircling building (Ring A/B)
- Concrete-encased ductbank, galvanized ground grid bonding at RMUs
- Pull boxes/manholes at 300–500 ft intervals; spare conduits for expansion

### Generator Yard (MV Generators)
- **Capacity:** 6 × 4.0 MW @ 13.8 kV diesel gens (N+1 at 12 MW design)
- **Pads:** Individual concrete pads with anchorage; crane access aisle
- **Fuel:** ~2,000 gal belly tanks per unit connected via common fuel manifold to centralized bulk fuel storage tank farm (24 hours runtime); spill containment per SPCC
- **Bulk Fuel Storage:** Above-ground or underground tank farm (~12,000 gal capacity for Phase 2) with redundant fuel service contracts (24-hour SLA)
- **Noise:** Enclosures targeting ≤65 dBA @ 7 m at property line compliance
- **Security:** Fenced, CCTV, vehicle barriers at perimeter
- **Access:** East-west emergency/maintenance access points for equipment delivery and temporary rental equipment

### Mechanical Yard (Air-Cooled)
- **Phase 1:** 4 × 1,500 kW chillers; **Phase 2:** +8 (total 12)
- **Layout:** Two rows with 15 ft service corridors; overhead pipe racks to building
- **Drainage:** Sloped slabs; trench drains to oil/water separator where needed
- **Access:** East-west emergency/maintenance access points for equipment delivery
- **Temporary Equipment Support:** Connection provisions for rental chillers and load banks via quick-connects and cable pass-through doors

### Building Envelope Equipment Yard Interface

**Cable Pass-Through Doors:**
- Multiple small access doors (~dog door sized, approximately 24" × 24") in building envelope at equipment yard boundaries
- Purpose: Pass temporary cables/hoses from secure equipment yard into building without opening larger doors
- Applications:
  - Temporary load bank connections during testing
  - Rental generator paralleling cables
  - Backup chiller piping/connections
  - Testing equipment hookups
- Security: Normally sealed/secured; opened only during authorized maintenance activities
- Location: Marked on as-built drawings with clear access paths from equipment yards

### Solar and BESS Areas
- **Solar:** Inverter stations at 13.8 kV tie to common bus (separate fenced area)
- **BESS:** 4–8 MWh containers; 13.8 kV bi-directional inverters; space for growth
- **Fire lanes:** 20 ft access; signage; clearances per NFPA 855 for energy storage

### Stormwater Management
- **Detention/Retention:** Southeast "horseshoe/moat" basin; sized for local criteria
- **Quality:** Forebay + outlet control; bioswales where feasible
- **Discharge:** Match pre-development rates; protect downstream receiving waters

### Paving and Hardscape
- **Access roads:** 12" aggregate base; asphalt or PCC pavement per truck loads
- **Dock apron:** 10" PCC with doweled joints
- **Parking:** 30–45 stalls; EV-ready conduits stubbed
- **Walks:** 6 ft sidewalks to entries; ADA routes and ramps

### Site Access and Entrances

**Two Property Entrances:**

**1. Main Entrance (NE Corner):**
- Primary manned entrance with sally port vehicle trap
- Permanent visitor center (climate-controlled guard post)
- Full-height pedestrian turnstile adjacent to vehicle entrance
- K4-rated vehicle arrestor
- Primary access for all normal operations, deliveries, visitors, and personnel

**2. Secondary Entrance (NW Side - Emergency/Construction Access):**
- Normally unmanned emergency and construction entrance
- Single-gate with K4-rated vehicle arrestor
- Card-controlled pedestrian gate
- Remote operation visible from Security Control Booth (SCB) at loading dock
- Used for emergencies or special construction/maintenance activities (not employed during normal operations)

### Fencing, Lighting, and Landscaping
- **Perimeter fence:** 8 ft + 3-strand barbwire or ornamental steel (AHJ)
- **Lighting:** LED poles at yards and perimeter; photocell + BMS control
- **Landscaping:** Native drought-tolerant planting; clear CCTV sightlines

---

## SITE LAYOUT (High-Level)

- **NE Corner:** Main entrance with sally port vehicle trap and permanent visitor center
- **NW Side:** Secondary emergency/construction entrance (normally unmanned, visible from loading dock SCB)
- **North:** Electrical yard (generators, substation, RMUs)
- **South:** Mechanical yard (chillers, pumps, pipe racks)
- **East/West:** Dual MPOE/MMR fiber entries; delivery dock on leeward side
- **Southeast:** Detention basin; public frontage landscaped buffer

---

## CODES AND STANDARDS
- IBC/IFC 2021 (local amendments)
- NFPA 110, 70 (NEC), 855 (for BESS if deployed)
- IEEE 80 (substation grounding), 142 (grounding), 484/485 (battery rooms as applicable)
- Oklahoma DEQ stormwater and erosion control

---

## COST SUMMARY (ROM)
| Scope | ROM Cost |
|-------|---------|
| Earthwork, grading, pads | $0.7–1.2M |
| MV ductbanks, manholes | $0.6–1.0M |
| Substation yard civil (excl. electrical) | $0.4–0.8M |
| Generator/Chiller yards civil | $0.4–0.8M |
| Paving, parking, dock | $0.4–0.7M |
| Fencing, lighting, landscaping | $0.3–0.6M |
| Stormwater basin & LID | $0.3–0.6M |
| Total Div 31–32 (civil scope) | $3.1–5.7M |

---

**Tags:** #site #infrastructure #substation #yards #stormwater #ductbank #csi-31-32

**Next Steps:**
1. Complete topo and geotechnical; finalize grading and pad elevations
2. Lay out MV ductbank/ring routes and manholes
3. Substation civil/grounding design (IEEE 80 study)
4. Finalize stormwater basin hydraulics/hydrology
5. Site plan approval and permits (grading, stormwater)

---

**Document Control:**
- **Source:** Pryor_Bod_EVS_Rev01.md, Electrical Div 26, Erik_BOD references
- **Date Updated:** October 29, 2025
- **Prepared by:** EVS / PGCIS Team
- **Key Updates:** 345 kV substation yard, MV rings, BESS/solar yards, 50,000 SF mech yard