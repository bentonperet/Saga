# De📄 Reading markdown file...
🔍 Parsing markdown...
   Found 158 blocks
🔐 Authenticating with Google...
📝 Creating Google Doc...

✅ Document published successfully!

   Title: Design Review Findings - Mechanical System Single Points of Failure
   URL:   https://docs.google.com/document/d/1KgppmjNvIXiK5-fp5R1PuvM84cfKlFuKrPTHnznwAPk/edit

sign Review Findings - Mechanical System Single Points of Failure

**Created:** 2025-10-31 00:00
**Tags:** #gge #data-center #mechanical #design-review #spof #tier-iii
**Related:** [[Design Review Findings - Biliki Data Center]], [[RFI - Critical Design Clarifications Required]], [[GGE Design Review]]

**Project:** BILIKI Data Center Unit (DCU), Tbilisi, Georgia
**Document Reviewed:** GE01-CAS-0004-CO6-C02 (Mechanical Flow Diagram, Sheet 8, dated 27.10.2025)
**Review Date:** October 31, 2025
**Reviewed by:** Design Review Team

---

## Executive Summary

This design review identifies **critical single points of failure (SPOFs)** in the mechanical cooling system design as shown in drawing GE01-CAS-0004-CO6-C02. The analysis focuses on Tier III compliance requirements for concurrent maintainability, which mandate that any single cooling component can be isolated for maintenance without impacting IT operations.

**Key Findings:**
- **5 Single Points of Failure** identified in the cooling distribution system
- **Primary Issue:** Lack of redundant A/B cooling distribution paths to IT spaces (Tier III non-compliance)
- **Single DN250 distribution headers** per chiller plant serving multiple IT rooms
- **Undersized expansion vessels** for system volume
- **Positive Note:** Makeup water systems ARE connected via "MAKEUP RING" configuration, and CRV1/CRV2 share river water loop (system-level integration exists)

**Tier III Impact:** The current design **DOES NOT clearly demonstrate Uptime Institute Tier III concurrent maintainability requirements** for the chilled water distribution system. Clarification or redesign of distribution piping may be required.

---

## Important Clarification: System-Level Connectivity

**CORRECTION:** Initial review suggested CRV1 and CRV2 were completely isolated. Further examination reveals:

✅ **Makeup water systems ARE connected** - Drawing shows "MAKEUP RING" label indicating ring/loop configuration
✅ **River water loop is shared** - "Loop with River Water" serves both chiller plants
✅ **Utility-level integration exists** - Plants share common utility infrastructure

**Therefore:** The chiller plants have system-level connectivity at the utility/condenser water level.

**PRIMARY CONCERN REMAINS:** The **chilled water distribution to IT spaces** - whether redundant A/B paths exist from chiller plants to individual IAC units. This is the critical Tier III compliance question.

---

## Single Points of Failure - Detailed Analysis

### SPOF #1: Single DN250 Distribution Headers Per Chiller Plant (NO CLEAR A/B REDUNDANCY)

**Location:** Center of drawing - horizontal main distribution pipes
**Drawing Reference:** DN250 pipes running horizontally from CRV1 to V1-V5 area, and from CRV2 to E-A/HB area

**Description:**
The drawing shows what appears to be single-path distribution from each chiller plant:
- **CRV1 system:** DN250 supply/return headers serve V1, V2, V3, V4, V5 VIP rooms
- **CRV2 system:** DN250 supply/return headers serve E-A Enterprise and HB Hub computer rooms
- **No redundant parallel headers clearly shown**
- **No cross-tie visible** between CRV1 and CRV2 distribution headers

**Tier III Requirement:**
Concurrent maintainability requires **redundant distribution paths (A/B)** to all critical cooling equipment, where either path can carry full load while the other is isolated for maintenance.

**Questions That Need Clarification:**
1. Are there actually redundant A/B headers that are not clearly shown on this schematic-level drawing?
2. Does the DN250 header represent a dual/parallel pipe arrangement?
3. Is there cross-tie capability between CRV1 and CRV2 distribution headers?
4. Can each chiller plant back up the other at the chilled water distribution level?

**Failure Scenarios If Single-Path:**
- Pipe rupture/leak in DN250 header requires isolation = loss of cooling to multiple IT rooms
- Valve failure in distribution header affects entire zone
- Flange gasket failure requires shutdown of affected rooms
- Seismic pipe separation (Zone VIII seismicity) could sever distribution
- Cannot maintain distribution piping without IT impact

