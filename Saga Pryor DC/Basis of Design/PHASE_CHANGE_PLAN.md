# Pryor DC Phase Change Implementation Plan & Progress Tracker

**Date Started:** 2025-11-07
**Purpose:** Complete restructuring of BOD from (3/6/15/22 MW) to (6/12/18/24 MW) phasing

---

## Change Summary

### Core Changes
- **Phasing:** 3/6/15/22 MW → 6/12/18/24 MW (6MW IT blocks)
- **Generators:** 4.0MW → 3.6MW, 9 total → 16 total (4 per block, N+1)
- **E-Houses:** 2 total → 16 total (4 per block)
- **PUE Marketing:** State 1.4 average
- **PUE Electrical Calc:** 1.6 for sizing (overhead for OK heat)
- **Chillers:** Recalculate per 6MW block (~7MW cooling each)
- **MV Switchboards:** ADD at 13.8kV (count TBD)
- **Transformers:** Keep 3.5 MVA (needs user confirmation)
- **Racks (specs):** Remove specific counts
- **Racks (pricing):** 60 DDC/block @ $50k = $12M total
- **L2C Cooling:** Simplify details, keep concept/benefits
- **Commissioning:** $150k/MW IT load (remove Div 01 details)

### Technical Calculations

**Per 6MW Block:**
- IT Load: 6.0 MW
- Facility Load: 9.6 MW (@ 1.6 PUE)
- Cooling Load: ~7 MW (≈2,000 tons)
- Generators: 4 × 3.6MW (N+1: 3 running = 10.8 MW)
- E-Houses: 4 units
- Racks: 60 DDC racks @ $50k

**Phase 4 Full Build (24 MW IT):**
- Facility Load: 38.4 MW
- Generators: 16 units (12 running, 43.2 MW capacity)
- E-Houses: 16 units
- Chillers: 12-16 units (TBD based on vendor sizing)
- Racks: 240 DDC @ $50k = $12M
- Commissioning: 24 MW × $150k = $3.6M

---

## Execution Progress

### ✅ Pre-Work
- [ ] Step 1: Create PHASE_CHANGE_PLAN.md ← IN PROGRESS
- [ ] Step 2: Git checkpoint with phase change note

### Foundation Documents (Critical)
- [ ] Step 3: 7BOD - Electrical
- [ ] Step 4: 5BOD - HVAC
- [ ] Step 5: SLD_Phase4_24MW.md (rename from SLD_Phase4_22MW.md)

### Detailed Technical Appendices
- [ ] Step 6: Appendix - Phase 4 Electrical Equipment and Cost Analysis
- [ ] Step 7: Appendix - Electrical House Design Notes

### Site & Infrastructure
- [ ] Step 8: 10BOD - Site and Infrastructure

### Executive Documents
- [ ] Step 9: _BOD - Exec Summary (MAJOR CONDENSING)
- [ ] Step 10: _TOC - Basis of Design Contents

### Supporting CSI Divisions
- [ ] Step 11: 1BOD - General Requirements (simplify Cx)
- [ ] Step 12: 0BOD - Procurement
- [ ] Step 13: 2BOD - Facility Construction
- [ ] Step 14: 3BOD - Fire Suppression
- [ ] Step 15: 4BOD - Plumbing
- [ ] Step 16: 6BOD - Integrated Automation
- [ ] Step 17: 8BOD - Communications
- [ ] Step 18: 9BOD - Electronic Safety & Security

### Cost Documents
- [ ] Step 19: Project Cost Summary - Phase 4 Full Build-Out
- [ ] Step 20: Land Acquisition and Soft Costs

### Final Verification
- [ ] Step 21: Global search - rack count references
- [ ] Step 22: Global search - old phase numbers (3/15/22 MW)
- [ ] Step 23: Consistency check across all documents
- [ ] Step 24: Mark execution complete

---

## Notes & Issues Tracker

### User Confirmations Needed
- **Transformer sizing:** Keeping 3.5 MVA, needs confirmation
- **MV Switchboard count:** User will provide later

### Important Reminders
- REDUCE word count throughout - be concise
- No full pricing updates yet (except racks $12M, Cx $3.6M)
- Maintain dual-ring topology with RMUs
- Maintain N+1 redundancy philosophy throughout
- Each document should be tighter and clearer than before

### Git Checkpoint Info
- **Commit before changes:** [TO BE ADDED]
- **Purpose:** Enable before/after comparison if needed

---

## Document Change Log

### [Document Name] - [Date]
- Changes made
- Issues encountered
- Notes

---

**Last Updated:** 2025-11-07
**Status:** IN PROGRESS
