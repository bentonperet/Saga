# GGE DATA CENTER - ELECTRICAL DESIGN
## N+1 MTU DRUPS with HPP Priority + Utility Makeup
### Phase 1: 3.0 MW IT Capacity

**Document:** GGE-EL-DESIGN-002
**Date:** 2025-11-04
**Revision:** 01 - HPP Priority Architecture
**Prepared by:** EVS / GGE Engineering Team

---

## EXECUTIVE SUMMARY

### **Design Philosophy:**
- **HPP Priority Operation:** Maximize renewable energy utilization (3.7 MW HPP = 84% of load)
- **Utility Makeup:** Grid provides supplemental power (0.7 MW = 16% of load)
- **Generator Protection:** HPP auto-disconnect on utility failure to protect MTU diesel generators
- **N+1 Redundancy:** 3 × 2,750 kVA MTU DRUPS (2 running + 1 standby)
- **Concurrent Maintainability:** Tier III compliance with full bypass capability

### **Key Capacity Metrics:**
```
IT Capacity:              3.0 MW (Phase 1)
Total Facility Load:      4.4 MW
MTU Running Capacity:     5.5 MVA (2 × 2,750 kVA)
MTU Standby:              2.75 MVA (N+1)
PUE Target:               1.50 (design max), 1.30 (annual with free cooling)
```

---

## POWER SOURCE CONFIGURATION

### **1. PRIMARY SOURCES**

#### **Utility Grid Source**
- **Capacity:** 6 MW @ 10 kV, 3-phase, 50 Hz
- **Configuration:** Dual diverse feeds
  - Feed 1: 3 MW → MV-SWBD-A
  - Feed 2: 3 MW → MV-SWBD-B
- **Normal Operation:** Provides 0.7 MW makeup power (16% of total load)
- **Protection:** VCB-UA and VCB-UB (630A, 40 kA @ 10 kV)

#### **HPP (Hydroelectric Power Plant) Source**
- **Capacity:** 3.7 MW @ 400V, 3-phase, 50 Hz
- **Configuration:** Dual feeds via step-up transformers
  - Feed 1: 1.85 MW @ 400V → XFMR-H1 (2,500 kVA) → 10 kV → MV-SWBD-A
  - Feed 2: 1.85 MW @ 400V → XFMR-H2 (2,500 kVA) → 10 kV → MV-SWBD-B
- **Normal Operation:** Provides 3.7 MW (84% of total load)
- **Protection:** VCB-HA and VCB-HB (630A, 40 kA @ 10 kV) with fast-acting auto-disconnect

#### **Solar Array (Office Only)**
- **Capacity:** 800 kW AC @ 400V
- **Configuration:** Direct to office SWBD via ATS (solar priority)
- **Protection:** Isolated from critical data center loads

---

## LOAD CALCULATIONS

### **Total Facility Load:**
```
MTU Running Capacity:     2 × 2,750 kVA = 5,500 kVA
Power Factor:             0.8 (typical data center)
Total Facility Power:     5,500 × 0.8 = 4,400 kW

PUE:                      1.5 (design maximum)
IT Load:                  4,400 / 1.5 = 2,933 kW ≈ 3.0 MW
Infrastructure:           4,400 - 2,933 = 1,467 kW (33%)
```

### **Detailed Power Budget:**

| Load Category | Power (kW) | Current @ 400V (A) | % of Total |
|---------------|------------|-------------------|------------|
| **IT Load** | 2,933 | 4,995 | 67% |
| **Cooling - Chillers** | 650 | 1,106 | 15% |
| **Cooling - CHW Pumps** | 90 | 153 | 2% |
| **Cooling - CW Pumps** | 105 | 179 | 2% |
| **Cooling - River Pumps** | 75 | 128 | 2% |
| **Cooling - In-row fans** | 80 | 136 | 2% |
| **Electrical Losses** | 280 | - | 6% |
| **Lighting, BMS, Controls** | 100 | 170 | 2% |
| **Building HVAC (Office)** | 87 | 148 | 2% |
| **TOTAL FACILITY** | **4,400** | **7,481** | **100%** |

### **Load Distribution (Normal Operation):**

