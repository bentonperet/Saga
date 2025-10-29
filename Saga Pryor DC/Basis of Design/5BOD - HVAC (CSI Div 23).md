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
- **PUE:** 1.2-1.3 (annual average)
  - Free cooling months (Oct-Apr): 1.15-1.25
  - Mechanical cooling months (May-Sep): 1.25-1.35
- **IT Space Conditions:** 18-27°C (64-80°F), 5.5°C-60% RH dew point per ASHRAE A1

---

## CHILLED WATER PLANT

### Chiller Configuration - Updated Oct 2025

**Expanded Capacity for 12 MW Initial / 20-24 MW Ultimate**
- **Chiller Count:** ~16 total chillers (phased deployment)
- **Chiller Sizing:** 1.5 MW per chiller (air-cooled with integrated free cooling)
- **Modular 3 MW Blocks:** 3 chillers per 3 MW IT load block (provides N+1 redundancy per block)
- **Phase 1 Deployment:** Chillers for initial 12 MW capacity
- **Phase 2 Deployment:** Additional chillers as density upgrades occur (20-24 MW ultimate)

**Original (RD109):** 3× 1,177 kW chillers for 7.4 MW
**Updated (Oct 2025):** ~16× 1.5 MW chillers for 12-24 MW (phased)

### Chiller Technical Specifications

| **Parameter** | **Specification** |
|---|---|
| **Chiller Type** | Air-cooled screw compressor with integrated free cooling |
| **Nominal Cooling Capacity** | 1.5 MW (5,100 MBH / 428 tons) |
| **Compressor Type** | Dual screw compressors (2 per unit for staging) |
| **Refrigerant** | Low-GWP refrigerant (R-513A or R-1234ze) |
| **Refrigerant Charge** | ~300-400 lbs per unit |
| **Condenser Type** | Microchannel air-cooled coil with EC fans |
| **Fan Configuration** | 4-6 variable speed EC fans per condenser section |
| **Evaporator Type** | Brazed plate heat exchanger (BPHE) |
| **Chilled Water Flow** | 360 GPM @ 10°F ΔT (adjustable) |
| **Supply Temperature Range** | 45-50°F (7-10°C) adjustable |
| **Entering Water Temperature** | 60-65°F (15-18°C) design |
| **Operating Range** | -20°F to 115°F ambient (-29°C to 46°C) |
| **Efficiency (Full Load)** | 0.85-0.95 kW/ton @ 95°F ambient |
| **Efficiency (Free Cooling)** | 0.10-0.15 kW/ton @ 45°F ambient (fans only) |
| **Part Load Performance** | IPLV 0.60-0.70 kW/ton per AHRI 550/590 |
| **Sound Level** | ≤85 dBA @ 30 ft (with optional sound attenuation) |
| **Power Supply** | 480V, 3-phase, 60 Hz |
| **Electrical Connection** | Dual A+B feeds from mechanical switchboards (480V) |
| **Full Load Amps (FLA)** | ~240-280A per unit |
| **Locked Rotor Amps (LRA)** | ~1,200-1,400A per compressor |
| **Starter Type** | VFD soft start on compressors |
| **Control Interface** | BACnet/IP, Modbus TCP/IP to BMS |
| **Operating Modes** | (1) Full Free Cooling, (2) Partial Free Cooling, (3) Mechanical Cooling |
| **Safety Features** | High/low pressure cutouts, freeze protection, oil level monitoring |
| **Dimensions (L×W×H)** | ~25 ft × 10 ft × 12 ft (TBD per vendor) |
| **Operating Weight** | ~18,000-22,000 lbs per unit |
| **Outdoor Rating** | NEMA 3R weatherproof enclosure |
| **Seismic Rating** | IBC 2021, Seismic Design Category C (Oklahoma) |
| **Warranty** | 5-year compressor, 1-year parts (standard manufacturer warranty) |

### Integrated Free Cooling Technology

**Free Cooling Capability:**
- Each chiller equipped with integrated economizer mode
- Refrigerant migration cooling (refrigerant circulates via natural thermosiphon when ambient < setpoint)
- Transition from mechanical to free cooling is automatic and seamless

