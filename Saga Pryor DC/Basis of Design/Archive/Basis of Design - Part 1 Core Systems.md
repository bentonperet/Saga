**Created:** 2025-10-17 18:30

# BASIS OF DESIGN - PART 1: CORE SYSTEMS
## Saga Energy – Pryor Data Center
### Mayes County, Oklahoma

**Project Reference:** Schneider Electric EcoStruxure™ Reference Design 109 (RD109)
**Document Status:** DRAFT - Complete (Part 1 of 2)
**Prepared by:** PGCIS Program Management Team
**Date:** October 17, 2025
**Purpose:** Technical design foundation for investor package and downstream detailed design

**Related Documents:**
- [[Feasibility Memo V3]] - Strategic decisions and validation studies
- [[RD109_0.0_Table-Of-Contents_R10]] - Schneider Electric baseline reference design
- [[BESS as UPS Replacement - Feasibility Analysis V2]] - Power system optimization analysis
- [[_Project Plan]] - Project schedule and milestones
- [[Basis of Design - Part 2 Supporting Systems]] - Sections 7-13 (Fire, Security, Telecom, Controls, Operations, Sustainability, Deviations)

---

## TABLE OF CONTENTS - PART 1

1. [PROJECT OVERVIEW & REQUIREMENTS](#1-project-overview--requirements)
2. [SITE & BUILDING ARCHITECTURE](#2-site--building-architecture)
3. [CRITICAL ELECTRICAL SYSTEMS](#3-critical-electrical-systems)
4. [RENEWABLE ENERGY & MICROGRID](#4-renewable-energy--microgrid)
5. [MECHANICAL & COOLING SYSTEMS](#5-mechanical--cooling-systems)
6. [PLUMBING & UTILITIES](#6-plumbing--utilities)

**→ For Sections 7-13, see [[Basis of Design - Part 2 Supporting Systems]]**

---

# 1. PROJECT OVERVIEW & REQUIREMENTS

## 1.1 Project Summary

The Saga Energy Pryor Data Center is a purpose-built, colocation facility designed to support AI and enterprise compute workloads. The facility combines proven data center design practices with innovative renewable energy integration to deliver a sustainable, resilient, and economically optimized infrastructure solution.

**Key Project Parameters:**
- **IT Load Capacity:** 7.4 MW (48 AI racks @ 132 kW + 48 network racks @ 22 kW)
- **Total Facility Load:** ~10 MW (IT + mechanical + support systems)
- **Data Hall Size:** 25,000 SF white space
- **Location:** 121-acre site, Mayes County, Oklahoma (approximately 4 miles from Google Pryor campus)
- **Design Life:** 25+ years with modular expansion capability
- **Target PUE:** 1.2 – 1.3 (annual average)
- **Availability Target:** Tier III-equivalent (N+1 redundancy, concurrent maintainability)

**Strategic Differentiators:**
1. Integrated 12 MW solar array + Battery Energy Storage System (BESS) owned by Saga Energy
2. Proximity to Google campus enabling low-latency GCP interconnection opportunity
3. Power pass-through pricing model removing commodity risk from operator
4. Validated design foundation based on Schneider Electric RD109 reference architecture

## 1.2 Design Reference Baseline
<!-- Don't put a carriage return after an H2 headline - adjust this on this doc and edit the claude.md file -->
This Basis of Design (BoD) is anchored to **Schneider Electric EcoStruxure™ Reference Design 109 (RD109), Revision 10**, a validated and proven architecture for high-density data centers. The RD109 provides detailed specifications for:
- Electrical systems (power generation, distribution, UPS, rack power)
- Mechanical systems (cooling plant, distribution, in-room cooling)
- IT space layout and equipment configuration

**RD109 Baseline Configuration (Dallas, TX):**
- 7.4 MW IT load capacity
- Tier III-equivalent electrical redundancy (N+1 generators, UPS, transformers)
- Hybrid cooling: air-cooled chillers with free cooling + adiabatic fluid coolers
- Liquid cooling infrastructure for high-density AI racks (CDUs)
- Hot aisle containment with BMS/DCIM integration

**Purpose of Using RD109:**
The RD109 serves as a validated starting point that accelerates the design process and provides proven equipment selections for key systems. While RD109 offers a solid foundation, PGCIS is designing a best-in-class data center optimized for Oklahoma's climate, Saga Energy's renewable integration strategy, and modern high-density workload requirements. The final design incorporates significant enhancements and site-specific optimizations beyond the baseline reference design.

**Key Deviations from RD109:**
This BoD documents several strategic modifications to the RD109 baseline, including:
1. **BESS-as-UPS architecture** - Eliminates traditional UPS systems by using grid-forming battery inverters (pending Decision #5)
2. **Raised floor elimination** - Overhead cable distribution on structural slab (pending geotechnical validation)
3. **Cooling system optimization** - Hybrid air-cooled chillers with integrated free cooling, elimination of adiabatic assist
4. **Generator fuel strategy** - Diesel, natural gas, or dual-fuel (pending Decision #2)
5. **Climate-specific sizing** - Oklahoma psychrometric conditions vs. Dallas baseline
6. **Additional support spaces** - Staging/burn-in area, enhanced staff amenities, tornado hardening

All deviations are documented in Section 13 with technical rationale and cost/schedule impacts.

## 1.3 Key Performance Targets
The facility is designed to meet or exceed the following performance criteria:

### Availability & Redundancy
- **Uptime Tier:** Tier III-equivalent (99.982% availability, 1.6 hours/year planned downtime)
- **Electrical Redundancy:** N+1 configuration for all critical power components (generators, UPS/BESS, transformers, switchgear)
- **Mechanical Redundancy:** N+1 configuration for all critical cooling components (chillers, pumps, CDUs)
- **Concurrent Maintainability:** Any single component can be removed for maintenance without impacting IT load
- **Fault Tolerance:** No single point of failure in critical power or cooling distribution paths

### Energy Efficiency
- **Target PUE:** 1.2 – 1.3 (annual average)
  - 1.15 – 1.25 during free cooling months (October – April)
  - 1.25 – 1.35 during mechanical cooling months (May – September)
- **Renewable Energy Contribution:** Target 60-80% of annual energy consumption from on-site solar *(preliminary estimate pending Camelot net load analysis)*
- **Generator Runtime Reduction:** Target 87% reduction in generator operating hours vs. traditional UPS-only architecture *(preliminary estimate based on BESS backup duration analysis)*

### Power Density & Capacity
- **AI Rack Density:** Up to 132 kW/rack for liquid-cooled AI workloads
- **Network Rack Density:** Up to 22 kW/rack for air-cooled network equipment
- **Rack Count:** 96 total racks (48 AI + 48 network in baseline configuration)
- **Power Distribution:** 2N redundant feeds to each rack via overhead busway and RPPs
- **Voltage:** 480V 3-phase distribution; 208V 3-phase at rack level

### Environmental & Operating Conditions
- **IT Space Temperature:** 18-27°C (64-80°F) per ASHRAE A1 envelope
- **IT Space Humidity:** 5.5°C – 60% RH dew point, 60% RH maximum
- **Electrical Room Temperature:** 25°C ± 2°C (77°F ± 4°F)
- **Design Ambient Conditions (Pryor, OK):**
  - Summer: 95°F dry bulb / 78°F wet bulb (99.6% ASHRAE design day)
  - Winter: 10°F dry bulb (99.6% ASHRAE design day)
  - Elevation: ~750 ft above sea level

## 1.4 Regulatory & Code Compliance Framework
**Note:** This section is a placeholder. Detailed code compliance and permitting requirements will be provided by the engineering consultant and permitting specialist. All codes, standards, and regulatory requirements listed in this document must be verified and updated during detailed design. See Appendix A for preliminary code compliance matrix.

---

# 2. SITE & BUILDING ARCHITECTURE

## 2.1 Site Layout & Orientation

The 121-acre site in Mayes County, Oklahoma provides exceptional flexibility for data center development, renewable energy integration, and future expansion.

**Site Characteristics:**
- **Location:** Approximately 4 miles by road from Google Pryor campus
- **Topography:** Relatively flat with minimal grading required (pending ALTA survey confirmation)
- **Access:** Frontage road with adequate ingress/egress for truck traffic
- **Utilities:** 138 kV transmission line proximity confirmed; water/sewer availability under study
- **Fiber:** Fiber route analysis underway via Camelot (Task 3, expected delivery early November)

**Building Orientation:**
- Data hall oriented to minimize solar heat gain on primary façade
- Generator and chiller yards positioned on north side to reduce noise impact on staff areas
- Equipment delivery and loading dock on [TBD - confirm preferred side] for truck circulation
- Solar array positioned to maximize southern exposure and minimize shading (12 MW footprint ~80-100 acres)

**Security Perimeter:**
- Outer perimeter fence encompasses data center facility and BESS enclosure
- Solar array may have separate perimeter depending on interconnection strategy (single vs. dual POI)
- Clear stand-off zone around data hall for vehicle barriers and surveillance coverage

**Stormwater Management:**
- Site grading directs runoff away from critical equipment areas
- Detention/retention ponds sized per Oklahoma DEQ stormwater permit requirements
- Low-impact development (LID) features incorporated where feasible

**Future Expansion Zones:**
- Site plan reserves space for future data hall expansion (estimated 2-3 additional buildings of similar size)
- Electrical infrastructure pathways sized for ultimate buildout capacity
- Solar array expansion potential remains (additional 10-15 MW if demand justifies)

**Site-Level Decisions Pending:**
- ALTA/NSPS survey to confirm legal boundaries, easements, and topography
- Geotechnical analysis to validate soil bearing capacity and foundation type
- Water delineation study to identify wetlands or floodplains
- Utility coordination with OG&E for 138 kV interconnection point and required upgrades

## 2.2 Building Envelope & Structural System

The data center building is designed as a hardened, energy-efficient envelope optimized for Oklahoma climate conditions and tornado risk.

**Building Type:** Pre-engineered metal building (PEMB) with insulated metal panels
- **Rationale:** Cost-effective, fast construction, proven for data center applications
- **Alternative Considered:** Tilt-up concrete (higher cost, longer schedule)

**Structural System:**
- **Roof Structure:** Clear-span steel frame, designed for equipment loads (HVAC units, cable tray)
- **Floor System:** Reinforced concrete slab-on-grade, 6-8" thick (exact thickness pending geotechnical report)
- **Column Grid:** 50-60 ft typical spacing to minimize columns in data hall
- **Foundation:** Spread footings or drilled piers (type TBD based on soil bearing capacity)

**Tornado Hardening (Oklahoma-Specific Requirement):**
Data centers in Oklahoma's tornado-prone region require enhanced wind resistance beyond standard IBC requirements.

**Wind Design Criteria:**
- **Basic Wind Speed:** 115 mph per ASCE 7-22 for Mayes County
- **Risk Category:** III or IV (essential facility classification)
- **Tornado Design:** EF-2 tornado resistance (135 mph winds) for critical areas
  - Data hall, electrical rooms, mechanical rooms, NOC
  - Generator and fuel storage enclosures
- **Missile Impact Protection:** Steel roof deck with impact-resistant insulation layer

**FM Global Compliance:**
Insurance underwriting typically requires FM Global roof and wall panel specifications for data centers:
- **Roof Rating:** FM 1-90 or 1-120 (wind uplift resistance)
- **Fire Rating:** Class 1 roof assembly (non-combustible construction)
- **Wall Panels:** 22-gauge steel with impact-resistant core

**Cost Impact:** Enhanced tornado hardening adds ~$150-250/SF to building envelope vs. standard PEMB construction. See [[Roof Upgrade Financial Analysis - 25K SF Building]] for detailed analysis.

**Building Height:**
- **Data Hall Ceiling Height:** 16-18 ft clear (measured from finished floor to underside of structure)
  - Accommodates overhead cable tray, busway, containment, and CDU piping
  - Higher ceiling enables better airflow management and equipment access
- **Support Space Ceiling Height:** 10-12 ft typical

**Thermal Envelope Performance:**
- **Roof Insulation:** R-30 minimum (exceeds ASHRAE 90.1-2019 for climate zone)
- **Wall Insulation:** R-19 minimum
- **Air Infiltration:** 0.25 CFM/SF @ 0.3" w.c. (tight envelope for PUE optimization)
- **Solar Reflectance:** Cool roof coating (SRI ≥78) to reduce cooling load

## 2.3 Data Hall Configuration

The data hall is the core IT production space, designed for high-density AI and network workloads with flexibility for customer-specific configurations.

**Data Hall Dimensions:**
- **Total White Space:** 25,000 SF
- **Layout:** Open floor plan with defined hot aisle containment zones
- **Floor System:** Structural slab-on-grade with overhead cable distribution (no raised floor)
  - Eliminates raised floor cost ($0.9-1.25M savings) and accelerates construction (2-4 weeks)
  - Provides superior structural stability for high-density rack loads
  - Simplifies cleaning and maintenance vs. underfloor plenum
  - All power and cooling distribution routed overhead via cable tray and busway

**Rack Layout:**
- **Total Rack Count:** 96 racks (48 AI + 48 network in baseline configuration)
- **Hot Aisle Configuration:** All racks face hot aisles with containment doors
- **Aisle Widths:**
  - Hot aisle: 4-5 ft (contained)
  - Cold aisle: 4-5 ft (open to room)
- **Cabinet Spacing:** 42U racks on 2 ft centers (rack-to-rack)

**Power Distribution Strategy:**
- **Overhead Busway:** 480V 3-phase busway runs parallel to hot aisles at ~12-14 ft elevation
- **Rack Power Panels (RPPs):** Drop from busway to each rack or row of racks
- **Redundancy:** 2N power feeds (A+B feeds from independent UPS/BESS systems)
- **Circuit Protection:** Branch circuit breakers at RPP level

**Cooling Distribution Strategy:**
- **Air-Cooled Zones (Network Racks):**
  - Option 1 (RD109 Baseline): Fan walls at end of hot aisles
  - Option 2 (PGCIS Recommendation): Rear-Door Heat Exchangers (RDHx) for per-rack control
  - **[DECISION PENDING]** - See Section 5.5 for detailed analysis
- **Liquid-Cooled Zones (AI Racks):**
  - Chilled water manifolds run overhead or under raised floor
  - Coolant Distribution Units (CDUs) provide rack-level liquid cooling
  - Rear-door coils or direct-to-chip cooling (customer-specific)

**Access & Egress:**
- **Minimum Exit Doors:** 2 (per IBC occupancy load calculation)
- **Door Width:** 3 ft minimum, 4 ft preferred for equipment moves
- **Emergency Lighting:** Battery-backed LED fixtures per NFPA 101
- **Exit Signage:** Illuminated "EXIT" signs at all egress points

**Physical Security:**
- Customer cages/suites defined by steel mesh partitions (floor-to-ceiling)
- Lockable cage doors with electronic access control
- Individual customer areas isolated for multi-tenant deployments

## 2.4 Support Spaces
Critical support spaces are sized and positioned to ensure efficient operations and maintenance.

### Electrical Rooms
- **Quantity:** 4 electrical rooms (one per UPS/BESS + switchboard train)
- **Size:** ~1,500 SF each (total ~6,000 SF)
- **Equipment:** UPS/BESS, switchboards, distribution panels, battery cabinets (if not BESS-as-UPS)
- **Access:** Roll-up doors for equipment delivery; direct access from exterior
- **Cooling:** Dedicated DX units (16× 42 kW per RD109 baseline)
- **Fire Suppression:** Clean agent (e.g., FM-200, Novec 1230) per NFPA 2001

### Mechanical Rooms
- **Quantity:** 2 mechanical rooms (N+1 redundancy)
- **Size:** ~2,000 SF each (total ~4,000 SF)
- **Equipment:** Chilled water pumps, expansion tanks, pressurization units, water treatment, chemical dosing
- **Access:** Direct access from exterior for equipment service
- **Cooling:** Dedicated DX units (4× 15 kW per RD109 baseline)

### Network Operations Center (NOC)
- **Size:** ~500 SF
- **Purpose:** 24/7 monitoring of facility systems (BMS, DCIM, security)
- **Equipment:** Workstations, video wall, server rack for monitoring systems
- **Cooling:** Separate HVAC zone (avoid impacting critical systems)
- **Security:** Controlled access;視線 to data hall entry points

### Staging & Burn-In Area **[OPTIMIZATION OPPORTUNITY - See Section 6 of Feasibility Memo]**
- **Size:** ~2,000 SF (proposed addition to RD109 baseline)
- **Purpose:** Pre-deployment equipment assembly, testing, and configuration
- **Rationale:** Prevents contamination of data hall, accelerates customer onboarding
- **Power:** Dedicated circuits for equipment burn-in testing
- **Cost Impact:** +$300-400K (includes building area + MEP)

### Loading Dock & Shipping/Receiving
- **Size:** ~1,000 SF staging area
- **Dock Height:** 48" standard truck bed height
- **Overhead Door:** 12 ft W × 14 ft H minimum
- **Access:** Direct path to data hall and staging area

### Staff Amenities
- **Office/Conference:** ~1,000 SF for management, engineering, sales meetings
- **Break Room/Kitchen:** ~400 SF with refrigerator, microwave, seating
- **Restrooms:** ADA-compliant, sized per IBC occupancy load
- **Showers & Lockers:** ~700 SF **[OPTIMIZATION OPPORTUNITY]** - Supports 24/7 operations and emergency response
  - Cost Impact: +$140-175K

### Telecommunications Rooms
- **Meet-Me-Room (MMR):** ~500 SF for carrier cross-connects
- **Main Distribution Area (MDA):** ~300 SF for facility backbone equipment
- **Intermediate Distribution Areas (IDA):** As needed for fiber distribution to customer cages

## 2.5 Loading Dock & Equipment Delivery Strategy

**Equipment Delivery Requirements:**
- **Truck Access:** Site design accommodates full-size semi-trailers (53 ft)
- **Turning Radius:** Adequate for tractor-trailer maneuvering
- **Dock-to-Data-Hall Path:** Clear path width 8-10 ft minimum for rack moves
- **Floor Load Capacity:** Slab designed for forklift operations (8,000 lb wheel loads)

**Critical Equipment Deliveries:**
- Chillers, generators, transformers delivered pre-assembled to outdoor yards
- UPS/BESS units delivered in modules, assembled in electrical rooms
- Racks delivered in crates, staged in staging area before deployment

## 2.6 Exterior Equipment Yards

Critical outdoor equipment is grouped into dedicated yards with appropriate clearances, screening, and access.

### Generator Yard
- **Location:** North side of building (minimize noise to staff areas)
- **Size:** ~5,000 SF (4× generators + 2× mechanical generators per RD109)
- **Fuel Storage:** Double-wall sub-base tanks or above-ground diesel tanks (48-hour runtime minimum)
- **Sound Attenuation:** Outdoor-rated sound enclosures (75 dBA @ 23 ft per RD109)
- **Clearances:** 10 ft minimum from building for exhaust discharge, maintenance access

### Chiller Plant Yard
- **Location:** North or east side of building
- **Size:** ~8,000 SF (3× air-cooled chillers + 5× fluid coolers per RD109)
- **Piping Runs:** Minimize distance to mechanical rooms to reduce pumping energy
- **Clearances:** Per manufacturer requirements for airflow and service access

### BESS Enclosure
- **Location:** Adjacent to electrical rooms (minimize cable runs)
- **Size:** **~4,500 SF (12 MW / 48 MWh BESS** in containerized or modular format)
- **Fire Safety:** NFPA 855 compliant (automatic suppression, gas detection, HVAC, explosion protection)
- **Security:** Separate fence with controlled access (high-value asset)
- **Clearances:** 10-15 ft from building per fire code and insurance requirements

### Utility Transformer Pad
- **Location:** Adjacent to building at utility service entry point
- **Size:** ~1,500 SF (**15-20 MVA transformer**, sized for full facility load + **12MW BESS charging**)
- **Oil Containment:** Containment basin per EPA Spill Prevention Control and Countermeasure (SPCC) requirements
- **Clearances:** Per NEC and utility company standards

---

# 3. CRITICAL ELECTRICAL SYSTEMS

## 3.1 Utility Interconnection Strategy

The facility requires high-voltage utility service to support the ~10 MW facility load and integrate the 12 MW solar + BESS microgrid.

**Utility Service Parameters:**
- **Utility Provider:** Oklahoma Gas & Electric (OG&E)
- **Voltage Level:** 138 kV transmission line (nearby line confirmed, exact interconnection point TBD)
- **Service Type:** Single-phase or three-phase high voltage (TBD via utility study)
- **On-Site Transformation:** Step-down to 13.8 kV medium voltage via utility-owned or customer-owned substation

**Point of Interconnection (POI) Strategy - [DECISION PENDING - See Decision #1 in Feasibility Memo]:**

**Option 1: Single POI with Behind-the-Meter (BTM) Configuration (RECOMMENDED)**
- Solar + BESS + data center all connect behind a single utility meter
- Microgrid operates as a single customer load/generation profile from utility perspective
- Advantages: Simplified metering, maximized solar utilization, optimal BESS dispatch
- Disadvantages: Requires advanced microgrid controls, utility may require additional study/upgrades

**Option 2: Dual POI Configuration (Fallback)**
- Data center connects at one POI (load only)
- Solar + BESS connect at separate POI (generation/storage)
- Advantages: Simpler utility approval process, follows traditional interconnection model
- Disadvantages: Limits behind-the-meter solar optimization, more complex metering/billing

**Critical Path Action Required:**
Initiate formal interconnection request with OG&E immediately. This study will define:
- Available capacity at nearest substation
- Required utility upgrades (transformers, switchgear, protection)
- Interconnection costs and timeline
- Preferred POI configuration

**Cost Exposure:**
- Utility system upgrades: $2-5M (TBD via utility study)
- Interconnection study fees: $50-150K
- Schedule risk: 6-18+ months if major upgrades required

## 3.2 Backup Power Generation Systems
Backup power generation provides continuous operation during extended utility outages or periods when solar + BESS cannot support full load (>4 hours).

**Primary Option: Natural Gas Turbines (RECOMMENDED)**
- **IT Load:** Natural gas turbines (sizing TBD)
- **Mechanical Load:** Natural gas turbines (sizing TBD)
- **Fuel Source:** Pipeline natural gas (nearby line identified, capacity confirmation required)
- **Advantages:**
  - Unlimited runtime (no on-site fuel storage constraints)
  - Lower emissions than diesel (NOx, particulates)
  - Lower fuel cost vs. diesel
  - No on-site fuel storage tanks (reduced environmental permitting)
- **Considerations:**
  - Requires natural gas service confirmation and capacity study
  - Turbine sizing and redundancy strategy differs from reciprocating engines

<!-- TODO: Research and update natural gas turbine sizing and redundancy strategy - discuss at site meeting. Turbine manufacturer TBD. -->

**Fallback Option 1: Natural Gas Reciprocating Generators**
- **Configuration:** Similar to RD109 baseline (4× IT + 2× mechanical), sized for natural gas fuel
- **Fuel:** Pipeline natural gas with potential diesel backup tanks
- **Use Case:** If turbines not feasible for site or capacity requirements

**Fallback Option 2: Diesel Generators (RD109 Baseline)**
- **IT Load Generators:** 4× 3,750 kVA diesel generators, N+1 redundancy
- **Mechanical Load Generators:** 2× 1,705 kVA diesel generators, N+1 redundancy
- **Total Installed Capacity:** 18.4 MVA (15 MVA IT + 3.4 MVA mechanical)
- **Fuel Storage:** 48-hour on-site diesel storage (8,000+ gallons total)
- **Use Case:** If natural gas service unavailable or insufficient capacity

**Generator Siting:**
- **Location:** Outdoor generator yard, north side of building
- **Enclosures:** Sound-attenuated weather-rated enclosures (75 dBA @ 23 ft per RD109)
- **Fuel Storage:** Double-wall sub-base tanks (1,320 gallons per generator per RD109) or separate above-ground tanks
- **Runtime at Full Load:** 48 hours minimum on-site fuel (expandable to 72+ hours with additional tankage)

**Runtime Reduction via BESS:**
With **48 MWh BESS providing 4.8+ hours of backup @ 10MW facility load** before generators start, annual generator runtime is projected to be reduced by 87% vs. traditional UPS-only architecture. This significantly reduces fuel costs, emissions, and generator maintenance requirements.

**Electrical Integration:**
- Each generator paired with dedicated 3,000 kVA (IT) or 1,500 kVA (mechanical) transformer
- Medium voltage output: 13.8 kV, 3-phase
- Automatic start on utility failure or BESS low state-of-charge (SOC) threshold
- Synchronization and load-sharing controls for parallel operation

**Standards Compliance:**
- NFPA 110 - Emergency and Standby Power Systems
- NEC Article 700 - Emergency Systems
- EPA Tier 4 emissions (if diesel) or equivalent state requirements

## 3.3 UPS Architecture

**[CRITICAL DESIGN DECISION - See Decision #5 in Feasibility Memo & BESS Analysis V2]**

Two mutually exclusive UPS architecture options are under evaluation:

### Option A: Pure BESS-as-UPS with Phased Deployment (RECOMMENDED)
- **BESS:** **16 MW / 48 MWh** with grid-forming inverters (N+1 redundancy), phased deployment
- **Phase 1:** 3×4MW inverters (8MW available N+1), supports ~75% occupancy
- **Phase 2:** Add 4th 4MW inverter (12MW available N+1), supports 100% occupancy
- **Traditional UPS:** None (BESS replaces UPS entirely)
- **Backup Duration:** **Phase 1: 6 hrs @ 8MW; Phase 2: 4.8 hrs @ 10MW** before generators required
- **BESS Function:** Dual-purpose (solar storage + UPS power conditioning)
- **Phase 1 CAPEX:** **$29.7-31.2M** (BESS + generators + advanced controls)
- **Phase 2 Incremental CAPEX:** **+$2.8-3.5M**
- **Total CAPEX:** **$32.5-34.7M**
- **CAPEX Savings:** **-$7.3-9.3M (-18% to -23%)** vs. Option B
- **Deferred CAPEX:** **~$2-3M deferred 8-12 months**
- **Annual O&M Savings:** -$445K/year (no UPS maintenance + reduced generator runtime)

**Architecture:** BESS grid-forming inverters operate in "always-on" mode, providing continuous power conditioning identical to online double-conversion UPS. No separate UPS layer required. Generators serve only as extended backup for outages >4 hours.

**Technical Requirements for Option A (BESS-as-UPS):**
To eliminate traditional UPS, the BESS must include the following capabilities:

✅ **Grid-Forming Inverters**
- Establish voltage and frequency independently (not grid-following)
- Response time <50ms to grid disturbances (within ITIC curve for IT equipment)
- Voltage regulation ±1%, frequency regulation ±0.1 Hz
- Harmonic distortion <5% THD (IEEE 519 compliant)

✅ **IEEE 2030.7/2030.8 Compliance**
- Advanced microgrid control algorithms (real-time power balancing)
- Seamless islanding and resynchronization
- Black-start capability
- Factory Acceptance Testing (FAT) and Site Acceptance Testing (SAT) protocols

✅ **N+1 Inverter Redundancy**
- **Phase 1:** 3× 4MW inverters for 12 MW total capacity (8MW available with one unit down)
- **Phase 2:** 4× 4MW inverters for 16 MW total capacity (12MW available with one unit down)
- Can lose any single inverter without load disruption

✅ **NFPA 855 Fire Safety Compliance**
- Automatic fire suppression system
- Gas detection and monitoring
- HVAC and thermal management
- Explosion protection (venting or suppression)

**Recommended Vendors:**
- Tesla Megapack (grid-forming capable, $400-500/kWh)
- Fluence Gridstack Pro (proven in data center applications, $500-600/kWh)
- Wärtsilä GridSolv Quantum (modular, good for phased expansion, $450-550/kWh)

**Decision Criteria:**
Option B (Pure BESS-as-UPS) is technically feasible and financially superior if the following conditions are met:
1. BESS vendor confirms grid-forming inverter capability
2. IEEE 2030.7/2030.8 compliant controls are implemented
3. NFPA 855 fire safety systems are designed and budgeted
4. Insurance quotes confirm BESS-only architecture is acceptable
5. Saga Energy commits to BESS-specific operations training

If any condition cannot be met, proceed with Option A (traditional UPS + BESS) as fallback.

**Final Decision Required:** End of October 2025 (to maintain equipment procurement schedule)

### Option B: Traditional UPS + BESS (Fallback)
- **UPS:** 8× 1,500 kW Galaxy VX UPS units (N+1 redundancy in 2N configuration)
- **UPS Batteries:** 32× Lithium-ion battery cabinets (17 modules each) for IT load
- **Mechanical UPS:** 2× 200 kW Galaxy VL UPS units + 2× battery cabinets (16 modules each)
- **BESS:** **12 MW / 48 MWh** (dedicated for solar storage only, not UPS function)
- **Backup Duration:** UPS provides 10-15 minutes (until generators online), BESS provides solar storage
- **Total CAPEX:** **$39-41M** (UPS + batteries + BESS + generators)
- **CAPEX Premium:** **+$6.5-8.5M (+20% to +26%)** vs. Option A
- **Annual O&M Premium:** +$445K/year (UPS maintenance + higher generator runtime)

**Architecture:** Traditional double-conversion UPS provides power conditioning and 10-15 minutes backup. Generators serve as primary backup power (start within 10 seconds of utility failure). BESS used only for solar energy storage, not backup power.

**Use Case for Option B:** If any of the following conditions apply:
1. BESS vendor cannot confirm grid-forming inverter capability meeting ITIC curve requirements
2. Insurance underwriters reject BESS-only backup architecture
3. Customer preference for proven UPS technology
4. Timeline constraints prevent IEEE 2030.7/2030.8 validation testing

## 3.4 Medium Voltage Distribution

All power sources (utility, generators, BESS) are distributed at 13.8 kV medium voltage to minimize electrical losses and simplify switchgear architecture.

**Medium Voltage Equipment:**
- **Voltage Level:** 13.8 kV, 3-phase
- **Main Switchgear:** Arc-resistant metal-clad switchgear per IEEE C37.20.7
- **Protective Relaying:** Microprocessor-based relays with arc flash detection and trip
- **Grounding:** Solidly grounded system per NEC Article 250

**Distribution Topology:**
- Utility service → 138kV/13.8kV transformer → Main switchgear
- Main switchgear → Generator paralleling switchgear (or BESS inverter switchgear)
- Generator/BESS switchgear → 4× IT transformers (3,000 kVA each)
- Generator/BESS switchgear → 2× Mechanical transformers (1,500 kVA each)

**Transformer Specifications (RD109 Baseline):**
- **IT Transformers:** 4× 3,000 kVA, 13.8kV-480Y/277V, VPI dry-type, outdoor rated
- **Mechanical Transformers:** 2× 1,500 kVA, 13.8kV-480Y/277V, VPI dry-type, outdoor rated
- **Impedance:** 5.75% typical
- **Cooling:** Dry-type, forced air (fans for overload conditions)

**Note on Substation Transformer Sizing:**
RD109 baseline does not explicitly size the utility-side 138kV/13.8kV transformer. For this project, the substation transformer must accommodate:
1. Initial facility load: ~10 MW
2. BESS charging load: Up to **12 MW** (if BESS charging from grid during low solar periods)
3. Future expansion: Reserve capacity for additional data halls

**Recommended Sizing:** **15-20 MVA minimum** (to accommodate 10MW facility + 12MW BESS charging), or dual transformers in N+1 configuration if utility allows.

**Action Required:** Confirm substation transformer capacity requirements with utility during interconnection study.

## 3.5 Low Voltage Distribution

Medium voltage is stepped down to 480V low voltage for distribution to all facility loads.

**Low Voltage Switchboards (RD109 Baseline):**
- **IT Switchboards (SWBD):** 4× QED-2 switchboards, 4,000A, 480V, 65kA SCCR (one per transformer)
- **Mechanical Switchboards (MECH SWBD):** 2× QED-2 switchboards, 1,600A, 480V, 35kA SCCR

**Distribution Architecture:**
- Each IT switchboard feeds overhead busway running through data hall
- Mechanical switchboards feed chiller plant, pumps, DX units, support spaces
- Critical mechanical loads (chillers, pumps) have 2N redundant feeds
- Non-critical loads (lighting, office HVAC) fed from single switchboard

**Circuit Breakers:**
- Main breakers: Molded-case or insulated-case breakers with electronic trip units
- Branch breakers: Thermal-magnetic or electronic trip
- Arc flash labels: Calculated per IEEE 1584 and NFPA 70E

**Power Quality:**
- Harmonic mitigation: UPS/BESS inverters provide filtering (no additional harmonic filters required)
- Power factor correction: Not required (UPS/BESS inverters operate at unity power factor)
- Transient voltage surge suppression (TVSS): Installed at main switchboards

## 3.6 Rack Power Distribution

480V power from switchboards is distributed via overhead busway to Rack Power Panels (RPPs), which step down to 208V for rack equipment.

**Overhead Busway System:**
- **Voltage:** 480V, 3-phase, 4-wire
- **Capacity:** 800-1000A per busway run (sized for rack density + growth)
- **Routing:** Parallel to hot aisles, mounted at ~12-14 ft elevation
- **Redundancy:** 2N feeds (A+B busway from independent UPS/BESS trains)
- **Manufacturer:** Starline, Eaton, or equivalent

**Rack Power Panels (RPPs):**
- **Input:** 480V from A+B busway
- **Output:** 208V, 3-phase for rack PDUs
- **Transformer:** Integrated 480V-208V step-down transformer
- **Protection:** Branch circuit breakers with remote monitoring
- **Redundancy:** Dual-corded equipment receives A+B feeds; single-corded from A or B

**Rack-Level Power:**
- **Power Density:** Up to 132 kW/rack (AI liquid-cooled), up to 22 kW/rack (network air-cooled)
- **PDU Configuration:** Vertical rack-mount PDUs, dual-corded for redundancy
- **Outlets:** C13/C19 or high-density outlets per customer requirements
- **Monitoring:** Real-time kW, kWh, voltage, current, power factor per rack (integrated with DCIM)

**Open Compute Project (OCP) Compliance:**
RD109 baseline specifies OCP-compliant rack power distribution. This is typical for hyperscale customers but may not be required for all colocation tenants.

**Question:** Is OCP compliance required for this project, or can traditional PDU architecture be used? (See line 64 of Feasibility Memo)

## 3.7 Electrical Redundancy & Fault Tolerance

The electrical system is designed to meet Tier III-equivalent concurrent maintainability and N+1 redundancy.

**N+1 Redundancy Strategy:**
- **Generators (Nat Gas Turbines):** Sizing and redundancy strategy TBD - turbine configuration differs from reciprocating engines. Research required on turbine parallel operation and N+1 implementation.
- **Generators (Diesel/Nat Gas Reciprocating - Fallback):** 4 generators support IT load; system designed for 3 active + 1 standby
- **UPS/BESS:** If traditional UPS: 8 UPS units in 2N configuration (4+4). If BESS with phased deployment:
  - **Phase 1:** 3× 4MW inverters (2+1 configuration, 8MW available with one unit down)
  - **Phase 2:** 4× 4MW inverters (3+1 configuration, 12MW available with one unit down)
- **Transformers:** 4 IT transformers (3+1 configuration)
- **Switchboards:** 4 IT switchboards (3+1 configuration)

**2N Power Paths to Racks:**
- A-side power path: Utility/Gen → TX-A → SWBD-A → Busway-A → RPP-A → Rack PDU-A
- B-side power path: Utility/Gen → TX-B → SWBD-B → Busway-B → RPP-B → Rack PDU-B
- Dual-corded IT equipment receives both A and B feeds (automatic failover via internal STS or external STS)

**Concurrent Maintainability:**
Any single electrical component (generator, transformer, switchboard, busway, RPP) can be removed for maintenance without impacting IT load, provided:
- Maintenance performed during planned maintenance window
- Load transferred to redundant path before work begins
- Procedures documented in O&M manuals

**Single Points of Failure (Intentionally Accepted):**
- Utility service entry (mitigated by generators + BESS backup)
- Rack-level single-corded equipment (customer responsibility to deploy dual-corded servers)

## 3.8 Grounding & Lightning Protection

**Electrical Grounding System:**
- **Ground Electrode System:** Building steel, concrete-encased electrode (Ufer ground), ground ring, driven ground rods
- **Target Ground Resistance:** <5 ohms (measured via fall-of-potential test)
- **TIA-942 Compliance:** Telecommunications grounding per TIA-607-C
- **Isolated Ground System:** Dedicated isolated ground for IT equipment (if required by customer, optional)

**Lightning Protection System:**
- **Roof-Level Air Terminals:** Lightning rods per NFPA 780 or UL 96A
- **Down Conductors:** Minimum 2 down conductors, bonded to building ground system
- **Surge Protection Devices (SPDs):** Installed at:
  - Utility service entrance (Type 1 SPD)
  - Main switchboards (Type 2 SPD)
  - Rack PDUs (optional Type 3 SPD for sensitive equipment)

## 3.9 DEVIATION: BESS-as-UPS Integration

**If Option B (Pure BESS-as-UPS) is selected, the following deviations from RD109 apply:**

### Equipment Eliminated:
- ❌ 8× 1,500 kW Galaxy VX UPS units
- ❌ 32× Lithium-ion battery cabinets (17 modules each)
- ❌ 2× 200 kW Galaxy VL UPS units (mechanical room)
- ❌ 2× Lithium-ion battery cabinets (16 modules each)

### Equipment Added:
- ✅ **16 MW / 48 MWh BESS** with grid-forming inverters (N+1 configuration, phased deployment)
  - Phase 1: 3×4MW inverters + full 48MWh battery
  - Phase 2: 4th 4MW inverter
- ✅ IEEE 2030.7/2030.8 compliant microgrid controller
- ✅ NFPA 855 fire suppression system for BESS enclosure
- ✅ Advanced energy management system (EMS) for solar + BESS + generator coordination

### Electrical Room Space Impact:
- Traditional UPS rooms can be repurposed or reduced in size
- BESS housed in outdoor containerized or modular enclosures (no indoor space required)
- Result: ~3,000-4,000 SF of electrical room space freed for future use or eliminated from building footprint

### Functional Changes:
- BESS operates in "always-on" grid-forming mode, providing continuous power conditioning
- Generators serve only as extended backup (>4 hours), not primary backup
- No separate UPS topology (BESS inverters perform all UPS functions)

**Cost Impact:**
- Phase 1: **$29.7-31.2M** vs. $39-41M traditional (saves $7.3-9.3M)
- Phase 2: **+$2.8-3.5M** (deferred 8-12 months)
- Total: **$32.5-34.7M** vs. $39-41M traditional
**Schedule Impact:** Neutral (BESS procurement timeline similar to UPS lead times)
**Cash Flow Benefit:** Defers ~$2-3M CAPEX by 8-12 months, aligns with lease-up
**Risk:** Requires advanced microgrid controls and vendor validation of grid-forming capability

See [[BESS as UPS Replacement - Feasibility Analysis V2]] for complete technical and financial analysis.

---

# 4. RENEWABLE ENERGY & MICROGRID

## 4.1 Solar Array Integration

A 12 MW DC solar photovoltaic (PV) array is being developed by Saga Energy on the same 121-acre site to provide renewable energy for the data center.

**Solar Array Parameters:**
- **Capacity:** 12 MW DC (approximately 9-10 MW AC depending on inverter efficiency)
- **Array Footprint:** ~80-100 acres (depending on panel efficiency and row spacing)
- **Panel Type:** High-efficiency monocrystalline silicon (TBD via solar EPC contractor)
- **Mounting:** Fixed-tilt ground mount or single-axis tracking (tracking increases energy yield ~15-20%)
- **Inverters:** String inverters or central inverters (TBD)
- **Design Life:** 25+ years with 80-85% capacity retention

**Annual Energy Production (Estimated):**
- **Location:** Pryor, OK (36.3°N latitude)
- **Solar Irradiance:** ~5.0-5.2 kWh/m²/day (annual average)
- **Capacity Factor:** ~18-22% (depending on tracking vs. fixed-tilt)
- **Annual Energy:** ~19-24 GWh/year

**Data Center Annual Energy Consumption:**
- **IT Load:** 7.4 MW × 8,760 hrs = 64.8 GWh/year (assumes 100% utilization)
- **Facility Load (PUE 1.25):** 64.8 GWh × 1.25 = 81 GWh/year

**Solar Contribution:**
- Solar provides ~24-30% of annual data center energy consumption (direct generation)
- With BESS storage, effective solar contribution increases to ~60-80% (pending Camelot net load analysis)

**Interconnection Approach:**
Solar array interconnects at the same Point of Interconnection (POI) as the data center, creating an integrated microgrid.

**Single POI (Behind-the-Meter) Configuration (RECOMMENDED):**
```
Utility 138kV
    ↓
[Substation Transformer 15-20 MVA]
    ↓
13.8kV Microgrid Bus
    ├── Data Center Load (~10 MW)
    ├── Solar Inverters (9-10 MW AC)
    └── BESS (16 MW total / 48 MWh, phased: 12MW→16MW)
```

**Advantages:**
- Solar energy consumed directly by data center (no export/import losses)
- BESS can store excess solar for nighttime use
- Simplified utility metering and billing
- Maximizes renewable energy utilization

**Disadvantages:**
- Requires advanced microgrid controls (included in BESS-as-UPS approach)
- Utility may require additional interconnection study and upgrades
- More complex protection and islanding logic

## 4.2 Battery Energy Storage System (BESS) Configuration

The BESS serves a dual function: solar energy storage and data center backup power (if BESS-as-UPS architecture is selected).

**BESS Specifications:**
- **Power Rating:** **16 MW AC (N+1 inverter redundancy), phased deployment**
  - Phase 1: 12 MW (3×4MW inverters), 8MW available N+1
  - Phase 2: 16 MW (4×4MW inverters), 12MW available N+1
- **Energy Capacity:** **48 MWh (4-hour duration at 12MW capacity; 6 hours @ 8MW Phase 1; 4.8 hours @ 10MW Phase 2)**
- **Chemistry:** Lithium Iron Phosphate (LFP)
  - Safer than NMC (lower thermal runaway risk)
  - Longer cycle life (6,000+ cycles @ 80% depth of discharge)
  - 12-year replacement cycle
- **Inverter Type:** Grid-forming (required for BESS-as-UPS function)
- **Response Time:** <50ms (meets ITIC curve for IT equipment protection)
- **Roundtrip Efficiency:** 85-90% (AC-to-AC)
- **Operating Temperature:** 15-35°C (active thermal management via liquid cooling or HVAC)

**BESS Deployment:**
- **Form Factor:** Containerized modules or outdoor-rated enclosures (e.g., Tesla Megapack, Fluence Gridstack)
- **Location:** Adjacent to electrical rooms (minimize cable runs)
- **Footprint:** **~4,500 SF for 48 MWh system**
- **Fire Safety:** NFPA 855 compliant enclosure with:
  - Automatic fire suppression (clean agent or water mist)
  - Gas detection (hydrogen, smoke, CO)
  - HVAC with smoke evacuation
  - Explosion venting or suppression

**BESS Operating Modes:**
1. **Solar Storage Mode (Daytime):**
   - Excess solar energy (beyond data center load) charges BESS
   - BESS maintains 80-100% state of charge (SOC)

2. **Discharge Mode (Nighttime / Low Solar):**
   - BESS discharges to serve data center load
   - Can support **full 10 MW facility load for 4.8+ hours** before generators required

3. **Grid Services Mode (Optional):**
   - If dual POI or front-of-meter configuration is selected, BESS can participate in SPP energy markets
   - Revenue stack includes: day-ahead energy, real-time energy, frequency regulation, reserves
   - (See Camelot Task 2 - Net Load Analysis for detailed revenue projections)

**Cycle Life & Replacement:**
- **Annual Cycles:** Estimated 20-30 cycles/year (one discharge/charge per day on average)
- **Warranty:** 6,000 cycles @ 80% depth of discharge (DOD)
- **Replacement Trigger:** When capacity degrades to <80% of original (typically 12-15 years)
- **Replacement Cost:** Budget **~$18-22M in Year 12** (escalated future dollars)

### **BESS Sizing Validation**

The 12 MW / 48 MWh configuration is based on the following validated assumptions:

**Total Facility Load Breakdown:**
- **IT Load:** 7.4 MW (48 AI racks @ 132 kW + 48 network racks @ 22 kW)
- **Cooling Load:** 1.8-2.6 MW (calculated from PUE 1.2-1.3)
- **Auxiliary Systems:** 0.2-0.4 MW (lighting, BMS, pumps, fans, UPS/inverter losses)
- **Total Facility Load:** **~10 MW**

**N+1 Redundancy Strategy:**
- **Phase 1 Configuration:** 3×4MW grid-forming inverters
  - Available Power: 8MW with one inverter down (covers ~75-80% facility occupancy)
- **Phase 2 Configuration:** 4×4MW grid-forming inverters
  - Available Power: 12MW with one inverter down (covers 10MW facility load + 20% margin)
- **Failure Mode:** Can lose any single inverter without impacting facility load in both phases

**Solar Array Match:**
- **Solar Capacity:** 12 MW DC solar array (~9-10 MW AC)
- **BESS Capacity:** 12 MW perfectly matches solar for symmetric microgrid design
- **Benefit:** Optimal energy balance; BESS can absorb full solar output during low-load periods

**Backup Duration:**
- **At 12MW:** 48MWh ÷ 12MW = 4.0 hours
- **At 10MW (actual facility load):** 48MWh ÷ 10MW = **4.8 hours**
- **Generator Start:** Generators auto-start when BESS reaches 20-30% SOC (~1 hour reserve remaining)

**⚠️ Action Required:**
1. Commission detailed electrical load study to validate 10MW total facility load
2. If PUE optimization achieves 1.2 (vs. 1.3), facility load may be ~8.8-9MW
3. Validate 16MW/48MWh phased deployment pricing with vendor RFIs
4. Include contractual option to purchase 4th inverter at locked pricing in Phase 1 contract

### 4.2.1 Phased Deployment Infrastructure Requirements

To support adding the 4th inverter in Phase 2 without major rework:

**Electrical Infrastructure (Size for 4, Build for 4):**
- Substation transformer: 15-20 MVA (supports full 16MW BESS + 10MW load)
- 13.8kV switchgear: 4 breaker positions for BESS inverters (all installed day 1)
- DC buswork: Sized for 16MW continuous rating
- AC distribution: 4 inverter connection points with isolation breakers

**Physical Infrastructure:**
- BESS enclosure: 4,500 SF (accommodates 4 inverters + 12 battery containers)
- Inverter foundation pads: Install 4 pads in Phase 1 (occupy pad 4 with temp barrier)
- Cable trays/conduit: Route for all 4 inverters in Phase 1
- Fire suppression: Size for full 4-inverter layout

**Procurement Strategy:**
- Execute equipment contract with option to purchase 4th inverter
- Lock pricing and delivery terms for Phase 2 inverter
- Maintain spare parts compatibility across both phases
- Coordinate with EPC for installation readiness

**Phase 2 Trigger Point:**
- Target: When facility reaches ~75% leased (~7.5MW committed load)
- Lead time: 6-9 months from order to commissioning
- Coordination: Plan installation during scheduled maintenance window

## 4.3 Microgrid Controls & Energy Management System

The microgrid controller is the "brain" that coordinates power flow between utility, solar, BESS, generators, and data center load.

**Microgrid Controller Requirements:**

**IEEE 2030.7 Compliance (Microgrid Controller Standard):**
- Real-time power balancing (solar + BESS + gensets = data center load + losses)
- Seamless mode transitions:
  - Grid-connected mode (normal operation)
  - Islanded mode (utility outage, running on solar + BESS + generators)
  - Generator-supported mode (BESS low SOC, generators online)
- Frequency and voltage regulation (maintain 60 Hz ± 0.1 Hz, 480V ± 1%)

**IEEE 2030.8 Compliance (Microgrid Testing Standard):**
- Factory Acceptance Testing (FAT) procedures
- Site Acceptance Testing (SAT) procedures
- Integrated system testing (verify all operating modes)

**Key Control Functions:**
1. **BESS State Management:**
   - Monitor SOC, temperature, voltage, current
   - Optimize charging/discharging to extend battery life
   - Prevent over-discharge (<20% SOC) or over-charge (>95% SOC)

2. **Generator Dispatch Logic:**
   - Auto-start generators when BESS SOC reaches threshold (e.g., 30%)
   - Load sharing between generators (if multiple units online)
   - Ramp-down generators when solar/BESS can resume load support

3. **Solar Curtailment (if needed):**
   - If BESS fully charged and data center load low, curtail solar output to prevent reverse power flow to utility (unless export is permitted)

4. **Power Quality Monitoring:**
   - Continuous monitoring of voltage, frequency, harmonics, power factor
   - Fault detection and isolation
   - Automatic protective relay coordination

5. **Predictive Analytics:**
   - Solar generation forecasting (weather-based)
   - Data center load prediction (historical patterns)
   - Optimize BESS charging/discharging to minimize grid import

6. **SCADA Integration:**
   - 24/7 remote monitoring and control
   - Integration with Building Management System (BMS) and DCIM
   - Alarms and notifications for off-normal conditions

**Recommended Microgrid Control Systems:**
- **Schneider Electric EcoStruxure Microgrid Advisor** - Integrates seamlessly with RD109 baseline equipment
- **Siemens Spectrum Power Microgrid Management System** - Utility-grade reliability, proven in large-scale deployments
- **Fluence NISPERA** - Advanced distributed energy resource (DER) management platform (if Fluence BESS selected)

**Cost:** $1.05-1.55M for fully IEEE 2030.7/2030.8 compliant system

## 4.4 Behind-the-Meter vs. Front-of-Meter Strategy

**Behind-the-Meter (BTM) - RECOMMENDED:**
- Solar and BESS interconnect on customer side of utility meter
- All solar energy consumed by data center first; only net load (or net export) seen by utility
- BESS optimized for data center backup and solar storage (not grid services)
- Advantages: Maximizes solar utilization, minimizes utility demand charges, simplifies customer billing
- Disadvantages: Foregoes potential grid services revenue from BESS

**Front-of-Meter (FTM) - Alternative:**
- Solar and BESS interconnect on utility side of meter (separate metering point)
- Solar can export to grid when data center load is low
- BESS can participate in SPP energy and ancillary services markets
- Advantages: Additional revenue streams from energy arbitrage and frequency regulation
- Disadvantages: Complex metering, revenue uncertainty, may not maximize data center resilience

**Decision Criteria:**
- If primary goal is **data center resilience and renewable energy utilization**, choose BTM
- If primary goal is **maximizing financial return from solar/BESS assets**, evaluate FTM (requires Camelot net load analysis to quantify revenue potential)

**Action Required:** Camelot Task 2 (Net Load Analysis) will model both configurations and provide revenue projections. Final decision pending study completion (expected early November 2025).

## 4.5 Demand Response & Grid Services Participation

The microgrid configuration enables optional participation in utility demand response (DR) and grid services programs.

**Potential Revenue Streams:**
1. **Demand Response (DR):** Curtail data center load or shift load to generators/BESS during utility peak demand events
   - Risk: Requires customer agreement to interrupt non-critical loads

1. **Frequency Regulation:** BESS responds to real-time frequency signals from grid operator (SPP)
   - Risk: Increases BESS cycling (reduces battery life if not managed)

1. **Spinning Reserves:** BESS or generators on standby to provide backup capacity to grid
   - Risk: Requires generators to be online or BESS to reserve capacity

**Feasibility for This Project:**
- BTM configuration limits grid services participation (BESS behind customer meter)
- FTM configuration enables full participation but reduces data center resilience benefits
- Recommendation: Prioritize data center resilience; evaluate DR/grid services as secondary revenue if FTM configuration is selected

**Study Required:** Camelot Task 1 (SPP Oklahoma Market Study) will analyze market dynamics and revenue stack potential. Expected delivery early November 2025.

---

# 5. MECHANICAL & COOLING SYSTEMS

## 5.1 Cooling Architecture Overview
The facility employs a hybrid cooling strategy to efficiently support both high-density AI racks (liquid-cooled) and standard-density network racks (air-cooled).

**Cooling Philosophy:**
- **Air Cooling for Network Racks:** Up to 22 kW/rack via rear-door heat exchangers (RDHx)
  - **RDHx Approach:** Rack-based cooling with chilled water coils mounted on each rack's rear door (vs. RD109's zonal fan wall approach)
  - **Advantage:** Provides per-customer cooling control, monitoring, and billing - critical for flexible colocation model
  - **Trade-off:** Higher upfront cost per rack vs. centralized fan walls, but better flexibility for mixed density deployments
- **Liquid Cooling for AI Racks:** Up to 132 kW/rack via coolant distribution units (CDUs) and direct-to-chip or rear-door coils
- **Hot Aisle Containment:** All racks face hot aisles; containment doors isolate hot air return path
  - <!-- TODO: Verify if hot aisle containment is typically needed with RDHx rack-based cooling - may not be required if RDHx handles all rack exhaust heat -->
- **Room-Level Air Handling:** CRAH units required for general humidity control and sensible heat load from building envelope, lighting, and PDU losses (RDHx/CDUs address rack heat only)
- **Redundancy:** N+1 configuration for all critical cooling components (chillers, pumps, CDUs, CRAH units)

**Target PUE:** 1.2-1.3 (annual average)
- Free cooling months (Oct-Apr): PUE 1.15-1.25
- Mechanical cooling months (May-Sep): PUE 1.25-1.35

**Design Approach:**
The cooling system is based on Schneider Electric RD109 Reference Design, optimized for Oklahoma climate conditions (Pryor is similar to Dallas in summer heat but colder in winter, enabling extended free cooling).

## 5.2 Chilled Water Plant

The chilled water plant provides cooling capacity for all data hall and support space loads.

**Chiller Configuration (RD109 Baseline - Dallas):**
- **Quantity:** 3× air-cooled chillers with integrated free cooling (N+1 redundancy)
- **Capacity per Chiller:** 1,177 kW (Dallas configuration)
- **Total Installed Capacity:** 3,531 kW (N+1, any two chillers support full load)
- **Model Reference:** Uniflair XRAF3612G (screw compressor, dual power supply)

**Free Cooling Capability:**
Modern air-cooled chillers with integrated free cooling operate in three modes:
1. **Full Free Cooling Mode (Winter):** Compressors off, heat rejected via air-cooled coils only (ambient <50-55°F)
2. **Partial Free Cooling Mode (Spring/Fall):** Compressors run at reduced capacity (ambient 55-75°F)
3. **Full Mechanical Cooling Mode (Summer):** Compressors run at full capacity (ambient >75°F)

**DEVIATION: Elimination of Adiabatic Fluid Coolers**

**RD109 Baseline Includes:**
- 5× adiabatic fluid coolers with HydroBlu technology (Dallas configuration)
- Capacity: 1,478 kW each
- Function: Pre-cool outdoor air via evaporative assist before entering chiller coils

**PGCIS Recommendation: Eliminate Adiabatic Fluid Coolers**

**Primary Rationale:**
1. **Zero Water Consumption:** Closed-loop air-cooled system vs. evaporative pre-cooling
2. **Sustainability Story:** Compelling for investors and customers (no water use in drought-prone region)
3. **Reduced Complexity:** Fewer components, simpler controls, easier commissioning
4. **Lower Long-Term O&M:** No water treatment chemicals, no nozzle maintenance, no seasonal startup/shutdown

**System-Wide Impacts of This Decision:**

**Chiller Sizing & Performance:**
- Air-cooled chillers must work harder during peak summer months without evaporative assist
- May require slightly larger chiller capacity (+5-10%) to maintain design supply temperature during 95°F ambient conditions
- Expected impact: Increase chiller installed capacity from 3× 1,177 kW (RD109) to 3× 1,250-1,300 kW for Pryor climate

**PUE Impact:**
- Modest PUE increase during peak summer months: +0.02 to +0.05 (e.g., 1.28 → 1.30-1.33)
- Minimal annual PUE impact due to Oklahoma's extended free cooling season (~215 days/year)
- Trade-off: Slightly higher summer electrical consumption vs. zero water consumption year-round

**Cost Impact:**
- Eliminate adiabatic fluid coolers: -$750K to -$1M (5 units @ $150-200K each)
- Larger air-cooled chillers: +$900K to +$1.3M (3 units @ $300-400K each)
- **Net CAPEX Impact: +$150K to +$450K**
- **Annual OPEX Savings: -$15-25K/year** (water cost + treatment + maintenance)

**Climate Validation Required:**
Pryor, Oklahoma has a humid subtropical climate similar to Dallas but with colder winters, which extends the free cooling season.

**Pryor, OK Design Conditions (ASHRAE):**
- Summer: 95°F dry bulb / 78°F wet bulb (99.6% design day)
- Winter: 10°F dry bulb (99.6% design day)
- Annual cooling degree days: ~2,200 (similar to Dallas)
- Annual heating degree days: ~3,600 (colder than Dallas, better for free cooling)

**Action Required:**
Mechanical engineer must perform bin analysis using Pryor, OK psychrometric data to:
1. Confirm chiller capacity required for 95°F/78°F wet bulb design day
2. Calculate annual PUE across all operating modes (free cooling, partial, full mechanical)
3. Validate that PUE increase is within acceptable range (target: maintain annual PUE <1.30)

**Decision:** Proceed with adiabatic elimination unless PUE modeling shows annual average >1.35 or unacceptable summer peak performance.

**Chiller Siting:**
- Location: Outdoor chiller yard, north or east side of building
- Clearances: Per manufacturer specifications for airflow (typically 10-15 ft for service access)
- Noise: Outdoor enclosures or acoustic barriers if noise ordinance requires (<70 dBA at property line typical limit)

## 5.3 Pumping & Distribution

Chilled water is circulated through the facility via primary/secondary pumping loops with N+1 redundancy.

**Pumping Configuration (RD109 Baseline):**
- **Chilled Water Pumps (CWP):** 5-8 pumps (exact count TBD during detailed design)
  - Primary pumps: Constant flow through chillers
  - Secondary pumps: Variable flow to data hall loads (CDUs, RDHx, air handlers)
- **Redundancy:** N+1 (any single pump failure does not impact cooling capacity)
- **VFD Control:** Variable frequency drives on secondary pumps to optimize energy efficiency

**Piping Distribution:**
- **Supply Temperature:** 45-50°F (adjustable based on load profile)
- **Return Temperature:** 60-65°F (ΔT = 10-15°F target)
- **Piping Material:** Schedule 40 steel or CPVC (indoor), insulated to prevent condensation
- **Routing:** Overhead or under raised floor (if raised floor is selected)

**Water Treatment System:**
- **Pressurization Unit (PU):** 2× dual pump units (N+1) with feeder tank
- **Expansion Tanks (ET):** 2× bladder-type tanks (sized for system volume)
- **Chemical Dosing Pot (CDP):** 2× 8L units for corrosion and biological inhibitors
- **Dirt & Air Separator (DAS):** 2× horizontal-type units for system cleanliness

**Thermal Storage Tanks (Optional):**
RD109 baseline includes 2× 10,000-gallon thermal storage tanks. These can be used for:
1. Load shifting: Charge tanks during off-peak hours, discharge during peak
2. Thermal inertia: Buffer against chiller start/stop cycles
3. Resilience: Additional cooling capacity during chiller maintenance

**Decision:** Evaluate thermal storage tank benefit via PUE modeling. If peak load shifting is not required (due to solar/BESS microgrid), tanks may be eliminated to reduce cost.

## 5.4 In-Row Cooling vs. Rear-Door Heat Exchangers (RDHx)

**PGCIS Recommendation: Rear-Door Heat Exchangers (RDHx) for Air-Cooled Racks**

**RD109 Baseline Approach:**
- Fan walls at end of hot aisles
- Hot air pulled from hot aisle containment, cooled via fan wall heat exchangers, returned to data hall

**Limitations of Fan Walls:**
- Serves entire zone (difficult to allocate cooling to individual customers)
- Less flexibility for variable rack densities within same row
- Challenging to bill cooling usage per customer

**Alternative: Rear-Door Heat Exchangers (RDHx):**
- Passive or active rear-door coils mounted on each rack
- Chilled water circulates through coil, rejecting heat from rack exhaust air
- Each rack has dedicated cooling capacity (no shared zones)

**Advantages of RDHx:**
- **Per-Customer Control:** Each customer suite has isolated cooling capacity
- **Flexibility:** Mix high-density and low-density racks in same row without airflow conflicts
- **Billing:** Measure chilled water flow per rack for accurate cooling cost allocation
- **Scalability:** Add RDHx only where needed (not entire data hall)

**Disadvantages of RDHx:**
- Higher upfront cost per rack (~$3-5K per RDHx vs. centralized fan wall)
- More chilled water connections (more leak detection points)
- Customer-specific: Some customers may prefer fan wall approach

**Recommendation:**
- If business model is **flexible colocation** with multiple customers of varying densities, RDHx is preferred
- If business model is **single-tenant master lease**, fan walls are lower cost and sufficient

**Action Required:** Align cooling strategy with Saga Energy sales and marketing approach. Decision required by Oct 20 Midpoint Review.

## 5.5 Liquid Cooling for AI Racks

High-density AI racks (up to 132 kW/rack) require liquid cooling due to heat density exceeding air-cooling limits (~25-30 kW/rack maximum for air).

**Liquid Cooling Architecture (RD109 Baseline):**
- **Coolant Distribution Units (CDUs):** 9× MCDU-50 equivalent units (or similar)
- **Function:** Provide rack-level chilled water distribution and return collection
- **Capacity:** ~50 kW per CDU (scalable based on rack count)
- **Coolant Type:** Facility chilled water (45-50°F supply) or dielectric fluid (for direct-to-chip)

**Rack-Level Liquid Cooling Options:**
1. **Rear-Door Liquid Coils:** Chilled water coil mounted on rack rear door (passive or active fans)
   - Capacity: 50-80 kW/rack
   - Simple retrofit to existing racks
   - Lower cost vs. direct-to-chip

2. **Direct-to-Chip Liquid Cooling:** Cold plates mounted directly on CPUs/GPUs
   - Capacity: 100-150+ kW/rack
   - Requires server OEM support (Dell, HPE, Supermicro)
   - Higher efficiency (removes heat at source before it enters air)

**Deployment Strategy:**
- **Initial Deployment:** Pre-install CDUs and chilled water manifolds for 48 AI racks
- **Customer-Specific:** Liquid cooling hardware (rear-door coils or cold plates) deployed when customer moves in
- **Flexibility:** Some customers may deploy lower-density AI racks air-cooled; reserve liquid cooling capacity for high-density customers

**Manifold Distribution:**
- Overhead chilled water manifolds run parallel to rack rows
- Quick-connect fittings at each rack position for fast deployment
- Leak detection sensors under all connections (integrated with BMS)

## 5.6 Hot Aisle Containment Strategy

All racks exhaust to hot aisles with physical containment to improve cooling efficiency and PUE.

**Containment Design:**
- **Type:** Hard-sided hot aisle containment with doors
- **Materials:** Polycarbonate panels or metal framed doors (transparent for visibility)
- **Height:** Floor-to-ceiling (if raised floor) or floor-to-overhead cable tray (if slab)
- **Pressure:** Negative pressure in hot aisle (fans pull air from containment)

**Benefits:**
- Prevents hot/cold air mixing (improves cooling efficiency)
- Increases supply air temperature setpoint (reduces chiller energy)
- Enables higher density deployments (cold air not diluted by hot exhaust)

**Access:**
- Hot aisle doors for maintenance access to rear of racks
- Interlocked with fire suppression (doors auto-open on fire alarm)

## 5.7 Mechanical Equipment Redundancy

All critical cooling components are deployed in N+1 redundancy to ensure concurrent maintainability.

**N+1 Redundancy Summary:**
- **Chillers:** 3 units, any 2 support full load (N+1)
- **Chilled Water Pumps:** 5-8 units, any one failure does not impact capacity
- **CDUs (Liquid Cooling):** 9 units for 48 AI racks (N+1 if ~6-7 units required for full load)
- **Fan Walls or RDHx:** N+1 capacity per zone

**Maintenance Mode:**
- Any single chiller can be isolated and removed from service without impacting IT load
- Chilled water loop includes isolation valves and bypass piping for maintenance
- Pumps have redundant units to allow rotation for preventive maintenance

## 5.8 PUE Targets & Energy Efficiency Measures

**Target PUE:** 1.2-1.3 (annual average)

**PUE Breakdown:**
- IT Load: 7.4 MW (100%)
- Cooling Load: ~1.2-1.8 MW (15-25% of IT load, varies by season)
- Lighting & Support: ~0.2-0.3 MW (3-5%)
- Total Facility Load: ~9-9.5 MW
- PUE = 9.5 MW / 7.4 MW = 1.28

**Energy Efficiency Strategies:**
1. **Free Cooling:** Maximize hours of free cooling operation (Oct-Apr in Oklahoma)
2. **Variable Speed Drives (VFDs):** All pumps and fans on VFDs to optimize part-load efficiency
3. **High Supply Temperature:** Increase chilled water supply temperature to 50°F (reduces chiller lift)
4. **Hot Aisle Containment:** Prevents hot/cold air mixing
5. **LED Lighting:** High-efficiency LED lighting with occupancy sensors
6. **Efficient UPS/BESS:** If BESS-as-UPS selected, eliminates 4-8% UPS conversion losses (see Section 3.3)

**Monitoring & Verification:**
- Real-time PUE monitoring via DCIM platform
- Monthly PUE reporting (calculated per The Green Grid guidelines)
- Continuous commissioning to identify efficiency degradation

## 5.9 Water Usage & Treatment

**DEVIATION: Closed-Loop System (No Water Consumption)**

**RD109 Baseline:**
- Adiabatic fluid coolers consume water via evaporative pre-cooling
- Estimated water usage: [TBD - calculate based on 1,478 kW per unit × 5 units × operating hours]

**PGCIS Recommendation:**
- Eliminate adiabatic cooling (see detailed analysis in Section 5.2)
- Air-cooled chillers with integrated free cooling (closed-loop, no evaporation)
- **Water Usage: ~0 gallons/year for cooling** (only domestic water for staff use)

**Benefits:**
- Eliminates ongoing water cost and supply risk
- Strong sustainability story (no water consumption in drought-prone region)
- Reduces permitting complexity (no water rights or wastewater discharge permits for cooling)

**Water Treatment (Chilled Water Loop):**
- Chemical treatment for corrosion and biological control
- Make-up water only needed for initial fill and leak replacement (minimal)

**Domestic Water:**
- Site water service required for:
  - Restrooms and break room
  - Emergency eyewash/showers (if required by OSHA for chemical handling)
  - Fire suppression system fill (if wet pipe sprinkler system is used)

**Action Required:** Confirm water service availability and capacity via Water & Wastewater Availability Study (recommended in Feasibility Memo Section 4.3).

## 5.10 Climate-Specific Optimization

**Pryor, Oklahoma Climate Characteristics:**
- **ASHRAE Climate Zone:** 3A (warm-humid)
- **Cooling Season:** May - September (~150 days)
- **Free Cooling Season:** October - April (~215 days)
- **Average Winter Low:** 30-40°F (excellent for free cooling)
- **Average Summer High:** 85-95°F (requires mechanical cooling)

**Optimization Opportunities:**
1. **Extended Free Cooling:** Pryor's colder winters (vs. Dallas baseline) extend free cooling season by ~30 days
2. **Economizer Mode:** Chillers can operate in economizer mode (compressors off) for ~60% of annual hours
3. **Part-Load Efficiency:** Size chillers for part-load operation (2 of 3 chillers running most of year)

**Action Required:** Mechanical engineer to perform bin analysis (ASHRAE 8760 hour climate data) to:
- Validate free cooling hours
- Confirm chiller sizing for Oklahoma conditions
- Calculate annual PUE with climate-optimized controls

## 5.11 Support Space HVAC

Non-critical support spaces (offices, break room, NOC) are served by independent HVAC systems to isolate from critical cooling.

**Electrical Rooms:**
- **Cooling:** 16× 42 kW DX units with remote air-cooled condensers (per RD109)
- **Redundancy:** N+1 (any single unit failure does not exceed temperature limits)
- **Setpoint:** 25°C ± 2°C (77°F ± 4°F)

**Mechanical Rooms:**
- **Cooling:** 4× 15 kW DX units with remote air-cooled condensers (per RD109)
- **Redundancy:** N+1

**Office/NOC/Break Room:**
- **System Type:** Rooftop package units (RTUs) or split systems
- **Redundancy:** Not required (non-critical spaces)
- **Control:** Thermostat control, occupied/unoccupied setback

## 5.12 DEVIATION: Elimination of Adiabatic Cooling

**Summary of Deviation:**
- ❌ Eliminate: 5× Guntner GFD V-Shape adiabatic fluid coolers (RD109 baseline)
- ✅ Use: Air-cooled chillers with integrated free cooling only

**Rationale:**
1. Closed-loop system (no water consumption)
2. Simpler operation and maintenance
3. Better sustainability story
4. Lower long-term operating cost (no water, no water treatment)

**Cost Impact:**
- Adiabatic fluid coolers: ~$150-200K each × 5 = $750K-1M
- Air-cooled chillers with free cooling: ~$300-400K each × 3 = $900K-1.2M
- **Net Impact: ~$150-450K cost increase** (higher chiller cost offset by elimination of fluid coolers)

**Performance Impact:**
- PUE may increase by 0.02-0.05 during peak summer months (reduced pre-cooling effectiveness)
- Annual PUE impact minimal due to Oklahoma's extended free cooling season

**Decision:** Recommend elimination of adiabatic cooling unless PUE modeling shows unacceptable performance degradation.

---

# 6. PLUMBING & UTILITIES

## 6.1 Domestic Water Service

The facility requires domestic water for staff use and fire suppression system fill (if wet pipe sprinkler system is used).

**Water Demand:**
- **Domestic Use:** Restrooms, break room, showers (if added per Feasibility Memo optimization)
  - Estimated demand: ~500-1,000 gallons/day (assuming 5-10 staff on-site)
- **Fire Suppression Fill:** One-time fill for wet pipe sprinkler system (if used)
  - Estimated volume: 5,000-10,000 gallons (one-time)
- **Cooling System Fill:** One-time fill for chilled water loop
  - Estimated volume: 5,000-8,000 gallons (closed-loop, minimal makeup)

**Water Service Requirements:**
- **Supply:** Municipal water or on-site well (TBD via site study)
- **Pressure:** 60-80 psi minimum at building entry point
- **Meter Size:** 2-3" meter (adequate for domestic flow + fire system fill)
- **Backflow Prevention:** Reduced pressure backflow preventer (RP) required by code

**Action Required:**
- Confirm water service availability via local water authority
- Request Water & Wastewater Availability Study (recommended in Feasibility Memo) to validate:
  - Service line capacity
  - Pressure at site
  - Connection fees and timeline

## 6.2 Sanitary Sewer & Wastewater

Sanitary sewer service is required for staff restrooms, break room, and showers (if added).

**Wastewater Flow:**
- **Domestic Wastewater:** ~500-1,000 gallons/day (restrooms, break room, showers)
- **Process Wastewater:** None (closed-loop cooling system, no blowdown or discharge)

**Sewer Service Requirements:**
- **Connection:** Municipal sanitary sewer or on-site septic system (TBD via site study)
- **Pipe Size:** 4-6" sanitary sewer lateral
- **Grease Trap:** Required if commercial kitchen is included (break room sink only = not required)

**Action Required:**
- Confirm sanitary sewer availability and capacity via local wastewater authority
- If municipal sewer not available, design on-site septic system per Oklahoma DEQ requirements

## 6.3 Chilled Water Makeup & Treatment

The chilled water system is a closed-loop with minimal makeup water requirements.

**Makeup Water Sources:**
- **Initial Fill:** ~5,000-8,000 gallons (one-time)
- **Annual Makeup:** <1% of system volume per year (leak replacement only)
- **Source:** Domestic water service (filtered and treated before entering chilled water loop)

**Water Treatment System:**
- **Chemical Dosing:** Corrosion inhibitors, biological growth inhibitors, pH buffers
- **Filtration:** Side-stream filters to remove particulates
- **Monitoring:** Conductivity, pH, dissolved oxygen sensors (integrated with BMS)

**Chemical Storage:**
- **Location:** Mechanical room or outdoor chemical storage shed
- **Containment:** Secondary containment per EPA SPCC requirements (if >55 gallons)

## 6.4 Water Leak Detection System

Leak detection is critical to protect IT equipment and enable rapid response to water system failures.

**Leak Detection Zones:**
- Under all chilled water piping in data hall (if overhead routing)
- Under all CDU connections
- Under all quick-connect fittings for liquid-cooled racks
- Mechanical rooms (near pumps, valves, heat exchangers)

**Detection Technology:**
- **Sensing Cable:** Conductive fluid detection cable (detects presence of water)
- **Spot Detectors:** Discrete leak detectors at high-risk locations (under CDUs, valves)
- **Integration:** All leak detection alarms integrated with BMS and DCIM (immediate notification to NOC)

**Response Procedures:**
- Leak alarm triggers:
  1. Audible and visual alarm in NOC
  2. Automatic alert to on-call engineer (SMS/email)
  3. Automatic isolation valve closure (if leak in specific zone can be isolated)
  4. Maintenance team dispatched to locate and repair leak

## 6.5 Natural Gas Service

Natural gas service is required only if dual-fuel or natural gas generators are selected (pending Decision #2).

**Natural Gas Demand:**
- **Generators:** 4× 3750 kVA generators (IT) + 2× 1705 kVA generators (mechanical)
- **Fuel Consumption at Full Load:** ~500-700 CFH per IT generator, ~200-300 CFH per mechanical generator
- **Peak Demand:** ~3,000-4,000 CFH (if all generators running simultaneously)

**Gas Service Requirements:**
- **Pressure:** 5-10 psig at meter (typical utility delivery pressure)
- **Meter Size:** 6-8" meter for peak demand
- **Backup Fuel:** Diesel fuel in sub-base tanks or separate storage (dual-fuel mode)

**Action Required:**
- If dual-fuel or natural gas generators are selected, confirm natural gas service availability to site
- Request capacity study from gas utility (Oklahoma Natural Gas or local provider)

## 6.6 Fuel Oil Storage (If Diesel Generators)

If diesel-only generators are selected, on-site fuel oil storage is required for 48-hour minimum runtime.

**Fuel Storage Configuration (RD109 Baseline):**
- **Type:** Double-wall sub-base tanks integrated with generator enclosures
- **Capacity per Generator:** 1,320 gallons per IT generator (per RD109 spec)
- **Total On-Site Storage:** ~8,000 gallons (6× generators × 1,320 gal each)

**Alternative: Above-Ground Storage Tanks (AST):**
- Centralized fuel farm with 10,000-20,000 gallon AST
- Day tanks at each generator (smaller sub-base tanks for immediate use)
- Fuel transfer pumps from AST to day tanks

**Regulatory Requirements:**
- **EPA SPCC Plan:** Required if total fuel storage >1,320 gallons (aggregate across all tanks)
- **Secondary Containment:** 110% of largest tank volume
- **Spill Kits:** On-site spill response equipment and training
- **Tank Inspections:** Annual inspections per EPA and Oklahoma DEQ requirements

**Fuel Delivery:**
- **Truck Access:** Fuel delivery trucks require access to generator yard or AST location
- **Fill Connections:** Camlock or threaded fill connections per NFPA 30 and 110

---

