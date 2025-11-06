

# PROJECT COST SUMMARY - PHASE 4 FULL BUILD-OUT
## Pryor Data Center - PACHYDERM GLOBAL

---

## EXECUTIVE SUMMARY

This document consolidates capital expenditure (CAPEX) estimates for the Pryor Data Center at Phase 4 full build-out (22 MW IT capacity). All costs are Rough Order of Magnitude (ROM) estimates suitable for preliminary budgeting and financing discussions.

**Project Overview:**
- **Location:** Pryor, Oklahoma
- **Facility Type:** Tier III Data Center with High Risk (HR) tornado hardening
- **IT Capacity:** 22 MW (Phase 4 ultimate)
- **Facility Load:** ~30 MW total (PUE 1.35)
- **White Space:** 20,000 SF (two 10,000 SF data halls)
- **Total Building:** 38,000 SF gross
- **Cooling Strategy:** Air-cooled chillers, zero water consumption (WUE <0.5 L/kWh)

---

## TOTAL PROJECT COST BY CSI DIVISION

| CSI Division | System Description                   | Subtotal         | Confidence | Key Scope Items                                                                                    |
| ------------ | ------------------------------------ | ---------------- | ---------- | -------------------------------------------------------------------------------------------------- |
| **02-14**    | Facility Construction (Shell & Core) | $11,939,000      | ±25%       | Precast tilt-up walls, FM 1-150 roof, 38,000 SF building, FEMA 361 storm shelter, elevator         |
| **21**       | Fire Suppression                     | $1,742,000       | ±23%       | Preaction sprinklers (20,000 SF data halls), VESDA detection, fire alarm, emergency lighting       |
| **22**       | Plumbing                             | $350,000         | ±27%       | Domestic water service, sanitary/storm drainage, fixtures, hot water system (no cooling tower)     |
| **23**       | HVAC (Mechanical Cooling)            | $15,273,555      | ±35%       | Chillers (18 units @ 1,500 kW), glycol systems, piping/distribution, leak detection, DOAS units    |
| **26**       | Electrical                           | $75,472,183      | ±20%       | Substation (2×35 MVA), generators (9×4 MW), transformers (11×3.5 MVA), UPS (23 modules), E-Houses  |
| **27**       | Communications                       | $1,500,000       | ±33%       | Dual MPOE/MMR, fiber backbone, structured cabling, cloud on-ramps, grounding/bonding               |
| **28**       | Electronic Safety & Security         | $4,213,000       | ±25%       | Perimeter fence/sally port, access control, CCTV (125 cameras), SCR, CICO checkpoint, HR hardening |
| **31-32**    | Site & Infrastructure                | $5,016,000       | ±30%       | Grading/earthwork, MV ductbanks (dual-ring), paving/parking, stormwater basin, landscaping         |
|              |                                      |                  |            |                                                                                                    |
|              | **TOTAL (Excludes CDU/RDHx)**        | **$115,505,738** | **±23%**   |                                                                                                    |

**Note:**
- **Liquid cooling distribution (~$30M estimated):** CDUs (324 units for A/B redundancy) and RDHx units (232 units) are excluded from this total as costs will be incurred based on client-specific requirements at time of signup. See HVAC BOD Section 12.0 for details.

---

## PROJECT METRICS (PHASE 4)

| Metric                         | Value             | Calculation Basis                                 |
| ------------------------------ | ----------------- | ------------------------------------------------- |
| **Cost per MW (IT Load)**      | **$5.25M/MW**     | $115.5M ÷ 22 MW IT capacity                       |
| **Cost per kW (IT Load)**      | **$5,250/kW**     | Industry benchmark: $8-12M/MW for AI data centers |
| **Cost per SF (White Space)**  | **$5,775/SF**     | $115.5M ÷ 20,000 SF white space                   |
| **Cost per SF (Building GSF)** | **$3,040/SF**     | $115.5M ÷ 38,000 SF gross building area           |
| **Cost per Rack (394 total)**  | **$293,162/rack** | $115.5M ÷ 394 racks (162 L2C + 232 RDHx)          |

**Note:** Excludes ~$30M liquid cooling distribution (CDUs/RDHx). Add $76,142/rack if liquid cooling deployed for all racks.

---

## MAJOR COST DRIVERS (TOP 5)

