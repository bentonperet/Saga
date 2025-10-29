**Created:** 2025-10-23 09:45

# BASIS OF DESIGN - CSI MASTERFORMAT
## Saga Energy – Pryor Data Center
### Mayes County, Oklahoma

**Document Status:** CURRENT - CSI-Organized Reference
**Prepared by:** PGCIS Program Management Team
**Date:** October 2025
**Purpose:** Executive-level basis of design organized by CSI MasterFormat divisions for specifications, cost estimating, and financial modeling

**Related Documents:**
- [[Architectural Meeting Changes by CSI Division]] - October 2025 design updates
- [[Feasibility Memo V3]] - Strategic decisions and validation studies
- [[Why BESS Should Not Be UPS]] - Technical analysis rejecting BESS-as-UPS topology
- [[Excess Solar Monetization Strategy]] - Economic BESS evaluation (rejected - negative NPV)
- [[Diesel vs NatGas Generator CAPEX]] - Generator fuel type cost analysis
- [[_Project Plan]] - Project schedule and milestones

---
## EXECUTIVE SUMMARY

 This plan assumes a phased deployment designed to optimize CapEx spend to closely align with customer occupation of the data center. The entire data center shell will be constructed, as well as the relevant out-buildings, but only half of the data center will be fit out. Next, the space required for updating MEP to accommodate additional rack density has been included in the plan.


<!-- update all these with links to their source pages - then i won't have duplicate information to maintain, right now these are the most updated -->
#### **FACILITY OVERVIEW**
- **IT Capacity:** 12 MW initial (Phase 1-4), expandable to 24MW ultimately
- **White Space:** 20,000 SF total (Phase 1: 10,000 SF fitted, Phase 2: 10,000 SF shell)
- **Power Density:** 1,000-1,200 W/SF (RDHx) → 2,000 W/SF (RDHx / liquid-to-chip)
- **IT Rack Configuration:** {TBD - Rack Density Numbers}
- **Availability:** Tier III-equivalent (N+1 redundancy, concurrent maintainability)
- **Target PUE:** 1.2-1.35 (annual average)
- **Site:** 121 acres, Mayes County, OK (~4 miles from Google Pryor)
- **Building Layout**: Optimized for employee comfort and the corporate sales process

#### **ELECTRICAL SYSTEMS**
- Primary Service: 138 kV to 13.8 kV substation (15-20 MVA transformer)
- UPS: N+1 modular UPS (500 kW modules) with dual paths A/B
  - Phase 1: 8 modules (4 MW capacity)
  - Phase 4: 32 modules (16 MW capacity)
  - Phase 5: 64 modules (32 MW capacity)
- UPS Topology: Dual A/B busways, concurrent maintainability
- IT Transformers: 5,000 kVA, 13.8kV-480Y/277V (Phase 1: 2, Phase 4: 5, Phase 5: 10 units)
- IT Switchboards: 6,000A, 480V (quantities match transformers for N+1 chain)
- Generators: 4.3 MW natural gas turbine (Phase 1: 2, Phase 4: 5, Phase 5: 10 units, N+1 redundancy)
- Generator Fuel: Diesel (if grid Day 1) or natural gas turbine (if no grid Day 1)
- Electrical Enclosures: Outdoor containerized (12 units with space for 16, ~12 ft × 55 ft each {TBC})
- Distribution: 480V overhead busway at 12-14 ft elevation
- Electrical Code: NEC 2023, Oklahoma amendments
- **Design Note:** Generator → Transformer → Switchboard quantities match exactly to maintain unbroken N+1 redundancy chain


#### **MECHANICAL SYSTEMS** 
- **Cooling:** ~16 air-cooled chillers (1.5 MW each) in modular 3 MW blocks (N+1 per block)
	- <!-- Benton - verify chiller capacity to planned IT / facility load -->
- **Chiller Configuration:** Phased deployment aligned with IT load growth
- **IT Cooling:** CDUs + rack-based rear-door heat exchangers (RDHx) or potentially DDC Cabinets (top-cooling) {TBC}
- **Data Hall HVAC:** Rooftop AHUs for comfort cooling and humidity control
- **Zero Water Strategy:** No evaporative cooling, closed-loop chilled water
- **Free Cooling:** ~215 days/year in Oklahoma climate (integrated free cooling mode)
- **Controls:** BMS with chiller rotation, setpoint reset, pump VFD optimization {TBC}
- **Mechanical Code:** IMC 2021, ASHRAE 90.1-2019
- <!-- Go through switch to get to equipment list -->

