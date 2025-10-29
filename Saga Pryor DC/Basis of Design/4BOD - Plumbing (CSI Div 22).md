**Created:** 2025-10-23 10:25

# BASIS OF DESIGN - PLUMBING
## CSI Division 22
### Saga Energy – Pryor Data Center

**Parent Document:** [[_BOD - Exec Summary and TOC]]
**Related:** [[Basis of Design - Part 1 Core Systems]] | [[11BOD - Utilities DC Critical (CSI Div 33)]]

---

## OVERVIEW
Plumbing systems support domestic use, fire suppression fill, and chilled water makeup. Zero water consumption for cooling (closed-loop air-cooled system).

---

## DOMESTIC WATER SERVICE

### Water Demand Summary
- **Domestic Use:** 500-1,000 gallons/day (restrooms, break room, showers for 5-10 staff)
- **Fire Suppression Fill:** 5,000-10,000 gallons one-time fill
- **Cooling System Fill:** 12,000-15,000 gallons one-time (Phase 1), 24,000-30,000 gallons (Ultimate)
- **Annual Makeup:** <1% of chilled water system volume (~150-300 gallons/year for leaks)

### Service Requirements
- **Supply Source:** Municipal water or on-site well (TBD via site utility study)
- **Service Pressure:** 60-80 psi minimum at building entry point
- **Service Size:** 2-3" water service line (adequate for domestic flow + fire system fill rate)
- **Meter:** 2-3" compound meter with remote reading capability
- **Backflow Prevention:** Reduced pressure backflow preventer (RPBP) per IPC and local code
- **Pressure Booster:** Not anticipated (adequate municipal pressure assumed, TBD in detailed design)

**Site Coordination:** Confirm water service availability and capacity via Water & Wastewater Availability Study (see [[11BOD - Utilities DC Critical (CSI Div 33)]])

---

## SANITARY PLUMBING & WASTEWATER (Detailed Design Phase)

**Note:** This section to be fully developed during detailed design phase. Key requirements flagged below.

### Sanitary Wastewater Flow
- **Domestic Wastewater:** ~500-1,000 gallons/day (restrooms, break room, showers for 5-10 staff)
- **Process Wastewater:** None (closed-loop cooling, no blowdown or discharge)

### Service Requirements (TBD in Detailed Design)
- **Connection:** Municipal sanitary sewer or on-site septic system (confirm via site utility study)
- **Pipe Size:** 4-6" sanitary sewer lateral (fixture unit calculation in detailed design)
- **Grease Trap:** Not required (break room sink only, no commercial kitchen)
- **Cleanouts:** Per IPC code requirements

### Sanitary Fixtures & Pipe Sizing (Detailed Design)
- Fixture unit calculations per IPC Table 702.1
- Vent sizing per IPC Chapter 9
- Trap sizing and cleanout locations per IPC requirements

**Site Coordination:** Confirm sanitary sewer availability via local wastewater authority. If unavailable, design on-site septic system per Oklahoma DEQ requirements (see [[11BOD - Utilities DC Critical (CSI Div 33)]]).

---

## CHILLED WATER MAKEUP & TREATMENT

### System Overview
The chilled water system is a **closed-loop, air-cooled architecture** requiring only one-time fill and minimal annual makeup for leak replacement. Water treatment is critical to prevent corrosion, scale formation, and biological growth that would degrade heat transfer efficiency and equipment life.

### Chilled Water System Sizing
- **Phase 1 Volume:** ~12,000-15,000 gallons total system volume
  - Chillers: ~1,200 gal (3× chillers @ 400 gal each)
  - Piping & headers: ~8,000-10,000 gal (estimated based on distribution routing)
  - CDUs & RDHx: ~2,000-3,000 gal
  - Expansion tanks & buffer: ~1,000-2,000 gal
- **Ultimate Volume:** ~24,000-30,000 gallons (Phase 5 buildout)

### Makeup Water Requirements
- **Initial Fill:** 12,000-15,000 gallons (Phase 1), 24,000-30,000 gallons (Ultimate)
- **Annual Makeup:** <1% of system volume per year = 150-300 gallons/year
- **Makeup Source:** Municipal water via domestic water service
- **Makeup Treatment:** Filtered and chemically treated before entering chilled water loop

### Water Treatment Chemistry (Municipal Water Source)

**Municipal Water Quality Assumptions (Typical Oklahoma):**
- Hardness: 150-250 ppm as CaCO₃ (moderately hard)
- Total Dissolved Solids (TDS): 200-400 ppm
- pH: 7.0-8.5
- Chlorine: 0.5-2.0 ppm (requires neutralization)
- Iron: <0.3 ppm (low)

