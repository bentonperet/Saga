**Created:** 2025-11-05
**Tags:** #liquid-cooling #l2c #direct-to-chip #best-practices #reference #cooling-design
**Related:** [[5BOD - HVAC (CSI Div 23)]], [[7BOD - Electrical (CSI Div 26) v2]]

# L2C BEST PRACTICES: DIRECT-TO-CHIP LIQUID COOLING DESIGN GUIDE

## DOCUMENT PURPOSE

This document provides comprehensive best practices for designing, specifying, and implementing Liquid-to-Chip (L2C) direct-to-chip cooling systems for high-density AI/ML data center applications. It serves as a technical reference for Basis of Design (BOD) development and detailed engineering design.

---

## 1.0 SYSTEM OVERVIEW & FUNDAMENTALS

### 1.1 What is L2C Direct-to-Chip Cooling?

**Definition:** L2C cooling delivers liquid coolant directly to cold plates mounted on high-heat components (CPUs, GPUs, memory, power modules), capturing heat at the source before it enters the air stream.

**Key Characteristics:**
- **Heat Capture:** 80-100% of component heat removed via liquid (remaining 0-20% via air)
- **Heat Transfer Capacity:** 3,500× greater than air cooling
- **Typical Applications:** AI training clusters, HPC, GPU compute (>70kW/rack)
- **Rack Densities:** 70 kW to 600+ kW per rack (with extreme densities expected by 2027)

### 1.2 When L2C is Required

**Mandatory for:**
- Rack densities >70 kW (air cooling physical limit)
- NVIDIA GB200/GB300 systems (163 kW typical, up to 300+ kW)
- Future NVL144/NVL576 platforms (300-600+ kW per rack)
- AI inference clusters with sustained high utilization

**Not Required for:**
- Traditional enterprise servers (<10 kW/rack)
- Storage arrays
- Network switches
- Low-density compute (<25 kW/rack) - can use rear-door heat exchangers (RDHx)

---

## 2.0 SYSTEM ARCHITECTURE

### 2.1 Three-Loop Architecture (Recommended)

**Primary Loop (Facility Water):**
- Source: Air-cooled chillers, dry coolers, or hybrid systems
- Fluid: 25% propylene glycol / 75% water
- Supply Temperature: **85°F (29°C)** for L2C applications (warm water optimization)
- Function: Rejects heat from CDUs to atmosphere

**Secondary Loop (CDU to IT Equipment):**
- Source: Coolant Distribution Units (CDUs)
- Fluid: Dielectric fluid OR facility-safe coolant (propylene glycol/water)
- Supply Temperature: Controlled by CDU (typically 5-10°C below primary supply)
- Function: Circulates coolant through rack-mounted cold plates

**Tertiary Loop (Cold Plate Internal):**
- Source: Micro-channels within cold plates
- Fluid: Same as secondary loop
- Function: Direct contact heat exchange with chip surfaces

**Why Three Loops?**
- **Isolation:** Protects IT equipment from facility water contamination
- **Pressure Control:** Prevents over-pressurization of sensitive cold plates
- **Fluid Selection:** Allows dielectric fluid in secondary loop while using glycol/water in primary
- **Temperature Control:** CDU can independently regulate secondary loop temperature

### 2.2 Separation Between Facility Water and IT Coolant

**Critical Principle:** NEVER allow facility water to directly contact IT equipment.

**Separation Method:**
- **Heat Exchanger in CDU:** Liquid-to-liquid plate heat exchanger transfers thermal energy from secondary to primary loop
- **No Cross-Contamination:** Facility water stays in primary loop; IT coolant stays in secondary loop
- **Independent Chemistry:** Different fluid treatment programs for each loop

**Benefits of Separation:**
- **Water Quality Control:** IT equipment requires ultra-clean, treated coolant
- **Leak Mitigation:** Dielectric fluid in secondary loop prevents electrical damage from leaks
- **Pressure Management:** Secondary loop operates at lower pressure to protect cold plates
- **Fluid Compatibility:** Primary loop can use aggressive corrosion inhibitors; secondary uses IT-safe fluids

---

## 3.0 CHILLER SIZING FOR L2C SYSTEMS

### 3.1 Warm Water Advantage (85°F Supply)

**Why 85°F (29°C)?**
- **Efficiency Gain:** Every 1°C increase in supply temperature = 2-3% chiller energy savings
- **85°F vs. 55°F Comparison:**
  - 85°F: COP 5.0-6.5 (mechanical mode)
  - 55°F: COP 3.8-4.2 (mechanical mode)
  - **Result:** ~30-50% better efficiency at 85°F
