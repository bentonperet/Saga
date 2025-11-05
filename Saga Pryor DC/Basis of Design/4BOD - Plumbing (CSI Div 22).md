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
- **Minimal domestic use:** Staff amenities only (~10-20 occupants)
- **Sustainable design:** Stormwater management, low-flow fixtures

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

## NATURAL GAS (IF AVAILABLE)

**Potential Uses:**
- Emergency generator fuel (if dual-fuel capability desired)
- Space heating (if needed for office areas)

**Service:**
- Coordinate with local gas utility for availability
- If unavailable: All-electric building design

---

## SCOPE CLARIFICATION - DIVISION 22 vs DIVISION 23

**Critical Note:** To prevent scope gaps and bid-day confusion, this section clarifies the boundary between Division 22 (Plumbing) and Division 23 (HVAC) scopes.

### Division 22 (Plumbing) SHALL INCLUDE:

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

### Division 22 (Plumbing) SHALL NOT INCLUDE:

**Chilled Water & Glycol Systems (Division 23 Scope):**
- ❌ All chilled water piping (Loops 1, 2, and 3)
- ❌ Overhead chilled water manifolds in data halls
- ❌ Quick-disconnect fittings for CDU or RDHx connections
- ❌ Glycol storage tanks (3 × 500-gal tanks)
- ❌ Glycol fill pumps and fill stations
- ❌ Chemical treatment systems (dosing pots, inhibitors)
- ❌ Expansion tanks, air separators, dirt separators for chilled water loops
- ❌ Water quality testing/treatment for HVAC systems
- ❌ Leak detection systems for chilled water piping or equipment
- ❌ Piping insulation for chilled water systems

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

## SUSTAINABILITY & EFFICIENCY

### Water Usage Effectiveness (WUE)

**Target: <0.5 L/kWh**
- Air-cooled chillers: Zero evaporative cooling water
- Closed-loop glycol: Minimal makeup (<200 gal/year)
- Domestic water only: Staff use (~500-1,000 gal/day)

**Comparison:**
- Traditional data centers: 1.8 L/kWh (cooling towers)
- Pryor DC: <0.5 L/kWh (air-cooled) ✓

### Low-Flow Fixtures

**Water Savings:**
- Low-flow toilets: 1.28 GPF vs. 3.5 GPF (63% reduction)
- Low-flow faucets: 0.5 GPM vs. 2.2 GPM (77% reduction)
- Low-flow showers: 2.0 GPM vs. 2.5 GPM (20% reduction)

**Annual Savings:** [ROM] 30-40% vs. standard fixtures

---

## EQUIPMENT AND COST SUMMARY

| System | Equipment | Quantity | Notes |
|--------|-----------|----------|-------|
| **Domestic Water** | 3-4" service connection | 1 | Municipal or well |
| **Backflow Prevention** | RPZ backflow preventer | 1 | Required by code |
| **Makeup Water Connections** | 3/4" stub connections | 3 | To HVAC glycol systems (HVAC to connect) |
| **Sanitary Sewer** | 6" lateral connection | 1 | Municipal or septic |
| **Water Heaters** | 80-gallon electric | 2 | N+1 redundancy |
| **Emergency Fixtures** | Eyewash/shower stations | 2-3 | Chemical storage, mech rooms |
| **Plumbing Fixtures** | Toilets, sinks, urinals | ~15-20 | Low-flow fixtures |
| **Storm Drains** | Roof drains + leaders | 8-12 | 6" interior drains |

### Cost Summary (Rough Order of Magnitude)

**Pricing Methodology:** Hybrid approach combining systems-based parametric pricing for distribution piping and bottom-up equipment pricing for discrete items. Costs are ROM estimates suitable for BOD-level budgeting (±25-30% accuracy).

**General Conditions:** Material and labor costs based on Oklahoma pricing. Assumes contractor access, normal working hours, and coordinated installation with other trades.

