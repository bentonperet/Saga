**Created:** 2025-10-23 10:30

# BASIS OF DESIGN - HVAC
## CSI Division 23
### Saga Energy – Pryor Data Center

**Parent Document:** [[_BOD - Exec Summary and TOC]]
**Related:** 

---

## OVERVIEW
Hybrid cooling strategy supporting high-density AI racks (liquid-cooled) and standard-density network racks. Target PUE 1.2-1.35 through extended free cooling, efficient equipment, and zero water consumption.

---

## COOLING ARCHITECTURE {TBC}

### System Design Philosophy
- **Air Cooling:** Rear-Door Heat Exchangers (RDHx) for network racks up to 22 kW/rack OR 
- **Liquid Cooling:** Coolant Distribution Units (CDUs) for AI racks up to 132 kW/rack
- **Room-Level Conditioning:** Rooftop AHUs for humidity control and building over-pressurization
- **Redundancy:** N+1 configuration within each 3 MW block
- **Modular Deployment:** Equipment deployed in 3 MW increments aligned with customer lease-up

### Target Performance
- **PUE:** 1.2-1.35 (annual average)
  - Free cooling months (Oct-Apr): 1.15-1.25
  - Mechanical cooling months (May-Sep): 1.25-1.35
- **IT Space Conditions:** 18-27°C (64-80°F), 5.5°C-60% RH dew point per ASHRAE A1

---

## CHILLED WATER PLANT

### Chiller Sizing & Configuration

**Cooling Load Calculation:**
| Phase | IT Load | Cooling Required | Notes |
|---|---|---|---|
| 1 | 3 MW | 3.3 MW | IT + ~0.3 MW non-IT loads |
| 2 | 6 MW | 6.5 MW | IT + ~0.5 MW non-IT loads |
| 3 | 9 MW | 9.8 MW | IT + ~0.8 MW non-IT loads |
| 4 | 12 MW | 13 MW | IT + ~1 MW non-IT loads |
| 5 | 20-24 MW | 21-25 MW | IT + ~1-1.5 MW non-IT loads |

**Chiller Configuration:**
- **Standard Chillers:** 1.5 MW each (air-cooled with integrated free cooling)
- **High-Capacity Chillers (Phase 5):** 2.5 MW each for high-density AI loads
- **Modular Deployment:**
  - Phase 1: 4 × 1.5 MW = 6 MW capacity (for 3.3 MW load)
  - Phase 2: 8 × 1.5 MW = 12 MW capacity (for 6.5 MW load)
  - Phase 3: 12 × 1.5 MW = 18 MW capacity (for 9.8 MW load)
  - Phase 4: 12 × 1.5 MW = 18 MW capacity (for 13 MW load)
  - Phase 5: 12 × 1.5 MW + 4 × 2.5 MW = 28 MW capacity (for 21-25 MW load)

### IT Load Density Evolution

**Why Two Chiller Sizes:**

The data center industry is experiencing a fundamental shift in rack power density driven by AI workloads. Traditional air-cooled network/storage racks operate at 5-15 kW, while modern AI/GPU racks require 50-100+ kW with liquid cooling. This density evolution drives our dual-chiller strategy:

- **Phase 1-4 (1.5 MW chillers):** Optimized for traditional air-cooled IT at 10-15 kW/rack
- **Phase 5 (2.5 MW chillers):** Sized for high-density liquid-cooled AI at 50-100 kW/rack

Using larger chillers for Phase 5 provides:
- Better efficiency at higher cooling loads
- Reduced yard footprint (16 total chillers vs 24)
- Dedicated capacity for liquid-cooled zones
- Future flexibility as AI workloads grow

### Key Chiller Specifications (Basis of Design)

| **Parameter** | **1.5 MW Standard** | **2.5 MW High-Capacity** |
|---|---|---|
| **Type** | Air-cooled screw with free cooling | Air-cooled screw with free cooling |
| **Capacity** | 1.5 MW (428 tons) | 2.5 MW (710 tons) |
| **Refrigerant** | Low-GWP (R-513A or equiv) | Low-GWP (R-513A or equiv) |
| **Supply Temp** | 45-50°F adjustable | 45-50°F adjustable |
| **Efficiency** | 0.85-0.95 kW/ton @ 95°F | 0.80-0.90 kW/ton @ 95°F |
| **Free Cooling** | <0.15 kW/ton @ 45°F | <0.15 kW/ton @ 45°F |
| **Power** | 480V, 3-phase | 480V or 4160V, 3-phase |
| **Dimensions** | ~25 ft × 10 ft | ~30 ft × 12 ft |