- **Free Cooling Hours:** 85°F supply enables **3,500-4,000 hours/year** free cooling in temperate climates (vs. 2,000-2,500 hours for 55°F systems)
- **Component Safety:** Modern GPUs/CPUs tolerate higher coolant temperatures (designed for 40-50°C junction temps)

### 3.2 Chiller Capacity Calculation

**Step 1: Determine Total IT Heat Load**

```
Total IT Load (kW) = Number of Racks × Average Rack Power (kW)
```

**Example:**
- 168 L2C racks × 100 kW/rack = **16,800 kW (16.8 MW)**

**Step 2: Add CDU Parasitic Load**

```
CDU Power Consumption = Total IT Load × 1-2%
```

**Example:**
- 16,800 kW × 1.5% = **252 kW**
- **Total Cooling Load = 16,800 + 252 = 17,052 kW**

**Step 3: Apply N+1 Redundancy**

```
Required Chiller Capacity = Total Cooling Load ÷ (N units - 1 unit)
```

**Example (Target: N+1 with optimal chiller utilization):**
- For 17,052 kW load, target 12 operating chillers + 1 standby
- Each chiller: 17,052 ÷ 12 = **1,421 kW minimum**
- **Specify:** 13 × 1,500 kW chillers (provides headroom and modularity)

**Important:** Avoid over-sizing individual chillers. Multiple smaller units provide:
- Better part-load efficiency
- Finer capacity control
- Easier maintenance (smaller crane requirements)
- Lower capital cost per kW

### 3.3 Phased Deployment Approach

**Principle:** Match chiller CapEx to IT load growth.

**Phasing Example (Saga Pryor DC):**

| Phase | IT Load | Required Capacity (N+1) | Chiller Strategy |
|-------|---------|-------------------------|------------------|
| 1 | 3.0 MW | 3.3 MW (with CDU load) | Deploy chillers for 3.0 MW |
| 2 | 6.0 MW | 6.6 MW | Add chillers for 3.0 MW RDHx (separate plant) |
| 3 | 15.0 MW | 16.5 MW | Add chillers as L2C + RDHx loads scale |
| 4 | 24.0 MW | 26.4 MW | Final build-out to 16.8 MW L2C + 7.2 MW RDHx |

**Key Considerations:**
- **Separate Warm/Cold Plants:** If mixing L2C (85°F) and RDHx (60°F), use separate chiller plants
- **Modular Expansion:** Size mechanical yard and piping for ultimate capacity
- **Equipment Standardization:** Use same chiller model across phases for parts/service commonality

---

## 4.0 CDU (COOLANT DISTRIBUTION UNIT) DESIGN

### 4.1 CDU Function & Components

**Primary Functions:**
1. **Heat Exchange:** Transfer heat from secondary (IT) loop to primary (facility) loop
2. **Pumping:** Circulate secondary coolant through cold plates
3. **Temperature Control:** Maintain precise supply temperature to IT equipment
4. **Filtration:** Remove particulates from secondary loop
5. **Monitoring:** Track temperature, pressure, flow rate, leak detection

**Key Components:**
- **Plate Heat Exchanger:** Liquid-to-liquid thermal transfer (primary ↔ secondary)
- **Secondary Pumps:** Variable-speed pumps (typically N+1 redundant)
- **Expansion Tank:** Accommodates fluid thermal expansion
- **Filtration System:** 5-10 micron filters to protect cold plates
- **Control System:** PLC with BACnet/IP integration
- **Leak Detection:** Sensors at all connections and manifold interfaces

### 4.2 CDU Sizing

**Capacity Range:**
- **Small:** 50-150 kW (single rack or blade chassis)
- **Medium:** 200-500 kW (3-5 racks)
- **Large:** 600-1,200 kW (6-12 racks)
- **Hyperscale:** 1,000-2,000+ kW (10-20 racks)

**Sizing Method:**

```
CDU Capacity = (Number of Racks Served × Rack Power) × 1.1 safety factor
```

**Example:**
- Serve 10 racks @ 100 kW each
- CDU Capacity = (10 × 100) × 1.1 = **1,100 kW minimum**
- **Specify:** 1,200 kW CDU (provides 9% headroom)

**A/B Redundancy for Critical Loads:**
- **Configuration:** Each rack fed by TWO independent CDUs (A-side + B-side)
- **Capacity:** Each CDU must support 100% of rack load independently
- **Failover:** Automatic switchover if primary CDU fails (<100ms response)
- **Use Case:** Mission-critical AI training clusters where downtime = revenue loss

### 4.3 CDU Location Strategy