**Bus A (LV-SWBD-A):**
- IT Load: 1,466 kW (2,497 A)
- Cooling Load: 500 kW (851 A)
- Subtotal: 1,966 kW (3,348 A)

**Bus B (LV-SWBD-B):**
- IT Load: 1,467 kW (2,498 A)
- Cooling Load: 500 kW (851 A)
- Subtotal: 1,967 kW (3,349 A)

**Common Loads:**
- Electrical losses, lighting, BMS, HVAC: 467 kW (795 A)

**Total:** 4,400 kW (7,481 A @ 400V)

---

## TRANSFORMER SIZING

### **HPP Step-Up Transformers (400V → 10 kV)**

**XFMR-H1 and XFMR-H2:**
- **Rating:** 2,500 kVA each
- **Voltage:** 400V Delta / 10 kV Wye grounded (Dyn11)
- **Load per transformer:** 1.85 MW / 0.8 pf = 2,312 kVA
- **Utilization:** 2,312 / 2,500 = 92.5% (good utilization)
- **Cooling:** ONAN (Oil Natural Air Natural)
- **Impedance:** 6% typical
- **Brands:** Schneider Electric, ABB, Siemens

### **MV Step-Down Transformers (10 kV → 400V) - 2N CONFIGURATION**

**Configuration: 4 × 5,000 kVA for Tier III Concurrent Maintainability**

```
MV-SWBD-A feeds:
├─ XFMR-1A: 5,000 kVA → LV-SWBD-A (primary path A)
└─ XFMR-1B: 5,000 kVA → LV-SWBD-B (cross-tie to B)

MV-SWBD-B feeds:
├─ XFMR-2A: 5,000 kVA → LV-SWBD-A (cross-tie to A)
└─ XFMR-2B: 5,000 kVA → LV-SWBD-B (primary path B)

Result: Each LV-SWBD receives power from BOTH MV switchboards via separate transformers
```

**XFMR-1A, XFMR-1B, XFMR-2A, XFMR-2B:**
- **Rating:** 5,000 kVA each
- **Voltage:** 10 kV Delta / 400V Wye grounded (Dyn11)
- **Normal load per transformer:** 1,100 kW / 0.8 pf = 1,375 kVA (25% of facility per transformer)
- **Single transformer failure:** Remaining 3 transformers carry 4,400 kW / 0.8 = 5,500 kVA
  - Load per transformer: 5,500 / 3 = 1,833 kVA
  - Utilization: 1,833 / 5,000 = 37% ✓ (excellent margin)
- **Concurrent maintainability:** Any single transformer can be removed for maintenance without capacity loss
- **Cooling:** ONAN (Oil Natural Air Natural)
- **Impedance:** 6% typical

**2N Benefits:**
1. **Concurrent Maintainability:** Any transformer can be isolated for maintenance/replacement
2. **Load Margin:** Even with 1 transformer out, remaining 3 operate at only 37% utilization
3. **Tier III Compliance:** No single point of failure in transformer layer
4. **Simplified Operations:** No emergency load shedding required during maintenance

---

## MTU KINETIC DRUPS CONFIGURATION

### **System Overview:**
```
3 × 2,750 kVA MTU Kinetic DRUPS (N+1)
├─ MTU-1: 2,750 kVA (Running - feeds LV-SWBD-A)
├─ MTU-2: 2,750 kVA (Running - feeds LV-SWBD-B)
└─ MTU-3: 2,750 kVA (Standby - N+1 redundancy)

Total Running Capacity: 5,500 kVA
Total Installed: 8,250 kVA
Redundancy: N+1 (any unit can fail, remaining 2 carry 100% load)
```

### **MTU Unit Specifications:**
- **Model:** MTU Kinetic PowerPack KP7 (or equivalent 2,750 kVA model)
- **Rating:** 2,750 kVA / 2,200 kW continuous data center rating
- **Input Voltage:** 400V, 3-phase, 50 Hz
- **Output Voltage:** 400V, 3-phase, 50 Hz
- **Technology:** Integrated diesel engine + kinetic flywheel energy storage
- **Flywheel Ride-Through:** 15-20 seconds (while diesel starts)
- **Diesel Start Time:** <10 seconds to rated speed and voltage
- **Transition Time:** Seamless (0 ms transfer from utility to flywheel to diesel)
- **Emissions:** EU Stage V compliant
- **Fuel:** Diesel, [TBD] liters storage, [TBD] hours runtime at full load

