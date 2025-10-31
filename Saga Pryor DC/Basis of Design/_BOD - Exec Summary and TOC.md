
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
- **IT Capacity:** 3 MW Phase 1 (30 cabinets @ 100 kW); 12 MW Phase 2 (30 cabinets @ 400 kW);  [TBD] - Follow-on Phases up to 12 MW
- **White Space:** 20,000 SF total all Phases (two 10,000 SF data halls); Phase 1 & 2 inside first 10,000 SF Data Hall (DH-E - East End of the Building)
- **Power Density:** Phase 1: 300 W/SF; Phase 2: 1,200 W/SF; up to 1,200 W/SF in Data Hall W (DH-W)
- **Cabinet Configuration:** Master Planned 30 × DDC S-Series cabinets (52U, 36" wide)
- **Availability:** Tier III (N+1 IT UPS with MV dual-ring path redundancy, N+1 mechanical, concurrent maintainability)
- **Target PUE:** 1.35 (Phase 1), 1.25 (Phase 2)
- **Target WUE:** <0.5 L/kWh (air-cooled, zero water consumption)
- **Site:** Pryor, Oklahoma (Tornado Alley - FM 1-150 protection)
- **Key Differentiator:** Customer-owned 345 kV substation with 13.8 kV distribution and true microgrid capability

---

### **ELECTRICAL SYSTEMS**
- **Primary Utility Service:** Customer-owned 345 kV substation
  - **345 kV Transmission:** Direct connection to utility transmission system
  - **Substation Transformers:** 2 × 25 MVA, 345kV/13.8kV (N+1 redundancy - either can carry full load)
- **13.8 kV Common Bus:** Single voltage platform for utility, solar, BESS, generators, data center (US standard voltage)
- **MV Distribution:** 13.8 kV dual-ring topology (Ring A + Ring B) via 6 RMUs
- **Generators:** 6 × 4.0 MW @ 13.8 kV, diesel, Tier 4 Final (N+1)
  - Phase 1: 3 units; Phase 2: +3 units
  - Fuel: ~2,000 gal belly tanks per unit connected via common manifold to centralized bulk fuel storage (24-hour runtime with redundant fuel contracts)
- **Transformers:** 8 × 3,500 kVA (13.8 kV/480V) oil-filled, N+1 with concurrent maintainability
  - Phase 1: 3 units; Phase 2: +5 units
- **IT UPS:** N+1 modular architecture (path redundancy from self-healing MV dual-ring)
  - Phase 1: ~5 × 1,250 kVA modules
  - Phase 2: ~13 × 1,250 kVA modules (add ~8)
  - Battery: 5-minute runtime maximum (allows for MV generator sync to bus, even two attempts)
  - **Redundancy Philosophy:** 13.8 kV dual-ring provides path redundancy via self-healing SCADA switching; N+1 UPS provides component redundancy
- **Mechanical UPS:** Phase 1: 8 × 250 kW; Phase 2: 20 × 250 kW (N+1 for pumps/fans)
- **LV Distribution:** Dual switchboards (SWBD-A/B) fed from different MV ring segments
- **Cabinet Power:** Dual PDUs fed from different 480V distribution panels - Phase 1: 2 × 50 kW; Phase 2: 2 × 200 kW
- **Electrical Enclosures:** Prefabricated PDMs with LV switchboards, UPS, MV gear
- **MV Distribution:** 6 RMUs (13.8 kV, 630A), dual-ring topology
- **Non-Critical Building Power (Separate System):**
  - House generators: 2 × 250-350 kW natural gas (N+1 redundancy)
  - Serves: offices, bathrooms, hallways, SCR, SCB, loading dock, NOC, gym, storm shelter
  - Portable UPS: ~20-30 units for IT equipment ride-through in non-critical areas
- **Electrical Code:** NEC 2023, Oklahoma amendments

---

### **MECHANICAL SYSTEMS**
- **Cooling Strategy:** Phased deployment aligned with IT load growth
- **Phase 1 (Air Cooling Only):**
  - IT Load: 3,000 kW (30 cabinets @ 100 kW each)
  - Cabinet FCUs: 100 kW capacity each (dual coils: 50 kW Loop 1 + 50 kW Loop 2)
  - Chillers: 4 × 1,500 kW air-cooled (Loops 1+2 shared plant, N+1)
  - Supply temp: 7-10°C; COP: 3.8-4.2 (mechanical), 15-25 (free cooling)
- **Phase 2 (Air + D2C Cooling):**
  - IT Load: 12,000 kW (30 cabinets @ 400 kW: 100 kW air + 300 kW D2C)
  - Air cooling: Same 4 chillers (Loops 1+2, 3,000 kW load unchanged)
  - D2C cooling: 8 × 1,500 kW air-cooled chillers (Loop 3 independent, N+1)
  - CDUs: 60 × 300 kW units (2 per cabinet, A/B redundancy)
  - Supply temp: 25°C; COP: 5.0-5.5 (higher efficiency than air cooling)
- **Free Cooling:** ~3,500-4,000 hours/year (Oklahoma climate)
- **Zero Water Strategy:** No evaporative cooling, closed-loop glycol
- **Building HVAC:** RTUs for offices, NOC, support spaces
- **Mechanical Code:** IMC 2021, ASHRAE 90.1-2019

---

### **FACILITY CONSTRUCTION**
- **Structure:** Pre-cast concrete tilt-up construction (tornado-resistant)
- **Total Building:** 50,000 GSF
- **Configuration:** Two 10,000 SF data halls + 30,000 SF support spaces
- **Roofing:** FM 1-150 tornado-rated (150 mph winds, Class 4 hail); storm-rated stainless steel debris screen; protected roof equipment
- **Walls:** Tilt-up concrete panels (8-12" thick, reinforced for high wind loads)
- **Floor:** Slab-on-grade (raised floor: Not Applicable), sealed concrete with optional epoxy
- **Ceiling Height:** 28-30 ft clear in data halls
- **Containment:** Not Applicable (DDC cabinets provide integrated cooling)
- **Storm Shelter/Safe Room:** FEMA 361 compliant prefabricated module (EF5 protection), 20 person capacity, located on Level 1 adjacent to elevator
- **Security:** 
  - K-rated perimeter fence (8 ft height, 100 ft building standoff)
  - **Two property entrances:**
    - **Main entrance (NE corner):** Sally port vehicle trap with permanent manned visitor center
    - **Secondary entrance (NW side):** Emergency/construction access (normally unmanned, visible from loading dock SCB)
  - Mantrap entry, full MFA (card + biometric), CCTV with 90-day retention
- **Rationale for Tilt-Up:** Superior tornado resistance vs. PEMB, better thermal mass, lower insurance premiums

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

**Equipment Yards:**
- Electrical: ~100,000 SF (sized for 24 MW master plan)
- Mechanical: ~50,000 SF (sized for 12 chillers total)

---

### **RENEWABLE ENERGY & UTILITIES**
- **Solar:** Adjacent 8+ MW solar array (owned separately, behind-the-meter)
- **BESS:** Battery Energy Storage System (separate from UPS)
- **Primary Utility Service:** Owner-constructed 345 kV substation with 2 × 25 MVA transformers (345kV/13.8kV, 2N redundancy)
  - Dual redundant 345 kV transmission line feeds
  - All power transformed to 13.8 kV common bus (US standard voltage for data centers and renewables)
- **Water:** Municipal or well (domestic use only, ~500-1,000 gal/day)
- **Sewer:** Municipal or septic (domestic wastewater)
- **Natural Gas:** Utility service for house generators (backup power to non-critical areas)
- **[TBD] OPTIONAL Micro-Turbine Natural Gas Generators:** For Oklahoma SB 480 qualification (budget in Solar/BESS CAPEX, not Data Center)
- **Fiber:** Dual diverse entries via underground ductbank

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

### **COST SUMMARY**

| Phase | IT Capacity | Electrical Cost | Total Project Cost* |
|-------|-------------|-----------------|---------------------|
| Phase 1 | 3 MW | $14.3M | $34-41M |
| Phase 2 | +9 MW (12 MW total) | $22.3M | $27-34M |
| **Total** | **12 MW** | **$36.6M** | **$61-75M** |

*Total project includes civil, architectural, site work, MEP systems

**Cost per MW:**
- Phase 1: $11.3-13.7M per MW (includes full infrastructure)
- Phase 2: $3.0-3.8M per MW (incremental)
- Blended average: $5.1-6.3M per MW

**Phase 1 Electrical Breakdown:**
- Generators (3 × 4.0 MW @ 13.8 kV diesel): $4.5M
- House generators (2 × 300 kW natural gas): $0.1M
- Transformers (3 × 3,500 kVA, 13.8kV/480V): $0.5M
- RMUs, MV switchgear, cable (including dual-ring SCADA controls): $1.4M
- LV switchboards, distribution: $1.3M
- IT UPS (~5 × 1,250 kVA N+1 + batteries): $1.2M
- Mechanical UPS (8 × 250 kW): $0.8M
- Portable UPS (non-critical areas): $0.05M
- PDMs (2 units): $2.5M
- Installation, testing, commissioning: $2.0M

**Phase 2 Electrical Breakdown:**
- Generators (3 × 4.0 MW): $4.5M
- Transformers (5 × 3,500 kVA): $0.85M
- MV/LV distribution expansion: $1.5M
- IT UPS (~8 × 1,250 kVA N+1 + batteries): $1.8M
- Mechanical UPS (12 × 250 kW): $1.2M
- Chillers Loop 3 (8 × 1,500 kW): $6.0M
- CDUs (60 units): $3.0M
- Cabinet PDU upgrades: $0.45M
- Installation, testing, commissioning: $3.0M

**Note:** If utility provides 34.5 kV service, add ~$1.0-1.5M for two 34.5kV/13.8kV step-down transformers

---

### **DESIGN STANDARDS**
- **Redundancy:** 
  - **Path redundancy:** 13.8 kV dual-ring MV distribution with self-healing automated switching
  - **Component redundancy:** N+1 (IT UPS, generators, transformers, chillers)
  - **Cooling redundancy:** N+N (air cooling loops - Loop 1 + Loop 2 independent)
- **Concurrent Maintainability:** All systems serviceable without IT interruption
- **Zero Single Points of Failure:** From 345 kV utility to cabinet-level distribution
- **Uptime:** Tier III-equivalent (99.982% = 1.6 hours downtime/year)
- **Monitoring:** DCIM with BMS and EPMS integration

---

### **PHASING STRATEGY**

**Phase 1: Foundation Operations (3 MW)**
- Data Hall 1 operational: 30 cabinets @ 100 kW each
- Air cooling: Loops 1+2 (4 chillers, N+1)
- Power: 3 generators, 3 transformers, ~5 IT UPS modules, 8 mechanical UPS
- Data Hall 2: Built as powered shell
- Timeline: [ROM] 18-24 months
- Cost: [ROM] $34-41M

**Phase 2: High-Density Expansion (12 MW)**
- Same 30 cabinets: Upgrade to 400 kW (100 kW air + 300 kW D2C)
- D2C cooling: Loop 3 (8 chillers, 60 CDUs, independent from air cooling)
- Power: Add 3 generators, 5 transformers, ~8 IT UPS modules, 12 mechanical UPS
- Zero-downtime implementation
- Timeline: [ROM] 12-15 months
- Cost: [ROM] $27-34M

---

## CSI MASTERFORMAT OUTLINE

### **PROCUREMENT AND CONTRACTING REQUIREMENTS GROUP**

#### **Division 00 – Procurement and Contracting Requirements**

See: [[Saga Pryor DC/Basis of Design/Erik_BOD_Updated/0BOD - Procurement & Contracting (CSI Div 00)]]

**Summary:**
- **Delivery Method:** Design-Build (DB) with Guaranteed Maximum Price (GMP)
- **Procurement Strategy:** Phased RFP process with early long-lead equipment orders (switchgear, UPS, generators, chillers)
- **Vendor Selection:** Tier 1 vendors only; pre-qualification based on data center experience, financial stability, service network
- **Contract Structure:** GMP with performance guarantees (PUE ≤ 1.4, Tier III uptime, 3 MW capacity)
- **Risk Allocation:** Design-builder assumes design/construction risk; owner retains site conditions and utility coordination
- **Schedule:** 24-month fast-track timeline from design kickoff to final completion
- **Budget:** ~$34-41M total project cost (3 MW Phase 1); $11.3-13.7M per MW
- **Quality Assurance:** Independent CxA, factory acceptance tests, third-party material testing

---

### **SPECIFICATIONS GROUP**

#### **GENERAL REQUIREMENTS SUBGROUP**

**Division 01 – General Requirements**

See: [[Saga Pryor DC/Basis of Design/Erik_BOD_Updated/1BOD - General Requirements (CSI Div 01)]]

**Summary:**
- **Project Coordination:** BIM-based design (LOD 400); weekly OAC meetings; design-assist from key subcontractors
- **Submittals:** Tiered review process (Tier 1: switchgear, UPS, generators, chillers require owner + engineer + CxA review)
- **Quality Control:** 3rd-party testing for concrete, soil, fireproofing, electrical thermography; NETA acceptance testing
- **Commissioning:** ASHRAE Guideline 0 + Uptime Tier III; independent CxA; Integrated Systems Test (IST) with simulated failures
- **Training:** 40+ hours hands-on training across all critical systems (electrical, mechanical, BMS, fire, security)
- **Closeout:** As-built drawings (CAD/BIM + PDF), O&M manuals (hard copy + digital), warranty register, test reports
- **Testing:** Load bank testing for generators (100% load, 4 hours) and UPS (100% load, 2 hours)
- **Regulatory:** Building permits, utility coordination, environmental permits (SWPPP, SPCC), code compliance (IBC 2018/2021, NEC 2020/2023)

---

#### **FACILITY CONSTRUCTION SUBGROUP**

See: [[Saga Pryor DC/Basis of Design/Erik_BOD_Updated/2BOD - Facility Construction (CSI Divs 02-14)]]

**Summary:**
- **Division 02 (Existing Conditions):** Greenfield site; clearing, grubbing, erosion control per SWPPP
- **Division 03 (Concrete):** 
  - Foundation: Spread footings below frost line (18-24"); bearing capacity TBD per geotech
  - Data hall slab: 6-8" reinforced concrete, 4,000 PSI, FF 50 / FL 40 flatness, densifier/sealer finish
  - **AI rack floor load:** 750 PSF sustained (supports 3,500 lb racks like NVIDIA GB200 NVL72)
  - Equipment pads: Isolated pads for chillers/generators; oil containment for transformers
- **Division 04 (Masonry):** Not applicable (precast tilt-up construction)
- **Division 05 (Metals):** Clear-span steel joists/beams (28-30 ft height); seismic IBC Category B; cable tray trapeze hangers
- **Division 07 (Thermal/Moisture Protection):**
  - **Precast tilt-up walls:** 8-10" panels with R-19 insulation sandwich; tornado resistance (EF3+); 50+ year lifespan
  - **FM 1-150 roof:** 150 mph wind, Class 4 hail, fire-rated; TPO/EPDM fully adhered; storm-rated debris protection; premium: ~$500-800K
  - **Cost premium:** Precast ~$1.3-2.0M more than PEMB; offset by insurance savings ($200-300K/year)
- **Division 08 (Openings):** Security mantrap; data hall doors (at least two 10 ft H × 8 ft W double doors per hall for large equipment, other doors 4 ft single; card + biometric); loading dock; no windows in data halls
- **Division 09 (Finishes):** Sealed concrete floors, painted gypsum walls, exposed MEP ceiling in data halls
- **Division 13 (Special Construction):**
  - **FEMA 361 storm shelter/safe room:** Prefabricated module, 20 person capacity, located Level 1 adjacent to elevator, EF5 protection
- **Division 14 (Conveying Equipment):**
  - **Elevator:** 4-stop (Level 1/2/3/Roof), 2,500-3,500 lb capacity, hydraulic or traction, weather-protected roof access with overhang

---

#### **FACILITY SERVICES SUBGROUP**

**Division 21 – Fire Suppression**

See: [[Saga Pryor DC/Basis of Design/Erik_BOD_Updated/3BOD - Fire Suppression (CSI Div 21)]]

**Summary:**
- **Data halls:** Pre-action sprinkler (NFPA 13) with VESDA early warning detection
- **Prefabricated PDMs (UPS/Electrical):** Integrated clean agent suppression (FM-200/Novec 1230) in PDM enclosures per NFPA 2001
  - UPS systems housed in outdoor prefabricated PDMs, not interior rooms
  - Maximizes building interior space for IT equipment
  - Factory-tested fire suppression systems for rapid deployment
- **Electrical/Mechanical rooms (interior):** Dry-pipe sprinkler or clean agent (if required)
- **Support spaces:** Wet-pipe sprinkler (offices, NOC, corridors)
- **Detection:** VESDA aspirating smoke detection in data halls; conventional smoke/heat in support spaces and PDMs
- **Suppression integration:** BMS lockouts (HVAC shutdown, damper closure) on alarm
- **Testing:** Pre-action system acceptance test, clean agent discharge test (simulated), PDM integrated suppression verification

---

**Division 22 – Plumbing**

See: [[Saga Pryor DC/Basis of Design/Erik_BOD_Updated/4BOD - Plumbing (CSI Div 22)]]

**Summary:**
- **Domestic water:** Municipal or well supply; 500-1,000 GPD usage (restrooms, kitchen, emergency eyewash)
- **Sanitary sewer:** Municipal connection or on-site septic (if required)
- **Chilled water:** Closed-loop glycol systems (Loops 1, 2, 3); no cross-connection with domestic water
- **Water efficiency:** Low-flow fixtures (1.5 GPM faucets, 1.28 GPF toilets); ADA-compliant
- **Backflow prevention:** RPZ backflow preventers on all water service connections
- **Emergency fixtures:** Eyewash/shower stations in electrical and mechanical rooms
- **Leak detection:** Under-floor leak detection in data halls (if applicable); BMS-monitored

---

**Division 23 – HVAC**

See: [[Saga Pryor DC/Basis of Design/Erik_BOD_Updated/5BOD - HVAC (CSI Div 23)]]

**Summary:**
- **Phase 1 (Air Cooling):**
  - IT load: 3,000 kW (30 cabinets @ 100 kW)
  - Cabinet FCUs: 100 kW capacity each (dual coils: 50 kW Loop 1 + 50 kW Loop 2)
  - Chillers: 4 × 1,500 kW air-cooled (N+1 redundancy, shared plant for Loops 1+2)
  - Supply temp: 7-10°C; COP: 3.8-4.2 (mechanical), 15-25 (free cooling)
  - Free cooling: ~3,500-4,000 hours/year (Oklahoma climate)
- **Phase 2 (Air + D2C Cooling):**
  - IT load: 12,000 kW (30 cabinets @ 400 kW: 100 kW air + 300 kW D2C per cabinet)
  - Air cooling: Same 4 chillers (Loops 1+2, 3,000 kW unchanged)
  - D2C cooling: 8 × 1,500 kW air-cooled chillers (Loop 3 independent, N+1)
  - CDUs: 60 × 300 kW units (2 per cabinet for A/B redundancy)
  - Supply temp: 25°C; COP: 5.0-5.5 (higher efficiency than air cooling)
- **Zero water strategy:** No evaporative cooling; closed-loop glycol only
- **Building HVAC:** Rooftop units (RTUs) for offices, NOC, support spaces
- **Containment:** Not Applicable (DDC cabinets provide integrated cooling)
- **Controls:** BMS integration with DCIM; temperature/humidity monitoring; alarm escalation

---

**Division 25 – Integrated Automation**

See: [[Saga Pryor DC/Basis of Design/Erik_BOD_Updated/6BOD - Integrated Automation (CSI Div 25)]]

**Summary:**
- **Building Management System (BMS):** Schneider Electric EcoStruxure or Johnson Controls Metasys
- **Electrical Power Monitoring System (EPMS):** Schneider Electric PowerLogic or Vertiv Trellis
- **Data Center Infrastructure Management (DCIM):** Schneider StruxureWare or Nlyte/Sunbird
- **Integration:** BACnet and Modbus protocols; unified dashboard for mechanical, electrical, security
- **Monitoring:** Real-time PUE, temperature/humidity, power consumption (cabinet-level metering)
- **Alarms:** Multi-tier escalation (SMS, email, SNMP traps); integration with NOC monitoring
- **Trending:** Historical data retention (5+ years); energy analytics and capacity planning
- **Remote access:** Secure VPN or cloud-based access for remote troubleshooting

---

**Division 26 – Electrical**

See: [[Saga Pryor DC/Basis of Design/Erik_BOD_Updated/7BOD - Electrical (CSI Div 26)]]

**Summary:**
- **Utility service:** 345 kV transmission → 2 × 25 MVA transformers (345kV/13.8kV) → 13.8 kV common bus
- **MV distribution:** 13.8 kV self-healing dual-ring topology via 6 RMUs (Ring A + Ring B) with automated SCADA switching
- **Generators:** 6 × 4.0 MW @ 13.8 kV diesel (N+1); Tier 4 Final emissions; ~2,000 gal belly tanks + central bulk fuel
- **Transformers:** 8 × 3,500 kVA (13.8 kV/480V) oil-filled (N+1 with concurrent maintainability)
- **IT UPS:** N+1 modular architecture; Phase 1: ~5 × 1,250 kVA modules; Phase 2: ~13 × 1,250 kVA modules (add ~8)
- **UPS batteries:** 5-minute runtime maximum; Lithium-ion preferred (longer life, smaller footprint)
- **Mechanical UPS:** N+1 for pumps/fans; Phase 1: 8 × 250 kW; Phase 2: 20 × 250 kW
- **LV distribution:** Dual switchboards (SWBD-A/B) fed from different MV ring segments
- **Cabinet power:** Dual PDUs fed from different 480V distribution panels; Phase 1: 2 × 50 kW; Phase 2: 2 × 200 kW
- **Prefabricated PDMs:** 2 units housing LV switchboards, UPS, MV gear for rapid deployment
- **Code compliance:** NEC 2023; arc flash studies; NETA acceptance testing

---

**Division 27 – Communications**

See: [[Saga Pryor DC/Basis of Design/Erik_BOD_Updated/8BOD - Communications (CSI Div 27)]]

**Summary:**
- **Fiber entrance:** 2 × geographically diverse MPOEs (Main Points of Entry)
- **Meet-me rooms (MMRs):** 2 × carrier-neutral cross-connect rooms
- **Pathways:** Underground ductbank to property line; 4" conduits with pull rope; fiber hand-off terminations
- **Backbone cabling:** Single-mode fiber (OS2) between MMRs and data halls
- **Horizontal cabling:** Overhead cable tray; separation from power cables per TIA-942
- **Grounding:** Telecommunication grounding busbar (TGB); bonding to building ground grid
- **Labeling:** Cable IDs at 10 ft intervals, both termination points, all junction boxes
- **Testing:** Fiber OTDR testing; certification reports for all fiber runs

---

**Division 28 – Electronic Safety and Security**

See: [[Saga Pryor DC/Basis of Design/Erik_BOD_Updated/9BOD - Electronic Safety and Security (CSI Div 28)]]

**Summary:**
- **Perimeter security:** K-rated fence (8 ft height), dual gates with card readers, anti-ram barriers
- **Access control:** HID or Lenel system; card + biometric (two-factor) for data halls; badge management
- **CCTV:** 24/7 recording, 90-day retention; cameras at all doors, equipment yards, data halls; Axis or Hanwha
- **Intrusion detection:** Perimeter sensors, door contacts; monitored by NOC or security service
- **Visitor management:** Log-in/log-out kiosk; escort required in data halls
- **Mantrap:** Double-door airlock at main entry; outer door must close before inner opens; fire override
- **Integration:** Access control and CCTV integrated with BMS; alarm escalation to NOC
- **Cybersecurity:** Segmented networks (IT, OT, security); firewall between BMS and corporate network

---

#### **SITE AND INFRASTRUCTURE SUBGROUP**

**Divisions 31-32 – Site and Infrastructure**

See: [[Saga Pryor DC/Basis of Design/Erik_BOD_Updated/3BOD - Site & Infrastructure (CSI Divs 31-32)]]

**Summary:**
- **Site area:** 20+ acres total; 50,000 GSF building footprint
- **Grading:** Cut/fill balance; positive drainage away from building; 2% min slope
- **Stormwater management:** Detention pond (100-year storm); SWPPP compliance (>1 acre disturbance); Oklahoma DEQ permit
- **Paving:** Reinforced concrete (equipment yards, loading dock); asphalt (parking, drives); 8" base course
- **Utilities:**
  - Water: 6" main from municipal or well
  - Sanitary: 8" gravity sewer to municipal or on-site septic
  - Fiber: Dual diverse underground duct bank entries (4" conduits)
- **Equipment yards:**
  - Electrical: ~100,000 SF (generators, transformers, switchgear); sized for 24 MW master plan
  - Mechanical: ~50,000 SF (chillers, cooling towers, pumps); sized for 12 chillers total
- **Fencing:** 8 ft K-rated perimeter; controlled access gates
- **Landscaping:** Drought-tolerant native species; drip irrigation; minimal turf area
- **Site lighting:** LED (100%); photocell/time clock control; dark-sky compliance
- **Fuel storage:** ~2,000 gal belly tanks per generator connected via common manifold to centralized bulk fuel tank farm (~12,000 gal capacity for 24-hour runtime); redundant fuel service contracts; SPCC compliance
- **Fire access:** 20 ft clear width; fire hydrants @ 500 ft spacing; fire lane striping

---

## EQUIPMENT SUMMARY

| Equipment | Phase 1 | Phase 2 Add | Total | Unit Size |
|-----------|---------|-------------|-------|-----------|
| **Generators** | 3 | +3 | 6 | 4.0 MW @ 13.8 kV |
| **Transformers (13.8kV/480V)** | 3 | +5 | 8 | 3,500 kVA |
| **Utility Xfmrs (if 34.5kV)** | 2 | 0 | 2 | ~20 MVA (34.5kV/13.8kV) |
| **RMUs** | 6 | 0 | 6 | 13.8 kV, 630A |
| **IT UPS** | ~5 | ~8 | ~13 | 1,250 kVA |
| **Mech UPS** | 8 | +12 | 20 | 250 kW |
| **Chillers (Loops 1+2)** | 4 | 0 | 4 | 1,500 kW |
| **Chillers (Loop 3)** | 0 | 8 | 8 | 1,500 kW |
| **CDUs** | 0 | 60 | 60 | 300 kW each |
| **Cabinets** | 30 | 0 | 30 | DDC S-Series |
| **PDUs** | 60 | upgrade | 60 | 50 kW → 200 kW |

---

## KEY DESIGN DECISIONS

### **Why Tilt-Up Concrete (Not PEMB)**
- **Tornado resistance:** Pre-cast concrete withstands EF3-EF5 events better than steel framing
- **Insurance:** 30-40% lower premiums vs. PEMB in Tornado Alley
- **Thermal mass:** Better temperature stability, reduces HVAC cycling
- **Cost:** ~$15-25/SF premium over PEMB, justified by insurance savings and resilience

### **Utility Voltage Options**
- **13.8 kV or 12.47 kV:** Direct connection to 13.8 kV generators and MV distribution (no step-down required)
- **34.5 kV:** Requires two 34.5kV/13.8kV step-down transformers (~20 MVA each, N-1 redundancy)
  - Cost adder: ~$1.0-1.5M
  - Benefits: Often lower utility rates, better stability on high-voltage transmission

### **Why 13.8 kV Generators (Not 480V)**
- Standard product availability (3-5 MW range)
- Cable sizing: 13.8 kV reduces current by 29×
  - 4 MW @ 480V = 8,333 A (requires 6 × 500 kcmil/phase)
  - 4 MW @ 13.8 kV = 290 A (requires 1 × 2/0/phase)
- Easier paralleling and lower I²R losses

### **Why Separate Loop 3 (D2C Cooling)**
- **Air cooling (Loops 1+2):** Predictable, stable loads (±10% variation)
- **D2C cooling (Loop 3):** Violent load swings (0-100% in seconds)
- **Problems if mixed:** Control hunting, reduced efficiency, accelerated wear
- **Benefits of separation:** Optimized controls, clear contractor boundaries, independent maintenance, fault isolation

### **Why N+1 IT UPS with MV Dual-Ring (Not Traditional 2N UPS)**
- **Path redundancy** provided by 13.8 kV self-healing dual-ring MV distribution
- **Component redundancy** provided by N+1 modular UPS architecture
- IT equipment retains dual PDUs fed from different 480V panels (SWBD-A/B on different MV ring segments)
- **Advantages:** Lower capital cost (~40-50% fewer UPS modules), higher efficiency, simplified maintenance
- **Equivalent reliability:** MV dual-ring switching provides path diversity; N+1 UPS provides component failure tolerance

### **Why Slab-on-Grade (No Raised Floor)**
- Cost savings (~$150K+)
- Eliminates failure modes and underfloor plenum complications
- Better seismic performance
- Overhead cable distribution provides equivalent flexibility

---

**Tags:** #pryor-data-center #basis-of-design #csi-masterformat #tier-iii #tilt-up-construction

**Next Steps:**
1. Confirm utility voltage (13.8 kV, 12.47 kV, or 34.5 kV)
2. Review detailed technical specifications by CSI division
3. Validate cost estimates with vendors
4. Begin detailed engineering design
5. Finalize equipment procurement schedule

---

**Document Control:**
- **Source:** Pryor_Bod_EVS_Rev01.md
- **Date Updated:** October 29, 2025
- **Prepared by:** EVS / PGCIS Team
- **Corrections:** Tilt-up construction, utility voltage options, mechanical yard sizing
