**Created:** 2025-10-23 10:25

# BASIS OF DESIGN - PLUMBING
## CSI Division 22
### Saga Energy – Pryor Data Center

**Parent Document:** [[Saga Pryor DC/Basis of Design/Benton_BOD/_BOD - Exec Summary and TOC]]
**Related:** [[Basis of Design - Part 1 Core Systems]] | [[Saga Pryor DC/Basis of Design/Benton_BOD/11BOD - Utilities DC Critical (CSI Div 33)]]

---

## OVERVIEW
Plumbing systems support domestic use, fire suppression fill, and chilled water makeup. Zero water consumption for cooling (closed-loop air-cooled system).

---

## DOMESTIC WATER SERVICE

### Water Demand
- **Domestic Use:** Restrooms, break room, showers
  - Estimated: ~500-1,000 gallons/day (5-10 staff on-site)
- **Fire Suppression Fill:** One-time fill for sprinkler system (if wet pipe used)
  - Estimated: 5,000-10,000 gallons (one-time)
- **Cooling System Fill:** One-time fill for chilled water loop
  - Estimated: 5,000-8,000 gallons (closed-loop, minimal makeup)

### Service Requirements
- **Supply:** Municipal water or on-site well (TBD via site study)
- **Pressure:** 60-80 psi minimum at building entry
- **Meter Size:** 2-3" meter (adequate for domestic flow + fire system fill)
- **Backflow Prevention:** Reduced pressure backflow preventer (RP) required by code

**Action Required:** Confirm water service availability via Water & Wastewater Availability Study (see [[Saga Pryor DC/Basis of Design/Benton_BOD/11BOD - Utilities DC Critical (CSI Div 33)]])

---

## SANITARY SEWER & WASTEWATER

### Wastewater Flow
- **Domestic Wastewater:** ~500-1,000 gallons/day (restrooms, break room, showers)
- **Process Wastewater:** None (closed-loop cooling, no blowdown or discharge)

### Service Requirements
- **Connection:** Municipal sanitary sewer or on-site septic system (TBD via site study)
- **Pipe Size:** 4-6" sanitary sewer lateral
- **Grease Trap:** Not required (break room sink only, no commercial kitchen)

**Action Required:** Confirm sanitary sewer availability via local wastewater authority. If unavailable, design on-site septic system per Oklahoma DEQ requirements.

---

## CHILLED WATER MAKEUP & TREATMENT

### Closed-Loop System
- **Initial Fill:** ~5,000-8,000 gallons (one-time)
- **Annual Makeup:** <1% of system volume per year (leak replacement only)
- **Source:** Domestic water service (filtered and treated before entering chilled water loop)

### Water Treatment System
- **Chemical Dosing:** Corrosion inhibitors, biological growth inhibitors, pH buffers
  - Equipment: 2× 8L chemical dosing pots (CDP)
- **Filtration:** Side-stream filters to remove particulates
  - Equipment: 2× dirt & air separators (DAS)
- **Monitoring:** Conductivity, pH, dissolved oxygen sensors (integrated with BMS)

### Chemical Storage
- **Location:** Mechanical room or outdoor chemical storage shed
- **Containment:** Secondary containment per EPA SPCC requirements (if >55 gallons)

---

## WATER LEAK DETECTION SYSTEM

Critical to protect IT equipment and enable rapid response to water system failures.

### Leak Detection Zones
- **Data Hall:** Under all chilled water piping (overhead routing)
- **CDU Connections:** Under all liquid-cooled rack connections
- **Quick-Connect Fittings:** Under all RDHx and CDU fittings
- **Mechanical Rooms:** Near pumps, valves, heat exchangers

### Detection Technology
- **Sensing Cable:** Conductive fluid detection cable (detects water presence)
- **Spot Detectors:** Discrete leak detectors at high-risk locations (under CDUs, valves)
- **Integration:** All leak alarms integrated with BMS and DCIM (immediate NOC notification)

### Response Procedures
Leak alarm triggers:
1. Audible/visual alarm in NOC
2. Automatic alert to on-call engineer (SMS/email)
3. Automatic isolation valve closure (if leak in specific zone can be isolated)
4. Maintenance team dispatched to locate and repair

---

## STORMWATER MANAGEMENT

### Site Drainage
- **Detention Pond:** Relocated to southeast perimeter (horseshoe/moat configuration)
- **Configuration:** Wraps around southeast and east sides of facility
- **Purpose:**
  - Required stormwater detention capacity per Oklahoma DEQ
  - Frees space for data center building expansion
  - Creates aesthetic moat feature around facility
- **Design:** Sized per Oklahoma stormwater permit requirements

### Low-Impact Development
- **Features:** Permeable paving, bioswales, rain gardens where feasible
- **Site Grading:** Directs runoff away from critical equipment areas

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

## PLUMBING FIXTURES & EQUIPMENT

### Staff Amenities
- **Restrooms:** ADA-compliant fixtures, low-flow toilets/faucets
- **Break Room:** Sink, refrigerator, microwave (no commercial kitchen)
- **Showers & Lockers:** ~700 SF shower/locker room (supports 24/7 operations)
  - Cost Impact: +$140-175K

### Emergency Fixtures
- **Eyewash/Shower:** If required by OSHA for chemical handling (mechanical room, chemical storage area)

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

## COST IMPACTS

| System | Cost Estimate |
|---|---|
| Domestic water service connection | TBD (site-specific) |
| Sanitary sewer connection | TBD (site-specific) |
| Chilled water treatment system | ~$50-100K |
| Leak detection system | ~$75-150K |
| Stormwater detention pond | ~$200-500K |
| Shower/locker facilities | +$140-175K |

---

**Tags:** #saga-project #plumbing #water-systems #leak-detection #csi-division-22

**Related Documents:**
- [[Saga Pryor DC/Basis of Design/Benton_BOD/_BOD - Exec Summary and TOC]] - Main title page
- [[Saga Pryor DC/Basis of Design/Benton_BOD/5BOD - HVAC (CSI Div 23)]] - Chilled water system details
- [[Saga Pryor DC/Basis of Design/Benton_BOD/11BOD - Utilities DC Critical (CSI Div 33)]] - Water/sewer availability