**Option 1: In-Rack CDU (Not Recommended for High Density)**
- **Pros:** Short piping runs, easy serviceability
- **Cons:** Consumes valuable rack space, heat in hot aisle, limited capacity

**Option 2: Mechanical Gallery / Pipe Chase (RECOMMENDED)**
- **Pros:** Centralized maintenance, no white space consumed, supports high-capacity CDUs
- **Cons:** Longer piping runs, requires separate mechanical room
- **Typical Layout:** Mechanical gallery on building perimeter, piping through overhead to racks

**Option 3: End-of-Row CDU**
- **Pros:** Balance of proximity and centralization
- **Cons:** Still consumes floor space in white space

**Best Practice (Saga Pryor DC Approach):**
- CDUs in dedicated **mechanical gallery (north pipe gallery)**
- **Secondary dielectric fluid distribution** via overhead manifolds into data halls
- **Quick-disconnect fittings** at each rack for hot-swap capability

---

## 5.0 FLUID SELECTION & WATER QUALITY

### 5.1 Primary Loop (Facility Water)

**Recommended Fluid:** 25% Propylene Glycol / 75% Deionized Water

**Why Propylene Glycol?**
- **Freeze Protection:** Down to -10°F (-23°C) at 25% concentration
- **Corrosion Inhibition:** Protects copper, steel, aluminum
- **Non-Toxic:** Food-grade safe (vs. ethylene glycol)
- **Heat Transfer:** Minimal performance penalty vs. pure water

**Water Quality Requirements:**
- **Conductivity:** <100 µS/cm (prevents galvanic corrosion)
- **pH:** 7.5-8.5 (slightly alkaline to prevent corrosion)
- **Dissolved Oxygen:** <0.1 ppm (minimizes oxidation)
- **Particulates:** <200 microns (5-10 micron filtration at CDU inlet)
- **Biocide:** Quarterly dosing to prevent microbial growth

**Treatment Program:**
- **Initial Fill:** Deionized water + propylene glycol + corrosion inhibitor package
- **Makeup System:** Automatic dosing to maintain 25% glycol concentration
- **Monitoring:** Weekly pH/conductivity testing, quarterly full chemical analysis
- **Flushing:** Pre-commissioning flush with 1.5× system volume at 5 fps velocity

### 5.2 Secondary Loop (IT Equipment Coolant)

**Option 1: Dielectric Fluid (High Reliability)**
- **Fluid:** 3M Novec, Vertrel, or equivalent
- **Pros:** Electrically non-conductive, leak-safe for IT equipment
- **Cons:** Lower thermal capacity, higher viscosity, expensive (2-3× glycol cost)
- **Use Case:** Mission-critical systems where leak = catastrophic failure

**Option 2: Facility-Safe Coolant (Balanced Approach)**
- **Fluid:** 25% Propylene Glycol / 75% Deionized Water
- **Pros:** Excellent thermal performance, lower cost, easier maintenance
- **Cons:** Requires robust leak detection, potential IT damage if leaked
- **Use Case:** Systems with integrated leak detection and containment

**Water Quality (Secondary Loop - CRITICAL):**
- **Conductivity:** <5 µS/cm (ultra-pure to protect electronics)
- **pH:** 7.0-8.0 (neutral to slightly alkaline)
- **Particulates:** <5 microns (fine filtration to protect cold plate micro-channels)
- **Dissolved Oxygen:** <0.05 ppm
- **No Biofilm:** Aggressive biocide program + UV sterilization

**Separation from Facility Water:**
- **NEVER mix primary and secondary loops** - always use plate heat exchanger in CDU
- **Reason:** Facility water quality insufficient for direct IT contact

---

## 6.0 COLD PLATE SPECIFICATIONS

### 6.1 Cold Plate Design Requirements

**Thermal Performance:**
- **Thermal Resistance:** 0.01-0.05 °C/W (lower = better)
- **Heat Flux Capacity:** 250-700 W/cm² (10-15× greater than air cooling)
- **Operating Temperature Range:** 15-70°C (component-dependent)

**Mechanical Specifications:**
- **Material:** Copper (400 W/m·K) preferred over aluminum (237 W/m·K)
- **Micro-Channel Design:** Optimized for turbulent flow and minimal pressure drop
- **Pressure Drop:** 2-44 kPa at 1-2 LPM (minimize pumping power)
- **Flow Rate:** 0.5-2 LPM per cold plate (component-specific)

**Installation Requirements:**
- **Thermal Interface Material (TIM):** Required between chip and cold plate
- **TIM Types:**
  - **Thermal Grease:** For CPU/GPU contact surfaces (reusable, high performance)
  - **Thermal Pads:** For memory, VRMs, secondary components (easier install)
