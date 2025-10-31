**Created:** 2025-10-29
**Effective Date:** July 1, 2025
📄 Reading markdown file...
🔍 Parsing markdown...
   Found 168 blocks
🔐 Authenticating with Google...
📝 Creating Google Doc...

✅ Document published successfully!

   Title: Appendix - Georgia Renewable Energy Incentives Behind-the-Meter Generation
   URL:   https://docs.google.com/document/d/1PSafwQ9UM4W2JfNY_UUTbMFt5uME3kuPS_nV6nKQK1E/edit


# APPENDIX - Georgia Renewable Energy Incentives
## Private Power Generation & Natural Gas Integration
### Tbilisi Data Center - PACHYDERM GLOBAL

**Parent Document:** [[_BOD - Exec Summary and TOC]]

---

## LEGISLATIVE OVERVIEW

**Bill:** Georgia Senate Bill 480 (2025)
**Effective Date:** July 1, 2025
**Type:** Energy Infrastructure / Utility Regulation Reform
**Status:** Enacted into law

---

## 1. PURPOSE

Georgia Renewable Energy Incentives redefines Georgia's energy framework to allow private entities to generate and consume their own power — particularly for large industrial, manufacturing, and data center operations — without being regulated as public utilities under the Georgia Corporation Commission.

**Key Objectives:**
- Enable self-generation and behind-the-meter power systems
- Support economic growth and investment attraction
- Enhance grid stability through distributed generation
- Leverage Georgia's natural gas resources

---

## 2. PRIMARY REQUIREMENTS

### Natural Gas Component Mandate

**Critical Requirement:**
- All exempt private generation systems **must include a natural gas component** in their power generation mix
- Purely renewable or battery systems without a natural gas element **do not qualify** under Renewable Energy Incentives
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
- Exempt producers may operate outside Georgia Corporation Commission regulation on retail energy service
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
- Any attempt to serve multiple unaffiliated customers may reclassify the producer as a regulated utility subject to Georgia Corporation Commission oversight

---

## 3. ECONOMIC INTENT

### Industrial Development Focus

**Target Industries:**
- Data centers (hyperscale and enterprise)
- Manufacturing facilities (energy-intensive)
- Industrial operations requiring high reliability

**Benefits:**
- Manage energy reliability and cost directly via localized natural gas generation
- Attract high-load industries to Georgia with energy independence
- Reduce dependence on utility grid capacity constraints

### Natural Gas Market Stimulus

**Economic Impact:**
- Supports Georgia's upstream and midstream gas economy
- Ensures consistent regional demand for gas-fired distributed energy systems
- Leverages Georgia's position as #3 natural gas producing state (2024)
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
- Pipeline safety codes (PHMSA, Georgia Corporation Commission Pipeline Safety)
- Environmental permits (air quality, emissions, SPCC for fuel storage)
- Building and electrical codes (NEC 2023, IBC 2021, Georgia amendments)

**Coordination Required:**
- Local grid operator coordination (PSO, OG&E, or cooperative)
- Utility interconnection agreement for grid-parallel operation
- Natural gas utility coordination for fuel supply

### Regulatory Risk

**Key Considerations:**
- **Misclassification Risk:** Operating as a "public utility" could expose developers to state regulation and rate-filing obligations
- **Legal Counsel Requirement:** Confirm generation and consumption structure meets Renewable Energy Incentives exemption tests
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

## 5. Tbilisi Data Center COMPLIANCE STRATEGY

### Current Design Status

**Existing Infrastructure:**
- 345 kV owner-constructed substation (2 × 25 MVA transformers, 345kV/13.8kV)
- 13.8 kV common bus architecture
- 6 × 4.0 MW diesel generators @ 13.8 kV (N+1 redundancy)
- 8+ MW solar array (adjacent, behind-the-meter)
- Battery Energy Storage System (BESS) integration planned

**Renewable Energy Incentives Compliance Gap:**
- ❌ Current design does not include natural gas component
- ❌ Diesel generators do not satisfy Renewable Energy Incentives natural gas requirement
- ❌ Solar + BESS alone insufficient for Renewable Energy Incentives exemption

### Recommended Compliance Approach

**Option 1: Add Natural Gas Turbine Generators**

