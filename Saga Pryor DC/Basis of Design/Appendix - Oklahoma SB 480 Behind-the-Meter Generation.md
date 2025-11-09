

# APPENDIX - OKLAHOMA SB 480
## Private Power Generation & Natural Gas Integration
### Pryor Data Center - PACHYDERM GLOBAL

**Parent Document:** [[Saga Pryor DC/Basis of Design/Erik_BOD_Updated/_BOD - Exec Summary and TOC]]. 
  
---

## LEGISLATIVE OVERVIEW

**Bill:** Oklahoma Senate Bill 480 (2025)
**Effective Date:** July 1, 2025
**Type:** Energy Infrastructure / Utility Regulation Reform
**Status:** Enacted into law

---

## 1. PURPOSE

Oklahoma SB 480 redefines Oklahoma's energy framework to allow private entities to generate and consume their own power — particularly for large industrial, manufacturing, and data center operations — without being regulated as public utilities under the Oklahoma Corporation Commission.

**Key Objectives:**
- Enable self-generation and behind-the-meter power systems
- Support economic growth and investment attraction
- Enhance grid stability through distributed generation
- Leverage Oklahoma's natural gas resources

---

## 2. PRIMARY REQUIREMENTS

### Natural Gas Component Mandate

**Critical Requirement:**
- All exempt private generation systems **must include a natural gas component** in their power generation mix
- Purely renewable or battery systems without a natural gas element **do not qualify** under SB 480
- Natural gas turbines, microturbines, or combined-heat-and-power (CHP) systems required

**Compliant Technology Examples:**
- Gas turbine + solar hybrid systems
- Natural gas microturbines + battery energy storage systems (BESS)
- Combined-cycle gas turbines (CCGT) with renewable integration
- Reciprocating gas engines with solar/wind

**Non-Compliant Examples:**
- 100% solar + BESS systems (no gas component)
- Pure renewable microgrids without gas generation
- Diesel-only generation systems

### Exemption from Public Utility Classification

**Exemption Criteria:**
- Entities generating electricity solely for **their own use** or for a **specific contracted customer** are not considered public utilities
- Exempt producers may operate outside Oklahoma Corporation Commission regulation on retail energy service
- Private power-purchase agreements (PPAs) or energy-as-a-service models permitted between private parties

**Permitted Use Cases:**
1. Self-generation on owned or leased property for exclusive use
2. Power-purchase agreements (PPAs) between private parties (non-public)
3. Energy-as-a-service models for specific contracted customers

### Prohibited Activities

**Cannot:**
- Sell electricity to the general public
- Serve multiple unaffiliated customers without risk of reclassification
- Act as a retail electricity provider

**Risk:**
- Any attempt to serve multiple unaffiliated customers may reclassify the producer as a regulated utility subject to Oklahoma Corporation Commission oversight

---

## 3. ECONOMIC INTENT

### Industrial Development Focus

**Target Industries:**
- Data centers (hyperscale and enterprise)
- Manufacturing facilities (energy-intensive)
- Industrial operations requiring high reliability

**Benefits:**
- Manage energy reliability and cost directly via localized natural gas generation
- Attract high-load industries to Oklahoma with energy independence
- Reduce dependence on utility grid capacity constraints

### Natural Gas Market Stimulus

**Economic Impact:**
- Supports Oklahoma's upstream and midstream gas economy
- Ensures consistent regional demand for gas-fired distributed energy systems
- Leverages Oklahoma's position as #3 natural gas producing state (2024)
- Creates new markets for natural gas producers and pipeline operators

### Grid Relief & Resilience

**Grid Benefits:**
- Reduces strain on long-distance transmission networks
- Decreases peak demand on distribution infrastructure
- Enables localized resilience strategies for critical infrastructure projects
- Provides grid stability through dispatchable natural gas generation

