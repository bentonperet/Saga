**Created:** 2025-10-21 17:35

# Site Layout Requirements - Architect Handoff
## Saga Energy Pryor Data Center

**Purpose:** Concise space planning requirements for site layout design.

**Tags:** #saga-project #site-planning #architect-deliverable

---

## 1. DATA HALL & BUILDING SIZING

### Scenario Comparison

| Metric               | 10MW DC   | 12MW DC ⭐     | 20MW Shell    |
| -------------------- | --------- | ------------- | ------------- |
| **IT Load**          | 10,000 kW | 12,000 kW     | 20,000 kW     |
| **Facility Load**    | 15 MW     | 16.8 MW       | 28 MW         |
| **Rack Count**       | 130 racks | 156 racks     | 260 racks     |
| **Data Hall**        | 39,000 SF | 40,000 SF     | 65,000 SF     |
| **Electrical Rooms** | 10,000 SF | 13,000 SF     | 13,000 SF     |
| **Office/NOC**       | 5,000 SF  | 5,000 SF      | 5,000 SF      |
| **TOTAL BUILDING**   | 54,000 SF | **64,800 SF** | **83,000 SF** |


20k x 20k sq ft

**Recommendation:** Build 20MW shell (83,000 SF), fit out 12MW initially (64,800 SF active).

A good ballpark for today's DC. 17KW per cabinet.
We'd want to goto 20,000 square foot (maybe 2 10k sq/ft sections)

### Building Footprint

| Option | Dimensions | SF | Notes |
|--------|------------|-----|-------|
| **Compact** | 260' × 250' | 65,000 SF | Tight fit, minimal future expansion |
| **Recommended** | 275' × 300' | 82,500 SF | 20MW shell, 12MW fit-out |
| **Expansion-ready** | 300' × 300' | 90,000 SF | Room for future 25MW+ |

**Building Height:** 16-18 ft floor-to-floor (data hall), 14 ft (electrical rooms), single-story.

### Space Breakdown (12MW with 20MW Shell)

| Component        | Active (12MW) | Shell Only       | Total (20MW)  |
| ---------------- | ------------- | ---------------- | ------------- |
| Data hall        | 46,800 SF     | +18,200 SF       | 65,000 SF     |
| Electrical rooms | 13,000 SF     | Conduit rough-in | 13,000 SF     |
| Office/NOC/MMR   | 5,000 SF      | -                | 5,000 SF      |
| **TOTAL**        | **64,800 SF** | **+18,200 SF**   | **83,000 SF** |

---

## 2. OUTDOOR INFRASTRUCTURE

### Generator Yard

| Item | Spec | Footprint | Clearances |
|------|------|-----------|------------|
| **Units (Phase 1)** | 5×4.3MW natural gas | 20' × 10' each | 10 ft between units |
| **Units (20MW future)** | +2 units (7 total) | 20' × 10' each | Space reserved |
| **Exhaust stacks** | 30 ft tall | 3 ft diameter | 25 ft from buildings |
| **Service area** | Maintenance access | - | 25 ft clear on 2 sides |
| **Total yard** | - | **8,400 SF** | **70' × 120'** |
| **Building setback** | NFPA 37 | - | **50-100 ft** (noise/exhaust) |

**Note:** Yard sized for 7 generators final (5 Phase 1, +2 for 20MW expansion).

### BESS Yard

| Item | Spec | Footprint | Clearances |
|------|------|-----------|------------|
| **Battery containers** | 4×20' ISO containers (12-15 MWh) | 20' × 8' each | 15 ft between units |
| **Inverter containers** | 6×20' ISO containers (24MW AC) | 20' × 8' each | 10 ft from batteries |
| **Cooling equipment** | Outdoor chillers | 600 SF | Adjacent to containers |
| **Fire suppression** | Integrated in containers | - | - |
| **Total yard** | - | **5,400 SF** | **75' × 72'** |
| **Building setback** | NFPA 855 | - | **50-100 ft OR 4-hr fire wall** |

**Power Rating:** 6×4MW inverters (N+1 redundancy) = 24MW total, 20MW available. Sized to carry full 16.8MW facility load during nighttime grid outage.

### Utility Interconnection

| Item                    | Spec             | Footprint    | Location                |
| ----------------------- | ---------------- | ------------ | ----------------------- |
| **Utility transformer** | 30-35 MVA, 138kV | 20' × 30'    | Property line/easement  |
| **Switchgear**          | 138kV metering   | 15' × 20'    | Adjacent to transformer |
| **Oil containment**     | Concrete pad     | 600 SF       | If oil-filled xfmr      |
| **Total yard**          | -                | **1,500 SF** | **40' × 40'**           |

**Note:** Transformer sized for 20MW future load (28MW facility). 30-35 MVA supports both Phase 1 (16.8MW) and expansion (28MW).

### Support Infrastructure

| Item                      | Size                             | Notes                       |                                      |
| ------------------------- | -------------------------------- | --------------------------- | ------------------------------------ |
| **Fire water tank**       | 500,000 gal (30' dia × 40' tall) | 2,800 SF footprint          |                                      |
| **Fire pump house**       | 400 SF                           | Adjacent to tank            |                                      |
| **Parking**               | 30 spaces                        | 15,000 SF (9' × 18' spaces) |                                      |
| **Stormwater detention**  | 1-2 acres                        | Per local code              |                                      |
| **Potable water service** | 2-4" domestic line               | Tie to Office/NOC           | Coordinate with architect            |
| **Sanitary sewer**        | 6-8" sewer connection            | Tie to Office/NOC           | Coordinate with architect            |
| **Construction laydown**  | 2-3 acres (temporary)            | Material staging, trailers  | Can become parking post-construction |

