# GGE DATA CENTER - ELECTRICAL DESIGN (REVISED)
## Main-Tie-Main (MTM) Configuration with Dual Utility Sources

**Document:** ELEC-001-REV02
**Date:** 2025-11-04
**Revision:** 02 (Major Revision)
**Supersedes:** P&ID-E-001 Rev 01

---

## SECTION 1: ELECTRICAL ARCHITECTURE OVERVIEW

### 1.1 DUAL UTILITY SOURCES

**Source 1: HPP (Hydroelectric Power Plant)**
- Capacity: 3.7 MW
- Voltage: 11 kV, 3-phase, 50 Hz
- Connection: Dedicated feeder to GGE
- Reliability: High (hydro generation, stable)

**Source 2: Utility Grid**
- Capacity: 4.0 MW
- Voltage: 11 kV, 3-phase, 50 Hz
- Connection: Grid utility service
- Reliability: Standard utility reliability

**Source 3: On-Site Solar Array (Non-Critical Loads Only)**
- Capacity: ~0.8 MW DC (peak)
- AC Output: ~700 kW AC (after inverter losses)
- Voltage: 400V AC, 3-phase, 50 Hz (via solar inverters)
- Purpose: Office loads only (not critical power)

---

### 1.2 LOAD DISTRIBUTION

#### CRITICAL LOADS (IT + Mechanical Cooling)

| Load Category | Power (kW) | Notes |
|---------------|------------|-------|
| **IT Equipment** | 1,467 | Server/network gear (dual-corded) |
| **Chillers (3 × 800 kW)** | 267 | Compressor loads (2 running, 1 standby) |
| **CHW Pumps (3 × 30 kW)** | 60 | 2 running, 1 standby (N+1) |
| **CW Pumps (3 × 45 kW)** | 90 | 2 running, 1 standby (N+1) |
| **River Water Pumps (3 × 30 kW)** | 60 | 2 running, 1 standby (N+1) |
| **In-Row Cooling Units** | 50 | Fan power (12 units) |
| **Data Hall Lighting** | 15 | LED, emergency backup |
| **BMS & Controls** | 20 | Building management, DCIM, security |
| **Electrical Losses** | 100 | Transformers, distribution (4-5%) |
| **Contingency** | 6 | Future expansion margin |
| **TOTAL CRITICAL LOAD** | **2,135 kW** | Fed from dual utility via MTM |

**Demand Factor:** 1.0 (all critical loads assumed running simultaneously)
**Power Factor:** 0.85 (typical for mixed IT + mechanical loads)
**kVA (Critical):** 2,135 / 0.85 = **2,512 kVA**

---

#### NON-CRITICAL LOADS (Offices, Support Spaces)

| Load Category | Power (kW) | Notes |
|---------------|------------|-------|
| **Office HVAC** | 60 | RTUs for offices, NOC, break rooms |
| **Office Lighting** | 20 | LED, daylight sensors |
| **Office Equipment** | 25 | Computers, printers, kitchen, coffee |
| **NOC Equipment** | 10 | Workstations, monitors (non-critical) |
| **Electrical Losses** | 10 | Office SWBD transformer, distribution |
| **TOTAL NON-CRITICAL LOAD** | **125 kW** | Fed from utility + solar |

**Demand Factor:** 0.80 (not all office loads run simultaneously)
**Diversified Load:** 125 × 0.80 = **100 kW**
**Power Factor:** 0.90 (typical for office/lighting loads)
**kVA (Non-Critical):** 100 / 0.90 = **111 kVA**

---

### 1.3 DESIGN PHILOSOPHY

**Critical Power System:**
- **Topology:** Main-Tie-Main (MTM) with automatic transfer
- **Redundancy:** N+1 at utility source level + 2N at generator level
- **Normal Operation:** Each utility source feeds one main SWBD; tie breaker open
- **Failure Mode:** If one source fails, tie breaker closes, healthy source feeds both SWBDs
- **Backup:** 2 × MTU Kinetic PowerPack (2N) provide backup for both sources
- **Concurrent Maintainability:** Any transformer, breaker, or busway can be isolated without IT impact

**Non-Critical Power System:**
- **Topology:** Dual source (Utility + Solar) with automatic transfer
- **Normal Operation:** Solar provides power during daylight, utility supplements or takes over
- **No UPS/Generator:** Acceptable downtime for office loads during outages

---

## SECTION 2: CRITICAL POWER SYSTEM - MTM CONFIGURATION

### 2.1 SYSTEM SINGLE-LINE DIAGRAM