### Free Cooling Strategy

**Operating Modes:**
- **Full Free Cooling:** Ambient ≤45°F → Compressors off, fans only
- **Partial Free Cooling:** 45°F < Ambient ≤70°F → Reduced compressor operation
- **Mechanical Cooling:** Ambient >70°F → Full mechanical cooling

**Oklahoma Climate Advantage:**
- ~200+ days/year of free or partial free cooling
- Design conditions: 95°F summer / 10°F winter (ASHRAE 99.6%)
- Annual average efficiency target: 0.45-0.55 kW/ton


### Chiller Yard Layout
- **Location:** Opposite side of building to electrical equipment
- **Configuration:** Single or double row arrangement to fit 16 total chillers
- **Clearances:** 8-10 ft minimum between units for airflow and maintenance
- **Yard Capacity:** Sized for maximum 16 chillers (12 × 1.5 MW + 4 × 2.5 MW)
- **Phased Installation:**
  - Phase 1-4: Progressive installation in single row
  - Phase 5: Add larger 2.5 MW units in available positions
- **Sound Attenuation:** Acoustic barriers if required by local ordinance


---

## PUMPING & DISTRIBUTION

### System Architecture

**Primary/Secondary Configuration with Hydraulic Decoupling**
- **Primary Loop:** Constant flow through chillers (protects equipment)
- **Secondary Loop:** Variable flow to loads (energy efficiency)
- **Common Pipe:** Hydraulic separation between loops
- **Topology confirmed:** Industry-standard for data center applications

### Pump Sizing

**Primary Pumps (Constant Speed):**
- One pump per chiller, plus shared standby pumps
- ~360 GPM per chiller @ 60-80 ft head
- 20-30 HP motors, 480V power

**Secondary Pumps (Variable Speed with VFDs):**
- Phase 1-4: 3 pumps (2 duty + 1 standby) for 12 MW
- Phase 5: 5-6 pumps for 24 MW
- 1,200-1,500 GPM each @ 100-140 ft head
- 75-100 HP motors with VFDs for energy optimization


### Piping Distribution

**Design Parameters:**
- **Supply/Return Temperatures:** 45-50°F supply, 60-65°F return (15°F ΔT)
- **Distribution:** Overhead piping at 12-14 ft elevation (no raised floor)
- **Material:** Schedule 40 steel with grooved connections for flexibility
- **Insulation:** 1.5" closed-cell foam with vapor barrier (condensation control)

**Key Features:**
- Primary loop connects chillers in mechanical room/yard
- Secondary loop distributes to data hall via overhead routing
- Quick-connect fittings at rack locations for CDU/RDHx connections
- Isolation valves for maintenance without system shutdown

### Balance of Plant Equipment
- **Pressurization Units (PU):** 2× dual pump units (N+1) with feeder tank
- **Expansion Tanks (ET):** 2× bladder-type tanks (sized for system volume)
- **Chemical Dosing Pots (CDP):** 2× 8L units for corrosion/biological inhibitors
- **Dirt & Air Separators (DAS):** 2× horizontal-type units for system cleanliness

### Thermal Storage Tanks - Evaluation
- **RD109 Baseline:** 2× 10,000-gallon thermal storage tanks
- **Use Cases:**
  - Load shifting: Charge during off-peak, discharge during peak
  - Thermal inertia: Buffer against chiller cycling
  - Resilience: Additional capacity during chiller maintenance
- **Decision:** Evaluate benefit via PUE modeling. If peak load shifting not required (due to solar/BESS microgrid), tanks may be eliminated to reduce cost.

---

## DATA HALL COOLING {TBC}

### Rear-Door Heat Exchangers (RDHx) - Confirmed Approach

**Updated (Oct 2025):** Fan walls eliminated, RDHx confirmed as primary air-cooling strategy.

**Configuration:**
- **Type:** Rack-based cooling with chilled water coils mounted on each rack's rear door
- **Deployment:** Network racks (air-cooled, up to 22 kW/rack)
- **Coil Type:** Passive or active rear-door coils (active = fans integrated)
- **Chilled Water:** Overhead manifolds with quick-connect fittings at each rack

**Advantages:**
- **Per-Customer Control:** Each customer suite has isolated cooling capacity
- **Flexible Billing:** Measure chilled water flow per rack for accurate cost allocation
- **Mixed Density Support:** Handle varying rack densities in same row without airflow conflicts
- **Scalability:** Add RDHx only where needed (not entire data hall upfront)