**Reliability Advantages:**
- Behind-the-meter generation reduces exposure to grid outages
- Natural gas fuel supply via pipeline (diversified from diesel/oil)
- Ability to island from grid during disturbances
- Black-start capability for critical loads

---

## 4. CONSTRAINTS & COMPLIANCE CONSIDERATIONS

### Interconnection & Safety

**Still Required:**
- Interconnection standards compliance (IEEE 1547, utility-specific requirements)
- Pipeline safety codes (PHMSA, Oklahoma Corporation Commission Pipeline Safety)
- Environmental permits (air quality, emissions, SPCC for fuel storage)
- Building and electrical codes (NEC 2023, IBC 2021, Oklahoma amendments)

**Coordination Required:**
- Local grid operator coordination (PSO, OG&E, or cooperative)
- Utility interconnection agreement for grid-parallel operation
- Natural gas utility coordination for fuel supply

### Regulatory Risk

**Key Considerations:**
- **Misclassification Risk:** Operating as a "public utility" could expose developers to state regulation and rate-filing obligations
- **Legal Counsel Requirement:** Confirm generation and consumption structure meets SB 480 exemption tests
- **Ongoing Compliance:** Document that power is for own-use or specific contracted customer only

**Documentation Best Practices:**
- Maintain clear ownership/lease documentation for generation assets
- Document power consumption patterns (behind-the-meter only)
- Avoid language suggesting service to "customers" (use "facilities" or "operations")
- Keep records of natural gas component generation capacity and runtime

### Technology Mix Requirements

**Compliant Systems:**
- Combined-heat-and-power (CHP) systems with natural gas
- Gas turbine or microturbine hybrid systems
- Natural gas generators + renewable + BESS
- Reciprocating gas engines with solar/wind integration

**Non-Compliant:**
- 100% renewable microgrids without gas component
- Solar-only + BESS systems
- Diesel-only generation (no natural gas element)

**Recommended Minimum:**
- Natural gas generation capacity sufficient to meet minimum load requirements
- Gas component must be functional and operational (not just nominal)
- Document gas fuel consumption and generation hours for compliance verification

---

## 5. PRYOR DATA CENTER COMPLIANCE STRATEGY

### Current Design Status

**Existing Infrastructure:**
- 161 kV owner-constructed substation (2 × 25 MVA transformers, 161kV/13.8kV)
- 13.8 kV common bus architecture
- 6 × 4.0 MW diesel generators @ 13.8 kV (N+1 redundancy)
- 8+ MW solar array (adjacent, behind-the-meter)
- Battery Energy Storage System (BESS) integration planned

**SB 480 Compliance Gap:**
- Current design does not include natural gas component
- Diesel generators do not satisfy SB 480 natural gas requirement
- **Solar + BESS alone insufficient for SB 480 exemption**

### Compliance Approach (If the numbers work)

**Option 1: Add Natural Gas Turbine Generators**

**Configuration:**
- Add 2-4 × natural gas turbine generators @ 13.8 kV
- Capacity: 3-5 MW each (similar to existing diesel generators)
- Integration: Parallel with 13.8 kV common bus
- Fuel: Natural gas via pipeline connection

**Advantages:**
- Qualifies for SB 480 exemption
- Diversifies fuel supply (natural gas + diesel backup)
- Potential for lower fuel costs vs. diesel (depending on gas prices)
- Cleaner emissions than diesel (lower NOx, particulates)
- Enables combined-cycle or CHP opportunities (waste heat recovery)

**Cost Estimate:**
- Natural gas turbine generators: $1.5-3.0M per MW (installed)
- Natural gas infrastructure (pipeline tap, gas metering, compression if required): $500K-2M
- Fuel gas treatment system (if required): $200K-500K
- Total incremental cost: $5-15M (depending on configuration and pipeline distance)

**Option 2: Retrofit Existing Diesel Generators for Dual-Fuel (Diesel + Natural Gas)**