- **Mounting Pressure:** Follow OEM specs (typically 30-50 psi uniform pressure)
- **TIM Application:** Thin, even layer (<0.1mm) to eliminate air gaps

### 6.2 Cold Plate Integration

**Component Coverage:**
- **Minimum:** CPU + GPU cold plates
- **Recommended:** CPU + GPU + Memory + VRMs (captures 95%+ of heat)
- **Maximum:** All heat-generating components (>100W each)

**Quick-Disconnect Integration:**
- **Connector Type:** Dry-break, self-sealing couplings
- **Spillage Limit:** <1 cm³ on disconnect
- **Locking Mechanism:** Steel ball lock or equivalent
- **Material:** Stainless steel or brass (corrosion-resistant)

**OCP (Open Compute Project) Standards:**
- Follow OCP Liquid Cooling Cold Plate Requirements (latest revision)
- Standardized mounting patterns for interoperability
- Qualification testing per OCP Cold Plate Development & Qualification guide

---

## 7.0 PIPING & DISTRIBUTION MANIFOLDS

### 7.1 Manifold Design

**Function:** Distribute secondary coolant from CDU to multiple racks via central spine with parallel ports.

**Configuration Options:**
- **Vertical Manifold:** Runs vertically along rack row (typical for high-density)
- **Horizontal Manifold:** Runs overhead across rack row (easier maintenance access)
- **Hybrid:** Combination of vertical and overhead distribution

**Material Specifications:**
- **Pipe Material:** Stainless steel (corrosion-resistant, high pressure rating)
- **Pressure Rating:** 150-300 psi (withstand pressure spikes)
- **Pipe Sizing:** 1"-3" diameter depending on flow rate and number of racks

**Design Principles:**
- **Even Flow Distribution:** Parallel ports sized for equal pressure drop to each rack
- **Isolation Valves:** Ball valves at each rack branch for maintenance isolation
- **Air/Pressure Relief:** Integrated valves at high points to purge air during fill
- **Blind-Mate Connectors:** 1mm radial alignment tolerance for easy installation

### 7.2 Quick Disconnects (QDCs)

**Purpose:** Enable hot-swappable servers without draining system.

**Key Features:**
- **Bidirectional Self-Sealing:** Prevents spillage when disconnected
- **Tool-Less Operation:** Hand-operated coupling/decoupling
- **Low Pressure Drop:** <5 psi across QDC
- **Durability:** Rated for 10,000+ connect/disconnect cycles

**Installation Locations:**
- **Rack Manifold to Server:** At each server inlet/outlet
- **CDU to Manifold:** At manifold supply/return headers
- **Maintenance Points:** Strategic locations for temporary chiller connection

**Leak Prevention:**
- **Dry-Break Design:** <1 cm³ spillage on disconnect
- **Leak Detection Sensors:** At all QDC locations, integrated with BMS
- **Drip Pans:** Under all QDC points (backup containment)

### 7.3 Overhead vs. Under-Floor Distribution

**Overhead (RECOMMENDED for L2C):**
- **Pros:** Easy visual inspection, no plenum contamination, easier routing
- **Cons:** Aesthetic impact, must coordinate with cable trays and HVAC ductwork
- **Best Practice:** Run manifolds parallel to rack rows, 8-10 ft above finished floor

**Under-Floor:**
- **Pros:** Hidden from view, utilizes raised floor plenum
- **Cons:** Leak risk in plenum, difficult maintenance access, limited to low-pressure systems
- **Use Case:** Only for low-density systems (<50 kW/rack) with minimal leak risk

---

## 8.0 REDUNDANCY & RELIABILITY

### 8.1 N+1 Redundancy Strategy

**Definition:** N+1 = Capacity required (N) + 1 additional unit for failover.

**Application Levels:**
1. **Chiller Plant:** N+1 chillers (e.g., 12 required + 1 standby = 13 total)
2. **CDU:** N+1 CDUs per zone (e.g., 2 CDUs for 1 zone of racks)
3. **Pumps:** Dual pumps in each CDU (1 active + 1 standby)

**Failover Characteristics:**
- **Automatic Switchover:** PLC detects failure, activates standby unit
- **Response Time:** <100ms for pump failover, <5 minutes for chiller staging
- **Flow Continuity:** Secondary loop flow fluctuation <5% during failover

### 8.2 A/B Redundant CDU Configuration

**Architecture:** Each rack served by TWO independent CDUs.

**Operational Modes:**
- **Normal:** CDU-A active, CDU-B standby (or load-sharing 50/50)
- **Failover:** CDU-A fails → CDU-B assumes 100% load automatically
- **Maintenance:** Isolate CDU-A for service while CDU-B maintains cooling

