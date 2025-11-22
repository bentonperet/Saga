**Created:** 2025-10-22 16:15

# Mobile Edge Computing - Site Layout Requirements
## Physical Planning for Container Deployment

**Saga Energy Pryor Data Center**

**Document Purpose:** Provide detailed site planning requirements for mobile edge computing container deployment to avoid conflicts with Phase 3-5 infrastructure buildout.

**Prepared By:** PACHYDERM GLOBAL / PGCIS
**Prepared For:** Saga Energy (Site Planning Team)
**Date:** 2025-10-22
**Status:** PLANNING GUIDANCE

**Related Documents:**
- [[Excess Solar Monetization Strategy]] - Financial comparison of monetization options
- [[Why BESS Should Not Be UPS]] - Alternative BESS design approach

**Tags:** #saga-project #mobile-edge #site-planning #phase-deployment #vendor-requirements

---

## EXECUTIVE SUMMARY

### CRITICAL UPDATE (2025-10-22)

**MAJOR CORRECTION TO CONTAINER COUNT:** Previous analysis incorrectly stated 150-300 containers. Modern mobile edge computing deployments use **high-density containers** at 500-750 kW each.

**CORRECTED REQUIREMENTS:**
- **Container count:** 8-12 high-density 40-ft containers
- **Footprint:** ~1 acre total (not 7-10 acres)
- **Site conflicts:** MINIMAL — fits easily in generator yard with room to spare

### The Container Challenge

Deploying 6MW of mobile edge computing capacity in Phase 1-2 requires **8-12 high-density shipping containers** occupying **~1 acre** for 18-36 months. This is a **dramatically smaller footprint** than originally calculated.

### Critical Questions (Updated Priority)

1. **Generator yard space:** Do we have ~1 acre in generator yard for 8-12 containers? (Likely YES)
2. **Electrical distribution:** Can vendors connect to existing substation infrastructure? (Likely YES, but requires utility interconnection study)
3. **Phase 3 timeline coordination:** Can containers be removed by Month 24-28? (YES — much easier with only 8-12 units)

### Key Takeaway

**Site layout is NO LONGER a major constraint.** With only 8-12 containers on ~1 acre, placement is straightforward. The critical path item is now **utility interconnection study** (see main monetization strategy document), not physical space.

---

## 1. CONTAINER COUNT CALCULATION (CORRECTED)

### 1.1 Power Density by Container Type (Updated)

**CORRECTION:** Previous analysis used outdated power densities (20-40 kW/container). Modern mobile edge computing uses **high-density modular containers** with integrated cooling and power distribution:

| Container Type | kW per Container | Primary Use | Vendor Examples |
|----------------|------------------|-------------|-----------------|
| **High-Density GPU (Modern)** | **500-750 kW** | AI training, inference | Crusoe Energy, Applied Digital |
| **Medium-Density Mixed** | 300-400 kW | Crypto mining, rendering | Lancium |
| **Low-Density (Legacy)** | 150-200 kW | Bitcoin mining only | Older deployments |

**Key Insight:** Vendors like Crusoe Energy and Applied Digital deploy **40-ft integrated modules** containing:
- 50-100 GPUs or ASICs per container
- Integrated liquid cooling systems
- Onboard transformers and switchgear
- Power density 10-20× higher than assumed in original calculation

### 1.2 Container Count by Phase (CORRECTED)

**Phase 1 (6MW firm capacity from 7.7MW peak excess):**

| Container Density | kW/Container | Container Count | Rationale |
|-------------------|--------------|-----------------|-----------|
| **High-Density (Modern)** | 600 kW | **10 containers** | ✅ Recommended: Small footprint, AI-optimized |
| **Medium-Density** | 400 kW | **15 containers** | Mixed crypto/AI, moderate footprint |
| **Low-Density (Legacy)** | 200 kW | **30 containers** | NOT RECOMMENDED (obsolete technology) |

**Phase 2 (3MW firm capacity from 3.5MW peak excess):**
- Vendor removes 50% of containers (5 containers remaining)
- Footprint reduces to ~0.5 acres

**Phase 3 (Month 30 - full vendor exit):**
- All containers removed (10 units total)
- Site restoration: Simple grading, minimal disruption

**REVISED Planning Assumption:** **8-12 high-density containers** (600 kW avg = 10 containers for 6MW)