**Risk Level:** **CRITICAL** (if truly single-path with no redundancy)

**Recommended Solution:**
1. **If redundancy exists:** Update drawing to clearly show A/B distribution paths, isolation valve locations, and demonstrate concurrent maintainability
2. **If single-path confirmed:** Redesign with one of the following:
   - **Option A:** Implement dual A/B headers from each chiller plant (2N distribution)
   - **Option B:** Add cross-tie between CRV1 and CRV2 so each can back up the other
   - **Option C:** Create looped/ring distribution topology
3. Add isolation valves at strategic locations
4. Clearly label A-side and B-side distribution on drawings

---

### SPOF #2: Single Piping Path to Each In-Row Cooling Unit

**Location:** Throughout drawing - all IAC (In-row Air Conditioning) connections
**Drawing Reference:** Individual unit connections labeled V1/IAC/1 through V1/IAC/6, V2/IAC/1-6, etc.

**Description:**
Every in-row air conditioning unit appears to have only one supply and one return connection:
- Total of **~92 IAC units** shown across all IT spaces
- Each unit: Single supply pipe, single return pipe
- No redundant feed capability shown to individual units
- No cross-connect between adjacent units

**Tier III Compliance Status:**
This is **ACCEPTABLE for Tier III at the individual unit level**, PROVIDED that:
- N+1 or greater cooling capacity exists within each zone
- Loss of any single IAC unit does not affect IT load
- Multiple units serve each rack row so single unit loss is tolerable

**However, this SPOF escalates to CRITICAL when combined with SPOF #1:**
- If distribution header fails, multiple IAC units lose cooling simultaneously
- If chiller plant fails without cross-tie, entire groups of IAC units are affected
- Single upstream valve closure can orphan many downstream units

**Risk Level:** **MEDIUM** (at unit level), **CRITICAL** (when combined with upstream header SPOF)

**Recommended Solution:**
1. **Primary:** Resolve SPOF #1 to provide redundant feed paths at distribution header level
2. **Verify:** N+1 or N+2 IAC unit redundancy exists within each room/zone
3. **Document:** Equipment schedule showing total cooling capacity vs. required load
4. **Add:** Local isolation valves at each unit for independent maintenance

**Industry Practice:** Modern hyperscale data centers typically use overhead A/B distribution buses with each IAC unit served from both A and B headers, allowing any distribution component to be maintained.

---

### SPOF #3: Inadequate Expansion Tank Sizing

**Location:** Throughout system - multiple 0.5 t expansion tanks shown
**Drawing Reference:** "Expansion Tank 0,5 t" labels on small tank symbols throughout drawing

**Description:**
Drawing shows multiple 0.5 t (500 liter / 132 gallon) expansion tanks distributed throughout the system. This appears severely undersized for a 5.6 MW data center cooling system.

**Sizing Analysis:**

**System Volume Estimation:**
For 5.6 MW IT load + infrastructure cooling:
- Total heat rejection ≈ 8.4 MW thermal (PUE 1.5)
- Typical chilled water flow: 2.4 L/s per 100 kW
- Required flow ≈ 200 L/s = 720 m³/hr
- **Estimated system volume:**
  - Primary/secondary piping (DN250 + distribution): 50-70 m³
  - Chillers and heat exchangers: 10-15 m³
  - 92× in-row cooling units (50L each): 5 m³
  - Buffer tanks (if any): 20-30 m³
  - **Total: 100-150 m³ (26,000-40,000 gallons)**

**Expansion Volume Calculation:**
Water expansion from 5°C to 40°C (35°C ΔT):
- Volumetric expansion: ~1.5%
- Expansion volume = 100-150 m³ × 1.5% = **1.5-2.25 m³**
- With safety factor (1.5×): **2.25-3.4 m³**
- With acceptance volume accounting: **5-10 m³ needed**

**Current Capacity:**
- Drawing shows approximately 6× "Expansion Tank 0,5 t"
- 6 × 500 L = **3,000 L = 3.0 m³ total**
- This is **marginal at best**, with no redundancy

**Consequences of Undersizing:**
- Frequent pressure relief valve discharge (water loss)
- Constant makeup water replenishment required
- Pressure fluctuations affecting pumps and controls
- Risk of cavitation during rapid temperature changes
- Air entrainment if vacuum develops during cooldown

**Risk Level:** **HIGH**

