# Architect Onboarding & Handoff — One‑Page Checklist

**Goal:** Provide the incoming Architect of Record everything they need to move quickly from LOD200 investor package → LOD300+ permitable design.

**Handoff Package (files to deliver together)**

1. `SAGA_DC_ARCH_v###.rvt` (native Revit with Levels, Grids, Worksets)
2. `SAGA_DC_IFC_v###.ifc` (IFC4 LOD200) + note on IFC export settings
3. `SAGA_DC_FEDERATION.nwc` or `SAGA_DC_FEDERATION.ifc` (consolidated snapshot used for clash checks)
4. `SAGA_DC_PLAN_PDF_v###.pdf` and `SAGA_DC_ELEVATIONS_PDF_v###.pdf`
5. `SAGA_DC_RENDER_AERIAL_v###.png` and `SAGA_DC_RENDER_APPROACH_v###.png` + camera settings file(s)
6. `ASSUMPTIONS_SAGA_DC.csv` (fields: Item, Value, Unit, Source, Confidence) — include rack counts, U/rack, MW assumptions, PUE band, cooling strategy baseline
7. `EQUIP_SCHEDULE_SAGA_DC.csv` (major items: type, footprint LxW, weight, electrical demand, lead time)
8. `README_COORDINATES.md` (origin, units, CRS, how to align DWG / topo)
9. `MINI_BEP_README.pdf` (this doc) + `ARCH_ONBOARDING_README.pdf` (one‑page quick notes)

**Top 5 things the Architect will ask for — preempt these**
1. Geotechnical report (if piles or special foundation required).
2. True survey (control points / site monument coordinates).
3. Telecom paths & fiber ownership confirmation.
4. Interconnection status & utility POC / single‑line.
5. Any local zoning/height restrictions or floodplain maps.

**Model hygiene notes the Architect will appreciate**
- Keep visualization-only families in `VISUALIZATION` workset and exclude from IFC.
- Provide an `EXPORT_FILTER` parameter set for IFC exports (list of included categories & property mappings).
- Tag or mark any placeholder family with `PLACEHOLDER` in the family name and provide a short comment in `ASSUMPTIONS_SAGA_DC.csv`.

**Onboarding call agenda (30–45 min)**
- Quick tour of Revit file (levels, grids, origin) — 10 min.
- Review Assumptions CSV + BoD highlights — 10 min.
- Walk through major equipment schedule & long‑lead items — 10 min.
- Q&A & next steps (who owns LOD300 conversion + timeline) — 10–15 min.

**Suggested immediate next steps for Architect**
1. Import Revit + set project templates & company standards.
2. Confirm coordinate alignment with topo and survey.
3. Confirm which placeholders to convert to manufacturer families.
4. Scope LOD300 permit path and provide an estimate for gaps.

**Acceptance/handoff signoff**
- Deliverable checklist signed by Owner & Deliverable lead confirming: native .rvt opens, IFC opens, renders received, assumptions CSV accepted, and README coordinate check completed.