**Implementation:**
- **Dual Manifolds:** Separate A-side and B-side distribution headers
- **Rack-Level Valves:** Each rack has A/B selector valves (automatic or manual)
- **Capacity:** Each CDU sized for 100% of rack load (not 50%)

**Cost vs. Reliability:**
- **Cost:** 2× CDU capital cost + 2× piping cost
- **Reliability:** Zero downtime from CDU failure (critical for AI training)
- **ROI:** Justify for >$10M/year revenue clusters (downtime cost > redundancy cost)

### 8.3 Bypass Mode & Temporary Cooling

**Bypass Valves:**
- **Location:** At each CDU and chiller
- **Purpose:** Allow equipment isolation for maintenance without system shutdown
- **Configuration:** 3-way valves to route flow around bypassed equipment

**Temporary Chiller Connection:**
- **Quick-Connect Points:** Camlock fittings at strategic piping locations
- **Purpose:** Support rental/backup chillers during maintenance or emergency
- **Sizing:** 6"-8" diameter, rated for 300-1,500 kW per connection point
- **Access:** Connection points accessible from equipment yard with pass-through in building envelope

---

## 9.0 COMMISSIONING & STARTUP

### 9.1 Pre-Commissioning Requirements

**Mechanical Completion:**
- [ ] All piping pressure tested to 1.5× design pressure for 24 hours (no leaks)
- [ ] Piping flushed at 5 fps velocity with 1.5× system volume
- [ ] Filters installed at all CDU inlets (5-10 micron)
- [ ] Quick disconnects function tested (no leaks on connect/disconnect)
- [ ] Isolation valves verified operational
- [ ] Leak detection sensors installed and tested

**Electrical Completion:**
- [ ] Chillers, CDUs, pumps energized and motor rotation verified
- [ ] VFDs programmed and tested
- [ ] BMS integration completed (all points mapping to BMS)
- [ ] Emergency shutoff (EPO) circuit tested

**Fluid System Preparation:**
- [ ] Deionized water procured (conductivity <100 µS/cm verified)
- [ ] Propylene glycol delivered (25% concentration calculated)
- [ ] Corrosion inhibitor and biocide on-site
- [ ] Initial fluid chemistry baseline established

### 9.2 Fill & Startup Procedure

**Step 1: Progressive Fill (Primary Loop)**
1. Close all isolation valves except lowest fill point
2. Begin fill at 10 gpm (slow rate to prevent water hammer)
3. Pause every 25% fill to inspect for leaks (30 min soak test)
4. Open isolation valves progressively as fluid reaches each zone
5. Continue until system 100% full + expansion tank at 50% level
6. Purge air at all high points using air relief valves

**Step 2: Primary Loop Circulation**
1. Start primary pumps at 25% speed (low flow to detect leaks)
2. Increase speed to 50% after 1 hour (if no leaks)
3. Increase to 100% speed after 2 hours
4. Verify flow rates at each CDU (compare to design)
5. Adjust balancing valves to achieve target flow distribution

**Step 3: Secondary Loop Fill**
1. Isolate secondary loop from racks (close QDCs)
2. Fill secondary loop with dielectric fluid or glycol (same progressive method)
3. Circulate through CDU and manifolds only (no IT equipment yet)
4. Verify CDU heat exchanger performance (measure ΔT across exchanger)
5. Purge air from secondary loop

**Step 4: Rack Integration**
1. Connect one rack at a time via QDCs
2. Open isolation valve slowly (prevent pressure spike)
3. Verify flow through cold plates (measure inlet/outlet temps)
4. Check for leaks at all cold plate connections
5. Repeat for remaining racks (progressive commissioning)

**Step 5: Chiller Startup**
1. Start chillers in staging sequence (1 → 2 → 3, etc.)
2. Verify supply temperature reaches 85°F setpoint
3. Confirm free cooling mode activates when ambient permits
4. Test N+1 failover (disable one chiller, verify others compensate)

### 9.3 Thermal Qualification Testing

**Purpose:** Verify cooling system meets performance requirements under load.

**Test Procedure:**
1. **Baseline:** Servers at idle (minimal heat load)
   - Record: Supply/return temps, flow rates, component temps
2. **Ramp Test:** Increase IT load in 25% increments (use stress testing software)
   - Monitor: Cold plate temps, GPU/CPU junction temps, CDU performance
3. **Full Load:** Servers at 100% utilization for 24 hours
   - Verify: All components within thermal limits, no throttling