### Liquid Cooling for AI Racks (Client-Specific Deployment)

**Coolant Distribution Units (CDUs):**
- **Quantity:** 9× CDU units (nominal, adjustable based on client requirements)
- **Capacity:** 50-80 kW cooling per CDU (supports 1-2 high-density AI racks)
- **Function:** Secondary heat exchanger between facility chilled water (45-50°F) and rack-level coolant loop
- **Rack Connection:** Quick-connect fittings, leak detection at all connections
- **Client-Specific:** Final CDU deployment and rack-level cooling hardware determined by tenant requirements

### Hot Aisle Containment 
*Optional based on customer demand*

---

## ROOFTOP AIR HANDLING UNITS (AHUs)

### Data Hall Environmental Control

**Purpose:** Humidity control and building pressurization (NOT primary cooling)

**Configuration:**
- **Quantity:** 3-4 units Phase 1, 5-6 units Ultimate (N+1 redundancy)
- **Capacity:** 10-15 tons cooling per unit (handles non-IT loads only)
- **Primary Function:** Maintain ASHRAE A1 environmental conditions
  - Temperature: 64-80°F (controlled by RDHx/CDUs)
  - Humidity: 20-60% RH (controlled by AHUs)
  - Pressurization: +0.02-0.05" WC (prevent dust ingress)

**Note:** IT cooling handled by RDHx/CDUs. AHUs provide environmental control only.

---

## SUPPORT SPACE HVAC {TBC}

### Electrical Rooms (Outdoor Enclosures)
- **Cooling:** Self-contained HVAC in outdoor electrical enclosures (weather-rated containers)
- **Target Temp:** 25°C ± 2°C (77°F ± 4°F)
- **Redundancy:** Integrated into container design

**Note:** Outdoor electrical enclosures replace traditional indoor electrical rooms with DX units.

### Mechanical Rooms
- **Cooling:** 4× 15 kW DX units with remote air-cooled condensers (per RD109)
- **Redundancy:** N+1

### Office/NOC/Break Room
- **System Type:** Rooftop package units (RTUs) or split systems
- **Redundancy:** Not required (non-critical spaces)
- **Control:** Thermostat control, occupied/unoccupied setback

---

## ENERGY EFFICIENCY MEASURES

### PUE Optimization Strategies
1. **Extended Free Cooling:** Maximize hours of free cooling operation (~215 days/year in Oklahoma)
2. **Variable Speed Drives (VFDs):** All pumps and AHU fans on VFDs for part-load efficiency
3. **High Supply Temperature:** Increase chilled water supply temp to 50°F (reduces chiller lift)
4. **Hot Aisle Containment:** Prevents hot/cold air mixing
5. **LED Lighting:** High-efficiency LED with occupancy sensors
6. **BESS-as-UPS:** Eliminates 4-8% UPS conversion losses (if BESS-as-UPS confirmed)

### Monitoring & Verification
- Real-time PUE monitoring via DCIM platform
- Monthly PUE reporting per The Green Grid guidelines
- Continuous commissioning to identify efficiency degradation

---

## MECHANICAL SYSTEM REDUNDANCY TOPOLOGY

### Chilled Water System Flow Diagram

```
                    CHILLER PLANT (N+1 per 3MW Block)
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
    Chiller 1            Chiller 2            Chiller 3
    (1.5 MW)             (1.5 MW)             (1.5 MW)
        │                     │                     │
        └─────────────────────┼─────────────────────┘
                              │
                    PRIMARY LOOP HEADER
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
   Primary Pump 1      Primary Pump 2      Primary Pump 3
   (Lead)              (Lag)               (Standby)
        │                     │                     │
        └─────────────────────┼─────────────────────┘
                              │
                      COMMON PIPE (Decoupler)
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
  Secondary Pump 1    Secondary Pump 2    Secondary Pump 3
  (VFD - Lead)        (VFD - Lag)         (VFD - Standby)
        │                     │                     │
        └─────────────────────┼─────────────────────┘
                              │
                  SECONDARY LOOP HEADER (Variable Flow)
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
   Data Hall CDUs      Data Hall RDHx         Rooftop AHUs
   (Liquid-Cooled      (Air-Cooled           (Humidity Control)
    AI Racks)           Network Racks)
```

### N+1 Redundancy Paths

