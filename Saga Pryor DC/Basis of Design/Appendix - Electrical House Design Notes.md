

# APPENDIX - ELECTRICAL HOUSE DESIGN NOTES
## Supplemental Analysis: Key Design Decisions
### Pryor Data Center - PACHYDERM GLOBAL


---

## OVERVIEW

This document provides a high-level comparison of two foundational design choices: Electrical Power Architecture and E-House Construction Method. These decisions underpin the electrical infrastructure design specified in the main Electrical BOD (Division 26).

---

## 1. Power Architecture: Shared vs. Block Redundant

This decision defines how generators and E-Houses (PPMs) are configured to provide redundancy (e.g., N+1).

### Option 1: Shared Redundant (Common Bus) RECOMMENDED

This is the architecture selected for the Pachyderm project. All power sources (utility, 9 generators) feed a single "common bus" or "pool," and all loads (the two A/B E-House systems) draw from that same pool.

**Pros:**
- **Capital Efficiency (Lower CAPEX):** This is the primary advantage. Redundancy is shared. An N+1 design (8 loads) requires only **one** spare generator (9 total), not a spare for each block.
- **Load Flexibility:** Power can be distributed dynamically. If Hall 1 is at 30% load and Hall 2 is at 80%, the common pool supports this imbalance without issue.
- **Higher Utilization:** All "N" components are active, and no capacity is "stranded" (i.e., a spare for one block sitting idle while another block needs it).
- **Ideal for Asymmetric Loads:** This architecture is perfectly suited for the site's asymmetric data hall loads (e.g., DH-W @ 16.2 MW vs. DH-E @ 5.8 MW). The common power pool (22 MW total) serves both halls efficiently, whereas a "Block Redundant" design would require two different-sized, non-standard "blocks," eliminating any "cookie-cutter" efficiency.


**Cons:**
- **Higher Control Complexity:** Requires a more sophisticated (and well-tested) SCADA system and automated switchgear (like the RMUs) to manage the shared bus and isolate faults correctly.
- **Shared Fault Domain:** A catastrophic, uncontained fault on the common bus or in its primary switchgear could theoretically impact all connected loads. (This risk is heavily mitigated by the A/B dual-ring design).

### Option 2: Block Redundant (1:1)

This is a 1:1 architecture where each IT load "block" has its own dedicated, isolated power chain (e.g., 1 Generator -> 1 E-House -> 1 IT Load Block).

**Pros:**
- **Ultimate Fault Isolation:** This is the main advantage. The design is simple, and the power chains are physically and electrically separate. A total failure in Block 1 has zero impact on Block 2.
- **Simple Phasing:** Scalability is very simple "cookie-cutter" deployment. You build out an entire block, then copy-paste it for the next phase.

**Cons:**
- **High Capital Cost (CAPEX):** You are duplicating _all_ redundant equipment. An N+1 design with 8 active blocks would require 8 spare generators (16 total) or a more complex N+2 shared-block model.
- **Stranded Capacity:** The spare generator and E-House for Block 1 cannot be used to help Block 1. This is a very inefficient use of capital.
- **Load Inflexibility:** Power cannot be shared between blocks.

## 2. Construction Method: Prefabricated vs. Stick-Built

This decision defines _how_ the E-Houses are constructed and delivered.

### Option 1: Prefabricated E-Houses (Shipped)

This is the method selected for the Pachyderm project. E-Houses are fully constructed, integrated, and tested in a factory before being shipped to the site in shippable modules.

**Pros:**
- **Massive Schedule Acceleration:** This is the #1 reason for this method. The E-Houses are built in a factory _in parallel_ with the site's civil and foundation work, removing 3-6 months from the sequential schedule.
- **Higher Quality & Lower Risk:** Factory assembly is not subject to weather, field labor variables, or site congestion. Wiring and integration are higher quality with fewer errors.
- **Factory Acceptance Testing (FAT):** The entire system (switchgear, UPS, controls) is fully tested as a complete unit _before_ it leaves the factory, arriving on-site as a "known good" system.
- **Cost Certainty:** Provides a fixed, predictable cost from a single vendor, minimizing the risk of on-site labor or weather-related cost overruns.

