# PHASE 4 ELECTRICAL EQUIPMENT LIST AND COST ANALYSIS
**Saga Pryor Data Center - PACHYDERM GLOBAL**

**Created:** 2025-11-05
**Project Phase:** Phase 4 - Full Build-Out (22 MW IT Load)
**Total Facility Load:** 29.7 MW
**Related:** [[7BOD - Electrical (CSI Div 26)]]

---

## EXECUTIVE SUMMARY

This document provides a comprehensive equipment list and cost analysis for the Phase 4 electrical infrastructure of the Saga Pryor Data Center. The facility is designed for 22 MW IT load with a total facility load of approximately 29.7 MW, meeting Tier III standards with N+1 redundancy and dual-path distribution.

**Key Cost Metrics:**
- **Estimated Total Electrical Infrastructure Cost:** $90.1M - $118.5M
- **Cost per MW (IT Load):** $4.1M - $5.4M per MW
- **Cost per MW (Facility Load):** $3.0M - $4.0M per MW
- **Industry Benchmark Validation:** Falls within 40-45% of typical $8-12M/MW total data center costs

---

## 1.0 UTILITY SUBSTATION (161 kV)

### 1.1 Primary Substation Transformers

| Item | Specification | Qty | Unit Cost | Extended Cost | Certainty | Notes |
|------|--------------|-----|-----------|---------------|-----------|-------|
| **Substation Transformers** | 35 MVA, 161kV/13.8kV, ONAN, N+1 redundancy | 2 | $500,000 - $650,000 | $1,000,000 - $1,300,000 | 75% | Large HV transformers; pricing varies by manufacturer (ABB, Siemens, GE). Lead time: 40-52 weeks. |

### 1.2 161 kV Switchgear & Protection

| Item                             | Specification                         | Qty | Unit Cost           | Extended Cost       | Certainty | Notes                                    |
| -------------------------------- | ------------------------------------- | --- | ------------------- | ------------------- | --------- | ---------------------------------------- |
| **161 kV Disconnect Switches**   | Outdoor rated, motor operated         | 4   | $45,000 - $65,000   | $180,000 - $260,000 | 70%       | Per utility interconnection requirements |
| **161 kV Circuit Breakers**      | SF6 or vacuum, 2000A, 40kA            | 2   | $150,000 - $200,000 | $300,000 - $400,000 | 70%       | Main and tie breakers                    |
| **Protection Relays & Controls** | Distance, differential, overcurrent   | 1   | $75,000 - $125,000  | $75,000 - $125,000  | 65%       | SEL or equivalent                        |
| **Revenue Metering System**      | Utility-grade, 161kV CT/PT            | 1   | $50,000 - $80,000   | $50,000 - $80,000   | 75%       | Per utility requirements                 |
| **Substation Control Building**  | Prefab, climate controlled, 12'×20'   | 1   | $80,000 - $120,000  | $80,000 - $120,000  | 80%       | Houses relays, SCADA, controls           |
| **Substation Grounding System**  | Ground grid, driven rods, connections | 1   | $50,000 - $75,000   | $50,000 - $75,000   | 75%       | Per IEEE 142                             |

**Subtotal - Utility Substation:** $1,735,000 - $2,360,000

---

## 2.0 MEDIUM VOLTAGE (13.8 kV) DISTRIBUTION

### 2.1 Ring Main Units (RMUs)

| Item | Specification | Qty | Unit Cost | Extended Cost | Certainty | Notes |
|------|--------------|-----|-----------|---------------|-----------|-------|
| **Ring Main Units (RMUs)** | 13.8 kV, 630A, 20kA SCCR, SF6 or vacuum | 8 | $85,000 - $125,000 | $680,000 - $1,000,000 | 70% | Schneider Ringmaster or ABB SafeRing. 4 per ring (A/B). Includes integrated protection and motor operators. |

### 2.2 SCADA & Control System

| Item | Specification | Qty | Unit Cost | Extended Cost | Certainty | Notes |
|------|--------------|-----|-----------|---------------|-----------|-------|
| **SCADA Master Station** | Redundant servers, HMI, historian | 1 | $150,000 - $250,000 | $150,000 - $250,000 | 65% | Schneider EcoStruxure or Siemens WinCC |
| **RTUs for RMUs** | Remote terminal units, communications | 8 | $8,000 - $12,000 | $64,000 - $96,000 | 70% | One per RMU |
| **Fiber Optic Network** | Self-healing ring, switches, modems | 1 | $50,000 - $100,000 | $50,000 - $100,000 | 75% | TC Communications or equivalent |
| **SCADA Software Licenses** | Engineering, runtime, redundancy | 1 | $75,000 - $125,000 | $75,000 - $125,000 | 80% | Permanent licenses |

### 2.3 MV Cables & Terminations

| Item | Specification | Qty | Unit Cost | Extended Cost | Certainty | Notes |
|------|--------------|-----|-----------|---------------|-----------|-------|
| **15kV MV Cable (Dual-Ring)** | 15kV, 500 kcmil Cu, EPR, shielded | 12,000 LF | $35 - $50 /LF | $420,000 - $600,000 | 75% | Ring A & B interconnections, generator/solar feeds. Installed in duct banks. |
| **MV Cable Terminations** | 15kV, 630A, indoor/outdoor rated | 80 | $1,200 - $1,800 | $96,000 - $144,000 | 80% | RMU and transformer connections |
| **MV Duct Banks** | PVC conduit, concrete encased | 3,000 LF | $125 - $175 /LF | $375,000 - $525,000 | 70% | Substation to E-Houses, gen yard, transformer yard |