### **Normal Operation:**
- **MTU-1 Load:** 2,200 kW (50% of facility)
- **MTU-2 Load:** 2,200 kW (50% of facility)
- **MTU-3 Status:** Standby (flywheel spinning, diesel off)
- **Diesel Engines:** OFF (flywheels spinning on utility power)
- **Mode:** Pass-through (utility power flows through MTU to output)

### **Utility Failure Operation:**
- **T+0-15 sec:** Flywheel provides continuous power (no interruption)
- **T+10-15 sec:** Diesel engines start and synchronize
- **T+15 sec+:** Diesel engines carry full load
- **MTU-1 Load:** 2,200 kW (50%)
- **MTU-2 Load:** 2,200 kW (50%)
- **MTU-3:** Available for N+1 backup

### **N+1 Failure Scenario (One MTU Fails):**
- **Remaining 2 MTUs:** 2 × 2,750 kVA = 5,500 kVA
- **Facility Load:** 4,400 kW / 0.8 = 5,500 kVA
- **Utilization:** 5,500 / 5,500 = 100% (no margin - critical!)
- **Recommendation:** Consider load shedding plan or upsize MTU units

---

## MV SWITCHBOARD CONFIGURATION

### **MV-SWBD-A (10 kV Bus)**

**Incoming Feeders:**
- **VCB-UA:** Utility Feed 1 (3 MW capacity)
  - Rating: 630A, 40 kA SCCR
  - Normal State: CLOSED
  - Function: Primary utility source

- **VCB-HA:** HPP Feed 1 (1.85 MW capacity via XFMR-H1)
  - Rating: 630A, 40 kA SCCR
  - Normal State: CLOSED
  - **CRITICAL:** Fast-acting auto-disconnect on utility failure
  - Opening time: <50 ms (5 cycles @ 50 Hz)

**Outgoing Feeders (2N Configuration):**
- **VCB-1A:** To XFMR-1A (feeds LV-SWBD-A)
  - Rating: 630A, 40 kA SCCR
  - Normal State: CLOSED
  - Load: 1,100 kW (25% of facility)

- **VCB-1B:** To XFMR-1B (feeds LV-SWBD-B)
  - Rating: 630A, 40 kA SCCR
  - Normal State: CLOSED
  - Load: 1,100 kW (25% of facility)

**Protection & Control:**
- Undervoltage relays on both utility feeds (set @ 80% nominal)
- HPP disconnect logic (VCB-HA auto-open on utility loss)
- Overcurrent protection (IDMT curves)
- Ground fault protection
- Arc flash labeling per IEC 61482

### **MV-SWBD-B (10 kV Bus)**

**Incoming Feeders:**
- **VCB-UB:** Utility Feed 2 (3 MW capacity)
  - Rating: 630A, 40 kA SCCR
  - Normal State: CLOSED
  - Function: Primary utility source

- **VCB-HB:** HPP Feed 2 (1.85 MW capacity via XFMR-H2)
  - Rating: 630A, 40 kA SCCR
  - Normal State: CLOSED
  - **CRITICAL:** Fast-acting auto-disconnect on utility failure
  - Opening time: <50 ms (5 cycles @ 50 Hz)

**Outgoing Feeders (2N Configuration):**
- **VCB-2A:** To XFMR-2A (feeds LV-SWBD-A)
  - Rating: 630A, 40 kA SCCR
  - Normal State: CLOSED
  - Load: 1,100 kW (25% of facility)

- **VCB-2B:** To XFMR-2B (feeds LV-SWBD-B)
  - Rating: 630A, 40 kA SCCR
  - Normal State: CLOSED
  - Load: 1,100 kW (25% of facility)

**Protection & Control:**
- Same as MV-SWBD-A
- Independent protection systems (no common failure points)

---

## LV DISTRIBUTION (400V)

