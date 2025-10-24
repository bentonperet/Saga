**Created:** 2025-10-23 09:45

# CHANGES FROM ARCHITECTURAL MID-POINT MEETING
## Saga Pryor Data Center - Design Changes by CSI MasterFormat Division

**Meeting Date:** October 22, 2025
**Source:** [[Architectural Mid Point Meeting]]
**Related:** [[Basis of Design - Part 1 Core Systems]] | [[Basis of Design - Part 2 Supporting Systems]]

---

## OVERVIEW

This document organizes all design changes discussed in the October 22 architectural meeting, sorted by CSI MasterFormat divisions for integration into project specifications and updated basis of design documents.

**Major Change:** IT load capacity increased from 7.4 MW to 12 MW initial phase (with expansion capacity to 20-24 MW ultimate).

---

## DIVISION 00 - PROCUREMENT AND CONTRACTING REQUIREMENTS

### Capacity & Phasing
- **IT load increase**: From 7.4 MW to 12 MW initial phase
- **Ultimate capacity**: 20-24 MW with density upgrades
- **Phased deployment**:
  - Phase 1: 12 MW (four 3 MW blocks)
  - Phase 2: Additional 12 MW capacity (shell built day one, fit out later)

---

## DIVISION 01 - GENERAL REQUIREMENTS

No changes mentioned.

---

## FACILITY CONSTRUCTION SUBGROUP (DIVISIONS 02-14)

### DIVISION 03 - CONCRETE

#### Structural Slab
- **Confirm slab-on-grade**: Continue with structural slab approach (no raised floor)
- **Building footprint expansion**: Increase to accommodate 40,000 SF total white space
  - Phase 1: 20,000 SF fitted out
  - Phase 2: 20,000 SF shell space

#### Foundation
- No changes to foundation approach (pending geotechnical report)

---

### DIVISION 05 - METALS

#### Structural System Evaluation
- **Two-story vs. single-story analysis required**:
  - FM-150 rated roof requires substantial structural steel regardless
  - Two-story may be cost-effective given required structure for tornado-hardened roof
  - Single-story requires larger footprint but simpler MEP distribution
  - **Decision pending**: Cost comparison analysis needed

#### Considerations
- Smaller footprint with two-story preserves more solar array space
- Single-story preferred for shorter electrical/mechanical runs (copper cost savings)
- FM-150 roof structural requirements may offset traditional two-story cost premium

---

### DIVISION 07 - THERMAL AND MOISTURE PROTECTION

#### Roof System
- **FM-150 roof rating**: Confirmed EF-2 tornado resistance requirement
- **Missile impact protection**: Maintain steel roof deck with impact-resistant insulation
- Higher structural requirements acknowledged; factored into two-story evaluation

---

### DIVISIONS 08-14 - OPENINGS, FINISHES, SPECIALTIES, EQUIPMENT, FURNISHINGS, SPECIAL CONSTRUCTION, CONVEYING

No specific changes mentioned.

---

## FACILITY SERVICES SUBGROUP (DIVISIONS 21-28)

### DIVISION 21 - FIRE SUPPRESSION

No changes beyond existing NFPA 855 requirements for BESS enclosure.

---

### DIVISION 22 - PLUMBING

#### Site Stormwater Management
- **Retention pond relocation**: Move from current location to southeast perimeter
- **Configuration**: Horseshoe/moat shape wrapping around southeast and east sides of facility
- **Purpose**:
  - Frees up space for data center building expansion
  - Creates aesthetic moat feature around facility
  - Maintains required stormwater detention capacity

---

### DIVISION 23 - HVAC (HEATING, VENTILATING, AND AIR CONDITIONING)

#### Data Hall Cooling - Major Changes

##### Remove Fan Walls
- **Eliminate**: All fan wall equipment from data hall
- **Rationale**: Not needed with rack-based cooling approach

##### Rear-Door Heat Exchangers (RDHx)
- **Confirm RDHx approach**: Rack-based cooling for air-cooled network equipment
- **Benefits**: Per-customer control, flexible billing, mixed density support

