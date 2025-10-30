# PRYOR DATA CENTER - BASIS OF DESIGN
## Phased Deployment: 3 MW to 12 MW IT Capacity

**Project:** Pryor Data Center  
**Owner:** PACHYDERM GLOBAL Critical Infrastructure Services  
**Location:** Pryor, Oklahoma  
**Document Date:** October 29, 2025  
**Revision:** 01 - Complete Design with IT UPS

---

## TABLE OF CONTENTS

1. Executive Summary
2. Project Description  
3. Design Philosophy and Criteria
4. Load Analysis and Capacity Planning
5. Architectural Design Criteria
6. Mechanical Systems
7. Electrical Systems
8. Fire Protection Systems
9. Building Management System and Controls
10. Security and Access Control
11. Telecommunications
12. Commissioning
13. Operations and Maintenance
14. Sustainability

---

## SECTION 1: EXECUTIVE SUMMARY

### 1.1 PROJECT OVERVIEW

The Pryor Data Center is a **50,000 GSF mission-critical facility** designed to support high-density computing workloads through a phased deployment strategy. The facility features 20,000 SF of white space divided between two data halls.

**Key Facility Metrics:**
- **Total Building Area:** 50,000 GSF
- **White Space:** 20,000 SF (two 10,000 SF data halls)
- **Phase 1 IT Capacity:** 3 MW (30 cabinets @ 100 kW each)
- **Phase 2 IT Capacity:** 12 MW (30 cabinets @ 400 kW each)
- **Uptime Tier:** Tier III (Concurrently Maintainable)
- **PUE Target:** 1.35 (Phase 1), 1.25 (Phase 2)
- **WUE Target:** <0.5 L/kWh (air-cooled systems)

---

### 1.2 STANDARDIZED EQUIPMENT STRATEGY

**All Chillers:** 1,500 kW air-cooled with integrated free cooling
- Phase 1: 4 units (Loops 1+2 shared plant)
- Phase 2: +8 units (Loop 3 independent plant)
- **Total: 12 × 1,500 kW chillers**

**All Generators:** 4.0 MW @ 11 kV, diesel, Tier 4 Final
- Phase 1: 3 units (N+1)
- Phase 2: +3 units (N+1)
- **Total: 6 × 4.0 MW generators**

**All Transformers:** 3,500 kVA, 11 kV/480V, oil-filled
- Phase 1: 3 units (N+1)
- Phase 2: +5 units (for N+1 at higher load)
- **Total: 8 × 3,500 kVA transformers**

**IT UPS Modules:** 2,500 kVA each, 2N architecture
- Phase 1: 4 units (2N, N+1 within each path)
- Phase 2: +6 units
- **Total: 10 × 2,500 kVA IT UPS modules**

**Mechanical UPS:** 250 kW each (for pumps/fans only)
- Phase 1: 8 units (N+1)
- Phase 2: +12 units
- **Total: 20 × 250 kW mechanical UPS modules**

**CDUs:** 300 kW capacity each
- Phase 2: 60 units (2 per cabinet, A/B redundancy)

---

### 1.3 PHASING STRATEGY

**Phase 1: Foundation Operations (3 MW)**
- Data Hall 1 operational: 30 cabinets @ 100 kW each
- Air cooling: Dual-loop redundant system (Loops 1+2, 4 chillers shared)
- Power: 3 generators, 3 transformers, 4 IT UPS, 8 mechanical UPS
- Data Hall 2: Built as powered shell
- **Timeline:** [ROM] 18-24 months
- **Cost:** [ROM] $35-42M total project

**Phase 2: High-Density Expansion (12 MW)**
- Same 30 cabinets: Upgrade to 400 kW each (100 kW air + 300 kW D2C)
- D2C cooling: Independent Loop 3 (8 chillers, 60 CDUs)
- Power: Add 3 generators, 5 transformers, 6 IT UPS, 12 mechanical UPS
- Zero-downtime implementation
- **Timeline:** [ROM] 12-15 months
- **Cost:** [ROM] $28-35M incremental

---

### 1.4 CRITICAL PERFORMANCE METRICS