---

## 2. PHYSICAL SPACE REQUIREMENTS (CORRECTED)

### 2.1 Container Dimensions

**Standard 40-ft High-Density Container:**
- **External dimensions:** 8 ft wide × 40 ft long × 9.5 ft tall (may stack 2-high for some configs)
- **Footprint:** 320 sq ft per container
- **Weight (loaded):** 40,000-60,000 lbs (requires reinforced concrete pad or compacted gravel)
- **Cooling:** Integrated liquid cooling (requires water supply or closed-loop chillers)

### 2.2 Spacing Requirements (Updated)

**Fire Safety (NFPA Standards):**
- **Minimum spacing between containers:** 10-15 ft (for fire access, cooling equipment access)
- **Aisle width for maintenance vehicles:** 20 ft (allows bucket truck, refrigerant service)
- **Perimeter clearance from buildings:** 50 ft (NFPA 855 for high-density electrical equipment)

**Electrical Distribution (HIGH-DENSITY CONFIGURATION):**
- **Transformer pads:** Vendors typically provide integrated transformers (minimal site impact)
- **Medium-voltage switchgear:** 1-2 pads (12 ft × 15 ft each) for 6MW
- **Cable runs:** Medium-voltage (13.8kV or 480V) from substation to container cluster
- **NOTE:** Modern containers include onboard power distribution, reducing site infrastructure

### 2.3 Total Footprint Calculation (CORRECTED)

**Revised Layout: 10 High-Density Containers**

**Configuration: 2 rows × 5 containers per row**

```
Row Layout (East-West):
- Container length: 40 ft
- Spacing between containers: 15 ft (cooling/access)
- Row length: 5 containers × 55 ft = 275 ft

Column Layout (North-South):
- Container width: 8 ft
- Aisle width (maintenance access): 20 ft
- Column width: 2 rows × (8 ft + 20 ft) = 56 ft

Core Container Area:
275 ft × 56 ft = 15,400 sq ft = 0.35 acres
```

**Additional Infrastructure:**

| Component | Footprint | Notes |
|-----------|-----------|-------|
| **Medium-voltage switchgear** | +0.05 acres | 2 pads (12 ft × 15 ft each) |
| **Cooling equipment** | +0.10 acres | Chillers or cooling towers (if not integrated) |
| **Perimeter fencing** | +0.15 acres | 8-ft chain-link around container cluster |
| **Access roads** | +0.20 acres | Single 20-ft gravel access road |
| **Vendor staging/office** | +0.05 acres | 1 office trailer (optional) |

**Total Land Use: 0.90 acres** (for 10 containers, 6MW)

**With 10% contingency for irregular site geometry:** **~1.0 acre required**

**THIS IS A 90% REDUCTION from original 8-10 acre estimate.**

---

## 3. POTENTIAL SITE LOCATIONS

### 3.1 Option 1: Generator Yard Expansion

**Description:**
- Extend existing generator yard northward/westward
- Containers adjacent to backup generators and fuel storage
- Leverage existing substation interconnection and security fencing

**Advantages:**
- ✅ Power distribution already in place (reduces CAPEX $100-200k)
- ✅ Security fencing, access roads, grading already complete
- ✅ Close to electrical substation (minimal voltage drop)
- ✅ Isolated from main DC building (fire separation maintained)

**Disadvantages:**
- ❌ May need this space for Phase 4-5 additional generators (5×4MW → 8×4MW)
- ❌ Fuel truck access conflicts during refueling operations
- ❌ Noise from containers + generators may exceed site limits

**Conflict Risk: MEDIUM**
- Phase 3: Low conflict (no generator expansion needed yet)
- Phase 4-5: High conflict (need space for 3 additional 4MW turbines)

**Mitigation:**
- Reserve western 3 acres for future generator expansion
- Place containers in northern/eastern sections only
- Include site restoration clause: "Containers removed by Month 30, area graded for future generator pads"

---

### 3.2 Option 2: Solar Field Integration

**Description:**
- Deploy containers between or underneath solar array rows
- Utilize land already designated for solar infrastructure
- Containers consume power generated directly adjacent

**Advantages:**
- ✅ Minimal additional land use (dual-purpose solar/compute area)
- ✅ Shortest electrical runs (solar inverters → containers)
- ✅ Shading from containers may reduce solar panel temperature (marginal efficiency gain)
- ✅ Unlikely to conflict with Phase 3-5 building footprints

