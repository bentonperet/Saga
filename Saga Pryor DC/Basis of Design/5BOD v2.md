$$PROJECT NAME$$

- MECHANICAL BASIS OF DESIGN (BOD)

# CSI DIVISION 23 - (TIER III - 24 MW)

## 1.0 OVERVIEW & DESIGN PHILOSOPHY

### 1.1 Overview

This document defines the phased mechanical cooling strategy for a 24 MW IT (30 MW facility) data center. The design is optimized for AI/ML workloads, starting with a **3 MW L2C (Liquid-to-Chip) anchor tenant (Phase 1)** and expanding to a 24 MW ultimate capacity.

The design is built on a **zoned-hall** (DH-W vs. DH-E) concept with **two independent, physically separate cooling plants** (a 16.8 MW warm-water L2C plant and a 7.2 MW cold-water RDHx plant).

### 1.2 Design Philosophy

- **Phased Deployment:** Cooling plant CapEx is deployed in phases to match IT load and rack growth (30 → 150 → 285 → 468 racks).
    
- **Zoned-Hall Strategy:**
    
    - **Data Hall West:** Served by Loop 3 (L2C)
        
    - **Data Hall East:** Served by Loops 1+2 (RDHx)
        
- **Separate Loop Architecture:**
    
    - **Loop 3 (L2C):** 16.8 MW plant with an **85°F (29°C)** "warm water" supply. This temperature is specified to maximize chiller efficiency and free cooling hours.
        
    - **Loops 1+2 (RDHx):** 7.2 MW plant with a **60°F (15.5°C)** "cold water" supply. This temperature is required for effective rear-door air cooling.
        
- **Redundancy:** N+1 for all chillers, pumps, and cooling distribution units.
    
- **Zero Water Consumption:** Design uses all air-cooled chillers, closed-loop glycol/fluid systems, and zero evaporative cooling.
    
- **Target PUE:** 1.40 (Phase 1) improving to **1.25** (Phase 4) at scale, driven by warm-water cooling efficiencies.
    

## 2.0 COOLING LOAD PHASING

### 2.1 IT Load & Rack Phasing

|   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|
|**Phase**|**IT MW (Cumulative)**|**Racks (Total)**|**L2C Racks (100kW)**|**RDHx Racks (25kW)**|**L2C Load**|**RDHx Load**|
|**1**|3 MW|30|30|0|3.0 MW|0 MW|
|**2**|6 MW|150|30|120|3.0 MW|3.0 MW|
|**3**|15 MW|285|105|180|10.5 MW|4.5 MW|
|**4**|24 MW|468|168|288|**16.8 MW**|**7.2 MW**|

### 2.2 Mechanical Plant Phasing

|   |   |   |   |   |   |
|---|---|---|---|---|---|
|**Phase**|**L2C Load**|**L2C Plant (N+1)**|**RDHx Load**|**RDHx Plant (N+1)**|**L2C CDU Solution**|
|**1**|3.0 MW|Phased to 3 MW|0 MW|Not Commissioned|A/B for 30 Racks|
|**2**|3.0 MW|Phased to 3 MW|3.0 MW|Phased to 3 MW|A/B for 30 Racks|
|**3**|10.5 MW|Phased to 10.5 MW|4.5 MW|Phased to 4.5 MW|A/B for 105 Racks|
|**4**|16.8 MW|Phased to 16.8 MW|7.2 MW|Phased to 7.2 MW|A/B for 168 Racks|

## 3.0 LOOP 3: WARM WATER L2C PLANT (16.8 MW)

This plant serves the 168 high-density (100 kW) L2C racks in Data Hall West.

### 3.1 L2C Chiller Plant

- **Capacity (Phase 4):** Shall be an N+1 air-cooled chiller plant, phased to meet the ultimate **16.8 MW** L2C load.
    
- **Fluid:** 25% Propylene Glycol / Water Mixture
    
- **Supply Temperature:** **85°F (29°C)**
    
- **Efficiency:** The 85°F supply temperature is specified to maximize mechanical COP and free-cooling opportunities.
    
- **Pumping:** **Variable Primary Flow (VPF)**. All primary pumps shall be integrated into the packaged chillers with VFDs. No separate pump rooms required.
    

### 3.2 L2C Coolant Distribution

- **CDUs (Coolant Distribution Units):** The L2C load will be served by high-capacity CDUs located in the adjacent mechanical galleries, not in the data hall.
    
- **Redundancy:** Each 100 kW L2C rack shall be fed by an **A/B redundant CDU solution.**
    
- **Capacity (Each CDU):** The A/B CDU solution shall be sized to support the full 100 kW rack load.
    
- **Primary Side:** 85°F warm water from Loop 3.
    
- **Secondary Side:** Dielectric fluid (or facility-safe fluid) piped via overhead manifolds to quick-disconnects at each rack's cold plates.
    
- **Controls:** Integrated leak detection at all connections, reporting to BMS.
    

## 4.0 LOOPS 1+2: COLD WATER RDHx PLANT (7.2 MW)

This plant serves the 288 medium-density (25 kW) RDHx racks in Data Hall East.

### 4.1 RDHx Chiller Plant

- **Capacity (Phase 4):** Shall be an N+1 air-cooled chiller plant, phased to meet the ultimate **7.2 MW** RDHx load.
    