```
═══════════════════════════════════════════════════════════════════════════════
                        11 kV MEDIUM VOLTAGE DISTRIBUTION
═══════════════════════════════════════════════════════════════════════════════

    HPP SOURCE                                   UTILITY SOURCE
    3.7 MW, 11 kV                                4.0 MW, 11 kV
         │                                              │
         │                                              │
    ┌────▼────┐                                    ┌────▼────┐
    │  11 kV  │                                    │  11 kV  │
    │   CB    │                                    │   CB    │
    │  630A   │                                    │  630A   │
    │         │                                    │         │
    │  52-H1  │                                    │  52-U1  │
    └────┬────┘                                    └────┬────┘
         │                                              │
         │  3 × 185mm² Cu Cable                         │  3 × 185mm² Cu Cable
         │  (11 kV rated)                               │  (11 kV rated)
         │                                              │
    ┌────▼────────────────────┐                   ┌────▼────────────────────┐
    │  TRANSFORMER A           │                   │  TRANSFORMER B           │
    │  3,500 kVA               │                   │  3,500 kVA               │
    │  11 kV / 400V            │                   │  11 kV / 400V            │
    │  Dyn11 (Delta/Wye)       │                   │  Dyn11 (Delta/Wye)       │
    │  Impedance: 6%           │                   │  Impedance: 6%           │
    │  Oil-filled, ONAN        │                   │  Oil-filled, ONAN        │
    │                          │                   │                          │
    │  T1                      │                   │  T2                      │
    └────┬─────────────────────┘                   └────┬─────────────────────┘
         │                                              │
         │  400V Bus                                    │  400V Bus
         │                                              │
    ┌────▼────┐        BYPASS SWITCH            ┌────▼────┐
    │ ACB-M1  │        (Concurrent Maint)       │ ACB-M2  │
    │ 6,300A  │◄───────────────────────────────►│ 6,300A  │
    │ Main 1  │                                  │ Main 2  │
    │         │                                  │         │
    │ Drawout │                                  │ Drawout │
    └────┬────┘                                  └────┬────┘
         │                                            │
         │                                            │
    ┌────▼────────────────────────────────────────────▼────┐
    │            400V MAIN-TIE-MAIN SWITCHBOARD            │
    │                                                       │
    │    MAIN 1 BUS         TIE BREAKER        MAIN 2 BUS  │
    │    (Bus A)            (Normally Open)     (Bus B)    │
    │                                                       │
    │    ┌────────┐         ┌────────┐        ┌────────┐  │
    │    │  Bus A │◄────────┤  Tie   ├────────►│  Bus B │  │
    │    │ 6,300A │         │  ACB   │         │ 6,300A │  │
    │    └────────┘         │ 6,300A │         └────────┘  │
    │                       │        │                      │
    │                       │ 52-TIE │                      │
    │                       │        │                      │
    │                       │Drawout │                      │
    │                       └────────┘                      │
    │                                                       │
    └────┬──────────────────────────────────────────┬──────┘
         │                                          │
         │                                          │


═══════════════════════════════════════════════════════════════════════════════
                    MTU KINETIC POWERPACK BACKUP (2N)
═══════════════════════════════════════════════════════════════════════════════

         │                                          │
         │                                          │
    ┌────▼────────────────┐                   ┌────▼────────────────┐
    │  MTU KP7 UNIT #1    │                   │  MTU KP7 UNIT #2    │
    │  2,200 kW / 2,750kVA│                   │  2,200 kW / 2,750kVA│
    │  400V, 50 Hz        │                   │  400V, 50 Hz        │
    │  Flywheel: 15-20s   │                   │  Flywheel: 15-20s   │
    │                     │                   │                     │
    │  Connects via ATS   │                   │  Connects via ATS   │
    │  to Bus A           │                   │  to Bus B           │
    │                     │                   │                     │
    │  MTU-1              │                   │  MTU-2              │
    └────┬────────────────┘                   └────┬────────────────┘
         │                                          │
         │  400V, 5,000A ACB                        │  400V, 5,000A ACB
         │  Automatic Transfer                      │  Automatic Transfer
         │                                          │
    To Bus A (ATS)                             To Bus B (ATS)
    (Seamless transfer)                        (Seamless transfer)


═══════════════════════════════════════════════════════════════════════════════
                    400V CRITICAL LOAD DISTRIBUTION
═══════════════════════════════════════════════════════════════════════════════

    BUS A (Main 1)                              BUS B (Main 2)
         │                                          │
         ├────────────────┬────────────────┬────────┤
         │                │                │        │
    ┌────▼────┐      ┌────▼────┐     ┌────▼────┐  │
    │ Panel   │      │ Panel   │     │ Panel   │  │
    │ A-IT-1  │      │ A-COOL-1│     │ B-IT-1  │  │
    │ 2,500A  │      │ 3,200A  │     │ 2,500A  │  │
    │ MCCB    │      │ MCCB    │     │ MCCB    │  │
    └────┬────┘      └────┬────┘     └────┬────┘  │
         │                │                │       │
         │                │                │  ┌────▼────┐
    IT Racks         Chillers         IT Racks │ Panel   │
    PDU-A Side       CHW Pumps        PDU-B    │ B-COOL-1│
    (750 kW)         CW Pumps         Side     │ 3,200A  │
                     River Pumps      (750 kW) │ MCCB    │
                     In-Row Units              └────┬────┘
                     (527 kW)                       │
                                                    │
                                               Chillers
                                               CHW Pumps
                                               CW Pumps
                                               River Pumps
                                               In-Row Units
                                               (527 kW)
```