##### Chilled Water Plant Expansion
- **Target chiller count**: ~16 total chillers for 20 MW ultimate capacity
- **Chiller sizing**: 1.5 MW per chiller (air-cooled with integrated free cooling)
- **Configuration**: 3 chillers per 3 MW block (provides N+1 redundancy per block)
- **Layout**: Horizontal arrangement in equipment yard (one long row or two rows)
- **Clearance**: 8-10 ft minimum between chillers for airflow and maintenance access

##### Chiller Yard Arrangement
- **Location**: Along bottom/south side of building (opposite electrical equipment)
- **Future expansion spaces**: Leave blank positions for additional chillers when density increases
- **Approach**: Deploy chillers as 3 MW blocks are commissioned

##### Adiabatic Fluid Cooler Elimination
- **Confirmed**: Elimination of 5× adiabatic fluid coolers (already removed in BoD)
- **Result**: Zero water consumption for cooling

#### Comfort Cooling & Air Quality

##### Air Handling Strategy
- **Equipment**: Rooftop air handling units (AHUs) for data hall comfort
- **Functions**:
  - Humidity control
  - Building over-pressurization (prevent dust ingress)
  - Air quality (Merv filtration)
  - Minimal sensible cooling (rack-based cooling handles IT heat)
- **Redundancy**: N+1 AHU configuration
- **Phasing**:
  - Phase 1: Half-building comfort cooling capacity
  - Phase 2: Add remaining AHU capacity when second half fitted out

---

### DIVISION 26 - ELECTRICAL

#### UPS Equipment Removal - Major Change