**Disadvantages:**
- ❌ Interferes with solar array maintenance (panel cleaning, tracker repairs)
- ❌ Shading from containers reduces solar production (~5-10% loss)
- ❌ Vehicle access between arrays limited (fire truck access concerns)
- ❌ May violate solar site lease terms (if land leased vs. owned)

**Conflict Risk: LOW-MEDIUM**
- Phase 3: Low conflict (solar array remains operational)
- Future: Medium conflict if planning solar array expansion

**Mitigation:**
- Deploy containers only in "dead zones" (areas already shaded by trees, buildings)
- Use elevated solar tracking systems with 12-ft clearance (containers fit underneath)
- Confirm solar site control documents allow temporary structures

---

### 3.3 Option 3: Future Phase 4-5 Construction Staging Area

**Description:**
- Occupy land designated for Phase 4-5 data hall expansion
- Temporary use during Phase 1-2, cleared before Phase 3 construction
- Likely the largest open space available on campus

**Advantages:**
- ✅ Largest available footprint (10-20 acres typically reserved)
- ✅ Flat, graded land suitable for container deployment
- ✅ Far from existing buildings (fire separation not an issue)
- ✅ Can co-locate with construction laydown yard initially

**Disadvantages:**
- ❌ MUST be cleared by Month 24-30 (Phase 3 mobilization)
- ❌ May require longer power runs from substation (+$200-400k CAPEX)
- ❌ Conflicts with early Phase 3 site prep (geotechnical borings, utility marking)
- ❌ Site restoration required (remove gravel, restore drainage)

**Conflict Risk: HIGH**
- Phase 3: HIGH conflict (construction mobilization begins Month 24)
- Requires firm vendor exit commitment by Month 30 or earlier

**Mitigation:**
- **Contract clause:** "Vendor must demobilize 100% containers within 60 days of written notice"
- **Phased removal:** 50% containers removed by Month 20, remaining 50% by Month 28
- **Site restoration bond:** Vendor posts $100k bond for grading, drainage restoration
- **Alternative site identified:** If Phase 3 accelerates, vendor relocates to Option 1 or 2

---

### 3.4 Recommended Site Selection Matrix (UPDATED FOR ~1 ACRE FOOTPRINT)

**KEY CHANGE:** With only ~1 acre required (vs. 7-10 acres), all site options are now LOW RISK.

| Criteria | Generator Yard | Solar Field | Future Construction Area |
|----------|----------------|-------------|--------------------------|
| **Available Space** | ✅ 1 acre easily fits | ✅ 1 acre easily fits | ✅ 1 acre easily fits |
| **CAPEX (Power Dist.)** | Low ($100-150k) | Low ($150-200k) | Medium ($300-400k) |
| **Phase 3 Conflict** | **LOW** (minimal footprint) | **LOW** | Medium (still must exit) |
| **Phase 4-5 Conflict** | **LOW** (1 acre easy to work around) | Low | Low |
| **Fire Separation** | ✅ OK (50+ ft) | ✅ OK (100+ ft) | ✅ Excellent (200+ ft) |
| **Maintenance Access** | ✅ Good | Medium (solar access) | ✅ Excellent |
| **Vendor Exit Risk** | **LOW** (10 containers easy to remove) | **LOW** | Medium |
| **Overall Risk Score** | **LOW** ✅ | **LOW-MEDIUM** | **MEDIUM** |

**REVISED Recommendation (2025-10-22):**

**1. FIRST CHOICE: Generator Yard Expansion** ✅
- Only 1 acre needed — easily fits without Phase 4-5 generator conflicts
- Lowest CAPEX ($100-150k power distribution)
- Existing fencing, access roads, security
- Close to substation (minimal interconnection complexity)
- **THIS IS NOW THE CLEAR WINNER**

**2. Second Choice:** Solar Field Integration
- 1 acre footprint reduces solar shading impact to <1%
- Good technical fit, but adds operational complexity (solar maintenance coordination)
- Slightly higher CAPEX vs. generator yard

**3. Third Choice:** Future Construction Area
- Not needed — Generator yard easily accommodates 1 acre
- Only consider if generator yard unavailable for other reasons

---