---

### 2.2 LOAD CALCULATIONS - CRITICAL SYSTEM

#### Bus A (Main 1) - Normal Operation

**Panel A-IT-1 (IT Equipment - A-Side PDUs)**
- Connected IT load: 1,467 kW (total facility IT)
- A-Side PDUs: 50% of IT = 734 kW
- Power factor: 0.95 (IT equipment with power supplies)
- kVA: 734 / 0.95 = 773 kVA
- Current @ 400V: I = 773,000 / (√3 × 400) = **1,115 A**
- **Panel rating: 2,500 A MCCB** (feeder from Bus A)

**Panel A-COOL-1 (Cooling Equipment - A-Side)**
- Chiller #1 compressor: 134 kW
- CHW Pump #1: 30 kW
- CW Pump #1: 45 kW
- River Water Pump #1: 30 kW
- In-Row Units #1-6 (6 × 8 kW fans): 48 kW
- **Total: 287 kW**
- Power factor: 0.85 (motors, VFDs)
- kVA: 287 / 0.85 = 338 kVA
- Current @ 400V: I = 338,000 / (√3 × 400) = **487 A**
- With 150% motor starting: 487 × 1.5 = 731 A
- **Panel rating: 3,200 A MCCB** (accommodates motor starting)

**Data Hall Lighting, BMS (A-Side)**
- Lighting: 8 kW (50% of 15 kW)
- BMS/Controls: 10 kW (50% of 20 kW)
- **Total: 18 kW**
- Current @ 400V: **26 A**
- **Fed from A-IT-1 panel via sub-panel, 100 A MCCB**

**Total Bus A Load (Normal Operation):**
- IT (A-side): 734 kW
- Cooling (A-side): 287 kW
- Lighting/BMS: 18 kW
- **Total: 1,039 kW** = **1,222 kVA** @ 0.85 PF
- **Current: 1,763 A @ 400V**

---

#### Bus B (Main 2) - Normal Operation

**Panel B-IT-1 (IT Equipment - B-Side PDUs)**
- Connected IT load: 1,467 kW (total facility IT)
- B-Side PDUs: 50% of IT = 734 kW
- Power factor: 0.95
- kVA: 773 kVA
- Current @ 400V: **1,115 A**
- **Panel rating: 2,500 A MCCB**

**Panel B-COOL-1 (Cooling Equipment - B-Side)**
- Chiller #2 compressor: 134 kW
- CHW Pump #2: 30 kW
- CW Pump #2: 45 kW
- River Water Pump #2: 30 kW
- In-Row Units #7-12 (6 × 8 kW fans): 48 kW
- **Total: 287 kW**
- Power factor: 0.85
- kVA: 338 kVA
- Current @ 400V: **487 A** (731 A with motor starting)
- **Panel rating: 3,200 A MCCB**

**Data Hall Lighting, BMS (B-Side)**
- Lighting: 8 kW
- BMS/Controls: 10 kW
- **Total: 18 kW**
- Current: **26 A**
- **Fed from B-IT-1 panel via sub-panel, 100 A MCCB**

**Total Bus B Load (Normal Operation):**
- IT (B-side): 734 kW
- Cooling (B-side): 287 kW
- Lighting/BMS: 18 kW
- **Total: 1,039 kW** = **1,222 kVA** @ 0.85 PF
- **Current: 1,763 A @ 400V**

---

#### Standby Equipment (Powered from Either Bus via Selector Switch)

**Chiller #3 (Standby)**
- Power: 134 kW
- Normally OFF, manually started if Chiller #1 or #2 fails
- Can be powered from Bus A or Bus B (manual selector switch)

**Pumps #3 (Standby - CHW, CW, River Water)**
- CHW Pump #3: 30 kW
- CW Pump #3: 45 kW
- River Water Pump #3: 30 kW
- **Total: 105 kW**
- Powered from whichever bus has spare capacity (automatic VFD start)

---

### 2.3 SINGLE SOURCE OPERATION (Failure Mode)

**Scenario: HPP Source Fails (Source 1 Down)**

When HPP fails:
1. Bus A loses utility power
2. Tie breaker (52-TIE) automatically closes (within 100ms)
3. Bus B (fed from Utility Source 2) now feeds both Bus A and Bus B
4. Total load on Bus B: 1,039 kW (Bus A) + 1,039 kW (Bus B) = **2,078 kW**

**Verification:**
- Transformer B capacity: 3,500 kVA = 2,975 kW @ 0.85 PF
- Load: 2,078 kW = 2,445 kVA @ 0.85 PF
- **Margin: 2,975 - 2,078 = 897 kW (30% margin) ✓**

**Utility Source 2 Capacity:**
- Source capacity: 4.0 MW
- Load: 2.078 MW
- **Margin: 4.0 - 2.078 = 1.922 MW (48% margin) ✓**