| System/Component | Description | Unit | Qty | Unit Cost | Extended Cost | Notes |
|------------------|-------------|------|-----|-----------|---------------|-------|
| **DOMESTIC WATER SERVICE** | | | | | | |
| Water Service Connection | 3-4" service lateral to building | LS | 1 | $18,000 | $18,000 | Assumes municipal connection within 100 ft |
| Water Meter & Vault | 3" compound meter with vault | EA | 1 | $8,500 | $8,500 | Remote reading capability |
| RPZ Backflow Preventer | 3" reduced pressure zone device | EA | 1 | $4,500 | $4,500 | Required by code |
| Well System (Allowance) | If municipal unavailable | LS | 1 | $75,000 | $0 | Contingency - only if needed |
| Water Filtration System | 5-micron cartridge filters | EA | 1 | $3,500 | $3,500 | Building entry point |
| **Subtotal - Domestic Water Service** | | | | | **$34,500** | |
| | | | | | | |
| **DOMESTIC WATER DISTRIBUTION** | | | | | | |
| Cold Water Piping | 1" - 3" copper Type L piping | LF | 800 | $45 | $36,000 | To fixtures, mechanical rooms |
| Makeup Water Stubs | 3/4" stub to HVAC glycol systems | EA | 3 | $850 | $2,550 | Isolation valve + union at 3 locations |
| Pressure Reducing Valves | PRV stations | EA | 2 | $2,200 | $4,400 | If pressure >80 psi |
| Piping Insulation | Insulation for cold water piping | LF | 800 | $8 | $6,400 | Energy code compliance |
| **Subtotal - Domestic Water Distribution** | | | | | **$49,350** | |
| | | | | | | |
| **SANITARY SEWER & VENTING** | | | | | | |
| Sanitary Sewer Lateral | 6" lateral to municipal connection | LF | 150 | $85 | $12,750 | Assumes connection within 150 ft |
| Sanitary Waste Piping | 2" - 6" PVC/ABS waste piping | LF | 600 | $35 | $21,000 | From fixtures to lateral |
| Vent Piping | 1.5" - 4" PVC vent piping | LF | 400 | $28 | $11,200 | Through roof |
| Cleanouts & Access | CO's at direction changes | EA | 8 | $450 | $3,600 | Every 100 ft + changes |
| Septic System (Allowance) | If municipal unavailable | LS | 1 | $65,000 | $0 | Contingency - 2,000 gpd capacity |
| **Subtotal - Sanitary Sewer** | | | | | **$48,550** | |
| | | | | | | |
| **STORM DRAINAGE** | | | | | | |
| Roof Drains | 6" interior roof drains | EA | 10 | $1,850 | $18,500 | Primary drains, cast iron |
| Overflow Scuppers | 6" roof edge scuppers | EA | 8 | $650 | $5,200 | Secondary overflow |
| Storm Leaders | 6" interior storm piping | LF | 400 | $55 | $22,000 | Insulated in conditioned space |
| Site Storm Connection | Connection to detention system | LS | 1 | $8,500 | $8,500 | Coordinate with civil |
| **Subtotal - Storm Drainage** | | | | | **$54,200** | |
| | | | | | | |
| **PLUMBING FIXTURES** | | | | | | |
| Water Closets | Low-flow (1.28 GPF), ADA | EA | 8 | $1,200 | $9,600 | Wall-hung or floor-mount |
| Urinals | 0.5 GPF or waterless | EA | 3 | $950 | $2,850 | Men's restrooms |
| Lavatories | 0.5 GPM sensor faucets | EA | 10 | $850 | $8,500 | ADA-compliant |
| Break Room Sinks | Stainless steel sinks | EA | 3 | $650 | $1,950 | Break rooms |
| Janitor Sinks | Utility/service sinks | EA | 2 | $800 | $1,600 | Cleaning areas |
| Shower Stalls | Low-flow (2.0 GPM) showers | EA | 4 | $2,800 | $11,200 | Private stalls with ADA access |
| Shower Accessories | Benches, grab bars, hooks | LS | 1 | $4,500 | $4,500 | Locker room finishes |
| Dishwasher Connection | Break room dishwasher | EA | 1 | $450 | $450 | Rough-in only |
| Ice Maker Connection | Break room ice maker | EA | 1 | $350 | $350 | Cold water + drain |
| **Subtotal - Plumbing Fixtures** | | | | | **$41,000** | |
| | | | | | | |
| **DOMESTIC HOT WATER** | | | | | | |
| Electric Water Heaters | 80-gal, 240V electric | EA | 2 | $3,200 | $6,400 | N+1 redundancy |
| Recirculation Pumps | With VFD controls | EA | 2 | $2,400 | $4,800 | Bronze/SS, small 3-phase |
| Expansion Tanks | DHW expansion tank | EA | 1 | $650 | $650 | ASME rated |
| Hot Water Piping | 3/4" - 1.5" copper Type L | LF | 500 | $38 | $19,000 | Supply + recirculation loop |
| Hot Water Insulation | 1" fiberglass insulation | LF | 500 | $9 | $4,500 | Energy code compliance |
| Tempering Valves | Thermostatic mixing valves | EA | 3 | $850 | $2,550 | Temper to 110°F at fixtures |
| **Subtotal - Domestic Hot Water** | | | | | **$37,900** | |
| | | | | | | |
| **EMERGENCY SAFETY FIXTURES** | | | | | | |
| Eyewash/Safety Showers | ANSI Z358.1 compliant stations | EA | 3 | $4,200 | $12,600 | Chemical storage + mech rooms |
| Freeze Protection | Heat trace for outdoor fixtures | LS | 1 | $2,500 | $2,500 | If exposed to freezing |
| **Subtotal - Emergency Fixtures** | | | | | **$15,100** | |
| | | | | | | |
| **TESTING & COMMISSIONING** | | | | | | |
| Pressure Testing | Hydrostatic testing of all systems | LS | 1 | $5,500 | $5,500 | Domestic water, DHW, gas |
| Water Quality Testing | Initial water analysis | LS | 1 | $1,200 | $1,200 | Hardness, pH, contaminants |
| Backflow Certification | RPZ annual testing/certification | EA | 1 | $350 | $350 | Initial certification |
| Disinfection & Flushing | Chlorination and flushing per ASHRAE 188 | LS | 1 | $3,500 | $3,500 | Legionella prevention |
| As-Built Documentation | Record drawings and O&M manuals | LS | 1 | $4,500 | $4,500 | Final documentation |
| **Subtotal - Testing & Commissioning** | | | | | **$15,050** | |
| | | | | | | |
| **PROJECT MANAGEMENT & MISC** | | | | | | |
| General Conditions | Bonds, insurance, mobilization | % | 8% | - | $23,500 | 8% of subtotal |
| Contractor Overhead & Profit | Markup on direct costs | % | 15% | - | $47,900 | 15% of subtotal + GC |
| **Subtotal - PM & Markup** | | | | | **$71,400** | |
| | | | | | | |
| **TOTAL - DIVISION 22 (PLUMBING)** | | | | | **$367,050** | **ROM ±25-30%** |

