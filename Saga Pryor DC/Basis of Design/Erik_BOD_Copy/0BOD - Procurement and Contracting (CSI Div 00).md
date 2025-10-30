**Created:** 2025-10-23 13:00

# BASIS OF DESIGN - PROCUREMENT AND CONTRACTING REQUIREMENTS
## CSI Division 00
### Saga Energy – Pryor Data Center

---

## OVERVIEW

Division 00 defines project delivery approach, contracting strategy, and phasing methodology to optimize capital efficiency and align construction with lease-up. It includes:

- **Bidding Requirements:** Instructions to Bidders (ITB), bid forms, and information on the bid process (e.g., pre-bid meeting, site access, due date).
- **Contracting Requirements:** The actual contract agreement (e.g., AIA A101), the General Conditions of the contract (e.g., AIA A201), and Supplementary Conditions that modify the General Conditions for this specific project.
- **Legal & Financial:** Requirements for bonds (bid, performance, payment), insurance certificates, and other legal notices.

*Note: This division is not a technical specification; it is the "front-end" documentation that contains all the business and legal information required to bid on and enter into a contract for the project.*


---
<!-- Everything below: this document needs a complete rewrite -->

## PHASED DEPLOYMENT STRATEGY

### Phase 1: Initial Build (Day One)

**Scope:**
- **Building Shell:** 40,000 SF envelope (complete structure)
- **White Space Fit-Out:** 20,000 SF (half building only)
- **IT Capacity:** 3 MW initial build
- **UPS:** 3MW N+1 (2N modular frames with Phase 1 modules only)
- **Generators:** 2 units (N+1 for ~4 MW load)
- **Chillers:** 3 units (2 1.5MW blocks, Plus 1 for N+1) {TBC}
- **Support Spaces:** NOC, MMRs, staging area, electrical/mechanical rooms

**CAPEX:** $TBD (includes building shell + Phase 1 fit-out + long-lead equipment)

**Timeline:** TBD

### Phase 2: Shell Space Fit-Out

**Scope:**
- **White Space Fit-Out:** Additional 20,000 SF (complete 40,000 SF total)
- **IT Capacity:** +6 MW additional capacity
- **UPS:** Add modules to existing 2N frames (expand from 6MW to 10-12MW N+1)
- **Generators:** Add 2-3 units (N+1 for expanded load)
- **Chillers:** Add 6 units (expand to 4 blocks total)

**CAPEX:** $TBD (fit-out only, MEP expansion)

**Timeline:** 6-9 months (triggered by lease-up)

**Trigger:** 70-80% occupancy of Phase 1 white space

### Phases 3-5: Density Upgrades

**Scope:**
- **IT Capacity:** Density upgrades from 500 W/SF → 1,000 W/SF → 2,000 W/SF
- **UPS:** Phased module additions to reach ultimate 28MW capacity
- **Generators:** Additional units to support ultimate load (8 total)
- **Chillers:** Additional units to support density increases (~16 total ultimate)
- **Cooling Upgrades:** Enhanced RDHx, liquid-to-chip infrastructure

**CAPEX:** $TBD (equipment-focused, minimal building changes)

**Timeline:** Phased over 5-10 years based on customer demand

**Trigger:** Customer requests for higher-density deployments

---

## MODULAR 3 MW BLOCK STRATEGY

| Phase | IT Load | Facility Load (PUE 1.35-1.42) | Buildout Timeline |
| ----- | ------- | ----------------------------- | ----------------- |
| **1** | 3MW     | 4.0-4.3MW                     | Months 0-12       |
| **2** | 6MW     | 8.0-8.5MW                     | Months 12-24      |
| **3** | 9MW     | 12.0-12.8MW                   | Months 24-36      |
| **4** | 12MW    | 16.0-17.0MW                   | Months 36-48      |
| **5** | 20MW    | 27.0-28.4MW                   | Months 48-60+     |
|       |         |                               |                   |

### Customer Flexibility Model

**Concept:**
- Each 3 MW block = 3 chillers (N+1 redundancy within block)
- MEP systems deployed in 3 MW increments aligned with lease commitments

**Benefits:**
- **Capital Efficiency:** Deploy cooling capacity only as revenue materializes
- **Customer Optionality:** Flexibility for phased move-ins or expansion
- **Risk Mitigation:** Avoid stranded capacity if lease-up slower than projected


---

## PROCUREMENT SCHEDULE


---

## CONTRACTING APPROACHES BY SYSTEM

### Electrical Systems

**UPS:**
- **Contract Type:** Owner-direct purchase, contractor installation
- **Vendor Selection:** Schneider, Eaton, or Vertiv (evaluate service ecosystem)
- **Procurement:** Negotiate pricing for Phase 1 + option pricing for Phases 2-5

**Generators:**
- **Contract Type:** Design-build or owner-direct purchase
- **Vendor Options:** Caterpillar, Cummins, or similar for diesel; Solar Turbines for natural gas turbines

**Electrical Distribution:**
- **Contract Type:** Subcontract under GC (or owner-direct for major components)
- Switchgear, busway, transformers, distribution panels

### Mechanical Systems

**Chillers:**
- **Contract Type:** Owner-direct purchase (phased procurement)
- **Rationale:** Long lead time, phased deployment requires flexibility

**Balance of Mechanical:**
- CDUs, pumps, piping, controls: Subcontract under GC or mechanical subcontractor

---

## COMPETITIVE BIDDING REQUIREMENTS


---

## CONSTRUCTION PHASING & SITE LOGISTICS

### Site Access & Staging

**Staging Area:** Adequate area within 121-acre site for:
- Equipment laydown (chillers, generators, UPS, transformers)
- Material storage (structural steel, electrical gear, piping)
- Temporary construction trailers

**Delivery Access:** Good highway access for semi-trailer deliveries (equipment, structural steel)

---

## COMMISSIONING REQUIREMENTS


---

## COST CONTROL & CONTINGENCIES


---

## PAYMENT & FINANCING

**JIT UPS Deployment Benefit:** Phase 1 CAPEX reduced by $21.8M (deferred to Phases 2-5), improves construction loan draw requirements

---

## RISK ALLOCATION


---

## OUTSTANDING PROCUREMENT DECISIONS


---

**Tags:** #saga-project #procurement #contracting #phasing #csi-division-00

**Related Documents:**
- [[Saga Pryor DC/Basis of Design/Erik_BOD_Copy/_BOD - Exec Summary and TOC]] - Main title page
- [[Saga Pryor DC/Basis of Design/Erik_BOD_Copy/1BOD - General Requirements (CSI Div 01)]] - Commissioning and testing requirements
- [[Financial Model Change Log]] - CAPEX phasing and JIT deployment strategy
- [[Saga Pryor DC/Basis of Design/Erik_BOD_Copy/7BOD - Electrical (CSI Div 26)]] - UPS and generator specifications
- [[Saga Pryor DC/Basis of Design/Erik_BOD_Copy/5BOD - HVAC (CSI Div 23)]] - Chiller procurement strategy
