# GGE DATA CENTER - COOLING SYSTEM DESIGN
## Scaled for 3.0 MW IT Capacity (N+1 MTU Configuration)

**Document:** GGE-COOL-DESIGN-002
**Date:** 2025-11-04
**Revision:** 01 - Scaled for 3.0 MW IT
**Prepared by:** EVS / GGE Engineering Team

---

## COOLING REQUIREMENTS

### **IT Heat Rejection:**
```
IT Load:                 2,933 kW (100% becomes heat)
Pump Heat (in data hall): 240 kW (CHW, CW, River pumps)
Fan Heat (in-row units):   80 kW (fan motors)
─────────────────────────────────────────────
Total Data Hall Heat:    3,253 kW
```

### **Chiller Compressor Heat:**
```
Chiller COP:             5.5 (water-cooled, design condition)
Chiller Input Power:     3,253 / 5.5 = 591 kW (compressor electrical)
Condenser Heat Rejection: 3,253 + 591 = 3,844 kW (to Kura River)
```

---

## WATER-COOLED CHILLER PLANT

### **Configuration:**
```
3 × 1,600 kW Water-Cooled Chillers (N+1 Redundancy)
├─ Chiller #1: 1,600 kW (Running)
├─ Chiller #2: 1,600 kW (Running)
└─ Chiller #3: 1,600 kW (Standby - N+1)

Total Running Capacity: 3,200 kW
Total Installed: 4,800 kW
Margin: 3,200 / 3,253 = 98% → MARGINAL (need 1,800 kW chillers for 20% margin)
```

### **RECOMMENDED: Upsize to 1,800 kW Chillers**
```
3 × 1,800 kW Water-Cooled Chillers (N+1)
Running Capacity: 3,600 kW
Margin: 3,600 / 3,253 = 111% → 11% margin ✓
```

### **Chiller Specifications:**
- **Cooling Capacity:** 1,800 kW each (6,145,000 BTU/hr)
- **Type:** Water-cooled, screw or centrifugal compressor
- **Refrigerant:** R-134a or R-513A (low GWP)
- **Evaporator:** Produces CHW at 12°C supply, 18°C return (ΔT = 6°C)
- **Condenser:** Cooled by CW loop at 20-30°C supply, 30-40°C return (ΔT = 10°C)
- **COP:** 5.5 (water-cooled, design condition)
- **Compressor Power:** 1,800 / 5.5 = 327 kW per chiller
- **Brands:** Carrier, Trane, York, Daikin, Johnson Controls
- **Location:** Indoor mechanical room (protected from weather)
- **Control:** VFD-driven compressors, integrated BMS control
- **Concurrent Maintenance:** Isolation valves allow any chiller to be removed from service

---

## CHILLED WATER DISTRIBUTION (LOOP 1 - CHW)

### **Purpose:** Deliver cooling to data hall via in-row cooling units

### **Design Conditions:**
- **Supply Temperature:** 12°C
- **Return Temperature:** 18°C
- **Temperature Differential (ΔT):** 6°C
- **Total Cooling Load:** 3,253 kW

### **Flow Rate Calculation:**
```
Q = ṁ × Cp × ΔT
3,253 kW = ṁ × 4.186 kJ/(kg·°C) × 6°C
ṁ = 3,253 / (4.186 × 6) = 129.5 kg/s = 7,770 L/min
```

### **CHW Pumps:**
```
Configuration: 3 × CHW Pumps (2 running + 1 standby, N+1)
Flow per pump: 3,885 L/min (50% capacity)
Total Head: 40m (131 ft) - includes piping, valves, coils, elevation
Power per pump: 45 kW (60 HP)
Total Power (running): 90 kW
Drive: VFD for variable flow control
Location: Data center mechanical room
Critical Power: Yes (fed from MTU-backed 400V distribution)
```