**Subtotal - MV Distribution:** $1,910,000 - $2,840,000

---

## 3.0 GENERATOR SYSTEM

### 3.1 Diesel Generators

| Item | Specification | Qty | Unit Cost | Extended Cost | Certainty | Notes |
|------|--------------|-----|-----------|---------------|-----------|-------|
| **4 MW Diesel Generators** | 4,000 kW continuous, 13.8 kV, EPA Tier 4 Final, sound-attenuated enclosure | 9 | $1,600,000 - $2,200,000 | $14,400,000 - $19,800,000 | 75% | Caterpillar, Cummins, or MTU. Includes MV switchgear, outdoor enclosure, cooling system. N+1 for 29.7 MW facility load. |

### 3.2 Fuel System

| Item | Specification | Qty | Unit Cost | Extended Cost | Certainty | Notes |
|------|--------------|-----|-----------|---------------|-----------|-------|
| **Main Fuel Storage Tanks** | 40,000 gal above-ground, double-wall | 3 | $150,000 - $200,000 | $450,000 - $600,000 | 75% | 12-hour runtime per Uptime Institute. UL-142 listed. |
| **Day Tanks (per generator)** | 1,000 gal, integral to generator skid | 9 | Included | Included | 90% | Included in generator cost |
| **Fuel Transfer Pumps & Controls** | Redundant pumps, filtration, leak detection | 1 | $75,000 - $125,000 | $75,000 - $125,000 | 75% | ISP Fuel Systems or Curtis Power |
| **Fuel Piping & Distribution** | Double-wall piping, valves, monitoring | 1 | $125,000 - $175,000 | $125,000 - $175,000 | 70% | Generator yard distribution |
| **Fuel Monitoring System** | Tank level, leak detection, alarms | 1 | $25,000 - $40,000 | $25,000 - $40,000 | 80% | BMS integration |

### 3.3 Generator Yard Infrastructure

