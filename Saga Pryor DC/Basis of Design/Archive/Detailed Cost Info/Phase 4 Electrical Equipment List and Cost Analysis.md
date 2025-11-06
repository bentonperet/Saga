# PHASE 4 ELECTRICAL EQUIPMENT LIST AND COST ANALYSIS v2.1
**Saga Pryor Data Center - PACHYDERM GLOBAL**

**Created:** 2025-11-03
**Updated:** 2025-11-06
**Version:** 2.0
**Project Phase:** Phase 4 - Full Build-Out (22 MW IT Load)
**Total Facility Load:** 29.7 MW
**Related:** [[7BOD - Electrical (CSI Div 26)]]

---

## EXECUTIVE SUMMARY

This document provides a comprehensive equipment list and cost analysis for the Phase 4 electrical infrastructure of the Saga Pryor Data Center. The facility is designed for 22 MW IT load with a total facility load of approximately 29.7 MW, meeting Tier III standards with N+1 redundancy and dual-path distribution.

**Key Cost Metrics:**
- **Total Electrical Infrastructure Cost:** $75,472,183
- **Cost per MW (IT Load):** $3.43M per MW
- **Cost per MW (Facility Load):** $2.54M per MW
- **Cost per Rack (394 racks):** $191,553 per rack

---

## 1.0 UTILITY SUBSTATION (161 kV)

### 1.1 Primary Substation Transformers

| Item                        | Specification                              | Qty | Unit Cost | Extended Cost | +/- % | Certainty | Notes                                                                                             |
| --------------------------- | ------------------------------------------ | --- | --------- | ------------- | ----- | --------- | ------------------------------------------------------------------------------------------------- |
| **Substation Transformers** | 35 MVA, 161kV/13.8kV, ONAN, N+1 redundancy | 2   | $575,000  | $1,150,000    | ±15%  | 75%       | Large HV transformers; pricing varies by manufacturer (ABB, Siemens, GE). Lead time: 40-52 weeks. |

### 1.2 161 kV Switchgear & Protection

| Item                             | Specification                         | Qty | Unit Cost | Extended Cost | +/- % | Certainty | Notes                                    |
| -------------------------------- | ------------------------------------- | --- | --------- | ------------- | ----- | --------- | ---------------------------------------- |
| **161 kV Disconnect Switches**   | Outdoor rated, motor operated         | 4   | $55,000   | $220,000      | ±20%  | 70%       | Per utility interconnection requirements |
| **161 kV Circuit Breakers**      | SF6 or vacuum, 2000A, 40kA            | 2   | $175,000  | $350,000      | ±15%  | 70%       | Main and tie breakers                    |
| **Protection Relays & Controls** | Distance, differential, overcurrent   | 1   | $100,000  | $100,000      | ±25%  | 65%       | SEL or equivalent                        |
| **Revenue Metering System**      | Utility-grade, 161kV CT/PT            | 1   | $65,000   | $65,000       | ±25%  | 75%       | Per utility requirements                 |
| **Substation Control Building**  | Prefab, climate controlled, 12'×20'   | 1   | $100,000  | $100,000      | ±20%  | 80%       | Houses relays, SCADA, controls           |
| **Substation Grounding System**  | Ground grid, driven rods, connections | 1   | $62,500   | $62,500       | ±20%  | 75%       | Per IEEE 142                             |

**Subtotal - Utility Substation:** $2,047,500

---

## 2.0 MEDIUM VOLTAGE (13.8 kV) DISTRIBUTION

### 2.1 Ring Main Units (RMUs)

| Item                       | Specification                           | Qty | Unit Cost | Extended Cost | +/- % | Certainty | Notes                                                                                                       |
| -------------------------- | --------------------------------------- | --- | --------- | ------------- | ----- | --------- | ----------------------------------------------------------------------------------------------------------- |
| **Ring Main Units (RMUs)** | 13.8 kV, 630A, 20kA SCCR, SF6 or vacuum | 8   | $105,000  | $840,000      | ±20%  | 70%       | Schneider Ringmaster or ABB SafeRing. 4 per ring (A/B). Includes integrated protection and motor operators. |

### 2.2 SCADA & Control System

| Item                        | Specification                         | Qty | Unit Cost | Extended Cost | +/- % | Certainty | Notes                                  |
| --------------------------- | ------------------------------------- | --- | --------- | ------------- | ----- | --------- | -------------------------------------- |
| **SCADA Master Station**    | Redundant servers, HMI, historian     | 1   | $200,000  | $200,000      | ±25%  | 65%       | Schneider EcoStruxure or Siemens WinCC |
| **RTUs for RMUs**           | Remote terminal units, communications | 8   | $10,000   | $80,000       | ±20%  | 70%       | One per RMU                            |
| **Fiber Optic Network**     | Self-healing ring, switches, modems   | 1   | $75,000   | $75,000       | ±30%  | 75%       | TC Communications or equivalent        |
| **SCADA Software Licenses** | Engineering, runtime, redundancy      | 1   | $100,000  | $100,000      | ±25%  | 80%       | Permanent licenses                     |