**Control Logic:**
- **Mode 1 (Full Free Cooling):** Ambient ≤50°F → Compressors off, fans modulate to maintain supply temp
- **Mode 2 (Partial Free Cooling):** 50°F < Ambient ≤75°F → Compressors run at reduced capacity, fans assist
- **Mode 3 (Mechanical Cooling):** Ambient >75°F → Full compressor operation, fans at design speed

**Annual Performance (Pryor, OK Climate):**
- Mode 1 hours: ~3,800 hrs/year (43%)
- Mode 2 hours: ~2,900 hrs/year (33%)
- Mode 3 hours: ~2,060 hrs/year (24%)
- Weighted average efficiency: 0.45-0.55 kW/ton annual

### Free Cooling Operation Modes

**Mode 1: Full Free Cooling (Winter)**
- **Conditions:** Ambient <50-55°F
- **Operation:** Compressors off, heat rejected via air-cooled coils only
- **PUE Impact:** Minimal cooling energy, PUE ~1.15-1.20

**Mode 2: Partial Free Cooling (Spring/Fall)**
- **Conditions:** Ambient 55-75°F
- **Operation:** Compressors run at reduced capacity
- **PUE Impact:** Moderate cooling energy, PUE ~1.20-1.25

**Mode 3: Full Mechanical Cooling (Summer)**
- **Conditions:** Ambient >75°F
- **Operation:** Compressors run at full capacity
- **PUE Impact:** Maximum cooling energy, PUE ~1.25-1.35

### Oklahoma Climate Optimization
- **Design Conditions (Pryor, OK):**
  - Summer: 95°F dry bulb / 78°F wet bulb (99.6% ASHRAE design day)
  - Winter: 10°F dry bulb (99.6% ASHRAE design day)
- **Free Cooling Season:** ~215 days/year (Oct-Apr)
- **Extended free cooling vs Dallas:** +30 days/year due to colder Oklahoma winters

### Chiller Yard Layout - Updated Oct 2025
- **Location:** South side of building (opposite electrical equipment)
- **Configuration:** Horizontal arrangement (one long row or two rows)
- **Clearances:** 8-10 ft minimum between chillers for airflow and maintenance access
- **Future Expansion:** Leave blank positions for additional chillers as density increases
- **Sound Attenuation:** Outdoor enclosures or acoustic barriers if noise ordinance requires

### Adiabatic Fluid Cooler Elimination - Confirmed
- **RD109 Baseline:** 5× adiabatic fluid coolers (1,478 kW each) with evaporative pre-cooling
- **Saga Pryor:** Eliminated (zero water consumption strategy)
- **Cost Impact:** +$150-450K net (larger chillers offset by eliminating fluid coolers)
- **PUE Impact:** +0.02-0.05 during peak summer (minimal annual impact due to extended free cooling)
- **OPEX Savings:** -$15-25K/year (water cost + treatment + maintenance)

---

## PUMPING & DISTRIBUTION {TBC}

### Chilled Water Pumps
- **Configuration:** Primary/secondary pumping loops
- **Primary Pumps:** Constant flow through chillers
- **Secondary Pumps:** Variable flow to data hall loads (CDUs, RDHx, AHUs)
- **Redundancy:** N+1 (any single pump failure does not impact cooling capacity)
- **VFD Control:** Variable frequency drives on secondary pumps for energy optimization

**Pump Count:** 5-8 pumps total (exact count TBD during detailed design, scaled for 12 MW capacity)

### Piping Distribution
- **Supply Temperature:** 45-50°F (adjustable based on load profile)
- **Return Temperature:** 60-65°F (ΔT = 10-15°F target)
- **Piping Material:** Schedule 40 steel or CPVC (indoor), insulated to prevent condensation
- **Routing:** Overhead distribution (no raised floor)

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

**Cost Impact:** +$3-5K per RDHx unit (~48 network racks × $3-5K = +$144-240K total)