**Cost Breakdown by Category:**
- Domestic Water: $83,850 (23%)
- Sanitary/Storm: $102,750 (28%)
- Fixtures & DHW: $78,900 (21%)
- Testing & PM: $86,450 (24%)
- Contingency items: $140,000 (well + septic, if needed)

**Excluded from This Estimate:**
- Site civil work (grading, paving, utilities beyond building connection points)
- Stormwater detention pond (civil scope)
- HVAC chilled water systems (Division 23 scope - see HVAC BOD)
- Fire protection piping (Division 21 scope)
- Electrical work for pumps, water heaters (Division 26 scope)

**Cost Escalation Notes:**
- Costs based on 2025 pricing
- Oklahoma labor rates (~$65-85/hr skilled labor)
- If construction delayed >6 months, apply 3-4% annual escalation
- Material costs for copper piping subject to commodity price fluctuations

---

**Tags:** #pryor-dc #plumbing #domestic-water #glycol-systems #leak-detection #wue

**Next Steps:**
1. Confirm municipal water/sewer availability via utility coordination
2. Design glycol mix stations and bulk storage
3. Detail leak detection routing and zones
4. Coordinate eyewash/safety shower locations with OSHA compliance review
5. Stormwater permit application (Oklahoma DEQ)

---

**Document Control:**
- **Source:** Pryor_Bod_EVS_Rev01.md and Erik_BOD reference
- **Date Updated:** October 29, 2025
- **Prepared by:** EVS / PGCIS Team
- **Key Updates:** Glycol system details, leak detection expansion for D2C