**Configuration:**
- Retrofit 3-6 existing diesel generators for dual-fuel operation
- Primary fuel: Natural gas (pipeline)
- Backup fuel: Diesel (~2,000 gal belly tanks per generator + centralized bulk fuel storage)
- Mode: Natural gas primary with diesel pilot injection

**Advantages:**
- Lower capital cost than new gas turbines
- Leverages existing generator investment
- Maintains diesel backup capability
- Qualifies for SB 480 exemption (natural gas component present)

**Challenges:**
- Not all diesel generators can be economically retrofitted
- May require manufacturer support for dual-fuel kits
- Potential de-rating when operating on natural gas
- Emissions compliance more complex in dual-fuel mode

**Cost Estimate:**
- Dual-fuel retrofit kits: $200K-500K per generator
- Natural gas infrastructure: $500K-2M
- Total incremental cost: $1.5-5M (6 generators + infrastructure)

**Option 3: Add Small Natural Gas Microturbines for Base Load + Incentive Qualification**

**Configuration:**
- Add 3-5 × natural gas microturbines (500 kW - 1 MW each)
- Total capacity: 2-5 MW natural gas generation
- Operation: Base load or peak shaving mode
- Integration: 480V or 11 kV (via step-up transformers)

**Advantages:**
- Lower capital cost than large gas turbines
- CHP potential (waste heat recovery for building HVAC or process heat)
- Qualifies for SB 480 exemption (natural gas component)
- Continuous operation demonstrates gas component utilization
- High efficiency at partial load (vs. large turbines)

**Challenges:**
- Lower per-MW capacity vs. diesel generators (not full facility backup)
- Maintenance requirements (gas turbines require periodic overhauls)
- Noise and vibration considerations (outdoor installation typical)

**Cost Estimate:**
- Microturbines: $2-3M per MW (installed, including CHP if applicable)
- Natural gas infrastructure: $500K-2M
- Total incremental cost: $4-10M (3-5 MW microturbines + infrastructure)

### Natural Gas Infrastructure Requirements

**All Options Require:**

**Pipeline Connection:**
- Natural gas pipeline tap from nearest interstate or intrastate pipeline
- Pipeline distance and capacity verification required
- Oklahoma Corporation Commission Pipeline Safety coordination
- Utility coordination: Oklahoma Natural Gas (ONG) or other supplier

**Gas Metering Station:**
- ANSI/AGA-compliant metering
- Telemetry for gas consumption monitoring (compliance documentation)
- Pressure regulation (pipeline pressure → generator inlet pressure)
- Odorization verification (if required by code)

**Fuel Gas Treatment (if required):**
- Filtration (particulate removal)
- Gas heating (prevent freeze-off during pressure reduction)
- Moisture removal (if pipeline gas is saturated)
- H2S removal (if pipeline gas contains sulfur compounds)

**Estimated Lead Time:**
- Pipeline feasibility study: 1-3 months
- Pipeline tap permitting and design: 3-6 months
- Pipeline construction: 3-6 months
- Total: 9-15 months from initiation to gas-on

**Estimated Cost Range:**
- Short distance (<1 mile): $500K-1M
- Medium distance (1-5 miles): $1-3M
- Long distance (>5 miles): $3-10M+


---

## REFERENCES

- **Oklahoma Senate Bill 480 (2025):** [Oklahoma Legislature - SB 480](http://www.oklegislature.gov/)
- **Oklahoma Corporation Commission:** Utility regulation and pipeline safety oversight
- **Oklahoma Department of Environmental Quality (DEQ):** Air quality permitting for natural gas generation
- **Oklahoma Natural Gas (ONG):** Natural gas supplier serving northeast Oklahoma
- **Federal Energy Regulatory Commission (FERC):** Interstate pipeline regulatory oversight

---

**Document Control:**
- **Source:** Oklahoma SB 480 legislative summary and PACHYDERM strategic analysis
- **Date Created:** October 29, 2025
- **Status:** Planning / Feasibility Phase
