
# BASIS OF DESIGN - CSI MASTERFORMAT
## Pryor Data Center - PACHYDERM GLOBAL / Saga Energy
### Pryor, Oklahoma

**Prepared by:** PGCIS Team for Saga Energy
**Date:** October 30, 2025 
**Purpose:** Comprehensive Basis of Design for Pryor Data Center organized by CSI Master Format

---

## EXECUTIVE SUMMARY


### **FACILITY OVERVIEW**
- **IT Capacity:** Minimum 2-phase and up to 4-phase buildouts available, with up to 24 MW ultimate capacity
- **Total Compound:** 140,000 SF (Two 10,000 SF data halls + 18,000 SF support spaces)
  - **Covered Building:** 38,000 SF
  - **Equipment Yard:** 102,000 SF
- **Power Density:** Scalable by 6MW blocks. A 12, 18, or 24 MW deployment all possible depending on client specifications.
- **Rack Capacity:** Client-specific deployment (Medium and high density supported, depending on client demand)
- **Availability:** Tier III (N+1 component redundancy per 6MW block, MV dual-ring path redundancy, concurrent maintainability)
- **Target PUE:** 1.3 - 1.4 average
- **Target WUE:** 0 L/kWh - zero water for cooling
- **Site:** Pryor, Oklahoma (Tornado Alley - FM 1-150 protection)
- **Key Differentiators:**
  - Google Cloud proximity (sub-millisecond latency, eliminate data egress costs)
  - Customer-owned 161 kV substation with 13.8 kV distribution
  - Block-based deployment (6MW IT blocks) with 4 E-Houses per block
  - L2C liquid cooling capable from day 1 (85°F warm water)

---

### **ELECTRICAL SYSTEMS**
- **Primary Utility Service:** Customer-owned 161 kV substation
  - **161 kV Transmission:** Direct connection to utility transmission system
  - **Substation Transformers:** 2 × 50 MVA, 161kV/13.8kV (N+1 redundancy)
- **13.8 kV Common Bus:** Single voltage platform for utility, solar, generators, data center (US standard voltage)
- **MV Distribution:** 13.8 kV dual-ring topology (Ring A + Ring B) via 8 RMUs <!-- @muhammed -->
- **Generators:** Scalable N+1 diesel generators @ 13.8 kV
- **LV Transformers:** 11 × 3.5 MVA oil-filled transformers (13.8kV/480V) on outdoor pads, N+1 with concurrent maintainability (Location: Outdoor concrete pads with oil containment adjacent to E-Houses).
- **Electrical Houses:** 16 climate-controlled prefabricated E-Houses <!-- @muhammed -->
  - Configuration: One E-House per 13.8 kV ring (E-House A for Ring A, E-House B for Ring B)
  - Contents: MV switchgear (RMUs), LV switchboards, IT UPS, Mechanical UPS, battery cabinets, distribution panels
- **IT UPS:** N+1 modular architecture (path redundancy from self-healing MV dual-ring)
  - Battery: 5-minute runtime maximum (allows for MV generator sync to bus)
  - **Redundancy Philosophy:** 13.8 kV dual-ring provides path redundancy via self-healing SCADA switching; N+1 UPS provides component redundancy
- **Mechanical UPS:** N+1 modular UPS for mechanical loads (chiller pumps, CRAH fans)
- **LV Distribution:** Dual switchboards (SWBD-A/B) fed from different MV ring segments
- **Cabinet Power:** Dual PDUs fed from different 480V distribution panels (sized per customer rack density) <!-- @muhammed -->
- **MV Distribution:** 8 RMUs (13.8 kV, 630A), dual-ring topology <!-- @muhammed -->
- **Non-Critical Building Power (Separate System):**
  - House generators: 2 × 250-350 kW natural gas (N+1 redundancy)
  - Serves: offices, bathrooms, hallways, SCR, SCB, loading dock, NOC, gym, storm shelter
  - UPS: 2 units for IT equipment ride-through in non-critical areas
- **Electrical Code:** NEC 2023, Oklahoma amendments

**Electrical Equipment Phasing:**