**Cons:**
- **Logistical Complexity:** Requires detailed planning, road permits, and large cranes for setting the modules.
- **Design Constraints:** The E-House _modules_ are limited to shippable dimensions (e.g., 14-16 ft wide), which can force long, narrow "bowling alley" layouts.

### Option 2: Stick-Built Onsite (Traditional)

This involves building a traditional cinder block or metal-skinned building on the concrete pad, then having electricians install and wire all the equipment (switchgear, UPS, etc.) in the field.

**Pros:**
- **Total Design Flexibility:** The building can be any size or shape (e.g., 30-ft-wide) to optimize the equipment layout.
- **No Shipping Logistics:** Eliminates the need for road permits, pilot cars, and massive crane lifts.

**Cons:**
- **Major Schedule Delay:** This is a _sequential_ process. You must build the foundation, then the walls, then the roof, then wait for it to be "dried in" _before_ you can even start installing the electrical gear.
- **Higher Risk & Lower Quality:** Construction is exposed to weather delays (rain, mud, snow, heat). All integration and wiring are done in the field, leading to a higher chance of errors.
- **Higher Cost Risk:** Highly susceptible to on-site labor shortages, material price changes, and weather delays, leading to cost overruns.
- **Site Congestion & Safety:** Creates a long-term, active construction zone with multiple trades in a small, critical area.

## 3. Physical Placement & Interconnection Strategy

This section addresses the physical logistics of the selected "Shared Redundant" architecture using "Prefabricated E-Houses."

### E-House Specifications

**Configuration:** 2 E-Houses (E-House A for Ring A, E-House B for Ring B)

**Dimensions:** Each E-House is 14' W × 260' L (3,640 SF)

**Construction:** Each E-House is constructed from 6-7 connected prefabricated modules (each 40-50 ft long)

**Phase 1 Delivery:** Both E-Houses delivered complete with full 260' length. Equipment for Phase 1 is pre-installed; reserved space and conduit stubs provided for Phases 2-4 equipment.

**Phasing Strategy:** Equipment added to reserved spaces within existing E-Houses in Phases 2-4. No additional E-House modules or building envelope modifications required after Phase 1 delivery.

### LV Transformer Yard

**Configuration:** 11 × 3.5 MVA oil-filled transformers (13.8kV/480V) on outdoor concrete pads with oil containment

**Location:** Adjacent to E-Houses in electrical equipment yard

**Allocation:** 6 transformers on pads near E-House A (Ring A), 5 transformers on pads near E-House B (Ring B)

**Separation:** Transformers are separate from E-Houses to simplify E-House design (no oil containment inside climate-controlled enclosures)

### Physical Layout

- **Placement:** The two E-House systems (A and B) are placed as two long, parallel rows in the south electrical equipment yard. LV transformers on outdoor pads are positioned adjacent to their respective E-Houses.

- **Interconnection:** All power and data cabling from the E-Houses to the data halls will be routed via **underground duct banks**.
    - These duct banks (concrete-encased conduits) are installed _before_ the E-House pads are poured.
    - The E-Houses are built with pre-cut openings in the floor, which align with the conduit "stub-ups" from the duct bank.
    - Transformer pads have conduit stubs connecting to adjacent E-House MV/LV gear.

- **Redundancy:** At no point do cables from the "A" E-House or Ring A transformers pass _through_ the "B" E-House (or vice versa). The duct banks maintain 100% physical separation of the A/B power paths, which is critical for a Tier III, concurrently maintainable design. This is a standard and robust industry practice.


## 12.0 PREFABRICATED E-HOUSES (ELECTRICAL HOUSES)

### 12.1 Configuration

**Quantity:** Two (2) outdoor, walk-in E-Houses for Phase 1-4 (one per 13.8 kV ring)
**Dimensions:** Each E-House: **14' W × 260' L (3,640 SF)**

**Function:** Each E-House contains one complete 13.8 kV distribution ring (Ring A or Ring B) plus all associated 480V power distribution equipment. The two E-Houses work together to provide dual-path (A/B) redundancy for all critical data center loads.

