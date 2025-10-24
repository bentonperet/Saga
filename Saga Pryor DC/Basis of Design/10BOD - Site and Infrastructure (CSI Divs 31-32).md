**Created:** 2025-10-23 10:55

# BASIS OF DESIGN - SITE AND INFRASTRUCTURE
## CSI Divisions 31-32
### Saga Energy – Pryor Data Center

**Parent Document:** [[_BOD - Exec Summary and TOC]]
**Related:** [[Basis of Design - Part 1 Core Systems]] | [[Architectural Meeting Changes by CSI Division]]

---

## DIVISION 31 – EARTHWORK

### Site Characteristics
- **Size:** 121 acres
- **Topography:** Relatively flat, minimal grading required (pending ALTA survey confirmation)
- **Location:** Mayes County, Oklahoma (~4 miles from Google Pryor campus)
- **Access:** Frontage road with adequate ingress/egress for truck traffic

### Site Surveys Required
- **ALTA/NSPS Survey:** Confirm legal boundaries, easements, topography
- **Geotechnical Investigation:** Soil bearing capacity, foundation design recommendations
- **Water Delineation Study:** Identify wetlands or floodplains
- **Environmental Phase I:** Hazardous materials assessment

### Site Grading
- **Building Pad:** Grading for 40,000 SF white space data center building + support spaces
- **Equipment Yards:** Grading for chiller yard, generator yard, BESS enclosure
- **Access Roads:** Truck circulation for equipment delivery and emergency vehicle access
- **Drainage:** Site grading directs runoff away from critical equipment areas to retention pond

### Excavation & Earthwork
- **Building Foundation:** Excavation for spread footings or drilled piers (TBD based on geotechnical report)
- **Retention Pond:** Excavation for stormwater detention pond (relocated to southeast perimeter)
- **Utility Trenches:** Trenching for electrical, water, sewer, natural gas, fiber
- **Equipment Pads:** Subgrade preparation for chiller pads, generator pads, BESS containers

---

## DIVISION 32 – EXTERIOR IMPROVEMENTS

### Stormwater Management - Updated Oct 2025

**Retention Pond Relocation:**
- **Original Location:** TBD (unspecified in original BOD)
- **Updated Location (Oct 2025):** Southeast perimeter of site
- **Configuration:** Horseshoe/moat shape wrapping around southeast and east sides of facility
- **Purpose:**
  - Frees space for data center building expansion
  - Creates aesthetic moat feature around facility
  - Maintains required stormwater detention capacity per Oklahoma DEQ
- **Design:** Sized per Oklahoma stormwater permit requirements

**Low-Impact Development (LID):**
- Permeable paving where feasible
- Bioswales and rain gardens for water quality treatment
- Native vegetation for erosion control

### Equipment Yards - Updated Oct 2025

**Chiller Yard:**
- **Location:** South side of building (opposite electrical equipment)
- **Configuration:** Horizontal arrangement (one long row or two rows)
- **Equipment:** ~16 chillers (1.5 MW each, phased deployment)
- **Clearances:** 8-10 ft minimum between chillers for airflow and maintenance
- **Surface:** Concrete pads with proper drainage
- **Future Expansion:** Leave blank positions for additional chillers as density increases

**Generator Yard:**
- **Location:** North side of building
- **Configuration:** Horizontal arrangement with 8-10 ft clearances
- **Equipment:** 5-6 generators (turbine + diesel recip mix)
- **Fuel Storage:** Belly tanks or above-ground storage tanks (48-hour minimum)
- **Surface:** Concrete pads with secondary containment (if above-ground fuel storage)
- **Sound Attenuation:** Outdoor sound enclosures (75 dBA @ 23 ft)

**Utility Transformer Pad:**
- **Location:** Adjacent to building at utility service entry point
- **Equipment:** 15-20 MVA transformer (sized for facility load)
- **Surface:** Concrete pad with oil containment basin per EPA SPCC requirements
- **Clearances:** Per NEC and utility company standards

