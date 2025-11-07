
# BASIS OF DESIGN - CSI MASTERFORMAT
## Pryor Data Center - PACHYDERM GLOBAL
### Pryor, Oklahoma

**Document Status:** REVISION 02 - 161 kV Substation + 13.8 kV Distribution (US Standard Voltage)
**Prepared by:** PGCIS Team
**Date:** October 30, 2025 
**Purpose:** Comprehensive Basis of Design for Pryor Data Center organized by CSI Master Format

---

## EXECUTIVE SUMMARY


### **FACILITY OVERVIEW**
- **IT Capacity:** 4-phase buildout to 22 MW ultimate capacity
  - Phase 1: 3 MW (30 racks @ 100 kW, L2C anchor tenant in DH-W)
  - Phase 2: 6 MW (150 racks total: 30 L2C + 120 RDHx, open both halls)
  - Phase 3: 15 MW (285 racks total: 105 L2C + 180 RDHx, scale both halls)
  - Phase 4: 22 MW (394 racks total: 162 L2C + 232 RDHx, full build-out)
- **Total Compound:** 140,000 SF (Two 10,000 SF data halls + 18,000 SF support spaces)
  - **Covered Building:** 38,000 SF
  - **Equipment Yard:** 102,000 SF
  - Phase 1: DH-W only (30 racks)
  - Phase 2+: Both halls operational (394 racks total capacity)
- **Power Density:** Scales from 300 W/SF (Phase 1) to 1,100 W/SF (Phase 4)
- **Rack Capacity:** DH-W: 162 racks (L2C), DH-E: 232 racks (RDHx)
- **Availability:** Tier III (N+1 IT UPS with MV dual-ring path redundancy, N+1 mechanical, concurrent maintainability)
- **Target PUE:** 1.45 (Phase 1), 1.45 (Phase 2), 1.35 (Phase 3), 1.35 (Phase 4)
- **Target WUE:** 0 L/kWh - zero water for cooling
- **Site:** Pryor, Oklahoma (Tornado Alley - FM 1-150 protection)
- **Key Differentiators:**
  - Google Cloud proximity (sub-millisecond latency, eliminate data egress costs)
  - Customer-owned 161 kV substation with 13.8 kV distribution
  - L2C liquid cooling ready from day 1

**Phasing Summary:**

| Phase | IT Load | PUE  | Facility Load | Total Racks | L2C Racks | RDHx Racks | Active Halls |
|-------|---------|------|---------------|-------------|-----------|------------|--------------|
| **1** | 3 MW    | 1.45 | 4.35 MW       | 30          | 30        | 0          | DH-W only    |
| **2** | 6 MW    | 1.45 | 8.7 MW        | 150         | 30        | 120        | DH-W + DH-E  |
| **3** | 15 MW   | 1.35 | 20.25 MW      | 285         | 105       | 180        | DH-W + DH-E  |
| **4** | 22 MW   | 1.35 | 29.7 MW       | 394         | 162       | 232        | DH-W + DH-E  |

---

### **ELECTRICAL SYSTEMS**
- **Primary Utility Service:** Customer-owned 161 kV substation
  - **161 kV Transmission:** Direct connection to utility transmission system
  - **Substation Transformers:** 2 × 35 MVA, 161kV/13.8kV (N+1 redundancy - either can carry full 30 MW facility load)
- **13.8 kV Common Bus:** Single voltage platform for utility, solar, BESS, generators, data center (US standard voltage)
- **MV Distribution:** 13.8 kV dual-ring topology (Ring A + Ring B) via 8 RMUs
- **Generators:** Scalable N+1 diesel generators @ 13.8 kV, Tier 4 Final
  - Phase 1: 3 × 4.0 MW (N+1 for 4.35 MW facility load)
  - Phase 2: 4 × 4.0 MW total (N+1 for 8.7 MW facility load, add 1 unit)
  - Phase 3: 7 × 4.0 MW total (N+1 for 20.25 MW facility load, add 3 units)
  - Phase 4: 9 × 4.0 MW total (N+1 for 29.7 MW facility load, add 2 units)
  - Fuel: ~2,000 gal belly tanks per unit connected via common manifold to centralized bulk fuel storage (24-hour runtime with redundant fuel contracts)