**Recommended Solution:**
1. Recalculate expansion requirements based on actual system volume and operating temperatures
2. Upsize to **5-10 m³ per major cooling loop**
3. Use **bladder-type expansion tanks** rated for chilled water service
4. Provide **redundant capacity** (dual tanks with isolation valves)
5. Pre-charge to correct pressure (typically 1.5× static head at highest system point)
6. Install pressure sensors and alarms

**Industry Standard:** 5-10% of system volume, suggesting 5-15 m³ for this facility.

---

### SPOF #4: Single Degassing System Per Loop

**Location:** Bottom sections, near makeup water connections
**Drawing Reference:** "DC Degassing line" shown in legend

**Description:**
Drawing indicates degassing systems for each cooling loop:
- **DC line** extracts gas-rich water from system
- Degassing unit removes dissolved air/gases
- **DC line** returns degassed water to system
- No redundant degassing capability shown

**Function of Degassing:**
Critical for:
- Preventing pump cavitation and impeller damage
- Eliminating air binding in high points
- Maintaining heat transfer efficiency
- Reducing corrosion from dissolved oxygen
- Preventing flow blockages from air pockets

**Failure Impact Timeline:**
- **Days:** Gradual air accumulation, minor efficiency loss
- **Weeks:** Pump noise, flow reduction, air binding in coils
- **Months:** Equipment damage, system inefficiency, shutdown required

**Risk Level:** **MEDIUM**

**Recommended Solution:**
1. Provide redundant degassing units (A/B) with isolation valving
2. Size each unit for 100% flow capacity
3. Add automatic air vents at high points as backup
4. Install differential pressure monitors to detect air accumulation
5. Include in preventive maintenance schedule with bypass capability

---

### SPOF #5: Water Storage Capacity and Function Unclear

**Location:** Bottom corners of drawing
**Drawing Reference:** Water storage tanks - "Water storage 50 m³ - A1", "Water storage 50 m³ - B1" (left side), two "Water storage 125 m³" (right side)

**Description:**
Substantial water storage shown:
- **Left side (CRV1):** 2× 50 m³ = 100 m³ total
- **Right side (CRV2):** 2× 125 m³ = 250 m³ total
- **Total:** 350 m³ (92,000 gallons)

**Critical Questions:**

**1. What is the primary function of these tanks?**
   - Makeup water storage for closed-loop system replenishment?
   - Emergency condenser water supply during river water outage?
   - Both functions combined?

**2. If emergency condenser water supply:**
   - At full load (8.4 MW heat rejection), typical condenser flow ≈ 1,620 m³/hr
   - 350 m³ storage ÷ 1,620 m³/hr = **13 minutes runtime**
   - This is **insufficient** for meaningful emergency cooling
   - Typically need 2-4 hours minimum

**3. If makeup water storage:**
   - System volume ≈ 100-150 m³
   - 350 m³ = 2-3× full system refill capacity (adequate for makeup)
   - But need verification of redundancy and isolation capability

**4. Redundancy and Isolation:**
   - Are tanks in duty/standby configuration?
   - Can one tank be isolated for maintenance?
   - Are isolation valves provided?
   - Is there automatic switchover?

**Risk Level:** **MEDIUM** (needs clarification and improved redundancy design)

**Recommended Solution:**
1. **Clarify tank purpose** in design documents and equipment schedule
2. **If emergency condenser water:**
   - Increase to 3,000-5,000 m³ for 2-3 hour autonomy, OR
   - Add municipal water backup connection with automatic switchover, OR
   - Document limited autonomy and include partial load shedding procedures
3. **If makeup water storage:**
   - Add isolation valves between tanks for independent operation
   - Implement duty/standby configuration with automatic switchover
   - Size for maintenance (one tank offline while maintaining function)
4. Add level sensors, low-level alarms, and monitoring
5. Include tank maintenance procedures in O&M manual

---

## Tier III Compliance Assessment

### Concurrent Maintainability Requirements

Uptime Institute Tier III requires:
> "Any single component in the distribution path can be removed from service for maintenance without impacting IT operations."

### Current Design Compliance Summary:

| System Component | Tier III Requirement | Drawing Status | Compliant? |
|-----------------|---------------------|----------------|------------|
| Chiller plants | N+1 or 2N | Stated as "N+1" in BOD but specs not shown | **UNKNOWN** |
| Plant-level connectivity | System integration | YES - connected via makeup ring & river loop | **✓ YES** |
| Distribution headers | Redundant A/B paths to IT | Not clearly shown | **UNKNOWN** |
| Cross-tie capability | Back-feed between plants | Not visible on drawing | **UNKNOWN** |
| IAC unit redundancy | N+1 capacity per zone | 92 units shown, capacity unverified | **UNKNOWN** |
| Expansion system | Adequate + redundant | 3.0 m³ total (undersized, no redundancy) | **✗ NO** |
| Makeup water | Redundant capability | Connected via ring (appears adequate) | **? LIKELY** |
| Water storage | Adequate for purpose | Function unclear, autonomy unverified | **UNKNOWN** |
| Isolation valving | Strategic isolation points | Not shown on schematic | **UNKNOWN** |

### Overall Tier III Mechanical Compliance: **CANNOT VERIFY - INSUFFICIENT DETAIL**

**Critical Uncertainties:**
1. **Chilled water distribution redundancy** - Are A/B paths provided to IT spaces?
2. **Equipment specifications** - Chiller capacities, N+1 verification
3. **Isolation valve strategy** - Where are isolation points for concurrent maintenance?
4. **Water storage function** - Emergency cooling? Makeup water? Runtime?