## 4. PHASE 3-5 INFRASTRUCTURE CONFLICTS

### 4.1 Conflict Types and Risk Assessment

| Conflict Type | Description | Risk Level | Mitigation |
|---------------|-------------|------------|------------|
| **Building Footprints** | Containers occupy Phase 3 data hall location | **CRITICAL** | Master plan overlay showing container area excludes Phase 3 building pad |
| **Construction Access** | Container yard blocks crane staging, material delivery | **HIGH** | Maintain 50-ft access corridor along south/east property lines |
| **Underground Utilities** | Containers placed over future conduit runs, fiber, water lines | **HIGH** | Utility master plan marks "no-build zones" for future infrastructure |
| **Fire Apparatus Access** | NFPA requires 20-ft fire lane around Phase 3 building | **MEDIUM** | Container perimeter must be 70+ ft from Phase 3 building footprint |
| **Substation Expansion** | Phase 4 requires additional transformer pads, switchgear | **MEDIUM** | Reserve 100-ft radius around existing substation for future growth |
| **Storm Water Management** | Containers create impervious surface, alter drainage patterns | **LOW** | Temporary erosion control, restore site to original grade upon removal |
| **Telecom/Fiber** | Vendor internet drops conflict with Phase 3 backbone routes | **LOW** | Use temporary aerial fiber, remove before Phase 3 underground install |

### 4.2 Timeline Coordination (SIMPLIFIED WITH 10 CONTAINERS)

**Critical Milestones (Updated):**

| Month | Event | Container Deployment Status | Required Action |
|-------|-------|----------------------------|-----------------|
| **0** | Phase 1 DC operational | Deploy 10 containers (6MW) | Site prep, vendor mobilization |
| **12** | Phase 2 DC expansion | Reduce to 5 containers (3MW) | Vendor removes 50% containers |
| **20** | Phase 3 design complete | 5 containers remain | Review Phase 3 master plan (likely no conflicts) |
| **24** | Phase 3 construction begins | **Begin removal** | Vendor removes remaining containers |
| **26-28** | Phase 3 site grading starts | **All containers removed** | Site restoration (minimal — only 1 acre) |
| **30** | Phase 3 building foundation | Site available for use | Grading, utility installation |

**Key Insight (UPDATED):** With only 10 containers on ~1 acre, removal is MUCH SIMPLER. Vendor can complete 100% removal in **2-4 weeks** (vs. 6-12 months for 200 containers). Timeline risk is now **LOW**.

---

## 5. VENDOR RFI REQUIREMENTS

### 5.1 Site Planning Questions for Vendors

**Include in RFI to Crusoe Energy, Lancium, Applied Digital:**

**1. Container Specifications:**
   - Power consumption per container (kW)?
   - Physical dimensions (assume 40-ft standard, but confirm)?
   - Weight (loaded with equipment)?
   - Cooling method (air-cooled, liquid-cooled, evaporative)?

**2. Footprint Requirements:**
   - How many containers for 6MW capacity?
   - Minimum spacing between containers (fire safety)?
   - Aisle width needed for maintenance vehicles?
   - Total acreage required (including perimeter, access roads)?

**3. Site Preparation:**
   - Surface requirements (gravel, concrete, asphalt)?
   - Grading/drainage specifications?
   - Environmental permits needed (stormwater, air quality)?
   - Timeline from site prep to revenue generation?

**4. Electrical Distribution:**
   - Voltage requirements (480V, 13.8kV, other)?
   - Number and size of transformers needed?
   - Cable trench depth and routing?
   - Who provides transformers (vendor or site owner)?

**5. Removal and Demobilization:**
   - How long to remove 100 containers (days/weeks)?
   - Site restoration scope (who pays for grading, reseeding)?
   - Can you stage partial removal (50% Month 24, 50% Month 28)?
   - Liquidated damages for delayed removal?

**6. Flexibility and Relocation:**
   - Can containers be relocated mid-contract if site conflicts arise?
   - Cost to move containers within site ($/container)?
   - Early termination penalty if Phase 3 accelerates?

### 5.2 Required Vendor Deliverables

**Site Layout Drawing (Required in RFI Response):**
- **Scale:** 1" = 100 ft (or CAD file in DWG/DXF format)
- **Content:**
  - Container locations (numbered grid)
  - Transformer pads and switchgear locations
  - Cable trench routes
  - Access roads and vehicle turnaround areas
  - Perimeter fencing
  - Fire apparatus access lanes (20-ft minimum)
  - Setbacks from property lines and existing buildings

