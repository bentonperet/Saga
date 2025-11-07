# GGE DATA CENTER - COOLING SYSTEMS P&ID
## Three-Loop Water Cooling System with Kura River Economization

**Document:** P&ID-M-001
**Date:** 2025-11-04
**Revision:** 01

---

## SYSTEM OVERVIEW

Three independent water loops:
1. **CHW (Chilled Water)** - Loop 1: Data hall cooling (closed loop)
2. **CW (Condenser Water)** - Loop 2: Chiller heat rejection (closed loop)
3. **RW (River Water)** - Loop 3: River cooling (open loop)

---

## P&ID - CHILLED WATER (CHW) LOOP 1

```
═══════════════════════════════════════════════════════════════════════════════
                    DATA HALL CHILLED WATER DISTRIBUTION
═══════════════════════════════════════════════════════════════════════════════

        DATA CENTER MECHANICAL ROOM                    DATA HALL

  ┌──────────────────────────────────┐
  │  CHILLER #1 (800 kW)             │
  │  Evaporator: 12°C → 18°C         │
  │  Flow: 1,227 L/min               │
  ├──────────────────────────────────┤
  │  CHILLER #2 (800 kW)             │
  │  Evaporator: 12°C → 18°C         │
  │  Flow: 1,227 L/min               │
  ├──────────────────────────────────┤
  │  CHILLER #3 (800 kW) STANDBY     │
  │  Evaporator: 12°C → 18°C         │
  │  Flow: 1,227 L/min               │
  └───┬──────────────────────────┬───┘
      │                          │
      │  CHW Supply Header       │  CHW Return Header
      │  12°C                    │  18°C
      │  3,680 L/min             │  3,680 L/min
      │                          │
  ┌───▼──────────────────────────▼───┐
  │  BUFFER TANK (Optional)          │
  │  Volume: 5-10 m³                 │
  │  Purpose: Thermal inertia        │
  └───┬──────────────────────────┬───┘
      │                          │
  ┌───▼────┐  ┌────────┐  ┌──────▼──┐
  │ P-CHW1 │  │ P-CHW2 │  │ P-CHW3  │
  │ 30 kW  │  │ 30 kW  │  │ 30 kW   │ (STANDBY)
  │ VFD    │  │ VFD    │  │ VFD     │
  └───┬────┘  └────┬───┘  └───┬─────┘
      │            │           │
      └────────────┼───────────┘
                   │
  ┌────────────────▼────────────────┐
  │  CHW SUPPLY HEADER               │
  │  12°C, 3,680 L/min              │
  │  DN200 (8") Insulated Steel     │
  └────────────┬────────────────────┘
               │
               ├─────────────────────┐
               │                     │
       ┌───────▼─────┐       ┌───────▼─────┐
       │ SUPPLY      │       │ SUPPLY      │
       │ MANIFOLD 1  │       │ MANIFOLD 2  │
       │ (Units 1-6) │       │ (Units 7-12)│
       └───────┬─────┘       └───────┬─────┘
               │                     │
    ┌──────────┼──────────┐   ┌──────┼──────────┐
    │   │   │  │  │   │   │   │   │  │  │   │   │
  ┌─▼─┐ │ ┌─▼─┐│ ┌─▼─┐   │ ┌─▼─┐  │ ┌─▼─┐   │ ┌─▼─┐
  │IRU││ │IRU││ │IRU│   │ │IRU│  │ │IRU│   │ │IRU│
  │ 1 ││ │ 3 ││ │ 5 │   │ │ 7 │  │ │ 9 │   │ │11 │
  └─┬─┘│ └─┬─┘│ └─┬─┘   │ └─┬─┘  │ └─┬─┘   │ └─┬─┘
    │ ┌▼─┐ │┌─▼┐ │ ┌──▼┐│  │ ┌─▼┐│  │┌──▼┐│  │ ┌─▼┐
    │ │2 │ ││ 4│ │ │ 6 ││  │ │ 8││  ││10 ││  │ │12│
    │ └┬─┘ │└─┬┘ │ └──┬┘│  │ └─┬┘│  │└──┬┘│  │ └─┬┘
    │  │   │  │  │    │ │  │   │ │  │   │ │  │   │
    └──┼───┴──┼──┴────┼─┘  └───┼─┴──┴───┼─┘  └───┼──┘
       │      │       │        │        │        │
  ┌────▼──────▼───────▼────────▼────────▼────────▼───┐
  │  CHW RETURN HEADER                                │
  │  18°C, 3,680 L/min                               │
  │  DN200 (8") Insulated Steel                      │
  └────────────┬──────────────────────────────────────┘
               │
               │  Back to Chillers
               │
  ┌────────────▼──────────────────┐
  │  EXPANSION TANK                │
  │  50 L, pressurized             │
  └────────────────────────────────┘

IRU = In-Row Cooling Unit (150 kW each)


═══════════════════════════════════════════════════════════════════════════════
        CHW LOOP INSTRUMENTATION & CONTROLS
═══════════════════════════════════════════════════════════════════════════════

**Temperature Sensors:**
- TE-CHW-001: Supply header temp (12°C setpoint)
- TE-CHW-002: Return header temp (18°C typical)
- TE-CHW-101 to 112: Each IRU return temp

**Pressure Sensors:**
- PT-CHW-001: Supply header pressure (maintain 3-4 bar)
- PT-CHW-002: Return header pressure
- PD-CHW-001: Differential pressure (ΔP control for VFD pumps)

**Flow Meters:**
- FT-CHW-001: Total CHW flow (3,680 L/min nominal)
- FT-CHW-101 to 112: Individual IRU flow meters (optional)

**Control Valves:**
- MOV-CHW-001 to 003: Chiller isolation valves (motorized)
- MOV-CHW-P1 to P3: Pump isolation valves (motorized)

**Control Strategy:**
- Variable flow: VFD pumps modulate to maintain ΔP
- Chiller staging: Lead/lag based on return temp + runtime equalization
- Low load: Single chiller operation (<800 kW load)
- High load: Dual chiller operation (>800 kW load)


═══════════════════════════════════════════════════════════════════════════════
```