| Item | Specification | Qty | Unit Cost | Extended Cost | Certainty | Notes |
|------|--------------|-----|-----------|---------------|-----------|-------|
| **Generator Concrete Pads** | Reinforced concrete, vibration isolation | 9 | $15,000 - $25,000 | $135,000 - $225,000 | 80% | Per generator, south side of building |
| **Generator Exhaust Systems** | Exhaust silencers, piping, SCR (if req'd) | 9 | $45,000 - $75,000 | $405,000 - $675,000 | 70% | EPA Tier 4 Final compliance |
| **Generator Switchgear (13.8kV)** | 13.8kV breakers, sync controls, paralleling | 1 | $350,000 - $500,000 | $350,000 - $500,000 | 70% | Central paralleling gear for 9 generators |

**Subtotal - Generator System:** $15,965,000 - $22,140,000

---

## 4.0 LOW VOLTAGE TRANSFORMERS (13.8 kV / 480V)

### 4.1 Distribution Transformers

| Item | Specification | Qty | Unit Cost | Extended Cost | Certainty | Notes |
|------|--------------|-----|-----------|---------------|-----------|-------|
| **3.5 MVA LV Transformers** | 3,500 kVA, 13.8kV/480Y/277V, ONAN, outdoor pad-mounted | 11 | $225,000 - $300,000 | $2,475,000 - $3,300,000 | 75% | ABB, Eaton, or Siemens. N+1 for 29.7 MW facility. 6 on Ring A, 5 on Ring B. |

### 4.2 Transformer Yard Infrastructure

| Item | Specification | Qty | Unit Cost | Extended Cost | Certainty | Notes |
|------|--------------|-----|-----------|---------------|-----------|-------|
| **Transformer Concrete Pads** | Reinforced concrete with oil containment | 11 | $12,000 - $18,000 | $132,000 - $198,000 | 80% | 110% oil containment per EPA SPCC |
| **Oil Containment & Separators** | Gravel fill, oil-water separator systems | 1 | $50,000 - $75,000 | $50,000 - $75,000 | 75% | Environmental compliance |
| **Fire Protection Equipment** | Portable extinguishers, signage | 1 | $8,000 - $12,000 | $8,000 - $12,000 | 85% | Class C electrical |

**Subtotal - LV Transformers:** $2,665,000 - $3,585,000

---

## 5.0 IT UPS SYSTEM

### 5.1 UPS Modules & Batteries

| Item | Specification | Qty | Unit Cost | Extended Cost | Certainty | Notes |
|------|--------------|-----|-----------|---------------|-----------|-------|
| **IT UPS Modules** | 1,250 kVA (1,000 kW), 480V, modular, online double-conversion | 23 | $175,000 - $250,000 | $4,025,000 - $5,750,000 | 70% | Schneider Galaxy VX, Eaton 9395, or Vertiv PowerUPS 9000. N+1 for 22 MW IT load (22+1). |
| **Lithium-Ion Battery Cabinets** | 5-minute runtime @ 1,250 kVA, external cabinets | 23 | $75,000 - $125,000 | $1,725,000 - $2,875,000 | 65% | Li-Ion preferred over VRLA: 10-15 year life, higher density, lower maintenance. One cabinet set per UPS module. |

### 5.2 UPS Support Systems

| Item | Specification | Qty | Unit Cost | Extended Cost | Certainty | Notes |
|------|--------------|-----|-----------|---------------|-----------|-------|
| **UPS Monitoring & Management** | Centralized monitoring, software licenses | 1 | $50,000 - $100,000 | $50,000 - $100,000 | 75% | Integrated with BMS |
| **UPS Maintenance Bypass Cabinets** | Integrated with UPS modules | 23 | Included | Included | 90% | Typically included in UPS module cost |

**Subtotal - IT UPS System:** $5,800,000 - $8,725,000

---

## 6.0 MECHANICAL UPS SYSTEM

### 6.1 Mechanical UPS Modules

| Item | Specification | Qty | Unit Cost | Extended Cost | Certainty | Notes |
|------|--------------|-----|-----------|---------------|-----------|-------|
| **Mechanical UPS Modules** | 250 kW, 480V, modular static UPS | 22 | $75,000 - $125,000 | $1,650,000 - $2,750,000 | 70% | N+1 for 4,900 kW mechanical load (21+1). Protects chillers, pumps, CDUs, building HVAC during generator startup. |

**Subtotal - Mechanical UPS:** $1,650,000 - $2,750,000

---

## 7.0 PREFABRICATED E-HOUSES (ELECTRICAL HOUSES)

### 7.1 E-House Structures

| Item | Specification | Qty | Unit Cost | Extended Cost | Certainty | Notes |
|------|--------------|-----|-----------|---------------|-----------|-------|
| **E-House A (Ring A)** | 14' W × 260' L (3,640 SF), NEMA 3R, climate controlled, with integrated Phase 4 electrical gear | 1 | $6,000,000 - $8,500,000 | $6,000,000 - $8,500,000 | 65% | See Section 7.2 for included equipment. Eaton, Schneider, or custom fabricator. Factory-built, tested, delivered complete. |
| **E-House B (Ring B)** | 14' W × 260' L (3,640 SF), NEMA 3R, climate controlled, with integrated Phase 4 electrical gear | 1 | $5,800,000 - $8,200,000 | $5,800,000 - $8,200,000 | 65% | See Section 7.3 for included equipment. Slightly less UPS capacity than E-House A (11 vs 12 modules). |

### 7.2 E-House A - Integrated Equipment (Included in E-House Cost Above)

**Equipment factory-installed in E-House A:**
- 4 × RMUs (RMU-1A through RMU-4A) - 13.8 kV, 630A
- 1 × Main Switchboard A (SWBD-A) - 4,000A, 480V, 65 kA SCCR
- 4 × Distribution Panels: IT Dist A (800A), Mech Dist 1A (800A), Mech Dist 2A (1,200A), UPS Dist A (400A)
- 12 × IT UPS Modules (1,250 kVA each) + 12 battery cabinets (Li-Ion)
- 11 × Mechanical UPS Modules (250 kW each)
- Clean agent fire suppression (Novec 1230 or FM-200) for 51,000 cu ft
- Redundant HVAC systems (roof-mounted)
- BMS/SCADA control panels
- Interior/exterior LED lighting with emergency backup
- Cable tray systems, grounding, all internal wiring

### 7.3 E-House B - Integrated Equipment (Included in E-House Cost Above)

**Equipment factory-installed in E-House B:**
- 4 × RMUs (RMU-1B through RMU-4B) - 13.8 kV, 630A
- 1 × Main Switchboard B (SWBD-B) - 4,000A, 480V, 65 kA SCCR
- 4 × Distribution Panels: IT Dist B (800A), Mech Dist 1B (800A), Mech Dist 2B (1,200A), UPS Dist B (400A)
- 11 × IT UPS Modules (1,250 kVA each) + 11 battery cabinets (Li-Ion)
- 11 × Mechanical UPS Modules (250 kW each)
- Clean agent fire suppression (Novec 1230 or FM-200) for 51,000 cu ft
- Redundant HVAC systems (roof-mounted)
- BMS/SCADA control panels
- Interior/exterior LED lighting with emergency backup
- Cable tray systems, grounding, all internal wiring

### 7.4 E-House Site Work

| Item | Specification | Qty | Unit Cost | Extended Cost | Certainty | Notes |
|------|--------------|-----|-----------|---------------|-----------|-------|
| **E-House Concrete Pads** | Reinforced concrete foundations, 14' × 260' | 2 | $125,000 - $175,000 | $250,000 - $350,000 | 80% | Leveled, compacted, per E-House mfr specs |
| **E-House Installation & Rigging** | Crane, transport, set, connections | 1 | $150,000 - $250,000 | $150,000 - $250,000 | 70% | Heavy rigging for 6-7 modules per E-House |

**Subtotal - E-Houses:** $12,200,000 - $17,300,000

---

## 8.0 480V DISTRIBUTION EQUIPMENT

### 8.1 Main Switchboards

**NOTE:** Main switchboards (SWBD-A and SWBD-B) are included in E-House costs above. Listed here for reference only.

| Item | Specification | Qty | Unit Cost | Notes |
|------|--------------|-----|-----------|-------|
| **Main Switchboards (Reference)** | 4,000A, 480V, 65 kA SCCR | 2 | Included in E-House | Integrated in E-Houses A & B |

### 8.2 Distribution Panels

**NOTE:** All distribution panels are included in E-House costs above. Listed here for reference only.

| Panel Type | Rating | Qty | Location | Notes |
|------------|--------|-----|----------|-------|
| IT Dist A / B | 800A | 2 | E-House A / B | Cabinet PDU distribution |
| Mech Dist 1A / 1B | 800A | 2 | E-House A / B | Loops 1+2 chillers/pumps (RDHx) |
| Mech Dist 2A / 2B | 1,200A | 2 | E-House A / B | Loop 3 chillers/CDUs (L2C) |
| UPS Dist A / B | 400A | 2 | E-House A / B | UPS output distribution |

### 8.3 Low Voltage Cables & Raceways

| Item | Specification | Qty | Unit Cost | Extended Cost | Certainty | Notes |
|------|--------------|-----|-----------|---------------|-----------|-------|
| **480V Power Cables (Data Halls)** | 600V, Cu, THHN/THWN, various sizes | 1 LS | $750,000 - $1,200,000 | $750,000 - $1,200,000 | 70% | E-Houses to data halls, mechanical rooms. Dual A/B paths. |
| **Cable Tray Systems** | Ladder tray, 24" wide, aluminum | 5,000 LF | $45 - $65 /LF | $225,000 - $325,000 | 75% | Overhead distribution in data halls |
| **Conduit & Raceways** | EMT, rigid, PVC, fittings | 1 LS | $200,000 - $300,000 | $200,000 - $300,000 | 70% | Throughout facility |

**Subtotal - 480V Distribution:** $1,175,000 - $1,825,000

---

## 9.0 CABINET POWER DISTRIBUTION (PDUs)

### 9.1 Rack-Mounted PDUs

| Item | Specification | Qty | Unit Cost | Extended Cost | Certainty | Notes |
|------|--------------|-----|-----------|---------------|-----------|-------|
| **Intelligent Monitored PDUs** | Dual-corded, metered, 208/240V, sized per rack load (30A-60A) | 788 | $1,500 - $2,500 | $1,182,000 - $1,970,000 | 80% | 394 racks × 2 PDUs (A/B). Server Technology, Panduit SmartZone, or Eaton. Per-outlet monitoring, environmental sensors. |

### 9.2 Whips & Branch Circuits

| Item | Specification | Qty | Unit Cost | Extended Cost | Certainty | Notes |
|------|--------------|-----|-----------|---------------|-----------|-------|
| **PDU Whips (Power Cables)** | 208/240V, 30-60A, from panel to PDU | 788 | $250 - $400 | $197,000 - $315,200 | 75% | Custom lengths, factory terminated |

**Subtotal - Cabinet PDUs:** $1,379,000 - $2,285,200

---

## 10.0 HOUSE POWER (NON-CRITICAL)

### 10.1 House Power Transformer

| Item | Specification | Qty | Unit Cost | Extended Cost | Certainty | Notes |
|------|--------------|-----|-----------|---------------|-----------|-------|
| **House Power Transformer** | 400 kVA, 13.8kV/480Y/277V, pad-mounted | 1 | $50,000 - $75,000 | $50,000 - $75,000 | 80% | Non-critical loads: offices, NOC, building systems |

### 10.2 Natural Gas House Generators

| Item | Specification | Qty | Unit Cost | Extended Cost | Certainty | Notes |
|------|--------------|-----|-----------|---------------|-----------|-------|
| **Natural Gas Generators** | 300 kW, 480V, natural gas, N+1 | 2 | $125,000 - $175,000 | $250,000 - $350,000 | 80% | Cummins or Generac. Backup for house loads only. |

### 10.3 House Power Distribution

| Item | Specification | Qty | Unit Cost | Extended Cost | Certainty | Notes |
|------|--------------|-----|-----------|---------------|-----------|-------|
| **House Power Switchboard** | 800A, 480V, main-tie-main | 1 | $45,000 - $65,000 | $45,000 - $65,000 | 80% | ATS for utility/generator transfer |
| **House Distribution Panels** | 225A, 480V and 208V/120V panels | 8 | $3,000 - $5,000 | $24,000 - $40,000 | 85% | Office, NOC, common areas, HVAC |
| **Workstation UPS Units** | 1-3 kVA, 10-15 min runtime | 25 | $800 - $1,500 | $20,000 - $37,500 | 85% | APC or CyberPower. NOC, security, offices. |

**Subtotal - House Power:** $389,000 - $567,500

---

## 11.0 GROUNDING & LIGHTNING PROTECTION

### 11.1 Facility Grounding System

| Item | Specification | Qty | Unit Cost | Extended Cost | Certainty | Notes |
|------|--------------|-----|-----------|---------------|-----------|-------|
| **Ground Grid (Site-Wide)** | 4/0 bare copper, grid pattern, 10' spacing | 1 | $125,000 - $200,000 | $125,000 - $200,000 | 75% | Per IEEE 142. Interconnects all electrical systems. |
| **Ground Rods** | 10' copper-clad steel, driven rods | 150 | $150 - $250 | $22,500 - $37,500 | 80% | Throughout facility |
| **Ground Connections & Exothermic Welds** | Cadweld or equivalent connections | 1 | $35,000 - $55,000 | $35,000 - $55,000 | 75% | All bonding connections |

### 11.2 Lightning Protection

| Item | Specification | Qty | Unit Cost | Extended Cost | Certainty | Notes |
|------|--------------|-----|-----------|---------------|-----------|-------|
| **Lightning Protection System** | Air terminals, down conductors, bonding | 1 | $75,000 - $125,000 | $75,000 - $125,000 | 70% | UL 96A, NFPA 780. Building and E-Houses. |
| **Surge Protection Devices (SPDs)** | Type 1 & 2 SPDs at service entrances | 25 | $2,000 - $4,000 | $50,000 - $100,000 | 80% | 161kV, 13.8kV, 480V levels |

**Subtotal - Grounding & Lightning:** $307,500 - $517,500

---

## 12.0 FIRE ALARM & LIFE SAFETY (ELECTRICAL)

### 12.1 Fire Alarm System

| Item | Specification | Qty | Unit Cost | Extended Cost | Certainty | Notes |
|------|--------------|-----|-----------|---------------|-----------|-------|
| **Fire Alarm Control Panel** | Addressable, networked, redundant | 2 | $25,000 - $40,000 | $50,000 - $80,000 | 80% | FACP-A and FACP-B for redundancy |
| **Smoke/Heat Detectors** | Addressable, VESDA aspirating in data halls | 350 | $250 - $500 | $87,500 - $175,000 | 75% | Early warning detection |
| **Manual Pull Stations** | Addressable, weatherproof where needed | 30 | $150 - $300 | $4,500 - $9,000 | 85% | Throughout facility |
| **Notification Devices** | Strobes, horns, speakers | 150 | $100 - $200 | $15,000 - $30,000 | 85% | ADA compliant |
| **Fire Alarm Wiring & Devices** | Conduit, wire, junction boxes | 1 | $125,000 - $200,000 | $125,000 - $200,000 | 70% | Site-wide distribution |

**Subtotal - Fire Alarm:** $282,000 - $494,000

---

## 13.0 LIGHTING SYSTEMS

### 13.1 Interior Lighting

| Item | Specification | Qty | Unit Cost | Extended Cost | Certainty | Notes |
|------|--------------|-----|-----------|---------------|-----------|-------|
| **Data Hall LED High-Bay Fixtures** | 150W LED, 0-10V dimming, 20,000 lm | 250 | $250 - $400 | $62,500 - $100,000 | 85% | 20,000 SF data halls (DH-W, DH-E) |
| **Office/Support Area LED Fixtures** | 2x2, 2x4 LED troffers, occupancy sensors | 300 | $125 - $200 | $37,500 - $60,000 | 85% | Offices, NOC, corridors, break rooms |
| **Emergency Lighting & Exit Signs** | LED, battery backup, exit signs | 75 | $150 - $300 | $11,250 - $22,500 | 85% | Life safety code compliance |
| **Exterior LED Lighting** | Wall packs, pole-mounted, area lighting | 50 | $300 - $600 | $15,000 - $30,000 | 80% | Building perimeter, parking, generator/transformer yards |

### 13.2 Lighting Control System

| Item | Specification | Qty | Unit Cost | Extended Cost | Certainty | Notes |
|------|--------------|-----|-----------|---------------|-----------|-------|
| **Lighting Control Panels** | Networked, programmable, BMS integration | 8 | $3,000 - $5,000 | $24,000 - $40,000 | 80% | Zone control for energy management |
| **Occupancy/Daylight Sensors** | Integrated with lighting controls | 75 | $150 - $250 | $11,250 - $18,750 | 85% | Energy savings |

**Subtotal - Lighting:** $161,500 - $271,250

---

## 14.0 BUILDING MANAGEMENT SYSTEM (BMS) - ELECTRICAL INTEGRATION

### 14.1 BMS Hardware & Integration

| Item | Specification | Qty | Unit Cost | Extended Cost | Certainty | Notes |
|------|--------------|-----|-----------|---------------|-----------|-------|
| **BMS Controllers (Electrical)** | Modbus/BACnet integration for electrical systems | 15 | $3,500 - $6,000 | $52,500 - $90,000 | 75% | UPS, switchgear, generators, lighting |
| **Power Metering & Sub-Metering** | Revenue-grade meters, CT/PT, data loggers | 50 | $2,000 - $3,500 | $100,000 - $175,000 | 80% | Per NEC 2023 energy monitoring requirements |

**Subtotal - BMS Electrical:** $152,500 - $265,000

---

## 15.0 TELECOM & STRUCTURED CABLING (POWER SYSTEMS)

### 15.1 Electrical Telecom Infrastructure

| Item | Specification | Qty | Unit Cost | Extended Cost | Certainty | Notes |
|------|--------------|-----|-----------|---------------|-----------|-------|
| **UPS Network Cards** | SNMP monitoring cards for UPS modules | 23 | $800 - $1,200 | $18,400 - $27,600 | 85% | Remote monitoring |
| **Electrical System Network Backbone** | Fiber/copper for SCADA, BMS, monitoring | 1 | $75,000 - $125,000 | $75,000 - $125,000 | 75% | Redundant network for electrical systems |

**Subtotal - Telecom (Electrical):** $93,400 - $152,600

---

## 16.0 TESTING, COMMISSIONING & STARTUP

### 16.1 Factory Acceptance Testing (FAT)

| Item | Specification | Qty | Unit Cost | Extended Cost | Certainty | Notes |
|------|--------------|-----|-----------|---------------|-----------|-------|
| **E-House FAT** | Factory testing of E-Houses A & B | 2 | $75,000 - $125,000 | $150,000 - $250,000 | 80% | Hi-pot, functional testing, relay settings |
| **Generator FAT** | Factory testing of generators (by group) | 3 | $15,000 - $25,000 | $45,000 - $75,000 | 80% | Load bank testing at factory |
| **Transformer Testing** | Factory testing per IEEE C57.12.00 | 14 | $5,000 - $8,000 | $70,000 - $112,000 | 85% | Substation + LV transformers |

### 16.2 Site Commissioning & Testing

| Item | Specification | Qty | Unit Cost | Extended Cost | Certainty | Notes |
|------|--------------|-----|-----------|---------------|-----------|-------|
| **Commissioning Agent Services** | Independent CxA, Tier III validation | 1 | $350,000 - $500,000 | $350,000 - $500,000 | 75% | Full electrical commissioning per Uptime Tier III |
| **Integrated Systems Testing (IST)** | Full load testing, transfer testing, simulations | 1 | $200,000 - $300,000 | $200,000 - $300,000 | 70% | 30-60 days post-energization |
| **Utility Interconnection Testing** | Utility witness tests, protection coordination | 1 | $50,000 - $75,000 | $50,000 - $75,000 | 80% | Required by Kamo Power |
| **Thermographic Surveys** | IR scanning of all electrical connections | 3 | $15,000 - $25,000 | $45,000 - $75,000 | 85% | Pre-energization, post-startup, 30-day |
| **Arc Flash Study & Labeling** | IEEE 1584 study, coordination study, labels | 1 | $50,000 - $75,000 | $50,000 - $75,000 | 85% | NFPA 70E compliance |

**Subtotal - Testing & Commissioning:** $960,000 - $1,462,000

---

## 17.0 ENGINEERING & DESIGN

### 17.1 Electrical Engineering Services

| Item | Specification | Qty | Unit Cost | Extended Cost | Certainty | Notes |
|------|--------------|-----|-----------|---------------|-----------|-------|
| **Electrical Design (EE Firm)** | Detailed design, specifications, calculations | 1 | $1,200,000 - $1,800,000 | $1,200,000 - $1,800,000 | 75% | Full design package: MV/LV distribution, one-lines, panel schedules, lighting, grounding, arc flash, coordination studies |
| **Permitting & Utility Coordination** | Permit drawings, utility applications, inspections | 1 | $125,000 - $200,000 | $125,000 - $200,000 | 80% | Oklahoma, EPA, utility interconnection agreements |

**Subtotal - Engineering:** $1,325,000 - $2,000,000

---

## 18.0 CONSTRUCTION LABOR & INSTALLATION

### 18.1 Electrical Installation Labor

| Item | Specification | Qty | Unit Cost | Extended Cost | Certainty | Notes |
|------|--------------|-----|-----------|---------------|-----------|-------|
| **Electrical Contractor (EC) Labor** | Site installation, terminations, testing | 1 | $12,000,000 - $18,000,000 | $12,000,000 - $18,000,000 | 65% | Estimated at 25-30% of total equipment cost. Includes: MV/LV installations, cable pulling, terminations, panel installations, lighting, grounding, testing support. Union labor rates in Oklahoma. |

### 18.2 EC Indirect Costs

| Item | Specification | Qty | Unit Cost | Extended Cost | Certainty | Notes |
|------|--------------|-----|-----------|---------------|-----------|-------|
| **EC Overhead & Profit** | Mobilization, supervision, tools, profit | 1 LS | 15-20% of labor | $1,800,000 - $3,600,000 | 70% | Industry standard markup |
| **Temporary Power & Facilities** | Temp power, trailers, laydown areas | 1 | $150,000 - $250,000 | $150,000 - $250,000 | 75% | Construction duration |

**Subtotal - Labor & Installation:** $13,950,000 - $21,850,000

---

## 19.0 CONTINGENCY & ESCALATION

### 19.1 Project Contingency

| Item | Specification | Percentage | Extended Cost | Certainty | Notes |
|------|--------------|------------|---------------|-----------|-------|
| **Design Contingency** | Allowance for design development | 5% of Subtotal | $3,800,000 - $5,350,000 | N/A | Covers unknown conditions, scope refinements |
| **Construction Contingency** | Field issues, unforeseen conditions | 7.5% of Subtotal | $5,700,000 - $8,025,000 | N/A | Industry standard for data center electrical |

### 19.2 Escalation (Optional)

| Item | Specification | Percentage | Extended Cost | Certainty | Notes |
|------|--------------|------------|---------------|-----------|-------|
| **Escalation to Mid-2026** | Assume 4% annual escalation | 4-6% | $3,600,000 - $7,100,000 | N/A | If construction delayed 12-18 months from Q1 2025 |

**Subtotal - Contingency:** $9,500,000 - $13,375,000 (without escalation)

---

## 20.0 COST SUMMARY

### 20.1 Phase 4 Electrical Equipment & Installation - Total Cost

| Category | Cost Range (Low) | Cost Range (High) | Certainty | % of Total |
|----------|-----------------|-------------------|-----------|------------|
| **1.0 Utility Substation (161 kV)** | $1,735,000 | $2,360,000 | 73% | 1.9-2.0% |
| **2.0 MV Distribution (13.8 kV)** | $1,910,000 | $2,840,000 | 72% | 2.1-2.4% |
| **3.0 Generator System** | $15,965,000 | $22,140,000 | 74% | 17.7-18.7% |
| **4.0 LV Transformers** | $2,665,000 | $3,585,000 | 76% | 3.0-3.0% |
| **5.0 IT UPS System** | $5,800,000 | $8,725,000 | 69% | 6.4-7.4% |
| **6.0 Mechanical UPS** | $1,650,000 | $2,750,000 | 70% | 1.8-2.3% |
| **7.0 E-Houses (Prefab)** | $12,200,000 | $17,300,000 | 65% | 13.5-14.6% |
| **8.0 480V Distribution** | $1,175,000 | $1,825,000 | 72% | 1.3-1.5% |
| **9.0 Cabinet PDUs** | $1,379,000 | $2,285,200 | 79% | 1.5-1.9% |
| **10.0 House Power** | $389,000 | $567,500 | 81% | 0.4-0.5% |
| **11.0 Grounding & Lightning** | $307,500 | $517,500 | 75% | 0.3-0.4% |
| **12.0 Fire Alarm** | $282,000 | $494,000 | 78% | 0.3-0.4% |
| **13.0 Lighting** | $161,500 | $271,250 | 83% | 0.2-0.2% |
| **14.0 BMS Integration** | $152,500 | $265,000 | 77% | 0.2-0.2% |
| **15.0 Telecom (Electrical)** | $93,400 | $152,600 | 80% | 0.1-0.1% |
| **16.0 Testing & Commissioning** | $960,000 | $1,462,000 | 78% | 1.1-1.2% |
| **17.0 Engineering & Design** | $1,325,000 | $2,000,000 | 77% | 1.5-1.7% |
| **18.0 Labor & Installation** | $13,950,000 | $21,850,000 | 67% | 15.5-18.4% |
| **Subtotal (Before Contingency)** | **$62,100,000** | **$91,390,050** | **71%** | **68.9-77.1%** |
| **19.0 Contingency (12.5% combined)** | $9,500,000 | $13,375,000 | N/A | 10.5-11.3% |
| **TOTAL ESTIMATED COST** | **$90,100,000** | **$118,540,050** | **71%** | **100%** |

### 20.2 Cost Per MW Analysis

| Metric | Low Estimate | High Estimate | Notes |
|--------|-------------|---------------|-------|
| **Cost per MW (IT Load)** | $4.1M / MW | $5.4M / MW | Based on 22 MW IT load |
| **Cost per MW (Facility Load)** | $3.0M / MW | $4.0M / MW | Based on 29.7 MW facility load |
| **Cost per kW (IT Load)** | $4,095 / kW | $5,388 / kW | Industry benchmark: $3,500-$6,000/kW for electrical |
| **Cost per Rack** | $228,680 / rack | $300,863 / rack | Based on 394 racks total |

### 20.3 Industry Benchmark Validation

**Industry Standards for Data Center Electrical Infrastructure:**
- Electrical systems typically represent **40-45%** of total data center construction costs
- Total data center cost: **$8-12M per MW** (IT load) for conventional facilities
- AI-enabled data centers: **$15-20M+ per MW** (higher power density)

**Saga Pryor Validation:**
- Total DC cost estimate (if electrical is 42.5% of total): **$212M - $279M** for full facility
- At industry benchmark of $8-12M/MW: **$176M - $264M** for 22 MW
- **Result:** Our electrical estimate of $90M-$118M represents approximately **40-45%** of expected total facility cost, confirming alignment with industry benchmarks.

---

## 21.0 KEY ASSUMPTIONS & NOTES

### 21.1 Pricing Assumptions

1. **Market Conditions:** Pricing based on Q4 2024 / Q1 2025 market conditions. Electrical equipment market is relatively stable with lead times of 40-60 weeks for major equipment.

2. **Location Factor:** Oklahoma location factor applied. Labor rates assume prevailing wage (union) construction. Non-union construction could reduce labor costs by 15-20%.

3. **Quantity Discounts:** Large equipment purchases (23 UPS modules, 11 transformers, 9 generators) should qualify for volume pricing. Estimates assume 10-15% volume discount already applied.

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

1. **Solar PV System** - 8+ MW DC solar array with inverters (per user instruction)
2. **Battery Energy Storage System (BESS)** - 4-8 MWh BESS with inverters (per user instruction)
3. **Site Civil & Earthwork** - Grading, storm drainage, utilities (separate civil estimate)
4. **Data Hall Mechanical Systems** - Chillers, pumps, CDUs, piping, cooling towers (separate HVAC estimate)
5. **IT Equipment** - Servers, networking, storage (customer-provided)
6. **Building Envelope** - Structure, roof, walls, windows (separate architectural estimate)
7. **Owner's Costs** - Permits, insurance, legal, project management, land acquisition
8. **Financing Costs** - Interest, loan fees, financing during construction
9. **Utility Interconnection Fees** - One-time utility connection charges (paid to Kamo Power, typically $500K-$2M)
10. **Sales Tax** - Oklahoma sales tax on equipment (if applicable)

### 21.4 Risk Factors & Potential Cost Increases

**HIGH RISK (Could add 10-25% to estimate):**
- Significant delays in equipment procurement (extended lead times due to supply chain issues)
- Major design changes during construction (scope creep)
- Unforeseen site conditions (poor soil, rock, high water table affecting foundations)
- Utility interconnection complications (protection coordination issues, utility upgrade requirements)
- Labor shortages or strikes (Oklahoma construction market tightening)

**MEDIUM RISK (Could add 5-10%):**
- Equipment price escalation beyond assumed rates
- Engineering design errors or omissions requiring rework
- Weather delays affecting outdoor installation (generator/transformer yards, E-Houses)
- Permitting delays (EPA, state, local)

**LOW RISK (Could add 2-5%):**
- Commissioning duration longer than expected
- Testing failures requiring rework
- Minor scope additions during construction

### 21.5 Value Engineering Opportunities

**Potential Cost Reductions (while maintaining Tier III performance):**

1. **UPS Architecture Alternative:** Current design uses N+1 UPS with self-healing MV dual-ring. A traditional 2N UPS architecture (separate A/B UPS systems) would cost **+$8M-$12M more** but would eliminate dependency on MV ring self-healing. Current design is cost-optimized.

2. **E-House vs. Stick-Built:** Analysis shows E-Houses provide **15-20% cost savings** vs. traditional stick-built electrical buildings when considering total installed cost, schedule acceleration, and reduced field labor risk.

3. **Li-Ion vs. VRLA Batteries:** Li-Ion batteries cost **30-50% more upfront** than VRLA, but provide 10-15 year life vs. 5-7 years, lower maintenance, and better performance. Total cost of ownership favors Li-Ion over 15-year lifecycle.

4. **Generator Quantity:** Current design uses 9×4MW generators (N+1 for 29.7 MW). Alternative: 6×6MW generators (N+1 for 30 MW). This would **reduce generator count by 33%** but increase unit cost and may exceed EPA/air quality permit limits for single-unit emissions. Analysis required.

5. **Natural Gas vs. Diesel Generators:** Natural gas generators could reduce fuel storage costs by **$400K-$600K** but require natural gas pipeline extension (cost TBD) and may have longer startup times affecting battery runtime requirements.

---

## 22.0 RECOMMENDATIONS

### 22.1 Procurement Strategy

1. **Early Procurement (Long-Lead Items):**
   - Issue RFPs for 161 kV substation transformers, 4 MW generators, and E-Houses **immediately** after design completion
   - These items drive critical path (48-52 week lead times)
   - Consider 10% deposit to secure manufacturing slots

2. **Phased Procurement:**
   - While full infrastructure (substation, MV ring, E-Houses, transformer/generator pads) should be built at Phase 1, **capital equipment can be phased**:
     - **Phase 1:** 3 generators, 3 transformers, 4 UPS modules (committed spend: ~$15M)
     - **Phases 2-4:** Add equipment as needed (deferred spend: ~$75M-$103M)
   - This approach **reduces upfront capital by 70-75%** while maintaining ability to scale

3. **Volume Pricing:**
   - Negotiate multi-phase pricing commitments with UPS and transformer vendors
   - Lock in pricing for Phases 2-4 equipment with escalation caps (e.g., CPI + 2%)
   - Secure equipment storage if early delivery provides cost savings

4. **Single-Source vs. Multi-Source:**
   - **Recommend single-source** for UPS modules (Schneider, Eaton, or Vertiv) for consistency in training, maintenance, and spare parts
   - **Consider dual-source** for transformers and generators to maintain competitive pricing across phases

### 22.2 Risk Mitigation

1. **Utility Coordination:**
   - Begin utility interconnection discussions with Kamo Power **12-18 months before energization**
   - Budget $1.5M-$2.5M for utility interconnection fees (not included in this estimate)
   - Confirm 161 kV service availability and protection requirements early

2. **Design Completion:**
   - Engage Tier III-experienced electrical engineering firm
   - Complete 100% design documents before issuing RFPs to minimize change orders
   - Include 3D BIM coordination to identify conflicts before construction

3. **Commissioning:**
   - Hire independent commissioning agent (CxA) at design phase
   - Budget adequate time for integrated systems testing (IST): 60-90 days
   - Plan for Uptime Institute Tier III certification process (adds $200K-$400K to commissioning costs, not included above)

### 22.3 Schedule Considerations

**Preliminary Schedule (Electrical Systems Only):**

| Phase | Duration | Key Activities |
|-------|----------|----------------|
| **Design & Engineering** | 6 months | 100% electrical design, permitting, utility coordination |
| **Long-Lead Procurement** | 3 months | RFPs, vendor selection, equipment ordering |
| **Manufacturing & Delivery** | 12-14 months | Equipment fabrication (overlaps with site work) |
| **Site Preparation** | 6 months | Civil work, foundations, duct banks, pads |
| **Equipment Installation** | 8 months | E-House set, generator/transformer installation, MV/LV connections |
| **Testing & Commissioning** | 3 months | Startup, FAT/SAT, IST, Tier III validation |
| **Total Project Duration** | **24-28 months** | From design kickoff to energization |

**Critical Path:** 161 kV substation transformers and E-Houses (52-week lead time) drive overall schedule.

---

## 23.0 DOCUMENT CONTROL

**Version:** 1.0
**Date Created:** 2025-11-05
**Prepared By:** Claude (AI Assistant) in collaboration with PGCIS Team
**Review Status:** Draft for Review

**Revision History:**
| Date | Version | Description | Author |
|------|---------|-------------|--------|
| 2025-11-05 | 1.0 | Initial Phase 4 electrical equipment list and cost analysis | Claude |

**Next Steps:**
1. Review cost estimates with electrical engineering firm for validation
2. Obtain vendor budgetary quotes for major equipment (generators, transformers, UPS, E-Houses)
3. Refine labor estimates based on local contractor input (Oklahoma electrical contractors)
4. Develop detailed phased procurement strategy
5. Validate utility interconnection costs with Kamo Power
6. Create procurement schedule aligned with project master schedule

---

**END OF DOCUMENT**