**Treatment Requirements for Closed-Loop Chilled Water:**

| **Treatment Goal** | **Method** | **Chemical/Equipment** |
|---|---|---|
| **Corrosion Inhibition** | Filming amine or nitrite/molybdate inhibitor | Liquid corrosion inhibitor, dosed to 200-500 ppm |
| **Scale Prevention** | Sequestering agent or pH control | Phosphate-based scale inhibitor |
| **Biological Growth Control** | Biocide (non-oxidizing) | Quarterly slug dose or continuous low-level feed |
| **pH Buffering** | Maintain pH 8.5-9.5 for optimal corrosion protection | Caustic soda (NaOH) or pH buffer |
| **Oxygen Removal** | Closed system + nitrogen blanket (optional) | Chemical oxygen scavenger (sodium sulfite) |
| **Particulate Removal** | Filtration on initial fill and side-stream | 20-50 micron strainer/filter |

**Chemical Dosing Strategy:**
- **Initial Fill Treatment:** Add full dose of corrosion inhibitor, biocide, and pH buffer during system fill
- **Quarterly Monitoring:** Test conductivity, pH, inhibitor levels, bacteria count
- **Annual Adjustment:** Add makeup chemicals as needed based on test results
- **Continuous Monitoring:** Automated conductivity and pH sensors (BMS-integrated) with alarm on out-of-range

### Water Treatment Equipment

| **Equipment** | **Qty** | **Function** | **Specifications** |
|---|---|---|---|
| **Chemical Dosing Pot (CDP)** | 2-3 | Inject corrosion inhibitors, biocides, pH buffers into system | 8L capacity, 316SS construction, isolation valves |
| **Dirt & Air Separator (DAS)** | 2 | Remove particulates and entrained air from chilled water loop | Horizontal configuration, sized for system flow (600-1,200 GPM) |
| **Side-Stream Filter** | 1 | Continuous particulate removal (10% of system flow) | 20-50 micron cartridge or bag filter, 60-120 GPM |
| **Conductivity Sensor** | 2 | Monitor TDS and chemical concentration | 4-20mA output to BMS, alarm on high/low |
| **pH Sensor** | 2 | Monitor pH (target 8.5-9.5) | 4-20mA output to BMS, alarm on out-of-range |
| **Makeup Water Meter** | 1 | Track annual makeup water volume (detect leaks) | Pulse output to BMS for totalizing |

### Chemical Storage & Handling
- **Storage Location:** Mechanical room or outdoor chemical storage shed (weather-protected)
- **Containment:** Secondary containment per EPA SPCC requirements (if total storage >55 gallons)
- **Drum Storage:** 55-gallon drums on spill pallets with containment (corrosion inhibitor, biocide)
- **Safety:** Eyewash/shower station if concentrated chemicals handled (OSHA requirement)
- **Labeling:** All chemicals labeled per OSHA Hazard Communication Standard (HCS)

### Monitoring & Maintenance Protocol
- **Quarterly Water Analysis:** Sample chilled water for pH, conductivity, inhibitor level, bacteria count
- **Annual System Flush:** Not required for closed-loop (initial fill flush only)
- **Chemical Adjustment:** Based on quarterly test results, adjust inhibitor/biocide levels
- **Leak Detection:** Monitor makeup water meter totalizer; >500 gal/year indicates leak requiring investigation

---

## WATER LEAK DETECTION SYSTEM

### System Purpose
Protect IT equipment from water damage and enable rapid response to chilled water system leaks. Early detection minimizes downtime and equipment damage.

### Leak Detection Zones

| **Zone** | **Detection Method** | **Coverage** | **Alarm Action** |
|---|---|---|---|
| **Data Hall Overhead Piping** | Sensing cable along pipe runs | 100% of chilled water distribution piping | NOC alarm + BMS notification |
| **CDU Base Pans** | Spot detectors in drip pans | All CDU locations (9-12 units) | Zone-specific alarm, identify unit |
| **RDHx Quick-Connect Fittings** | Spot detectors below each connection | All rack quick-connects (48 racks) | Rack-level alarm, identify location |
| **Mechanical Room Equipment** | Sensing cable + spot detectors | Pumps, heat exchangers, valves, expansion tanks | Equipment-specific alarm |
| **Chiller Yard** | Spot detectors at chiller connections | All outdoor chiller evaporator connections (16 units) | Chiller ID alarm |
| **Pipe Penetrations** | Spot detectors at floor/wall penetrations | All building penetrations for CHW piping | Penetration location alarm |