---

## P&ID - CONDENSER WATER (CW) LOOP 2 + RIVER WATER (RW) LOOP 3

```
═══════════════════════════════════════════════════════════════════════════════
     DATA CENTER MECH ROOM              RIVER-EDGE ENCLOSURE (100m away)
═══════════════════════════════════════════════════════════════════════════════

   CHILLERS (Condensers)
        │
        │  CW Return (Hot)
        │  30-40°C
        │  4,950 L/min
        │
  ┌─────▼─────────────────┐
  │ 3 × CHILLERS          │
  │ Condensers            │
  │ (Water-cooled)        │
  │                       │
  │ CH-1: 1,650 L/min     │
  │ CH-2: 1,650 L/min     │
  │ CH-3: 1,650 L/min (s) │
  └─────┬─────────────────┘
        │
        │  CW Supply (Cool)
        │  20-30°C
        │  4,950 L/min
        │
  ┌─────▼─────────────────┐
  │ CW SUPPLY HEADER      │
  │ 20-30°C, 4,950 L/min  │
  └─────┬─────────────────┘
        │
  ┌─────▼────┐  ┌──────┐  ┌────────┐
  │ P-CW1    │  │P-CW2 │  │ P-CW3  │
  │ 45 kW    │  │45 kW │  │ 45 kW  │ (STANDBY)
  │ VFD      │  │VFD   │  │ VFD    │
  └─────┬────┘  └───┬──┘  └────┬───┘
        │           │          │
        └───────────┼──────────┘
                    │
  ┌─────────────────▼──────────────────┐
  │ CW SUPPLY PIPING                   │
  │ DN200 (8") HDPE, Insulated         │
  │ Buried 1.5m depth                  │
  │ 100m length to River Enclosure     │
  └─────────────────┬──────────────────┘
                    │
                    │ 100 meters underground
                    │
       ┌────────────▼───────────────────────────────────────┐
       │     RIVER-EDGE ENCLOSURE (8m × 5m × 3m)           │
       │                                                    │
       │   ┌────────────────────────────────────┐          │
       │   │  3-WAY BYPASS VALVE A              │          │
       │   │  MOV-CW-BYP-A (DN200)              │          │
       │   │  (Motorized, fail-to-bypass)       │          │
       │   └──────┬──────────────────┬──────────┘          │
       │          │                  │                     │
       │          │ To HX            │ BYPASS LINE        │
       │          │                  │                     │
       │   ┌──────▼──────┐    ┌──────▼──────┐             │
       │   │ PLATE HX #1 │    │ PLATE HX #2 │             │
       │   │ 1,000 kW    │    │ 1,000 kW    │             │
       │   │             │    │             │             │
       │   │ PRIMARY:    │    │ PRIMARY:    │             │
       │   │ CW Loop     │    │ CW Loop     │             │
       │   │ (Closed)    │    │ (Closed)    │             │
       │   │             │    │             │             │
       │   │ SECONDARY:  │    │ SECONDARY:  │             │
       │   │ River Water │    │ River Water │             │
       │   │ (Open)      │    │ (Open)      │             │
       │   └──────┬──────┘    └──────┬──────┘             │
       │          │                  │                     │
       │          │ From HX          │ BYPASS LINE        │
       │   ┌──────▼──────────────────▼──────────┐         │
       │   │  3-WAY BYPASS VALVE B              │         │
       │   │  MOV-CW-BYP-B (DN200)              │         │
       │   │  (Motorized, fail-to-bypass)       │         │
       │   └──────┬─────────────────────────────┘         │
       │          │                                        │
       └──────────┼────────────────────────────────────────┘
                  │
  ┌───────────────▼──────────────────┐
  │ CW RETURN PIPING                 │
  │ DN200 (8") HDPE, Insulated       │
  │ Buried 1.5m depth                │
  │ 100m length back to DC           │
  └───────────────┬──────────────────┘
                  │
                  │ 100 meters underground
                  │
  ┌───────────────▼──────────────────┐
  │ CW RETURN HEADER                 │
  │ 30-40°C, 4,950 L/min             │
  │                                  │
  │ (Back to Chiller Condensers)     │
  └──────────────────────────────────┘


═══════════════════════════════════════════════════════════════════════════════
                 RIVER WATER LOOP 3 (Inside River Enclosure)
═══════════════════════════════════════════════════════════════════════════════

                     KURA RIVER
                        │
                        │ Intake @ -2m depth
                        │
                  ┌─────▼──────┐
                  │ COARSE     │
                  │ SCREEN     │
                  │ 50mm bars  │
                  └─────┬──────┘
                        │
                  ┌─────▼──────┐
                  │ INTAKE     │
                  │ PIPING     │
                  │ DN200 HDPE │
                  │ 20m length │
                  └─────┬──────┘
                        │
       ┌────────────────▼─────────────────────────────────┐
       │     RIVER-EDGE ENCLOSURE                         │
       │                                                   │
       │   ┌──────────────────────────────────┐           │
       │   │  FINE SCREEN                     │           │
       │   │  Traveling screen, 5-10mm        │           │
       │   │  Automatic backwash              │           │
       │   └────────┬─────────────────────────┘           │
       │            │                                      │
       │   ┌────────▼─────────────────────────┐           │
       │   │  AUTOMATIC STRAINER #1           │           │
       │   │  100-200 micron                  │           │
       │   │  Self-cleaning backflush         │           │
       │   └────────┬─────────────────────────┘           │
       │            │                                      │
       │   ┌────────▼─────────────────────────┐           │
       │   │  AUTOMATIC STRAINER #2           │           │
       │   │  100-200 micron (Parallel)       │           │
       │   │  Self-cleaning backflush         │           │
       │   └────────┬─────────────────────────┘           │
       │            │                                      │
       │   ┌────────▼──────────────────────┐              │
       │   │  RIVER WATER SUPPLY HEADER    │              │
       │   │  6-27°C (seasonal)            │              │
       │   │  5,500 L/min                  │              │
       │   └────────┬──────────────────────┘              │
       │            │                                      │
       │   ┌────────▼──────┐  ┌────────────┐  ┌────────┐ │
       │   │ P-RW1         │  │ P-RW2      │  │ P-RW3  │ │
       │   │ 30 kW         │  │ 30 kW      │  │ 30 kW  │ │
       │   │ VFD           │  │ VFD        │  │ VFD(s) │ │
       │   │ Vert. Turbine │  │ Vert. Turb │  │        │ │
       │   └────────┬──────┘  └─────┬──────┘  └────┬───┘ │
       │            │                │              │     │
       │            └────────────────┼──────────────┘     │
       │                             │                    │
       │                   ┌─────────▼──────────┐         │
       │                   │  To Plate HX #1/#2 │         │
       │                   │  (Secondary Side)  │         │
       │                   └─────────┬──────────┘         │
       │                             │                    │
       │                   ┌─────────▼──────────┐         │
       │                   │  From Plate HX     │         │
       │                   │  (Heated Water)    │         │
       │                   │  16-37°C           │         │
       │                   └─────────┬──────────┘         │
       │                             │                    │
       │   ┌─────────────────────────▼──────────┐         │
       │   │  RIVER WATER RETURN HEADER         │         │
       │   │  16-37°C (River + 10°C)            │         │
       │   │  5,500 L/min                       │         │
       │   └─────────────────────────┬──────────┘         │
       │                             │                    │
       └─────────────────────────────┼────────────────────┘
                                     │
                              ┌──────▼──────┐
                              │ DISCHARGE   │
                              │ PIPING      │
                              │ DN200 HDPE  │
                              │ 20m length  │
                              └──────┬──────┘
                                     │
                              ┌──────▼──────┐
                              │ DIFFUSER    │
                              │ @ -1m depth │
                              └──────┬──────┘
                                     │
                                KURA RIVER


═══════════════════════════════════════════════════════════════════════════════
          CONDENSER WATER INSTRUMENTATION & CONTROLS
═══════════════════════════════════════════════════════════════════════════════

**Temperature Sensors:**
- TE-CW-001: Supply header (20-30°C from HX)
- TE-CW-002: Return header (30-40°C to HX)
- TE-CW-HX1-IN/OUT: Plate HX #1 primary side temps
- TE-CW-HX2-IN/OUT: Plate HX #2 primary side temps

**Pressure Sensors:**
- PT-CW-001: Supply header pressure
- PT-CW-002: Return header pressure
- PD-CW-HX1: Differential pressure across HX #1
- PD-CW-HX2: Differential pressure across HX #2

**Flow Meters:**
- FT-CW-001: Total CW flow (4,950 L/min)
- FT-CW-HX1: Flow through HX #1
- FT-CW-HX2: Flow through HX #2

**Control Valves:**
- MOV-CW-BYP-A: 3-way bypass valve A (supply side)
- MOV-CW-BYP-B: 3-way bypass valve B (return side)
- MOV-CW-HX1-ISO: HX #1 isolation (4 valves: in/out on both sides)
- MOV-CW-HX2-ISO: HX #2 isolation (4 valves: in/out on both sides)


═══════════════════════════════════════════════════════════════════════════════
          RIVER WATER INSTRUMENTATION & CONTROLS
═══════════════════════════════════════════════════════════════════════════════

**Temperature Sensors:**
- TE-RW-001: River intake temp (6-27°C seasonal)
- TE-RW-002: Post-filtration temp
- TE-RW-HX1-IN/OUT: Plate HX #1 secondary side temps
- TE-RW-HX2-IN/OUT: Plate HX #2 secondary side temps
- TE-RW-003: Discharge temp (intake + 10°C)

**Pressure Sensors:**
- PT-RW-001: Pump suction pressure
- PT-RW-002: Pump discharge pressure
- PD-RW-FILT1: Strainer #1 differential pressure (backflush trigger)
- PD-RW-FILT2: Strainer #2 differential pressure (backflush trigger)

**Flow Meters:**
- FT-RW-001: Total river water flow (5,500 L/min)
- FT-RW-INTAKE: Intake flow verification
- FT-RW-DISCHARGE: Discharge flow verification

**Water Quality:**
- AE-RW-001: Conductivity (water quality monitoring)
- AE-RW-002: pH (7-8 typical for Kura River)
- AE-RW-003: Turbidity (filtration performance)

**Control Valves:**
- None (pumps provide flow control via VFD)


═══════════════════════════════════════════════════════════════════════════════
          BYPASS & FREE COOLING CONTROL LOGIC
═══════════════════════════════════════════════════════════════════════════════

**Mode 1: 100% Free Cooling (River < 10°C)**
- River temp: 6-10°C
- CW bypass valves: 100% to HX
- River water pumps: ON at full flow
- CW pumps: ON at reduced flow (variable)
- Chillers: OFF (compressors not running)
- Result: River water cools CW to 9-13°C → Can produce 12°C CHW

**Mode 2: Partial Free Cooling (River 10-23°C)**
- River temp: 10-23°C
- CW bypass valves: Modulating (mix HX + bypass)
- River water pumps: ON at variable flow
- CW pumps: ON at full flow
- Chillers: ON at reduced load (30-70%)
- Result: River pre-cools CW, chillers finish cooling

**Mode 3: Full Mechanical (River > 23°C)**
- River temp: 23-27°C
- CW bypass valves: 100% to HX
- River water pumps: ON at full flow
- CW pumps: ON at full flow
- Chillers: ON at full load
- Result: River water cools condenser, chillers at full capacity

**Mode 4: Bypass / Maintenance (HX Offline)**
- CW bypass valves: 100% bypass (skip HX)
- River water pumps: OFF
- CW pumps: ON at full flow
- Chillers: ON at full load (reduced efficiency)
- HX: Isolated for cleaning/maintenance
- Result: Air-cooled mode (less efficient, emergency only)


═══════════════════════════════════════════════════════════════════════════════
          PIPING SPECIFICATIONS
═══════════════════════════════════════════════════════════════════════════════

**CHW Loop (Data Center):**
- Material: Carbon steel, Sch 40 or HDPE SDR 11
- Size: DN200 (8") supply + return headers
- Insulation: 50mm closed-cell elastomeric foam
- Vapor barrier: Aluminum foil jacket
- Fittings: Welded or flanged (steel), butt-fusion (HDPE)
- Supports: Trapeze hangers @ 3m spacing, insulation shields
- Expansion: Expansion loops or flexible connectors at equipment
- Slope: 1:200 minimum for air venting/drainage

**CW Loop (DC to River Enclosure):**
- Material: HDPE SDR 11 (buried)
- Size: DN200 (8") supply + return (100m each = 200m total)
- Insulation: 50mm polyurethane foam (underground)
- Depth: 1.5m below grade (frost protection + protection from damage)
- Bedding: Sand bedding 150mm under/over pipe
- Marker tape: Detectable warning tape 300mm above pipe
- Entry/exit: Building penetration with watertight seal

**RW Loop (River to Enclosure):**
- Material: HDPE SDR 11
- Size: DN200 (8") intake + discharge (20m each = 40m total)
- Insulation: None (open loop, non-critical temp loss)
- Depth: 1.5m below grade or riverbed
- Intake: Submerged @ -2m below low water level
- Discharge: Submerged @ -1m below low water level with diffuser


═══════════════════════════════════════════════════════════════════════════════
          EQUIPMENT SCHEDULE - COOLING SYSTEMS
═══════════════════════════════════════════════════════════════════════════════

| Tag | Description | Capacity | Qty | Redundancy | Power |
|-----|-------------|----------|-----|------------|-------|
| CH-1 | Chiller #1 | 800 kW | 1 | N+1 | 134 kW |
| CH-2 | Chiller #2 | 800 kW | 1 | N+1 | 134 kW |
| CH-3 | Chiller #3 (Standby) | 800 kW | 1 | N+1 | 134 kW |
| P-CHW1 | CHW Pump #1 | 1,840 L/min | 1 | N+1 | 30 kW |
| P-CHW2 | CHW Pump #2 | 1,840 L/min | 1 | N+1 | 30 kW |
| P-CHW3 | CHW Pump #3 (Standby) | 1,840 L/min | 1 | N+1 | 30 kW |
| P-CW1 | CW Pump #1 | 2,475 L/min | 1 | N+1 | 45 kW |
| P-CW2 | CW Pump #2 | 2,475 L/min | 1 | N+1 | 45 kW |
| P-CW3 | CW Pump #3 (Standby) | 2,475 L/min | 1 | N+1 | 45 kW |
| HX-1 | Plate Heat Exchanger #1 | 1,000 kW | 1 | N+1 | 0 |
| HX-2 | Plate Heat Exchanger #2 | 1,000 kW | 1 | N+1 | 0 |
| P-RW1 | River Water Pump #1 | 2,750 L/min | 1 | N+1 | 30 kW |
| P-RW2 | River Water Pump #2 | 2,750 L/min | 1 | N+1 | 30 kW |
| P-RW3 | River Water Pump #3 (Stby) | 2,750 L/min | 1 | N+1 | 30 kW |
| IRU-1 to 12 | In-Row Cooling Units | 150 kW each | 12 | N+1 | 4 kW each |


═══════════════════════════════════════════════════════════════════════════════
                              NOTES
═══════════════════════════════════════════════════════════════════════════════

1. All pumps are on critical power (400V from MTU Kinetic PowerPack)
2. All piping to be hydrostatically tested to 1.5× design pressure
3. Chilled water treatment: Corrosion inhibitor + biocide (closed loop)
4. Condenser water treatment: Corrosion inhibitor + biocide (closed loop)
5. River water: Filtration only, minimal chemical treatment
6. All automatic valves fail to safe position (bypass for CW, closed for isolation)
7. BMS integration via BACnet/Modbus for all control points
8. Vibration isolation on all pumps and chillers
9. Seismic restraints per IBC 2021 (Georgia seismic zone)
10. Freeze protection: Glycol not required (indoor CHW loop, CW drained if offline)

---

**Prepared by:** EVS / GGE Engineering Team
**Date:** November 4, 2025
**Revision:** 01
**Status:** For Construction
```
