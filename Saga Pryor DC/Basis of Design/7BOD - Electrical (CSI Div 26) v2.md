
<!-- @claude, our other doc has the correct formatting at the very beginning of the doc -->

### 1.1 Overview

This Basis of Design defines the electrical infrastructure for a two-hall, 20,000 SF data center with an ultimate IT load of **24 MW** and a total facility load of approximately **30 MW**. The system is designed to meet Tier III standards, providing N+1 component redundancy and 2N path redundancy for all critical loads.

The electrical backbone is a 13.8 kV common bus, allowing for the flexible integration of utility power, backup generators, and renewable energy sources.

### 1.2 Design Philosophy

- **Availability:** Tier III (Concurrent Maintainability).
    
- **Component Redundancy:** N+1 for all core infrastructure (Substation Transformers, Generators, LV Transformers, Mechanical UPS, and UPS modules within each 2N system).
    
- **Path Redundancy (2N):** True 2N (A/B) path diversity from the MV distribution through the IT UPS systems to the dual-PDUs in each cabinet.
    
- **Phasing:** All infrastructure (substation, generator pads, PDM pads, conduit) shall be designed for the 30 MW full build-out, with capital equipment (generators, transformers, UPS modules) purchased in phases.
    

## 2.0 UTILITY SERVICE & SUBSTATION

### 2.1 Utility Interconnection

- **Service:** A new, customer-owned and maintained substation will be constructed on-site.
    
- **Primary Voltage:** 345 kV or 161 kV, based on the final utility interconnection study, capacity, and cost.
    
- **Metering:** Utility revenue-grade metering will be at the transmission voltage point of interconnection.
    

### 2.2 Substation Transformers

- **Quantity:** Two (2)
    
- **Configuration:** N+1 Redundancy. Either transformer shall be capable of supporting the full 30 MW facility load.
    
- **Rating:** 35 MVA (or as required for 30 MW N+1)
    
- **Secondary Voltage:** 13.8 kV, 3-phase, 60 Hz.
    
- **Location:** Outdoor substation yard.
    

## 3.0 MEDIUM VOLTAGE (13.8 KV) DISTRIBUTION

### 3.1 13.8 kV Common Bus

A 13.8 kV "common bus" infrastructure will serve as the single voltage platform for:

- Utility power (from substation transformers)
    
- Backup generators
    
- Renewable energy (Solar)
    
- Battery Energy Storage (BESS)
    
- Data center critical and mechanical loads
    

### 3.2 MV Dual-Ring Topology

- **Configuration:** Two (2) independent 13.8 kV distribution rings (Ring A and Ring B) providing redundant power paths to the data center's A/B electrical systems.
    
- **Ring Main Units (RMUs):** Approximately eight (8) RMUs will be used for switching, isolation, and load distribution from the rings.
    
- **Controls:** A SCADA-controlled system will provide automated switching for fault isolation and load transfer between rings.
    

## 4.0 GENERATOR SYSTEM

### 4.1 Configuration

- **Redundancy:** N+1, sized for the total 30 MW facility load.
    
- **Quantity (Phase 4):** Nine (9) diesel generators.
    
    - N = 8 generators (8 x 4.0 MW = 32 MW)
        
    - N+1 = 9 generators total.
        
- **Rating:** 4.0 MW (continuous) @ 13.8 kV
    
- **Phasing:** Generators will be added in phases to match load growth.
    
- **Fuel:** Diesel (EPA Tier 4 Final).
    
- **Fuel Storage:** On-site bulk fuel storage to provide 24 hours of runtime at full 30 MW facility load.
    
- **Enclosures:** Sound-attenuated enclosures (performance target: 65 dBA @ 7m).
    
- **Paralleling:** PLC-based paralleling switchgear to sync and parallel all generators onto the 13.8 kV common bus.
    

## 5.0 TRANSFORMER SYSTEM (13.8 KV / 480V)

### 5.1 Configuration

- **Redundancy:** N+1, sized for the total 30 MW facility load.
    
- **Quantity (Phase 4):** Eleven (11) oil-filled transformers.
    
    - (Based on 3,500 kVA / 3.15 MW units: N=10, N+1=11)
        
- **Rating:** 3,500 kVA (or similar), 13.8kV / 480Y/277V.
    
- **Phasing:** Transformers will be added in phases.
    
- **Location:** Outdoor electrical yard with secondary containment per EPA requirements.
    

## 6.0 IT UPS SYSTEM (2N ARCHITECTURE)

### 6.1 Configuration

- **Redundancy:** 2N (fully redundant, dual-path) architecture to meet Tier III concurrent maintainability.
    
- **Topology:** The 24 MW IT load will be protected by two (2) independent **12 MW (N+1)** UPS systems (System A and System B).
    

### 6.2 System Sizing (Phase 4)

- **System A (12 MW N+1):**
    
    - Load: 12 MW
        
    - UPS Modules: 13 x 1,250 kVA (or similar) modules (12+1)
        
- **System B (12 MW N+1):**
    
    - Load: 12 MW
        
    - UPS Modules: 13 x 1,250 kVA (or similar) modules (12+1)
        
- **Total Modules (Phase 4):** 26
    

### 6.3 Path Redundancy

- **Path A:** `MV Ring A -> XFMRs-A -> SWBD-A -> UPS-System-A (12MW N+1) -> Panel-A -> Cabinet PDU-A`
    