**Transformer B Current:**
- kVA: 2,445 kVA
- Current @ 400V: I = 2,445,000 / (√3 × 400) = **3,526 A**
- Transformer rating: 3,500 kVA → 5,052 A @ 400V
- **Utilization: 3,526 / 5,052 = 70% ✓**

---

**Scenario: Utility Source Fails (Source 2 Down)**

When Utility fails:
1. Bus B loses utility power
2. Tie breaker (52-TIE) automatically closes
3. Bus A (fed from HPP Source 1) now feeds both buses
4. Total load on Bus A: **2,078 kW**

**Verification:**
- Transformer A capacity: 3,500 kVA = 2,975 kW @ 0.85 PF
- Load: 2,078 kW
- **Margin: 897 kW (30% margin) ✓**

**HPP Source Capacity:**
- Source capacity: 3.7 MW
- Load: 2.078 MW
- **Margin: 3.7 - 2.078 = 1.622 MW (44% margin) ✓**

---

### 2.4 BREAKER SIZING - CRITICAL SYSTEM

#### 11 kV Medium Voltage Breakers

**52-H1 (HPP Source Breaker)**
- Load: 3,500 kVA transformer (max)
- Current @ 11 kV: I = 3,500,000 / (√3 × 11,000) = 184 A
- Rating: **630 A @ 11 kV** (vacuum circuit breaker, VCB)
- Short-circuit rating: 25 kA (3-second)
- Type: Indoor, withdrawable, motor-operated

**52-U1 (Utility Source Breaker)**
- Load: 3,500 kVA transformer (max)
- Current @ 11 kV: 184 A
- Rating: **630 A @ 11 kV** (VCB)
- Short-circuit rating: 25 kA (3-second)
- Type: Indoor, withdrawable, motor-operated

---

#### 400V Low Voltage Breakers

**ACB-M1 (Main 1 Breaker - Bus A)**
- Load: 1,222 kVA normal, 2,445 kVA (failure mode)
- Current normal: 1,763 A
- Current failure mode: 3,526 A
- Motor starting inrush: +50% = 5,289 A peak
- Rating: **6,300 A @ 400V** (air circuit breaker, ACB)
- Trip setting: 6,300 A frame, 5,000 A trip
- Short-circuit rating: 65 kA @ 400V
- Type: Drawout, electronically-tripped, with ground fault protection

**ACB-M2 (Main 2 Breaker - Bus B)**
- Load: 1,222 kVA normal, 2,445 kVA (failure mode)
- Current normal: 1,763 A
- Current failure mode: 3,526 A
- Rating: **6,300 A @ 400V** (ACB)
- Trip setting: 6,300 A frame, 5,000 A trip
- Short-circuit rating: 65 kA @ 400V
- Type: Drawout, electronically-tripped, with ground fault protection

**52-TIE (Tie Breaker)**
- Load: 2,445 kVA (when closed during failure)
- Current: 3,526 A
- Motor starting inrush: 5,289 A peak
- Rating: **6,300 A @ 400V** (ACB)
- Trip setting: 6,300 A frame, 5,000 A trip
- Short-circuit rating: 65 kA @ 400V
- Type: Drawout, electronically-tripped
- **Control:** Automatic closure on source failure (relay logic)
- **Normal position:** OPEN (no parallel operation of sources)

---

#### MTU Kinetic PowerPack Breakers

