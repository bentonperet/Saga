**Created:** 2025-11-19 15:15
**Tags:** #building-h #generators #correction #schematics #analysis
**Related:** [[Commissioning Plan - Building H Summary]], [[Commissioning Plan Alignment Analysis - Building H]]

---

# CORRECTED: Building H Generator Analysis Based on Electrical Schematics

## Executive Summary

After reviewing the actual electrical one-line diagrams for Building H, I can now provide a **DEFINITIVE ANSWER** to the generator question that reconciles all apparent conflicts:

**FINDING:** Building H has **BOTH generator-backed AND utility-only power blocks**, creating a hybrid configuration.

---

## Complete Building H Power Architecture (From Schematics)

### Power Block Types in Building H

Based on the electrical one-line diagrams (E07-12A through E07-12L), Building H contains:

| Block Type | Quantity | Generator-Backed? | Generator Type | Notes |
|------------|----------|-------------------|----------------|-------|
| **MA Blocks** (GPU Mechanical) | 8 | ❌ **NO** | N/A - Utility only | SWBD-MA-01H through MA-08H |
| **MB Blocks** (Mechanical) | 3 | ✅ **YES** | 2 × 1.25 MW per block | SWBD-MB-01H, MB-02H, MB-03H |
| **PA Blocks** (GPU Power) | 18 | ❌ **NO** | N/A - Utility only | SWBD-PA-01H through PA-18H |
| **PB Blocks** (IT Power) | 6 | ✅ **YES** | 2 × 1.25 MW per block | SWBD-PB-01H through PB-06H |
| **RA Block** (GPU Reserve) | 1 | ❌ **NO** | N/A - Utility only | SWBD-RA-01H |

**TOTAL POWER BLOCKS:** 36 blocks in Building H

---

## Generator Configuration - DETAILED BREAKDOWN

### Generator-Backed Blocks (9 blocks total)

**MB Blocks (Mechanical) - 3 blocks:**
- Each MB block has **2 × 1.25 MW diesel generators**
- Generator naming: GEN-MB-0XH-1 and GEN-MB-0XH-2
- Configuration: Parallel operation (2.5 MW total per block when paralleled)
- Total for MB blocks: **6 generators = 7.5 MW capacity**

**PB Blocks (IT Power) - 6 blocks:**
- Each PB block has **2 × 1.25 MW diesel generators**
- Generator naming: GEN-PB-0XH-1 and GEN-PB-0XH-2
- Configuration: Parallel operation (2.5 MW total per block when paralleled)
- Total for PB blocks: **12 generators = 15 MW capacity**

### **TOTAL BUILDING H GENERATORS: 18 × 1.25 MW = 22.5 MW**

This perfectly matches the OFE CSV data showing 18 CAT generators!

---

## Why the Actual Commissioning Plan Said "No Generators"

### The Reconciliation

The actual commissioning plan stated:
> "Building H does NOT have on-site generators"
> "Generator-backed systems are in other buildings (MB, PB blocks)"

**EXPLANATION:** The commissioning plan was referring specifically to the **MA and PA blocks** (the GPU blocks), which are indeed utility-fed only. However, this was **misleading** because:

1. **MB and PB blocks ARE physically in Building H** (per the electrical drawings)
2. **MB and PB blocks DO have generators** (18 total, per schematics)
3. The commissioning plan appears to have been written from the perspective of the "primary GPU systems" (MA/PA blocks) which don't have generators

### The Confusion Explained

The commissioning plan likely focused on the **MA and PA blocks** as the "main" Building H systems because:
- MA blocks: 8 blocks serving GPU mechanical loads (chillers, pumps, etc.)
- PA blocks: 18 blocks serving GPU power loads
- These 26 blocks are utility-fed only

The **MB and PB blocks** (9 total) were possibly considered "auxiliary" or "support" systems, even though they're physically in the same building.

---

## Detailed Power Block Analysis From Schematics

### MA Blocks (GPU Mechanical) - 8 Blocks - UTILITY FED ONLY

**Drawing Reference:** E07-12A (SWBD-MA-01H typical)

**Configuration per MA Block:**
- **Transformer:** 3000 KVA, 34.5kV-415V
- **Main Switchboard:** 4000A, 415/240V
- **UPS System:** 3 × 250 KVA (parallel operation)
- **Cooling:** 3 × Chillers (ACC-MA-0XH-1, 2, 3)
- **Pumps:** 3 × 75 HP Chilled Water Pumps (VFD)
- **Fan Wall:** 6 fans typical
- **Generators:** ❌ NONE - Direct utility feed only

