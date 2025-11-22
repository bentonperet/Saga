**Created:** 2025-11-19 14:00
**Tags:** #coreweave #building-selection #commissioning #priority-analysis
**Related:** [[Building Selection Analysis]], [[powsybl-project/README]]

---

# REVISED Building Selection - Priority-Based Analysis

## Client Priority Criteria (in order)

1. **Greatest amount of time to complete L4 and L5 with buffer to handover** (in case of issues)
2. **Least interdependencies/conflicts with other phases & lower complexity** (independent systems)
3. **Speed to mobilize** - Target mobilization: December 1, 2025

---

## Critical Re-Analysis: Time, Buffer & Independence

### PRIORITY 1: Maximum L4/L5 Duration + Buffer to Handoff

| Building | L4 Ready Date | Handoff Date | Total Buffer | L4 Cx Days | L5 Cx Days | Total Cx | Post-Cx Buffer |
|----------|---------------|--------------|--------------|------------|------------|----------|----------------|
| **G** | 12/8/25 | 12/27/25 | **19 days** | 24 days (planned) | 3 days | 27 days | -8 days ❌ |
| **F** | 12/8/25 | 1/22/26 | **45 days** ✅ | 14 days | 3 days | 17 days | 28 days ✅ |
| **D** | 12/18/25 | 2/2/26 | **46 days** ✅ | 14 days | 5 days | 19 days | 27 days ✅ |
| **C** | 2/11/26 | 3/22/26 | **39 days** | 14 days | 5 days | 19 days | 20 days |
| **H** | 3/6/26 | 4/30/26 | **55 days** ✅✅ | 14 days | 5 days | 19 days | 36 days ✅✅ |
| **B** | 3/20/26 | 5/3/26 | **44 days** ✅ | 14 days | 5 days | 19 days | 25 days ✅ |

**WINNER: Building H** - 55 days total buffer (DATA hall energized 3/6/26 → handoff 4/30/26)

---

### PRIORITY 2: Independence & Low Complexity

#### Building F (North Campus)
**Independence Score: 9/10** ✅✅
- **Standalone exterior yards** - No shared courtyards
- **North campus isolation** - Separate from south campus construction
- **Completed MV loop** by 11/22/25 (energized 11/22/25)
- **Independent chiller yard** - No shared infrastructure
- **No crane conflicts** - Equipment set before Cx starts
- **Minimal active construction nearby** during Cx phase

**Complexity: LOW**
- 345-day construction (standard duration)
- Chiller system ready 12/1/25 (Milestone: ID 610)
- Exterior skids started/ready 11/15/25 (Milestone: ID 722)
- Clear, sequential milestones

#### Building D (South Campus)
**Independence Score: 7/10** ✅
- **South wall independent** - Separate from courtyard work
- **Chiller yard complete** by 12/18/25
- **D-C courtyard** - Some shared equipment setting (11/18/25 - 1/8/26)
- **MV loop energized** 11/19/25 (early)
- **Moderate crane activity** in D-C courtyard during prep

**Complexity: LOW-MEDIUM**
- 160-day construction
- Some courtyard coordination with C
- South wall ready 12/13/25 (independent from courtyard)

#### Building H (South Campus)
**Independence Score: 10/10** ✅✅✅
- **Completely independent location** - No shared courtyards
- **Standalone equipment yards** - No conflicts with other buildings
- **No crane sharing** - Dedicated equipment setting areas
- **Isolated from other construction** - Far from B, C, D activities
- **Latest start** = no upstream dependencies

**Complexity: MEDIUM**
- 196-day construction
- Long flush/fill (15 days) indicates complexity
- Compressed interior (90 days) but independent
- **78-day data hall construction** (12/11/25 - 3/17/26)

#### Building B (South Campus)
**Independence Score: 3/10** ❌
- **Heavy B-C courtyard sharing** - Equipment sets 12/30/25 - 1/26/26
- **Crane conflicts** - Shared 650-ton crane operations through February
- **Most dependencies** - Relies on C completion first
- **Shared mezz equipment** setting with C
- **Complex coordination** required

**Complexity: HIGH**
- **210.5-day construction** (longest)
- Heavy interdependencies with Building C
- Latest building = inherits all prior delays