#### **FACILITY CONSTRUCTION**
- **Structure:** PEMB (steel frame with insulated metal panels)
- **Configuration:** Single story
- **Roofing:** FM-150 tornado-rated (EF-2 resistance, 135 mph winds)
- **Tornado Hardening:** +$150-250/SF premium for FM-150 envelope {TBC}
- **Floor:** Structural slab-on-grade (no raised floor), 6-8" reinforced concrete {TBC}
- **Ceiling Height:** ~30 ft clearance in data hall
- **Hot Aisle Containment:** Optional based on customer demand
- **Security:** Perimeter fence, mantrap entry, CCTV, card access control

#### **RENEWABLE ENERGY & MICROGRID**
- Solar: 12 MW DC array (~19-24 GWh/year generation)
- Renewable Penetration: 60-80% of annual facility energy from on-site solar
- Configuration: Behind-the-meter (BTM) single point of interconnection (POI) {TBC}
- EMS: Simplified power monitoring system ($200-400K) {TBC}
- Demand Response: Assuming natural gas turbines, generators participate in OG&E Load Reduction Program ($600k/year revenue) 
- BESS: Discuss inclusion of BESS at all

#### **SUPPORT SPACES**
- NOC: ~1500SF with overhead view of data hall, 24/7 staffing capability
- Meet-Me Rooms: 2× 250-300 SF (north/south for diverse fiber paths) {TBC}
	- <!-- @julia - confirm MMR sizes (include OME whatever room) -->
- Electrical Enclosures: Outdoor containerized (12-16 units, eliminates indoor cost/risk)
- Mechanical Rooms: 2× 2,000 SF (N+1 redundancy for pumps/controls)
- Staging/Burn-In: 2,000 SF for pre-deployment equipment testing
	- <!-- @julia - confirm MMR sizes (include OME whatever room) -->
- Office/Conference: ~1,000 SF for management, engineering, sales meetings
	- <!-- @julia - confirm MMR sizes (include OME whatever room) -->
- Break Room/Kitchen: 400 SF with appliances, seating for 12 staff
	- <!-- @julia - confirm MMR sizes (include OME whatever room) -->
- Showers/Lockers: 700 SF with washer/dryer (supports 24/7 operations)
	- <!-- @julia - confirm MMR sizes (include OME whatever room) -->

#### **UTILITIES & INFRASTRUCTURE**
- Utility Interconnection: 138 kV transmission line, OG&E service territory
- Substation Transformer: 15-20 MVA (customer-owned or utility-owned, TBD)
- Natural Gas: Pipeline service for turbine generators (~500-700 CFH per turbine) {TBC}
- Diesel Storage: Belly tanks (interconnected and redundant fuel service contracts) or above-ground storage tank (48-hour minimum) {TBC}
- Water: Municipal or on-site well (domestic use only, ~500-1,000 gal/day) {TBC}
- Sewer: Municipal or on-site septic system (domestic wastewater only) {TBD}
- Fiber: Dual diverse entries (recommend redundant fiber connections) via underground ductbank {TBC}
- Stormwater: Detention pond
- Cloud Onramp: GCP Dedicated Interconnect via dark fiber to Google Pryor (~4 miles) {TBC}

#### **FIRE PROTECTION & LIFE SAFETY**
- Data Hall: Pre-action sprinkler or clean agent (FM-200/Novec 1230) per customer preference
- UPS Rooms: Clean agent flooding systems per NFPA 2001
- Detection: VESDA or aspirating smoke detection (ASD) in data hall
- Spot Detection: Electrical rooms, mechanical rooms, support spaces
- Egress: Multiple exits, panic hardware
- Emergency Lighting: 90-minute battery backup, 1 fc average illumination
- Tornado Safety: Tornado shelter room in NOC area and hardened roof and exterior
- NFPA Compliance: NFPA 72, 75, 2001, 101; IBC 2021

#### **CONSTRUCTION & COST BASIS**
- Pricing Date: October 2025 USD
- Geographic Basis: Mayes County, Oklahoma (Tulsa metro labor market)
- Labor: IBEW Local 584 (Tulsa) union rates
- Work Schedule: 6×10 with overtime factor for schedule acceleration
- Construction Duration: 18 months estimated (site prep to commissioning)
- Staging: Adequate area within 121-acre site for laydown and equipment assembly

#### **REGULATORY & PERMITTING**
- Building Code: Oklahoma Building Code (IBC 2021 base)
- Electrical Code: Oklahoma Electrical Code (NEC 2023 base)
- Mechanical Code: Oklahoma Mechanical Code (IMC 2021 base)
- Fire Code: Oklahoma Fire Code with local amendments
- Zoning: Special use permit for data center facility (assumed)
- Environmental: Phase I/II studies required, no remediation assumed