**Total MA Blocks:** 8 (MA-01H through MA-08H)

### MB Blocks (Mechanical) - 3 Blocks - GENERATOR BACKED

**Drawing References:**
- E07-12B: SWBD-MB-01H
- E07-12C: SWBD-MB-02H
- E07-12D: SWBD-MB-03H

**Configuration per MB Block:**
- **Transformer:** 3000 KVA (MB-01H, MB-02H) or 2550 KVA (MB-03H), 34.5kV-415V
- **Main Switchboard:** 4000A, 415/240V
- **UPS System:** 3 × 250 KVA (parallel operation)
- **Generators:** ✅ **2 × 1.25 MW diesel generators** (GEN-MB-0XH-1 and GEN-MB-0XH-2)
- **Generator Switchgear:** PSG-MB-0XH (4000A, 415V)
- **ATS Controller:** Automatic Transfer Switch logic
- **Cooling:** 3 × Chillers (ACC-MB-0XH-1, 2, 3)
- **Pumps:** 3 × 75 HP Chilled Water Pumps (VFD)
- **Fan Wall:** 7 fans typical
- **Configuration:** Generators can operate in parallel (2.5 MW total)

**Keyed Note from Drawing:**
> "1250KW PARALLEL GENERATORS PROVIDED TO ACHIEVE 2500KW OF GENERATION"

**Total MB Blocks:** 3 (MB-01H, MB-02H, MB-03H)
**Total MB Generators:** 6 generators = 7.5 MW

### PA Blocks (GPU Power) - 18 Blocks - UTILITY FED ONLY

**Drawing Reference:** E07-12E (SWBD-PA-01H typical)

**Configuration per PA Block:**
- **Transformer:** 3000 KVA, 34.5kV-415V
- **Main Switchboard:** 4000A, 415/240V
- **UPS System:** 2 × 1250 KVA (parallel operation)
- **Static Transfer Switches:** 4 × 800A STS per block
- **Busway Distribution:** 800A busways to GPU racks
- **Generators:** ❌ NONE - Direct utility feed only

**Total PA Blocks:** 18 (PA-01H through PA-18H)

### PB Blocks (IT Power) - 6 Blocks - GENERATOR BACKED

**Drawing References:**
- E07-12F: SWBD-PB-01H
- E07-12G: SWBD-PB-02H
- E07-12H: SWBD-PB-03H
- E07-12I: SWBD-PB-04H
- E07-12J: SWBD-PB-05H
- E07-12K: SWBD-PB-06H

**Configuration per PB Block:**
- **Transformer:** 3000 KVA (PB-01H, PB-02H) or 2550 KVA (PB-03H through PB-06H), 34.5kV-415V
- **Main Switchboard:** 4000A, 415/240V
- **UPS System:** 2 × 1250 KVA (parallel operation)
- **Generators:** ✅ **2 × 1.25 MW diesel generators** (GEN-PB-0XH-1 and GEN-PB-0XH-2)
- **Generator Switchgear:** PSG-PB-0XH (4000A, 415V)
- **ATS Controller:** Automatic Transfer Switch logic
- **Busway Distribution:** 10 × 600A busways per block
- **DOAS/Mechanical:** Separate 480V system with DOAS and humidifier
- **Configuration:** Generators can operate in parallel (2.5 MW total)

**Keyed Note from Drawing:**
> "1250KW PARALLEL GENERATORS PROVIDED TO ACHIEVE 2500KW OF GENERATION"

**Total PB Blocks:** 6 (PB-01H through PB-06H)
**Total PB Generators:** 12 generators = 15 MW

### RA Block (GPU Reserve) - 1 Block - UTILITY FED ONLY

**Drawing Reference:** E07-12L (SWBD-RA-01H)

**Configuration:**
- **Transformer:** 3000 KVA, 34.5kV-415V
- **Main Switchboard:** 4000A, 415/240V
- **UPS System:** 2 × 1250 KVA (parallel operation)
- **Reserve Busway:** 4000A bus feeding reserve capacity to PA blocks
- **Function:** Provides redundancy for PA GPU blocks
- **Generators:** ❌ NONE - Direct utility feed only

**Total RA Blocks:** 1 (RA-01H)

---

## Generator Summary for Building H

### Total Generator Count: 18 Generators