#### Building C (South Campus)
**Independence Score: 5/10** ⚠️
- **D-C courtyard sharing** - Equipment sets through 1/8/26
- **B-C courtyard sharing** - Some mezz coordination
- **Moderate crane activity** - Shared operations
- **Chiller piping on mezz** conflicts (1/9/26 - 1/31/26)

**Complexity: MEDIUM**
- 170-day construction
- Multiple courtyard dependencies
- Mid-pack = some learned lessons

---

### PRIORITY 3: December 1, 2025 Mobilization

**Can we mobilize by 12/1/25?**

| Building | Key Milestones Before 12/1/25 | Mobilization Feasible? | Pre-Cx Prep Activities Available |
|----------|-------------------------------|------------------------|----------------------------------|
| **G** | - Chiller ready 12/1/25<br>- L4 ready 12/8/25 | **NO** ❌ | Too compressed, handoff 12/27/25 |
| **F** | - Chiller ready 12/1/25<br>- Exterior skids ready 11/15/25<br>- L4 ready 12/8/25 | **YES** ✅✅ | - Review startup reports from exterior (11/7-11/20)<br>- Develop test procedures<br>- Equipment familiarization<br>- Pre-functional checklists |
| **D** | - South wall ready 12/13/25<br>- Chiller yard ready 12/18/25<br>- D courtyard ready 12/9/25 | **YES** ✅ | - Observe south wall startups (12/6-12/13)<br>- Review chiller yard startups<br>- Prep test procedures |
| **C** | - Early access 12/23/25<br>- (Not L4 ready until 2/11/26) | **YES** ✅ | - 2+ months pre-Cx prep time<br>- Observe D, F, G Cx activities<br>- Long lead preparation |
| **H** | - Exterior roof complete 12/16/25<br>- (Not L4 ready until 3/6/26) | **YES** ✅✅ | - **3+ months prep time**<br>- Observe all prior buildings<br>- Most prep time available |
| **B** | - Early access 2/5/26<br>- (Not L4 ready until 3/20/26) | **YES** ✅ | - Extensive prep time<br>- Observe 5 prior buildings |

**WINNER: Buildings F, H** - F has immediate work available, H has maximum prep time

---

## REVISED Ranking by Priority Weights

### Priority 1: Buffer Time (40% weight)
1. **H: 55 days** (10/10 points)
2. **D: 46 days** (8/10 points)
3. **F: 45 days** (8/10 points)
4. **B: 44 days** (8/10 points)
5. **C: 39 days** (7/10 points)
6. **G: 19 days** (3/10 points) ❌

### Priority 2: Independence (40% weight)
1. **H: Complete independence** (10/10 points)
2. **F: Standalone north campus** (9/10 points)
3. **D: Moderate south campus** (7/10 points)
4. **C: Some courtyard sharing** (5/10 points)
5. **B: Heavy dependencies** (3/10 points) ❌

### Priority 3: Dec 1 Mobilization (20% weight)
1. **F: Immediate work available** (10/10 points)
2. **H: Maximum prep time** (9/10 points)
3. **D: Good prep opportunities** (8/10 points)
4. **C: Adequate prep time** (7/10 points)
5. **B: Extensive prep time** (7/10 points)
6. **G: Too compressed** (2/10 points) ❌

---

## WEIGHTED SCORES

| Building | Buffer (40%) | Independence (40%) | Mobilization (20%) | **TOTAL** |
|----------|--------------|--------------------|--------------------|-----------|
| **H** | 4.0 | 4.0 | 1.8 | **9.8** ✅✅✅ |
| **F** | 3.2 | 3.6 | 2.0 | **8.8** ✅✅ |
| **D** | 3.2 | 2.8 | 1.6 | **7.6** ✅ |
| **B** | 3.2 | 1.2 | 1.4 | **5.8** |
| **C** | 2.8 | 2.0 | 1.4 | **6.2** |
| **G** | 1.2 | N/A | 0.4 | **1.6** ❌ |

---

## REVISED RECOMMENDATION

### Primary Recommendation: **Building H** (Score: 9.8/10)

**Meets ALL Three Priorities:**

✅ **Priority 1: Maximum Buffer**
- **55 days** from DATA hall energized (3/6/26) to handoff (4/30/26)
- **36 days post-Cx buffer** for issue resolution
- 19-day L4/L5 commissioning with room for expansion