4. **N+1 Failover Test:** Disable one CDU during full load
   - Verify: Automatic failover, no component overheating
5. **Documentation:** Generate thermal qualification report with all data

**Acceptance Criteria:**
- Component temperatures <85°C at full load (GPU/CPU junction temps)
- Supply temperature stable at 85°F ±2°F
- No thermal throttling during 24-hour burn-in
- N+1 failover <100ms with <5% flow fluctuation

---

## 10.0 WATER QUALITY MONITORING & MAINTENANCE

### 10.1 Routine Testing Schedule

| Parameter | Frequency | Target Range | Action if Out of Spec |
|-----------|-----------|--------------|----------------------|
| **pH** | Weekly | 7.5-8.5 | Adjust with pH buffer |
| **Conductivity** | Weekly | <100 µS/cm (primary), <5 µS/cm (secondary) | Add deionized water to dilute |
| **Glycol Concentration** | Monthly | 24-26% | Add glycol or water to adjust |
| **Dissolved Oxygen** | Monthly | <0.1 ppm | Add oxygen scavenger |
| **Particulates** | Monthly | <200 microns | Replace filters |
| **Biocide Level** | Quarterly | Per manufacturer | Dose with biocide |
| **Corrosion Inhibitor** | Quarterly | Per manufacturer | Dose with inhibitor |
| **Full Chemistry Panel** | Annually | All parameters | Complete fluid replacement if degraded |

### 10.2 Filter Maintenance

**Pre-Filters (CDU Inlet):**
- **Type:** 200-micron bag filters
- **Change Frequency:** Every 3 months or when ΔP >5 psi
- **Purpose:** Protect CDU heat exchanger and pumps

**Fine Filters (Secondary Loop):**
- **Type:** 5-10 micron cartridge filters
- **Change Frequency:** Every 6 months or when ΔP >3 psi
- **Purpose:** Protect cold plate micro-channels from blockage

**Filter Change Procedure:**
1. Isolate filter assembly with upstream/downstream valves
2. Depressurize via drain valve
3. Remove filter cartridge
4. Inspect housing for sediment (flush if excessive)
5. Install new filter and pressurize slowly
6. Monitor for leaks

### 10.3 Leak Detection & Response

**Leak Detection Methods:**
- **Moisture Sensors:** Under all QDCs and at CDU base (detect <1 cm³ spillage)
- **Flow Meters:** Detect sudden flow loss (indicates leak)
- **Pressure Sensors:** Detect pressure drop (indicates leak)
- **Visual Inspection:** Weekly walk-through of manifolds and connections

**Leak Response Protocol:**
1. **Alarm:** BMS alerts facility team via email/SMS
2. **Isolate:** Close valves upstream/downstream of leak zone
3. **Drain:** Drain affected section to minimize spillage
4. **Repair:** Replace gasket/fitting/hose as needed
5. **Test:** Pressure test repair to 1.5× design pressure
6. **Refill:** Restore coolant and purge air
7. **Document:** Log leak location, cause, repair action in maintenance database

---

## 11.0 ENERGY EFFICIENCY & FREE COOLING

### 11.1 Optimizing for Warm Water (85°F) Supply

**Efficiency Benefits:**
- **Chiller COP:** 5.0-6.5 vs. 3.8-4.2 for 55°F systems (30-50% improvement)
- **Free Cooling Hours:** 3,500-4,000 hours/year in temperate climates
- **Annual Energy Savings:** 50-60% reduction in cooling energy vs. cold water

**Design Considerations:**
- **Component Compatibility:** Verify GPU/CPU thermal limits support 85°F coolant
- **CDU Heat Exchanger:** Size for 10-15°F approach temperature (primary to secondary)
- **BMS Logic:** Program to maximize free cooling hours (enable when ambient <75°F)

### 11.2 Free Cooling Modes

**Mode 1: Full Free Cooling (Ambient <75°F / 24°C)**
- Chiller compressors OFF
- Heat rejected via air-cooled coils only
- COP = 20-35 (waterside economizer efficiency)
- **Season:** October-May in temperate climates (6-7 months/year)

**Mode 2: Partial Free Cooling (Ambient 75-85°F / 24-29°C)**
- Chiller compressors run at reduced capacity (part-load)
- Blended free cooling + mechanical cooling
- COP = 8-12 (partial economizer mode)
- **Season:** March-April, September-October (shoulder seasons)

**Mode 3: Mechanical Cooling (Ambient >85°F / 29°C)**
- Chiller compressors run at full capacity
- Still higher efficiency than 55°F systems due to warm water COP advantage
- COP = 5.0-6.5
- **Season:** June-August (peak summer, 3-4 months/year)