| Block Type | Blocks | Generators per Block | Total Generators | Total Capacity |
|------------|--------|---------------------|------------------|----------------|
| MB (Mechanical) | 3 | 2 × 1.25 MW | 6 generators | 7.5 MW |
| PB (IT Power) | 6 | 2 × 1.25 MW | 12 generators | 15.0 MW |
| **TOTAL** | **9 blocks** | **-** | **18 generators** | **22.5 MW** |

### Generator Specifications (from schematics)

- **Manufacturer:** CAT (Caterpillar) - confirmed by T5 supplier per OFE CSV
- **Rating:** 1250 kW (1.25 MW) each
- **Fuel:** Diesel
- **Configuration:** Pairs operate in parallel per block (2.5 MW per block)
- **Switchgear:** PSG-XX-0XH (4000A, 415V, 65kAIC)
- **Transfer Logic:** ATS Controller with automatic utility/generator transfer

---

## Commissioning Implications - REVISED

### My Original Plan Assessment: ✅ **CORRECT**

My commissioning plan that included 18 generator commissioning was **CORRECT** based on the OFE CSV data and now confirmed by electrical schematics.

### Actual Commissioning Plan Assessment: ⚠️ **MISLEADING**

The actual commissioning plan's statement "Building H does NOT have on-site generators" is **technically incorrect** or at minimum **highly misleading** because:
- 18 generators ARE physically in Building H
- 18 generators ARE assigned to Building H systems (MB and PB blocks)
- 18 generators MUST be commissioned as part of Building H commissioning

### Corrected Commissioning Scope for Building H

**GENERATOR COMMISSIONING REQUIRED:**

#### MB Block Generator Testing (6 generators)
- **MB-01H:** GEN-MB-01H-1, GEN-MB-01H-2
- **MB-02H:** GEN-MB-02H-1, GEN-MB-02H-2
- **MB-03H:** GEN-MB-03H-1, GEN-MB-03H-2

**Testing per MB block:**
1. Individual generator startup and operation
2. Parallel operation testing (2 generators per block)
3. Load bank testing (up to 2.5 MW per block)
4. Automatic transfer switch (ATS) operation
5. Utility failure simulation
6. Generator failure simulation (N+1 verification)
7. Fuel system testing
8. Controls and monitoring integration

#### PB Block Generator Testing (12 generators)
- **PB-01H:** GEN-PB-01H-1, GEN-PB-01H-2
- **PB-02H:** GEN-PB-02H-1, GEN-PB-02H-2
- **PB-03H:** GEN-PB-03H-1, GEN-PB-03H-2
- **PB-04H:** GEN-PB-04H-1, GEN-PB-04H-2
- **PB-05H:** GEN-PB-05H-1, GEN-PB-05H-2
- **PB-06H:** GEN-PB-06H-1, GEN-PB-06H-2

**Testing per PB block:**
1. Individual generator startup and operation
2. Parallel operation testing (2 generators per block)
3. Load bank testing (up to 2.5 MW per block)
4. Automatic transfer switch (ATS) operation
5. Utility failure simulation
6. Generator failure simulation (N+1 verification)
7. Fuel system testing
8. Controls and monitoring integration
9. Integration with UPS systems (2 × 1250 KVA per block)

### Load Bank Requirements - CONFIRMED

My original recommendation of **2 × 2.5 MW load banks** is **APPROPRIATE** for generator testing:
- Each block has 2 × 1.25 MW generators that parallel to 2.5 MW
- Need to test parallel operation at full load
- 2.5 MW load bank allows testing one complete block at a time

**Additional load banks needed for UPS/distribution testing:**
- 1.5 MVA for 1250 KVA UPS testing (PA, PB, RA blocks)
- 800 kW for STS and busway testing

**Total recommended load bank capacity:**
- 2 × 2.5 MW resistive (generator testing)
- 1 × 1.5 MVA (UPS testing)
- 1 × 800 kW resistive (distribution testing)

This aligns with my original plan, NOT the actual plan's 3.8 MW recommendation.

---

## Commissioning Schedule Impact

### Generator Testing Duration (Revised Estimate)

**MB Blocks (3 blocks × 2 generators each):**
- Individual startup: 0.5 days per block
- Parallel operation testing: 1 day per block
- Load bank testing: 1 day per block
- ATS and transfer testing: 0.5 days per block
- **Total MB testing:** ~9 days