| Equipment Type                 | Phase 1 | Phase 2       | Phase 3       | Phase 4       | Sizing Notes           |
| ------------------------------ | ------- | ------------- | ------------- | ------------- | ---------------------- |
| **Generators (4.0 MW ea)**     | 3 units | 4 units (+1)  | 7 units (+3)  | 9 units (+2)  | N+1 for facility load  |
| **LV Transformers (3.5 MVA)**  | 3 units | 4 units (+1)  | 8 units (+4)  | 11 units (+3) | N+1 for facility load  |
| **IT UPS Modules (1,250 kVA)** | 4 units | 7 units (+3)  | 16 units (+9) | 23 units (+7) | N+1 for IT load        |
| **Mechanical UPS (250 kW)**    | 8 units | 12 units (+4) | 16 units (+4) | 22 units (+6) | N+1 for mech load      |
| **E-Houses (14'×260')**        | 2 units | 2 units       | 2 units       | 2 units       | Full delivery Phase 1  |
| **RMUs (13.8 kV)**             | 8 units | 8 units       | 8 units       | 8 units       | Dual-ring (4 per ring) |
<!-- @muhammed update the table -->


---

### **MECHANICAL SYSTEMS**
- **Cooling Strategy:** Separate loop architecture optimized for efficiency and rack diversity
- **Loop 3 (Warm Water - L2C Direct-to-Chip):**
  - Temperature: ~85°F supply (29°C) - optimized for warm water cooling efficiency
- **Loops 1+2 (Cold Water - RDHx Rear-Door Cooling):**
  - Temperature: ~60°F supply (15.5°C) - required for rear-door air cooling
- **Separate Loop Rationale:** 85°F warm water for L2C provides superior efficiency vs. traditional colder temperature cooling for other liquid cooling.
- **Free Cooling:** ~3,500-4,000 hours/year
- **Zero Water Strategy:** No evaporative cooling, closed-loop glycol only
- **Building HVAC:** Separate package units for offices/support spaces
- **Mechanical Code:** IMC 2021, ASHRAE 90.1-2019

---

### **FACILITY CONSTRUCTION**
- **Structure:** Pre-cast concrete tilt-up construction (tornado-resistant)
- **Roofing:** FM 1-150 tornado-rated (150 mph winds, Class 4 hail); storm-rated stainless steel debris screen; protected roof equipment
- **Walls:** Tilt-up concrete panels
- **Floor:** Slab-on-grade (raised floor: Not Applicable), sealed concrete with optional epoxy
- **Ceiling Height:** ~30 ft clear in data halls
- **Containment:** Not Applicable (DDC cabinets provide integrated cooling). If client specifies, design allows for containment with ample ceiling height.
- **Storm Shelter/Safe Room:** FEMA 361 compliant prefabricated module (EF5 protection), 20 person capacity, located on Level 1 adjacent to elevator
- **Security:** 
  - K-rated perimeter fence (8 ft height)
  - Main entrance (NE corner): Sally port vehicle trap.
  - Secondary entrance (NW side): Emergency / construction access (visible from loading dock SCB)
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
- **E-Houses:** 16 Electrical Houses at Phase 4 (4 per 6MW block) located in south electrical equipment yard, plus LV transformers on outdoor pads

**Multi-Level Central Spine:**
*Note: The central spine features 3 occupied levels plus roof access. All other areas (data halls, offices, loading zone) are single-level.*
- **Level 1 (Grade Level):** Prefabricated storm shelter/safe room (20 person), elevator/stairwell, redundant restrooms, men's/women's showers, break room, lounge
- **Level 2 (Secure NOC):** NOC (~2,060 SF), private NOC area
- **Level 3 (Tour Route):** Secure tour route with internal windows into critical areas, weather-protected balconies (north/south) for equipment yard views, accessible to security and technical operations staff for routine site walks
- **Roof Access:** Weather-protected access via elevator/stairwell; storm-rated SS debris screen; protected roof-mounted equipment

---

