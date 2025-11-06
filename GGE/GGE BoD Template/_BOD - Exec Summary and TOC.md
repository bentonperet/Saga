**Created:** 2025-11-04
**Updated from:** GGE Design Calculations with MTU Kinetic PowerPack

# BASIS OF DESIGN - CSI MASTERFORMAT
## GGE Data Center - Phase 1
### Tbilisi, Georgia

**Document Status:** REVISION 04 - MV Voltage Updated to 10kV (was 11kV)
**Prepared by:** EVS / GGE Engineering Team
**Date:** November 6, 2025
**Purpose:** Comprehensive Basis of Design for GGE Data Center Phase 1 organized by CSI Master Format
**Key Update:** Medium voltage distribution changed from 11kV to 10kV throughout

---

## EXECUTIVE SUMMARY

### **FACILITY OVERVIEW**
- **IT Capacity:** 1.47 MW Phase 1 (expandable via independent follow-on phases)
- **Generator Capacity:** 2 × 2,200 kW (4,400 kW installed, 2N redundancy)
- **White Space:** [TBD] SF data hall
- **Power Density:** [TBD] W/SF
- **Availability:** Tier III (2N generators, N+1 mechanical, concurrent maintainability)
- **Target PUE:** 1.50 design maximum, 1.30 annual average (with river free cooling)
- **Target WUE:** 0 L/kWh (zero evaporative water consumption, river cooling via closed loop)
- **Site:** Tbilisi, Georgia - 100 meters from Kura River
- **Key Differentiator:** MTU Kinetic PowerPack (integrated diesel + flywheel UPS), direct Kura River economization via indirect heat exchangers

---

---

### **MECHANICAL SYSTEMS - COOLING**

#### IT Heat Rejection
- **IT Load:** 1,467 kW (100% becomes heat)
- **Chiller electrical load:** 267 kW (included in PUE)
- **Pump electrical load:** 210 kW (all three loops, included in PUE)
- **Total condenser heat:** 1,734 kW (rejected to Kura River)

#### Water-Cooled Chiller Plant
- **Configuration:** 3 × 800 kW water-cooled chillers (N+1 redundancy)
- **Total capacity:** 2,400 kW installed
- **Running capacity:** 1,600 kW (2 units running, 1 standby)
- **Design margin:** 1,600 / 1,467 = 109% ✓
- **Chiller COP:** 5.5 (water-cooled, design condition)
- **Refrigerant:** R-134a or R-513A (low-GWP alternatives)
- **Compressor type:** Screw or centrifugal
- **Evaporator:** Produces chilled water (CHW) at 12°C supply, 18°C return (ΔT = 6°C)
- **Condenser:** Cooled by closed condenser water loop (CW) at 20-30°C supply, 30-40°C return (ΔT = 10°C)
- **Brands:** Carrier, Trane, York, Daikin (available via Turkey/Georgia distribution)
- **Location:** Indoor mechanical room (protected from weather)
- **Concurrent maintenance:** Any chiller can be isolated via isolation valves without IT impact

#### Chilled Water Distribution (Loop 1 - CHW)
- **Purpose:** Deliver cooling to data hall
- **Supply temperature:** 12°C
- **Return temperature:** 18°C
- **ΔT:** 6°C
- **Flow rate:** 3,680 L/min (972 GPM)
- **Piping:** Insulated steel or HDPE, overhead or underground distribution
- **Pumps:** 3 × CHW pumps (2 duty + 1 standby, N+1)
  - Flow: 1,840 L/min each (50% capacity)
  - Head: 35m (115 ft)
  - Power: 30 kW each
  - Drive: VFD (variable frequency drive) for variable flow
  - Total power: 60 kW running
  - **On critical power:** Fed from 400V MTU Kinetic PowerPack
- **Control:** Variable flow based on data hall return temperature