**PB Blocks (6 blocks × 2 generators each):**
- Individual startup: 0.5 days per block
- Parallel operation testing: 1 day per block
- Load bank testing: 1 day per block
- ATS and transfer testing: 0.5 days per block
- **Total PB testing:** ~18 days

**Total Generator Commissioning Time:** ~27 days (4 weeks)

### Integration with Actual Schedule

The actual commissioning plan timeline was:
- L4: 14 days (March 18 - April 6)
- L5: 5 days (April 7 - April 13)
- **Total:** 19 days

**PROBLEM:** Generator commissioning alone requires ~27 days, which exceeds the entire L4/L5 window by 8 days.

**RESOLUTION OPTIONS:**

1. **Parallel Testing:** Test multiple generator blocks simultaneously
   - Test 2-3 MB blocks concurrently
   - Test 2-3 PB blocks concurrently
   - Requires more personnel and equipment
   - Could compress to ~12-15 days

2. **L2/L3 Integration:** Move some generator testing into L2/L3 phase
   - Individual generator startups during L3 (Feb-Mar)
   - Parallel operation and load testing during L4 (Mar 18 - Apr 6)
   - Final integrated testing during L5 (Apr 7-13)

3. **Extended L4 Schedule:** Add 1-2 weeks to L4 phase
   - New L4 timeline: March 18 - April 20
   - Would delay customer handoff

---

## UPS Configuration - VERIFIED FROM SCHEMATICS

| Block Type | UPS Configuration | Total UPS Units | UPS Capacity |
|------------|-------------------|-----------------|--------------|
| **MA Blocks** (8) | 3 × 250 KVA per block | 24 units | 6 MVA |
| **MB Blocks** (3) | 3 × 250 KVA per block | 9 units | 2.25 MVA |
| **PA Blocks** (18) | 2 × 1250 KVA per block | 36 units | 45 MVA |
| **PB Blocks** (6) | 2 × 1250 KVA per block | 12 units | 15 MVA |
| **RA Block** (1) | 2 × 1250 KVA | 2 units | 2.5 MVA |
| **TOTAL** | - | **83 UPS units** | **70.75 MVA** |

### OFE CSV Comparison

**OFE CSV showed:**
- 42 × 1250 KVA UPS
- 30 × 250 KVA UPS
- **Total:** 72 units

**Schematics show:**
- 50 × 1250 KVA UPS (36 PA + 12 PB + 2 RA)
- 33 × 250 KVA UPS (24 MA + 9 MB)
- **Total:** 83 units

**Discrepancy:** 11 additional UPS units in schematics vs. OFE CSV
- Possible explanation: OFE CSV may not include MB block UPS
- Or: Additional UPS added after procurement data exported

---

## STS Configuration - VERIFIED FROM SCHEMATICS

| Block Type | STS per Block | Total STS Units |
|------------|---------------|-----------------|
| **PA Blocks** (18) | 4 × 800A | 72 STS |
| **All Others** | 0 | 0 |
| **TOTAL** | - | **72 STS** |

This matches both my plan and the actual commissioning plan: **72 STS units**

---

## Chiller Configuration - VERIFIED FROM SCHEMATICS

| Block Type | Chillers per Block | Total Chillers |
|------------|-------------------|----------------|
| **MA Blocks** (8) | 3 per block | 24 chillers |
| **MB Blocks** (3) | 3 per block | 9 chillers |
| **PA Blocks** (18) | 0 | 0 |
| **PB Blocks** (6) | 0 | 0 |
| **RA Block** (1) | 0 | 0 |
| **TOTAL** | - | **33 chillers** |

### OFE CSV Comparison

**OFE CSV showed:** 30 × JCI 500T chillers

**Schematics show:** 33 chillers (24 MA + 9 MB)

**Discrepancy:** 3 additional chillers
- Likely explanation: MB blocks added after CSV export
- Or: CSV counted only MA blocks

---

## Key Findings Summary

### ✅ CONFIRMED: My Plan Was Correct

1. **18 generators DO exist in Building H** - confirmed by schematics
2. **Generator commissioning IS required** - 9 blocks need generator testing
3. **Load bank requirements accurate** - 2.5 MW load banks appropriate
4. **Commissioning duration understated** - actual plan's 19 days insufficient

### ❌ ACTUAL PLAN ISSUES IDENTIFIED

1. **"No generators" statement is INCORRECT** - Building H has 18 generators
2. **Generator testing not scoped** - no mention of MB/PB block generator commissioning
3. **Load bank sizing understated** - 3.8 MW insufficient for generator testing
4. **Schedule too compressed** - 19 days inadequate for full scope