### 2.3 MV Cables & Terminations

| Item | Specification | Qty | Unit Cost | Extended Cost | +/- % | Certainty | Notes |
|------|--------------|-----|-----------|---------------|-------|-----------|-------|
| **15kV MV Cable (Dual-Ring)** | 15kV, 500 kcmil Cu, EPR, shielded | 12,000 LF | $42.50 /LF | $510,000 | ±18% | 75% | Ring A & B interconnections, generator/solar feeds. Installed in duct banks. |
| **MV Cable Terminations** | 15kV, 630A, indoor/outdoor rated | 80 | $1,500 | $120,000 | ±20% | 80% | RMU and transformer connections |
| **MV Duct Banks** | PVC conduit, concrete encased | 3,000 LF | $150 /LF | $450,000 | ±17% | 70% | Substation to E-Houses, gen yard, transformer yard |

**Subtotal - MV Distribution:** $2,375,000

---

## 3.0 GENERATOR SYSTEM

### 3.1 Diesel Generators

| Item | Specification | Qty | Unit Cost | Extended Cost | +/- % | Certainty | Notes |
|------|--------------|-----|-----------|---------------|-------|-----------|-------|
| **4 MW Diesel Generators** | 4,000 kW continuous, 13.8 kV, EPA Tier 4 Final, sound-attenuated enclosure | 9 | $1,900,000 | $17,100,000 | ±16% | 75% | Caterpillar, Cummins, or MTU. Includes MV switchgear, outdoor enclosure, cooling system. N+1 for 29.7 MW facility load. |

### 3.2 Fuel System

| Item                               | Specification                               | Qty | Unit Cost | Extended Cost | +/- % | Certainty | Notes                                                |
| ---------------------------------- | ------------------------------------------- | --- | --------- | ------------- | ----- | --------- | ---------------------------------------------------- |
| **Main Fuel Storage Tanks**        | 40,000 gal above-ground, double-wall        | 3   | $175,000  | $525,000      | ±15%  | 75%       | 12-hour runtime per Uptime Institute. UL-142 listed. |
| **Day Tanks (per generator)**      | 1,000 gal, integral to generator skid       | 9   | Included  | Included      | N/A   | 90%       | Included in generator cost                           |
| **Fuel Transfer Pumps & Controls** | Redundant pumps, filtration, leak detection | 1   | $100,000  | $100,000      | ±25%  | 75%       | ISP Fuel Systems or Curtis Power                     |
| **Fuel Piping & Distribution**     | Double-wall piping, valves, monitoring      | 1   | $150,000  | $150,000      | ±17%  | 70%       | Generator yard distribution                          |
| **Fuel Monitoring System**         | Tank level, leak detection, alarms          | 1   | $32,500   | $32,500       | ±23%  | 80%       | BMS integration                                      |

### 3.3 Generator Yard Infrastructure