#### Condenser Water System (Loop 2 - CW - Closed Primary)
- **Purpose:** Reject heat from chillers to river heat exchangers
- **Configuration:** Closed loop (treated water, minimal makeup)
- **Supply temperature:** 20°C (winter with free cooling) to 30°C (summer)
- **Return temperature:** 30°C (winter) to 40°C (summer)
- **ΔT:** 10°C
- **Flow rate:** 4,950 L/min (1,307 GPM)
- **Piping:** DN200 (8") HDPE, insulated, buried 1.5m depth
- **Route:** Data center mechanical room → 100m → River-edge enclosure → 100m → Return
- **Total piping:** 200m (supply + return)
- **Pumps:** 3 × CW pumps (2 duty + 1 standby, N+1)
  - Flow: 2,475 L/min each (50% capacity)
  - Head: 40m (131 ft) - includes piping loss + heat exchanger pressure drop
  - Power: 45 kW each
  - Drive: VFD for variable flow
  - Total power: 90 kW running
  - **On critical power:** Fed from 400V MTU Kinetic PowerPack
  - **Location:** Data center mechanical room
- **Water treatment:** Corrosion inhibitor, biocide (annual), side-stream filtration (50 micron)
- **Bypass capability:** 3-way valves allow bypass of river heat exchangers (maintenance or summer heat rejection to atmosphere if needed)

#### River Water System (Loop 3 - RW - Open Secondary)
- **Purpose:** Cool condenser water via plate heat exchangers
- **Source:** Kura River (100m from data center)
- **Configuration:** Open loop (river water intake → filter → heat exchanger → river discharge)
- **Flow rate:** 5,500 L/min (1,453 GPM)
- **Temperature range:** 6°C (winter) to 27°C (summer)
- **Piping:** DN200 (8") HDPE, buried 1.5m depth
- **Route:** River intake → 20m → Enclosure → 20m → River discharge
- **Pumps:** 3 × River water pumps (2 duty + 1 standby, N+1)
  - Flow: 2,750 L/min each (50% capacity)
  - Head: 25m (82 ft) - includes intake lift + piping + HX pressure drop
  - Power: 30 kW each
  - Drive: VFD for variable flow
  - Total power: 60 kW running
  - **On critical power:** Fed from 400V via 100m underground cable to river enclosure
  - **Location:** River-edge enclosure (100m from data center)

#### River-Edge Enclosure & Heat Exchangers
- **Location:** 100m from data center, at Kura River bank
- **Structure:** Precast concrete vault, 8m × 5m × 3m (L × W × H interior)
- **Footprint:** 40 m² interior
- **Foundation:** Reinforced concrete, elevated 1m above 100-year flood level
- **Access:** Paved service road, lockable steel door, card reader, CCTV
- **Environmental control:** Ventilation, heating (freeze protection), drainage

**Plate Heat Exchangers (Inside Enclosure):**
- **Quantity:** 2 × 1,000 kW capacity (N+1 redundancy)
- **Total capacity:** 2,000 kW (> 1,734 kW required) ✓
- **Type:** Brazed plate, stainless steel
- **Primary side (CW - closed loop):** Condenser water from chillers
- **Secondary side (RW - river water):** Kura River water
- **Approach temperature:** 3°C (typical for plate HX)
- **Isolation:** Each HX has isolation valves for independent maintenance
- **Brands:** Alfa Laval, SWEP, Danfoss (available via Turkey/Georgia)
- **Dimensions (each):** ~1.5m × 0.8m × 1.2m (H × W × D)
- **Weight:** ~800 kg empty
- **Connections:** DN150 (6") flanged

**Filtration & Treatment:**
- **Coarse screen (at intake):** 50mm bar spacing (trash rack), removes large debris
- **Fine screen (at enclosure):** 5-10mm traveling screen, removes fish/leaves, automatic backwash
- **Automatic strainers:** 2 × 100% duty, 100-200 micron, self-cleaning backflush
- **Chemical treatment:** Minimal low-dose chlorination (~0.5 ppm intermittent) for biofouling control
- **Monitoring:** Flow, temperature, pressure differential, conductivity, pH

**Bypass & Isolation:**
- **Bypass valves:** 2 × motorized 3-way valves (DN200) on CW loop
- **Purpose:** Allow CW to bypass HX during maintenance or when river temp too high
- **Isolation valves:** 8 × butterfly valves (DN200) to isolate individual heat exchangers
- **Control:** BMS-integrated PLC logic, automatic mode switching

#### Free Cooling Optimization (Kura River Economization)
- **River temperature range:** 6°C (winter) to 27°C (summer)
- **CHW supply target:** 12°C

**Cooling Modes:**
1. **100% Free Cooling (River < 10°C):** ~5,500 hours/year (November-April)
   - Chillers OFF
   - River water cools CW to 9-13°C
   - CW produces CHW at 12°C via additional heat exchanger (or direct if compatible)
   - Energy: Pumps only (210 kW vs. 477 kW with chillers) = **56% savings**

2. **Partial Free Cooling (River 10-23°C):** ~2,000 hours/year (May, October)
   - Chillers ON at reduced load (30-70%)
   - River pre-cools condenser water
   - Energy savings: 30-50% vs. full mechanical

3. **Full Mechanical (River > 23°C):** ~1,260 hours/year (June-September)
   - Chillers ON at full load
   - River water still provides condenser cooling (more efficient than air-cooled)
   - COP: 5.5 (vs. 3.5 for air-cooled)

**Annual PUE Performance:**
- **Design maximum PUE:** 1.50 (full mechanical cooling)
- **Free cooling PUE:** 1.18 (chillers off, pumps only)
- **Annual weighted average PUE:** 1.30 (20% improvement over design)
- **Annual cooling energy savings:** $51,000/year vs. no free cooling

#### Data Hall Cooling Distribution
- **Configuration:** In-row cooling units with CHW coils
- **Quantity:** 12 × 150 kW units (N+1 distributed redundancy)
- **Total capacity:** 1,800 kW installed, 1,650 kW running
- **Supply air temp:** 18-20°C
- **Airflow:** [TBD] CFM per unit
- **Fan power:** ~50 kW total (included in PUE)
- **Brands:** Stulz, Schneider (APC), Vertiv (available in Tbilisi/Turkey)
- **Control:** BMS-integrated, modulating control based on room temperature
- **Redundancy:** Any unit can fail without IT impact

#### Building HVAC (Non-Critical Spaces)
- **Offices, NOC, support spaces:** [TBD] - Separate RTUs or split systems
- **Not on critical power**

#### Mechanical Code Compliance
- **Standards:** IMC 2021 (International Mechanical Code), ASHRAE 90.1-2019
- **Refrigerant:** F-gas regulations (EU 517/2014 as adopted in Georgia)

---

### **POWER BUDGET - PHASE 1**

| Load Category | Power (kW) | % of Total |
|---------------|------------|------------|
| **IT Load** | 1,467 | 66.7% |
| **Cooling - Chillers** | 267 | 12.1% |
| **Cooling - CHW Pumps** | 60 | 2.7% |
| **Cooling - CW Pumps** | 90 | 4.1% |
| **Cooling - River Water Pumps** | 60 | 2.7% |
| **Cooling - In-row unit fans** | 50 | 2.3% |
| **Electrical Losses (Xfmrs, distribution)** | 110 | 5.0% |
| **Lighting, BMS, controls** | 30 | 1.4% |
| **Building HVAC, offices** | 60 | 2.7% |
| **Contingency/Future** | 6 | 0.3% |
| **TOTAL FACILITY LOAD** | **2,200 kW** | **100%** |

**PUE Calculation:**
```
PUE = Total Facility Power / IT Power
PUE = 2,200 kW / 1,467 kW = 1.50 (design maximum)
```

**Infrastructure Power:**
```
Infrastructure = Total - IT = 2,200 - 1,467 = 733 kW (33.3% overhead)
```

---

### **KURA RIVER ENVIRONMENTAL IMPACT**

#### River Water Usage
- **Intake flow:** 5,500 L/min = 330,000 L/hr = 7,920,000 L/day = 7,920 m³/day
- **Annual usage:** 2,890,800 m³/year (365 days × 7,920 m³/day)
- **Note:** 100% of intake water is returned to river (closed loop, zero consumption)

#### Thermal Discharge
- **Heat rejected:** 1,734 kW = 1,734,000 W
- **Temperature rise (ΔT):** 10°C average
- **Discharge temperature:** River temp + 10°C
  - Winter: 6°C + 10°C = 16°C discharge
  - Summer: 27°C + 10°C = 37°C discharge

#### River Mixing Analysis (See detailed calculations in Section 4 below)
- **Kura River flow rate:** [TBD] m³/s (minimum low flow)
- **Discharge proportion:** [TBD]% of river flow
- **Temperature rise at 100m downstream:** [TBD]°C (complete mixing)
- **Compliance:** Georgian environmental discharge standards [TBD]

---

### **FACILITY CONSTRUCTION**

[TBD - To be determined based on site requirements]

**Structure:** [TBD] - Tilt-up concrete, PEMB, or other
**Total Building:** [TBD] GSF
**Data Hall:** [TBD] SF
**Ceiling Height:** [TBD] ft
**Floor:** [TBD] - Raised floor or slab-on-grade
**Support Spaces:** [TBD] - Offices, NOC, electrical room, mechanical room

---

### **TIER III COMPLIANCE SUMMARY**

| System | Requirement | GGE Design | Compliant |
|--------|-------------|------------|-----------|
| **Generators** | N+1 minimum | 2N (2 × 100%) | ✓ Exceeds |
| **Transformers** | N+1 minimum | 2N (2 × 100%) | ✓ Exceeds |
| **Chillers** | N+1 | 3 × 800 kW (N+1) | ✓ Yes |
| **Pumps (all loops)** | N+1 | 3 each (N+1) | ✓ Yes |
| **Concurrent Maintenance** | Any component removable | Isolation valves throughout | ✓ Yes |
| **Dual Distribution** | A/B power paths | SWBD-A + SWBD-B | ✓ Yes |
| **IT Equipment** | Dual-corded | Dual PDUs (A/B) | ✓ Yes |

**Tier III Certification:** Designed for Uptime Institute Tier III certification (concurrent maintainability, no single points of failure in distribution)

---

### **EQUIPMENT SUMMARY - PHASE 1**

| Equipment | Qty | Unit Size | Total Capacity | Redundancy | Critical Power |
|-----------|-----|-----------|----------------|------------|----------------|
| **ELECTRICAL - PRIMARY SOURCES** |
| HPP Utility Source | 1 | 3.7 MW @ 400V | 3.7 MW | Dual source | Upstream |
| Grid Utility Source | 1 | 4.0 MW @ 10 kV | 4.0 MW | Dual source | Upstream |
| HPP Step-Up Transformer | 1 | 3,500 kVA, 400V/10kV | 3.5 MVA | - | HPP path |
| MV Switchboard A (10 kV) | 1 | 630A bus | - | Redundant | HPP path |
| MV Switchboard B (10 kV) | 1 | 630A bus | - | Redundant | Grid path |
| Step-Down Transformers (10kV/400V) | 2 | 3,500 kVA | 7,000 kVA | 2N | Downstream |
| **ELECTRICAL - MTM DISTRIBUTION** |
| 400V Main Breakers (ACB-M1, M2) | 2 | 6,300A frame | - | Main | Drawout |
| 400V Tie Breaker (52-TIE) | 1 | 6,300A frame | - | N.O. | Drawout |
| 400V Main Switchboards (A, B) | 2 | 2,500A bus | - | MTM | MTU-fed |
| **ELECTRICAL - BACKUP POWER** |
| MTU KP7 Kinetic PowerPack | 2 | 2,200 kW | 4,400 kW | 2N | Self-powered |
| MTU Breakers (ACB-MTU1, MTU2) | 2 | 5,000A frame | - | - | w/ ATS |
| **ELECTRICAL - DISTRIBUTION PANELS** |
| IT Distribution Panels (A, B) | 2 | 2,500A MCCB | - | A/B | MTU-fed |
| Cooling Panels (A-COOL, B-COOL) | 2 | 3,200A MCCB | - | A/B | MTU-fed |
| **ELECTRICAL - OFFICE / SOLAR** |
| Solar Inverters | 1 set | 700 kW AC | 700 kW | - | Solar array |
| Office Transformer (11kV/400V) | 1 | 250 kVA | 250 kVA | - | Grid utility |
| Office ATS | 1 | 630A | - | - | Solar priority |
| Office Switchboard | 1 | 630A bus | - | - | Non-critical |
| **COOLING - DATA CENTER** |
| Water-Cooled Chillers | 3 | 800 kW | 2,400 kW | N+1 | Yes (400V) |
| CHW Pumps | 3 | 30 kW | 90 kW | N+1 | Yes (400V) |
| CW Pumps | 3 | 45 kW | 135 kW | N+1 | Yes (400V) |
| In-Row Cooling Units | 12 | 150 kW | 1,800 kW | N+1 | Yes (400V) |
| **COOLING - RIVER ENCLOSURE** |
| Plate Heat Exchangers | 2 | 1,000 kW | 2,000 kW | N+1 | N/A |
| River Water Pumps | 3 | 30 kW | 90 kW | N+1 | Yes (400V) |
| Automatic Strainers | 2 | 100% duty | - | 2N | No |
| 3-Way Bypass Valves | 2 | DN200 | - | - | No |
| Isolation Valves | 8 | DN200 | - | - | No |
| **PIPING** |
| CW Piping (DC to River) | 200m | DN200 | - | - | N/A |
| River Intake/Discharge | 40m | DN200 | - | - | N/A |

---

### **COST SUMMARY - PHASE 1**

| System | Cost Estimate |
|--------|---------------|
| **Electrical Systems - Critical Power** |
| 2 × MTU KP7 Kinetic PowerPack | $4,000,000 |
| HPP Step-Up Transformer (400V/10kV, 3,500 kVA) | $100,000 |
| 2 × MV Switchboards (10 kV, 630A bus, VCB lineup) | $200,000 |
| 2 × Step-Down Transformers (10kV/400V, 3,500 kVA) | $200,000 |
| 400V Main Breakers (2 × 6,300A ACB drawout) | $120,000 |
| 400V Tie Breaker (1 × 6,300A ACB drawout) | $60,000 |
| 400V Switchboards A & B (2 × 2,500A bus) | $200,000 |
| Distribution Panels (IT + Cooling, 4 total) | $160,000 |
| MTM Controller & Protection Relays | $40,000 |
| **Electrical Systems - Office / Solar** |
| Solar Array (700 kW AC, inverters + panels) | $700,000 |
| Office Transformer (250 kVA, 10kV/400V) | $25,000 |
| Office ATS (630A with solar priority) | $15,000 |
| Office Switchboard (630A bus) | $20,000 |
| **Electrical - Installation & Commissioning** |
| Installation, testing, commissioning | $385,000 |
| **Subtotal Electrical** | **$6,175,000** |
| **Cooling Systems - Data Center** |
| 3 × 800 kW Water-Cooled Chillers | $450,000 |
| CHW + CW Pumps (6 total) | $90,000 |
| 12 × In-Row Cooling Units | $360,000 |
| Piping, valves, insulation (CHW distribution) | $150,000 |
| **Subtotal Cooling (DC)** | **$1,050,000** |
| **Cooling Systems - River Infrastructure** |
| River-edge enclosure (concrete vault) | $120,000 |
| 2 × Plate heat exchangers (1,000 kW) | $100,000 |
| 3 × River water pumps + VFD | $45,000 |
| Filtration (screens + strainers) | $60,000 |
| CW piping (200m DN200 insulated) | $60,000 |
| River piping (40m DN200) | $8,000 |
| Valves, controls, instrumentation | $65,000 |
| Intake/discharge structures | $45,000 |
| 400V power feed to enclosure (100m) | $15,000 |
| Installation & commissioning | $120,000 |
| **Subtotal River Cooling** | **$638,000** |
| **Building & Site** | [TBD] |
| **BMS, Controls, Monitoring** | $200,000 |
| **Fire Protection, Security** | [TBD] |
| **TOTAL PHASE 1 (MEP SYSTEMS)** | **$8,063,000 + [TBD]** |

**Cost per MW (IT):**
- $8,063,000 / 1.47 MW = **$5.5M per MW** (MEP systems only, excludes building shell)
- Note: Includes 700 kW solar array for office loads (~$700K of total cost)
- Note: Includes HPP step-up transformer and redundant MV switchboards (~$300K)

---

### **KEY DESIGN DECISIONS**

#### Why HPP at 400V with Step-Up (vs. 10 kV Direct)?
1. ✅ **HPP source characteristic:** Local hydroelectric plant generates at low voltage (400V generator output)
2. ✅ **Step-up required:** 400V → 10 kV transformation needed to match MV distribution voltage
3. ✅ **Common voltage platform:** Both sources normalized to 10 kV at MV switchboards for uniform distribution
4. ✅ **Redundant MV switchboards:** Separate MV-SWBD-A (HPP) and MV-SWBD-B (Grid) for isolation and protection
5. ✅ **Flexible architecture:** Can accommodate different utility source voltages via transformers
6. ✅ **Concurrent maintainability:** Step-up transformer can be isolated, facility fed from Grid via tie breaker

#### Why Main-Tie-Main (MTM) Topology (vs. Traditional 2N UPS)?
1. ✅ **Leverages dual utility sources:** HPP (3.7 MW) + Grid (4.0 MW) = diverse primary power
2. ✅ **Simple automatic failover:** Tie breaker closes on single source failure (<1 second transfer)
3. ✅ **Lower cost:** Eliminates need for separate utility ATS, reduces switchgear complexity
4. ✅ **Better reliability:** Dual utility + 2N MTU = triple redundancy (vs. single utility + 2N UPS)
5. ✅ **Concurrent maintainability:** Either transformer/breaker can be maintained via tie breaker
6. ✅ **Standard topology:** Proven design, widely used in industrial/commercial applications
7. ✅ **Simple controller:** Relay-based logic (no complex PLC), reduces cost and failure modes

#### Why MTU Kinetic PowerPack (vs. Separate UPS + Generators)?
1. ✅ **Integrated solution:** Diesel + flywheel UPS in single package
2. ✅ **No separate static UPS needed:** Saves ~$500K-800K CAPEX
3. ✅ **Smaller footprint:** 40% smaller than equivalent static UPS system
4. ✅ **Lower maintenance:** Fewer components, reduced failure modes
5. ✅ **Tier III/IV certified:** Uptime Institute approved for all tier levels
6. ✅ **Fast start:** 15-20 second ride-through, diesel starts in <10 seconds

#### Why 400V Distribution (vs. 480V)?
1. ✅ **Matches utility voltage:** 11 kV → 400V transformation standard in Georgia (IEC country)
2. ✅ **Single voltage platform:** No additional transformation needed
3. ✅ **Equipment availability:** Most European equipment rated 380-415V (IEC standard)
4. ✅ **MTU output voltage:** Kinetic PowerPack outputs 400V natively
5. ✅ **Lower current vs. 230V:** 400V 3-phase reduces copper sizing vs. single-phase

#### Why 3 × 800 kW Chillers (vs. 4 × 400 kW)?
1. ✅ **Proper N+1 redundancy:** 1,600 kW running > 1,467 kW required
2. ✅ **Fewer units:** Simpler maintenance, lower parts count
3. ✅ **Standard industrial size:** Better availability in Georgia/Turkey market
4. ✅ **Better load staging:** 0% / 50% / 100% load steps (vs. 33% / 66% / 100%)
5. ✅ **Lower installed cost:** ~$50K savings vs. 4 smaller units

#### Why Indirect River Cooling (vs. Direct)?
1. ✅ **Chiller protection:** Clean, treated water to expensive condensers
2. ✅ **Reduced fouling:** Plate HX easier to clean than chiller tubes
3. ✅ **Isolation capability:** Can bypass river system for maintenance
4. ✅ **Water quality control:** Closed condenser loop has stable chemistry
5. ✅ **Regulatory compliance:** Easier permitting with indirect discharge

#### Why River-Edge Enclosure (vs. Pumping to Building)?
1. ✅ **Minimize pumping energy:** Equipment at river level (low head)
2. ✅ **Centralized filtration:** All river water treatment at one location
3. ✅ **Easy maintenance access:** Dedicated service structure
4. ✅ **Flood protection:** Elevated above 100-year flood level
5. ✅ **Reduced building footprint:** Heat exchangers not in main building

#### Why Separate Office SWBD with Solar Priority?
1. ✅ **Sustainability:** 700 kW solar reduces carbon footprint, aligns with green DC goals
2. ✅ **Cost savings:** Solar offsets office electricity costs (payback ~5-7 years in Georgia)
3. ✅ **Grid independence:** Office loads (103 kW) operate during solar hours without utility
4. ✅ **Non-critical isolation:** Office failures don't impact critical data center operations
5. ✅ **No UPS/generator needed:** Office outages acceptable, reduces capital and operating cost
6. ✅ **Simple ATS:** Solar priority with utility backup, standard residential/commercial solution

---

### **DESIGN STANDARDS & CODES**

**Electrical:**
- IEC 60364 (Low-voltage electrical installations)
- IEC 61439 (Low-voltage switchgear and controlgear assemblies)
- IEEE 1584 (Arc flash hazard calculation)
- Uptime Institute Tier Standard: Topology

**Mechanical:**
- ASHRAE 90.1-2019 (Energy Standard for Buildings)
- ASHRAE 127-2012 (Data Center Thermal Guidelines)
- ISO 14644 (Cleanrooms and controlled environments)
- EN 378 (Refrigerating systems and heat pumps)

**Building:**
- IBC 2021 (International Building Code)
- NFPA 75 (Protection of Information Technology Equipment)
- Georgian Building Code (based on Eurocode)

**Environmental:**
- Georgian Water Pollution Control Regulations
- EU Water Framework Directive (2000/60/EC) as adopted in Georgia
- Kura River Basin Management Plan

---

### **NEXT STEPS**

1. **Finalize building architecture and site layout**
2. **Conduct Kura River environmental impact study (detailed)**
3. **Obtain river water usage and discharge permits**
4. **Confirm equipment lead times (MTU, chillers, transformers)**
5. **Develop detailed electrical single-line diagrams**
6. **Develop detailed mechanical P&IDs**
7. **Begin procurement of long-lead items (MTU units, transformers)**
8. **Engage Uptime Institute for Tier III certification process**

---

## CSI MASTERFORMAT OUTLINE

[Detailed sections to follow, organized by CSI divisions]

---

**Tags:** #GGE-data-center #basis-of-design #tbilisi-georgia #drups #kura-river-cooling #tier-iii #400v-distribution #mtm-topology #dual-utility #solar-integration #10kv-mv

---

### **SPECIFICATIONS GROUP**

#### **GENERAL REQUIREMENTS SUBGROUP**

**Division 01 – General Requirements**



**Summary:**
- **Project Coordination:** BIM-based design (LOD 400); weekly OAC meetings; design-assist from key subcontractors
- **Submittals:** Tiered review process (Tier 1: switchgear, UPS, generators, chillers require owner + engineer + CxA review)
- **Quality Control:** 3rd-party testing for concrete, soil, fireproofing, electrical thermography; NETA acceptance testing
- **Commissioning:** ASHRAE Guideline 0 + Uptime Tier III; independent CxA; Integrated Systems Test (IST) with simulated failures
- **Training:** 40+ hours hands-on training across all critical systems (electrical, mechanical, BMS, fire, security)
- **Closeout:** As-built drawings (CAD/BIM + PDF), O&M manuals (hard copy + digital), warranty register, test reports
- **Testing:** Load bank testing for generators (100% load, 4 hours) and UPS (100% load, 2 hours)
- **Regulatory:** Building permits, utility coordination, environmental permits (SWPPP, SPCC), code compliance (IBC 2018/2021, NEC 2020/2023)

---

#### **FACILITY CONSTRUCTION SUBGROUP**



**Summary:**
- **Division 02 (Existing Conditions):** Greenfield site; clearing, grubbing, erosion control per SWPPP
- **Division 03 (Concrete):** 
  - Foundation: Spread footings below frost line (18-24"); bearing capacity TBD per geotech
  - Data hall slab: 6-8" reinforced concrete, 4,000 PSI, FF 50 / FL 40 flatness, densifier/sealer finish
  - **AI rack floor load:** 750 PSF sustained (supports 3,500 lb racks like NVIDIA GB200 NVL72)
  - Equipment pads: Isolated pads for chillers/generators; oil containment for transformers
- **Division 04 (Masonry):** Not applicable (precast tilt-up construction)
- **Division 05 (Metals):** Clear-span steel joists/beams (28-30 ft height); seismic IBC Category B; cable tray trapeze hangers
- **Division 07 (Thermal/Moisture Protection):**
  - **Precast tilt-up walls:** 8-10" panels with R-19 insulation sandwich; tornado resistance (EF3+); 50+ year lifespan
  - **FM 1-150 roof:** 150 mph wind, Class 4 hail, fire-rated; TPO/EPDM fully adhered; storm-rated debris protection; premium: ~$500-800K
  - **Cost premium:** Precast ~$1.3-2.0M more than PEMB; offset by insurance savings ($200-300K/year)
- **Division 08 (Openings):** Security mantrap; data hall doors (at least two 10 ft H × 8 ft W double doors per hall for large equipment, other doors 4 ft single; card + biometric); loading dock; no windows in data halls
- **Division 09 (Finishes):** Sealed concrete floors, painted gypsum walls, exposed MEP ceiling in data halls
- **Division 13 (Special Construction):**
  - **FEMA 361 storm shelter/safe room:** Prefabricated module, 20 person capacity, located Level 1 adjacent to elevator, EF5 protection
- **Division 14 (Conveying Equipment):**
  - **Elevator:** 4-stop (Level 1/2/3/Roof), 2,500-3,500 lb capacity, hydraulic or traction, weather-protected roof access with overhang

---

#### **FACILITY SERVICES SUBGROUP**

**Division 21 – Fire Suppression**



**Summary:**
- **Data halls:** Pre-action sprinkler (NFPA 13) with VESDA early warning detection
- **Prefabricated PDMs (UPS/Electrical):** Integrated clean agent suppression (FM-200/Novec 1230) in PDM enclosures per NFPA 2001
  - UPS systems housed in outdoor prefabricated PDMs, not interior rooms
  - Maximizes building interior space for IT equipment
  - Factory-tested fire suppression systems for rapid deployment
- **Electrical/Mechanical rooms (interior):** Dry-pipe sprinkler or clean agent (if required)
- **Support spaces:** Wet-pipe sprinkler (offices, NOC, corridors)
- **Detection:** VESDA aspirating smoke detection in data halls; conventional smoke/heat in support spaces and PDMs
- **Suppression integration:** BMS lockouts (HVAC shutdown, damper closure) on alarm
- **Testing:** Pre-action system acceptance test, clean agent discharge test (simulated), PDM integrated suppression verification

---

**Division 22 – Plumbing**



**Summary:**
- **Domestic water:** Municipal or well supply; 500-1,000 GPD usage (restrooms, kitchen, emergency eyewash)
- **Sanitary sewer:** Municipal connection or on-site septic (if required)
- **Chilled water:** Closed-loop glycol systems (Loops 1, 2, 3); no cross-connection with domestic water
- **Water efficiency:** Low-flow fixtures (1.5 GPM faucets, 1.28 GPF toilets); ADA-compliant
- **Backflow prevention:** RPZ backflow preventers on all water service connections
- **Emergency fixtures:** Eyewash/shower stations in electrical and mechanical rooms
- **Leak detection:** Under-floor leak detection in data halls (if applicable); BMS-monitored

---

**Division 23 – HVAC**



**Summary:**
- **Phase 1 (Air Cooling):**
  - IT load: 3,000 kW (30 cabinets @ 100 kW)
  - Cabinet FCUs: 100 kW capacity each (dual coils: 50 kW Loop 1 + 50 kW Loop 2)
  - Chillers: 4 × 1,500 kW air-cooled (N+1 redundancy, shared plant for Loops 1+2)
  - Supply temp: 7-10°C; COP: 3.8-4.2 (mechanical), 15-25 (free cooling)
  - Free cooling: ~3,500-4,000 hours/year (Georgia climate)
- **Phase 2 (Air + D2C Cooling):**
  - IT load: 12,000 kW (30 cabinets @ 400 kW: 100 kW air + 300 kW D2C per cabinet)
  - Air cooling: Same 4 chillers (Loops 1+2, 3,000 kW unchanged)
  - D2C cooling: 8 × 1,500 kW air-cooled chillers (Loop 3 independent, N+1)
  - CDUs: 60 × 300 kW units (2 per cabinet for A/B redundancy)
  - Supply temp: 25°C; COP: 5.0-5.5 (higher efficiency than air cooling)
- **Zero water strategy:** No evaporative cooling; closed-loop glycol only
- **Building HVAC:** Rooftop units (RTUs) for offices, NOC, support spaces
- **Containment:** Cold aisle containment with doors (48" cold aisles, 60" hot aisles)
- **Controls:** BMS integration with DCIM; temperature/humidity monitoring; alarm escalation

---

**Division 25 – Integrated Automation**



**Summary:**
- **Building Management System (BMS):** Schneider Electric EcoStruxure or Johnson Controls Metasys
- **Electrical Power Monitoring System (EPMS):** Schneider Electric PowerLogic or Vertiv Trellis
- **Data Center Infrastructure Management (DCIM):** Schneider StruxureWare or Nlyte/Sunbird
- **Integration:** BACnet and Modbus protocols; unified dashboard for mechanical, electrical, security
- **Monitoring:** Real-time PUE, temperature/humidity, power consumption (cabinet-level metering)
- **Alarms:** Multi-tier escalation (SMS, email, SNMP traps); integration with NOC monitoring
- **Trending:** Historical data retention (5+ years); energy analytics and capacity planning
- **Remote access:** Secure VPN or cloud-based access for remote troubleshooting

---

**Division 26 – Electrical**



**Summary:**
- **Utility service:** 345 kV transmission → 2 × 25 MVA transformers (345kV/13.8kV) → 13.8 kV common bus
- **MV distribution:** 13.8 kV self-healing dual-ring topology via 6 RMUs (Ring A + Ring B) with automated SCADA switching
- **Generators:** 6 × 4.0 MW @ 13.8 kV diesel (N+1); Tier 4 Final emissions; ~2,000 gal belly tanks + central bulk fuel
- **Transformers:** 8 × 3,500 kVA (13.8 kV/480V) oil-filled (N+1 with concurrent maintainability)
- **IT UPS:** N+1 modular architecture; Phase 1: 5-6 × 1,250 kVA (4-5 running, 1 standby); Phase 2: 13-15 × 1,250 kVA (12-13 running, 1-2 standby)
- **UPS batteries:** 5-minute runtime maximum; Lithium-ion preferred (longer life, smaller footprint)
- **Mechanical UPS:** N+1 for pumps/fans; Phase 1: 8 × 250 kW; Phase 2: 20 × 250 kW
- **LV distribution:** Dual switchboards (SWBD-A/B) fed from different MV ring segments
- **Cabinet power:** Dual PDUs fed from different 480V distribution panels; Phase 1: 2 × 50 kW; Phase 2: 2 × 200 kW
- **Prefabricated PDMs:** 2 units housing LV switchboards, UPS, MV gear for rapid deployment
- **Code compliance:** NEC 2023; arc flash studies; NETA acceptance testing

---

**Division 27 – Communications**



**Summary:**
- **Fiber entrance:** 2 × geographically diverse MPOEs (Main Points of Entry)
- **Meet-me rooms (MMRs):** 2 × carrier-neutral cross-connect rooms
- **Pathways:** Underground ductbank to property line; 4" conduits with pull rope; fiber hand-off terminations
- **Backbone cabling:** Single-mode fiber (OS2) between MMRs and data halls
- **Horizontal cabling:** Overhead cable tray; separation from power cables per TIA-942
- **Grounding:** Telecommunication grounding busbar (TGB); bonding to building ground grid
- **Labeling:** Cable IDs at 10 ft intervals, both termination points, all junction boxes
- **Testing:** Fiber OTDR testing; certification reports for all fiber runs

---

**Division 28 – Electronic Safety and Security**



**Summary:**
- **Perimeter security:** K-rated fence (8 ft height), dual gates with card readers, anti-ram barriers
- **Access control:** HID or Lenel system; card + biometric (two-factor) for data halls; badge management
- **CCTV:** 24/7 recording, 90-day retention; cameras at all doors, equipment yards, data halls; Axis or Hanwha
- **Intrusion detection:** Perimeter sensors, door contacts; monitored by NOC or security service
- **Visitor management:** Log-in/log-out kiosk; escort required in data halls
- **Mantrap:** Double-door airlock at main entry; outer door must close before inner opens; fire override
- **Integration:** Access control and CCTV integrated with BMS; alarm escalation to NOC
- **Cybersecurity:** Segmented networks (IT, OT, security); firewall between BMS and corporate network

---

#### **SITE AND INFRASTRUCTURE SUBGROUP**

**Divisions 31-32 – Site and Infrastructure**



**Summary:**
- **Site area:** 20+ acres total; 50,000 GSF building footprint
- **Grading:** Cut/fill balance; positive drainage away from building; 2% min slope
- **Stormwater management:** Detention pond (100-year storm); SWPPP compliance (>1 acre disturbance); Georgia DEQ permit
- **Paving:** Reinforced concrete (equipment yards, loading dock); asphalt (parking, drives); 8" base course
- **Utilities:**
  - Water: 6" main from municipal or well
  - Sanitary: 8" gravity sewer to municipal or on-site septic
  - Fiber: Dual diverse underground duct bank entries (4" conduits)
- **Equipment yards:**
  - Electrical: ~100,000 SF (generators, transformers, switchgear); sized for 24 MW master plan
  - Mechanical: ~50,000 SF (chillers, cooling towers, pumps); sized for 12 chillers total
- **Fencing:** 8 ft K-rated perimeter; controlled access gates
- **Landscaping:** Drought-tolerant native species; drip irrigation; minimal turf area
- **Site lighting:** LED (100%); photocell/time clock control; dark-sky compliance
- **Fuel storage:** ~2,000 gal belly tanks per generator connected via common manifold to centralized bulk fuel tank farm (~12,000 gal capacity for 24-hour runtime); redundant fuel service contracts; SPCC compliance
- **Fire access:** 20 ft clear width; fire hydrants @ 500 ft spacing; fire lane striping

---

## EQUIPMENT SUMMARY

| Equipment                      | Phase 1 | Phase 2 Add | Total | Unit Size               |
| ------------------------------ | ------- | ----------- | ----- | ----------------------- |
| **Generators**                 | 3       | +3          | 6     | 4.0 MW @ 13.8 kV        |
| **Transformers (13.8kV/480V)** | 3       | +5          | 8     | 3,500 kVA               |
| **Utility Xfmrs (if 34.5kV)**  | 2       | 0           | 2     | ~20 MVA (34.5kV/13.8kV) |
| **RMUs**                       | 6       | 0           | 6     | 13.8 kV, 630A           |
| **IT UPS**                     | 5-6     | +8-9        | 13-15 | 1,250 kVA               |
| **Mech UPS**                   | 8       | +12         | 20    | 250 kW                  |
| **Chillers (Loops 1+2)**       | 4       | 0           | 4     | 1,500 kW                |
| **Chillers (Loop 3)**          | 0       | 8           | 8     | 1,500 kW                |
| **CDUs**                       | 0       | 60          | 60    | 300 kW each             |
| **Cabinets**                   | 30      | 0           | 30    | DDC S-Series            |
| **PDUs**                       | 60      | upgrade     | 60    | 50 kW → 200 kW          |

---

## KEY DESIGN DECISIONS

### **Why Tilt-Up Concrete (Not PEMB)**
- **Tornado resistance:** Pre-cast concrete withstands EF3-EF5 events better than steel framing
- **Insurance:** 30-40% lower premiums vs. PEMB in Tornado Alley
- **Thermal mass:** Better temperature stability, reduces HVAC cycling
- **Cost:** ~$15-25/SF premium over PEMB, justified by insurance savings and resilience

### **Utility Voltage Options**
- **13.8 kV or 12.47 kV:** Direct connection to 13.8 kV generators and MV distribution (no step-down required)
- **34.5 kV:** Requires two 34.5kV/13.8kV step-down transformers (~20 MVA each, N-1 redundancy)
  - Cost adder: ~$1.0-1.5M
  - Benefits: Often lower utility rates, better stability on high-voltage transmission

### **Why 13.8 kV Generators (Not 480V)**
- Standard product availability (3-5 MW range)
- Cable sizing: 13.8 kV reduces current by 29×
  - 4 MW @ 480V = 8,333 A (requires 6 × 500 kcmil/phase)
  - 4 MW @ 13.8 kV = 290 A (requires 1 × 2/0/phase)
- Easier paralleling and lower I²R losses

### **Why Separate Loop 3 (D2C Cooling)**
- **Air cooling (Loops 1+2):** Predictable, stable loads (±10% variation)
- **D2C cooling (Loop 3):** Violent load swings (0-100% in seconds)
- **Problems if mixed:** Control hunting, reduced efficiency, accelerated wear
- **Benefits of separation:** Optimized controls, clear contractor boundaries, independent maintenance, fault isolation

### **Why N+1 IT UPS with MV Dual-Ring (Not Traditional 2N UPS)**
- **Path redundancy** provided by 13.8 kV self-healing dual-ring MV distribution
- **Component redundancy** provided by N+1 modular UPS architecture
- IT equipment retains dual PDUs fed from different 480V panels (SWBD-A/B on different MV ring segments)
- **Advantages:** Lower capital cost (~40-50% fewer UPS modules), higher efficiency, simplified maintenance
- **Equivalent reliability:** MV dual-ring switching provides path diversity; N+1 UPS provides component failure tolerance

### **Why Slab-on-Grade (No Raised Floor)**
- Cost savings (~$150K+)
- Eliminates failure modes and underfloor plenum complications
- Better seismic performance
- Overhead cable distribution provides equivalent flexibility

---

**Tags:** #Tbilisi-data-center #basis-of-design #csi-masterformat #tier-iii #tilt-up-construction

**Next Steps:**
1. Confirm utility voltage (13.8 kV, 12.47 kV, or 34.5 kV)
2. Review detailed technical specifications by CSI division
3. Validate cost estimates with vendors
4. Begin detailed engineering design
5. Finalize equipment procurement schedule

---

**Document Control:**
- **Version:** 04 (MV voltage updated to 10kV)
- **Date Updated:** November 6, 2025
- **Prepared by:** EVS / GGE Engineering Team
- **Key Design Decisions:**
  - HPP source at 400V with step-up to 10 kV (local hydro generator characteristic)
  - Redundant MV switchboards (MV-SWBD-A @ HPP, MV-SWBD-B @ Grid)
  - Main-Tie-Main (MTM) topology at 400V LV level with dual utility sources:
    * HPP: 3.7 MW @ 400V → 10 kV → 400V (via step-up + step-down transformers)
    * Grid: 4.0 MW @ 10 kV → 400V (via step-down transformer)
  - MTU Kinetic PowerPack 2N (2 × 2,200 kW)
  - 400V distribution throughout critical loads
  - 3 × 800 kW chillers (N+1)
  - Indirect Kura River cooling via plate heat exchangers
  - Separate office SWBD with 700 kW solar array + utility backup
  - Simple relay-based MTM controller (not PLC)

**Revision History:**
- **Rev 04 (2025-11-06):** Medium voltage changed from 11kV to 10kV throughout
  - HPP step-up transformer: 400V/10kV (was 400V/11kV)
  - MV switchboards: 10kV (was 11kV)
  - Step-down transformers: 10kV/400V (was 11kV/400V)
  - Office transformer: 10kV/400V (was 11kV/400V)
  - Utility Grid incoming: 10kV (was 11kV)
  - Equipment cost impact: Minimal (10kV more common, potentially lower cost)
- **Rev 03 (2025-11-04):** MTM with HPP 400V Step-Up + Redundant MV SWBDs + Kura River Cooling