- **LV Transformers:** 11 × 3.5 MVA oil-filled transformers (13.8kV/480V) on outdoor pads, N+1 with concurrent maintainability
  - Phase 1: 3 × 3,500 kVA (N+1 for 4.35 MW facility load)
  - Phase 2: 4 × 3,500 kVA total (N+1 for 8.7 MW facility load, add 1 unit)
  - Phase 3: 8 × 3,500 kVA total (N+1 for 20.25 MW facility load, add 4 units)
  - Phase 4: 11 × 3,500 kVA total (N+1 for 29.7 MW facility load, add 3 units)
  - Location: Outdoor concrete pads with oil containment adjacent to E-Houses
- **E-Houses (Electrical Houses):** 2 climate-controlled prefabricated E-Houses (14' × 260' each, 3,640 SF per unit)
  - Configuration: One E-House per 13.8 kV ring (E-House A for Ring A, E-House B for Ring B)
  - Contents: MV switchgear (RMUs), LV switchboards, IT UPS, Mechanical UPS, battery cabinets, distribution panels
  - Enclosure: NEMA 3R weatherproof steel with redundant HVAC, clean agent fire suppression, BMS integration
  - Phasing: Both E-Houses delivered complete at Phase 1; equipment added to reserved space in Phases 2-4
  - Concurrent maintainability: Walk-in access, NEC clearances, A/B path isolation via underground duct banks
- **IT UPS:** N+1 modular architecture (path redundancy from self-healing MV dual-ring)
  - Phase 1: 4 × 1,250 kVA modules (N+1 for 3 MW IT load @ 80% loading)
  - Phase 2: 7 × 1,250 kVA modules total (N+1 for 6 MW IT load, add 3 units)
  - Phase 3: 16 × 1,250 kVA modules total (N+1 for 15 MW IT load, add 9 units)
  - Phase 4: 23 × 1,250 kVA modules total (N+1 for 22 MW IT load, add 7 units)
  - Battery: 5-minute runtime maximum (allows for MV generator sync to bus, even two attempts)
  - **Redundancy Philosophy:** 13.8 kV dual-ring provides path redundancy via self-healing SCADA switching; N+1 UPS provides component redundancy
- **Mechanical UPS:** N+1 modular UPS for mechanical loads (chiller pumps, CRAH fans)
- **LV Distribution:** Dual switchboards (SWBD-A/B) fed from different MV ring segments
- **Cabinet Power:** Dual PDUs fed from different 480V distribution panels (sized per customer rack density)
- **MV Distribution:** 8 RMUs (13.8 kV, 630A), dual-ring topology
- **Non-Critical Building Power (Separate System):**
  - House generators: 2 × 250-350 kW natural gas (N+1 redundancy)
  - Serves: offices, bathrooms, hallways, SCR, SCB, loading dock, NOC, gym, storm shelter
  - Portable UPS: ~20-30 units for IT equipment ride-through in non-critical areas
- **Electrical Code:** NEC 2023, Oklahoma amendments

**Electrical Equipment Phasing:**

| Equipment Type | Phase 1 | Phase 2 | Phase 3 | Phase 4 | Sizing Notes |
|----------------|---------|---------|---------|---------|--------------|
| **Generators (4.0 MW ea)** | 3 units | 4 units (+1) | 7 units (+3) | 9 units (+2) | N+1 for facility load |
| **LV Transformers (3.5 MVA)** | 3 units | 4 units (+1) | 8 units (+4) | 11 units (+3) | N+1 for facility load |
| **IT UPS Modules (1,250 kVA)** | 4 units | 7 units (+3) | 16 units (+9) | 23 units (+7) | N+1 for IT load |
| **Mechanical UPS (250 kW)** | 8 units | 12 units (+4) | 16 units (+4) | 22 units (+6) | N+1 for mech load |
| **E-Houses (14'×260')** | 2 units | 2 units | 2 units | 2 units | Full delivery Phase 1 |
| **RMUs (13.8 kV)** | 8 units | 8 units | 8 units | 8 units | Dual-ring (4 per ring) |