### **LV-SWBD-A (Bus A - 400V)**
- **Bus Rating:** 5,000A
- **Dual Inputs (2N Configuration):**
  - Input 1: MTU-1 output via XFMR-1A (from MV-SWBD-A)
  - Input 2: MTU-1 output via XFMR-2A (from MV-SWBD-B)
  - Each input: 1,100 kW (50% of A-side load)
- **Normal Load:** 2,200 kW (3,747 A) = 75% utilization
- **Single Transformer Failure:** 2,200 kW carried by remaining transformer @ 44% utilization ✓
- **Configuration:** Copper bus bars, IP42 enclosure

**Main Breaker:**
- **ACB-M1:** 6,300A frame, 5,000A trip setting
- **Type:** Air Circuit Breaker, drawout, motorized
- **Protection:** Electronic trip unit (LSIG functions)
- **Rating:** 65 kA SCCR @ 400V

**Distribution Panels:**
- **A-IT-1:** IT loads
  - Rating: 3,200A MCCB
  - Load: 1,466 kW (2,497 A)
  - Feeds: Dual-corded PDUs for A-side IT equipment

- **A-COOL-1:** Cooling loads
  - Rating: 4,000A MCCB with motor starting capability
  - Load: 500 kW (851 A)
  - Feeds: CHW pumps, CW pumps, river pumps, chillers, in-row units

### **LV-SWBD-B (Bus B - 400V)**
- **Bus Rating:** 5,000A
- **Dual Inputs (2N Configuration):**
  - Input 1: MTU-2 output via XFMR-1B (from MV-SWBD-A)
  - Input 2: MTU-2 output via XFMR-2B (from MV-SWBD-B)
  - Each input: 1,100 kW (50% of B-side load)
- **Normal Load:** 2,200 kW (3,747 A) = 75% utilization
- **Single Transformer Failure:** 2,200 kW carried by remaining transformer @ 44% utilization ✓
- **Configuration:** Copper bus bars, IP42 enclosure

**Main Breaker:**
- **ACB-M2:** 6,300A frame, 5,000A trip setting
- **Type:** Air Circuit Breaker, drawout, motorized
- **Protection:** Electronic trip unit (LSIG functions)
- **Rating:** 65 kA SCCR @ 400V

**Distribution Panels:**
- **B-IT-1:** IT loads
  - Rating: 3,200A MCCB
  - Load: 1,467 kW (2,498 A)
  - Feeds: Dual-corded PDUs for B-side IT equipment

- **B-COOL-1:** Cooling loads
  - Rating: 4,000A MCCB with motor starting capability
  - Load: 500 kW (851 A)
  - Feeds: CHW pumps, CW pumps, river pumps, chillers, in-row units

### **Tie Breaker (52-TIE)**
- **Rating:** 6,300A frame, 5,000A trip setting
- **Type:** Air Circuit Breaker, drawout, motorized
- **Normal State:** OPEN
- **Function:** Allows single-source operation during maintenance
- **Protection:** Electronic trip unit, interlocked with main breakers
- **NOTE:** Tie breaker closure creates overload condition (150% of bus rating) - requires immediate load shedding or source restoration

---

## PROTECTION & CONTROL SEQUENCE

### **NORMAL OPERATION (HPP Priority Mode)**

**Power Flow:**
```
HPP: 3.7 MW (84%)    →  Step-Up XFMR-H1/H2  →  MV-SWBD-A/B  →  Step-Down XFMR-A/B  →  MTU-1/2  →  LV-SWBD-A/B
Utility: 0.7 MW (16%) →  Direct to MV-SWBD-A/B  →  Step-Down XFMR-A/B  →  MTU-1/2  →  LV-SWBD-A/B
                                                                                           ↓
                                                                                      IT + Cooling Loads
```

**Monitoring:**
- Continuous voltage/frequency/power monitoring on all sources
- HPP output: 3.7 MW measured
- Utility makeup: 0.7 MW measured
- MTU pass-through mode: Diesel OFF, flywheel spinning

---

### **UTILITY FAILURE SEQUENCE (HPP Auto-Disconnect)**

**T+0 ms: UTILITY LOSS DETECTED**
```
Event: Both utility feeds (VCB-UA and VCB-UB) lose voltage
Detection: Undervoltage relays trigger @ <80% nominal voltage
Action: Protection logic activates HPP disconnect sequence
```