- **Overlay with Saga master plan:** Vendor drawing must show compatibility with Phase 3-5 infrastructure

**Removal Plan (Required in Contract):**
- **Timeline:** Month-by-month removal schedule
  - Month 20: Begin removal (50 containers)
  - Month 24: 50% removed (100 containers)
  - Month 28: 100% removed (0 containers)

- **Site Restoration:**
  - Remove all containers, transformers, switchgear
  - Remove perimeter fencing and access roads (unless Saga wants to retain)
  - Backfill cable trenches, compact to 95% density
  - Restore site to original grade (±6 inches)
  - Reseed with native grasses (if required)

- **Financial Guarantee:**
  - Performance bond: $100-200k (ensures removal completion)
  - Liquidated damages: $10k/day for delayed removal beyond Month 30

---

## 6. SITE PLANNING CHECKLIST

### 6.1 Pre-RFI Actions (Before Issuing Vendor RFI)

**Site Analysis:**
- [ ] Obtain current site master plan (all phases)
- [ ] Identify 7-10 acre "temporary use zone" candidates
- [ ] Verify property boundaries and easements
- [ ] Review utility master plan (underground conduits, fiber routes)
- [ ] Confirm Phase 3-5 building footprints and construction access needs

**Civil Engineering Review:**
- [ ] Assess soil bearing capacity (can support 40,000 lb containers?)
- [ ] Review storm water drainage (containers add impervious surface)
- [ ] Identify utility conflicts (gas, water, sewer, electrical)
- [ ] Confirm fire truck access and turnaround radius (150 ft min)

**Regulatory Compliance:**
- [ ] Zoning: Do temporary structures require permits?
- [ ] Environmental: Stormwater permit needed for 7+ acres disturbance?
- [ ] Fire Marshal: Pre-approval for 200 containers with electrical equipment?
- [ ] FAA: Site near airport? Container height restrictions?

### 6.2 Post-RFI Actions (After Vendor Proposals Received)

**Vendor Proposal Review:**
- [ ] Does vendor's site layout fit within identified temporary use zone?
- [ ] Are setbacks from Phase 3-5 infrastructure adequate (50+ ft)?
- [ ] Is removal timeline realistic (100% demobilized by Month 28)?
- [ ] Does vendor have equipment/labor to execute staged removal?

**Master Plan Integration:**
- [ ] Overlay vendor site plan with Phase 3-5 master plan (check conflicts)
- [ ] Confirm construction access corridors remain clear (20-ft minimum)
- [ ] Verify fire apparatus access to Phase 3 building (no obstructions)
- [ ] Check utility routing: Do cable trenches cross future building pads?

**Contract Provisions:**
- [ ] Include detailed removal timeline with monthly milestones
- [ ] Liquidated damages clause: $10k/day for delayed removal
- [ ] Site restoration bond: $100-200k posted before mobilization
- [ ] Right to relocate containers if Phase 3 accelerates (Saga pays $/container)
- [ ] Early termination option: 90-day notice with prorated revenue adjustment

---

## 7. RISK MITIGATION STRATEGIES

### 7.1 Schedule Risk: Phase 3 Accelerates

**Risk:** If Phase 3 construction begins early (Month 20 instead of Month 24), vendor may not have time to remove containers.

**Mitigation:**
1. **Contract clause:** "Saga may accelerate removal timeline with 120-day written notice"
2. **Incentive payment:** Saga pays $50k bonus for removal completed 90+ days early
3. **Alternative site:** Identify Option 1 or 2 as fallback relocation area
4. **Vendor pre-qualification:** Only accept vendors with demobilization track record

### 7.2 Site Restoration Risk: Vendor Abandons Containers

**Risk:** Vendor goes bankrupt or breaches contract, leaving 200 containers on-site.

**Mitigation:**
1. **Performance bond:** $200k bond from AAA-rated surety company
   - Triggered if vendor doesn't remove containers within 30 days of contract end
   - Saga uses bond to hire third-party removal contractor

2. **Monthly holdback:** Retain 10% of lease payments ($40-50k/month)
   - Escrow account released upon successful site restoration
   - Accumulated holdback: $1.0-1.5M over 24 months (covers removal cost)