### Detection Technology Specifications

**Sensing Cable (Primary Detection):**
- **Type:** Conductive fluid sensing cable (detects water, glycol, or other fluids)
- **Technology:** Resistive or capacitive sensing along entire cable length
- **Sensitivity:** Detects fluid presence within 10-30 seconds of contact
- **Coverage:** Install along full length of overhead piping runs
- **Mounting:** Clipped to pipe hangers or cable tray, positioned below piping
- **Zoning:** Divided into addressable zones (identify location within ~20-50 ft)
- **Interface:** 4-20mA or digital output to BMS/DCIM via leak detection panel

**Spot Detectors (Point Detection):**
- **Type:** Discrete leak detectors with conductivity sensors
- **Locations:** CDU drip pans, rack quick-connects, pump bases, valve groups
- **Sensitivity:** Detect water presence immediately upon contact
- **Mounting:** Floor-mounted or in drip pans/catch basins
- **Addressable:** Each detector has unique ID for precise location identification
- **Interface:** Wired to leak detection panel, integrated with BMS

**Leak Detection Control Panel:**
- **Function:** Centralized monitoring and alarm reporting for all leak detection zones
- **Capacity:** Support 50-100 zones/points (Phase 1), expandable to 200+ (Ultimate)
- **Power Supply:** 120V with battery backup (maintain alarm capability during power loss)
- **Outputs:** Dry contact relays for NOC alarm panel, BACnet/IP to BMS, SNMP to DCIM
- **Display:** Local LCD display showing active alarms with zone identification

### Alarm & Response Procedures

**Tier 1 Alarm (Data Hall or CDU/RDHx Leak):**
1. **Immediate Actions:**
   - Audible/visual alarm activates in NOC
   - BMS sends SMS/email alert to on-call facilities engineer
   - DCIM flags affected rack location or zone
   - Alarm log timestamp and zone ID recorded
2. **Response (Within 5-15 minutes):**
   - NOC staff or on-call engineer investigates alarm location
   - Visual inspection to confirm leak vs false alarm
   - If leak confirmed → isolate zone via manual isolation valves
3. **Remediation:**
   - Identify leak source (fitting, valve, pipe joint)
   - Repair or replace failed component
   - Clean up water, verify no IT equipment damage
   - Reset leak detector and return zone to service

**Tier 2 Alarm (Mechanical Room or Chiller Yard Leak):**
1. **Immediate Actions:** Same as Tier 1
2. **Response:** Less urgent (no immediate IT equipment risk), respond within 30-60 minutes
3. **Remediation:** Repair leak, monitor system pressure/makeup water

**Automatic Isolation (Optional, High-Risk Zones):**
- **Motorized Isolation Valves:** Consider motorized ball valves on CDU supply lines
- **Interlock Logic:** If leak detected in CDU zone → close motorized valve to that CDU
- **Manual Override:** Bypass switch to prevent unintended isolation
- **Trade-off:** Adds cost/complexity, but minimizes water release in high-risk areas

### System Integration
- **BMS Integration:** All leak alarms reported to BMS via BACnet/IP or Modbus
- **DCIM Integration:** Leak alarms mapped to physical rack/equipment locations
- **NOC Alarm Panel:** Visual/audible alarm panel in NOC with zone annunciation
- **Historical Logging:** All leak events logged with timestamp, zone, and duration

---

## STORMWATER MANAGEMENT (Detailed Design & Civil Engineering)

**Note:** Stormwater system design to be completed by civil engineer during detailed design phase. Key requirements flagged below.

### Site Drainage Strategy
- **Detention Pond:** Relocated to southeast perimeter (horseshoe/moat configuration per Oct 2025 design update)
- **Configuration:** Wraps around southeast and east sides of facility
- **Purpose:**
  - Required stormwater detention capacity per Oklahoma DEQ
  - Frees space for data center building expansion
  - Creates aesthetic moat feature around facility
- **Design Basis:** Sized per Oklahoma stormwater permit requirements (detailed calculations in civil design)

### Low-Impact Development (LID) Features
- **Features (TBD):** Permeable paving, bioswales, rain gardens where feasible
- **Site Grading:** Directs runoff away from critical equipment areas (chillers, electrical enclosures)

### Detailed Design Coordination
- Civil engineer to provide detention pond sizing calculations, outlet structure design, emergency spillway
- Oklahoma DEQ stormwater permit application and approval
- Coordinate pond location with chiller yard and electrical equipment placement