**T+10 ms: PROTECTION RELAY DECISION**
```
Logic: IF (Utility_A_Voltage < 80%) AND (Utility_B_Voltage < 80%) THEN
         HPP_Disconnect = TRUE
         MTU_Start = TRUE
       END IF
```

**T+50 ms: HPP DISCONNECT (CRITICAL)**
```
Action: VCB-HA and VCB-HB receive OPEN command
Result: HPP Feed 1 and HPP Feed 2 disconnected from MV switchboards
Reason: Protect MTU diesel generators from paralleling with unstable HPP source
Status: Data center load now isolated from HPP (utility gone, HPP disconnected)
```

**T+0-15 seconds: MTU FLYWHEEL BRIDGE**
```
MTU-1: Flywheel provides 2,200 kW continuous output to LV-SWBD-A
MTU-2: Flywheel provides 2,200 kW continuous output to LV-SWBD-B
IT Loads: NO INTERRUPTION (seamless flywheel support)
Diesel: Start command issued, engines cranking
```

**T+5-10 seconds: DIESEL CRANKING**
```
MTU-1 Diesel: Cranking, reaching rated speed (1500 RPM @ 50 Hz)
MTU-2 Diesel: Cranking, reaching rated speed (1500 RPM @ 50 Hz)
Flywheel: Still providing bridge power (energy depleting slowly)
```

**T+10-15 seconds: DIESEL SYNCHRONIZED**
```
MTU-1 Diesel: At rated speed, voltage buildup, synchronized with load
MTU-2 Diesel: At rated speed, voltage buildup, synchronized with load
Transition: Automatic switch from flywheel energy to diesel generator
Mode: Seamless (no interruption to IT loads)
```

**T+15 seconds+: FULL DIESEL OPERATION**
```
MTU-1 Load: 2,200 kW (50% of facility) - Diesel carrying full load
MTU-2 Load: 2,200 kW (50% of facility) - Diesel carrying full load
MTU-3 Status: Available for N+1 backup if needed
HPP Status: DISCONNECTED (VCB-HA and VCB-HB remain OPEN)
Utility Status: UNAVAILABLE
Duration: MTU can run indefinitely on diesel fuel
Fuel Consumption: ~175 L/hr per unit @ 50% load = 350 L/hr total
```

---

### **UTILITY RESTORATION SEQUENCE**

**T+0: UTILITY RETURNS**
```
Event: Utility voltage restored and stable
Criteria: Voltage >90%, Frequency 50 Hz ±0.5 Hz, stable for 5 minutes
Action: Auto-restoration sequence begins (operator approval may be required)
```

**T+5 minutes: UTILITY VERIFICATION**
```
Monitoring: 5-minute timer ensures utility stability
Check: Voltage, frequency, phase rotation, power quality
Status: Utility deemed acceptable for reconnection
```

**T+5 min + 30 sec: HPP RECONNECTION**
```
Action: VCB-HA closes (HPP Feed 1 reconnects to MV-SWBD-A)
        VCB-HB closes (HPP Feed 2 reconnects to MV-SWBD-B)
Result: HPP + Utility parallel operation resumes
Load Sharing: HPP 3.7 MW + Utility 0.7 MW
Mode: MTU still carrying load (diesel running)
```

**T+6 minutes: LOAD TRANSFER TO UTILITY/HPP**
```
Action: Gradual load transfer from MTU diesel to utility/HPP sources
Rate: ~10% per minute to avoid thermal shock
MTU-1/2: Output reduces from 2,200 kW → 0 kW over 10 minutes
Utility/HPP: Load increases to 4,400 kW
```

**T+16 minutes: MTU UNLOADED**
```
MTU-1 Output: 0 kW (diesel running at idle/no load)
MTU-2 Output: 0 kW (diesel running at idle/no load)
Load: 100% on Utility (0.7 MW) + HPP (3.7 MW)
Status: Ready for MTU cooldown
```

**T+16-26 minutes: MTU COOLDOWN**
```
Action: MTU diesel engines run at idle for 5-10 minutes (cooldown period)
Reason: Allow turbochargers and engine components to cool gradually
Monitoring: Oil temperature, coolant temperature, exhaust temp
```