3. **Parent company guarantee:** If vendor is subsidiary, require parent guarantee
   - Example: Crusoe Energy parent company guarantees removal obligations

### 7.3 Utility Conflict Risk: Containers Damage Underground Lines

**Risk:** Installing containers or power distribution accidentally cuts fiber, gas, water lines.

**Mitigation:**
1. **Pre-deployment utility locates:** Oklahoma 811 call before any excavation
2. **As-built drawing:** Vendor provides surveyed drawing of cable trenches, transformer pads
3. **Ground-penetrating radar (GPR):** Scan site before digging if utility records incomplete
4. **Minimum depth:** All new cable trenches ≥36 inches (below frost line, above existing utilities)

---

## 8. FINANCIAL IMPLICATIONS (UPDATED FOR 10 CONTAINERS)

### 8.1 CAPEX Impact by Site Location (REVISED)

**MAJOR CHANGE:** With only 10 containers (~1 acre), site prep costs are MUCH LOWER and less variable by location.

| Site Location | Power Distribution | Site Prep | Total Incremental CAPEX |
|---------------|-------------------|-----------|-------------------------|
| **Generator Yard** ✅ | $100-150k (short runs) | **$25-50k** (minimal grading, 1 acre) | **$125-200k** |
| **Solar Field** | $150-200k (moderate runs) | **$30-60k** (minimal impact) | **$180-260k** |
| **Future Construction Area** | $300-400k (long runs) | **$50-100k** (longer access road) | **$350-500k** |

**Impact on Option B NPV (CORRECTED):**
- **BEST CASE (Generator Yard):** CAPEX reduced to $125-200k (vs. original $150-300k estimate)
- **NPV IMPROVEMENT:** $12.2M → **$12.3M** (slightly better than original)
- If forced to use Future Construction Area: $350-500k CAPEX
- **NPV still strong:** $11.8-12.0M

**KEY INSIGHT:** Lower CAPEX due to smaller footprint **improves** Option B economics.

### 8.2 Risk-Adjusted CAPEX Range (UPDATED)

**Base Case (Generator Yard - RECOMMENDED):**
- CAPEX: $125-200k ✅
- NPV: **$12.3M** (improved from original $12.2M)
- **Capital Efficiency: 62× NPV/CAPEX** (vs. original 54×)

**Contingency Case (Solar Field):**
- CAPEX: $180-260k
- NPV: $12.1-12.2M
- Still excellent economics

**Worst Case (Forced Early Removal at Month 20):**
- Revenue loss: 8 months × $390k/month = $3.1M
- NPV: $9.2M (still 5-6× better than Option A: $1.5-2.5M)

**CONCLUSION:** Container count correction **strengthens** the financial case for Option B by reducing CAPEX $25-100k.

---

## 9. DECISION FRAMEWORK

### 9.1 Go/No-Go Criteria (UPDATED - MUCH SIMPLER)

**Proceed with Mobile Edge Computing (Option B) if:**

✅ **Site master plan confirms ~1 acre available in generator yard** (HIGHLY LIKELY)

✅ **Utility interconnection study successful:**
   - Upgrade costs <$500k
   - Timeline <9 months
   - This is now the **PRIMARY GATING FACTOR** (not site layout)

✅ **Vendor commits to removal timeline:**
   - 100% removed by Month 26-28 (2-4 weeks for 10 containers)

✅ **CAPEX remains ≤$200k** (site prep only — interconnection costs separate)

**Do NOT proceed if:**

❌ **Utility interconnection study fails** (>$1M costs or >12 month timeline) ← **MAIN RISK**

❌ No qualified vendors available (Crusoe, Lancium, Applied Digital all decline)

❌ Lenders reject mobile compute revenue in DSCR calculations

**KEY CHANGE:** Site layout is no longer a constraint. Focus on **interconnection study** as critical path item.

---

## 10. NEXT STEPS

### 10.1 Immediate Actions (Week 1-2)

1. **Obtain site master plan** from civil engineer:
   - Phase 1-5 building footprints
   - Utility master plan (underground and overhead)
   - Construction access and laydown areas
   - Future generator/transformer expansion areas

2. **Site visit with civil engineer:**
   - Walk three potential container locations
   - Mark boundaries with GPS
   - Photo documentation of existing conditions
   - Identify any obvious conflicts (trees, drainage, easements)

