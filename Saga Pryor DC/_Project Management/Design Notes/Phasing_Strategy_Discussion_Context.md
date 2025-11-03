**Created:** 2025-11-03
**Tags:** #phasing #strategy #customer-profiles #capacity-planning
**Status:** Active Discussion

# Pryor DC Phasing Strategy - Discussion Context

## Facility Parameters

**Data Halls:**
- 2× 10,000 sq ft halls = 20,000 sq ft total
- **Capacity:** 140 racks per hall (280-300 total facility) - MUCH higher than initial 30-rack estimate
- **Power ceiling:** 24 MW ultimate capacity
- **Liquid cooling:** D2C (direct-to-chip) capability from day 1

**Location Advantage:**
- **4 miles from Google DC campus** in Pryor, OK
- Direct GCP connectivity = ultra-low latency
- Makes facility ideal for **AI inference workloads**

---

## Customer Profiles (Priority Order)

### Customer #1: AI Inference Hub (GCP Ecosystem)
**Phasing:** Priority 1 (Anchor Tenant)

**Need:**
- Ultra-low latency to Google's us-central2 region
- Real-time AI (chat, recommendations, autonomous systems)

**Specs:**
- **Density:** 30-60 kW/rack
- **Cooling:** High-density air (RDHX) or D2C (flexible - customer choice)
- **Power:** Tier III (N+1 UPS)
- **Criticality:** 24/7 mission-critical

**Why they choose Pryor:**
- Sub-millisecond latency to GCP
- Cost-effective power vs. coastal markets
- Liquid cooling ready

---

### Customer #2: AI Training Cluster (AI Cloud Providers)
**Phasing:** Priority 1 or 2

**Need:**
- Massive parallel GPU power for building large models
- Less latency-sensitive but extremely power-hungry

**Specs:**
- **Density:** Ultra-high (70-130+ kW/rack)
- **Cooling:** D2C mandatory
- **Power:** Tier III (N+1 UPS)
- **Criticality:** 24/7 compute clusters

**Why they choose Pryor:**
- Cheap power (critical for training costs)
- Liquid cooling infrastructure
- Proximity to Google's data/models (if partnered)

---

### Customer #3: Industrial Enterprise (MAIP Tenants)
**Phasing:** Priority 2 (Multi-Tenant Fill)

**Need:**
- Local, high-reliability compute (digital twins, IoT, manufacturing lines)
- Oklahoma industrial base (aerospace, energy, ag-tech)

**Specs:**
- **Density:** Mixed (8-25 kW/rack)
- **Cooling:** Standard air-cooling
- **Power:** Tier III (N+1 UPS)
- **Criticality:** High reliability but not bleeding-edge

**Why they choose Pryor:**
- Local presence (Oklahoma/Arkansas industrial corridor)
- Tier III reliability
- Lower cost than Dallas/Kansas City

---

### Customer #4: Specialty Compute (Capacity Filler)
**Phasing:** Priority 3 (Margin Optimizer)

**Need:**
- Lowest possible cost-per-kilowatt
- Can tolerate outages (crypto, rendering, batch processing)

**Specs:**
- **Density:** High (30-80 kW/rack)
- **Cooling:** Hot-aisle containment (can tolerate high temps)
- **Power:** **Interruptible / Non-UPS** ← KEY DIFFERENTIATOR
  - Fed directly from substation (bypass UPS)
  - Can shed load during grid emergencies
  - 30-40% lower power pricing

**Why they choose Pryor:**
- Cheap power (no UPS cost overhead)
- Accepts interruptibility for lower rates
- High-density capability

**Electrical Implication:**
Requires **third power distribution path:**
1. Tier III Critical (IT UPS) - Customers #1, #2, #3
2. House Power (Non-Critical) - Building services
3. **Interruptible Power (Non-UPS)** - Customer #4

---

## Current BOD Phasing (2-Phase Model)

### Phase 1: 3 MW
- 30 cabinets @ 100 kW each = 3,000 kW
- Data Hall E operational, Data Hall W powered shell
- Air cooling only (Loops 1+2, 4× 1,500 kW chillers)
- 3× generators, 3× transformers, 5× IT UPS modules

### Phase 2: 12 MW
- Same 30 cabinets upgraded to 400 kW each = 12,000 kW
- Add D2C cooling (Loop 3, 8× 1,500 kW chillers, 60 CDUs)
- Add 3× generators (6 total), 5× transformers (8 total), 8× IT UPS modules (13 total)