---

## 3. TOTAL SITE REQUIREMENTS

### Site Area Summary

| Component                   | Area            | Notes                          |
| --------------------------- | --------------- | ------------------------------ |
| Data center building        | 1.9 acres       | 83,000 SF footprint            |
| Generator yard              | 0.19 acres      | 8,400 SF (7 units final)       |
| BESS yard                   | 0.12 acres      | 5,400 SF (6 inverters)         |
| Utility interconnection     | 0.03 acres      | Property line                  |
| Fire water tank/pump        | 0.10 acres      | 50 ft from building            |
| Parking                     | 0.34 acres      | 30 spaces                      |
| Construction laydown (temp) | 2-3 acres       | During construction only       |
| Access roads                | 1.5 acres       | Fire truck access (20 ft wide) |
| Stormwater detention        | 1-2 acres       | Drainage                       |
| Setbacks/buffer             | 2-3 acres       | Property line clearances       |
| **MINIMUM SITE**            | **10-12 acres** | Compact layout                 |
| **RECOMMENDED SITE**        | **15-20 acres** | Room for expansion + laydown   |

---

## 4. CRITICAL SETBACKS & CLEARANCES

### Fire Safety (NFPA)

| From | To | Distance | Code | Notes |
|------|-----|----------|------|-------|
| BESS containers | Building | 50 ft OR 4-hr barrier | NFPA 855 | 50 ft cheaper than fire wall |
| BESS containers | Each other | 10-15 ft | NFPA 855 | Fire containment |
| Generators | Building | 50-100 ft | NFPA 37 | Exhaust/noise |
| Generators | Property line | 25 ft | Local code | Noise ordinance |
| Fire water tank | Building | 50 ft | NFPA 22 | Fire dept access |

### Site Access

| Requirement | Dimension | Code | Notes |
|-------------|-----------|------|-------|
| Fire truck access road | 20 ft wide, 26 ft clear | IFC | Around entire building |
| Turning radius | 50 ft | IFC | Cul-de-sacs, turnarounds |
| Fire lane | 20 ft min width | IFC | "No Parking - Fire Lane" |
| Building access points | 150 ft max spacing | IFC | Doors for firefighters |

---

## 6. ARCHITECT QUESTIONS & ACTION ITEMS

### Questions for Architect

**Site Constraints:**
- [ ] Available site area? (Need 15-20 acres)
- [ ] Easements, wetlands, or restricted areas?
- [ ] Existing utilities on site?

**Utility Access:**
- [ ] Where is 138kV transmission line? (Distance to site? Need 30-35 MVA service)
- [ ] Where is natural gas pipeline? (Industrial service available?)
- [ ] Where is fiber entry point? (Telecom access?)
- [ ] Potable water service location and capacity?
- [ ] Sanitary sewer connection point?

**Zoning/Code:**
- [ ] Setbacks from property lines?
- [ ] Height restrictions? (Exhaust stacks 30 ft, building 18 ft)
- [ ] Noise ordinance limits? (Generators)

**Environmental:**
- [ ] Flood zones on site?
- [ ] Stormwater detention requirements? (Acreage?)
- [ ] Wetlands or protected areas?

**Access:**
- [ ] Fire department response route?
- [ ] Heavy equipment delivery path? (BESS containers, transformers need crane access)
- [ ] Separate service entrance for generators/BESS vs customer traffic?
- [ ] Construction laydown area location? (2-3 acres for staging, can become parking later)

### Deliverables Requested

1. **Site plan** showing:
   - Building footprint (275' × 300')
   - Generator yard (70' × 120'), BESS yard (75' × 72'), utility gear with setbacks
   - Parking, construction laydown, fire access roads
   - Potable water/sewer connections
   - Setbacks from property lines

2. **Phasing plan**:
   - Phase 1: 12MW fit-out (what gets built Month 0-12)
   - Shell allowance for 20MW future expansion

3. **Utility routing** (conceptual):
   - Grid interconnection path
   - Natural gas pipeline tie-in
   - Fiber entry point

---

## 7. KEY DESIGN ASSUMPTIONS

| Parameter | Value | Notes |
|-----------|-------|-------|
| IT load (Phase 1) | 12 MW | 156 racks @ 77 kW avg |
| Facility load (Phase 1) | 16.8 MW @ 1.4 PUE | Summer peak |
| Future capacity (shell) | 20 MW IT / 28 MW facility | 260 racks, same footprint |
| Generators (Phase 1) | 5×4.3MW natural gas (N+1) | Yard sized for 7 units final |
| BESS | 12-15 MWh / 24MW AC (6×4MW inv) | UPS replacement |
| Utility transformer | 30-35 MVA | Sized for 20MW future (28MW load) |
| Wind rating | 250 mph (EF-5 tornado) | Oklahoma FEMA 361 |
| Seismic | Zone 2 | Oklahoma code |
| Cooling design temp | 100°F | Oklahoma summer |

---

**Document Status:** Ready for architect meeting
**Next Review:** Post-meeting (update with site constraints)

**Related Documents:**
- [[Optimal DC Sizing Analysis - Turbine-Aligned Deployment]] - Technical rationale
- [[Part 1 - Solar-First Startup Strategy - BAD]] - System architecture

**Tags:** #saga-project #site-planning #architect-handoff #12mw-dc