**Deviation:** RD109 used fan walls at end of hot aisles. RDHx provides better flexibility for colocation model.

### Liquid Cooling for AI Racks {TBC}

**Coolant Distribution Units (CDUs)**
- **Quantity:** 9× MCDU-50 equivalent units (or similar)
- **Capacity:** ~50 kW per CDU (scalable based on rack count)
- **Function:** Rack-level chilled water distribution and return collection
- **Coolant Type:** Facility chilled water (45-50°F supply) or dielectric fluid (for direct-to-chip)

**Rack-Level Liquid Cooling Options:**
1. **Rear-Door Liquid Coils:** Chilled water coil on rack rear door
   - Capacity: 50-80 kW/rack
   - Simple retrofit, lower cost
2. **Direct-to-Chip:** Cold plates mounted directly on CPUs/GPUs
   - Capacity: 100-150+ kW/rack
   - Higher efficiency, requires server OEM support

**Deployment Strategy:**
- **Pre-Install:** CDUs and chilled water manifolds for 48 AI racks
- **Customer-Specific:** Liquid cooling hardware deployed when customer moves in
- **Flexibility:** Lower-density AI racks may use air cooling; reserve liquid capacity for high-density customers

**Manifold Distribution:**
- Overhead chilled water manifolds parallel to rack rows
- Quick-connect fittings at each rack position
- Leak detection sensors under all connections (integrated with BMS)

### Hot Aisle Containment

**Configuration:**
- **Type:** Hard-sided hot aisle containment with doors
- **Materials:** Polycarbonate panels or metal framed doors (transparent for visibility)
- **Height:** Floor-to-overhead cable tray (no raised floor)
- **Pressure:** Negative pressure in hot aisle (fans pull air from containment)

**Benefits:**
- Prevents hot/cold air mixing (improves cooling efficiency)
- Increases supply air temperature setpoint (reduces chiller energy)
- Enables higher density deployments

**Access:**
- Hot aisle doors for maintenance access to rear of racks
- Interlocked with fire suppression (doors auto-open on fire alarm)

---

## ROOFTOP AIR HANDLING UNITS (AHUs) - UPDATED OCT 2025 {TBC}

### Comfort Cooling & Air Quality Strategy

**Equipment:** Rooftop AHUs for data hall environmental conditioning

**Functions:**
- **Humidity Control:** Maintain 5.5°C-60% RH dew point per ASHRAE A1
- **Building Over-Pressurization:** Prevent dust ingress from exterior
- **Air Quality:** MERV filtration for particulate removal
- **Minimal Sensible Cooling:** RDHx/CDUs handle IT heat; AHUs address building envelope, lighting, PDU losses

**Redundancy:** N+1 AHU configuration

**Phasing:**
- **Phase 1:** AHU capacity for 20,000 SF fitted out white space
- **Phase 2:** Add remaining AHU capacity when second 20,000 SF fitted out

**Deviation:** RD109 did not explicitly call out rooftop AHUs for comfort. Saga Pryor adds this for improved environmental control.

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

## COST IMPACTS

| System | Cost Estimate |
|---|---|
| Chiller plant (~16 chillers @ 1.5 MW) | ~$8-12M (phased) |
| Chilled water pumps & piping | ~$2-3M |
| CDUs (9× units for liquid cooling) | ~$500K-1M |
| RDHx (48 network racks) | +$144-240K |
| Rooftop AHUs (comfort cooling) | ~$300-500K |
| Balance of plant (tanks, treatment, etc.) | ~$500K-1M |
| Adiabatic cooler elimination savings | -$750K to -$1M |
| **Net chiller plant cost increase** | +$150-450K |


---

**Tags:** #saga-project #hvac #cooling #chillers #rdx #csi-division-23

**Related Documents:**
- [[_BOD - Exec Summary and TOC]] - Main title page
- [[4BOD - Plumbing (CSI Div 22)]] - Chilled water treatment
- [[6BOD - Integrated Automation (CSI Div 25)]] - BMS controls
- [[Architectural Meeting Changes by CSI Division]] - October 2025 updates
