
# BASIS OF DESIGN - CSI MASTERFORMAT
## Pryor Data Center - PACHYDERM GLOBAL
### Pryor, Oklahoma

**Document Status:** REVISION 02 - 345 kV Substation + 13.8 kV Distribution (US Standard Voltage)
**Prepared by:** PGCIS Team
**Date:** October 30, 2025 
**Purpose:** Comprehensive Basis of Design for Pryor Data Center organized by CSI Master Format

---

## EXECUTIVE SUMMARY

### **FACILITY OVERVIEW**
- **IT Capacity:** 4-phase buildout to 24 MW ultimate capacity
  - Phase 1: 3 MW (30 racks @ 100 kW, D2C anchor tenant)
  - Phase 2: 6 MW (100 racks mixed density, add customer diversity)
  - Phase 3: 15 MW (260 racks total, commission second data hall)
  - Phase 4: 24 MW (280 racks, full densification)
- **White Space:** 20,000 SF total (two 10,000 SF data halls: DH-W and DH-E)
  - Phase 1-2: DH-W only (up to 140 racks capacity)
  - Phase 3+: Both halls operational (280 racks total capacity)
- **Power Density:** Scales from 300 W/SF (Phase 1) to 1,200 W/SF (Phase 4)
- **Rack Capacity:** 140 racks per hall maximum (280 total facility)
- **Availability:** Tier III (N+1 IT UPS with MV dual-ring path redundancy, N+1 mechanical, concurrent maintainability)
- **Target PUE:** 1.35 (Phase 1), 1.20-1.25 (Phase 4, optimized at scale)
- **Target WUE:** <0.5 L/kWh (air-cooled chillers, zero water consumption)
- **Site:** Pryor, Oklahoma (Tornado Alley - FM 1-150 protection)
- **Strategic Location:** **4 miles from Google's us-central2 data center campus** - enables direct fiber interconnect for AI/ML hybrid cloud workloads and inference.
- **Key Differentiators:**
  - Google Cloud proximity (sub-millisecond latency, eliminate data egress costs)
  - Customer-owned 345 kV substation with 13.8 kV distribution
  - D2C liquid cooling ready from day 1

---

### **ELECTRICAL SYSTEMS**
- **Primary Utility Service:** Customer-owned 345 kV substation
  - **345 kV Transmission:** Direct connection to utility transmission system
  - **Substation Transformers:** 2 × 25 MVA, 345kV/13.8kV (N+1 redundancy - either can carry full load)
- **13.8 kV Common Bus:** Single voltage platform for utility, solar, BESS, generators, data center (US standard voltage)
- **MV Distribution:** 13.8 kV dual-ring topology (Ring A + Ring B) via 8 RMUs
- **Generators:** Scalable N+1 diesel generators @ 13.8 kV, Tier 4 Final
  - Phase 1: 2 × 4.0 MW (N+1 for 4.5 MW facility load)
  - Phase 2: 3 × 4.0 MW total (N+1 for 9 MW facility load, add 1 unit)
  - Phase 3: 5 × 4.0 MW total (N+1 for 15-18 MW facility load, add 2 units)
  - Phase 4: 7 × 4.0 MW total (N+1 for 24-30 MW facility load, add 2 units)
  - Fuel: ~2,000 gal belly tanks per unit connected via common manifold to centralized bulk fuel storage (24-hour runtime with redundant fuel contracts)
- **Transformers:** Scalable 13.8 kV/480V oil-filled transformers, N+1 with concurrent maintainability
  - Phase 1: 2 × 3,500 kVA (N+1 for 4.5 MW facility load)
  - Phase 2: 3 × 3,500 kVA total (N+1 for 9 MW facility load, add 1 unit)
  - Phase 3: 6 × 3,500 kVA total (N+1 for 15-18 MW facility load, add 3 units)
  - Phase 4: 8 × 3,500 kVA total (N+1 for 24-30 MW facility load, add 2 units)
- **IT UPS:** N+1 modular architecture (path redundancy from self-healing MV dual-ring)
  - Phase 1: 4 × 1,250 kVA modules (N+1 for 3 MW IT load @ 80% loading)
  - Phase 2: 7 × 1,250 kVA modules total (N+1 for 6 MW IT load, add 3 units)
  - Phase 3: 16 × 1,250 kVA modules total (N+1 for 15 MW IT load, add 9 units)
  - Phase 4: 25 × 1,250 kVA modules total (N+1 for 24 MW IT load, add 9 units)
  - Battery: 5-minute runtime maximum (allows for MV generator sync to bus, even two attempts)
  - **Redundancy Philosophy:** 13.8 kV dual-ring provides path redundancy via self-healing SCADA switching; N+1 UPS provides component redundancy