**Updated (Oct 2025):** Pond relocated from original position to optimize site layout. See [[Architectural Meeting Changes by CSI Division]].

---

## ZERO WATER COOLING STRATEGY {TBC}

### Air-Cooled Chilled Water System
- **Chiller Type:** Air-cooled chillers with integrated free cooling
- **Water Consumption:** **~0 gallons/year for cooling** (closed-loop, no evaporation)
- **Only water use:** Domestic (staff use) and one-time chilled water fill

### Deviation from RD109 Baseline
- **RD109:** Included 5× adiabatic fluid coolers (evaporative pre-cooling)
- **Saga Pryor:** Eliminated adiabatic coolers
- **Rationale:**
  - Zero ongoing water cost and supply risk
  - Strong sustainability narrative (no water consumption in drought-prone region)
  - Simplified permitting (no water rights or wastewater discharge permits for cooling)

### Benefits
- **Water Savings:** ~60-80 million liters/year vs evaporative cooling
- **Industry Comparison:**
  - Traditional data centers: 1.8 liters per kWh
  - Saga Pryor: 0 liters per kWh for cooling
- **Reduced OPEX:** -$15-25K/year (water cost + treatment + maintenance)

---

## PLUMBING CODE COMPLIANCE (Detailed Design Phase)

**Note:** Detailed code compliance analysis to be completed during detailed design phase. Key applicable codes flagged below.

### Applicable Codes & Standards
- **International Plumbing Code (IPC) 2021** - Base code for Oklahoma
- **Oklahoma Plumbing Code** - State amendments to IPC
- **ASME B31.9** - Building services piping
- **ASHRAE 188** - Legionella risk management (domestic water)
- **NFPA 13** - Sprinkler system coordination (fire suppression fill)
- **EPA SPCC** - Spill Prevention Control and Countermeasures (chemical storage)

### Key Compliance Areas (Detailed Design)
- Domestic water pipe sizing per IPC Chapter 6
- Sanitary drainage and vent sizing per IPC Chapters 7-9
- Backflow prevention per IPC Chapter 6 and local water authority requirements
- Water heater sizing and safety (if required for showers)
- Accessible plumbing fixtures per ADA and IBC Chapter 11

---

## PLUMBING FIXTURES & EQUIPMENT

### Staff Amenities
- **Restrooms:** ADA-compliant fixtures, low-flow toilets/faucets per WaterSense standards
- **Break Room:** Sink, refrigerator, microwave (no commercial kitchen)
- **Showers & Lockers:** ~700 SF shower/locker room (supports 24/7 operations)
  - Cost Impact: +$140-175K (fixture allowance included)

### Emergency Fixtures
- **Eyewash/Shower:** Required by OSHA for chemical handling areas (mechanical room with chemical dosing equipment)
- **Location:** Adjacent to chemical storage area, accessible within 10 seconds per ANSI Z358.1

---

## PLUMBING EQUIPMENT SCHEDULE

### Key Plumbing Equipment (Major Cost Items)

| Equipment | Description | Qty (Phase 1) | Qty (Ultimate) |
|---|---|---|---|
| **Chemical Dosing Pot (CDP)** | 8L capacity, 316SS construction, for CHW treatment chemicals | 2 | 4 |
| **Dirt & Air Separator (DAS)** | Horizontal configuration, sized for CHW system flow (600-1,200 GPM) | 2 | 4 |
| **Side-Stream Filter** | 20-50 micron cartridge filter, 60-120 GPM, for CHW particulate removal | 1 | 2 |
| **Leak Detection Panel** | Central monitoring panel, 50-100 zone capacity, BACnet/IP interface | 1 | 2 |
| **Leak Detection Sensing Cable** | Conductive fluid sensing cable, addressable zones, full data hall coverage | 2,000 ft | 4,000 ft |
| **Leak Detection Spot Sensors** | Discrete conductivity-based leak sensors for CDUs, pumps, equipment | 30 | 60 |
| **Makeup Water Meter** | Pulse-output totalizing meter for CHW makeup water tracking | 1 | 1 |
| **Conductivity Sensor** | Inline sensor for CHW chemistry monitoring, 4-20mA output to BMS | 2 | 3 |
| **pH Sensor** | Inline sensor for CHW pH monitoring, 4-20mA output to BMS | 2 | 3 |
| **Backflow Preventer (RP)** | Reduced pressure backflow preventer for domestic water service, 2-3" size | 1 | 1 |
| **Emergency Eyewash/Shower** | ANSI Z358.1 compliant combination unit for chemical handling area | 1 | 2 |