✅ **Priority 2: Complete Independence**
- **NO shared courtyards** - Completely standalone location
- **NO crane conflicts** - Independent equipment yards
- **NO interdependencies** - Isolated from B, C, D construction
- **10/10 independence score** - Cleanest execution

✅ **Priority 3: December 1 Mobilization**
- **3+ months preparation time** before L4 ready (3/6/26)
- Can mobilize 12/1/25 to:
  - Observe Buildings G, F, D, C commissioning (Dec 25 - Mar 26)
  - Develop comprehensive test procedures
  - Pre-functional checklists and coordination
  - Equipment familiarization during construction
  - Build relationships with contractor team

**Additional H Advantages:**
- **Lessons learned from 5 buildings** completed before H Cx starts
- **Latest timeline** = contractor's processes fully mature
- **Weather protection** - Exterior complete 12/16/25, interior work protected
- **Clean execution** - No competing construction activities during Cx

---

### Secondary Recommendation: **Building F** (Score: 8.8/10)

**Strong Alternative if Early Completion Preferred:**

✅ **Priority 1: Excellent Buffer**
- **45 days** from L4 ready (12/8/25) to handoff (1/22/26)
- **28 days post-Cx buffer** for issues

✅ **Priority 2: Near-Complete Independence**
- **North Campus isolation** - Separate from south campus
- **Standalone yards** - No courtyard sharing
- **9/10 independence score** - Very clean

✅ **Priority 3: BEST for Dec 1 Mobilization**
- **Immediate work available** starting 12/1/25
- Exterior skids already started (11/7-11/15/25)
- Chiller ready 12/1/25
- Can begin pre-functional checks immediately
- L4 ready 12/8/25 = only 1 week after mobilization

**F Advantages:**
- **Fastest revenue** - Handoff 1/22/26 (earliest viable option)
- **Proven on Building G** - Contractor demonstrates capability on G first
- **North campus** - Away from complex south campus coordination
- **Early success story** - Demonstrates capability for additional buildings

**F Disadvantages vs H:**
- Less buffer time (45 vs 55 days)
- Less lessons learned (only G complete before F)
- Earlier timeline = less schedule float

---

### NOT Recommended: Building B

**Why B Fails Your Priorities:**

❌ **Priority 2 FAILURE: High Dependencies**
- **3/10 independence score** - Worst of all options
- Heavy B-C courtyard sharing through 1/26/26
- Crane conflicts through February
- Complex coordination requirements

❌ **Complexity:**
- **210.5-day construction** (longest = highest risk)
- Latest building inherits all prior delays
- Courtyard equipment setting conflicts during Cx prep

⚠️ **Priority 1 Mediocre:**
- 44-day buffer is good but not best
- L4 ready 3/20/26 very late for 5/3/26 handoff

✅ **Priority 3 OK:**
- Can mobilize 12/1/25 with extensive prep time
- Observe 5 prior buildings

**Verdict:** B's poor independence/high complexity disqualifies it despite adequate buffer

---

### NOT Recommended: Building C

**Why C Fails Your Priorities:**

⚠️ **Priority 1 Weakest Buffer:**
- **39-day buffer** (lowest of viable options)
- Only 20 days post-Cx for issue resolution

❌ **Priority 2: Moderate Dependencies**
- **5/10 independence score** - Multiple courtyard conflicts
- D-C courtyard through 1/8/26
- B-C mezz coordination
- Chiller piping conflicts 1/9-1/31/26

✅ **Priority 3 OK:**
- Can mobilize 12/1/25
- 2+ months prep time

**Verdict:** C's weak buffer and moderate dependencies don't meet priority criteria

---

## Implementation Strategy

### If Building H Selected:

**December 1, 2025 - March 6, 2026 (Pre-Cx Phase: 96 days)**

**Month 1 (Dec 2025):**
- Mobilize commissioning team to site 12/1/25
- Shadow Building G Cx (handoff 12/27/25)
- Shadow Building F Cx prep and execution
- Review H construction drawings and equipment submittals
- Develop H-specific test procedures and protocols
- Identify long-lead test equipment needs

**Month 2 (Jan 2026):**
- Shadow Building D Cx (handoff 2/2/26)
- Monitor H interior construction progress (started 11/24/25)
- Coordinate with H contractor on Cx access requirements
- Pre-functional checklist development
- Establish testing points of contact