### **RENEWABLE ENERGY & UTILITIES**
- **Solar:** Adjacent ~16.8 MW solar array (owned separately, behind-the-meter connection to 13.8 kV common bus)
- **Primary Utility Service:** Owner-constructed 161 kV substation with 2 × 50 MVA transformers (161kV/13.8kV, N+1 redundancy)
  - Dual redundant 161 kV transmission line feeds
  - All power transformed to 13.8 kV common bus (US standard voltage for data centers)
- **Water:** Municipal or well (domestic use only, ~500-1,000 gal/day)
- **Sewer:** Municipal or septic (domestic wastewater)
- **Natural Gas:** Utility service for house generators (backup power to non-critical areas)
- **[TBD] OPTIONAL Micro-Turbine Natural Gas Generators:** For Oklahoma SB 480 qualification (budget in Solar/BESS CAPEX, not Data Center)
- **Fiber:** Dual diverse entries  [CRITICAL PRIORITY - Must confirm physically diverse paths and carrier agreements before project proceeds]

---

### **FIRE PROTECTION & LIFE SAFETY**
- **Data Halls:** Zoned preaction sprinkler system with VESDA early warning detection
- **Cabinet Suppression:** Integrated fire suppression in DDC cabinets
- **E-Houses:** Clean agent suppression (Novec 1230 or FM-200) in E-Houses
- **LV Transformer Yard:** Portable fire extinguishers (Class C electrical) at outdoor transformer pads
- **Detection:** VESDA (Very Early Smoke Detection Apparatus) in data halls
- **Egress:** 2 minimum exits per data hall
- **Emergency Lighting:** 90-minute battery backup
- **NFPA Compliance:** NFPA 72, 75, 76, 2001, 101; IBC 2021

---

### **PHASING STRATEGY**

4-phase modular buildout using 6MW IT blocks:

| Phase | IT Load | Design PUE | Facility Load | Generators (3.6 MW) | Chillers (X MW) |
| ----- | ------- | ---------- | ------------- | ------------------- | --------------- |
| **1** | 6 MW    | 1.6        | 9.6 MW        | 4 (N+1)             | x               |
| **2** | 12 MW   | 1.6        | 19.2 MW       | 8 (N+1)             | x               |
| **3** | 18 MW   | 1.6        | 28.8 MW       | 12 (N+1)            | x               |
| **4** | 24 MW   | 1.6        | 38.4 MW       | 16 (N+1)            | x               |
<!-- @benton update this table -->
**Notes:**
- PUE 1.6 for electrical sizing (Oklahoma heat waves + overhead).


---

## KEY DESIGN DECISIONS

### **Why 6MW Block Architecture**
- **Simplified Redundancy:** N+1 at the block level (3 running + 1 backup per block) is straightforward to understand, procure equipment for, install, commission, operate, and maintain compared to facility-wide generator sharing.
- **Modular Growth:** Enables customer-driven expansion without overbuilding infrastructure. Each 6MW block is a self-contained unit that can be commissioned independently based on customer demand.
- **Independent Operation:** Each block includes dedicated generators (4 × 3.6MW, N+1) and E-Houses (4 units), providing clear separation and simplified redundancy management.
- **Flexible Deployment:** Blocks can be added incrementally as contracts are signed, avoiding the risk of stranded capital in unused capacity.
- **Cost Optimization:** Capital expenditure scales linearly with revenue. Each block is repeatable and supports financial modeling. However, total facility costs are less impactful per MW as additional capacity is installed.
- **Risk Mitigation:** If a single block experiences issues, the other blocks continue operating independently, limiting exposure and simplifying troubleshooting.

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


---


**Next Steps:**
1. TBD

---

**Document Control:**
- **Source:** PGCIS Team
- **Date Updated:** November 7, 2025
- **Version:** v2.0
- **Key Updates:** Phase restructure to 6MW blocks (6/12/18/24 MW), 16×3.6MW generators (4 per block), 16 E-Houses (4 per block), MV switchboards added, PUE 1.6 for sizing (1.4 marketing), client-specific rack deployment approach
- **Corrections:**


**CAPEX Savings Note:**
- We've kept the sparkle of the high ceilings and raised walking track for customer tours and security... However, for cost savings, an overall reduction in building height to ~20ft would provide ample space for any type of adaptation (hot aisle containment, etc.). It would save on steel and concrete, if required.