**Note:** Fixture counts (toilets, sinks, showers) and sanitary piping to be detailed in plumbing fixture schedule during detailed design phase.

---

## KEY DESIGN DECISIONS

### Zero Water Cooling Confirmed
- Closed-loop air-cooled system eliminates ongoing water consumption
- Supports sustainability goals and reduces operational risk

### Stormwater Pond Relocated
- Moved to southeast perimeter (Oct 2025 design update)
- Optimizes site layout for expanded data center building

### Leak Detection Critical
- Extensive leak detection in data hall protects IT equipment
- Rapid response via BMS/DCIM integration minimizes damage risk

---

## COST IMPACTS & FINANCIAL ANALYSIS

**Cost Analysis Prompt for Future Detailed Work:**

```
PLUMBING SYSTEMS COST ESTIMATION PROMPT

Using the equipment schedules above and the detailed specifications throughout this BOD,
perform a comprehensive cost analysis for the plumbing systems including:

1. EQUIPMENT PRICING
   - Itemize costs for each piece of equipment listed in the schedule
   - Include installation labor, materials (pipe, valves, fittings, insulation)
   - Provide vendor quotes for specialized equipment (leak detection, water treatment)
   - Account for geographic location (Mayes County, OK / Tulsa labor market)

2. UTILITY CONNECTION COSTS (Site-Specific)
   - Domestic water service tap and lateral connection
   - Sanitary sewer lateral connection or on-site septic system
   - Fire water service (if separate from domestic)
   - Coordinate with utility availability study (Division 33)

3. VENDOR CONFIDENCE LEVELS
   - Assign confidence level (High/Medium/Low) to each line item
   - High = Recent vendor quote or comparable installation
   - Medium = Industry pricing guides with regional adjustment
   - Low = Preliminary estimate requiring detailed engineering or site study

4. WATER TREATMENT OPEX
   - Annual chemical costs (corrosion inhibitor, biocide, pH buffer)
   - Quarterly water analysis and testing
   - Makeup water cost (~150-300 gal/year @ local water rates)
   - Leak detection system maintenance and calibration

5. ZERO WATER STRATEGY VALUE
   - Quantify annual water savings vs evaporative cooling baseline
   - Compare to typical data center water consumption (1.8 L/kWh industry average)
   - Sustainability narrative value for marketing/ESG reporting

OUTPUT FORMAT:
- Detailed cost breakdown table by system and equipment type
- Confidence level assigned to each line item with justification
- Highlight site-specific costs requiring utility coordination study
- Annual OPEX projection for water treatment and monitoring
```

**Placeholder Cost Summary (Detailed Analysis Required):**

| System | Estimated Cost Range | Confidence | Notes |
|---|---|---|---|
| Domestic water service connection | TBD ($50-150K) | Low | Site-specific, requires utility study |
| Sanitary sewer connection | TBD ($50-150K) | Low | Site-specific, or on-site septic $100-200K |
| Chilled water treatment system | $50-100K | Medium | Chemical dosing, filtration, sensors |
| Leak detection system (complete) | $75-150K | Medium | Sensing cable, spot detectors, panel, installation |
| Stormwater detention pond | $200-500K | Low | Civil engineering design, site-specific |
| Shower/locker room plumbing fixtures | $140-175K | Medium | Included in facility construction estimate |
| Backflow preventer and domestic piping | $30-50K | Medium | 2-3" RP, pipe, valves, insulation |
| **Total Plumbing (excl. site utilities)** | **$495-975K** | **Medium** | Excludes utility connection costs (TBD) |

**Note:** Detailed cost analysis to be completed in separate financial modeling exercise per prompt above. Site-specific utility connection costs require coordination with Division 33 utility availability study.

---

**Tags:** #saga-project #plumbing #water-systems #leak-detection #csi-division-22

**Related Documents:**
- [[_BOD - Exec Summary and TOC]] - Main title page and facility overview
- [[5BOD - HVAC (CSI Div 23)]] - Chilled water system design, pump specifications, piping distribution
- [[6BOD - Integrated Automation (CSI Div 25)]] - BMS integration for leak detection, water quality monitoring
- [[11BOD - Utilities DC Critical (CSI Div 33)]] - Water/sewer availability study, utility connections
- [[3BOD - Fire Suppression (CSI Div 21)]] - Fire water supply requirements, sprinkler system fill
- [[10BOD - Site and Infrastructure (CSI Divs 31-32)]] - Stormwater detention pond details
- [[Architectural Meeting Changes by CSI Division]] - October 2025 updates
