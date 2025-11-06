**Created:** 2025-10-29
**Updated from:** Pryor_Bod_EVS_Rev01.md

# BASIS OF DESIGN - PLUMBING
## CSI Division 22
### Pryor Data Center - PACHYDERM GLOBAL

**Parent Document:** [[Saga Pryor DC/Basis of Design/Erik_BOD_Updated/_BOD - Exec Summary and TOC]]

---

## OVERVIEW

Plumbing systems provide domestic water service, fire protection water supply, and sanitary/storm drainage. Zero water consumption for cooling operations (air-cooled chillers eliminate evaporative losses).

**Design Philosophy:**
- **Zero cooling water:** Air-cooled chillers, closed-loop glycol (WUE <0.5 L/kWh)
- **Minimal domestic use:** Staff amenities only (~20 occupants)

**Scope Note:** All chilled water piping, glycol systems, and cooling loop equipment are scoped under **Division 23 (HVAC)**. Division 22 provides domestic water service only, including stub connections for makeup water to HVAC glycol systems.

---

## DOMESTIC WATER SERVICE

### Water Demand Analysis

**Domestic Use:**
- Restrooms: 6-8 fixtures (staff + visitors)
- Break rooms: Sinks, dishwasher, ice maker
- Showers/lockers: 2-4 shower stalls (24/7 operations support)
- **Estimated demand:** 500-1,000 gallons/day (10-20 occupants)

**One-Time Fill Requirements:**
- Fire sprinkler system: 8,000-15,000 gallons (wet pipe areas)
- HVAC glycol system makeup water: Provided via domestic water stub connections (HVAC contractor to connect and fill)
- **Total initial fill (Plumbing scope):** ~8,000-15,000 gallons (fire sprinkler only)

### Service Specifications

**Municipal Connection:**
- **Service size:** 3-4" water main
- **Pressure required:** 60-80 psi at building entry
- **Meter:** 3" compound meter with remote reading
- **Backflow prevention:** Reduced pressure zone (RPZ) backflow preventer per IPC

**If Municipal Service Unavailable:**
- On-site well system (capacity: 50-100 GPM)
- Pressure tank and booster pumps
- Water quality testing and treatment as required
- Backup well for redundancy (if mission-critical)

**Water Quality:**
- Filtration: 5-micron cartridge filters at building entry
- Softening: If hardness >150 ppm (protects fixtures, humidifiers)
- Testing: Annual water quality analysis

---

## SANITARY SEWER & WASTEWATER

### Wastewater Generation

**Domestic Wastewater:**
- Restrooms, showers, break room sinks
- **Flow:** 500-1,000 gallons/day average
- **Peak:** 2,000 gallons/day (shift change, events)

**No Process Wastewater:**
- Closed-loop cooling (no blowdown or discharge)
- No cooling tower makeup or bleed-off
- No industrial processes

### Service Requirements

**Municipal Sewer Connection:**
- **Pipe size:** 6" sanitary sewer lateral
- **Invert depth:** Per local utility requirements
- **Cleanouts:** Every 100 ft, at direction changes

**If Municipal Sewer Unavailable:**
- On-site septic system per Oklahoma DEQ
- Sized for 2,000 gallons/day peak flow
- Leach field area: ~5,000-8,000 SF
- Permitting: Oklahoma DEQ approval required

**Grease Management:**
- No grease trap required (no commercial kitchen)
- Break room sink only (minimal grease load)

---

## STORM DRAINAGE

### Roof Drainage

**System Type:** Interior roof drains with overflow scuppers

**Sizing:**
- Design storm: 100-year, 1-hour duration (Oklahoma)
- Rainfall intensity: [ROM] 5-6 inches/hour
- Roof area: 50,000 SF
- Primary drains: [ROM] 8-12 × 6" drains
- Overflow: Scuppers at roof edge (backup)

**Routing:**
- Interior storm leaders (insulated in conditioned spaces)
- Discharge to site storm system (away from building)
- No discharge into sanitary sewer

### Site Stormwater Management

**Detention/Retention:**
- Detention pond(s) sized per Oklahoma DEQ stormwater permit
- Capacity: [ROM] 50,000-100,000 CF (varies by site grading)
- Outlet control structure (restricts discharge to pre-development rates)

**Low-Impact Development (LID):**
- Permeable paving in parking areas (if feasible)
- Bioswales and rain gardens for water quality treatment
- Native landscaping reduces irrigation demand

**Erosion Control:**
- During construction: Silt fences, sediment basins per SWPPP
- Permanent: Vegetated slopes, riprap at outfalls

---

## PLUMBING FIXTURES & EQUIPMENT

### Restrooms

**Fixtures:**
- Water closets: Low-flow (1.28 GPF), ADA-compliant
- Urinals: 0.5 GPF or waterless
- Lavatories: 0.5 GPM sensor-activated faucets
- Janitor sinks: 1 per floor (utility sink)

**Configuration:**
- 2 × restroom groups (men's + women's + unisex/ADA)
- Capacity: ~10-15 simultaneous occupants

### Break Rooms

**Equipment:**
- Sinks: 2-3 sinks, 1.5 GPM faucets
- Dishwasher: Residential-grade (low-flow)
- Ice maker: Self-contained (30-50 lb/day)
- Coffee/beverage: Point-of-use water filter

### Showers & Lockers

**Purpose:** Support 24/7 operations, on-call engineers

**Facilities:**
- 2-4 shower stalls (private, ADA-accessible)
- 10-15 lockers
- Changing area with benches
- **Flow:** 2.0 GPM low-flow showerheads

**Drainage:** Dedicated drain line to sanitary sewer

### Emergency Fixtures