### 1. Electrical Power Systems ($75.5M - 65.3% of total)
- 9×4.0 MW diesel generators @ 13.8 kV ($19.1M - 25% of electrical)
- 161 kV substation with 2×35 MVA transformers (N+1)
- 11×3,500 kVA LV transformers (13.8kV/480V, N+1)
- 23×1,250 kVA IT UPS modules + 22×250 kW mechanical UPS
- 2× prefabricated E-Houses (3,640 SF each)
- **Driver:** Tier III concurrent maintainability + 30 MW facility capacity + self-healing MV dual-ring architecture

### 2. HVAC Cooling Plant ($15.3M - 13.2% of total)
- 18 air-cooled chillers @ 1,500 kW each (12 for L2C warm water, 6 for RDHx cold water)
- Complex glycol distribution systems with overhead manifolds
- Leak detection systems (3,000 LF sensing cable, 500+ spot detectors)
- **Driver:** AI-optimized dual-temperature cooling architecture (85°F L2C + 60°F RDHx)

### 3. Facility Construction ($11.9M - 10.3% of total)
- Precast concrete tilt-up walls (~50,000 SF @ $49/SF)
- FM 1-150 tornado-rated roof with debris protection
- 38,000 SF building with 30 ft clear height in data halls
- **Driver:** Tornado hardening requirements (Oklahoma EF3+ zone)

### 4. Site & Infrastructure ($5.0M - 4.3% of total)
- 161 kV customer-owned substation yard (civil work only)
- Dual-ring 13.8 kV MV ductbanks (~3,500 LF)
- Earthwork/grading for 120-acre master plan
- **Driver:** Self-healing MV dual-ring architecture + large site development

### 5. Electronic Safety & Security ($4.2M - 3.6% of total)
- High Risk (HR) site requirements: sally port, permanent gatehouse, ballistic SCR
- 125-camera CCTV system with redundant NVR storage (90-day retention)
- Perimeter intrusion detection + access control (50+ doors with biometric MFA)
- **Driver:** HR site classification requires enhanced physical security ($620K+ premium over MR)

---

## CONFIDENCE RANGES & RISK FACTORS

### Confidence Level Analysis

**High Confidence (±15-25%):**
- Electrical: Major equipment budgetary quotes obtained, standardized systems (±20%)
- Facility Construction: Well-defined scope, standard materials, mature vendor pricing (±25%)
- Fire Suppression: NFPA-compliant systems with established RS Means pricing (±23%)
- Security: HR site requirements clearly specified, vendor quotes available (±25%)

**Medium Confidence (±25-35%):**
- HVAC: Complex liquid cooling distribution, evolving CDU/RDHx market pricing (±35%)
- Site & Infrastructure: Pre-geotechnical, pending utility coordination (±30%)
- Communications: Fiber route coordination pending, cloud on-ramp pricing variable (±33%)


---

## ITEMS NOT INCLUDED IN THIS ESTIMATE

### Excluded from CAPEX Budget

**Tenant Fit-Out & IT Equipment:**
- Customer IT equipment (servers, storage, networking)
- Customer cage/suite build-outs
- Tenant-specific modifications or custom requirements
- Liquid cooling distribution (CDUs/RDHx) deployed per customer contracts

**Commissioning & Startup:**
- Independent commissioning agent fees — ~2-3% of construction cost
- Startup power costs (energizing systems, load testing)
- Training programs for operations staff


---

**Validation Notes:**

**Confidence Assessment:**
- Overall project estimate confidence: **±23%** (ROM to budgetary level, suitable for preliminary financing)
- High-confidence divisions (±20-25%): Electrical, Construction, Fire, Plumbing, Security
- Medium-confidence divisions (±25-35%): HVAC (liquid cooling complexity), Site (pre-geotech), Communications (fiber routing TBD)

**Industry Benchmark Validation:**
- Total facility cost: **$115.5M** for 22 MW IT load = **$5.25M/MW**
- AI data center industry range: **$8-15M/MW** (high-density, tornado-hardened)
- Conventional data center range: **$8-12M/MW**
- **Assessment:** Our estimate is **conservative and competitive**, benefiting from:
  - Air-cooled chillers (no cooling tower infrastructure)
  - Self-healing MV dual-ring (eliminates duplicate UPS investment)
  - N+1 architecture vs. 2N (optimized redundancy)
  - Oklahoma location factor (lower than coastal metros)

