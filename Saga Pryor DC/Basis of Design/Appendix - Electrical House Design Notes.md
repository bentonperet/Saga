**Created:** 2025-11-05
**Project:** Saga Pryor Data Center - PACHYDERM GLOBAL
**Parent Document:** [[7BOD - Electrical (CSI Div 26) v2]]

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

- **Placement:** The two E-House systems (A and B) will be placed as two long, parallel rows of modules in the equipment yard. As the site grows, new modules will be added to the ends of these rows, extending their length.
- **Interconnection:** All power and data cabling from the E-Houses to the data halls will be routed via **underground duct banks**.
    - These duct banks (concrete-encased conduits) are installed _before_ the E-House pads are poured.
    - The E-Houses are built with pre-cut openings in the floor, which align with the conduit "stub-ups" from the duct bank.
    - This design ensures that cabling for the _furthest_ E-House modules simply runs **underneath** the concrete pads of the closer modules.
- **Redundancy:** At no point do cables from the "A" E-House pass _through_ the "B" E-House (or vice versa). The duct banks maintain 100% physical separation of the A/B power paths, which is critical for a Tier III, concurrently maintainable design. This is a standard and robust industry practice.

---

**Tags:** #pryor-dc #electrical #e-house #design-decisions #architecture #prefabrication #redundancy

---

**Document Control:**
- **Created:** 2025-11-05
- **Updated:** 2025-11-05
- **Related:** [[7BOD - Electrical (CSI Div 26) v2]], [[_BOD - Exec Summary]]
- **Purpose:** Supplemental analysis documenting key architectural decisions for electrical power distribution and E-House construction methodology