### ⚠️ CRITICAL CLARIFICATIONS NEEDED

1. **Is MB/PB generator commissioning included in "Building H" scope?**
   - If YES: Schedule must be extended
   - If NO: Separate commissioning plan needed for MB/PB blocks

2. **Why does actual plan omit generator testing?**
   - Oversight in planning?
   - Separate commissioning contract for generators?
   - Different project phase?

3. **What is the relationship between MB/PB blocks and MA/PA blocks?**
   - Are they separate commissioning packages?
   - Do they serve the same loads?
   - Why different power sources?

---

## Revised Commissioning Scope Recommendation

### Scenario 1: MB/PB Blocks Included in Building H Commissioning

**Total Building H Scope:**
- 36 power blocks total
- 18 generators (MB + PB blocks)
- 83 UPS systems
- 72 STS units
- 33 chillers

**Required Changes to Actual Plan:**
- Add generator commissioning section
- Extend L4 by 2 weeks (or compress via parallel testing)
- Increase load bank procurement to 7 MW total
- Add generator startup to L3 phase
- Update team size (add generator SMEs)

**Revised Timeline:**
- L2/L3: Nov 2025 - Mar 17, 2026 (include initial generator startups)
- L4: Mar 18 - Apr 20, 2026 (28 days instead of 14)
- L5: Apr 21 - Apr 27, 2026 (7 days instead of 5)
- **Total:** ~35 days standalone commissioning

### Scenario 2: MB/PB Blocks Commissioned Separately

**Building H "Core" Scope (MA, PA, RA blocks only):**
- 27 power blocks (8 MA + 18 PA + 1 RA)
- 0 generators
- 62 UPS systems
- 72 STS units
- 24 chillers

**Separate "MB/PB Block" Commissioning:**
- 9 power blocks (3 MB + 6 PB)
- 18 generators
- 21 UPS systems
- 0 STS units
- 9 chillers

This would reconcile the actual plan's "no generators" statement, but requires clarification on project organization.

---

## Action Items - URGENT

1. **Clarify commissioning scope boundaries**
   - Are MB/PB blocks part of "Building H" commissioning or separate?
   - Review contract documents and scope definitions

2. **Update commissioning plan if MB/PB included**
   - Add 18 generator testing procedures
   - Revise schedule to accommodate generator testing
   - Update load bank requirements
   - Add generator SME resources

3. **Coordinate with actual plan authors**
   - Understand why generators were omitted
   - Verify if separate generator commissioning plan exists
   - Align terminology and scope definitions

4. **Review OFE CSV discrepancies**
   - Verify final equipment counts (83 UPS vs 72, 33 chillers vs 30)
   - Confirm all equipment has been procured
   - Update commissioning matrices

---

## Conclusion

**MY ORIGINAL COMMISSIONING PLAN WAS CORRECT.** The OFE CSV data showing 18 generators assigned to Building H is accurate, as confirmed by the electrical one-line diagrams.

**THE ACTUAL COMMISSIONING PLAN'S STATEMENT** that "Building H does NOT have on-site generators" is either:
1. **Incorrect** - a factual error in the plan
2. **Misleading** - referring only to MA/PA blocks, not the complete Building H
3. **Scope-limited** - MB/PB blocks commissioned under different contract/plan

**The presence of 18 generators fundamentally changes the commissioning scope, schedule, budget, and resource requirements for Building H.**

This must be resolved immediately before commissioning begins.

---

**Document Control:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-11-19 | Analysis Team | Complete correction based on electrical schematics |

**Schematics Reviewed:**
- E07-12A: SWBD-MA-01H (typical of 8 MA blocks)
- E07-12B: SWBD-MB-01H (with generators)
- E07-12C: SWBD-MB-02H (with generators)
- E07-12D: SWBD-MB-03H (with generators)
- E07-12E: SWBD-PA-01H (typical of 18 PA blocks)
- E07-12F: SWBD-PB-01H (with generators)
- E07-12G: SWBD-PB-02H (with generators)
- E07-12H: SWBD-PB-03H (with generators)
- E07-12I: SWBD-PB-04H (with generators)
- E07-12J: SWBD-PB-05H (with generators)
- E07-12K: SWBD-PB-06H (with generators)
- E07-12L: SWBD-RA-01H (reserve block)

---

**END OF CORRECTED ANALYSIS**