**Problem with 2-phase model:**
- Huge jump from 3 MW → 12 MW (4× capacity increase)
- Doesn't match realistic lease-up/revenue curve
- Doesn't account for customer mix (inference vs training vs enterprise)
- Assumes all 30 cabinets densify together (unlikely in reality)

---

## Proposed Phasing Models

### User's Initial Instinct (4-Phase Model)
1. **Phase 1:** 3 MW, low density, prove market (DH-E)
2. **Phase 2:** Stay in DH-E, add some dense racks
3. **Phase 3:** Open DH-W, continue growth
4. **Phase 4:** Full 24 MW buildout

**This is directionally correct** ✓

---

### Claude's Refined Proposal (Based on Customer Mix)

#### Phase 1: Foundation (3-4 MW) - 12-18 months
**Goal:** Prove operations, attract anchor tenants (Customers #1 and #2)

**Data Hall E Layout:**
- **West Zone (Inference):** 40 racks @ 30-60 kW avg = 1.2-2.4 MW
  - Customer #1 (AI Inference)
  - Flexible cooling (RDHX or D2C customer choice)
  - Loops 1+2 (air) + Loop 3 (D2C) available

- **East Zone (Training):** 20 racks @ 100-130 kW = 2.0-2.6 MW
  - Customer #2 (AI Training)
  - D2C mandatory
  - Loop 3 primary

**Total Phase 1:** 60 racks, 3.2-5.0 MW flexible

**Infrastructure:**
- **Mechanical:**
  - Loops 1+2: 3× 1,000 kW chillers (N+1 for 2.4 MW air)
  - Loop 3: 3× 1,000 kW chillers (N+1 for 2.6 MW D2C)
- **Electrical:**
  - 3× 4 MW generators (N+1)
  - 3× 3.5 MVA transformers
  - Interruptible power roughed-in (not commissioned yet)
- **Data Halls:**
  - DH-E: Both zones fully built and commissioned
  - DH-W: Shell built, roughed-in, not commissioned

**Rationale:**
- ✅ Tests both air and D2C cooling in production
- ✅ Can sign both priority customer types immediately
- ✅ Chiller loading reasonable (65-85% utilization at full Phase 1)
- ✅ Proves market before big Phase 2 investment

---

#### Phase 2: Multi-Tenant Fill (6-10 MW) - 12-18 months after Phase 1
**Goal:** Fill remaining DH-E capacity, add Customer #3 (Industrial/Enterprise)

**Add to DH-E:**
- Fill remaining ~80 racks (140 total per hall capacity)
- Mix of Customers #1, #2, #3 based on demand
- Commission interruptible power for Customer #4 (if demand exists)

**Infrastructure Adds:**
- **Mechanical:**
  - Loops 1+2: Add 1-2× 1,000 kW chillers
  - Loop 3: Add 2-3× 1,500 kW chillers (now at scale)
- **Electrical:**
  - Add 1× generator (4 total) if needed
  - Add 2× transformers (5 total)
  - Commission interruptible distribution panels

**Total Facility:** 6-10 MW (Tier III + interruptible mix)

---

#### Phase 3: Second Data Hall (12-18 MW) - 12-24 months after Phase 2
**Goal:** Commission DH-W, replicate DH-E success

**DH-W Commissioning:**
- Mirror DH-E layout (inference zone + training zone)
- ~60-80 racks Phase 3, reserve ~60 for Phase 4
- All customer types available

**Infrastructure Adds:**
- **Mechanical:** Add chillers to match growth
- **Electrical:** Add 1-2× generators (5-6 total), 2-3× transformers (7-8 total)

**Total Facility:** 12-18 MW

---

#### Phase 4: Full Build-Out (20-24 MW) - As demand dictates
**Goal:** Fill all remaining capacity

**Fill DH-W + Densify DH-E:**
- Target ~200-250 racks total deployed

**Infrastructure Completion:**
- Final generators (6 total), transformers (8 total)
- All planned chillers

**Total Facility:** 20-24 MW

---

## Key Questions Still Open

### 1. Chiller Sizing Strategy
**Options:**
- **A:** Stick with 1,500 kW chillers throughout, accept lower efficiency early phases
- **B:** Right-size chillers to match phased loads (smaller in Phase 1, upsize later) ← Recommended
- **C:** Hybrid (small Phase 1, standardize 1,500 kW by Phase 2+)

**Issue:** Chillers run poorly below 40% load. If Loop 3 has 12 MW capacity (8× 1,500 kW) but only 600 kW load in Phase 1, efficiency tanks.

---

### 2. Phase 1 D2C Infrastructure
**Options:**
- **A:** Include small D2C capability from day 1 (2× chillers, CDU piping roughed-in) ← Recommended
- **B:** Truly start 100% air-cooled, add D2C in Phase 2

**Trade-off:** Option A costs more upfront but can serve Customer #2 (AI Training) immediately.

---

### 3. Generator Phasing
**Options:**
- **A:** Gradual additions (2 → 3 → 5 → 6) ← Spreads CAPEX
- **B:** Current plan (3 → 6) ← Fewer construction mobilizations

**Recommendation:** Gradual (matches revenue curve better)

---

### 4. DH-W Shell Timing
**Options:**
- **A:** Build shell in Phase 1 (enables faster Phase 3 deployment)
- **B:** Wait until Phase 2/3 (preserves cash)

**Trade-off:** Time vs. money

---

### 5. Density Progression
Does the ~60 kW → ~130 kW → ~165 kW average density curve feel realistic?
- Or expect faster jump to high-density AI workloads?
- Depends on how quickly Customer #2 (Training) leases vs. Customer #3 (Enterprise)

---

## Mechanical System Implications

### Air Cooling (Loops 1+2)
**Serves:**
- Customer #1 air-cooled portion (RDHX option)
- Customer #3 (Industrial/Enterprise)
- Building support systems

**Load Profile:**
- Predictable, stable
- ±10% diurnal variation
- Traditional HVAC controls work well

---

### D2C Cooling (Loop 3)
**Serves:**
- Customer #2 (AI Training)
- Customer #1 D2C option (Inference)

**Load Profile:**
- **Violent swings:** 0-100% in seconds (GPU jobs launch/stop)
- **Unpredictable:** AI/ML batch jobs
- Requires aggressive control tuning

**Why Separate from Air Cooling:**
- Different control strategies
- Prevents hunting/instability if mixed
- Clear contractor boundaries

---

### Chiller Plant Phasing (Proposed)

| Phase | Air Load (Loops 1+2) | D2C Load (Loop 3) | Interruptible (Customer #4) | Chillers L1+2 | Chillers L3 |
|-------|---------------------|-------------------|----------------------------|---------------|-------------|
| **1** | 1.2-2.4 MW | 2.0-2.6 MW | 0 (roughed-in) | 3× 1,000 kW | 3× 1,000 kW |
| **2** | 2.5-4.0 MW | 3.0-5.0 MW | 0.6-2.4 MW | 4-5× 1,000 kW | 4-5× 1,500 kW |
| **3** | 4.0-6.0 MW | 6.0-10.0 MW | 1.0-3.0 MW | 6× 1,500 kW | 7× 1,500 kW |
| **4** | 4.0-6.0 MW | 10.0-16.0 MW | 2.0-4.0 MW | 6× 1,500 kW | 10× 1,500 kW |

---

## Electrical System Implications

### Three Power Paths Required

**Path 1: Tier III Critical (IT UPS)**
- Customers #1, #2, #3
- 345 kV → 13.8 kV dual-ring → transformers → IT UPS → IT distribution

**Path 2: House Power (Non-Critical)**
- Building services (offices, HVAC, lighting)
- Natural gas generators for backup
- Portable UPS for NOC/security

**Path 3: Interruptible (Non-UPS)** ← NEW
- Customer #4 (Specialty Compute)
- 345 kV → 13.8 kV → transformers → direct 480V distribution (bypass UPS)
- Automatic load-shedding capability
- 30-40% lower power pricing

**Design Now, Commission Later:**
- Rough-in interruptible distribution panels in Phase 1
- Size electrical yard for future interruptible transformers
- Commission in Phase 2 when Customer #4 demand materializes

---

## Next Steps: Finalize Phasing Plan

**Decisions needed:**
1. Number of phases (3, 4, or 5?)
2. Phase 1 scope:
   - Air-only (simpler) vs. Mixed air+D2C (serves more customers)
   - DH-W shell timing (Phase 1 build vs. Phase 2+ build)
3. Chiller sizing strategy (right-size vs. standardize)
4. Generator phasing (gradual vs. batched)
5. Interruptible power priority (Phase 1 rough-in vs. Phase 2+ consideration)

**Once phasing locked:**
- Update BOD documents with finalized phase definitions
- Create SLD diagrams for each phase (Mermaid in Obsidian)
- Update equipment schedules and cost estimates
- Revise construction timeline

---

**Context saved:** 2025-11-03 15:00
**Ready to continue:** Waiting for user decisions on open questions