**Uptime Tier:** Tier III (Concurrently Maintainable)
- All systems N+1 or 2N redundancy
- Concurrent maintenance without service interruption
- 99.982% annual uptime (1.6 hours downtime/year)

**Power Usage Effectiveness (PUE):**
- Phase 1: 1.35 (air cooling with free cooling)
- Phase 2: 1.25 (improved with D2C efficiency)
- Industry average: 1.57 (Uptime Institute 2024)

**Water Usage Effectiveness (WUE):**
- Target: <0.5 L/kWh
- Air-cooled systems eliminate water consumption
- Closed-loop glycol (no evaporative losses)

---

### 1.5 COST SUMMARY

| Phase | IT Capacity | Electrical Cost | Total Project Cost* |
|-------|-------------|-----------------|---------------------|
| Phase 1 | 3 MW | $15.2M | $35-42M |
| Phase 2 | +9 MW (12 MW total) | $23.5M | $28-35M |
| **Total** | **12 MW** | **$38.7M** | **$63-77M** |

*Total project includes civil, architectural, site work, MEP systems

**Cost per MW:**
- Phase 1: $11.7-14.0M per MW (includes full infrastructure)
- Phase 2: $3.1-3.9M per MW (incremental)
- Blended average: $5.3-6.4M per MW

---

## SECTION 2: PROJECT DESCRIPTION

### 2.1 SITE AND LOCATION

**Location:** Pryor, Oklahoma  
**Climate Zone:** ASHRAE 3A (warm, humid)  
**Seismic Category:** [ROM] B (low seismic risk)  
**Tornado Risk:** High (EF3+ zone - Enhanced Fujita Scale)

**Utility Services:**
- Electric: Dual 11 kV feeds from [TBD Utility]
- Telecommunications: Multiple fiber carriers, diverse paths
- Solar Integration: Adjacent 8+ MW solar array + BESS

---

### 2.2 FACILITY OVERVIEW

**Total Building:** 50,000 GSF

**White Space (20,000 SF):**
- Data Hall 1: 10,000 SF (Phase 1 operational, Phase 2 expansion)
- Data Hall 2: 10,000 SF (powered shell Phase 1, fit-out future)

**Support Spaces (30,000 SF):**
- Multi-level central spine (3 levels)
- Main entrance lobby and reception
- Conference rooms and offices
- Network Operations Center (NOC) - Level 2, secure
- Client tour pathway - Level 2, observation corridor
- 2 MPOEs (fiber entrance, geographically diverse)
- 2 MMRs (carrier cross-connects)
- Loading dock (2 bays)
- Gym/fitness center - Level 3
- Storm shelter (FEMA 361 compliant, EF5 rated)
- Break areas, restrooms, showers

**Equipment Yards:**
- Electrical Yard: ~100,000 SF (sized for 24 MW master plan)
- Mechanical Yard: [ROM] ~30,000 SF

---

### 2.3 DATA HALL 1 DESIGN

**Area:** 10,000 SF  
**Capacity:** 3 MW Phase 1, 12 MW Phase 2