### 12.2 E-House Enclosure Specifications

The E-House shall be a self-contained, walk-in steel enclosure meeting the following minimum requirements:

| Parameter             | Specification                                                                                                                                                                                       |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Structure**         | Heavy-duty, NEMA 3R (or higher) weatherproof steel construction with insulated walls and roof                                                                                                       |
| **Width**             | 14 ft (maximum highway shipping width - no oversized load permits required)                                                                                                                         |
| **Length**            | 260 ft (constructed from 6-7 connected modules, each 40-50 ft long)                                                                                                                                 |
| **Floor Area**        | 3,640 SF per E-House                                                                                                                                                                                |
| **Height (Interior)** | 14 ft clear height minimum for equipment and cable tray overhead routing                                                                                                                            |
| **Ceiling**           | Insulated metal deck with integrated cable tray support structure                                                                                                                                   |
| **Climate Control**   | Integrated redundant HVAC systems (heating and cooling) to maintain stable internal operating temperature (68-77°F) and humidity (40-60% RH) for all electrical equipment                           |
| **Safety & Access**   | Integrated clean agent fire suppression (Novec 1230 or FM-200), interior/exterior LED lighting, emergency exits, personnel access doors (36" min) meeting all applicable codes, ADA-compliant ramps |
| **Monitoring**        | Integrated Building Management System (BMS) connection for HVAC status, temperature/humidity alarms, fire alarm, door access, and environmental monitoring                                          |

### 12.3 E-House A (Ring A) - Integrated Electrical Equipment

E-House A shall be factory-built and tested with the following equipment pre-installed, wired, and integrated:

**13.8 kV Medium Voltage Gear:**
- 4 × RMUs (Ring Main Units): RMU-1A, RMU-2A, RMU-3A, RMU-4A (13.8 kV, 630A, SF6 or vacuum breakers)
- MV cable terminations for Ring A connections to transformers, generators, substation
- Integrated SCADA controls for self-healing ring operation

**480V Low Voltage Gear:**
- 1 × Main Switchboard A (SWBD-A): 4,000A, 480V, 3-phase, 4-wire, 65 kA SCCR
- 4 × Distribution Panels: IT Dist A, Mech Dist 1A, Mech Dist 2A, UPS Dist A

**IT UPS System A:**
- Phase 1: 2 × 1,250 kVA modular UPS units + 2 battery cabinets
- Phase 4 (ultimate): 12 × 1,250 kVA modular UPS units + 12 battery cabinets (Li-Ion)
- Reserved space and pre-installed conduit stubs for Phases 2-4 equipment additions

**Mechanical UPS System A:**
- Phase 1: 4 × 250 kW modular static UPS units
- Phase 4 (ultimate): 11 × 250 kW modular static UPS units
- Reserved space for Phases 2-4 equipment additions

**Support Systems:**
- Clean agent fire suppression (Novec 1230 or FM-200) sized for 3,640 SF @ 14' height (~51,000 cubic feet)
- Redundant HVAC systems (roof-mounted, factory-installed)
- BMS/SCADA control panels and monitoring equipment
- Interior/exterior LED lighting with emergency backup
- All associated system controls, monitoring, and safety interlocks

### 12.4 E-House B (Ring B) - Integrated Electrical Equipment

E-House B shall be factory-built and tested with the following equipment pre-installed, wired, and integrated:

**13.8 kV Medium Voltage Gear:**
- 4 × RMUs (Ring Main Units): RMU-1B, RMU-2B, RMU-3B, RMU-4B (13.8 kV, 630A, SF6 or vacuum breakers)
- MV cable terminations for Ring B connections to transformers, generators, substation
- Integrated SCADA controls for self-healing ring operation

**480V Low Voltage Gear:**
- 1 × Main Switchboard B (SWBD-B): 4,000A, 480V, 3-phase, 4-wire, 65 kA SCCR
- 4 × Distribution Panels: IT Dist B, Mech Dist 1B, Mech Dist 2B, UPS Dist B

**IT UPS System B:**
- Phase 1: 2 × 1,250 kVA modular UPS units + 2 battery cabinets
- Phase 4 (ultimate): 11 × 1,250 kVA modular UPS units + 11 battery cabinets (Li-Ion)
- Reserved space and pre-installed conduit stubs for Phases 2-4 equipment additions

**Mechanical UPS System B:**
- Phase 1: 4 × 250 kW modular static UPS units
- Phase 4 (ultimate): 11 × 250 kW modular static UPS units
- Reserved space for Phases 2-4 equipment additions

**Support Systems:**
- Clean agent fire suppression (Novec 1230 or FM-200) sized for 3,640 SF @ 14' height (~51,000 cubic feet)
- Redundant HVAC systems (roof-mounted, factory-installed)
- BMS/SCADA control panels and monitoring equipment
- Interior/exterior LED lighting with emergency backup
- All associated system controls, monitoring, and safety interlocks

### 12.5 LV Transformer Yard (Separate from E-Houses)

**Configuration:** 11 × 3.5 MVA LV transformers (13.8kV/480V) located on outdoor concrete pads adjacent to E-Houses

**Transformer Allocation:**
- Ring A Transformers: 6 units on pads adjacent to E-House A
- Ring B Transformers: 5 units on pads adjacent to E-House B

**Transformer Specifications:**
- Rating: 3,500 kVA / 3.15 MW @ 0.9 power factor
- Voltage: 13,800V delta primary / 480Y/277V secondary
- Type: Oil-filled, ONAN cooling (Oil Natural, Air Natural)
- Outdoor-rated enclosure with weatherproof construction

**Transformer Pads:**
- Reinforced concrete pads sized for transformer + oil containment
- Oil containment per EPA SPCC requirements (110% of transformer oil volume)
- Gravel-filled containment with oil-water separator
- MV/LV conduit stubs to E-Houses via underground duct banks

**Fire Protection:**
- Portable fire extinguishers (Class C electrical) at transformer yard
- No fixed fire suppression required for outdoor transformers

### 12.6 Phasing Strategy

**Phase 1 Delivery:**
- Both E-House A and E-House B delivered complete (full 14' × 260' structures)
- E-Houses arrive factory-tested with Phase 1 equipment pre-installed
- Reserved space and conduit stubs for future equipment pre-configured
- Installation: Set on prepared pads, connect to duct banks, startup/commission

**Advantages of Full E-House Delivery at Phase 1:**
- No future crane mobilizations or E-House building additions
- Clean equipment expansion without weather exposure
- Cost certainty: Fixed E-House cost at Phase 1, variable equipment cost in later phases
- Simplified commissioning: Factory-tested building envelope

### 12.7 Benefits

**Factory Testing & Quality:**
- Complete E-House system factory-tested and commissioned before shipment, reducing field commissioning risk
- Factory acceptance testing (FAT) includes: Hi-pot testing, insulation resistance, protective relay settings, control system functional testing, fire suppression pre-action test
- Factory environment provides controlled conditions for assembly, wiring, and testing - higher quality than field construction

**Schedule Acceleration:**
- 8-12 week schedule acceleration vs. traditional stick-built electrical buildings
- E-Houses manufactured in parallel with site civil/foundation work
- Delivery and installation: 2-3 weeks (vs. 6-9 months for stick-built)

**Cost Certainty:**
- Fixed, predictable cost from single vendor
- Minimizes risk of on-site labor or weather-related cost overruns
- Eliminates multi-trade coordination (electrical, HVAC, fire suppression all integrated)

**Simplified Field Installation:**
- Pre-wired and pre-tested E-Houses require only MV/LV connections and startup
- Reduces field labor by 30-40% vs. traditional construction
- Underground duct banks installed before E-House delivery with alignment to floor penetrations



---

**Tags:** #pryor-dc #electrical #e-house #design-decisions #architecture #prefabrication #redundancy

---

**Document Control:**
- **Created:** 2025-11-05
- **Updated:** 2025-11-05
- **Related:** [[Saga Pryor DC/Basis of Design/7BOD - Electrical (CSI Div 26)]], [[_BOD - Exec Summary]]
- **Purpose:** Supplemental analysis documenting key architectural decisions for electrical power distribution and E-House construction methodology