**T+26 minutes: RETURN TO NORMAL**
```
Action: MTU-1 diesel engine stops
        MTU-2 diesel engine stops
        Flywheels continue spinning (on utility power - standby mode)
Status: Normal operation restored
  - HPP: 3.7 MW (84% of load)
  - Utility: 0.7 MW (16% of load)
  - MTU: Standby (flywheel spinning, diesel OFF)
```

---

## CONCURRENT MAINTAINABILITY (TIER III)

### **Maintenance Scenarios:**

**1. Utility Feed 1 Maintenance (VCB-UA):**
```
Procedure:
  1. HPP Feed 1 must carry full load to MV-SWBD-A
  2. Verify HPP output = 1.85 MW minimum
  3. Open VCB-UA (Utility Feed 1 isolated)
  4. Perform maintenance on Utility Feed 1
  5. No impact to data center (HPP Feed 1 supplies MV-SWBD-A)
```

**2. HPP Feed 1 Maintenance (VCB-HA):**
```
Procedure:
  1. Utility Feed 1 must carry full load to MV-SWBD-A
  2. Verify Utility capacity available
  3. Open VCB-HA (HPP Feed 1 isolated)
  4. Perform maintenance on HPP Feed 1 or XFMR-H1
  5. No impact to data center (Utility Feed 1 supplies MV-SWBD-A)
```

**3. MV-SWBD-A Maintenance:**
```
Procedure:
  1. Close tie breaker (52-TIE) at LV level
  2. Transfer LV-SWBD-A load to LV-SWBD-B (via tie)
  3. Open VCB-MA (XFMR-A disconnected from MV-SWBD-A)
  4. Open VCB-UA and VCB-HA (MV-SWBD-A de-energized)
  5. Perform maintenance on MV-SWBD-A
  6. All loads fed from MV-SWBD-B via tie breaker
  7. NOTE: Tie breaker carries 150% of rated load - time-limited maintenance
```

**4. XFMR-1A Maintenance (2N Transformer Configuration):**
```
Procedure:
  1. Verify XFMR-2A is carrying full LV-SWBD-A load (2,200 kW)
  2. Open VCB-1A at MV-SWBD-A (XFMR-1A primary isolated)
  3. Open secondary breaker for XFMR-1A at LV-SWBD-A
  4. Perform maintenance on XFMR-1A
  5. LV-SWBD-A continues operation from XFMR-2A (from MV-SWBD-B)
  6. XFMR-2A load: 2,200 kW / 5,000 kVA = 44% utilization ✓
  7. NO TIE BREAKER REQUIRED - Full concurrent maintainability
```

**Note:** Any of the 4 transformers (XFMR-1A, XFMR-1B, XFMR-2A, XFMR-2B) can be maintained using the same procedure. The 2N configuration ensures each LV switchboard always has a backup transformer from the opposite MV bus.

**5. MTU-1 Maintenance:**
```
Procedure:
  1. Bring MTU-3 (standby) online to feed LV-SWBD-A
  2. Transfer load from MTU-1 to MTU-3
  3. Isolate MTU-1 (input and output breakers OPEN)
  4. Perform maintenance on MTU-1
  5. Data center operates on MTU-2 + MTU-3 (N+1 maintained)
  6. NOTE: Each running MTU carries 50% load (2,200 kW)
```

**6. LV-SWBD-A Bus Maintenance:**
```
Procedure:
  1. Close tie breaker (52-TIE)
  2. Transfer all A-side loads to B-side via tie
  3. Open ACB-M1 (LV-SWBD-A de-energized)
  4. Perform maintenance on LV-SWBD-A bus
  5. All loads fed from LV-SWBD-B via tie breaker
  6. NOTE: Tie breaker carries 150% of rated load - time-limited maintenance
```

**7. A-side PDU Maintenance:**
```
Procedure:
  1. IT equipment auto-fails over to B-side PDU (dual-corded)
  2. Isolate A-side PDU
  3. Perform maintenance
  4. No impact to IT loads (running on B-side power)
```

---