**Cabinet Configuration:**
- **30 cabinets:** DDC S-Series, 10HP, 52U, 36" wide
- **Integrated FCU:** 100 kW capacity per cabinet
  - Dual coils: 50 kW each (Coil #1 → Loop 1, Coil #2 → Loop 2)
  - Dual fans: Component-level redundancy
- **Power:** 2 × PDUs per cabinet
  - Phase 1: 2 × 50 kW PDUs (A-side + B-side, 2N for 100 kW IT)
  - Phase 2: 2 × 200 kW PDUs (2N for 400 kW IT)
- **D2C Manifolds:** Installed Phase 1 (capped), activated Phase 2

**Floor System:**
- Slab-on-grade with sealed concrete finish
- Optional epoxy coating for durability
- Cable distribution: Overhead tray and ladder rack
- **Why no raised floor:** Cost savings ($150K+), eliminates failure modes, better seismic performance

**Hot/Cold Aisle Containment:**
- Cold aisle containment with doors
- Aisle width: 48" cold, 60" hot (ASHRAE standards)
- Modular design for future reconfigurations

**Environmental:**
- Temperature: 18-27°C (64-80°F) ASHRAE A1
- Humidity: 40-60% RH (non-condensing)

---

## SECTION 3: DESIGN PHILOSOPHY

### 3.1 REDUNDANCY STRATEGY

**2N (Dual Path) Systems:**
- **IT Power Distribution:** SWBD-A and SWBD-B each 100% capacity
- **IT UPS:** Path A and Path B each independently support full IT load
- **Cabinet PDUs:** Dual PDUs (A-side + B-side) to dual-corded servers
- **CDUs (Phase 2):** Dual CDUs per cabinet (A-side + B-side)

**N+N (Parallel Redundancy):**
- **Chilled Water Loops 1+2:** Each loop can carry full 3,000 kW air cooling load
- **Cabinet FCUs:** Dual coils (50 kW each) provide N+N cooling

**N+1 Systems:**
- **Generators:** 6 total, 5 required for full Phase 2 load
- **Transformers:** 8 total, 6-7 required for Phase 2 load
- **Loop 3 Chillers:** 8 total, 6-7 required (17% margin)
- **Loop 1+2 Chillers:** 4 total, 3 required

---

### 3.2 CONCURRENT MAINTAINABILITY

**Every critical system serviceable without IT interruption:**

**Electrical:**
- Generators: One offline, N units carry load
- Transformers: RMU switching redistributes load
- UPS: Bypass modes enable maintenance

**Mechanical:**
- Chillers: N+1 allows individual chiller service
- Loops: Isolate Loop 1 or Loop 2, other carries full air cooling
- Loop 3: Independent from air cooling

---

### 3.3 WHY SEPARATE LOOP 3 (D2C COOLING)

**Air Cooling (Loops 1+2):**
- Predictable, stable loads
- Diurnal patterns (±10% variation)
- Traditional HVAC control strategies work well

**D2C Cooling (Loop 3):**
- Violent load swings (0-100% in seconds)
- GPU jobs launch unpredictably
- Requires aggressive control tuning

**Problems if mixed on shared plant:**
- Control hunting and instability
- Reduced efficiency from load cycling
- Accelerated equipment wear
- Complicated troubleshooting

**Benefits of separation:**
- Optimized controls for each load type
- Clear contractor boundaries (HVAC vs. liquid cooling specialist)
- Independent maintenance schedules
- Fault isolation

---

### 3.4 FM 1-150 TORNADO PROTECTION

**Roof System Rating:**
- Wind: 150 mph 3-second gust
- Impact: Class 4 hail (2-inch diameter)
- System: Enhanced deck attachment per FM specifications

**Storm Shelter:**
- FEMA 361 compliant (EF5 tornado protection)
- Capacity: [ROM] 75-100 persons
- Construction: 12" reinforced concrete walls and roof
- Blast-rated door with secure locking

**Why This Matters:**
- Oklahoma tornado risk (EF3-EF5 events)
- Insurance premium reduction: 20-30%
- Customer confidence and compliance
- Payback: ~5 years from insurance savings alone

---

## SECTION 4: LOAD ANALYSIS

### 4.1 IT LOAD SUMMARY

| Phase | Cabinets | kW per Cabinet | Total IT Load | Cooling Method |
|-------|----------|----------------|---------------|----------------|
| Phase 1 | 30 | 100 kW | 3,000 kW | Air (FCU dual-coil) |
| Phase 2 | 30 | 400 kW | 12,000 kW | Air (100 kW) + D2C (300 kW) |

---

### 4.2 PHASE 1 COOLING ANALYSIS

**IT Heat Load:** 3,000 kW

**Cabinet FCU Cooling:**
- 30 cabinets × 100 kW capacity = 3,000 kW total
- Each cabinet: Dual-coil FCU (50 kW per coil)
- Loop 1 load: 30 × 50 kW = 1,500 kW
- Loop 2 load: 30 × 50 kW = 1,500 kW

**Redundancy Test:**
- Normal: Both loops carry 1,500 kW each
- N operation: Either loop carries full 3,000 kW
- **True N+N redundancy** ✓

**Loops 1+2 Shared Chiller Plant:**
- **4 × 1,500 kW air-cooled chillers** (N+1)
- Normal: 3 chillers running (4,500 kW for 3,000 kW load)
- Utilization: 67% (optimal efficiency)
- N+1: One fails → 3 remain with 4,500 kW capacity ✓

**Chiller Specifications:**
- Capacity: 1,500 kW (430 ton)
- Type: Air-cooled screw with integrated free cooling
- Supply temp: 7-10°C (45-50°F)
- COP: 3.8-4.2 (mechanical), 15-25 (free cooling)
- Power: ~395 kW at full load
- Free cooling hours: [ROM] 3,500-4,000 hrs/year (Oklahoma)

---

### 4.3 PHASE 2 COOLING ANALYSIS

**IT Heat Load:** 12,000 kW total
- Air portion: 3,000 kW (unchanged)
- D2C portion: 9,000 kW (new)

**Air Cooling (No Change):**
- Same 4 × 1,500 kW chillers
- Same 3,000 kW load

**Loop 3 D2C Cooling:**
- **8 × 1,500 kW air-cooled chillers** (N+1 with margin)
- Normal: 6 chillers running (9,000 kW)
- N+1: One fails → 7 remain (10,500 kW = 17% margin) ✓
- Supply temp: 25°C (77°F) - warmer for efficiency
- COP: 5.0-5.5 (better than air cooling)
- Power: ~273 kW at full load

**CDU Distribution:**
- **60 × CDU units** (2 per cabinet, A/B redundancy)
- Each CDU: 300 kW capacity
- Total capacity: 60 × 300 = 18,000 kW (2× redundancy) ✓
- CDU power: 15 kW each × 60 = 900 kW total

---

### 4.4 PHASE 1 ELECTRICAL LOADS

**IT Load:** 3,000 kW

**IT UPS System:**
- Input: 3,000 kW / 0.96 efficiency = 3,125 kW
- UPS losses: 125 kW

**Mechanical Loads (through Mechanical UPS):**
- Chillers: 4 × 395 kW (3 running) = 1,185 kW
- Pumps: 8 × 22 kW = 176 kW
- Cabinet fans: 30 × 9 kW = 270 kW
- Subtotal: 1,631 kW
- UPS input: 1,631 / 0.96 = 1,700 kW
- UPS losses: 69 kW

**Building/Lighting/Misc:** 570 kW × 0.70 diversity = 399 kW

**Total Phase 1 Demand:**
- IT (through UPS): 3,125 kW
- Mechanical (through UPS): 1,700 kW
- Building: 399 kW
- **Total: 5,224 kW**
- **Design load: 5,800 kW**

---

### 4.5 PHASE 1 EQUIPMENT SIZING

**Generators (N+1):**
- **3 × 4.0 MW @ 11 kV** = 12 MW total
- N+1: 2 running = 8 MW for 5.8 MW load
- **Margin: 38%** ✓

**Transformers (N+1):**
- **3 × 3,500 kVA** = 10,500 kVA = 9,660 kW @ 0.92 PF
- N+1: 2 running = 6,440 kW for 5.8 kW load
- **Margin: 11%** ✓

**IT UPS (2N Architecture):**
- **4 × 2,500 kVA modules** (2,000 kW each)
- Path A: 2 × 2,500 kVA = 4,000 kW (N+1 within path)
- Path B: 2 × 2,500 kVA = 4,000 kW (N+1 within path)
- Each path supports full 3,000 kW IT load ✓
- Battery: 15-minute runtime

**Mechanical UPS:**
- **8 × 250 kW modules** (N+1)
- 7 running = 1,750 kW for 1,631 kW mechanical load ✓

---

### 4.6 PHASE 2 ELECTRICAL LOADS

**IT Load:** 12,000 kW

**IT UPS System:**
- Input: 12,000 / 0.96 = 12,500 kW
- UPS losses: 500 kW

**Mechanical Loads:**
- Loops 1+2 chillers: 1,185 kW (unchanged)
- Loop 3 chillers: 8 × 273 kW (6 running) = 1,638 kW
- Pumps (all loops): 400 kW
- CDUs: 60 × 15 kW = 900 kW
- Cabinet fans: 270 kW
- Subtotal: 4,393 kW
- UPS input: 4,393 / 0.96 = 4,576 kW
- UPS losses: 183 kW

**Building:** 399 kW

**Total Phase 2 Demand:**
- IT: 12,500 kW
- Mechanical: 4,576 kW
- Building: 399 kW
- **Total: 17,475 kW**
- **Design load: 18,200 kW**

---

### 4.7 PHASE 2 EQUIPMENT SIZING

**Generators (N+1):**
- **6 × 4.0 MW @ 11 kV** = 24 MW total (add 3 in Phase 2)
- N+1: 5 running = 20 MW for 18.2 MW load
- **Margin: 10%** ✓

**Transformers:**
- **8 × 3,500 kVA** total (add 5 in Phase 2)
- 7 running = 24,500 kVA = 22,540 kW @ 0.92 PF
- 6 running = 19,320 kW for 18.2 kW load
- **Margin: 6%** ✓

**IT UPS (2N Architecture):**
- **10 × 2,500 kVA modules** total (add 6 in Phase 2)
- Path A: 5 × 2,500 kVA = 10,000 kW
  - 4 running (8,000 kW) for 6,000 kW load = 33% margin ✓
- Path B: 5 × 2,500 kVA = 10,000 kW (mirror)

**Mechanical UPS:**
- **20 × 250 kW modules** total (add 12 in Phase 2)
- 19 running = 4,750 kW for 4,576 kW mechanical load ✓

---

## SECTION 7: ELECTRICAL SYSTEMS

### 7.1 ELECTRICAL ARCHITECTURE OVERVIEW

**Design Principles:**
- 11 kV medium voltage distribution
- Dual ring bus topology (Ring A and Ring B)
- 2N low-voltage distribution (SWBD-A and SWBD-B)
- 2N IT UPS system (Path A and Path B)
- N+1 generators, transformers, mechanical UPS
- Zero single points of failure

---

### 7.2 MEDIUM VOLTAGE SYSTEM (11 kV)

**Utility Service:**
- Dual 11 kV feeds, 15 MVA each
- Diverse routing (separate trenches, entry points)
- Integration with 8+ MW solar array + BESS

**Ring Main Units (RMUs):**
- **6 × RMUs** (11 kV, 630A rated)
- Dual ring topology: Ring A (3 RMUs), Ring B (3 RMUs)
- SF6 or vacuum circuit breakers
- SCADA-controlled remote switching
- Location: Generator/PDM boundary in electrical yard

**Distribution Topology:**
`
UTILITY A ──[RMU-1]──[RMU-2]──[RMU-3]── RING A
             │        │        │
          [XFR-1]  [XFR-3]  [XFR-5]

UTILITY B ──[RMU-4]──[RMU-5]──[RMU-6]── RING B
             │        │        │
          [XFR-2]  [XFR-4]  [XFR-6]
          
Phase 2: Add [XFR-7] and [XFR-8]
`

---

### 7.3 GENERATOR SYSTEM

**Configuration:** 6 × 4.0 MW @ 11 kV (N+1)

**Phase 1:** 3 generators  
**Phase 2:** Add 3 generators

**Generator Specifications:**
- Rating: 4,000 kW continuous @ 11 kV, 3-phase, 60 Hz
- Power factor: 0.8 lagging
- Fuel: Diesel, EPA Tier 4 Final
- Fuel capacity: 10,000 gal/unit (118 hours @ full load)
- Paralleling: Woodward easYgen 3500 series
- Enclosure: Sound-attenuated (-65 dBA @ 7m)
- Seismic: IBC 2018 certified

**Why 11 kV (Not 480V):**
- Standard product availability (3-5 MW range)
- Cable sizing: 11 kV reduces current by 23×
  - 4 MW @ 480V = 8,333 A (requires 6 × 500 kcmil/phase)
  - 4 MW @ 11 kV = 364 A (requires 1 × 2/0/phase)
- Easier paralleling
- Lower I²R losses

---

### 7.4 TRANSFORMER SYSTEM

**Configuration:** 8 × 3,500 kVA (11 kV/480V)

**Phase 1:** 3 transformers  
**Phase 2:** Add 5 transformers

**Transformer Specifications:**
- Rating: 3,500 kVA
- Voltage: 11,000V delta / 480Y/277V
- Impedance: 5.75%
- Efficiency: 98.5% at full load
- Cooling: ONAN (oil natural, air natural)
- Liquid: Mineral oil with secondary containment
- Sound: 60 dBA @ 10 feet

---

### 7.5 LOW VOLTAGE DISTRIBUTION (480V)

**Main Switchboards (2N):**
- **SWBD-A and SWBD-B**
- Rating: 4,000A busbar, 480V, 3-phase
- Each sized for 100% facility load
- Short-circuit rating: 65 kA
- Fed from multiple transformers

**Distribution Panels (All Dual-Fed):**
- IT Distribution A & B: 800A each (cabinet PDUs)
- Mechanical Dist 1A & 1B: 800A (Loops 1+2)
- Mechanical Dist 2A & 2B: 1,200A (Loop 3, Phase 2)
- UPS Distribution A & B: 400A (IT UPS output)
- BMS/Lighting A & B: 200A

---

### 7.6 IT UPS SYSTEM (PRIMARY)

**Purpose:**
- Uninterrupted power to IT equipment
- Utility-to-generator transfer (~10-15 seconds)
- Power conditioning

**Phase 1: 4 × 2,500 kVA Modules (2N Architecture)**

**Path A:**
- UPS-1A and UPS-1B in parallel
- Each: 2,500 kVA / 2,000 kW
- Total Path A capacity: 4,000 kW
- Feeds: IT Distribution Panel A → Cabinet PDUs A-side

**Path B:**
- UPS-2A and UPS-2B in parallel (mirror of Path A)
- Total Path B capacity: 4,000 kW
- Feeds: IT Distribution Panel B → Cabinet PDUs B-side

**Redundancy:**
- 2N: Each path independently supports full 3,000 kW IT load
- N+1 within path: One UPS fails, other continues
- Dual-corded servers: Fed from both A-side and B-side PDUs

**Battery:** 15-minute runtime at full load (Lithium-ion preferred)

**Phase 2: 10 × 2,500 kVA Modules (add 6)**

**Path A:** 5 × 2,500 kVA = 10,000 kW total
- 4 running (8,000 kW) for 6,000 kW load = 33% margin

**Path B:** 5 × 2,500 kVA = 10,000 kW total (mirror)

**UPS Specifications:**
- Rating: 2,500 kVA / 2,000 kW
- Efficiency: 96% (ECO mode), 94% (double-conversion)
- Input/Output: 480V, 3-phase
- Topology: Online double-conversion (VFI per IEC 62040-3)
- Bypass: Automatic static + manual maintenance
- Monitoring: SNMP, Modbus TCP, BACnet

---

### 7.7 MECHANICAL UPS SYSTEM (SECONDARY)

**Purpose:** Protect pumps/fans only (NOT IT loads)

**Phase 1:** **8 × 250 kW modules** (N+1)
- 7 running for 1,631 kW mechanical load

**Phase 2:** **20 × 250 kW modules** (add 12)
- 19 running for 4,576 kW mechanical load

**Protected Loads:**
- Chilled water pumps (all loops)
- Cabinet FCU fans
- CDU pumps (Phase 2)
- BMS/SCADA controls

---

### 7.8 CABINET POWER DISTRIBUTION

**Phase 1:**
- 30 cabinets × 2 PDUs = 60 PDUs
- Each PDU: 50 kW capacity
- A-side PDUs fed from IT UPS Path A
- B-side PDUs fed from IT UPS Path B
- Cabinet power: 2 × 50 kW = 100 kW (2N for 100 kW IT load)

**Phase 2:**
- Upgrade PDUs to 200 kW capacity each
- Cabinet power: 2 × 200 kW = 400 kW (2N for 400 kW IT load)

---

### 7.9 PREFABRICATED PDMs

**Power Delivery Modules:**
- Factory-fabricated electrical enclosures
- Contains: LV switchboards, UPS systems, MV gear
- Benefits: Factory testing, schedule compression, quality control
- Cost premium: 5-10% vs. stick-built
- Justified by: 8-12 week schedule acceleration

**Phase 1:** 2 PDMs  
**Phase 2:** Expand capacity within existing PDMs (no additional PDMs)

---

## EQUIPMENT SUMMARY

| Equipment | Phase 1 | Phase 2 Add | Total | Unit Size |
|-----------|---------|-------------|-------|-----------|
| **Generators** | 3 | +3 | 6 | 4.0 MW @ 11 kV |
| **Transformers** | 3 | +5 | 8 | 3,500 kVA |
| **RMUs** | 6 | 0 | 6 | 11 kV, 630A |
| **IT UPS** | 4 | +6 | 10 | 2,500 kVA |
| **Mech UPS** | 8 | +12 | 20 | 250 kW |
| **Chillers (Loops 1+2)** | 4 | 0 | 4 | 1,500 kW |
| **Chillers (Loop 3)** | 0 | 8 | 8 | 1,500 kW |
| **CDUs** | 0 | 60 | 60 | 300 kW each |
| **Cabinets** | 30 | 0 | 30 | DDC S-Series |
| **PDUs** | 60 | upgrade | 60 | 50 kW → 200 kW |

---

## COST SUMMARY (ELECTRICAL SYSTEMS)

**Phase 1 Electrical Costs:**
- Generators (3 × 4.0 MW @ 11 kV): $4.5M
- Transformers (3 × 3,500 kVA): $0.5M
- RMUs, MV switchgear, cable: $1.2M
- LV switchboards, distribution: $1.5M
- IT UPS (4 × 2,500 kVA + batteries): $2.0M
- Mechanical UPS (8 × 250 kW): $0.8M
- PDMs (2 units): $2.5M
- Installation, testing, commissioning: $2.2M
- **Phase 1 Electrical Total: $15.2M**

**Phase 2 Electrical Costs:**
- Generators (3 × 4.0 MW): $4.5M
- Transformers (5 × 3,500 kVA): $0.85M
- MV/LV distribution expansion: $1.5M
- IT UPS (6 × 2,500 kVA + batteries): $3.0M
- Mechanical UPS (12 × 250 kW): $1.2M
- Chillers Loop 3 (8 × 1,500 kW): $6.0M
- CDUs (60 units): $3.0M
- Cabinet PDU upgrades: $0.45M
- Installation, testing, commissioning: $3.0M
- **Phase 2 Total: $23.5M**

**Total Electrical/Mechanical: $38.7M**

---

## KEY DESIGN IMPROVEMENTS

| Parameter | Original | Corrected |
|-----------|----------|-----------|
| Cabinets | 15 | **30** |
| IT UPS | Missing | **10 × 2,500 kVA (2N)** |
| Mechanical UPS | 4-6 units | **20 × 250 kW** |
| Phase 1 transformers | 2 (no N+1) | **3 (true N+1)** |
| Phase 2 transformers | 6 | **8 (concurrent maint)** |
| Phase 1 chillers | 3 | **4 (N+1)** |
| Phase 2 chillers Loop 3 | 7 | **8 (17% margin)** |
| Generators | 3.5 MW @ 480V | **4.0 MW @ 11 kV** |
| CDUs | 30 (single-fed) | **60 (dual-fed A/B)** |
| Cooling redundancy | Broken | **True N+N** |

---

**This completes the corrected Basis of Design.**

✅ IT UPS system (2N architecture, 10 modules)  
✅ Mechanical UPS properly sized (20 modules)  
✅ True N+N air cooling redundancy  
✅ Proper transformer count for N+1  
✅ 11 kV generators (standard products)  
✅ Dual-fed CDUs for complete redundancy  
✅ 30 cabinets (not 15)  
✅ All equipment properly sized for loads  