- **Mechanical UPS:** Phase 1: 8 × 250 kW; Phase 2: 20 × 250 kW (N+1 for pumps/fans)
- **LV Distribution:** Dual switchboards (SWBD-A/B) fed from different MV ring segments
- **Cabinet Power:** Dual PDUs fed from different 480V distribution panels (sized per customer rack density)
- **Electrical Enclosures:** Prefabricated PDMs with LV switchboards, UPS, MV gear
- **MV Distribution:** 8 RMUs (13.8 kV, 630A), dual-ring topology
- **Non-Critical Building Power (Separate System):**
  - House generators: 2 × 250-350 kW natural gas (N+1 redundancy)
  - Serves: offices, bathrooms, hallways, SCR, SCB, loading dock, NOC, gym, storm shelter
  - Portable UPS: ~20-30 units for IT equipment ride-through in non-critical areas
- **Electrical Code:** NEC 2023, Oklahoma amendments

---

### **MECHANICAL SYSTEMS**
- **Cooling Strategy:** Phased deployment optimized for AI/ML workload growth
- **Phase 1 (D2C Liquid Cooling Only - 3 MW):**
  - IT Load: 3,000 kW (30 racks @ 100 kW each, AI training anchor tenant)
  - D2C Cooling: 4 × 1,500 kW air-cooled chillers (Loop 3, N+1 redundancy)
  - CDUs: 30 units (1 per rack, 100+ kW capacity each)
  - RDHx: 30 rear-door heat exchangers (captures residual heat not cooled by D2C)
  - Fluid: 25% propylene glycol mix, 55°F supply, single loop serves both CDU + RDHx
  - Load split: ~80% D2C (2,400 kW), ~20% RDHx (600 kW)
  - Chiller utilization: 67% per operating chiller in N+1 configuration (optimal efficiency range)
  - Building HVAC: Separate package units for offices/support spaces
- **Phase 2 (Add Air Cooling - 6 MW):**
  - Add customer diversity: AI inference, enterprise, specialty compute
  - Add air cooling plant: 3 × 1,500 kW chillers (Loops 1+2, N+1 for 1,800 kW load)
  - D2C expansion: Add 2 chillers to Loop 3 (6 × 1,500 kW total, N+1 for 4,200 kW load)
  - Total cooling: Two independent plants (air and D2C separated)
  - Air cooling load: ~1,800 kW; D2C cooling load: ~4,200 kW
- **Phase 3 (Second Data Hall - 15 MW):**
  - Commission DH-E with mixed customer types
  - Air cooling load: ~4,500 kW → Scale to 5 × 1,500 kW chillers total (Loops 1+2, N+1)
  - D2C cooling load: ~10,500 kW → Scale to 9 × 1,500 kW chillers total (Loop 3, N+1)
- **Phase 4 (Full Build - 24 MW):**
  - Air cooling load: ~7,200 kW → Final: 6 × 1,500 kW chillers (Loops 1+2, N+1)
  - D2C cooling load: ~16,800 kW → Final: 14 × 1,500 kW chillers (Loop 3, N+1)
- **Free Cooling:** ~3,500-4,000 hours/year (Oklahoma climate)
- **Zero Water Strategy:** No evaporative cooling, closed-loop glycol only
- **Cooling Separation Rationale:** D2C loads swing violently (GPU workloads 0-100% in seconds), air loads are stable - separate plants prevent control instability
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
- **PDMs:** Power Delivery Modules located outside in electrical equipment yard

**Multi-Level Central Spine (4 Levels):**
- **Level 1:** Prefabricated storm shelter/safe room (20 person), elevator/stairwell, redundant restrooms, men's/women's showers, break room, lounge, gaming area (TBD)
- **Level 2 (Secure NOC):** NOC (~2,060 SF), private NOC area
- **Level 3 (Fitness/Tour Route):** Gym/fitness center, secure tour route with internal windows into critical areas, weather-protected balconies (north/south) for equipment yard views, accessible to security and technical operations staff for routine site walks
- **Roof Level:** Weather-protected access via elevator/stairwell; storm-rated SS debris screen; protected roof-mounted equipment