| Item                              | Specification                               | Qty | Unit Cost | Extended Cost | +/- % | Certainty | Notes                                     |
| --------------------------------- | ------------------------------------------- | --- | --------- | ------------- | ----- | --------- | ----------------------------------------- |
| **Generator Concrete Pads**       | Reinforced concrete, vibration isolation    | 9   | $20,000   | $180,000      | ±25%  | 80%       | n/a                                       |
| **Generator Exhaust Systems**     | Exhaust silencers, piping, SCR (if req'd)   | 9   | $60,000   | $540,000      | ±25%  | 70%       | n/a                                       |
| **Generator Switchgear (13.8kV)** | 13.8kV breakers, sync controls, paralleling | 1   | $425,000  | $425,000      | ±20%  | 70%       | Central paralleling gear for 9 generators |

**Subtotal - Generator System:** $19,052,500

---

## 4.0 LOW VOLTAGE TRANSFORMERS (13.8 kV / 480V)

### 4.1 Distribution Transformers

| Item                        | Specification                                          | Qty | Unit Cost | Extended Cost | +/- % | Certainty | Notes                                                |
| --------------------------- | ------------------------------------------------------ | --- | --------- | ------------- | ----- | --------- | ---------------------------------------------------- |
| **3.5 MVA LV Transformers** | 3,500 kVA, 13.8kV/480Y/277V, ONAN, outdoor pad-mounted | 11  | $262,500  | $2,887,500    | ±15%  | 75%       |  N+1 for 29.7 MW facility. 6 on Ring A, 5 on Ring B. |

### 4.2 Transformer Yard Infrastructure

| Item | Specification | Qty | Unit Cost | Extended Cost | +/- % | Certainty | Notes |
|------|--------------|-----|-----------|---------------|-------|-----------|-------|
| **Transformer Concrete Pads** | Reinforced concrete with oil containment | 11 | $15,000 | $165,000 | ±20% | 80% | 110% oil containment per EPA SPCC |
| **Oil Containment & Separators** | Gravel fill, oil-water separator systems | 1 | $62,500 | $62,500 | ±20% | 75% | Environmental compliance |
| **Fire Protection Equipment** | Portable extinguishers, signage | 1 | $10,000 | $10,000 | ±20% | 85% | Class C electrical |

**Subtotal - LV Transformers:** $3,125,000

---

## 5.0 IT UPS SYSTEM

### 5.1 UPS Modules & Batteries

| Item | Specification | Qty | Unit Cost | Extended Cost | +/- % | Certainty | Notes |
|------|--------------|-----|-----------|---------------|-------|-----------|-------|
| **IT UPS Modules** | 1,250 kVA (1,000 kW), 480V, modular, online double-conversion | 23 | $212,500 | $4,887,500 | ±18% | 70% | Schneider Galaxy VX, Eaton 9395, or Vertiv PowerUPS 9000. N+1 for 22 MW IT load (22+1). Installed in E-Houses A & B. |
| **Lithium-Ion Battery Cabinets** | 5-minute runtime @ 1,250 kVA, external cabinets | 23 | $100,000 | $2,300,000 | ±25% | 65% | Li-Ion preferred over VRLA: 10-15 year life, higher density, lower maintenance. One cabinet set per UPS module. Installed in E-Houses. |

### 5.2 UPS Support Systems

| Item                            | Specification                             | Qty | Unit Cost | Extended Cost | +/- % | Certainty | Notes               |
| ------------------------------- | ----------------------------------------- | --- | --------- | ------------- | ----- | --------- | ------------------- |
| **UPS Monitoring & Management** | Centralized monitoring, software licenses | 1   | $75,000   | $75,000       | ±30%  | 75%       | Integrated with BMS |

**Subtotal - IT UPS System:** $7,262,500

---

## 6.0 MECHANICAL UPS SYSTEM

### 6.1 Mechanical UPS Modules

| Item | Specification | Qty | Unit Cost | Extended Cost | +/- % | Certainty | Notes |
|------|--------------|-----|-----------|---------------|-------|-----------|-------|
| **Mechanical UPS Modules** | 250 kW, 480V, modular static UPS | 22 | $100,000 | $2,200,000 | ±25% | 70% | N+1 for 4,900 kW mechanical load (21+1). Protects chillers, pumps, CDUs, building HVAC during generator startup. Installed in E-Houses A & B. |

**Subtotal - Mechanical UPS:** $2,200,000

---

## 7.0 PREFABRICATED E-HOUSES (ENCLOSURES & SUPPORT SYSTEMS)

**IMPORTANT NOTE:** E-House costs in this section represent the physical building enclosures and support systems ONLY. All electrical equipment (RMUs, switchboards, distribution panels, UPS modules, batteries) is counted separately in their respective equipment sections above. This eliminates double counting from v1.

### 7.1 E-House Structures (Enclosures Only)

| Item                    | Specification                                                   | Qty | Unit Cost  | Extended Cost | +/- % | Certainty | Notes                                                                                                                                                                                                                                                         |
| ----------------------- | --------------------------------------------------------------- | --- | ---------- | ------------- | ----- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **E-House A Enclosure** | 14' W × 260' L (3,640 SF), NEMA 3R weatherproof steel structure | 1   | $1,950,000 | $1,950,000    | ±25%  | 65%       | Includes: Steel enclosure, insulated walls/roof, doors, windows, interior finishes, integrated HVAC (redundant systems), clean agent fire suppression (Novec 1230), LED lighting, BMS panels, cable tray infrastructure, grounding, factory assembly/testing. |
| **E-House B Enclosure** | 14' W × 260' L (3,640 SF), NEMA 3R weatherproof steel structure | 1   | $1,950,000 | $1,950,000    | ±25%  | 65%       | Identical to E-House A. Includes same support systems.                                                                                                                                                                                                        |

**What's Included in E-House Enclosure Cost:**
- Building shell (14' × 260', 3,640 SF, NEMA 3R)
- Redundant HVAC systems (roof-mounted, climate control 68-77°F)
- Clean agent fire suppression (Novec 1230 or FM-200 for 51,000 cu ft)
- Interior/exterior LED lighting with emergency backup
- BMS control panels and environmental monitoring
- Cable tray support structure and infrastructure
- Grounding grid (internal)
- Personnel access doors, ADA ramps, exits
- Factory assembly, wiring infrastructure, and FAT

### 7.2 E-House Site Work

| Item | Specification | Qty | Unit Cost | Extended Cost | +/- % | Certainty | Notes |
|------|--------------|-----|-----------|---------------|-------|-----------|-------|
| **E-House Concrete Pads** | Reinforced concrete foundations, 14' × 260' | 2 | $150,000 | $300,000 | ±17% | 80% | Leveled, compacted, per E-House mfr specs |
| **E-House Installation & Rigging** | Crane, transport, set, connections | 1 | $200,000 | $200,000 | ±25% | 70% | Heavy rigging for 6-7 modules per E-House |

**Subtotal - E-Houses (Enclosures Only):** $4,400,000

---

## 8.0 480V DISTRIBUTION EQUIPMENT

### 8.1 Main Switchboards

| Item | Specification | Qty | Unit Cost | Extended Cost | +/- % | Certainty | Notes |
|------|--------------|-----|-----------|---------------|-------|-----------|-------|
| **Main Switchboards** | 4,000A, 480V, 3-phase, 4-wire, 65 kA SCCR, copper busbar | 2 | $175,000 | $350,000 | ±14% | 75% | SWBD-A and SWBD-B. Fed from MV Ring A and Ring B transformers respectively. Installed in E-Houses. |

### 8.2 Distribution Panels

| Item                        | Specification                 | Qty | Unit Cost | Extended Cost | +/- % | Certainty | Notes                                                           |
| --------------------------- | ----------------------------- | --- | --------- | ------------- | ----- | --------- | --------------------------------------------------------------- |
| **IT Distribution Panels**  | 800A, 480V, dual-path (A/B)   | 2   | $30,000   | $60,000       | ±15%  | 80%       | Cabinet PDU distribution. Installed in E-Houses.                |
| **Mech Dist 1 Panels**      | 800A, 480V, dual-path (A/B)   | 2   | $30,000   | $60,000       | ±15%  | 80%       | Loops 1+2 chillers/pumps (RDHx cooling). Installed in E-Houses. |
| **Mech Dist 2 Panels**      | 1,200A, 480V, dual-path (A/B) | 2   | $42,500   | $85,000       | ±20%  | 80%       | Loop 3 chillers/CDUs (L2C cooling). Installed in E-Houses.      |
| **UPS Distribution Panels** | 400A, 480V, dual-path (A/B)   | 2   | $18,500   | $37,000       | ±20%  | 80%       | UPS output distribution. Installed in E-Houses.                 |

### 8.3 Low Voltage Cables & Raceways

| Item                               | Specification                      | Qty      | Unit Cost | Extended Cost | +/- % | Certainty | Notes                                                     |
| ---------------------------------- | ---------------------------------- | -------- | --------- | ------------- | ----- | --------- | --------------------------------------------------------- |
| **480V Power Cables (Data Halls)** | 600V, Cu, THHN/THWN, various sizes | 1 LS     | $975,000  | $975,000      | ±20%  | 70%       | E-Houses to data halls, mechanical rooms. Dual A/B paths. |
| **Cable Tray Systems**             | Ladder tray, 24" wide, aluminum    | 5,000 LF | $55 /LF   | $275,000      | ±20%  | 75%       | Overhead distribution in data halls                       |
| **Conduit & Raceways**             | EMT, rigid, PVC, fittings          | 1 LS     | $250,000  | $250,000      | ±20%  | 70%       | Throughout facility                                       |

**Subtotal - 480V Distribution:** $2,092,000

---

## 9.0 CABINET POWER DISTRIBUTION (PDUs)

### 9.1 Rack-Mounted PDUs

| Item | Specification | Qty | Unit Cost | Extended Cost | +/- % | Certainty | Notes |
|------|--------------|-----|-----------|---------------|-------|-----------|-------|
| **Intelligent Monitored PDUs** | Dual-corded, metered, 208/240V, sized per rack load (30A-60A) | 788 | $2,000 | $1,576,000 | ±25% | 80% | 394 racks × 2 PDUs (A/B). Server Technology, Panduit SmartZone, or Eaton. Per-outlet monitoring, environmental sensors. |

### 9.2 Whips & Branch Circuits

| Item                         | Specification                       | Qty | Unit Cost | Extended Cost | +/- % | Certainty | Notes                              |
| ---------------------------- | ----------------------------------- | --- | --------- | ------------- | ----- | --------- | ---------------------------------- |
| **PDU Whips (Power Cables)** | 208/240V, 30-60A, from panel to PDU | 788 | $325      | $256,100      | ±25%  | 75%       | Custom lengths, factory terminated |

**Subtotal - Cabinet PDUs:** $1,832,100

---

## 10.0 HOUSE POWER (NON-CRITICAL)

### 10.1 House Power Transformer

| Item | Specification | Qty | Unit Cost | Extended Cost | +/- % | Certainty | Notes |
|------|--------------|-----|-----------|---------------|-------|-----------|-------|
| **House Power Transformer** | 400 kVA, 13.8kV/480Y/277V, pad-mounted | 1 | $62,500 | $62,500 | ±20% | 80% | Non-critical loads: offices, NOC, building systems |

### 10.2 Natural Gas House Generators

| Item                       | Specification                  | Qty | Unit Cost | Extended Cost | +/- % | Certainty | Notes                                            |
| -------------------------- | ------------------------------ | --- | --------- | ------------- | ----- | --------- | ------------------------------------------------ |
| **Natural Gas Generators** | 300 kW, 480V, natural gas, N+1 | 2   | $150,000  | $300,000      | ±15%  | 80%       | Cummins or Generac. Backup for house loads only. |

### 10.3 House Power Distribution

| Item                            | Specification                                        | Qty | Unit Cost | Extended Cost | +/- % | Certainty | Notes                                                                                                         |
| ------------------------------- | ---------------------------------------------------- | --- | --------- | ------------- | ----- | --------- | ------------------------------------------------------------------------------------------------------------- |
| **House Power Switchboard**     | 800A, 480V, main-tie-main with ATS                   | 1   | $55,000   | $55,000       | ±20%  | 80%       | Automatic transfer switch for utility/generator                                                               |
| **House Distribution Panels**   | 225A, 480V and 208V/120V panels                      | 8   | $4,000    | $32,000       | ±25%  | 85%       | Office, NOC, common areas, HVAC                                                                               |
| **Centralized House UPS Units** | 30 kVA, 480V, 3-phase, online double-conversion, N+1 | 2   | $30,830   | $61,660       | ±25%  | 75%       | Eaton 93E, Schneider Galaxy VS, or Vertiv. Right-sized for 22.7 kVA load. Serves NOC, security, offices, BMS. |
| **House UPS Battery Cabinets**  | 10-15 min runtime @ 30 kVA, VRLA batteries           | 2   | $7,500    | $15,000       | ±25%  | 75%       | External VRLA battery cabinets for centralized UPS units                                                      |

**Subtotal - House Power:** $526,160

---

## 11.0 GROUNDING & LIGHTNING PROTECTION

### 11.1 Facility Grounding System

| Item                                      | Specification                              | Qty | Unit Cost | Extended Cost | +/- % | Certainty | Notes                                               |
| ----------------------------------------- | ------------------------------------------ | --- | --------- | ------------- | ----- | --------- | --------------------------------------------------- |
| **Ground Grid (Site-Wide)**               | 4/0 bare copper, grid pattern, 10' spacing | 1   | $162,500  | $162,500      | ±25%  | 75%       | Per IEEE 142. Interconnects all electrical systems. |
| **Ground Rods**                           | 10' copper-clad steel, driven rods         | 150 | $200      | $30,000       | ±25%  | 80%       | Throughout facility                                 |
| **Ground Connections & Exothermic Welds** | Cadweld or equivalent connections          | 1   | $45,000   | $45,000       | ±20%  | 75%       | All bonding connections                             |

### 11.2 Lightning Protection

| Item                                | Specification                           | Qty | Unit Cost | Extended Cost | +/- % | Certainty | Notes                                    |
| ----------------------------------- | --------------------------------------- | --- | --------- | ------------- | ----- | --------- | ---------------------------------------- |
| **Lightning Protection System**     | Air terminals, down conductors, bonding | 1   | $100,000  | $100,000      | ±25%  | 70%       | UL 96A, NFPA 780. Building and E-Houses. |
| **Surge Protection Devices (SPDs)** | Type 1 & 2 SPDs at service entrances    | 25  | $3,000    | $75,000       | ±30%  | 80%       | 161kV, 13.8kV, 480V levels               |

**Subtotal - Grounding & Lightning:** $412,500

---

## 12.0 FIRE ALARM & LIFE SAFETY (ELECTRICAL)

### 12.1 Fire Alarm System

| Item                            | Specification                               | Qty | Unit Cost | Extended Cost | +/- % | Certainty | Notes                            |
| ------------------------------- | ------------------------------------------- | --- | --------- | ------------- | ----- | --------- | -------------------------------- |
| **Fire Alarm Control Panel**    | Addressable, networked, redundant           | 2   | $32,500   | $65,000       | ±25%  | 80%       | FACP-A and FACP-B for redundancy |
| **Smoke/Heat Detectors**        | Addressable, VESDA aspirating in data halls | 350 | $375      | $131,250      | ±30%  | 75%       | Early warning detection          |
| **Manual Pull Stations**        | Addressable, weatherproof where needed      | 30  | $225      | $6,750        | ±30%  | 85%       | Throughout facility              |
| **Notification Devices**        | Strobes, horns, speakers                    | 150 | $150      | $22,500       | ±30%  | 85%       | ADA compliant                    |
| **Fire Alarm Wiring & Devices** | Conduit, wire, junction boxes               | 1   | $162,500  | $162,500      | ±20%  | 70%       | Site-wide distribution           |

**Subtotal - Fire Alarm:** $388,000

---

## 13.0 LIGHTING SYSTEMS

### 13.1 Interior Lighting

| Item                                 | Specification                            | Qty | Unit Cost | Extended Cost | +/- % | Certainty | Notes                                                    |
| ------------------------------------ | ---------------------------------------- | --- | --------- | ------------- | ----- | --------- | -------------------------------------------------------- |
| **Data Hall LED High-Bay Fixtures**  | 150W LED, 0-10V dimming, 20,000 lm       | 250 | $325      | $81,250       | ±25%  | 85%       | 20,000 SF data halls (DH-W, DH-E)                        |
| **Office/Support Area LED Fixtures** | 2x2, 2x4 LED troffers, occupancy sensors | 300 | $162.50   | $48,750       | ±25%  | 85%       | Offices, NOC, corridors, break rooms                     |
| **Emergency Lighting & Exit Signs**  | LED, battery backup, exit signs          | 75  | $225      | $16,875       | ±30%  | 85%       | Life safety code compliance                              |
| **Exterior LED Lighting**            | Wall packs, pole-mounted, area lighting  | 50  | $450      | $22,500       | ±30%  | 80%       | Building perimeter, parking, generator/transformer yards |

### 13.2 Lighting Control System

| Item | Specification | Qty | Unit Cost | Extended Cost | +/- % | Certainty | Notes |
|------|--------------|-----|-----------|---------------|-------|-----------|-------|
| **Lighting Control Panels** | Networked, programmable, BMS integration | 8 | $4,000 | $32,000 | ±25% | 80% | Zone control for energy management |
| **Occupancy/Daylight Sensors** | Integrated with lighting controls | 75 | $200 | $15,000 | ±25% | 85% | Energy savings |

**Subtotal - Lighting:** $216,375

---

## 14.0 BUILDING MANAGEMENT SYSTEM (BMS) - ELECTRICAL INTEGRATION

### 14.1 BMS Hardware & Integration

| Item                              | Specification                                    | Qty | Unit Cost | Extended Cost | +/- % | Certainty | Notes                                       |
| --------------------------------- | ------------------------------------------------ | --- | --------- | ------------- | ----- | --------- | ------------------------------------------- |
| **BMS Controllers (Electrical)**  | Modbus/BACnet integration for electrical systems | 15  | $4,750    | $71,250       | ±25%  | 75%       | UPS, switchgear, generators, lighting       |
| **Power Metering & Sub-Metering** | Revenue-grade meters, CT/PT, data loggers        | 50  | $2,750    | $137,500      | ±25%  | 80%       | Per NEC 2023 energy monitoring requirements |

**Subtotal - BMS Electrical:** $208,750

---

## 15.0 TELECOM & STRUCTURED CABLING (POWER SYSTEMS)

### 15.1 Electrical Telecom Infrastructure

| Item | Specification | Qty | Unit Cost | Extended Cost | +/- % | Certainty | Notes |
|------|--------------|-----|-----------|---------------|-------|-----------|-------|
| **UPS Network Cards** | SNMP monitoring cards for UPS modules | 23 | $1,000 | $23,000 | ±20% | 85% | Remote monitoring |
| **Electrical System Network Backbone** | Fiber/copper for SCADA, BMS, monitoring | 1 | $100,000 | $100,000 | ±25% | 75% | Redundant network for electrical systems |

**Subtotal - Telecom (Electrical):** $123,000

---

## 16.0 TESTING, COMMISSIONING & STARTUP

| Item | Specification | Qty | Unit Cost | Extended Cost | +/- % | Certainty | Notes |
|------|--------------|-----|-----------|---------------|-------|-----------|-------|
| **Testing, Commissioning & Startup** | Comprehensive commissioning services including FAT, SAT, IST, and Tier III certification | 1 LS | $1,500,000 | $1,500,000 | ±20% | 70% | Placeholder for detailed commissioning plan. See commissioning planning notes below. |

**Commissioning Planning:**
- Hire independent commissioning agent (CxA) at design phase
- Budget adequate time for integrated systems testing (IST): 60-90 days
- Plan for Uptime Institute Tier III certification process (adds $200K-$400K to commissioning costs)
- Total commissioning investment includes FAT, SAT, IST, and Tier III certification

**Subtotal - Testing & Commissioning:** $1,500,000

---

## 17.0 ENGINEERING & DESIGN

### 17.1 Electrical Engineering Services

| Item                            | Specification                                 | Qty | Unit Cost  | Extended Cost | +/- % | Certainty | Notes                                                                                                                                                           |
| ------------------------------- | --------------------------------------------- | --- | ---------- | ------------- | ----- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Electrical Design (EE Firm)** | Detailed design, specifications, calculations | 1   | $1,500,000 | $1,500,000    | ±20%  | 75%       | Full design package: MV/LV distribution, one-lines, panel schedules, lighting, grounding, arc flash, coordination studies. Includes permitting coordination. |

**Subtotal - Engineering:** $1,500,000

---

## 18.0 CONSTRUCTION LABOR & INSTALLATION

### 18.1 Electrical Installation Labor

| Item | Specification | Qty | Unit Cost | Extended Cost | +/- % | Certainty | Notes |
|------|--------------|-----|-----------|---------------|-------|-----------|-------|
| **Electrical Contractor (EC) Labor** | Site installation, terminations, testing | 1 LS | $15,000,000 | $15,000,000 | ±20% | 65% | Estimated at 25-30% of equipment cost. Includes: MV/LV installations, cable pulling, terminations, panel installations, lighting, grounding, testing support. Union labor rates in Oklahoma. |

### 18.2 EC Indirect Costs

| Item | Specification | Qty | Unit Cost | Extended Cost | +/- % | Certainty | Notes |
|------|--------------|-----|-----------|---------------|-------|-----------|-------|
| **EC Overhead & Profit** | Mobilization, supervision, tools, profit | 1 LS | $2,625,000 | $2,625,000 | ±20% | 70% | 17.5% of labor cost (industry standard) |
| **Temporary Power & Facilities** | Temp power, trailers, laydown areas | 1 | $200,000 | $200,000 | ±25% | 75% | Construction duration |

**Subtotal - Labor & Installation:** $17,825,000

---

## 19.0 CONTINGENCY

### 19.1 Project Contingency

| Item | Specification | Percentage | Base Amount | Extended Cost | Notes |
|------|--------------|------------|-------------|---------------|-------|
| **Design Contingency** | Allowance for design development | 5.0% | $67,086,385 | $3,354,319 | Covers unknown conditions, scope refinements |
| **Construction Contingency** | Field issues, unforeseen conditions | 7.5% | $67,086,385 | $5,031,479 | Industry standard for data center electrical |
| **Total Contingency** | Combined design + construction | 12.5% | $67,086,385 | $8,385,798 | Total project contingency |

**Subtotal - Contingency:** $8,385,798

---

## 20.0 COST SUMMARY

### 20.1 Phase 4 Electrical Equipment & Installation - Total Cost

| Category                              | Cost            | % of Total |
| ------------------------------------- | --------------- | ---------- |
| **1.0 Utility Substation (161 kV)**   | $2,047,500      | 2.7%       |
| **2.0 MV Distribution (13.8 kV)**     | $2,375,000      | 3.2%       |
| **3.0 Generator System**              | $19,052,500     | 25.3%      |
| **4.0 LV Transformers**               | $3,125,000      | 4.1%       |
| **5.0 IT UPS System**                 | $7,262,500      | 9.6%       |
| **6.0 Mechanical UPS**                | $2,200,000      | 2.9%       |
| **7.0 E-Houses (Enclosures Only)**    | $4,400,000      | 5.8%       |
| **8.0 480V Distribution**             | $2,092,000      | 2.8%       |
| **9.0 Cabinet PDUs**                  | $1,832,100      | 2.4%       |
| **10.0 House Power**                  | $526,160        | 0.7%       |
| **11.0 Grounding & Lightning**        | $412,500        | 0.5%       |
| **12.0 Fire Alarm**                   | $388,000        | 0.5%       |
| **13.0 Lighting**                     | $216,375        | 0.3%       |
| **14.0 BMS Integration**              | $208,750        | 0.3%       |
| **15.0 Telecom (Electrical)**         | $123,000        | 0.2%       |
| **16.0 Testing & Commissioning**      | $1,500,000      | 2.0%       |
| **17.0 Engineering & Design**         | $1,500,000      | 2.0%       |
| **18.0 Labor & Installation**         | $17,825,000     | 23.6%      |
| **Subtotal (Before Contingency)**     | **$67,086,385** | **88.9%**  |
| **19.0 Contingency (12.5% combined)** | $8,385,798      | 11.1%      |
| **TOTAL ESTIMATED COST**              | **$75,472,183** | **100%**   |

### 20.2 Cost Per MW Analysis

| Metric | Value | Notes |
|--------|-------|-------|
| **Cost per MW (IT Load)** | $3,430,554 / MW | Based on 22 MW IT load |
| **Cost per MW (Facility Load)** | $2,541,556 / MW | Based on 29.7 MW total facility load |
| **Cost per kW (IT Load)** | $3,431 / kW | Industry benchmark: $3,500-$6,000/kW for electrical |
| **Cost per Rack** | $191,553 / rack | Based on 394 racks total (162 L2C + 232 RDHx) |

### 20.3 Industry Benchmark Validation

**Industry Standards for Data Center Electrical Infrastructure:**
- Electrical systems typically represent **40-45%** of total data center construction costs
- Total data center cost: **$8-12M per MW** (IT load) for conventional facilities
- AI-enabled data centers: **$15-20M+ per MW** (higher power density)

**Saga Pryor Validation:**
- Electrical cost: **$75.3M** for 22 MW IT load
- At industry benchmark of 42.5% of total: **Total facility cost ≈ $177M**
- Industry range for 22 MW: **$176M - $264M**
- **Result:** Our estimate of $75.3M for electrical (42.5% of ~$177M) aligns with industry benchmarks ✓

### 20.4 Major Cost Drivers (Top 5)

| Cost Category | Amount | % of Total | Key Items |
|---------------|--------|------------|-----------|
| **Generator System** | $19,052,500 | 25.3% | 9× 4 MW diesel generators @ 13.8kV with fuel systems |
| **Labor & Installation** | $17,825,000 | 23.7% | EC labor, overhead, temporary facilities |
| **Contingency** | $8,363,997 | 11.1% | Design (5%) + construction (7.5%) contingency |
| **IT UPS System** | $7,262,500 | 9.7% | 23× 1,250 kVA UPS modules + Li-Ion batteries |
| **E-Houses (Enclosures)** | $4,400,000 | 5.8% | 2× prefab electrical buildings (3,640 SF each) |
| **Top 5 Subtotal** | **$56,903,997** | **75.6%** | Three-quarters of total cost |

---

## 21.0 KEY ASSUMPTIONS & NOTES

### 21.1 Pricing Assumptions

1. **Market Conditions:** Pricing based on Q4 2024 / Q1 2025 market conditions. Electrical equipment market is relatively stable with lead times of 40-60 weeks for major equipment.
2. **Location Factor:** Oklahoma location factor applied. Labor rates assume prevailing wage (union) construction. Non-union construction could reduce labor costs by 15-20%.
3. **Quantity Discounts:** Large equipment purchases (23 UPS modules, 11 transformers, 9 generators) assume 10-15% volume discount already applied.
4. **Single Prime Contractor:** Assumes single electrical contractor for entire scope. Multiple contractors could increase costs by 5-10% due to coordination overhead.

5. **Lead Times:** Critical path items:
   - 161 kV Substation Transformers: 52 weeks
   - 4 MW Generators: 48-52 weeks
   - E-Houses (custom): 40-48 weeks
   - 3.5 MVA LV Transformers: 36-40 weeks
   - UPS Modules: 24-32 weeks

### 21.2 Cost Certainty Levels Explained

- **80-90%:** Standard catalog items with published pricing (PDUs, lighting, small panels)
- **70-79%:** Major equipment with vendor budgetary quotes (UPS, transformers, smaller generators)
- **60-69%:** Complex integrated systems requiring custom quotes (E-Houses, large generators, SCADA)
- **<60%:** Items requiring detailed design and site-specific engineering (labor, civil, commissioning)


### 21.3 Excluded Items

The following items are **NOT INCLUDED** in this electrical estimate:

1. **Solar PV System** - 16.8+ MW DC solar array with inverters
2. **Battery Energy Storage System (BESS)** - BESS with inverters
3. **Site Civil & Earthwork** - Grading, storm drainage, utilities (separate civil estimate)
4. **Data Hall Mechanical Systems** - Chillers, pumps, CDUs, piping, cooling towers (separate HVAC estimate)
5. **IT Equipment** - Servers, networking, storage (customer-provided)
6. **Building Envelope** - Structure, roof, walls, windows (separate estimate)
7. **Owner's Costs** - Permits, insurance, legal, project management, land acquisition
8. **Financing Costs** - Interest, loan fees, financing during construction
9. **Utility Interconnection Fees** - One-time utility connection charges (paid to Kamo Power, typically $500K-$2M)
10. **Sales Tax** - Oklahoma sales tax on equipment (if applicable - typically 4.5% state + local)


---

## 22.0 VERSION HISTORY & DOCUMENT CONTROL

**Version:** 1.0
**Date Updated:** 2025-11-06
**Prepared By:** PGCIS Team
**Review Status:** Draft for Review

**Revision History:**

| Date       | Version | Description                                                | Author |
| ---------- | ------- | ---------------------------------------------------------- | ------ |
| 2025-11-05 | 1.0     | Initial Phase 4 electrical equipment list with cost ranges | Benton |


---

**END OF DOCUMENT**
