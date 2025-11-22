**Created:** 2025-11-03
**Tags:** #sld #mermaid #electrical #context-save
**Status:** In Progress - Paused for Phasing Work

# SLD Mermaid Diagram Work - Context Save

## What We Were Doing

Creating Mermaid-based Single-Line Diagrams (SLDs) for the Pryor DC electrical system as an alternative to Erik's complex Python/PowSyBl approach.

## Decision: Mermaid vs. PowSyBl

**Chose Mermaid because:**
- ✅ Text-based, lives in Obsidian markdown
- ✅ Version controlled (git-friendly)
- ✅ No complex dependencies
- ✅ Easy to update/iterate
- ✅ Good enough for internal documentation and investor presentations

**PowSyBl approach issues:**
- ❌ API instability (Erik's code written for older version)
- ❌ Heavy Java dependency
- ❌ Overkill for documentation purposes
- ❌ Better suited for actual power flow analysis (not our need)

## Completed Work

### File Created:
`Saga Pryor DC/Basis of Design/SLD_Phase1_3MW.md`

**Contents:**
- Full Mermaid diagram showing Phase 1 electrical system
- Equipment tables with all ratings
- Load calculations (IT, Mechanical, Building)
- Redundancy validation checks:
  - ✅ Generator N+1: 8.0 MW available vs 5.7 MW load (140% margin)
  - ✅ Transformer N+1: 7.0 MVA available vs 6.3 MVA load (111% margin)
  - ✅ IT UPS N+1: 5,000 kVA available vs 3,333 kVA load (150% margin)
  - ⚠️ Mech UPS N+1: 1,750 kW available vs 1,700 kW load (103% margin - TIGHT)
- Failure scenario analysis
- Maintenance scenarios
- Design notes and rationale

**Diagram Structure:**
```mermaid
graph TB
    345kV Utility → 2× 25MVA Substation TX → 13.8kV Dual Rings (A/B)
    → 8 RMUs → 3× Generators + 3× Step-down TX
    → Dual LV Switchboards → IT UPS (5×1,250kVA) + Mech UPS (8×250kW)
    → Cabinet PDUs (dual-fed) → 30 Cabinets @ 100kW
```

## Still To Do

### Phase 2 SLD Document
**File:** `SLD_Phase2_12MW.md`

**Should include:**
- Updated Mermaid diagram showing:
  - +3 generators (6 total)
  - +5 transformers (8 total)
  - +8 IT UPS modules (13 total)
  - +12 Mech UPS units (20 total)
  - Loop 3 D2C cooling infrastructure
  - 30 cabinets upgraded to 400 kW each
- Phase 2 validation calculations
- Equipment additions table
- Incremental commissioning notes

### Validation Findings from Phase 1

**Issues to address:**
1. ⚠️ Transformer N+1 margin tight (11%) - may want to add 4th transformer earlier
2. ⚠️ Mech UPS margin very tight (3%) - recommend 9 units instead of 8
3. ✓ All other systems have healthy margins

## Python Tools Context

### Erik's Tool (`pachyderm_bod_generator.py`)
- Location: `powsybl-project/`
- Status: Not compatible with current pypowsybl API
- Purpose: Auto-generate SLDs from BOD text + run power flow analysis
- Decision: Too complex for our needs, Mermaid is simpler

### Our Simple Parser (`parse_pryor_bod_simple.py`)
- Location: `powsybl-project/`
- Status: Working, generated metadata JSON
- Output: `pryor_dc_electrical_metadata.json`
- Could adapt this to generate Mermaid syntax instead of JSON

### Test SLD Generated
- File: `powsybl-project/test_ieee_sld.svg`
- Showed that pypowsybl CAN generate proper SLDs
- But API compatibility issues make it not worth the effort

## Approach Going Forward

**Two-tier strategy:**
1. **Internal/Iteration:** Mermaid diagrams in Obsidian (fast, version controlled)
2. **External/Final:** Erik creates professional AutoCAD SLDs for investors/contractors (after design locked)

**Workflow:**
```
BOD Text → Claude generates Mermaid SLD → Validation checks → Erik review
                                                                    ↓
                                                            Design locked
                                                                    ↓
                                                    Erik → Professional SLD
                                                              (AutoCAD/EPLAN)
```

## Technical Validation Process

**Three levels:**
1. **Automated:** Capacity checks (N+1 margins, load balance)
2. **Claude:** Review for common issues, suggest improvements
3. **Erik:** Final engineering sign-off

**Key checks:**
- Generator N+1 capacity ≥ total load × 1.2
- Transformer N+1 capacity ≥ total load / PF
- UPS capacity ≥ IT load × 1.5
- Dual-ring isolation verified
- Maintenance scenarios don't create SPOFs

## Next Session: Resume SLD Work

1. Create Phase 2 SLD document
2. Possibly create Phase 3/4 outlines (depending on phasing plan)
3. Build simple Python script to auto-generate Mermaid from BOD (optional)

---

## Why We Paused

User needs to finalize **phasing strategy** first based on customer profiles and realistic growth plan.

**Phasing impacts SLD work because:**
- Number of phases determines how many SLD documents needed
- Equipment staging (when to add generators, transformers, etc.)
- Customer mix (AI inference vs training vs enterprise) affects load profiles
- Interruptible power (Customer #4) may require third power path

**Resume SLD work after phasing plan is finalized.**

---

**Context saved:** 2025-11-03 14:50
**Ready to resume:** After phasing discussion complete