**Month 3 (Feb 2026):**
- Monitor H exterior yard startups (2/13-2/24/26)
- Shadow Building C Cx prep
- Finalize H test procedures
- Pre-functional coordination meetings
- Test equipment procurement and setup

**March 1-6, 2026:**
- H DATA hall energized 3/6/26
- Final pre-Cx walkdowns
- Pre-functional verification
- **BEGIN L4 CX: 3/18/26**

**March 18 - April 13, 2026 (L4/L5 Phase: 27 days)**
- L4 Cx: 3/18/26 - 4/6/26 (14 days planned, 20 days available)
- L5 Cx: 4/7/26 - 4/13/26 (5 days planned, 7 days available)
- **Buffer: 17 days for issues/delays**

**April 14-30, 2026 (Post-Cx Buffer: 17 days)**
- Issue resolution
- Retest failed systems
- Documentation finalization
- **Customer Handoff: 4/30/26**

---

### If Building F Selected:

**December 1-8, 2025 (Immediate Cx Prep: 7 days)**
- Mobilize 12/1/25
- F Chiller system ready 12/1/25
- F L4 ready 12/8/25
- Immediate pre-functional verification
- **BEGIN L4 CX: 12/9/25**

**December 9-24, 2025 (L4 Phase: 16 days)**
- L4 Cx: 12/9/25 - 12/24/25 (14 days planned, 16 days available)

**December 29, 2025 - January 5, 2026 (L5 Phase: 8 days)**
- L5 Cx: 12/29/25 - 1/5/26 (3 days planned, 8 days available)

**January 6-22, 2026 (Post-Cx Buffer: 17 days)**
- Issue resolution
- Retest failed systems
- Documentation
- **Customer Handoff: 1/22/26**

---

## Decision Matrix

| Criteria | Building H | Building F | Building D | Building C | Building B |
|----------|-----------|-----------|-----------|-----------|-----------|
| **Buffer to Handoff** | 55 days ✅✅ | 45 days ✅ | 46 days ✅ | 39 days ⚠️ | 44 days ✅ |
| **Independence** | 10/10 ✅✅ | 9/10 ✅✅ | 7/10 ✅ | 5/10 ⚠️ | 3/10 ❌ |
| **Dec 1 Mobilization** | 3+ months ✅✅ | Immediate ✅✅ | Good ✅ | Good ✅ | Good ✅ |
| **Complexity** | Medium | Low | Low-Med | Medium | High ❌ |
| **Lessons Learned** | 5 buildings ✅✅ | 1 building | 2 buildings | 3 buildings | 5 buildings ✅✅ |
| **Schedule Risk** | Medium | Low ✅ | Low ✅ | Medium | High ❌ |
| **TOTAL SCORE** | **9.8** ✅✅✅ | **8.8** ✅✅ | **7.6** ✅ | **6.2** | **5.8** ❌ |

---

## FINAL RECOMMENDATION

### **Building H is the clear winner** based on your stated priorities:

1. ✅ **Maximum buffer**: 55 days (best)
2. ✅ **Complete independence**: 10/10 (best)
3. ✅ **Dec 1 mobilization**: 3+ months prep (excellent)

### **Building F is strong secondary option** if you prefer:
- Earlier revenue (handoff 1/22/26 vs 4/30/26)
- Immediate hands-on work starting 12/1/25
- Lower overall risk (earlier in schedule)
- Faster proof of capability for follow-on buildings

### **Do NOT bid Buildings B or C** - fail independence/dependency criteria

---

## Questions for Client

1. **Is early completion valued?** (F: 1/22/26 vs H: 4/30/26)
2. **Preference for immediate work vs extended prep?** (F vs H)
3. **Is there value in observing multiple building Cx before starting?** (favors H)
4. **Are multiple buildings possible if we succeed on first?** (favors F as early proof)
5. **What is RFP response timeline?** (affects mobilization planning)

---

## Conclusion

**Building H dominates** your three priority criteria with:
- **Maximum buffer** (55 days)
- **Complete independence** (10/10)
- **Optimal Dec 1 mobilization** (3 months prep + observe 5 buildings)

**Building F is excellent alternative** with:
- Strong buffer (45 days)
- Near-complete independence (9/10)
- Immediate Dec 1 work available
- Fastest completion (1/22/26)

Choose **H for maximum safety and buffer**, or **F for speed and early success**.