## OFFICE LOADS (SEPARATE FROM CRITICAL)

### **Configuration:**
```
Solar Array (800 kW AC @ 400V)  →  ATS-OFFICE (Solar Priority)  ←  Utility Grid (250 kVA @ 10kV → 400V)
                                           ↓
                                    SWBD-OFFICE (630A @ 400V)
                                           ↓
                                   Office Loads: 103 kW
                                   - HVAC: 31 kW
                                   - Lighting: 20 kW
                                   - IT Office: 15 kW
                                   - Security/BMS: 10 kW
                                   - Misc: 27 kW
```

### **Operation:**
- **Normal:** Solar provides 103 kW (13% of solar capacity)
- **Solar Insufficient:** Utility transformer provides makeup
- **Solar Unavailable:** Utility provides 100% office loads
- **No UPS/MTU:** Office loads are non-critical (acceptable outages)

---

## EQUIPMENT SCHEDULE

| Tag | Description | Rating | Qty | Notes |
|-----|-------------|--------|-----|-------|
| **PRIMARY SOURCES** |
| UTILITY | Grid Source | 6 MW @ 10 kV | 2 feeds | 3 MW per feed |
| HPP | Hydro Source | 3.7 MW @ 400V | 2 feeds | 1.85 MW per feed |
| SOLAR | Solar Array | 800 kW @ 400V | 1 | Office only |
| **TRANSFORMERS** |
| XFMR-H1 | HPP Step-Up | 2,500 kVA, 400V/10kV | 1 | HPP Feed 1 |
| XFMR-H2 | HPP Step-Up | 2,500 kVA, 400V/10kV | 1 | HPP Feed 2 |
| XFMR-1A | MV Step-Down | 5,000 kVA, 10kV/400V | 1 | MV-SWBD-A to LV-SWBD-A |
| XFMR-1B | MV Step-Down | 5,000 kVA, 10kV/400V | 1 | MV-SWBD-A to LV-SWBD-B |
| XFMR-2A | MV Step-Down | 5,000 kVA, 10kV/400V | 1 | MV-SWBD-B to LV-SWBD-A |
| XFMR-2B | MV Step-Down | 5,000 kVA, 10kV/400V | 1 | MV-SWBD-B to LV-SWBD-B |
| XFMR-OFFICE | Office Step-Down | 250 kVA, 10kV/400V | 1 | Office loads |
| **MV SWITCHBOARDS** |
| MV-SWBD-A | MV Switchboard | 630A bus @ 10kV | 1 | Utility + HPP Feed 1 |
| MV-SWBD-B | MV Switchboard | 630A bus @ 10kV | 1 | Utility + HPP Feed 2 |
| VCB-UA | Utility VCB A | 630A, 40kA @ 10kV | 1 | Utility Feed 1 |
| VCB-UB | Utility VCB B | 630A, 40kA @ 10kV | 1 | Utility Feed 2 |
| VCB-HA | HPP VCB A | 630A, 40kA @ 10kV | 1 | HPP Feed 1, fast-acting |
| VCB-HB | HPP VCB B | 630A, 40kA @ 10kV | 1 | HPP Feed 2, fast-acting |
| **MTU DRUPS** |
| MTU-1 | DRUPS Unit 1 | 2,750 kVA @ 400V | 1 | Running - LV-SWBD-A |
| MTU-2 | DRUPS Unit 2 | 2,750 kVA @ 400V | 1 | Running - LV-SWBD-B |
| MTU-3 | DRUPS Unit 3 | 2,750 kVA @ 400V | 1 | Standby - N+1 |
| **LV DISTRIBUTION** |
| ACB-M1 | Main Breaker A | 6,300A frame, 5,000A trip | 1 | Drawout ACB |
| ACB-M2 | Main Breaker B | 6,300A frame, 5,000A trip | 1 | Drawout ACB |
| 52-TIE | Tie Breaker | 6,300A frame, 5,000A trip | 1 | N.O., drawout |
| LV-SWBD-A | LV Switchboard | 5,000A bus @ 400V | 1 | Bus A |
| LV-SWBD-B | LV Switchboard | 5,000A bus @ 400V | 1 | Bus B |
| A-IT-1 | IT Panel A | 3,200A MCCB | 1 | IT loads A-side |
| B-IT-1 | IT Panel B | 3,200A MCCB | 1 | IT loads B-side |
| A-COOL-1 | Cooling Panel A | 4,000A MCCB | 1 | Cooling loads A |
| B-COOL-1 | Cooling Panel B | 4,000A MCCB | 1 | Cooling loads B |
| **OFFICE** |
| ATS-OFFICE | Office ATS | 630A @ 400V | 1 | Solar priority |
| SWBD-OFFICE | Office SWBD | 630A bus @ 400V | 1 | Non-critical |