**Configuration:**
- Add 2-4 × natural gas turbine generators @ 13.8 kV
- Capacity: 3-5 MW each (similar to existing diesel generators)
- Integration: Parallel with 13.8 kV common bus
- Fuel: Natural gas via pipeline connection

**Advantages:**
- Qualifies for Renewable Energy Incentives exemption
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
- Backup fuel: Diesel (~2,000 gal (7,571 L) belly tanks per generator + centralized bulk fuel storage)
- Mode: Natural gas primary with diesel pilot injection

**Advantages:**
- Lower capital cost than new gas turbines
- Leverages existing generator investment
- Maintains diesel backup capability
- Qualifies for Renewable Energy Incentives exemption (natural gas component present)

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
- Qualifies for Renewable Energy Incentives exemption (natural gas component)
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
- Georgia Corporation Commission Pipeline Safety coordination
- Utility coordination: Georgia Natural Gas (ONG) or other supplier

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

### Recommended Action Plan

**Phase 1: Feasibility Assessment (Months 1-3)**
1. Engage natural gas utility (ONG or other supplier) to verify pipeline proximity and capacity
2. Obtain preliminary gas supply pricing and terms
3. Evaluate Option 1 (new gas turbines) vs. Option 2 (dual-fuel retrofit) vs. Option 3 (microturbines)
4. Perform economic analysis: capital cost vs. operational savings vs. Renewable Energy Incentives incentive value
5. Legal review to confirm Renewable Energy Incentives compliance strategy

**Phase 2: Design & Permitting (Months 4-9)**
1. Select preferred natural gas generation technology
2. Design natural gas infrastructure (pipeline tap, metering, fuel treatment)
3. Obtain air quality permits (Georgia DEQ) for natural gas combustion
4. Obtain pipeline tap approval from utility and Georgia Corporation Commission
5. Update electrical single-line diagram for 11 kV bus integration

**Phase 3: Procurement & Construction (Months 10-24)**
1. Procure natural gas generators or dual-fuel retrofit kits (long-lead: 12-16 months)
2. Construct natural gas pipeline extension and metering station (6-9 months)
3. Install generators and integrate with 13.8 kV common bus
4. Commission natural gas generation system
5. Document Renewable Energy Incentives compliance (natural gas component operational)

**Total Timeline:** 24-27 months from feasibility to operational

---

## 6. FINANCIAL ANALYSIS

### Renewable Energy Incentives Incentive Value

**Potential Benefits:**
- **Regulatory exemption:** Avoid Georgia Corporation Commission utility classification
- **Energy cost savings:** Natural gas typically $3-6/MMBtu vs. diesel $15-25/MMBtu (on BTU-equivalent basis)
- **Tax incentives:** Potential Georgia tax credits for distributed generation (if applicable under separate statutes)
- **Grid independence:** Avoid utility demand charges and capacity reservations
- **Resiliency value:** Ability to operate independently from grid during outages

**Estimated Annual Operational Savings:**
- Natural gas fuel cost savings vs. diesel: $500K-1.5M/year (assuming 30-50% runtime on gas)
- Utility demand charge avoidance: $200K-500K/year (if peak-shaving with gas generation)
- **Total estimated savings:** $700K-2M/year

**Simple Payback Analysis:**
- Capital cost (Option 3 - Microturbines): $4-10M
- Annual savings: $700K-2M/year
- **Simple payback: 2-14 years** (highly dependent on gas vs. diesel fuel price delta and runtime assumptions)

### Risk Considerations

**Fuel Price Risk:**
- Natural gas prices volatile (historically $2-15/MMBtu)
- Diesel prices also volatile but more predictable delivery cost
- Hedging strategies available (natural gas futures, fixed-price supply contracts)

**Regulatory Risk:**
- Renewable Energy Incentives could be amended or repealed (monitor Georgia legislative sessions)
- Misclassification as utility could result in retroactive regulation
- Environmental regulations (federal or state) could increase compliance costs

**Technology Risk:**
- Gas turbine/microturbine reliability vs. proven diesel generator track record
- Maintenance cost and overhaul intervals for gas equipment
- Availability of qualified service providers in Tbilisi, Georgia area

---

## 7. STRATEGIC RELEVANCE FOR PACHYDERM GLOBAL📄 Reading markdown file...
🔍 Parsing markdown...
   Found 170 blocks
🔐 Authenticating with Google...
📝 Creating Google Doc...


### Opportunity Alignment