**Chiller Plant Redundancy:**
- Each 3 MW block: 3 chillers @ 1.5 MW each = 4.5 MW total capacity
- IT Load: 3 MW + Facility Overhead @ 1.25 PUE = 3.75 MW cooling required
- N+1 Configuration: Any 2 of 3 chillers can support full block load
- Failure Mode: Single chiller failure → remaining 2 chillers at 94% capacity (within design margin)

**Pump Redundancy:**
- Primary Loop: 3 pumps (2 running + 1 standby) per 3 MW block
- Secondary Loop: 3 pumps (2 running + 1 standby) for entire facility
- Control: Automatic switchover on pump failure (BMS-controlled)

**Distribution Redundancy:**
- Multiple parallel piping paths to data hall
- Isolation valves allow section isolation without full system shutdown
- Quick-connect fittings at each rack for easy maintenance

## MECHANICAL REDUNDANCY SUMMARY

**N+1 Configuration Within Each 3 MW Block:**
- **Chillers:** 3 chillers per 3 MW block, any 2 support full block load
- **Pumps:** N+1 redundancy (any single pump failure does not impact capacity)
- **CDUs:** N+1 capacity for liquid-cooled AI racks
- **RDHx:** N+1 capacity per zone (rack-based approach inherently redundant)
- **AHUs:** N+1 rooftop units for comfort cooling

**Maintenance Mode:**
- Any single chiller can be isolated without impacting IT load
- Chilled water loop includes isolation valves and bypass piping
- Pumps have redundant units for rotation during preventive maintenance

---

## KEY DESIGN CHANGES FROM ORIGINAL BOD

### Capacity Expansion
- **Original:** 3× 1,177 kW chillers (7.4 MW IT load)
- **Updated (Oct 2025):** ~16× 1.5 MW chillers (12 MW initial, 20-24 MW ultimate)

### Cooling Strategy Refinement
- **Fan Walls Eliminated:** Replaced with RDHx for per-customer control
- **Rooftop AHUs Added:** For humidity control and building over-pressurization
- **Chiller Yard Relocated:** South side of building, horizontal layout with expansion space

### Modular 3 MW Blocks
- Deploy chillers as 3 MW IT load blocks are commissioned
- 3 chillers per block provides N+1 redundancy within each block
- Aligns equipment procurement with customer lease-up

---

## MECHANICAL EQUIPMENT SCHEDULE

### HVAC Equipment by Phase

| Equipment | Description | Phase 1 (3MW) | Phase 2 (6MW) | Phase 3 (9MW) | Phase 4 (12MW) | Phase 5 (20-24MW) |
|---|---|---|---|---|---|---|
| **1.5 MW Chiller** | Standard air-cooled with free cooling | 4 | 8 | 12 | 12 | 12 |
| **2.5 MW Chiller** | High-capacity for AI loads | 0 | 0 | 0 | 0 | 4 |
| **Primary CHW Pump** | 360 GPM @ 60-80 ft (1.5MW), 600 GPM (2.5MW) | 5 | 9 | 13 | 13 | 17 |
| **Secondary CHW Pump** | 1,200-1,500 GPM @ 100-140 ft, 75-100 HP, VFD | 3 | 3 | 3 | 3 | 5-6 |
| **Expansion Tank** | Bladder-type, ASME rated | 1 | 2 | 2 | 2 | 3 |
| **Pressurization Unit** | Dual pump with feeder tank | 1 | 1 | 1 | 1 | 2 |
| **Chemical Treatment** | Dosing pots, separators, filters | 1 set | 1 set | 1 set | 1 set | 2 sets |
| **CDU (if liquid cooling)** | 50-80 kW per unit | As needed | As needed | As needed | As needed | High qty |
| **Rooftop AHU** | Environmental control, 10-15 tons | 3 | 3 | 4 | 4 | 5-6 |
| **Support Space HVAC** | Mechanical rooms, offices | 1 set | 1 set | 1 set | 1 set | 1 set |

**Notes:**
- Phase 1-4: 1.5 MW chillers in groups of 4 (3 duty + 1 standby)
- Phase 5: Add 4 × 2.5 MW chillers for high-density liquid cooling
- Total chiller yard capacity: 16 units maximum
- Primary pumps: One per chiller + shared standby
- CDUs/RDHx: Customer-specific based on rack type
### Phasing Strategy
- **Phase 1 (3 MW IT):** Initial deployment with first 3 MW block
- **Phase 2 (6 MW IT):** Add second 3 MW block
- **Phase 3 (9 MW IT):** Add third 3 MW block
- **Phase 4 (12 MW IT):** Complete initial buildout (may not need additional chillers from Phase 3)
- **Phase 5 (20-24 MW IT):** Density upgrade - add chillers for increased load from liquid cooling