##### Eliminate Traditional UPS Systems
- **Remove**: All 8× 1,500 kW Galaxy VX UPS units (IT load)
- **Remove**: All 32× lithium-ion battery cabinets (IT - 17 modules each)
- **Remove**: 2× 200 kW Galaxy VL UPS units (mechanical load)
- **Remove**: 2× lithium-ion battery cabinets (mechanical - 16 modules each)
- **Rationale**: BESS-as-UPS architecture confirmed (Decision #5)

##### Maintain Small Battery Backup
- **Keep**: Small battery cabinet for switchgear control continuity during power transitions
- **Purpose**: Maintain switchboard control power if brief interruption occurs

#### Switchboard Equipment - Keep

##### Electrical Distribution
- **Retain**: All IT switchboards (SWBD) - 4× units, 480V distribution
- **Retain**: All mechanical switchboards (MECH SWBD) - 2× units
- **Function**: Primary distribution point from transformers to data hall and mechanical loads

#### Electrical Room Reconfiguration

##### Orientation Change
- **Change**: Flip electrical rooms from horizontal to vertical orientation
- **Enables**: Better space utilization with UPS/battery removal
- **Result**: Significantly smaller electrical room footprint required

##### Outdoor Electrical Enclosures
- **Approach**: Use containerized outdoor electrical equipment (similar to Switch Las Vegas)
- **Enclosure type**: Weather-rated containers with all electrical gear inside
- **Estimated size**: 12 ft × 55 ft per enclosure (based on Switch reference)
- **Quantity**: 2-3 outdoor electrical enclosures total
- **Location**: Along north or top side of building (near BESS for short cable runs)

#### Generator System Revisions

##### Generator Fuel & Type Strategy
- **Primary backup power**: Natural gas turbine(s)
  - High efficiency for backup power generation
  - ~4.3 MW capacity per turbine
  - Potential for mobile/temporary turbine if grid power delayed
- **Secondary backup power**: Diesel reciprocating generators (N+1 configuration)
  - Backup to the backup (fuel diversity)
  - Ensures power if natural gas service fails or turbine doesn't start
  - Standard diesel generators on belly tanks
- **Reasoning**: Two types of reserve power required for redundancy
  - Turbine: Efficiency and natural gas fuel
  - Diesel recip: Fuel diversity and proven reliability

##### Generator Count & Layout
- **IT load generators**: 4-5 generators (exact count TBD based on turbine/recip mix)
- **Mechanical load generators**: Reduce from 2 to 1 generator for office/non-critical areas
- **Total generators**: ~5-6 units
- **Layout**: Horizontal arrangement with 8-10 ft minimum clearance between units
- **Location**: Generator yard on north/top side of building

##### Generator Yard Sizing
- **Equipment**: Generators on belly fuel tanks in sound-attenuated enclosures
- **Clearances**: 8-10 ft between units minimum for airflow and maintenance

#### BESS System Refinements

##### BESS Sizing Confirmation
- **Capacity**: 16 MW / 48 MWh with phased inverter deployment
- **Phase 1 inverters**: 3× 4MW inverters
  - Total capacity: 12 MW
  - Available N+1: 8 MW (supports ~75% occupancy)
- **Phase 2 inverters**: Add 4th 4MW inverter
  - Total capacity: 16 MW
  - Available N+1: 12 MW (supports 10 MW facility load + 20% margin)

##### BESS Container Count Correction
- **Corrected estimate**: ~12 containers (20 ft × 8 ft footprint each)
- **Previous overestimate**: ~40+ containers (based on incorrect Saga layout reference)
- **Clearances**: Include 6 ft on each side for maintenance access
- **Result**: BESS footprint significantly smaller than initially drawn

##### BESS Location & Orientation
- **Rotation**: Rotate BESS enclosure 90° from current orientation
- **Location**: Along north boundary of data center site, near utility substation
- **Layout**: Horizontal arrangement of containers (trees on opposite side)
- **Rationale**: Minimize cable runs between BESS, substation, and electrical enclosures

#### Electrical/Mechanical Separation

##### Equipment Yard Organization (Following Switch Las Vegas Model)
- **Electrical equipment side**: One side of building (likely north/top)
  - Outdoor electrical enclosures (containerized switchgear)
  - Generator yard
  - BESS enclosure (separate area near substation)
- **Mechanical equipment side**: Opposite side of building (likely south/bottom)
  - Chiller yard (16 chillers in horizontal rows)
  - Pumping equipment
  - CDU access
- **Benefits**:
  - Clear separation of disciplines
  - Shorter cable/pipe runs within each discipline
  - Simplified maintenance access

---

### DIVISION 27 - COMMUNICATIONS

#### Meet-Me Rooms

##### Quantity & Sizing
- **Confirm two meet-me rooms**: North and south entries for diverse fiber paths
- **Size**: 250-300 SF each (ensure both are equal size)
- **Purpose**: Diverse carrier entry points, GCP interconnection

##### Access & Security
- **Security level**: Highest security access required
- **Door location**: Interior doors acceptable (not required to open to exterior)
- **Rack count**: TBD based on carrier requirements for 10+ MW facility

---

### DIVISION 28 - ELECTRONIC SAFETY AND SECURITY

No specific changes beyond meet-me room security requirements already noted.

---

## SITE AND INFRASTRUCTURE SUBGROUP (DIVISIONS 31-35)

### DIVISION 31 - EARTHWORK

#### Site Grading & Development
- **Pond relocation earthwork**: Excavation and grading for new horseshoe pond configuration
- **Building footprint expansion**: Additional site preparation for larger data center building
- **Equipment yard expansion**: Grading for expanded chiller and generator yards

---

### DIVISION 32 - EXTERIOR IMPROVEMENTS

#### Landscaping & Paving
- **Pond aesthetic treatment**: Potential for enhanced landscaping around moat-like retention pond
- **Equipment yard surfaces**: Paving/gravel for expanded mechanical and electrical yards

#### Equipment Yard Requirements
- **Chiller yard expansion**: Accommodate ~16 chillers in horizontal layout
- **Generator yard**: Layout for 5-6 generators with proper clearances
- **BESS yard optimization**: Reduce footprint from 40,000+ SF to ~20,000-25,000 SF

---

### DIVISION 33 - UTILITIES

#### Utility Service Sizing
- **Substation capacity confirmation**: Verify utility substation adequate for expanded load
  - Original: ~10 MW facility load + 12 MW BESS charging
  - Expanded: Up to ~15 MW facility load + 12 MW BESS charging
  - Transformer sizing: 15-20 MVA minimum (may need upward revision)

#### Natural Gas Service
- **Confirm availability**: Natural gas service capacity for turbine generators
- **Sizing**: Adequate capacity for primary backup power turbine(s)
- **Backup consideration**: Diesel generators provide fuel diversity if gas service fails

---

### DIVISIONS 34-35 - TRANSPORTATION, WATERWAY AND MARINE

Not applicable to this project.

---

## PROCESS EQUIPMENT SUBGROUP (DIVISIONS 40-48)

### DIVISION 48 - ELECTRICAL POWER GENERATION

#### Generator Fuel Strategy - Major Decision

##### Dual Fuel Approach
- **Primary backup**: Natural gas turbine(s)
  - High efficiency (lower fuel consumption per kWh)
  - Connected to pipeline natural gas
  - ~4.3 MW capacity per unit
  - Faster response for routine backup needs
- **Secondary backup**: Diesel reciprocating generators
  - Fuel diversity (independent of natural gas infrastructure)
  - N+1 redundancy within diesel genset group
  - Standard reliability and proven data center technology
  - Belly tanks or above-ground storage tanks (48-hour minimum fuel storage)

##### Reasoning for Dual Approach
- **Two types of reserve power required**: Cannot rely on single fuel source
- **Turbine benefits**: Lower emissions, unlimited runtime (pipeline fuel), higher efficiency
- **Diesel benefits**: Fuel independence, customer comfort with proven technology
- **Risk mitigation**: If natural gas service fails, diesel provides backup
- **Customer acceptance**: Easier to market with diesel backup option available

##### Bridge Power Consideration
- **Temporary turbine**: May deploy temporary mobile turbine if grid power not ready at facility opening
- **Removed when grid connected**: Temporary unit returns when utility service commissioned
- **Fallback**: Diesel generators provide permanent backup regardless of temporary turbine

---

## OUT OF SCOPE DIVISIONS FOR THIS PHASE

The following CSI MasterFormat divisions are not applicable to this data center project scope:

**Division 04** - Masonry (PEMB construction, no masonry)
**Division 06** - Wood, Plastics, and Composites (minimal scope)
**Division 10** - Specialties (minimal scope)
**Division 11** - Equipment (covered under Division 48 for power generation)
**Division 12** - Furnishings (office furniture not part of core facility scope)
**Division 13** - Special Construction (N/A)
**Division 14** - Conveying Equipment (no elevators, escalators, or lifts)
**Division 15-19** - Reserved for Future Expansion
**Division 20, 24, 29** - Reserved for Future Expansion
**Division 25** - Integrated Automation (covered under BMS/DCIM in original BoD, no changes)
**Division 30, 36-39** - Reserved for Future Expansion
**Division 34** - Transportation (N/A)
**Division 35** - Waterway and Marine Construction (N/A)
**Division 40-47, 49-50** - Other Process Equipment Divisions (N/A)

---

## KEY DESIGN PHILOSOPHY CHANGES

### Target White Space
- **Total white space goal**: 40,000 SF
  - Phase 1: 20,000 SF fitted out and commissioned
  - Phase 2: 20,000 SF shell space (empty, for future fit-out)
- **Power density progression**:
  - Initial: ~500 W/SF (10 kW/cabinet, air-cooled with RDHx)
  - Mid-term: ~1,000 W/SF (20 kW/cabinet, enhanced RDHx)
  - Ultimate: ~2,000 W/SF (40 kW/cabinet, liquid-to-chip cooling)

### Design Reference Change
- **Primary reference**: Switch Las Vegas layout preferred over RD109
- **Reason**: Better electrical/mechanical separation, outdoor equipment approach
- **Application**: Similar long rectangular building with equipment on opposite sides

### Phasing Strategy
- **Shell + core approach**:
  - Build complete building envelope day one (40,000 SF white space shell)
  - Fit out Phase 1 (20,000 SF white space + all support spaces)
  - Leave Phase 2 white space empty (shell only, no MEP fit-out)
  - Office, loading dock, NOC, restrooms fitted out in Phase 1
  - Equipment yards: Only Phase 1 equipment installed initially

### Modular 3 MW Building Blocks
- **Design increment**: 3 MW blocks for customer flexibility
- **Chiller association**: 3 chillers per 3 MW block (N+1 within block)
- **Electrical distribution**: Organized around 3 MW increments
- **Customer deployment**: Can lease/deploy in 3 MW increments

### Reference Building Dimensions
- **Switch Las Vegas white space**: ~88 ft × 458 ft = ~40,000 SF
- **Scale factor**: Switch is 48 MW; Saga Pryor initial is 12 MW (~25% of Switch)
- **Approach**: Similar layout at smaller scale for Phase 1, with expansion room built-in

---

## DECISIONS PENDING / ACTION ITEMS

### Immediate Actions Required

1. **Cost analysis**: Single-story vs. two-story building with FM-150 roof
   - Include structural steel costs for FM-150 in both scenarios
   - Compare copper/cable costs (shorter runs in single-story)
   - Evaluate footprint constraints and solar array impact

2. **BESS container sizing confirmation**:
   - Verify dimensions with Saga's installed BESS units
   - Confirm 12 containers adequate for 48 MWh
   - Update site layout with accurate BESS footprint

3. **Natural gas service confirmation**:
   - Confirm availability and capacity with Oklahoma Natural Gas
   - Size service for turbine generator(s)
   - Determine interconnection costs and timeline

4. **Utility substation sizing review**:
   - Confirm 15-20 MVA transformer adequate for expanded load
   - May need upward revision to 20-25 MVA
   - Coordinate with OG&E interconnection study

5. **White space layout development**:
   - Develop detailed layout showing 40,000 SF total
   - Phase 1: 20,000 SF with MEP fit-out
   - Phase 2: 20,000 SF shell space (gray out for renderings)

6. **Generator vendor coordination**:
   - Confirm turbine sizing and specifications (Dragon vendor)
   - Confirm diesel generator sizes for backup
   - Determine generator yard footprint requirements

### Design Development Decisions

**Decision required by:** Early November 2025

- **Building configuration**: Single-story vs. two-story (pending cost analysis)
- **Generator final strategy**: Turbine + diesel recip count and sizing
- **Electrical room final count**: 2 or 3 outdoor enclosures
- **Pond final configuration**: Exact horseshoe dimensions and depth

---

## SUMMARY OF MAJOR CHANGES

### Capacity Changes
- ✅ IT load: 7.4 MW → 12 MW initial (20-24 MW ultimate)
- ✅ White space: 25,000 SF → 40,000 SF total (20K + 20K phased)
- ✅ Chillers: 3 units → 16 units (phased deployment)

### Equipment Eliminations
- ❌ Remove all UPS units (8× IT UPS + 2× mechanical UPS)
- ❌ Remove all UPS battery cabinets (32× IT + 2× mechanical)
- ❌ Remove fan walls from data hall
- ❌ Confirm elimination of adiabatic fluid coolers

### Equipment Additions/Changes
- ✅ Natural gas turbine(s) for primary backup power
- ✅ Diesel generators maintained for fuel diversity backup
- ✅ Outdoor containerized electrical enclosures (2-3 units)
- ✅ Expanded chiller yard (~16 chillers vs. 3)
- ✅ Rooftop AHUs for comfort cooling

### Layout Changes
- ✅ Electrical equipment on one building side, mechanical on opposite
- ✅ Retention pond relocated to southeast perimeter (horseshoe/moat)
- ✅ BESS rotated 90° and positioned along north boundary
- ✅ Generator yard horizontal layout
- ✅ Electrical room orientation flipped vertical

### Design Approach Changes
- ✅ Switch Las Vegas layout reference preferred over RD109
- ✅ Shell + core phasing (build envelope day one, fit out in phases)
- ✅ 3 MW modular blocks for customer flexibility
- ✅ Two-story evaluation (may be cost-effective with FM-150 roof)

---

**Next Steps:**
1. Julia to update architectural drawings with revised layout
2. Cost analysis for single vs. two-story building
3. BESS container sizing confirmation
4. Natural gas service coordination
5. Updated BoD documents to reflect all changes

---

**Tags:** #saga-project #architectural-meeting #design-changes #csi-masterformat #basis-of-design

**Related Documents:**
- [[Architectural Mid Point Meeting]] - Source meeting transcript
- [[Basis of Design - Part 1 Core Systems]] - Original design basis
- [[Basis of Design - Part 2 Supporting Systems]] - Original design basis
- [[BESS as UPS Replacement - Feasibility Analysis V2]] - BESS-as-UPS decision analysis
- [[Feasibility Memo V3]] - Strategic decisions and validation studies