### 11.3 PUE Impact

**Target PUE by Phase:**
- **Phase 1 (3 MW):** 1.40 (initial operations, conservative)
- **Phase 2 (6 MW):** 1.35 (both loops operational)
- **Phase 3 (15 MW):** 1.30 (scale efficiencies)
- **Phase 4 (24 MW):** 1.25 (optimized at scale with warm water + free cooling)

**PUE Contributors:**
- **Cooling Energy:** 35-40% of total facility load (reduced by warm water)
- **Pumping Energy:** 5-10% of total facility load (VFD optimization critical)
- **Power Distribution Losses:** 3-5% (UPS, transformers, PDUs)
- **Lighting & Support:** 1-2%

---

## 12.0 DESIGN CHECKLIST FOR BOD DEVELOPMENT

### 12.1 System Architecture Decisions

- [ ] **Cooling Topology:** Direct-to-chip (L2C) vs. immersion vs. hybrid
- [ ] **Loop Architecture:** 2-loop vs. 3-loop (recommend 3-loop for facility water separation)
- [ ] **Redundancy Level:** N, N+1, or 2N (recommend N+1 minimum)
- [ ] **CDU Configuration:** Centralized vs. in-rack vs. end-of-row (recommend mechanical gallery)
- [ ] **Manifold Layout:** Overhead vs. under-floor (recommend overhead)

### 12.2 Performance Specifications

- [ ] **IT Heat Load:** Calculate total kW by phase
- [ ] **Chiller Supply Temperature:** Specify 85°F for L2C (warm water optimization)
- [ ] **Chiller Capacity:** Size for N+1 redundancy with phased deployment
- [ ] **CDU Capacity:** Size per rack zone with A/B redundancy if mission-critical
- [ ] **Cold Plate Coverage:** Specify minimum components (CPU+GPU) vs. comprehensive (CPU+GPU+memory+VRMs)

### 12.3 Fluid & Water Quality

- [ ] **Primary Loop Fluid:** Specify 25% propylene glycol / 75% deionized water
- [ ] **Secondary Loop Fluid:** Specify dielectric fluid OR glycol/water (with leak detection)
- [ ] **Water Quality Targets:** Conductivity, pH, dissolved oxygen, particulate limits
- [ ] **Treatment Program:** Corrosion inhibitor, biocide, oxygen scavenger
- [ ] **Monitoring Frequency:** Weekly, monthly, quarterly, annual testing schedule

### 12.4 Equipment Specifications

- [ ] **Chiller Type:** Air-cooled screw/scroll with integrated free cooling
- [ ] **Refrigerant:** Low-GWP compliant with EPA/AIM Act (performance-based, not chemical-specific)
- [ ] **CDU Components:** Heat exchanger, pumps (N+1), expansion tank, filtration, controls
- [ ] **Manifold Material:** Stainless steel, pressure-rated for 150-300 psi
- [ ] **Quick Disconnects:** Dry-break, self-sealing, <1 cm³ spillage

### 12.5 Integration & Controls

- [ ] **BMS Integration:** BACnet/IP or Modbus TCP protocol
- [ ] **Leak Detection:** Moisture sensors at all QDCs, manifolds, CDUs
- [ ] **Flow/Pressure Monitoring:** Sensors at CDU inlet/outlet, manifold headers
- [ ] **Automatic Failover:** N+1 chiller staging, A/B CDU switchover
- [ ] **Free Cooling Logic:** Enable waterside economizer when ambient permits

### 12.6 Commissioning Requirements

- [ ] **Pressure Testing:** 1.5× design pressure for 24 hours
- [ ] **Flushing:** 1.5× system volume at 5 fps velocity
- [ ] **Progressive Fill:** 25% increments with leak check pauses
- [ ] **Thermal Qualification:** Full load testing with component temp monitoring
- [ ] **Acceptance Criteria:** Junction temps <85°C, no throttling, N+1 failover verified

---

## 13.0 COMMON PITFALLS & LESSONS LEARNED

### 13.1 Design Phase Mistakes

**❌ Pitfall:** Over-specifying chiller counts in BOD (e.g., "13 × 1,500 kW chillers")
**✅ Solution:** Specify total N+1 capacity (e.g., "Phased to 16.8 MW N+1") to allow flexibility

**❌ Pitfall:** Using cold water (55°F) supply for L2C systems
**✅ Solution:** Specify 85°F warm water for 30-50% efficiency gain + extended free cooling

**❌ Pitfall:** Allowing facility water to directly contact IT equipment
**✅ Solution:** Always use 3-loop architecture with CDU heat exchanger separation