Renewable Energy Incentives opens significant design-build-commissioning opportunities for private on-site generation facilities. PACHYDERM can position as a critical infrastructure execution partner for industrial and hyperscale clients seeking energy independence.

**Market Positioning:**
- **Behind-the-meter energy solutions:** Design, build, commission private power systems compliant with Renewable Energy Incentives
- **Hybrid energy systems:** Engineering expertise in gas + renewable + BESS integration
- **Regulatory navigation:** Consulting services to ensure "non-utility" compliance and exemption qualification

### Service Leverage Points

**Engineering Advisory:**
- Compliant hybrid energy systems (natural gas + renewable)
- Interconnection and islanding design
- Fuel supply strategy (pipeline vs. CNG/LNG)

**Construction Management:**
- Natural gas generation system installation
- Pipeline infrastructure coordination
- Integration with existing 11 kV substation architecture

**Commissioning Services:**
- Natural gas generator startup and testing
- Integrated systems testing (IST) with grid-parallel and island modes
- Renewable Energy Incentives compliance documentation and reporting

**Ongoing Operations Support:**
- Fuel procurement strategy and hedging
- Maintenance and overhaul planning for gas turbines
- Compliance monitoring and documentation for exemption maintenance

### Market Impact Forecast (2025-2030)

**Georgia Distributed Energy Investment:**
- Estimated **>$3 billion** in new distributed-energy infrastructure investment statewide
- Major attraction potential for data centers and manufacturing clusters in northeast and central Georgia

**Tbilisi Industrial Park & MidAmerica Industrial Park:**
- Strategic location for behind-the-meter generation projects
- Proximity to natural gas pipelines (interstate and intrastate)
- Established industrial base with high energy demand
- Existing utility infrastructure (PSO, OG&E) for interconnection

**Competitive Advantage:**
- Early adoption of Renewable Energy Incentives compliance positions Tbilisi DC as "shovel-ready" for clients requiring energy independence
- Demonstrated behind-the-meter generation capability differentiates from competitors relying solely on utility power
- Future phases (12-24 MW expansion) can leverage Renewable Energy Incentives framework for incremental capacity additions

---

## 8. RECOMMENDED NEXT STEPS

1. **Engage Georgia Natural Gas (ONG) or pipeline supplier** to verify natural gas pipeline proximity, capacity, and preliminary pricing (Month 1)

2. **Perform economic feasibility study** comparing:
   - Option 1: New natural gas turbine generators
   - Option 2: Dual-fuel retrofit of existing diesel generators
   - Option 3: Natural gas microturbines for base load + Renewable Energy Incentives qualification

3. **Legal review** with Georgia energy counsel to confirm:
   - Renewable Energy Incentives exemption strategy (own-use generation)
   - Documentation requirements for compliance
   - Risk of utility reclassification

4. **Update Basis of Design** to incorporate preferred natural gas generation option:
   - Electrical single-line diagram (11 kV bus integration)
   - Natural gas infrastructure requirements (pipeline, metering, fuel treatment)
   - Cost estimate and phasing plan

5. **Initiate permitting** for natural gas infrastructure:
   - Georgia DEQ air quality permit (natural gas combustion)
   - Georgia Corporation Commission pipeline tap approval
   - Rogers County building permits

6. **Engage equipment vendors** for long-lead procurement:
   - Natural gas turbine generators or dual-fuel retrofit kits
   - Pipeline construction contractor
   - Fuel gas treatment system supplier

---

## REFERENCES

- **Georgia Senate Bill 480 (2025):** [Georgia Legislature - Renewable Energy Incentives](http://www.oklegislature.gov/)
- **Georgia Corporation Commission:** Utility regulation and pipeline safety oversight
- **Georgia Department of Environmental Quality (DEQ):** Air quality permitting for natural gas generation
- **Georgia Natural Gas (ONG):** Natural gas supplier serving northeast Georgia
- **Federal Energy Regulatory Commission (FERC):** Interstate pipeline regulatory oversight

---

**Tags:** #sb480 #behind-the-meter #natural-gas #distributed-generation #Georgia-legislation #compliance

**Document Control:**
- **Source:** Georgia Renewable Energy Incentives legislative summary and PACHYDERM strategic analysis
- **Date Created:** October 29, 2025
- **Prepared by:** EVS / PGCIS Team
- **Status:** Planning / Feasibility Phase