### **Piping:**
- **Material:** Insulated steel pipe or HDPE
- **Size:** DN250 (10") mains, DN100-150 (4"-6") branches
- **Insulation:** 50mm closed-cell elastomeric (prevent condensation)
- **Layout:** Overhead distribution to in-row units or under-floor

### **Control Strategy:**
- **Variable Flow:** VFD control based on data hall return temperature
- **Setpoint:** Maintain 12°C supply temperature
- **Turndown:** 30% minimum flow (to prevent chiller surge)

---

## CONDENSER WATER SYSTEM (LOOP 2 - CW - CLOSED PRIMARY)

### **Purpose:** Reject heat from chillers to river heat exchangers

### **Configuration:**
- **Type:** Closed loop (treated water, minimal makeup)
- **Primary Loop:** Mechanical room (chillers) to river enclosure (heat exchangers)

### **Design Conditions:**
- **Supply Temperature:** 20°C (winter with free cooling) to 30°C (summer)
- **Return Temperature:** 30°C (winter) to 40°C (summer)
- **Temperature Differential (ΔT):** 10°C
- **Heat Rejection:** 3,844 kW (total condenser load)

### **Flow Rate Calculation:**
```
Q = ṁ × Cp × ΔT
3,844 kW = ṁ × 4.186 kJ/(kg·°C) × 10°C
ṁ = 3,844 / (4.186 × 10) = 91.8 kg/s = 5,508 L/min
```

### **CW Pumps:**
```
Configuration: 3 × CW Pumps (2 running + 1 standby, N+1)
Flow per pump: 2,754 L/min (50% capacity)
Total Head: 45m (148 ft) - includes 200m piping run + heat exchanger pressure drop
Power per pump: 52 kW (70 HP)
Total Power (running): 104 kW
Drive: VFD for variable flow control
Location: Data center mechanical room
Critical Power: Yes (fed from MTU-backed 400V distribution)
```

### **Piping:**
- **Material:** DN200 (8") HDPE, insulated, buried 1.5m depth
- **Route:** Data center mechanical room → 100m → River-edge enclosure → 100m → Return
- **Total Length:** 200m (supply + return)
- **Insulation:** 50mm polyurethane foam (prevent heat gain/loss)

### **Water Treatment:**
- **Corrosion Inhibitor:** Molybdate or phosphate-based (annual dosing)
- **Biocide:** Non-oxidizing biocide (quarterly slug feed)
- **Filtration:** Side-stream 50 micron filtration (10% flow)
- **Monitoring:** pH, conductivity, temperature, flow

### **Bypass Capability:**
- **3-way Motorized Valves:** 2 × DN200 (at river enclosure)
- **Purpose:** Bypass river heat exchangers during maintenance or when river temp too high
- **Control:** BMS-integrated PLC logic, automatic mode switching

---

## RIVER WATER SYSTEM (LOOP 3 - RW - OPEN SECONDARY)

### **Purpose:** Cool condenser water via plate heat exchangers using Kura River water

### **Configuration:**
- **Type:** Open loop (river water intake → filter → heat exchanger → river discharge)
- **Source:** Kura River (100m from data center)

### **Design Conditions:**
- **River Temperature Range:** 6°C (winter) to 27°C (summer)
- **Temperature Rise:** 10°C average across heat exchanger
- **Heat Rejection:** 3,844 kW (total)

### **Flow Rate Calculation:**
```
Q = ṁ × Cp × ΔT
3,844 kW = ṁ × 4.186 kJ/(kg·°C) × 10°C
ṁ = 91.8 kg/s = 5,508 L/min

Add 10% for approach temperature loss:
River Water Flow = 5,508 × 1.1 = 6,059 L/min ≈ 6,100 L/min
```

### **River Water Pumps:**
```
Configuration: 3 × River Water Pumps (2 running + 1 standby, N+1)
Flow per pump: 3,050 L/min (50% capacity)
Total Head: 30m (98 ft) - includes intake lift + piping + HX pressure drop
Power per pump: 40 kW (54 HP)
Total Power (running): 80 kW
Drive: VFD for variable flow control
Location: River-edge enclosure (100m from data center)
Critical Power: Yes (fed from 400V via 100m underground cable)
```

### **Piping:**
- **Material:** DN200 (8") HDPE
- **Route:** River intake → 20m → Enclosure → 20m → River discharge
- **Total Length:** 40m (intake + discharge)
- **Burial:** 1.5m depth for frost protection

---

## RIVER-EDGE ENCLOSURE & HEAT EXCHANGERS

### **Enclosure Specifications:**
- **Location:** 100m from data center, at Kura River bank (elevated above 100-year flood)
- **Structure:** Precast concrete vault
- **Dimensions:** 10m × 6m × 3.5m (L × W × H interior)
- **Footprint:** 60 m² interior
- **Foundation:** Reinforced concrete, elevated 1m above flood level
- **Access:** Paved service road, lockable steel door, card reader, CCTV
- **Environmental Control:** Ventilation, heating (freeze protection), drainage sump pump

### **Plate Heat Exchangers:**
```
Configuration: 2 × 2,000 kW Capacity (N+1 Redundancy)
Total Capacity: 4,000 kW > 3,844 kW required ✓
Type: Brazed plate, stainless steel (316L)
Primary Side (CW): Closed condenser water loop (5,508 L/min total)
Secondary Side (RW): Kura River water (6,100 L/min total)
Approach Temperature: 3°C (typical for plate HX)
Pressure Drop: 50 kPa (primary), 50 kPa (secondary)
Isolation: Each HX has isolation valves for independent maintenance
Brands: Alfa Laval, SWEP, Danfoss (available via Turkey/Georgia)
Dimensions (each): 1.8m × 1.0m × 1.4m (H × W × D)
Weight: ~1,200 kg empty
Connections: DN200 (8") flanged
```

### **Filtration & Treatment:**
- **Coarse Screen (at intake):** 50mm bar spacing (trash rack), removes large debris, fish
- **Fine Screen (at enclosure):** 10mm traveling screen, automatic backwash
- **Automatic Strainers:** 2 × 100% duty, 100-200 micron, self-cleaning backflush
- **Chemical Treatment:** Minimal intermittent low-dose chlorination (~0.5 ppm) for biofouling control
- **Monitoring:** Flow, temperature, pressure differential, conductivity, pH

### **Bypass & Isolation Valves:**
- **Bypass Valves:** 2 × motorized 3-way valves (DN200) on CW loop
- **Purpose:** Allow CW to bypass heat exchangers during maintenance or when river temp too high
- **Isolation Valves:** 8 × butterfly valves (DN200) to isolate individual heat exchangers
- **Control:** BMS-integrated PLC logic, automatic mode switching

---

## FREE COOLING OPTIMIZATION (KURA RIVER ECONOMIZATION)

### **River Temperature Range:** 6°C (winter) to 27°C (summer)
### **CHW Supply Target:** 12°C

### **Cooling Modes:**

**1. 100% Free Cooling (River < 10°C):** ~5,500 hours/year (November-April)
```
Operation: Chillers OFF, river water cools CW to 9-13°C
Method: CW produces CHW at 12°C via additional plate HX or direct (if compatible)
Energy: Pumps only (270 kW) vs. pumps + chillers (861 kW)
Savings: 69% energy reduction vs. full mechanical cooling
Annual Cost Savings: ~$125,000/year vs. no free cooling
```

**2. Partial Free Cooling (River 10-23°C):** ~2,000 hours/year (May, October)
```
Operation: Chillers ON at reduced load (30-70%)
Method: River pre-cools condenser water, reducing chiller lift
Energy Savings: 30-50% vs. full mechanical cooling
```

**3. Full Mechanical (River > 23°C):** ~1,260 hours/year (June-September)
```
Operation: Chillers ON at full load
Method: River water provides condenser cooling (more efficient than air-cooled)
Chiller COP: 5.5 (vs. 3.5 for air-cooled = 57% more efficient)
```

### **Annual PUE Performance:**
```
Design Maximum PUE: 1.50 (full mechanical cooling)
Free Cooling PUE: 1.20 (chillers off, pumps only)
Annual Weighted Average PUE: 1.30 (25% improvement over design)
```

---

## DATA HALL COOLING DISTRIBUTION

### **In-Row Cooling Units:**
```
Configuration: 24 × 150 kW Units (N+1 Distributed Redundancy)
Total Capacity: 3,600 kW installed
Running Capacity: 3,450 kW (23 units running)
Margin: 3,450 / 3,253 = 106% ✓
Supply Air Temp: 18-20°C
Airflow: ~2,000 CFM per unit (total 46,000 CFM)
Fan Power: ~3.5 kW per unit (total 84 kW for 24 units)
Brands: Stulz, Schneider (APC InRow), Vertiv
Control: BMS-integrated, modulating control based on room temperature
Redundancy: Any unit can fail without IT impact (N+1 distributed)
```

### **Hot Aisle / Cold Aisle Containment:**
- **Configuration:** Hot aisle containment (recommended)
- **Supply:** Cold air to cold aisles (18-20°C)
- **Return:** Hot air from hot aisles (28-30°C)
- **Benefits:** Improved efficiency, prevents mixing, allows higher return temps

---

## ENVIRONMENTAL IMPACT (KURA RIVER)

### **River Water Usage:**
```
Intake Flow: 6,100 L/min = 366,000 L/hr = 8,784,000 L/day
Annual Usage: 3,206,160 m³/year (365 days)
Note: 100% of intake water is returned to river (closed loop, zero consumption)
```

### **Thermal Discharge:**
```
Heat Rejected: 3,844 kW = 3,844,000 W
Temperature Rise (ΔT): 10°C average
Discharge Temperature: River temp + 10°C
  - Winter: 6°C + 10°C = 16°C discharge
  - Summer: 27°C + 10°C = 37°C discharge
```

### **River Mixing Analysis:**
```
Kura River Summer Low Flow: ~800 m³/s (minimum)
Data Center Discharge: 0.102 m³/s
Discharge Proportion: 0.102 / 800 = 0.013% of river flow
Temperature Rise at 100m Downstream (complete mixing):
  ΔT_river = (Q_dc / Q_river) × ΔT_discharge
  ΔT_river = (0.102 / 800) × 10°C = 0.0013°C

Conclusion: NEGLIGIBLE impact on river temperature (<0.002°C rise)
Compliance: Meets all Georgian and EU environmental standards (3°C limit)
```

---

## COOLING SYSTEM POWER CONSUMPTION

| Equipment | Qty Running | Power Each (kW) | Total Power (kW) | % of Cooling |
|-----------|-------------|-----------------|------------------|--------------|
| **Full Mechanical Mode** |
| Chillers (compressors) | 2 | 327 | 654 | 71% |
| CHW Pumps | 2 | 45 | 90 | 10% |
| CW Pumps | 2 | 52 | 104 | 11% |
| River Water Pumps | 2 | 40 | 80 | 9% |
| **Total (Mechanical)** | | | **928 kW** | **100%** |
| **Free Cooling Mode** |
| Chillers | 0 | 0 | 0 | 0% |
| CHW Pumps | 2 | 45 | 90 | 33% |
| CW Pumps | 2 | 52 | 104 | 39% |
| River Water Pumps | 2 | 40 | 80 | 30% |
| **Total (Free Cooling)** | | | **274 kW** | **100%** |
| **Energy Savings** | | | **654 kW** | **70%** |

---

## EQUIPMENT COST ESTIMATE

| Equipment | Cost (USD) |
|-----------|------------|
| **Chillers** |
| 3 × 1,800 kW Water-Cooled Chillers | $900,000 |
| Chiller Installation & Piping | $150,000 |
| **Pumps** |
| 3 × CHW Pumps (45 kW, VFD) | $90,000 |
| 3 × CW Pumps (52 kW, VFD) | $105,000 |
| 3 × River Water Pumps (40 kW, VFD) | $100,000 |
| **In-Row Cooling** |
| 24 × 150 kW In-Row Units | $720,000 |
| Hot Aisle Containment | $100,000 |
| **River Infrastructure** |
| River-Edge Enclosure (concrete vault) | $150,000 |
| 2 × Plate Heat Exchangers (2,000 kW) | $150,000 |
| Filtration (screens + strainers) | $80,000 |
| CW Piping (200m DN200 insulated) | $80,000 |
| River Piping (40m DN200) | $10,000 |
| Valves, Controls, Instrumentation | $100,000 |
| Intake/Discharge Structures | $60,000 |
| 400V Power Feed to Enclosure (100m) | $20,000 |
| Installation & Commissioning | $180,000 |
| **CHW Distribution** |
| Piping, Valves, Insulation (CHW) | $200,000 |
| **TOTAL COOLING SYSTEMS** | **$3,195,000** |

**Cost per kW IT:** $3,195,000 / 2,933 kW = **$1,090 per kW** (excellent for water-cooled with river economization)

---

## KEY DESIGN NOTES

1. **Chiller Sizing:** 3 × 1,800 kW provides 11% margin with N+1 redundancy. 1,600 kW chillers would be marginal (98% utilization).

2. **Free Cooling:** ~5,500 hours/year of 100% free cooling (63% of year) provides significant energy savings and improves annual PUE to 1.30.

3. **River Impact:** Negligible thermal impact on Kura River (<0.002°C temperature rise at 100m downstream).

4. **In-Row Units:** 24 units (N+1 distributed) allows any single unit failure without IT impact. Better than centralized CRAC/CRAH approach.

5. **Pump Sizing:** All pumps sized with N+1 redundancy. VFD control provides energy savings at part load.

6. **Concurrent Maintainability:** All major components (chillers, pumps, heat exchangers) have isolation valves for maintenance without shutdown.

7. **Standards Compliance:** ASHRAE 90.1-2019, ASHRAE 127-2012 (data center thermal guidelines), Georgian environmental regulations.

---

**Prepared by:** EVS / GGE Engineering Team
**Date:** November 4, 2025
**Revision:** 01 - Scaled for 3.0 MW IT
**Status:** For Review