**BESS Enclosure: NOT APPLICABLE**
- BESS-as-UPS rejected (Tier III violation)
- Economic BESS rejected (negative NPV -$5.3M to -$6.2M)
- See [[Why BESS Should Not Be UPS]] and [[Excess Solar Monetization Strategy]]

### Landscaping & Site Improvements

**Native Landscaping:**
- Use native Oklahoma species (drought-tolerant, low maintenance)
- Trees for shade and aesthetic enhancement
- Grass or native prairie mix in non-equipment areas

**Perimeter Fencing:**
- 8 ft chain-link fence with barbed wire (or ornamental steel per zoning)
- Automated sliding gate for vehicle access
- Pedestrian gate with card reader/keypad

**Paving & Surfaces:**
- **Truck Access Roads:** Concrete or asphalt paving for semi-trailer circulation
- **Equipment Yard Access:** Concrete or reinforced gravel for maintenance vehicles
- **Parking:** Employee and visitor parking (sized per operational headcount)

### Site Lighting
- **Perimeter Lighting:** LED fixtures on poles for security coverage (integrated with CCTV)
- **Equipment Yard Lighting:** LED fixtures for nighttime maintenance access
- **Building Entry Lighting:** LED wall-mounted fixtures for security and wayfinding
- **Controls:** Photocell and occupancy sensors, integrated with BMS

---

## SITE LAYOUT ORGANIZATION - UPDATED OCT 2025

**Electrical Equipment:**
- Outdoor containerized electrical enclosures (2-3 units)
- Generator yard
- Utility substation transformer pad

**Mechanical Equipment:**
- Chiller yard (~16 chillers in horizontal rows)
- Pumping equipment
- CDU access

**Layout:** Equipment yard organization and side placement TBD during detailed design

**Benefits:**
- Clear separation of electrical and mechanical disciplines
- Outdoor enclosures eliminate indoor space requirements
- Shorter cable/pipe runs within each discipline
- Simplified maintenance access
- Optimized site layout for 40,000 SF building footprint

### Future Expansion Zones
- **Site Plan:** Reserves space for future data hall expansion (2-3 additional buildings of similar size)
- **Electrical Infrastructure:** Pathways sized for ultimate buildout capacity
- Expanison zones will accomodate temporary compute vendors during early phases

---

## BUILDING ORIENTATION & PLACEMENT

### Building Orientation
- Data hall oriented to minimize solar heat gain on primary façade {TBC}
- Equipment delivery and loading dock positioned for optimal truck circulation

### Security Perimeter
- Outer perimeter fence encompasses data center facility
- Solar array may have separate perimeter depending on interconnection strategy (single vs dual POI)
- Clear stand-off zone around data hall for vehicle barriers and surveillance coverage

---

## COST IMPACTS

| System | Cost Estimate |
|---|---|
| Site surveys (ALTA, geotechnical, water delineation) | ~$50-150K |
| Site grading and earthwork | ~$500K-1M |
| Retention pond (horseshoe configuration) | ~$200-500K |
| Equipment yard surfacing (concrete pads) | ~$300-600K |
| Landscaping and native vegetation | ~$100-300K |
| Perimeter fencing and gates | ~$200-400K |
| Site lighting | ~$100-200K |
| Paving (access roads, parking) | ~$300-600K |
| **Total Site & Infrastructure** | ~$1.75-3.75M |

---

**Tags:** #saga-project #site-development #earthwork #stormwater #equipment-yards #csi-divisions-31-32

**Related Documents:**
- [[_BOD - Exec Summary and TOC]] - Main title page
- [[4BOD - Plumbing (CSI Div 22)]] - Stormwater management details
- [[5BOD - HVAC (CSI Div 23)]] - Chiller yard layout
- [[7BOD - Electrical (CSI Div 26)]] - Generator yard and BESS enclosure
- [[11BOD - Utilities DC Critical (CSI Div 33)]] - Utility transformer placement
- [[Architectural Meeting Changes by CSI Division]] - October 2025 updates