#### **EXCLUSIONS**
- IT Equipment: Servers, networking, storage hardware (customer-provided)
- Land Acquisition: Site assumed to be owned/leased separately
- Long-term O&M: Service contracts beyond warranty periods
- Utility Capacity Charges: Beyond standard connection fees
- Sales Tax: Customer-specific exemptions may apply
- Solar Array: Owned by Saga Energy (not included in data center CAPEX)

#### **DESIGN STANDARDS**
- Power Density: 500 W/SF initial, expandable to 2,000 W/SF (liquid-to-chip cooling) {TBC}
- Cooling: Designed for 1.2-1.4 PUE target (air-cooled chillers with free cooling)
- Uptime: Tier III-equivalent redundancy and concurrent maintainability
- Security: Hyperscale data center standards (perimeter fence, mantrap, CCTV, card access)
- Monitoring: Comprehensive DCIM with BMS and EMS integration

#### **ASSUMPTIONS REQUIRING VALIDATION**
- Power Capacity: Is there enough grid power and can it be contracted? Formal interconnection study required (6-18 month lead time)
- Natural Gas Service: Pipeline capacity adequate for turbine generators, confirmation required
- Permitting: Special use permit for data center facility achievable
- Permitting: Generators and air pollution permissions
- Geotechnical: Based on preliminary assessment, detailed geotechnical study required
	- <!-- Benton -They sent, check this survey for key info -->
- Environmental: No contamination or protected species impacts (Phase I/II studies required)
- Local Labor: Adequate skilled workforce availability (IBEW Local 584 Tulsa jurisdiction)
- Material Delivery: No unusual transportation constraints to Mayes County site

#### **ESTIMATE ACCURACY**
- Class 3 (+/- 15-20%) based on preliminary design level information
- Major cost variables: utility interconnection upgrades, geotechnical conditions, tornado hardening premium
- Updated: October 2025 (post-BESS rejection, post-capacity increase to 12 MW)

---
## FINANCIAL SUMMARY
<!-- Create this section, there's some placeholder info right now -->

**Major CAPEX Drivers**
- Traditional N+1 UPS (dual paths): $24-32M total (phased: Phase 1 $3-4M, Phase 4 +$9-12M, Phase 5 +$12-16M)
- Generators: $12M total (phased: Phase 1 $2.4M, Phase 4 +$3.6M, Phase 5 +$6M)
- IT Transformers: $2M total (phased: Phase 1 $0.4M, Phase 4 +$0.6M, Phase 5 +$1M)
- Tornado hardening: +$150-250/SF building envelope premium
- Chiller plant: ~16 chillers @ 1.5 MW each, phased deployment

## CSI MASTERFORMAT OUTLINE

### **PROCUREMENT AND CONTRACTING REQUIREMENTS GROUP**

#### **Division 00 – Procurement and Contracting Requirements**

See: [[0BOD - Procurement and Contracting (CSI Div 00)]]

- *Project delivery, contracting strategy, phasing approach*
- Phase 1: 12 MW (20,000 SF white space + support spaces)
- Phase 2: Shell for additional 20,000 SF white space
- Modular 3 MW block procurement strategy

---

### **SPECIFICATIONS GROUP**

#### **GENERAL REQUIREMENTS SUBGROUP**

**Division 01 – General Requirements**

See: [[1BOD - General Requirements (CSI Div 01)]]

- *General project requirements, submittals, quality control*
- Commissioning requirements (FAT, SAT, integrated systems testing)
- UPS system testing protocols (load bank testing, bypass verification)
- Generator load testing and automatic transfer switch (ATS) verification

---
#### **FACILITY CONSTRUCTION SUBGROUP**

See: [[2BOD - Facility Construction (CSI Divs 02-14)]]

- **Division 02 – Existing Conditions** - *Site surveys, demolition (if any), hazardous materials*
- **Division 03 – Concrete** - *Structural slab-on-grade (no raised floor), foundations*
- **Division 04 – Masonry** - *Not applicable (PEMB construction)*
- **Division 05 – Metals** - *Structural steel, cable tray, overhead busway supports*
- **Division 06 – Wood, Plastics, and Composites** - *Minimal scope*
- **Division 07 – Thermal and Moisture Protection** - *FM-150 tornado-rated roof, building envelope*
- **Division 08 – Openings** - *Doors, security man-traps, loading dock*
- **Division 09 – Finishes** - *Interior finishes for office, NOC, support spaces*
- **Division 10 – Specialties** - *Minimal scope*
- **Division 11 – Equipment** - *Covered under Division 48 for power generation*
- **Division 12 – Furnishings** - *Office furniture (not part of core facility scope)*
- **Division 13 – Special Construction** - *Not applicable*
- **Division 14 – Conveying Equipment** - *Not applicable (no elevators or material handling)*
- **Divisions 15-19** - *Reserved for Future Expansion*