**ACB-MTU1 (MTU Unit #1 to Bus A)**
- MTU capacity: 2,750 kVA
- Current @ 400V: I = 2,750,000 / (√3 × 400) = 3,969 A
- Rating: **5,000 A @ 400V** (ACB)
- Trip setting: 5,000 A frame, 4,500 A trip
- Short-circuit rating: 65 kA @ 400V
- Type: Drawout, motorized, automatic transfer switch (ATS) function

**ACB-MTU2 (MTU Unit #2 to Bus B)**
- MTU capacity: 2,750 kVA
- Current @ 400V: 3,969 A
- Rating: **5,000 A @ 400V** (ACB)
- Trip setting: 5,000 A frame, 4,500 A trip
- Short-circuit rating: 65 kA @ 400V
- Type: Drawout, motorized, ATS function

---

#### Distribution Panel Breakers

**Panel A-IT-1 & B-IT-1 (IT Equipment)**
- Load: 773 kVA per panel
- Current: 1,115 A per panel
- Rating: **2,500 A MCCB** (molded case circuit breaker)
- Trip setting: 2,500 A frame, 1,600 A trip (adjustable)
- Short-circuit rating: 50 kA @ 400V

**Panel A-COOL-1 & B-COOL-1 (Cooling Equipment)**
- Load: 338 kVA per panel
- Current: 487 A continuous, 731 A (motor starting)
- Rating: **3,200 A MCCB**
- Trip setting: 3,200 A frame, 1,000 A trip, I²t curve for motor starting
- Short-circuit rating: 50 kA @ 400V

---

### 2.5 CONCURRENT MAINTAINABILITY - BYPASS PROVISIONS

**Transformer Bypass (for T1 and T2):**

Each transformer has a **manual bypass switch** to allow transformer maintenance without facility shutdown:

**Configuration:**
```
11 kV Source ──┬─── Transformer ───┬─── 400V Main Breaker ─── Bus
               │                   │
               └─── Bypass Path ───┘
                    (Manual Switch,
                     Normally Open)
```

**Bypass Switch Specifications:**
- Type: Load break switch, 630 A @ 11 kV
- Operation: Manual, padlock in OFF position (safety interlock)
- Purpose: During transformer oil sampling, breaker maintenance, or BDV testing

**Maintenance Procedure (Transformer T1):**
1. Transfer critical loads to Bus B only (close tie breaker 52-TIE)
2. Open Main 1 breaker (ACB-M1)
3. Open 11 kV breaker (52-H1)
4. Close bypass switch (energizes Bus A from HPP via bypass path, bypassing T1)
5. Isolate transformer T1 for maintenance
6. Restore: Reverse sequence

**Note:** Bypass switch rated for continuous operation, but typically used only during maintenance windows.

---

**Main Breaker Bypass (for ACB-M1, ACB-M2):**

All main breakers are **drawout type**, allowing removal for maintenance:

**Maintenance Procedure (Main 1 Breaker ACB-M1):**
1. Transfer all loads to Bus B (close tie breaker 52-TIE)
2. Open ACB-M1
3. Rack out (withdraw) ACB-M1 from cubicle
4. Perform maintenance on ACB-M1 off-site or in workshop
5. Install spare breaker (if available) or restore ACB-M1 after service

**Concurrent Maintenance Verification:**
- During ACB-M1 maintenance: All critical loads powered from Bus B via tie breaker ✓
- During ACB-M2 maintenance: All critical loads powered from Bus A via tie breaker ✓
- During 52-TIE maintenance: Each bus operates independently (redundant paths) ✓

---

**MTU Bypass Consideration:**

MTU Kinetic PowerPacks have **internal bypass capability** (flywheel can be isolated for maintenance while diesel engine continues to run).

**No external bypass switch required** for MTU units because:
1. MTU provides continuous power even during flywheel maintenance
2. 2N redundancy: Can isolate one MTU entirely, other MTU + utility source provides power
3. MTU maintenance typically performed during low-risk periods (both utility sources available)

---

### 2.6 CONTROLLER ARCHITECTURE - SIMPLE & REDUNDANT

**Control Philosophy:**
- Simple relay-based logic (not complex PLC)
- Redundant protection relays
- Automatic tie breaker control
- Manual override capability

**Key Control Functions:**

**1. Automatic Transfer (Tie Breaker Control)**

**Logic:**
- IF (HPP source voltage < 80% nominal) AND (Utility source voltage > 90% nominal)
  - THEN: Close tie breaker (52-TIE)
  - Result: Utility feeds both buses

- IF (Utility source voltage < 80% nominal) AND (HPP source voltage > 90% nominal)
  - THEN: Close tie breaker (52-TIE)
  - Result: HPP feeds both buses

- IF (Both sources healthy > 90% nominal)
  - THEN: Open tie breaker (52-TIE)
  - Result: Independent bus operation (normal)

**Redundancy:**
- Two independent protection relays monitor each source
- Voting logic: 2-out-of-2 agreement required for tie breaker action
- Manual override: Lockout switch prevents automatic closure (for maintenance)

**2. MTU Start Signal**

**Logic:**
- IF (Bus A voltage < 80% nominal for >1 second)
  - THEN: Send start signal to MTU-1
  - MTU provides 15-20s flywheel ride-through while diesel starts

- IF (Bus B voltage < 80% nominal for >1 second)
  - THEN: Send start signal to MTU-2

**Redundancy:**
- Independent undervoltage relays on each bus
- Hardwired start signal (not network-dependent)

**3. Load Shedding (Optional)**

If both sources fail AND MTU units running at >90% capacity:
- Shed non-essential cooling equipment (standby units)
- Maintain IT equipment power (priority)

**Not implemented in Phase 1** (MTU capacity sufficient for all loads)

---

**Controller Hardware:**

**Primary Controller:**
- Schneider Electric Easergy P5 or ABB REF615 protection relay
- Functions: Voltage sensing, tie breaker control, MTU start
- Redundant power supply (120V DC from battery bank)

**Secondary Controller (Redundant):**
- Identical relay, independent sensing
- Voting logic via hardwired inputs
- Takes over if primary fails (automatic switchover)

**Manual Control Panel:**
- Located in main electrical room
- Selector switches: Auto / Manual / Test
- Status lights: Source 1 OK, Source 2 OK, Tie breaker position, MTU running
- Emergency stop (opens all breakers, for safety during maintenance)

---

## SECTION 3: NON-CRITICAL POWER SYSTEM (OFFICE LOADS)

### 3.1 LOAD CALCULATION - OFFICE LOADS

| Load Category | Power (kW) | Demand Factor | Diversified Load (kW) |
|---------------|------------|---------------|-----------------------|
| **Office HVAC** | 60 | 0.80 | 48 |
| **Office Lighting** | 20 | 0.70 | 14 |
| **Office Equipment** | 25 | 0.60 | 15 |
| **NOC Equipment** | 10 | 1.00 | 10 |
| **Kitchen, Coffee** | 15 | 0.40 | 6 |
| **Electrical Losses** | 10 | 1.00 | 10 |
| **TOTAL** | 140 | - | **103 kW** |

**Power Factor:** 0.90 (mixed lighting + HVAC)
**kVA:** 103 / 0.90 = **114 kVA**
**Current @ 400V:** I = 114,000 / (√3 × 400) = **165 A**

---

### 3.2 OFFICE SWBD CONFIGURATION

```
═══════════════════════════════════════════════════════════════════════════════
                    OFFICE LOADS - DUAL SOURCE (UTILITY + SOLAR)
═══════════════════════════════════════════════════════════════════════════════

    UTILITY SOURCE                              SOLAR ARRAY
    11 kV                                       800 kW DC Peak
         │                                           │
         │                                      ┌────▼─────┐
    ┌────▼────────────┐                        │  Solar   │
    │  TRANSFORMER 3  │                        │ Inverters│
    │  250 kVA        │                        │ 700 kW AC│
    │  11 kV / 400V   │                        │ @ 400V   │
    │  Dyn11          │                        └────┬─────┘
    │                 │                             │
    │  T3             │                             │
    └────┬────────────┘                             │
         │                                           │
         │  400V                                     │  400V
         │                                           │
    ┌────▼────┐                                ┌────▼────┐
    │  CB-O1  │                                │  CB-S1  │
    │  400A   │                                │ 1,600A  │
    │  MCCB   │                                │  MCCB   │
    └────┬────┘                                └────┬────┘
         │                                           │
         └───────────────────┬───────────────────────┘
                             │
                   ┌─────────▼──────────┐
                   │  AUTOMATIC         │
                   │  TRANSFER SWITCH   │
                   │  (ATS)             │
                   │  Priority: Solar   │
                   │  Backup: Utility   │
                   └─────────┬──────────┘
                             │
                   ┌─────────▼──────────┐
                   │  OFFICE SWBD       │
                   │  400V, 400A        │
                   │                    │
                   │  Main Bus          │
                   └─────────┬──────────┘
                             │
                    ┌────────┼────────┐
                    │        │        │
               ┌────▼───┐ ┌──▼──┐ ┌──▼──┐
               │ HVAC   │ │Light│ │Equip│
               │ 100A   │ │ 63A │ │100A │
               │ Panel  │ │Panel│ │Panel│
               └────────┘ └─────┘ └─────┘
```

---

### 3.3 OFFICE SYSTEM BREAKER SIZING

**Transformer 3 (Utility to Office SWBD)**
- Rating: 250 kVA, 11 kV / 400V
- Purpose: Backup power for offices when solar unavailable
- Current @ 11 kV: I = 250,000 / (√3 × 11,000) = 13 A
- **11 kV breaker (CB-U2): 63 A @ 11 kV** (VCB)
- Current @ 400V: I = 250,000 / (√3 × 400) = 361 A
- **400V breaker (CB-O1): 400 A MCCB**

**Solar Inverter Output**
- Solar AC output: 700 kW (peak, midday)
- Power factor: 1.0 (inverter power factor correction)
- kVA: 700 kVA
- Current @ 400V: I = 700,000 / (√3 × 400) = 1,010 A
- **400V breaker (CB-S1): 1,600 A MCCB**
- Note: Oversized for solar capacity because inverters can provide short-term overload (1.1-1.2×)

**Office SWBD Main Breaker**
- Load: 114 kVA
- Current: 165 A
- Rating: **400 A MCCB** (main)
- Fed from ATS (either utility or solar source)

**Office Distribution Panel Breakers:**
- HVAC Panel: 48 kW → 69 A → **100 A MCCB**
- Lighting Panel: 14 kW → 20 A → **63 A MCCB**
- Equipment Panel: 15 kW → 22 A → **100 A MCCB** (includes receptacles, kitchen)

---

### 3.4 SOLAR + UTILITY OPERATION

**Daytime (Solar Available):**
- Solar inverters provide 700 kW AC (peak capacity)
- Office load: 103 kW
- **Excess solar: 700 - 103 = 597 kW** → Exported to utility grid OR curtailed
- ATS position: Solar (primary source)
- Utility transformer T3: Offline (no load)

**Evening/Night (No Solar):**
- Solar output: 0 kW
- ATS automatically transfers to utility source
- Transformer T3 provides 103 kW to office loads
- Transfer time: <100ms (fast transfer, acceptable for office equipment)

**Cloudy Day (Partial Solar):**
- Solar output: 100-400 kW (variable)
- If solar > office load: Solar provides all power
- If solar < office load: ATS transfers to utility
- No parallel operation (ATS is break-before-make)

**No Battery Storage:**
- Solar array does NOT include battery storage
- All excess solar exported to grid (if allowed by utility) or curtailed
- Offices have no UPS (acceptable downtime during transfers)

---

## SECTION 4: ELECTRICAL EQUIPMENT SCHEDULE

| Tag | Description | Rating | Qty | Location | Notes |
|-----|-------------|--------|-----|----------|-------|
| **MEDIUM VOLTAGE** |
| T1 | Transformer HPP→400V | 3,500 kVA, 11kV/400V | 1 | Outdoor pad | Oil-filled, ONAN |
| T2 | Transformer Utility→400V | 3,500 kVA, 11kV/400V | 1 | Outdoor pad | Oil-filled, ONAN |
| 52-H1 | HPP source breaker | 630A @ 11kV, VCB | 1 | 11kV switchgear | Motor-operated |
| 52-U1 | Utility source breaker | 630A @ 11kV, VCB | 1 | 11kV switchgear | Motor-operated |
| **LOW VOLTAGE - CRITICAL** |
| ACB-M1 | Main 1 breaker (Bus A) | 6,300A ACB @ 400V | 1 | MTM SWBD | Drawout, electronic trip |
| ACB-M2 | Main 2 breaker (Bus B) | 6,300A ACB @ 400V | 1 | MTM SWBD | Drawout, electronic trip |
| 52-TIE | Tie breaker | 6,300A ACB @ 400V | 1 | MTM SWBD | Drawout, auto-close |
| ACB-MTU1 | MTU #1 breaker | 5,000A ACB @ 400V | 1 | MTM SWBD | ATS function |
| ACB-MTU2 | MTU #2 breaker | 5,000A ACB @ 400V | 1 | MTM SWBD | ATS function |
| MTU-1 | Kinetic PowerPack #1 | 2,200 kW / 2,750 kVA | 1 | Generator yard | 2N redundancy |
| MTU-2 | Kinetic PowerPack #2 | 2,200 kW / 2,750 kVA | 1 | Generator yard | 2N redundancy |
| A-IT-1 | IT distribution panel A | 2,500A MCCB @ 400V | 1 | Elec room | To PDU-A side |
| B-IT-1 | IT distribution panel B | 2,500A MCCB @ 400V | 1 | Elec room | To PDU-B side |
| A-COOL-1 | Cooling panel A | 3,200A MCCB @ 400V | 1 | Elec room | Chillers, pumps |
| B-COOL-1 | Cooling panel B | 3,200A MCCB @ 400V | 1 | Elec room | Chillers, pumps |
| **LOW VOLTAGE - OFFICE** |
| T3 | Transformer Utility→Office | 250 kVA, 11kV/400V | 1 | Outdoor pad | Dry-type or oil |
| CB-U2 | Utility office breaker | 63A @ 11kV, VCB | 1 | 11kV switchgear | - |
| CB-O1 | Office utility breaker | 400A MCCB @ 400V | 1 | Office SWBD | From T3 |
| CB-S1 | Solar breaker | 1,600A MCCB @ 400V | 1 | Solar inverter room | From inverters |
| ATS-O1 | Office auto transfer switch | 400A @ 400V | 1 | Office SWBD | Solar priority |
| INV-1 to INV-4 | Solar inverters | 175 kW each @ 400V | 4 | Solar inverter room | 700 kW total AC |

---

## SECTION 5: CABLE SCHEDULE - MAJOR FEEDERS

| From | To | Cable Type | Size (mm²) | Length (m) | Voltage | Current Rating (A) |
|------|-----|------------|------------|------------|---------|-------------------|
| HPP utility pole | 52-H1 | MV XLPE, Cu | 3 × 185 | [TBD] | 11 kV | 630 |
| Utility pole | 52-U1 | MV XLPE, Cu | 3 × 185 | [TBD] | 11 kV | 630 |
| 52-H1 | T1 primary | MV XLPE, Cu | 3 × 185 | 20 | 11 kV | 630 |
| 52-U1 | T2 primary | MV XLPE, Cu | 3 × 185 | 25 | 11 kV | 630 |
| T1 secondary | ACB-M1 | LV PVC, Cu | 4 × 400 | 15 | 400V | 6,300 |
| T2 secondary | ACB-M2 | LV PVC, Cu | 4 × 400 | 15 | 400V | 6,300 |
| MTU-1 | ACB-MTU1 | LV PVC, Cu | 4 × 300 | 30 | 400V | 5,000 |
| MTU-2 | ACB-MTU2 | LV PVC, Cu | 4 × 300 | 30 | 400V | 5,000 |
| Bus A | A-IT-1 | Busway | 2,500A | 10 | 400V | 2,500 |
| Bus B | B-IT-1 | Busway | 2,500A | 10 | 400V | 2,500 |
| Bus A | A-COOL-1 | Busway | 3,200A | 15 | 400V | 3,200 |
| Bus B | B-COOL-1 | Busway | 3,200A | 15 | 400V | 3,200 |
| 52-U1 | T3 primary | MV XLPE, Cu | 3 × 25 | 30 | 11 kV | 63 |
| T3 secondary | CB-O1 | LV PVC, Cu | 4 × 120 | 10 | 400V | 400 |
| Solar inverters | CB-S1 | LV PVC, Cu | 4 × 300 | 50 | 400V | 1,600 |

**Notes:**
- Cable sizing per IEC 60364-5-52 (current-carrying capacity)
- Voltage drop: <3% for critical loads, <5% for non-critical
- All cables include protective earth (PE) conductor (4th wire)
- Busway: Aluminum or copper bus bars in sheet metal enclosure

---

## SECTION 6: SUMMARY & VERIFICATION

### 6.1 DESIGN SUMMARY

**Critical Power:**
- **Sources:** HPP (3.7 MW) + Utility (4.0 MW)
- **Configuration:** MTM with automatic tie breaker
- **Transformers:** 2 × 3,500 kVA (each can carry full load)
- **Backup:** 2 × MTU KP7 Kinetic PowerPack (2N redundancy)
- **Load:** 2,135 kW (IT + mechanical)
- **Concurrent maintainability:** ✓ All equipment has bypass/redundancy

**Non-Critical Power:**
- **Sources:** Utility (via T3) + Solar (800 kW DC / 700 kW AC)
- **Configuration:** ATS with solar priority
- **Load:** 103 kW diversified (offices, support spaces)
- **Backup:** No UPS/generator (acceptable downtime)

---

### 6.2 CAPACITY VERIFICATION

**Single Source Failure Mode:**
- Required capacity: 2,135 kW
- Each transformer: 3,500 kVA = 2,975 kW @ 0.85 PF
- **Margin: 2,975 - 2,135 = 840 kW (28% margin) ✓**

**MTU Capacity (Dual Source Failure):**
- Each MTU: 2,200 kW
- With 2N: Either MTU can carry full facility load
- Required: 2,135 kW
- **Margin: 2,200 - 2,135 = 65 kW (3% margin, minimal but acceptable) ✓**

**Recommendation:** If future expansion >2,200 kW, add 3rd MTU for N+1 configuration

---

### 6.3 TIER III COMPLIANCE

| Requirement | GGE Design | Compliant |
|-------------|------------|-----------|
| **Dual utility paths** | HPP + Utility (MTM) | ✓ Yes |
| **N+1 generators** | 2N (MTU units) | ✓ Exceeds |
| **N+1 transformers** | 2 × 3,500 kVA (each carries full load) | ✓ Exceeds (2N) |
| **Concurrent maint** | Drawout breakers, bypass switches, tie breaker | ✓ Yes |
| **No single point of failure** | Dual distribution (Bus A + Bus B) | ✓ Yes |
| **IT dual-corded** | PDU-A + PDU-B from separate buses | ✓ Yes |

**Conclusion:** Design meets Uptime Institute Tier III requirements. ✓

---

### 6.4 COST ESTIMATE (ELECTRICAL SYSTEMS)

| Item | Qty | Unit Cost | Total |
|------|-----|-----------|-------|
| **Medium Voltage** |
| 11 kV Switchgear (HPP + Utility + Office) | 1 | $200,000 | $200,000 |
| Transformers (3,500 kVA) | 2 | $100,000 | $200,000 |
| Transformer (250 kVA, office) | 1 | $25,000 | $25,000 |
| 11 kV cables, terminations | - | $50,000 | $50,000 |
| **Low Voltage - Critical** |
| MTM Switchboard (dual bus, 6,300A) | 1 | $400,000 | $400,000 |
| MTU Kinetic PowerPack (2,200 kW) | 2 | $2,000,000 | $4,000,000 |
| Distribution panels (IT + Cooling) | 4 | $50,000 | $200,000 |
| 400V cables, busway | - | $150,000 | $150,000 |
| **Low Voltage - Office** |
| Solar inverters (700 kW AC) | 1 | $350,000 | $350,000 |
| Solar array (800 kW DC) | 1 | $800,000 | $800,000 |
| Office SWBD + ATS | 1 | $50,000 | $50,000 |
| **Protection & Control** |
| Protection relays (redundant) | 1 | $50,000 | $50,000 |
| BMS integration, metering | 1 | $100,000 | $100,000 |
| **Installation & Commissioning** | - | $500,000 | $500,000 |
| **TOTAL ELECTRICAL SYSTEMS** | | | **$7,075,000** |

**Cost per MW (IT):** $7,075,000 / 1.47 MW = **$4.8M per MW**

---

**Prepared by:** EVS / GGE Engineering Team
**Date:** November 4, 2025
**Revision:** 02
**Status:** For Construction