**Eyewash/Safety Showers:**
- Required at chemical storage area (glycol, water treatment chemicals)
- Required in mechanical rooms (per OSHA 1910.151)
- **Flow:** 3 GPM eyewash, 20 GPM safety shower (ANSI Z358.1)

---

## DOMESTIC HOT WATER

### System Configuration

**Heat Source:** Electric water heaters (no gas available)

**Equipment:**
- 2 × 80-gallon electric water heaters (N+1 redundancy)
- 120°F setpoint (tempered to 110°F at fixtures)
- Recirculation pumps for instant hot water

**Distribution:**
- Insulated copper piping (Type L)
- Recirculation loop with thermostatic controls
- Expansion tank

**Energy Efficiency:**
- Heat pump water heaters (if suitable)
- Timer controls (reduce standby losses during low-occupancy)

---

## SCOPE CLARIFICATION - DIVISION 22 vs DIVISION 23

**Critical Note:** To prevent scope gaps and bid-day confusion, this section clarifies the boundary between Division 22 (Plumbing) and Division 23 (HVAC) scopes.

### Division 22 (Plumbing) INCLUDES:

**Domestic Water Systems:**
- Municipal water service connection (3-4" service lateral, meter, backflow preventer)
- If municipal unavailable: On-site well system with pressure tanks and booster pumps
- Domestic water distribution piping to all plumbing fixtures
- Water softening/filtration equipment (if required)
- Makeup water stub connections (3/4" isolation valve + union) at HVAC glycol system locations (3 locations)

**Sanitary Waste Systems:**
- Sanitary sewer lateral connection (6" to municipal system or on-site septic)
- All sanitary waste piping from fixtures to building lateral
- Vent piping for drainage system
- Cleanouts and access points

**Storm Drainage Systems:**
- Roof drains (8-12 primary drains)
- Overflow scuppers
- Interior storm leaders
- Connection to site storm system (coordinate with civil)

**Plumbing Fixtures & DHW:**
- All plumbing fixtures (toilets, urinals, lavatories, sinks, showers)
- Domestic hot water system (2 × 80-gal electric water heaters, recirculation pumps, distribution)
- Emergency eyewash/safety shower stations (even if located in mechanical rooms)

**Piping & Insulation:**
- All domestic water piping (hot and cold)
- All sanitary waste and vent piping
- All storm drainage piping
- Insulation for domestic water piping per energy code

### Division 22 (Plumbing) DOES NOT INCLUDE:

**Chilled Water & Glycol Systems (Division 23 Scope):**
- All chilled water piping (Loops 1, 2, and 3)
- Overhead chilled water manifolds in data halls
- Quick-disconnect fittings for CDU or RDHx connections
- Glycol systems 
- Chemical treatment systems (dosing pots, inhibitors)
- Expansion tanks, air separators, dirt separators for chilled water loops
- Water quality testing/treatment for HVAC systems
- Leak detection systems for chilled water piping or equipment
- Piping insulation for chilled water systems

**Coordination Point:**
- Division 22 shall provide 3/4" domestic water stub connections (with isolation valve + union) at locations indicated by HVAC contractor
- HVAC contractor shall connect makeup water from these stubs to their glycol mix tanks
- HVAC contractor is responsible for all glycol system fill operations, testing, and commissioning

---

## CODES AND STANDARDS

- **IPC 2021** (International Plumbing Code), Oklahoma amendments
- **UPC** (Uniform Plumbing Code) if adopted locally
- **ASHRAE 188** (Legionella risk management for building water systems)
- **EPA SPCC** (Spill Prevention, Control, and Countermeasure) for glycol storage >1,320 gallons
- **ANSI Z358.1** (Emergency eyewash and shower equipment)
- **Oklahoma DEQ** (Stormwater, septic system regulations)


---

## EQUIPMENT AND COST SUMMARY


### Cost Summary (Rough Order of Magnitude)

**Pricing Methodology:** Hybrid approach combining systems-based parametric pricing for distribution piping and bottom-up equipment pricing for discrete items. ROM estimates suitable for BOD-level budgeting (±25-30% accuracy).

| Category                           | Description                                                                         | Cost         |
| ---------------------------------- | ----------------------------------------------------------------------------------- | ------------ |
| **Domestic Water Systems**         | Service connection, meter, RPZ, filtration, distribution piping, makeup water stubs | $85,000      |
| **Sanitary & Storm**               | Sewer lateral, waste/vent piping, roof drains, storm leaders, site connections      | $100,000     |
| **Fixtures & DHW**                 | Toilets, sinks, showers, accessories, water heaters, recirculation system           | $80,000      |
| **Testing & PM**                   | Commissioning, water quality testing, general conditions, contractor markup         | $85,000      |
| **TOTAL - DIVISION 22 (PLUMBING)** |                                                                                     | **$350,000** |

**Contingency Items (if needed):**
- Well system: $75,000 (if municipal water unavailable)
- Septic system: $65,000 (if municipal sewer unavailable)

**Excluded from This Estimate:**
- HVAC chilled water systems (Division 23 scope - see HVAC BOD)
- Fire protection piping (Division 21 scope)
- Electrical work for pumps, water heaters (Division 26 scope)
- Site civil work beyond building connection points

---

**Next Steps:**
1. Confirm municipal water/sewer availability via utility coordination
2. Design glycol mix stations and bulk storage
3. Detail leak detection routing and zones
4. Coordinate eyewash/safety shower locations with OSHA compliance review
5. Stormwater permit application (Oklahoma DEQ)

---

**Document Control:**
- **Source:** Erik_BOD reference
- **Date Updated:** October 29, 2025
- **Key Updates:**