- **Path B:** `MV Ring B -> XFMRs-B -> SWBD-B -> UPS-System-B (12MW N+1) -> Panel-B -> Cabinet PDU-B`
    

### 6.4 Battery System

- **Type:** Lithium-Ion (preferred) or VRLA.
    
- **Runtime:** 5-minute runtime at full 12 MW load for each system. This runtime is sized to allow for MV generator synchronization to the bus.
    

### 6.5 Conceptual Diagram (2N UPS)

```
     MV RING A                         MV RING B
         │                                 │
    [XFMRs A]                           [XFMRs B]
         │                                 │
     [SWBD-A]                            [SWBD-B]
         │                                 │
┌───────────────────┐               ┌───────────────────┐
│ UPS-SYSTEM-A (N+1)│               │ UPS-SYSTEM-B (N+1)│
│ [M1] [M2]... [M13]│               │ [M1] [M2]... [M13]│
└─────────┬─────────┘               └─────────┬─────────┘
          │                                 │
    [Dist Panel A]                      [Dist Panel B]
          │                                 │
          └───────────┐   ┌─────────────┘
                      │   │
                ┌─────┴───┴─────┐
                │   RACK 1      │
                │ [PDU-A] [PDU-B] │
                └───────────────┘
```

## 7.0 MECHANICAL UPS SYSTEM

### 7.1 Configuration

- **Redundancy:** N+1 modular architecture.
    
- **Load:** Sized to protect the full 6 MW mechanical load (chiller pumps, CDU pumps, fans) from interruptions during the ~30-60 second transfer to generator power.
    
- **Phasing:** UPS modules will be added in phases to match the mechanical load growth.
    

## 8.0 LOW VOLTAGE (480V) DISTRIBUTION

### 8.1 Main Switchboards

- **Quantity:** Two (2) main switchboards (SWBD-A and SWBD-B).
    
- **Rating:** Sized for 2N distribution of the full facility load.
    
- **Source:** SWBD-A and SWBD-B shall be fed from independent 13.8 kV ring segments and transformer banks.
    

### 8.2 Distribution Panels

- All critical IT and mechanical loads will be served by dual (A/B) distribution panels fed from their respective (A/B) main switchboards.
    

## 9.0 CABINET POWER DISTRIBUTION

- **PDUs:** Each IT cabinet will be equipped with two (2) rack-mounted Power Distribution Units (PDUs), PDU-A and PDU-B.
    
- **Source:** PDU-A shall be fed from the "A" power path, and PDU-B from the "B" power path.
    
- **Rating:** PDUs shall be sized based on the cabinet's designed load (e.g., 2N for 25 kW or 2N for 100 kW).
    

## 10.0 NON-CRITICAL (HOUSE) POWER

### 10.1 Philosophy

- All non-critical support spaces (offices, NOC, security, break rooms) shall be on an electrical system **completely separate** from the critical data center infrastructure.
    

### 10.2 Backup Power

- **Generators:** Two (2) N+1 generators.
    
- **Fuel:** Natural Gas (preferred, if available) for unlimited runtime and to preserve diesel supply for critical loads.
    
- **ATS:** Automatic Transfer Switches will transfer non-critical loads to the house generators upon loss of utility.
    

### 10.3 UPS

- **Ride-Through:** Distributed, small-form-factor UPS units will be provided for critical workstations (NOC, Security) to ensure 10-15 minutes of runtime during the transfer to generator power.
    

## 11.0 RENEWABLE ENERGY INTEGRATION

- **Solar / BESS:** Provisions shall be made to connect future solar and/or BESS assets directly to the 13.8 kV common bus.
    
- **Controls:** The 13.8 kV switchgear shall include provisions for bi-directional metering and (if required) grid-forming inverter controls.
    

## 12.0 ELECTRICAL PHASING STRATEGY

**Note:** UPS Module count is based on a 2N (A/B) 12 MW N+1 system, using 1 MW (1250 kVA) modules.

|   |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|
|**Phase**|**IT MW**|**Racks (L2C/RDHx)**|**PUE**|**Facility MW**|**Generators (4 MW)**|**LV XFMRs (3.5 MVA)**|**IT UPS Modules (1 MW)**|
|**1**|3|30 (30/0)|1.40|~4.2|3 (N+1)|3 (N+1)|6 (2N x (1.5MW N+1))|
|**2**|6|150 (30/120)|1.35|~8.1|4 (N+1)|4 (N+1)|8 (2N x (3MW N+1))|
|**3**|15|285 (105/180)|1.30|~19.5|6 (N+1)|8 (N+1)|18 (2N x (7.5MW N+1))|
|**4**|24|468 (168/288)|1.25|~30.0|9 (N+1)|11 (N+1)|26 (2N x (12MW N+1))|

## 13.0 CODES AND STANDARDS

- **NEC 2023** (National Electrical Code), Oklahoma amendments
    
- **IEEE 141** (Red Book - Electric Power Distribution)
    
- **IEEE 142** (Green Book - Grounding)
    
- **IEEE 242** (Buff Book - Protection and Coordination)
    
- **NFPA 70E** (Standard for Electrical Safety in the Workplace)
    
- **NFPA 110** (Emergency and Standby Power Systems)
    
- **IEC 62040-3** (UPS Classification)