---

## COST IMPACTS & FINANCIAL ANALYSIS

**Cost Analysis Prompt for Future Detailed Work:**

```
MECHANICAL SYSTEMS COST ESTIMATION PROMPT

Using the equipment schedules above and the detailed specifications throughout this BOD,
perform a comprehensive cost analysis for the mechanical systems including:

1. EQUIPMENT PRICING BY PHASE
   - Itemize costs for each piece of equipment listed in the schedule
   - Include installation labor, rigging, startup, and commissioning
   - Provide vendor quotes or recent comparable project pricing
   - Account for geographic location (Mayes County, OK / Tulsa labor market)

2. VENDOR CONFIDENCE LEVELS
   - Assign confidence level (High/Medium/Low) to each line item
   - High = Recent vendor quote or comparable installation
   - Medium = Industry pricing guides with regional adjustment
   - Low = Preliminary estimate requiring detailed engineering

3. ALTERNATIVE OPTIONS WITH COST DELTAS
   - Compare air-cooled chillers vs evaporative-assisted (adiabatic pre-cooling)
   - Evaluate VFD vs constant speed pumps (CAPEX vs OPEX trade-off)
   - Consider thermal storage tanks (CAPEX impact, PUE/OPEX benefit)

4. OPEX IMPLICATIONS
   - Annual energy consumption by equipment type (chillers, pumps, fans)
   - Maintenance costs (preventive maintenance, filter replacement, water treatment)
   - Water consumption (if any - currently zero water strategy)
   - Refrigerant leak/replacement costs

5. PUE IMPACT ANALYSIS
   - Calculate PUE contribution of each major system component
   - Model annual PUE based on Oklahoma climate (free cooling hours)
   - Compare PUE to industry benchmarks for air-cooled data centers

6. IRR CONSIDERATIONS
   - Evaluate CAPEX vs OPEX trade-offs for alternative designs
   - Model impact of free cooling on annual operating costs
   - Consider phased deployment capital efficiency
   - Revenue opportunity from PUE-optimized customer contracts

OUTPUT FORMAT:
- Detailed cost breakdown table by CSI division and equipment type
- Confidence level assigned to each line item with justification
- Executive summary of total mechanical systems CAPEX by phase
- Annual OPEX projection and PUE impact summary
```

**Preliminary Cost Estimate:**

| System | Phase 1-4 (3-12 MW) | Phase 5 (20-24 MW) | Notes |
|---|---|---|---|
| 1.5 MW Chillers | $6-8M (12 units) | -- | Standard units @ $500-650K each |
| 2.5 MW Chillers | -- | +$3.2-4M (4 units) | High-capacity @ $800K-1M each |
| Pumps & Piping | $2-3M | +$1-1.5M | Primary/secondary system |
| Rooftop AHUs | $0.3-0.5M | +$0.2M | Environmental control only |
| Balance of Plant | $0.5-1M | +$0.5M | Tanks, treatment, controls |
| **Total HVAC** | **$8.8-12.5M** | **+$4.9-6.2M** | Excludes customer rack cooling |

**Notes:**
- CDUs and RDHx excluded (customer-specific)
- Detailed vendor quotes required for Phase 1 pricing
- Oklahoma labor rates and site conditions apply

**Note:** Detailed cost analysis to be completed in separate financial modeling exercise per prompt above.


---

**Tags:** #saga-project #hvac #cooling #chillers #rdx #csi-division-23

**Related Documents:**
- [[_BOD - Exec Summary and TOC]] - Main title page and facility overview
- [[4BOD - Plumbing (CSI Div 22)]] - Chilled water treatment chemistry, leak detection details
- [[6BOD - Integrated Automation (CSI Div 25)]] - BMS controls, DCIM integration, monitoring points
- [[7BOD - Electrical (CSI Div 26)]] - Mechanical switchboards, power supply to pumps/chillers
- [[2BOD - Facility Construction (CSI Divs 02-14)]] - Building envelope, rooftop AHU mounting
- [[10BOD - Site and Infrastructure (CSI Divs 31-32)]] - Chiller yard layout, equipment placement
- [[Architectural Meeting Changes by CSI Division]] - October 2025 design updates
