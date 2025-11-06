YOU # GGE DATA CENTER - ELECTRICAL SINGLE-LINE DIAGRAM (MTM)
## Phase 1: 1.47 MW IT Capacity - DUAL UTILITY SOURCES

**Document:** P&ID-E-001
**Date:** 2025-11-04
**Revision:** 03 - MTM with HPP 400V Step-Up + Redundant MV SWBDs

---

## ELECTRICAL SINGLE-LINE DIAGRAM - MAIN-TIE-MAIN (MTM) TOPOLOGY

```
═══════════════════════════════════════════════════════════════════════════════
                           DUAL UTILITY SOURCES (DIFFERENT VOLTAGES)
═══════════════════════════════════════════════════════════════════════════════

    SOURCE 1: HPP                                    SOURCE 2: UTILITY GRID
    3.7 MW @ 400V                                   4.0 MW @ 11 kV
    3-Phase, 50 Hz                                  3-Phase, 50 Hz
    (Low Voltage Source)                            (Medium Voltage Source)
         │                                                   │
         │                                                   │
    ┌────▼─────────────┐                            ┌────────▼──────────┐
    │ STEP-UP XFMR     │                            │ 11 kV VCB         │
    │ 3,500 kVA        │                            │ (Incoming)        │
    │ 400V / 11 kV     │                            │ 630A, 40 kA       │
    │ Dyn11 Vector     │                            └────────┬──────────┘
    │ Oil-filled ONAN  │                                     │
    │ Z = 6%           │                                     │
    └────┬─────────────┘                                     │
         │                                                   │
         │ 3×185mm² Cu XLPE                                 │ 3×185mm² Cu XLPE
         │ 11 kV MV Cable                                   │ 11 kV MV Cable
         │                                                   │
    ┌────▼─────────────┐                            ┌────────▼──────────┐
    │ MV SWBD A        │                            │ MV SWBD B         │
    │ (11 kV)          │                            │ (11 kV)           │
    │ 630A Bus         │                            │ 630A Bus          │
    │ VCB Lineup       │                            │ VCB Lineup        │
    └────┬─────────────┘                            └────────┬──────────┘
         │                                                   │
         │ 3×185mm² Cu XLPE                                 │ 3×185mm² Cu XLPE
         │ MV Cable                                          │ MV Cable
         │                                                   │
    ┌────▼─────────────┐                            ┌────────▼──────────┐
    │ STEP-DOWN XFMR-A │                            │ STEP-DOWN XFMR-B  │
    │ 3,500 kVA        │                            │ 3,500 kVA         │
    │ 11 kV / 400V     │                            │ 11 kV / 400V      │
    │ Dyn11 Vector     │                            │ Dyn11 Vector      │
    │ Oil-filled ONAN  │                            │ Oil-filled ONAN   │
    │ Z = 6%           │                            │ Z = 6%            │
    └────┬─────────────┘                            └────────┬──────────┘
         │                                                   │
         │ 4×400mm² Cu LV Cable                             │ 4×400mm² Cu LV Cable
         │                                                   │
    ┌────▼─────────────┐                            ┌────────▼──────────┐
    │ ACB-M1 (MAIN 1)  │                            │ ACB-M2 (MAIN 2)   │
    │ 6,300A Frame     │                            │ 6,300A Frame      │
    │ 5,000A Trip      │                            │ 5,000A Trip       │
    │ 65 kA SCCR       │                            │ 65 kA SCCR        │
    │ Drawout Type     │                            │ Drawout Type      │
    │ Electronic Trip  │                            │ Electronic Trip   │
    └────┬─────────────┘                            └────────┬──────────┘
         │                                                   │
         │                                                   │
    ┌────▼─────────────┐         ┌─────────┐        ┌───────▼───────────┐
    │  BUS A (MAIN 1)  │◄────────┤ 52-TIE  ├───────►│  BUS B (MAIN 2)   │
    │  SWBD-A          │         │ 6,300A  │        │  SWBD-B           │
    │  400V, 3Ø, 50Hz  │         │ N.O.    │        │  400V, 3Ø, 50Hz   │
    │  2,500A Bus      │         │ Drawout │        │  2,500A Bus       │
    └────┬─────────────┘         └─────────┘        └───────┬───────────┘
         │                                                   │
         │                                                   │
═══════════════════════════════════════════════════════════════════════════════
                         MTU KINETIC POWERPACK (2N BACKUP)
═══════════════════════════════════════════════════════════════════════════════

         │                                                   │
         │ (Normal: Utility via transformers)               │
         │ (Fail: MTU diesel + flywheel)                    │
         │                                                   │
    ┌────▼──────────────┐                          ┌────────▼─────────────┐
    │ MTU-1 UNIT #1     │                          │ MTU-2 UNIT #2        │
    │ 2,200 kW output   │                          │ 2,200 kW output      │
    │ 2,750 kVA         │                          │ 2,750 kVA            │
    │ 400V, 3Ø, 50 Hz   │                          │ 400V, 3Ø, 50 Hz      │
    │ Integrated Diesel │                          │ Integrated Diesel    │
    │ + Flywheel UPS    │                          │ + Flywheel UPS       │
    │ 15-20 sec bridge  │                          │ 15-20 sec bridge     │
    │ <10s diesel start │                          │ <10s diesel start    │
    └────┬──────────────┘                          └────────┬─────────────┘
         │                                                   │
         │ 4×300mm² Cu LV Cable                             │ 4×300mm² Cu LV Cable
         │                                                   │
    ┌────▼──────────────┐                          ┌────────▼─────────────┐
    │ ACB-MTU1          │                          │ ACB-MTU2             │
    │ 5,000A Frame      │                          │ 5,000A Frame         │
    │ 4,000A Trip       │                          │ 4,000A Trip          │
    │ 65 kA SCCR        │                          │ 65 kA SCCR           │
    │ w/ ATS Function   │                          │ w/ ATS Function      │
    └────┬──────────────┘                          └────────┬─────────────┘
         │                                                   │
         └─────────────────►to BUS A               ◄────────┘
                           (Seamless Transfer)     to BUS B


═══════════════════════════════════════════════════════════════════════════════
                      400V CRITICAL POWER DISTRIBUTION
═══════════════════════════════════════════════════════════════════════════════

    BUS A (SWBD-A)                                   BUS B (SWBD-B)
    Normal: 1,039 kW (1,763 A)                      Normal: 1,096 kW (1,861 A)
    Failure: 2,078 kW (3,529 A)                     Failure: 2,078 kW (3,529 A)
         │                                                  │
         ├───────────────────┬──────────────────┬──────────┤
         │                   │                  │          │
    ┌────▼──────┐       ┌────▼────┐       ┌────▼────┐  ┌────▼────┐
    │ Panel     │       │ Panel   │       │ Panel   │  │ Panel   │
    │ A-IT-1    │       │A-COOL-1 │       │ B-IT-1  │  │B-COOL-1 │
    │ 2,500A    │       │ 3,200A  │       │ 2,500A  │  │ 3,200A  │
    │ MCCB      │       │ MCCB    │       │ MCCB    │  │ MCCB    │
    │ Motor Ctr │       │Motor Ctr│       │Motor Ctr│  │Motor Ctr│
    └────┬──────┘       └────┬────┘       └────┬────┘  └────┬────┘
         │                   │                  │            │
         │                   │                  │            │
    IT LOADS              COOLING            IT LOADS     COOLING
    735 kW                304 kW             735 kW       361 kW
    (1,248 A)             (515 A)            (1,248 A)    (613 A)


═══════════════════════════════════════════════════════════════════════════════
                        CABINET POWER DISTRIBUTION (DUAL-CORDED)
═══════════════════════════════════════════════════════════════════════════════

    Each IT Cabinet receives power from BOTH buses via dual-corded PDUs:

         Panel A-IT-1 (BUS A)                Panel B-IT-1 (BUS B)
                │                                    │
                │ Feeder per cabinet                │ Feeder per cabinet
                │                                    │
         ┌──────▼──────┐                      ┌──────▼──────┐
         │   PDU-A     │                      │   PDU-B     │
         │   (Cabinet) │                      │   (Cabinet) │
         │   Input:    │                      │   Input:    │
         │   400V 3Φ   │                      │   400V 3Φ   │
         │   50Hz      │                      │   50Hz      │
         │   Output:   │                      │   Output:   │
         │   230V 1Φ   │                      │   230V 1Φ   │
         │   C19/C13   │                      │   C19/C13   │
         └──────┬──────┘                      └──────┬──────┘
                │                                    │
                └────────────┬───────────────────────┘
                             │
                    ┌────────▼─────────┐
                    │  IT Equipment    │
                    │  (Dual PSU)      │
                    │  Auto-failover:  │
                    │  If PDU-A fails, │
                    │  switch to PDU-B │
                    │  (seamless)      │
                    └──────────────────┘


═══════════════════════════════════════════════════════════════════════════════
                    CRITICAL COOLING LOADS (BACKED BY MTU)
═══════════════════════════════════════════════════════════════════════════════

    From Panel A-COOL-1 (BUS A)         From Panel B-COOL-1 (BUS B)
    Total: 304 kW (515 A)               Total: 361 kW (613 A)

    ┌─ CHW Pump #1 (30 kW)              ┌─ CHW Pump #2 (30 kW)
    ├─ CW Pump #1 (45 kW)               ├─ CW Pump #2 (45 kW)
    ├─ River Pump #1 (30 kW)            ├─ River Pump #2 (30 kW)
    ├─ In-Row Units #1-6 (75 kW)        ├─ In-Row Units #7-12 (75 kW)
    ├─ Chiller #1 (124 kW)              ├─ Chiller #2 (124 kW)
    └─                                   └─ Chiller #3 (57 kW standby)

    Note: Chiller #3 is N+1 standby, normally powered from BUS B
    All pumps and chillers on critical MTU-backed power


═══════════════════════════════════════════════════════════════════════════════
                    OFFICE / NON-CRITICAL LOADS (SEPARATE SWBD)
═══════════════════════════════════════════════════════════════════════════════

                     UTILITY GRID              ON-SITE SOLAR ARRAY
                     11 kV, 250 kVA            700 kW AC @ 400V
                            │                         │
                            │                         │
                     ┌──────▼──────┐           ┌──────▼──────┐
                     │ Transformer │           │ Solar       │
                     │ 250 kVA     │           │ Inverters   │
                     │ 11kV/400V   │           │ 700 kW AC   │
                     └──────┬──────┘           └──────┬──────┘
                            │                         │
                            │                         │
                     ┌──────▼─────────────────────────▼──────┐
                     │        ATS (AUTOMATIC TRANSFER)       │
                     │        Solar Priority Mode             │
                     │        Utility Backup                  │
                     └──────┬────────────────────────────────┘
                            │
                     ┌──────▼──────┐
                     │  SWBD-OFFICE│
                     │  400V, 3Ø   │
                     │  630A Bus   │
                     │  NO UPS     │
                     │  NO MTU     │
                     └──────┬──────┘
                            │
                      Office Loads:
                      - HVAC (31 kW)
                      - Lighting (20 kW)
                      - IT Office (15 kW)
                      - Security/BMS (10 kW)
                      - Misc (27 kW)
                      Total: 103 kW diversified


═══════════════════════════════════════════════════════════════════════════════
                         GROUNDING & PROTECTION
═══════════════════════════════════════════════════════════════════════════════

**System Configuration:** TN-S (Separate neutral and protective earth)

**Main Grounding Points:**
- MV/LV transformer neutrals bonded to earth (XFMR-A, XFMR-B, Office XFMR)
- 400V system: 3-phase + neutral + separate PE (protective earth)
- Equipment grounding: All metallic enclosures bonded to PE
- Grounding electrode: Perimeter ring ground + ground rods at building corners
- Solar array: Bonded to main facility ground system

**Protection:**
- 11 kV: VCBs with overcurrent, short-circuit, ground fault protection
- 400V: ACBs and MCCBs at all distribution levels with electronic trip units
- Ground fault: RCDs (residual current devices) on selected circuits
- Arc flash: Calculated per IEC 61482, labels on all switchgear
- Lightning: SPDs at 11 kV (both sources), 400V (all switchboards), solar DC

**Coordination:**
- Full selective coordination study performed
- Time-current curves ensure upstream/downstream selectivity
- Arc flash labels per IEC 61482-1-2

**Monitoring:**
- Power quality monitoring at SWBD-A, SWBD-B, SWBD-OFFICE
- Energy metering per distribution panel (for PUE tracking)
- Alarm integration with BMS for all breaker trips
- MTM controller monitors both utility sources, controls 52-TIE


═══════════════════════════════════════════════════════════════════════════════
                            EQUIPMENT SCHEDULE
═══════════════════════════════════════════════════════════════════════════════

**PRIMARY SOURCES & TRANSFORMERS**

| Tag | Description | Rating | Qty | Redundancy | Notes |
|-----|-------------|--------|-----|------------|-------|
| HPP | HPP Utility Source | 3.7 MW @ 400V | 1 | Dual source | Low voltage source |
| GRID | Utility Grid Source | 4.0 MW @ 11 kV | 1 | Dual source | MV source |
| XFMR-STEP-UP | HPP Step-Up Transformer | 3,500 kVA, 400V/11kV, Dyn11 | 1 | - | For HPP only |
| VCB-HPP | HPP MV Circuit Breaker | 630A, 40kA @ 11kV | 1 | MV SWBD A | After step-up |
| VCB-GRID | Grid MV Circuit Breaker | 630A, 40kA @ 11kV | 1 | MV SWBD B | Incoming |
| MV-SWBD-A | MV Switchboard A | 630A bus @ 11 kV | 1 | Redundant | Fed from HPP |
| MV-SWBD-B | MV Switchboard B | 630A bus @ 11 kV | 1 | Redundant | Fed from Grid |
| XFMR-A | Step-Down Transformer A | 3,500 kVA, 11kV/400V, Dyn11 | 1 | 2N | MV SWBD A → LV |
| XFMR-B | Step-Down Transformer B | 3,500 kVA, 11kV/400V, Dyn11 | 1 | 2N | MV SWBD B → LV |

**LOW VOLTAGE DISTRIBUTION (MTM)**

| Tag | Description | Rating | Qty | Config | Notes |
|-----|-------------|--------|-----|--------|-------|
| ACB-M1 | Main Breaker 1 | 6,300A frame, 5,000A trip | 1 | Main | 65kA SCCR, drawout |
| ACB-M2 | Main Breaker 2 | 6,300A frame, 5,000A trip | 1 | Main | 65kA SCCR, drawout |
| 52-TIE | Tie Breaker | 6,300A frame, 5,000A trip | 1 | N.O. | Auto-close on fail |
| SWBD-A | Switchboard A (Bus A) | 2,500A bus, 400V | 1 | Main 1 | MTM topology |
| SWBD-B | Switchboard B (Bus B) | 2,500A bus, 400V | 1 | Main 2 | MTM topology |

**BACKUP POWER (2N)**

| Tag | Description | Rating | Qty | Redundancy | Notes |
|-----|-------------|--------|-----|------------|-------|
| MTU-1 | Kinetic PowerPack #1 | 2,200 kW / 2,750 kVA @ 400V | 1 | 2N | Diesel + Flywheel |
| MTU-2 | Kinetic PowerPack #2 | 2,200 kW / 2,750 kVA @ 400V | 1 | 2N | Diesel + Flywheel |
| ACB-MTU1 | MTU-1 Breaker | 5,000A frame, 4,000A trip | 1 | - | w/ ATS function |
| ACB-MTU2 | MTU-2 Breaker | 5,000A frame, 4,000A trip | 1 | - | w/ ATS function |

**CRITICAL DISTRIBUTION PANELS**

| Tag | Description | Rating | Qty | Bus | Load (Normal) |
|-----|-------------|--------|-----|-----|---------------|
| A-IT-1 | IT Distribution Panel A | 2,500A MCCB | 1 | Bus A | 735 kW (1,248 A) |
| B-IT-1 | IT Distribution Panel B | 2,500A MCCB | 1 | Bus B | 735 kW (1,248 A) |
| A-COOL-1 | Cooling Distribution A | 3,200A MCCB | 1 | Bus A | 304 kW (515 A) |
| B-COOL-1 | Cooling Distribution B | 3,200A MCCB | 1 | Bus B | 361 kW (613 A) |

**OFFICE / NON-CRITICAL**

| Tag | Description | Rating | Qty | Source | Notes |
|-----|-------------|--------|-----|--------|-------|
| XFMR-OFFICE | Office Transformer | 250 kVA, 11kV/400V | 1 | Utility Grid | Not critical |
| SOLAR-INV | Solar Inverters | 700 kW AC @ 400V | 1 set | Solar Array | Priority source |
| ATS-OFFICE | Office ATS | 630A | 1 | - | Solar priority |
| SWBD-OFFICE | Office Switchboard | 630A bus, 400V | 1 | Non-critical | No UPS/MTU |


═══════════════════════════════════════════════════════════════════════════════
                          CABLE SCHEDULE (MAJOR FEEDERS)
═══════════════════════════════════════════════════════════════════════════════

**LOW VOLTAGE - HPP INCOMING (400V)**

| From | To | Cable Type | Size (Cu) | Ampacity | Length | Notes |
|------|-----|------------|-----------|----------|--------|-------|
| HPP Source | XFMR-STEP-UP | LV XLPE | 4×500mm² | 5,300A | [TBD] | 400V, 3.7 MW |

**MEDIUM VOLTAGE (11 kV)**

| From | To | Cable Type | Size (Cu) | Isc | Length | Notes |
|------|-----|------------|-----------|-----|--------|-------|
| XFMR-STEP-UP | MV-SWBD-A | MV XLPE | 3×185mm² | 25 kA | [TBD] | 11 kV from step-up |
| MV-SWBD-A | XFMR-A | MV XLPE | 3×185mm² | 25 kA | [TBD] | To step-down A |
| Grid Source | MV-SWBD-B | MV XLPE | 3×185mm² | 25 kA | [TBD] | 11 kV, 4.0 MW |
| MV-SWBD-B | XFMR-B | MV XLPE | 3×185mm² | 25 kA | [TBD] | To step-down B |
| Grid Source | XFMR-OFFICE | MV XLPE | 3×35mm² | 25 kA | [TBD] | Office 250 kVA |

**LOW VOLTAGE - MAIN DISTRIBUTION (400V)**

| From | To | Cable Type | Size (Cu) | Ampacity | Length | Notes |
|------|-----|------------|-----------|----------|--------|-------|
| XFMR-A | ACB-M1 | LV XLPE | 4×400mm² | 5,000A | [TBD] | Parallel runs |
| XFMR-B | ACB-M2 | LV XLPE | 4×400mm² | 5,000A | [TBD] | Parallel runs |
| MTU-1 | ACB-MTU1 | LV XLPE | 4×300mm² | 4,000A | [TBD] | Backup feed A |
| MTU-2 | ACB-MTU2 | LV XLPE | 4×300mm² | 4,000A | [TBD] | Backup feed B |
| ACB-M1 | SWBD-A | Busway | 2,500A | 2,500A | [TBD] | Bus duct |
| ACB-M2 | SWBD-B | Busway | 2,500A | 2,500A | [TBD] | Bus duct |
| SWBD-A | 52-TIE | Busway | 2,500A | 5,000A | [TBD] | Tie connection |
| 52-TIE | SWBD-B | Busway | 2,500A | 5,000A | [TBD] | Tie connection |

**LOW VOLTAGE - DISTRIBUTION PANELS (400V)**

| From | To | Cable Type | Size (Cu) | Ampacity | Length | Notes |
|------|-----|------------|-----------|----------|--------|-------|
| SWBD-A | A-IT-1 | LV XLPE | 4×240mm² | 2,500A | [TBD] | IT loads Bus A |
| SWBD-B | B-IT-1 | LV XLPE | 4×240mm² | 2,500A | [TBD] | IT loads Bus B |
| SWBD-A | A-COOL-1 | LV XLPE | 4×300mm² | 3,200A | [TBD] | Cooling Bus A |
| SWBD-B | B-COOL-1 | LV XLPE | 4×300mm² | 3,200A | [TBD] | Cooling Bus B |

**OFFICE / SOLAR (400V)**

| From | To | Cable Type | Size (Cu) | Ampacity | Length | Notes |
|------|-----|------------|-----------|----------|--------|-------|
| XFMR-OFFICE | ATS-OFFICE | LV XLPE | 4×70mm² | 630A | [TBD] | Utility backup |
| SOLAR-INV | ATS-OFFICE | LV XLPE | 4×185mm² | 1,200A | [TBD] | Solar priority |
| ATS-OFFICE | SWBD-OFFICE | LV XLPE | 4×70mm² | 630A | [TBD] | Office feed |


═══════════════════════════════════════════════════════════════════════════════
                      SEQUENCE OF OPERATIONS - NORMAL MODE (MTM)
═══════════════════════════════════════════════════════════════════════════════

**Normal Operating Configuration:**

1. **Primary Power (Both Utility Sources Active):**
   - **Path A (HPP):**
     * HPP @ 400V (3.7 MW) → XFMR-STEP-UP (400V/11kV) → MV-SWBD-A (11 kV)
     * MV-SWBD-A → XFMR-A (11kV/400V) → ACB-M1 → BUS A (SWBD-A @ 400V)
   - **Path B (Grid):**
     * Grid @ 11 kV (4.0 MW) → MV-SWBD-B (11 kV)
     * MV-SWBD-B → XFMR-B (11kV/400V) → ACB-M2 → BUS B (SWBD-B @ 400V)
   - 52-TIE breaker: **OPEN** (normally open at 400V LV level)
   - Each bus independently powered by separate utility source
   - Load distribution:
     * BUS A: 1,039 kW (IT: 735 kW + Cooling: 304 kW)
     * BUS B: 1,096 kW (IT: 735 kW + Cooling: 361 kW)

2. **Backup Power (Standby Mode):**
   - MTU-1 and MTU-2: Diesel engines OFF, flywheels spinning
   - ACB-MTU1 and ACB-MTU2: OPEN
   - Ready for automatic start on utility failure

3. **Office Loads (Non-Critical):**
   - Solar inverters (700 kW) → ATS-OFFICE → SWBD-OFFICE (priority source)
   - If solar insufficient/unavailable: Utility XFMR-OFFICE → ATS-OFFICE
   - Office loads: 103 kW diversified (HVAC, lighting, IT office, security, misc)

4. **Monitoring & Control:**
   - MTM controller monitors voltage/frequency on both BUS A and BUS B
   - Power quality monitoring (harmonics, power factor, voltage sags)
   - Energy metering per panel for PUE calculation
   - Alarms for any breaker trip, source failure, or abnormal condition


═══════════════════════════════════════════════════════════════════════════════
                 SEQUENCE OF OPERATIONS - SINGLE SOURCE FAILURE (MTM)
═══════════════════════════════════════════════════════════════════════════════

**Scenario A: HPP Source Fails (BUS A loses primary power)**

**T+0 seconds:**
- HPP source voltage drops below 80% nominal
- MTM controller detects loss on BUS A
- Simultaneously:
  * 52-TIE breaker receives CLOSE command
  * MTU-1 receives START signal

**T+0 to T+1 seconds (Tie Breaker Transfer):**
- 52-TIE closes automatically (fast-acting motorized breaker)
- BUS A now fed from BUS B via XFMR-B (Grid source)
- Total load on XFMR-B: 2,078 kW (within 3,500 kVA capacity)
- **NO INTERRUPTION** to IT or cooling loads (seamless transfer)

**T+0 to T+15 seconds (MTU Flywheel Backup):**
- MTU-1 flywheel provides backup if tie breaker transfer fails
- Diesel engine starts (0-10 seconds typical)
- Flywheel sustains BUS A loads for 15-20 seconds

**T+10-15 seconds:**
- MTU-1 diesel synchronized and ready
- Remains on standby (tie already carrying load)
- Provides additional N+1 redundancy

**Configuration during HPP failure:**
- BUS A and BUS B: Both fed from Grid via XFMR-B + 52-TIE
- MTU-1: Running on standby (diesel at idle/low load)
- MTU-2: On standby (diesel off, flywheel spinning)
- Redundancy: Grid + MTU-1 + MTU-2 (triple redundancy)

**HPP Source Restoration:**
- When HPP voltage restored and stable for 5 minutes
- 52-TIE opens automatically
- BUS A transfers back to HPP via XFMR-A
- MTU-1 cooldown (5-10 min), returns to standby

---

**Scenario B: Grid Source Fails (BUS B loses primary power)**

(Sequence identical to Scenario A, but reversed buses)

**T+0 seconds:**
- Grid source voltage drops below 80% nominal
- MTM controller detects loss on BUS B
- 52-TIE closes, MTU-2 starts

**T+0 to T+1 seconds:**
- 52-TIE closes, BUS B fed from BUS A via XFMR-A (HPP source)
- Total load on XFMR-A: 2,078 kW (within 3,500 kVA capacity)
- NO INTERRUPTION to loads

**Configuration during Grid failure:**
- BUS A and BUS B: Both fed from HPP via XFMR-A + 52-TIE
- MTU-2: Running on standby
- MTU-1: On standby
- Redundancy: HPP + MTU-1 + MTU-2 (triple redundancy)


═══════════════════════════════════════════════════════════════════════════════
                  SEQUENCE OF OPERATIONS - DUAL UTILITY FAILURE (MTM)
═══════════════════════════════════════════════════════════════════════════════

**Scenario: Both HPP and Grid sources fail simultaneously**

**T+0 seconds:**
- Both HPP and Grid voltages drop below 80% nominal
- MTM controller detects loss on both BUS A and BUS B
- Simultaneously:
  * ACB-M1 and ACB-M2 open (no utility available)
  * MTU-1 and MTU-2 receive START signals
  * 52-TIE remains OPEN (no utility to transfer)

**T+0 to T+15 seconds (Flywheel Ride-Through):**
- MTU-1 flywheel powers BUS A (1,039 kW normal load)
- MTU-2 flywheel powers BUS B (1,096 kW normal load)
- **NO INTERRUPTION** to IT or cooling loads
- Both diesel engines start (0-10 seconds typical)

**T+10-15 seconds (Diesel Synchronization):**
- Both diesel engines reach rated speed and voltage
- MTU-1 synchronizes with BUS A load
- MTU-2 synchronizes with BUS B load
- Seamless transition from flywheel to diesel generation

**T+15 seconds onward (Full Diesel Operation):**
- MTU-1 powers BUS A: 1,039 kW (47% of 2,200 kW capacity)
- MTU-2 powers BUS B: 1,096 kW (50% of 2,200 kW capacity)
- 52-TIE remains OPEN (load distribution optimized)
- Facility operating entirely on MTU diesel power

**Redundancy during dual utility failure:**
- 2N redundancy maintained: Either MTU can fail, 52-TIE will close
- If MTU-1 fails: 52-TIE closes, MTU-2 carries full facility load (2,078 kW = 94% capacity)
- If MTU-2 fails: 52-TIE closes, MTU-1 carries full facility load (2,078 kW = 94% capacity)
- Margin: Each MTU has 122 kW (6%) reserve at full facility load

**Fuel Consumption:**
- MTU-1 at 47% load: ~165 L/hr (estimated)
- MTU-2 at 50% load: ~175 L/hr (estimated)
- Total: ~340 L/hr for both units
- Fuel storage: [TBD] liters provides [TBD] hours runtime

**Utility Restoration:**
- When either HPP or Grid voltage restored and stable for 5 minutes
- Automatic transfer back to utility via ACB-M1 or ACB-M2
- MTU units cooldown (5-10 minutes)
- Return to normal mode (diesel off, flywheel spinning)


═══════════════════════════════════════════════════════════════════════════════
                      CONCURRENT MAINTAINABILITY (TIER III)
═══════════════════════════════════════════════════════════════════════════════

**Bypass Provisions for Maintenance Without Shutdown:**

1. **HPP Step-Up Transformer Maintenance (XFMR-STEP-UP):**
   - Close 52-TIE at 400V LV level to feed BUS A from Grid via BUS B
   - Isolate HPP source at 400V with disconnect switch
   - Isolate step-up transformer at 11 kV side (MV-SWBD-A VCB)
   - Full facility load carried by Grid source via tie breaker

2. **MV Switchboard Maintenance:**
   - **MV-SWBD-A:** Close 52-TIE, isolate MV-SWBD-A, feed BUS A from Grid
   - **MV-SWBD-B:** Close 52-TIE, isolate MV-SWBD-B, feed BUS B from HPP
   - Redundant MV switchboards allow independent maintenance

3. **Step-Down Transformer Maintenance (XFMR-A or XFMR-B):**
   - During XFMR-A maintenance: Close 52-TIE, open ACB-M1, isolate XFMR-A at MV-SWBD-A
   - During XFMR-B maintenance: Close 52-TIE, open ACB-M2, isolate XFMR-B at MV-SWBD-B
   - Full facility load carried by remaining transformer via tie breaker

4. **Main Breaker Maintenance (ACB-M1, ACB-M2):**
   - Drawout-type breakers (removable without shutdown)
   - Close 52-TIE first to establish parallel bus connection
   - Open and remove breaker for maintenance
   - Full facility load carried by remaining source + tie

5. **Tie Breaker Maintenance (52-TIE):**
   - Drawout-type breaker
   - Ensure both utility sources available and stable
   - Each bus operates independently during tie breaker maintenance
   - No load transfer capability until tie breaker restored

6. **MTU Maintenance:**
   - Each MTU can be maintained independently (2N redundancy)
   - Other MTU provides full backup capacity
   - Maintenance performed during utility-available periods preferred

7. **Distribution Panel Maintenance:**
   - IT loads dual-corded: Maintain one panel while other carries load
   - Cooling loads: N+1 redundancy allows single equipment maintenance


═══════════════════════════════════════════════════════════════════════════════
                               DESIGN NOTES
═══════════════════════════════════════════════════════════════════════════════

1. **Electrical Standards:** All equipment complies with IEC standards (Georgia follows IEC)
2. **Cable Sizing:** All cable sizes are Cu (copper) unless specified; sized per IEC 60364
3. **Protection:** All circuit breakers include overcurrent, short-circuit, and ground fault protection
4. **Surge Protection:** SPDs installed at 11 kV (both sources), 400V (all SWBDs), and solar DC
5. **Metering:** Energy metering at each distribution panel for DCIM/PUE monitoring
6. **Monitoring:** Remote monitoring of all switchgear via BMS (BACnet/Modbus protocol)
7. **Arc Flash:** Study to be performed during detailed design; labels per IEC 61482-1-2
8. **Environmental:** Electrical room temperature: 20-25°C maintained by building HVAC
9. **MTM Controller:** Simple relay-based logic (not PLC) for cost/reliability optimization
10. **Load Calculations:** Include 25% future growth margin at panel level
11. **Voltage Drop:** Maximum 3% from switchboard to load per IEC 60364-5-52
12. **Cable Installation:** Underground duct banks or overhead cable tray per site conditions
13. **Transformer Cooling:** ONAN (Oil Natural Air Natural) for reliability and low maintenance
14. **Breaker Coordination:** Full selective coordination study with time-current curves
15. **Solar Integration:** Office loads only (non-critical); no grid export (consumption only)

---

**Prepared by:** EVS / GGE Engineering Team
**Date:** November 4, 2025
**Revision:** 02 - MTM Configuration with Dual Utility Sources
**Status:** For Construction