3. **Preliminary site layout sketch:**
   - 200 containers in grid pattern
   - Overlay with Phase 3-5 infrastructure
   - Identify conflicts and mitigation options

### 10.2 RFI Development (Week 2-3)

4. **Draft vendor RFI** including:
   - Site layout drawing requirements
   - Removal timeline and site restoration specs
   - Performance bond and liquidated damages terms
   - Questions from Section 5.1

5. **Issue RFI to vendors:**
   - Crusoe Energy
   - Lancium
   - Applied Digital
   - [Other vendor names from earlier conversations]

6. **RFI response deadline:** 2 weeks from issue date

### 10.3 Vendor Evaluation (Week 4-5)

7. **Review vendor site layouts:**
   - Overlay with master plan (check conflicts)
   - Verify setbacks and access requirements
   - Assess CAPEX estimates (power distribution, site prep)

8. **Civil engineer review:**
   - Approve vendor site layout
   - Identify any utility conflicts
   - Confirm removal timeline is realistic

9. **Go/No-Go decision:**
   - If approved: Proceed to contract negotiation
   - If conflicts: Evaluate Option A (Grid Export) or Option C (BESS)

---

## APPENDIX A: EXAMPLE SITE LAYOUT (CORRECTED)

**10 High-Density Containers, 6MW Capacity, Generator Yard Location**

```
SITE PLAN - MOBILE EDGE COMPUTING DEPLOYMENT (UPDATED 2025-10-22)
Saga Energy Pryor Data Center - Generator Yard Extension

Scale: 1" = 50 ft

┌─────────────────────────────────────────────────────┐
│                 PROPERTY LINE (NORTH)                │
│                                                       │
│  [Phase 3 Building Reserved Area - NO CONFLICT] ──→ │
│                                                       │
│  ┌───────────────────────────┐                      │
│  │  PERIMETER FENCE (8-FT)   │                      │
│  │  ╔════════════════════╗   │                      │
│  │  ║  ROW 1 (North):    ║   │                      │
│  │  ║  [C][C][C][C][C]   ║   │  ← 5 containers      │
│  │  ║  ←─── 275 ft ────→ ║   │     600 kW each      │
│  │  ║                    ║   │     = 3MW            │
│  │  ║  ↕ 20 ft aisle     ║   │                      │
│  │  ║                    ║   │                      │
│  │  ║  ROW 2 (South):    ║   │                      │
│  │  ║  [C][C][C][C][C]   ║   │  ← 5 containers      │
│  │  ║                    ║   │     600 kW each      │
│  │  ╚════════════════════╝   │     = 3MW            │
│  │                           │                      │
│  │  [SW1] [SW2]              │  ← Medium-voltage    │
│  │   Switchgear (2 pads)     │     switchgear       │
│  │                           │                      │
│  └───────────────────────────┘                      │
│         Total: ~1.0 acre                             │
│                                                       │
│  ──── Access Road (20 ft gravel) ────                │
│                                                       │
│  [GEN] [GEN] [GEN] [GEN]  Existing Generators        │
│   ← 50 ft clearance                                  │
│                                                       │
│  [SUBSTATION] ← 200 ft cable run                     │
│                                                       │
└─────────────────────────────────────────────────────┘
         PROPERTY LINE (SOUTH)

Legend:
[C] = High-density 40-ft container (40 ft × 8 ft, 600 kW)
[SW] = Medium-voltage switchgear pad (12 ft × 15 ft)
[GEN] = Existing backup generator (20 ft × 8 ft)

Setbacks:
- 50 ft from existing generators (fire separation) ✅
- 100+ ft from Phase 3 building footprint (east) ✅
- 30 ft from property line (north/west) ✅

Total Footprint: 1.0 acre (90% reduction from original 8.2 acre estimate)

Removal Timeline: 2-4 weeks (vs. 6-12 months for 200 containers)
```

---

**Document Status:** CORRECTED PLANNING GUIDANCE
**Critical Update:** Container count error corrected (200 → 10 containers)
**Next Review:** After utility interconnection study complete (Week 8-12)
**Owner:** Site Planning Team / Civil Engineer

**Key Takeaway:** Site layout is now a **LOW RISK** item. Focus on utility interconnection study as the critical path.
