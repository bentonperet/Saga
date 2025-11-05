**Created:** 2025-10-29
**Updated from:** Pryor_Bod_EVS_Rev01.md

# BASIS OF DESIGN - PLUMBING
## CSI Division 22
### Pryor Data Center - PACHYDERM GLOBAL

**Parent Document:** [[Saga Pryor DC/Basis of Design/Erik_BOD_Updated/_BOD - Exec Summary and TOC]]

---

## OVERVIEW

Plumbing systems provide domestic water service, fire protection water supply, sanitary/storm drainage, and chilled water makeup for closed-loop glycol systems. Zero water consumption for cooling operations (air-cooled chillers eliminate evaporative losses).

**Design Philosophy:**
- **Zero cooling water:** Air-cooled chillers, closed-loop glycol (WUE <0.5 L/kWh)
- **Minimal domestic use:** Staff amenities only (~10-20 occupants)
- **Leak detection:** Comprehensive system protecting IT equipment
- **Sustainable design:** Stormwater management, low-flow fixtures

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
- Chilled water loops: 15,000-25,000 gallons total
  - Loops 1+2: ~5,000 gallons (Phase 1)
  - Loop 3: ~15,000 gallons (Phase 2)
- **Total initial fill:** ~25,000-40,000 gallons

**Annual Makeup (Closed-Loop Systems):**
- Chilled water makeup: <1% volume/year (leak replacement only)
- Glycol concentration maintenance: Minimal (~100-200 gallons/year)

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

## CHILLED WATER MAKEUP & TREATMENT

### Glycol System Fill (Closed-Loop)

**System Volumes:**
- **Loops 1+2 (Phase 1):** ~5,000 gallons total (includes glycol mixture)
- **Loop 3 (Phase 2):** ~15,000 gallons total (includes glycol mixture)
- **Total (Phase 2):** ~20,000 gallons total
- **Glycol concentration:** 25-30% for freeze protection

**Initial Fill Procedure:**
- Deionized or softened water only (no raw municipal water)
- Pre-mix glycol per design concentration
- Pump into system via fill stations (one per loop)
- Purge air via high-point vents, circulation
- Test concentration with refractometer

### Makeup Water System

**Equipment:**
- Glycol mix tanks (sized per system volumes, one per loop)
- Circulation pumps for mixing
- Fill connections at each chiller plant
- Totalizing flow meters (track makeup volume)

**Annual Makeup Requirements:**
- Target: <1% of system volume per year
- Typical: 100-200 gallons/year (leak replacement, expansion tank overflow)
- Alarm if makeup exceeds threshold (indicates leak)

### Water Treatment

**Chemical Treatment Program:**
- **Corrosion inhibitors:** Protect steel, copper, aluminum components
- **Biological inhibitors:** Prevent algae/bacteria growth
- **pH buffers:** Maintain pH 7.5-8.5
- **Supplier:** [TBD - e.g., Nalco, ChemTreat, Kurita]

**Monitoring:**
- Quarterly testing: pH, conductivity, inhibitor concentration, glycol %
- Annual full analysis: Metals, biological activity, fluid degradation
- BMS integration: Conductivity sensors provide continuous monitoring

**Chemical Dosing:**
- Manual dosing via chemical dosing pots (CDPs)
- Sized per loop volume and chemical treatment program
- Replenish per testing schedule

### Filtration

**Side-Stream Filtration:**
- Dirt and air separators (DAS) per loop
- Removes particulates, deaerates fluid
- Replaceable cartridge filters

---

## GLYCOL STORAGE & HANDLING

### Bulk Glycol Storage

**Phase 1 Initial Fill:**
- 1,500 gallons propylene glycol (30% of 5,000 gal system)
- Delivered in 55-gallon drums or 275-gallon totes
- Storage: Outdoor chemical storage shed with secondary containment

**Phase 2 Additional:**
- 4,500 gallons propylene glycol (Loop 3)
- Bulk delivery via tanker truck (if available)
- Temporary storage in totes during fill operation

**Safety:**
- Propylene glycol: Non-toxic, food-grade (safe for data center environment)
- SDS (Safety Data Sheets) on-site
- Spill kit and containment equipment

### Fill Stations

**One Fill Station per Loop (3 Total):**
- Location: Near each chiller plant
- Equipment: Hose connection, isolation valves, drain
- Pump: Portable transfer pump (200-300 GPM)
- Venting: High-point manual air vents during fill

---

## WATER LEAK DETECTION SYSTEM

Critical for protecting IT equipment from water damage.

### Detection Zones

**Data Hall Coverage:**
- Under all overhead chilled water piping
- At all cabinet D2C manifold connections (Phase 2)
- Under CDU units (Phase 2)
- At mechanical room penetrations

**Mechanical Room Coverage:**
- Under pumps, valves, heat exchangers
- At chiller connections
- Near expansion tanks, fill stations

### Detection Technology

**Sensing Cable:**
- Conductive fluid detection cable (continuous sensing)
- Detects water, glycol, or other conductive fluids
- Length: [ROM] 1,000-2,000 ft per data hall

**Spot Detectors:**
- Discrete leak detectors at high-risk points
- Under each CDU (60 detectors in Phase 2)
- At quick-disconnect fittings
- Response time: <1 second

**Control Panels:**
- 2 × leak detection control panels (redundant)
- BACnet/IP integration to BMS
- Audible/visual local alarms

### Alarm Response

**Automatic Actions:**
1. BMS alarm (visual + audible in NOC)
2. Email/SMS to on-call engineer
3. DCIM integration (log event, track location)
4. Optional: Close isolation valves if leak zone can be isolated

**Manual Response:**
1. Maintenance team dispatched within 15 minutes
2. Locate leak via sensing cable zone indication
3. Isolate affected loop/cabinet if possible
4. Repair and refill system

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
| **Sanitary Sewer** | 6" lateral connection | 1 | Municipal or septic |
| **Glycol Mix Tanks** | 500-gallon tanks | 3 | One per loop (1, 2, 3) |
| **Fill Pumps** | Transfer pumps | 3 | 200-300 GPM portable |
| **Water Heaters** | 80-gallon electric | 2 | N+1 redundancy |
| **Leak Detection Cable** | Conductive sensing cable | 2,000-3,000 ft | Data halls + mech rooms |
| **Leak Spot Detectors** | Discrete detectors | 100+ | CDUs, valves, pumps |
| **Emergency Fixtures** | Eyewash/shower stations | 2-3 | Chemical storage, mech rooms |

<!-- @claude add a cost summary table here -->

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