**Confirmed Deficiencies:**
1. **Expansion tank capacity** - Undersized by 2-3×, no redundancy (SPOF #3)
2. **Drawing detail level** - Schematic does not show enough detail to verify Tier III compliance

---

## Summary Table: Single Points of Failure

| SPOF # | Component | Location | Risk Level | Tier III Impact | Needs Clarification? |
|--------|-----------|----------|------------|-----------------|---------------------|
| **1** | Single DN250 distribution headers (no clear A/B) | Center, horizontal mains | **CRITICAL*** | May violate CM requirement | **YES - URGENT** |
| **2** | Single pipe to each IAC unit | Throughout, IAC connections | **MEDIUM** | Acceptable if N+1 units | Verify N+1 capacity |
| **3** | Undersized expansion tanks | Throughout, 0.5t tanks | **HIGH** | Operational risk | Recalculate & upsize |
| **4** | Single degassing per loop | Bottom, DC pipes | **MEDIUM** | CM concern | Add redundancy |
| **5** | Water storage function unclear | Bottom corners | **MEDIUM** | Unknown risk | Clarify purpose |

*CRITICAL if single-path confirmed; may be acceptable if A/B redundancy exists but is not shown on schematic-level drawing.

**NOT SPOFs (Corrections from Initial Review):**
- ~~Cross-tie between CRV1 and CRV2~~ - Plants ARE connected at utility level (makeup ring, river water)
- ~~Single makeup water per loop~~ - Drawing shows "MAKEUP RING" indicating interconnection

---

## Recommended Actions - Priority Order

### IMMEDIATE - REQUIRED FOR TIER III SUBMISSION

**1. Clarify Chilled Water Distribution Architecture**
   - **Question:** Do redundant A/B distribution paths exist to IT spaces?
   - **If YES:** Update drawings to clearly show A/B paths, isolation valves, and concurrent maintainability
   - **If NO:** Redesign distribution for A/B redundancy or add cross-tie between CRV1/CRV2
   - **Timeline:** This is **CRITICAL PATH** for Tier III certification

**2. Provide Equipment Specifications**
   - Chiller make, model, capacity, quantity (verify N+1)
   - Pump specifications (flow, head, power, redundancy)
   - Heat exchanger capacities
   - System design temperatures and flow rates
   - **Required for:** Capacity verification and Tier III documentation

**3. Show Isolation Valve Strategy**
   - Add isolation valve symbols and tag numbers to drawing
   - Identify isolation boundaries
   - Demonstrate how sections can be isolated for maintenance
   - **Required for:** Concurrent maintainability demonstration

### HIGH PRIORITY - BEFORE CONSTRUCTION

**4. Upsize Expansion Tanks**
   - Perform sizing calculation based on actual system volume
   - Increase from 3.0 m³ to 5-10 m³ per loop
   - Provide redundant tanks with isolation valves
   - Update specifications and drawings

**5. Clarify Water Storage Function and Sizing**
   - Document tank purpose (makeup vs. emergency cooling)
   - If emergency cooling: verify runtime or increase capacity
   - Add isolation valves for redundancy
   - Include in equipment schedule with specifications

**6. Add Degassing Redundancy**
   - Specify dual degassing units with isolation valving
   - Update P&ID to show redundant configuration

### MEDIUM PRIORITY - DETAILED DESIGN

**7. Verify IAC Unit N+1 Redundancy**
   - Calculate total cooling capacity per room/zone
   - Confirm N+1 or N+2 redundancy exists
   - Document in equipment schedule

**8. Add Cross-Tie Between CRV1 and CRV2 Distribution** (Best Practice)
   - While not strictly required for Tier III, cross-tie at chilled water distribution level provides additional resilience
   - Consider DN250 cross-connect with isolation valves
   - Allows either plant to back up the other in emergency

**9. Develop Seismic Design Details**
   - Zone VIII (PGA 0.25-0.27g) requires robust seismic design
   - Add flexible connections at all rotating equipment
   - Show seismic bracing for distribution piping
   - Detail equipment anchorage

---

## Reference Standards

- **Uptime Institute Tier Standard: Topology (ANSI/TIA-942)** - Concurrent maintainability requirements
- **ASHRAE TC 9.9** - Mission Critical Facilities, Data Centers, Technology Spaces
- **ASHRAE Handbook - HVAC Systems and Equipment, Chapter 13** - Expansion tanks and air elimination
- **ISO/IEC 22237-3** - Data centre facilities and infrastructures - Part 3: Building construction
- **EN 12828** - Heating systems in buildings - Design for water-based heating systems
- **ASME B31.9** - Building Services Piping
- **ASCE 7-16, Chapter 13** - Seismic Design Requirements for Nonstructural Components

---

## Conclusion and Path Forward

The mechanical cooling system design shown in GE01-CAS-0004-CO6-C02 **cannot be fully evaluated for Tier III compliance** due to insufficient detail on the schematic-level drawing.

**Key Positive Finding:**
✅ CRV1 and CRV2 chiller plants ARE connected at utility/condenser water level via makeup ring and river water loop

**Critical Question Requiring Immediate Clarification:**
❓ **Do redundant A/B chilled water distribution paths exist to IT spaces?**

**Confirmed Deficiencies:**
1. ❌ Expansion tanks undersized by 2-3× (3.0 m³ vs. 5-10 m³ required)
2. ❌ No redundancy shown for expansion, degassing, or water storage systems
3. ❌ Equipment specifications missing from drawing

**Path Forward:**

**This Week:**
1. Request clarification from CAS GmbH mechanical engineer: Do A/B distribution paths exist?
2. Request equipment schedule with chiller/pump specifications
3. Request isolation valve schedule and P&ID with more detail

**Next 2 Weeks:**
4. If A/B paths exist: Update drawings to show them clearly
5. If A/B paths do NOT exist: Redesign distribution system for concurrent maintainability
6. Perform expansion tank sizing calculation and upsize tanks
7. Clarify water storage function and verify adequacy

**Before Tier III Submission (4 Weeks):**
8. Issue updated mechanical drawings showing Tier III compliance
9. Provide equipment schedules and specifications
10. Develop maintenance isolation procedures demonstrating concurrent maintainability
11. Consider third-party peer review

**Timeline Impact:**
If distribution redesign is required, expect 3-4 weeks for engineering plus 1-2 weeks for review. This is on the **critical path** for Tier III certification.

---

## Document Control

**Prepared by:** Design Review Team
**Date:** October 31, 2025
**Revision:** Rev 1 (corrected based on "MAKEUP RING" and river water connectivity observation)
**Status:** Preliminary Design Review - Mechanical Systems - Requires Clarification
**Next Review:** After receiving clarifications from CAS GmbH and updated drawings

**Distribution:**
- GGE Project Management
- CAS GmbH Mechanical Engineering Team
- Uptime Institute (for Tier Certification review)
- Independent Commissioning Authority

---

## Appendices

**Appendix A: Questions for CAS GmbH Mechanical Engineer**

1. Do redundant A/B chilled water distribution paths exist from each chiller plant to IT spaces?
2. If yes, can you provide a drawing that clearly shows the A/B path segregation and isolation valve locations?
3. What are the chiller specifications (quantity, capacity, make/model, redundancy configuration)?
4. What is the total system volume and expansion tank sizing basis?
5. What is the function of the 350 m³ water storage - makeup water, emergency condenser water, or both?
6. If emergency condenser water, what is the design autonomy time at full load?
7. Are degassing systems redundant with isolation capability?
8. Where are the strategic isolation valves located to enable concurrent maintenance?

**Appendix B: Industry Best Practices - Redundant Distribution**

*(Future: Add reference architecture diagrams showing A/B distribution from comparable Tier III facilities)*

**Appendix C: Expansion Tank Sizing Calculation**

*(Future: Add detailed calculation once system volume is confirmed)*