---
#### **FACILITY SERVICES SUBGROUP**

- **Division 20** - *Reserved for Future Expansion*
- **Division 21 – Fire Suppression** - *Pre-action sprinklers, clean agent for UPS rooms* - [[3BOD - Fire Suppression (CSI Div 21)]]
- **Division 22 – Plumbing** - *Domestic water, sanitary sewer, chilled water makeup* - [[4BOD - Plumbing (CSI Div 22)]]
- **Division 23 – HVAC** - *16 air-cooled chillers, CDUs, RDHx, rooftop AHUs* - [[5BOD - HVAC (CSI Div 23)]]
- **Division 24** - *Reserved for Future Expansion*
- **Division 25 – Integrated Automation** - *BMS, DCIM, simplified EMS* - [[6BOD - Integrated Automation (CSI Div 25)]]
- **Division 26 – Electrical** - *N+1 modular UPS (dual paths), generators, switchboards, distribution* - [[7BOD - Electrical (CSI Div 26)]]
- **Division 27 – Communications** - *Dual MMRs, fiber diversity, GCP interconnection* - [[8BOD - Communications (CSI Div 27)]]
- **Division 28 – Electronic Safety and Security** - *Access control, CCTV, intrusion detection* - [[9BOD - Electronic Safety and Security (CSI Div 28)]]
- **Division 29** - *Reserved for Future Expansion*

---
#### **SITE AND INFRASTRUCTURE SUBGROUP**

- **Division 30** - *Reserved for Future Expansion*
- **Divisions 31-32 – Earthwork & Exterior Improvements** - *Grading, stormwater pond, equipment yards, landscaping* - [[10BOD - Site and Infrastructure (CSI Divs 31-32)]]
- **Division 33 – Utilities** - *138kV interconnection, natural gas, water/sewer* - [[11BOD - Utilities DC Critical (CSI Div 33)]]
- **Division 34 – Transportation** - *Not applicable*
- **Division 35 – Waterway and Marine Construction** - *Not applicable*
- **Divisions 36-39** - *Reserved for Future Expansion*

---
#### **PROCESS EQUIPMENT SUBGROUP**

See: [[BOD - Process Equipment (CSI Divs 40-48)]]

- **Division 40 – Process Integration** - *Simplified microgrid: solar + generators + DC load coordination*
- **Division 41 – Material Processing and Handling Equipment** - *Not applicable*
- **Division 42 – Process Heating, Cooling, and Drying Equipment** - *Not applicable*
- **Division 43 – Process Gas and Liquid Handling, Purification, and Storage Equipment** - *Not applicable*
- **Division 44 – Pollution and Waste Control Equipment** - *Not applicable*
- **Division 45 – Industry-Specific Manufacturing Equipment** - *Not applicable*
- **Division 46 – Water and Wastewater Equipment** - *Covered under Division 22 Plumbing*
- **Division 47** - *Reserved for Future Expansion*
- **Division 48 – Electrical Power Generation** - *12 MW solar array, natural gas turbines, diesel generators*
- **Division 49** - *Reserved for Future Expansion*
- **Division 50 – Specialized Construction** - *Not applicable*

---

## DEVIATIONS FROM RD109 BASELINE
<!-- Continue updating this section for Thur meeting -->

### Major Eliminations vs RD109
- ❌ Fan walls (replaced with RDHx rack-based cooling)
- ❌ Adiabatic fluid coolers (zero water cooling strategy)
- ❌ Raised floor (structural slab with overhead distribution)

### Major Additions vs RD109
- Traditional N+1 modular UPS with dual paths
- Natural gas turbine(s) for primary backup power / Potential Diesel generators for fuel diversity backup
- Expanded chiller plant (~16 chillers vs RD109's 3)
- Rooftop AHUs for data hall comfort cooling/humidity control

### Design Approach Changes
- Shell + core phasing (20,000 SF data hall, 10,000 SF Phase 1 fit-out)
- Modular 3 MW blocks for customer flexibility
- Electrical equipment on one building side, mechanical on opposite

---

**Tags:** #saga-project #basis-of-design #csi-masterformat #executive-summary

**Next Steps:**
1. Review subpages for detailed technical specifications by CSI division
2. Validate financial model inputs with cost estimating team (see [[Financial Model Change Log]])
3. Close outstanding decisions by November 2025
4. Handoff to MEP engineering consultant for detailed design

---