---

### **MECHANICAL SYSTEMS**
- **Cooling Strategy:** Separate loop architecture optimized for efficiency and rack diversity
- **Loop 3 (Warm Water - L2C Direct-to-Chip):**
  - Temperature: 85°F supply (29°C) - optimized for warm water cooling efficiency
  - Serves: 162 L2C racks (16.2 MW at Phase 4)
  - CDUs: 162 rack pairs (324 physical units with A/B redundancy, 100+ kW capacity each)
  - Phase 1: 4 × 1,500 kW air-cooled chillers (N+1 for 3 MW)
  - Phase 2: Keep 4 chillers (L2C load unchanged at 3 MW)
  - Phase 3: 9 × 1,500 kW chillers total (N+1 for 10.5 MW)
  - Phase 4: 12 × 1,500 kW chillers total (N+1 for 16.2 MW)
- **Loops 1+2 (Cold Water - RDHx Rear-Door Cooling):**
  - Temperature: 60°F supply (15.5°C) - required for rear-door air cooling
  - Serves: 232 RDHx racks (5.8 MW at Phase 4)
  - RDHx: 232 rear-door heat exchangers at full build-out (1 per RDHx rack)
  - Phase 1: Not commissioned (no RDHx racks)
  - Phase 2: 3 × 1,500 kW air-cooled chillers (N+1 for 3 MW)
  - Phase 3: 5 × 1,500 kW chillers total (N+1 for 4.5 MW)
  - Phase 4: 6 × 1,500 kW chillers total (N+1 for 5.8 MW)
- **Separate Loop Rationale:** 85°F warm water for L2C provides superior efficiency vs. traditional 55-60°F; separating loops optimizes each system independently
- **Free Cooling:** ~3,500-4,000 hours/year (Oklahoma climate with 85°F warm water - significantly more than 55°F systems)
- **Zero Water Strategy:** No evaporative cooling, closed-loop glycol only
- **Building HVAC:** Separate package units for offices/support spaces
- **Mechanical Code:** IMC 2021, ASHRAE 90.1-2019

---

### **FACILITY CONSTRUCTION**
- **Structure:** Pre-cast concrete tilt-up construction (tornado-resistant)
- **Total Compound:** 140,000 SF (Two 10,000 SF data halls + 18,000 SF support spaces)
	- **Covered Building:** 38,000 SF
	- **Equipment Yard:** 102,000 SF