- **Fluid:** 25% Propylene Glycol / Water Mixture
    
- **Supply Temperature:** **60°F (15.5°C)**
    
- **Rationale:** This colder temperature is required for the RDHx units to effectively cool air.
    
- **Pumping:** **Variable Primary Flow (VPF)**. All primary pumps shall be integrated into the packaged chillers with VFDs.
    

### 4.2 RDHx Distribution

- **RDHx Units:** One (1) Rear-Door Heat Exchanger shall be mounted on each of the 288 racks.
    
- **Capacity (Each RDHx):** Sized to support the 25 kW rack load.
    
- **Distribution:** 60°F cold water shall be piped via overhead manifolds to quick-disconnects at each RDHx unit.
    

## 5.0 CHILLER & FREE COOLING SPECIFICATIONS

### 5.1 General Chiller Specifications

- **Type:** Air-cooled screw or scroll compressors with integrated VFDs and free-cooling (waterside economizer) coils.
    
- **Refrigerant:** Shall be a **Low-GWP (Global Warming Potential) fluid** compliant with all current and anticipated EPA/AIM Act regulations.
    
- **Controls:** BACnet/IP integration with facility BMS for staging, rotation, and free-cooling optimization.
    

### 5.2 Free Cooling Operation

- **L2C Loop (85°F):** The warm-water loop allows for an extended free-cooling season. The BMS shall optimize for waterside economization when ambient conditions permit.
    
- **RDHx Loop (60°F):** Free cooling shall be utilized when ambient conditions permit.
    
- **Estimated Hours:** The 85°F loop is projected to provide **~3,500-4,000 hours/year** of full or partial free cooling in the Pryor, OK climate.
    

## 6.0 DATA HALL ENVIRONMENTAL CONTROL (HVAC)

The L2C and RDHx systems handle 100% of the IT heat load. A separate HVAC system is required to manage the data hall environment (air quality, humidity, pressurization).

### 6.1 DOAS (Dedicated Outdoor Air System)

- **Purpose:** To provide ventilation, humidity control, and positive pressurization to the data halls, per ASHRAE TC 9.9 guidelines.
    
- **Type:** Dedicated 100% outdoor air units with energy recovery (enthalpy wheel).
    
- **Redundancy:** N+1 DOAS units shall be provided for each data hall.
    
- **Pressurization:** System shall maintain a positive pressure to prevent dust/contaminant infiltration.
    
- **Filtration:** System shall provide air filtration compliant with **ASHRAE TC 9.9 for a Class A1 data center.**
    
- **Humidity Control:**
    
    - **Target:** 40-60% RH
        
    - **Humidification:** Steam injection humidifiers
        
    - **Dehumidification:** Integrated cooling coil + reheat in DOAS units
        

### 6.2 Support Space HVAC

- **Offices, NOC, Support:** Standard rooftop package units (RTUs) will provide comfort cooling and ventilation.
    
- **Electrical/PDM Rooms:** Integrated, redundant HVAC units (factory-installed) will maintain the optimal operating temperature for UPS and switchgear.
    

## 7.0 CODES AND STANDARDS

- **IMC 2021** (International Mechanical Code)
    
- **ASHRAE 90.1-2019** (Energy Standard)
    
- **ASHRAE 62.1** (Ventilation)
    
- **ASHRAE TC 9.9** (Mission Critical Facilities)
    
- **NFPA 90A** (Installation of A/C and Ventilating Systems)
    

## 8.0 VERSIONING CALLOUTS

This section details key "de-risking" changes made to this Basis of Design. The goal is to define the _performance requirement_ without over-prescribing a specific _solution_, which protects the project from being locked into a single vendor or costly, non-optimal design.

- **Chiller & CDU Sizing (Sections 2.2, 3.1, 4.1):**
    
    - **Removed:** Specific counts of chillers (e.g., "13 chillers") and specific CDU sizes (e.g., "300 kW").
        
    - **Why:** This document now defines the _total N+1 capacity_ required at each phase (e.g., "Phased to 16.8 MW N+1"). This gives the engineering team the flexibility to select the most cost-effective solution (e.g., 10 larger chillers vs. 13 smaller ones) that still meets the N+1 performance goal.
        
- **Refrigerant (Section 5.1):**
    
    - **Removed:** Specific chemical names (e.g., "R-134a").
        
    - **Why:** Replaced with a performance requirement ("Low-GWP... compliant with EPA/AIM Act"). This future-proofs the design against changing regulations and prevents being locked into a chemical that may become obsolete or expensive.
        
- **Return Temps & COP (Sections 3.1, 4.1):**
    
    - **Removed:** Specific "Return Temperature" (e.g., 95°F) and "COP" (e.g., 5.0-6.5) values.
        
    - **Why:** The BOD's job is to set the _input_ (the 85°F supply), which is the key design decision. The return temperature and COP are _outcomes_ dependent on the final load and vendor-specific chiller performance. Promising a specific COP in a BOD is a commercial risk.
        
- **Filtration (Section 6.1):**
    
    - **Removed:** Specific solution ("MERV 8/13").
        
    - **Why:** Replaced with the _standard_ ("compliant with ASHRAE TC 9.9 for a Class A1 data center"). This ensures the goal is met (a clean data hall) without over-prescribing the exact method.