**❌ Pitfall:** Under-sizing CDUs for future rack densification
**✅ Solution:** Size CDUs for 20% headroom (e.g., 120 kW for 100 kW rack)

### 13.2 Installation Mistakes

**❌ Pitfall:** Skipping pre-commissioning flush → particulates clog cold plates
**✅ Solution:** Mandatory 1.5× system volume flush at 5 fps before fill

**❌ Pitfall:** Rapid fill → water hammer damages fittings
**✅ Solution:** Progressive fill at 10 gpm with 30-min soak tests every 25%

**❌ Pitfall:** Using untreated water → corrosion and microbial growth
**✅ Solution:** Deionized water + glycol + corrosion inhibitor + biocide from day 1

**❌ Pitfall:** No leak detection at QDCs → undetected leaks damage IT equipment
**✅ Solution:** Moisture sensors at ALL QDCs, integrated with BMS alarming

### 13.3 Operational Mistakes

**❌ Pitfall:** Infrequent water quality testing → chemistry drift → corrosion
**✅ Solution:** Weekly pH/conductivity, monthly glycol concentration, quarterly full panel

**❌ Pitfall:** Ignoring filter ΔP → clogged filters → flow restriction → overheating
**✅ Solution:** Monthly ΔP checks, replace filters when ΔP >5 psi (pre-filters) or >3 psi (fine filters)

**❌ Pitfall:** No N+1 redundancy testing → failures during actual outage
**✅ Solution:** Quarterly N+1 failover tests (disable one chiller, verify seamless operation)

---

## 14.0 REFERENCES & STANDARDS

### 14.1 Industry Standards

- **OCP (Open Compute Project):**
  - Liquid Cooling Integration and Logistics White Paper (Rev 1.0)
  - Cold Plate Requirements Document (Rev 1.0)
  - Cold Plate Development and Qualification Guide
  - Rack Manifold Requirements and Qualification (v3)

- **ASHRAE:**
  - TC 9.9: Mission Critical Facilities, Technology Spaces, and Electronic Equipment
  - Thermal Guidelines for Data Processing Environments (Class A1)
  - Liquid Cooling for Data Centers (various white papers)

- **ANSI/TIA-942:**
  - Data Center Standards for Telecommunications Infrastructure
  - Liquid Cooling Annex (latest revision)

### 14.2 Manufacturer Resources

- **Vertiv:** Understanding Direct-to-Chip Cooling in HPC Infrastructure
- **Schneider Electric:** Navigating Liquid Cooling Architectures for Data Centers
- **Boyd Corporation:** CDU Design Guides and Cold Plate Specifications
- **nVent:** 2025 Liquid Cooling Best Practices
- **LiquidStack, Chilldyne, JetCool:** Commissioning guides and technical briefs

### 14.3 Technical Papers

- IEEE Spectrum: "Data Center Liquid Cooling: The AI Heat Solution" (2024)
- Data Center Dynamics: "Unlocking the Potential of Direct-to-Chip Liquid Cooling" (2024)
- ResearchGate: "Liquid to Liquid Cooling for High Heat Density Data Centers" (2023)
- ScienceDirect: "Experimental Evaluation of Direct-to-Chip Cold Plate Cooling" (2023)

---

## 15.0 SAGA PRYOR DC APPLICATION SUMMARY

**Project Context:** 24 MW IT (30 MW facility) data center optimized for AI/ML workloads

**L2C Design Highlights:**
- **Loop 3:** 16.8 MW warm-water (85°F) L2C plant serving 168 × 100 kW racks
- **Phasing:** 3 MW (Phase 1) → 10.5 MW (Phase 3) → 16.8 MW (Phase 4)
- **CDU Strategy:** A/B redundant CDUs in mechanical gallery (north pipe gallery)
- **Fluid:** 25% propylene glycol primary loop, dielectric secondary loop
- **Chiller Strategy:** Air-cooled chillers, low-GWP refrigerant, phased deployment to match load
- **Free Cooling:** ~3,500-4,000 hours/year in Pryor, OK climate
- **Target PUE:** 1.40 (Phase 1) → 1.25 (Phase 4)

**Key De-Risking Decisions (from 5BOD):**
1. Specify total N+1 capacity, not specific chiller counts (vendor flexibility)
2. Specify "Low-GWP refrigerant," not specific chemicals (regulatory future-proofing)
3. Omit return temps and COP values (outcomes, not design inputs)
4. Specify ASHRAE TC 9.9 compliance, not prescriptive solutions (performance-based)

---

**Document Version:** 1.0
**Last Updated:** 2025-11-05
**Prepared by:** Claude Code with industry research synthesis