- **Roofing:** FM 1-150 tornado-rated (150 mph winds, Class 4 hail); storm-rated stainless steel debris screen; protected roof equipment
- **Walls:** Tilt-up concrete panels (8-12" thick, reinforced for high wind loads)
- **Floor:** Slab-on-grade (raised floor: Not Applicable), sealed concrete with optional epoxy
- **Ceiling Height:** 30+ ft clear in data halls
- **Containment:** Not Applicable (DDC cabinets provide integrated cooling)
- **Storm Shelter/Safe Room:** FEMA 361 compliant prefabricated module (EF5 protection), 20 person capacity, located on Level 1 adjacent to elevator
- **Security:** 
  - K-rated perimeter fence (8 ft height, 100 ft building standoff)
  - Two property entrances:
    - Main entrance (NE corner): Sally port vehicle trap
    - Secondary entrance (NW side): Emergency/construction access (visible from loading dock SCB)
  - Mantrap entry, full MFA (card + biometric), CCTV with 90-day retention

---

### **SUPPORT SPACES**

**East End Entry Zone:**
- **Main entrance (Blue Zone):** Lobby with luggage room, public restroom, Security Control Room (SCR)
- **Secure office zone (Yellow Zone):** Post-mantrap access to conference room, 2 restrooms, hoteling office area, 2 soundproof call pods, seating area
- **Telecommunications:** MPOE (fiber entrance), MMR (meet-me-room), fire riser
- **Perimeter corridor:** Secure perimeter corridor providing access to secure data hall access points and secure indoor mechanical gallery maintenance areas

**West End Loading Zone:**
- **Loading dock:** 2-bay weather-protected loading area with Security Control Booth (SCB)
- **Support areas:** Secure staging, secure storage, janitor closet, internal restroom
- **Telecommunications:** Second MPOE (redundant fiber entrance), second MMR (redundant meet-me-room), fire riser
- **Delivery driver restroom:** Accessible only from outside at NW corner (within view of security)
- **E-Houses:** 2 Electrical Houses (14' × 260' each) located in south electrical equipment yard, plus 11 LV transformers on outdoor pads

**Multi-Level Central Spine:**

*Note: The central spine features 3 occupied levels plus roof access. All other areas (data halls, offices, loading zone) are single-level.*

- **Level 1 (Grade Level):** Prefabricated storm shelter/safe room (20 person), elevator/stairwell, redundant restrooms, men's/women's showers, break room, lounge, gaming area (TBD)
- **Level 2 (Secure NOC):** NOC (~2,060 SF), private NOC area
- **Level 3 (Fitness/Tour Route):** Gym/fitness center, secure tour route with internal windows into critical areas, weather-protected balconies (north/south) for equipment yard views, accessible to security and technical operations staff for routine site walks
- **Roof Access:** Weather-protected access via elevator/stairwell; storm-rated SS debris screen; protected roof-mounted equipment

---

### **RENEWABLE ENERGY & UTILITIES**
- **Solar:** Adjacent ~12 MW solar array (owned separately, behind-the-meter connection to 13.8 kV common bus)
- **BESS:** Battery Energy Storage System (owned separately, behind-the-meter connection to 13.8 kV common bus)
- **Primary Utility Service:** Owner-constructed 161 kV substation with 2 × 35 MVA transformers (161kV/13.8kV, N+1 redundancy)
  - Dual redundant 161 kV transmission line feeds
  - All power transformed to 13.8 kV common bus (US standard voltage for data centers and renewables)
- **Water:** Municipal or well (domestic use only, ~500-1,000 gal/day)
- **Sewer:** Municipal or septic (domestic wastewater)
- **Natural Gas:** Utility service for house generators (backup power to non-critical areas)
- **[TBD] OPTIONAL Micro-Turbine Natural Gas Generators:** For Oklahoma SB 480 qualification (budget in Solar/BESS CAPEX, not Data Center)
- **Fiber:** Dual diverse entries via underground ductbank [CRITICAL PRIORITY - Must confirm physically diverse paths and carrier agreements before project proceeds]

---

### **FIRE PROTECTION & LIFE SAFETY**
- **Data Halls:** Zoned preaction sprinkler system with VESDA early warning detection
- **Cabinet Suppression:** Integrated fire suppression in DDC cabinets
- **E-Houses:** Clean agent suppression (Novec 1230 or FM-200) in both E-Houses (sized for 3,640 SF @ 14' height per enclosure)
- **LV Transformer Yard:** Portable fire extinguishers (Class C electrical) at outdoor transformer pads
- **Detection:** VESDA (Very Early Smoke Detection Apparatus) in data halls
- **Egress:** 2 minimum exits per data hall, 36" doors (44" preferred)
- **Emergency Lighting:** 90-minute battery backup
- **NFPA Compliance:** NFPA 72, 75, 76, 2001, 101; IBC 2021

---

### **PHASING STRATEGY**

4-phase customer-driven buildout optimized for AI/ML workload growth:

| Phase | IT MW | Total Racks | L2C Racks | RDHx Racks | Avg kW/rack | Active Halls | Primary Strategy                        |
| ----- | ----- | ----------- | --------- | ---------- | ----------- | ------------ | --------------------------------------- |
| **1** | 3     | 30          | 30        | 0          | 100.0       | DH-W only    | L2C anchor tenant (AI Training)         |
| **2** | 6     | 150         | 30        | 120        | 40.0        | DH-W + DH-E  | Open both halls, add RDHx diversity     |
| **3** | 15    | 285         | 105       | 180        | 52.6        | DH-W + DH-E  | Scale both L2C and RDHx capacity        |
| **4** | 22    | 394         | 162       | 232        | 55.8        | DH-W + DH-E  | Full build-out (16.2 MW L2C, 5.8 MW RDHx) |

**Phase 1 Strategy:** L2C liquid cooling only (no RDHx cooling plant) = lower CAPEX, proves high-density capability with AI training anchor tenant.

**Phase 2 Strategy:** Open both data halls, commission RDHx cooling plant (Loops 1+2) to add customer diversity with medium-density racks.

**Detailed phasing specifications:** See Electrical BOD (Div 26) and Mechanical BOD (Div 23).

---

## KEY DESIGN DECISIONS


### **Why Tilt-Up Concrete (Not PEMB)**
- **Tornado resistance:** Pre-cast concrete withstands EF3-EF5 events better than steel framing
- **Insurance:** 30-40% lower premiums vs. PEMB in Tornado Alley
- **Thermal mass:** Better temperature stability, reduces HVAC cycling
- **Cost:** ~$15-25/SF premium over PEMB, justified by insurance savings and resilience

### **Why Slab-on-Grade (No Raised Floor)**
- Cost savings (~$150K+)
- Eliminates failure modes and underfloor plenum complications
- Better seismic performance
- Overhead cable distribution provides equivalent flexibility

### **Why FM 1-150 Roofing**
- **Tornado protection:** 150 mph wind resistance, Class 4 hail rating
- **Storm-rated infrastructure:** Stainless steel debris screen protects roof equipment
- **Insurance requirement:** Mandatory in Tornado Alley for facility insurance coverage
- **Cost premium:** ~$500-800K justified by 30-40% lower annual insurance premiums
- **Long-term resilience:** Protects critical infrastructure investment

### **Why Separate Warm/Cold Loop Architecture (85°F vs 60°F)**
- **Loop 3 (Warm Water - 85°F for L2C):** Optimized for liquid-to-chip direct cooling, provides 30-50% better COP than traditional cold water systems
- **Loops 1+2 (Cold Water - 60°F for RDHx):** Required temperature for rear-door air heat exchangers
- **Efficiency advantage:** 85°F warm water enables 5,000-6,000 hours/year of free cooling (vs. 3,500 hours with cold water)
- **Independent control:** L2C loads swing violently with GPU workloads; RDHx loads are stable - separating prevents control instability
- **Required for high density:** L2C enables 100+ kW/rack densities that air cooling cannot achieve
- **Phase 1 enabler:** Proves warm water liquid cooling capability to attract AI training anchor tenant

### **Why Zoned-Hall Design (L2C vs. RDHx)**
- **Customer-Driven CapEx:** Aligns capital spending directly with customer demand. We can build either the 16.2 MW L2C plant (for DH-W) **or** the 5.8 MW RDHx plant (for DH-E) first, depending on which anchor tenant signs. This prevents building millions in a stranded, unused cooling plant.
- **Maximized Rack Count:** Optimizes the 20,000 SF footprint. The L2C hall requires wide 6-ft service aisles (fitting ~162 racks), while the RDHx hall uses a standard 4-ft layout (fitting ~232 racks), maximizing the facility's total inventory to 394 racks.
- **Simplified Infrastructure:** Each hall has its own dedicated cooling loop at optimized temperature. This **prevents high-risk "spaghetti" piping** from mixing warm/cold systems, simplifies construction, and lowers long-term operational risk.
- **Dual Market Strategy:** Creates two distinct, marketable products: a **High-Density Zone** (100 kW L2C for AI training) and a **Medium-Density Zone** (25 kW RDHx for AI inference/enterprise), providing maximum flexibility to serve the entire AI market.

---


**Next Steps:**
1. TBD

---

**Document Control:**
- **Source:** PGCIS Team
- **Date Updated:** October 29, 2025
- **Corrections:**


**CAPEX Savings Note:**
- We've kept the sparkle of the high ceilings and raised walking track for customer tours and security... However, for cost savings, an overall reduction in building height to ~20ft would provide ample space for any type of adaptation (hot aisle containment, etc.). It would save on steel and concrete, if required.