---

## COST ESTIMATE (UPDATED FOR N+1 MTU + 2N TRANSFORMERS)

| System | Cost Estimate (USD) |
|--------|---------------------|
| **PRIMARY SOURCES & TRANSFORMERS** |
| 2 × HPP Step-Up Transformers (2,500 kVA, 400V/10kV) | $200,000 |
| 4 × MV Step-Down Transformers (5,000 kVA, 10kV/400V) - 2N Configuration | $600,000 |
| 2 × MV Switchboards (10 kV, 630A, VCB lineup) | $250,000 |
| Office Transformer (250 kVA, 10kV/400V) | $25,000 |
| **MTU DRUPS (N+1)** |
| 3 × MTU Kinetic DRUPS (2,750 kVA each) | $6,600,000 |
| MTU-3 Bypass Transfer Switches | $50,000 |
| **LV DISTRIBUTION** |
| 2 × Main Breakers (6,300A ACB drawout) | $120,000 |
| 1 × Tie Breaker (6,300A ACB drawout) | $60,000 |
| 2 × LV Switchboards (5,000A bus @ 400V) | $200,000 |
| 4 × Distribution Panels (IT + Cooling) | $180,000 |
| **SOLAR & OFFICE** |
| Solar Array (800 kW AC, inverters + panels) | $800,000 |
| Office ATS (630A with solar priority) | $15,000 |
| Office Switchboard (630A bus) | $20,000 |
| **PROTECTION & CONTROLS** |
| HPP Disconnect Protection System (fast-acting) | $100,000 |
| MTM Controller & Protection Relays | $50,000 |
| BMS Integration & Monitoring | $200,000 |
| **INSTALLATION & COMMISSIONING** |
| Installation, testing, commissioning | $500,000 |
| **SUBTOTAL ELECTRICAL** | **$9,970,000** |

**Cost per MW (IT):**
- $9,970,000 / 3.0 MW = **$3.32M per MW** (excellent for N+1 DRUPS with 2N transformers + HPP integration)

---

## KEY DESIGN NOTES

1. **HPP Priority Operation:** System designed for maximum renewable energy utilization (84% HPP, 16% utility makeup)

2. **Generator Protection:** HPP auto-disconnect (<50 ms) on utility failure protects MTU diesel generators from paralleling with unstable HPP source

3. **2N Transformer Configuration:** 4 × 5,000 kVA step-down transformers provide true Tier III concurrent maintainability
   - Each LV switchboard receives power from BOTH MV switchboards
   - Any single transformer can be removed for maintenance without capacity loss
   - Single transformer failure: Remaining 3 transformers at only 37% utilization (excellent margin)
   - NO tie breaker required for transformer maintenance

4. **N+1 MTU Sizing:** With 2 running + 1 standby, loss of 1 MTU results in 100% utilization of remaining 2 units. No margin for further failures. Consider load shedding plan or upsize MTUs if additional margin required.

5. **Cooling System:** Requires 3 × 1,800 kW chillers (N+1) for 3.0 MW IT load. See separate cooling design document.

6. **Standards Compliance:** IEC 60364 (Georgia), TN-S grounding, 400V distribution throughout

7. **Concurrent Maintainability:** Full Tier III compliance:
   - 2N transformers (any 1 can be maintained)
   - N+1 MTU DRUPS (any 1 can be maintained)
   - Dual MV and LV switchboards
   - Dual-path distribution to all IT loads

---

**Prepared by:** EVS / GGE Engineering Team
**Date:** November 4, 2025
**Revision:** 01
**Status:** For Review