---

### **RENEWABLE ENERGY & UTILITIES**
- **Solar:** Adjacent ~12 MW solar array (owned separately)
- **BESS:** Battery Energy Storage System (owned separately, separate from UPS)
- **Primary Utility Service:** Owner-constructed 345 kV substation with 2 × 25 MVA transformers (345kV/13.8kV, N+1 redundancy)
  - Dual redundant 345 kV transmission line feeds
  - All power transformed to 13.8 kV common bus (US standard voltage for data centers and renewables)
- **Water:** Municipal or well (domestic use only, ~500-1,000 gal/day)
- **Sewer:** Municipal or septic (domestic wastewater)
- **Natural Gas:** Utility service for house generators (backup power to non-critical areas)
- **[TBD] OPTIONAL Micro-Turbine Natural Gas Generators:** For Oklahoma SB 480 qualification (budget in Solar/BESS CAPEX, not Data Center)
- **Fiber:** Dual diverse entries via underground ductbank {To be Confirmed}

---

### **FIRE PROTECTION & LIFE SAFETY**
- **Data Halls:** Zoned preaction sprinkler system with VESDA early warning detection
- **Cabinet Suppression:** Integrated fire suppression in DDC cabinets
- **Prefabricated PDMs:** Clean agent or other suppression per NFPA standards in PDM enclosures housing UPS, switchboards, MV gear
- **Detection:** VESDA (Very Early Smoke Detection Apparatus) in data halls
- **Egress:** 2 minimum exits per data hall, 36" doors (44" preferred)
- **Emergency Lighting:** 90-minute battery backup
- **NFPA Compliance:** NFPA 72, 75, 76, 2001, 101; IBC 2021

---

### **PHASING STRATEGY**

4-phase customer-driven buildout optimized for AI/ML workload growth:

| Phase | IT MW | Total Racks | Active Halls | Primary Strategy                   |
| ----- | ----- | ----------- | ------------ | ---------------------------------- |
| **1** | 3     | ~30         | DH-W only    | D2C anchor tenant (AI Training)    |
| **2** | 6     | ~100        | DH-W only    | Add customer diversity (air + D2C) |
| **3** | 15    | ~260        | DH-W + DH-E  | Commission second data hall        |
| **4** | 24    | ~280        | DH-W + DH-E  | Full densification                 |

**Phase 1 Strategy:** D2C liquid cooling only (no air cooling plant) = lower CAPEX, proves high-density capability with AI training anchor tenant.

**Detailed phasing specifications:** See Electrical BOD (Div 26) and Mechanical BOD (Div 23).

---

## KEY DESIGN DECISIONS

### **Why N+1 IT UPS with MV Dual-Ring (Not Traditional 2N UPS)**
- **Path redundancy** provided by 13.8 kV self-healing dual-ring MV distribution
- **Component redundancy** provided by N+1 modular UPS architecture
- IT equipment retains dual PDUs fed from different 480V panels (SWBD-A/B on different MV ring segments)
- **Advantages:** Lower capital cost (~40-50% fewer UPS modules), higher efficiency, simplified maintenance
- **Equivalent reliability:** MV dual-ring switching provides path diversity; N+1 UPS provides component failure tolerance

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

### **Why D2C Liquid Cooling with RDHx (Not Air Cooling Alone)**
- **D2C cold plates capture 70-90% of heat** directly from CPUs and GPUs
- **RDHx captures residual 10-30%** from power supplies, NICs, storage, and VRMs
- **Single fluid loop serves both:** Simplified infrastructure (25% propylene glycol, 12-15°C supply)
- **Required for high density:** Enables 100+ kW/rack densities that air cooling cannot achieve
- **Phase 1 enabler:** Proves liquid cooling capability to attract AI training anchor tenant
- **Better efficiency:** D2C achieves higher COP than traditional air cooling at high densities


---

**Tags:** #pryor-data-center #basis-of-design #csi-masterformat #tier-iii #tilt-up-construction

**Next Steps:**
1. TBD

---

**Document Control:**
- **Source:** Pryor_Bod_EVS_Rev01.md
- **Date Updated:** October 29, 2025
- **Prepared by:** EVS / PGCIS Team
- **Corrections:** Tilt-up construction, utility voltage options, mechanical yard sizing
