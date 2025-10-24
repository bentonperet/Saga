
# Mini‑BEP (6‑Week Investor Sprint) — Saga Energy

**Purpose:** Minimal, enforceable BIM rules to produce investor‑grade deliverables (Revit LOD200, IFC, renders) and a clean handoff for the future Architect of Record.

**Project ID / File Naming**
- Project short name: `SAGA_DC` (example).
- Revit naming: `SAGA_DC_<DISCIPLINE>_v###.rvt` (e.g., `SAGA_DC_ARCH_v001.rvt`).
- Exports: `SAGA_DC_<TYPE>_v###.<ext>` (e.g., `SAGA_DC_IFC_v001.ifc`, `SAGA_DC_RENDER_AERIAL_v001.png`).
    

**Shared Coordinates & Levels**
- Use a single site origin. Document the origin in `README_coordinates.txt` (method used, units, CRS if available).
- Create and freeze Revit Levels (Level names must match BoD: e.g., `L0_GRADE`, `L1_DATAHALL`).

**LOD Target & Deliverables**
- Deliverable LOD: **Revit LOD200 (non‑permit)**. IFC Export: **IFC4** (Reference View acceptable)
- Required deliverables: native .rvt, IFC LOD200, NWC/NWD federation snapshot, PDF plans & elevations, 2 renders (PNG), Assumptions CSV, BoD PDF, Mini‑BEP README.


**Worksets / Model Organization**
- Minimum worksets: `VISUALIZATION`, `COORDINATION`, `ARCH`, `STRUCT`, `MEP`, `ELEC`, `SITE`.
- Put purely visual-only geometry (trees, entourage, high‑poly props) in `VISUALIZATION` only — do not include in IFC exports.


**Families & Geometry Rules**
- Use generic symbolic families for major equipment footprints (switchgear, genset, chiller, battery rack, data‑rack). Keep geometry simplified for LOD200.
- Avoid excessive nested families; keep file sizes manageable.

**Publish & Versioning Cadence**
- WIP: daily saves (local). Central publish: Tue / Thu mornings (one consolidated .rvt). Client packet: Fridays (PDFs + renders + IFC snapshot if applicable).
    

**Clash & QA**
- Light clash check: weekly Navisworks (or Solibri) quick scan focusing on critical clashes: equipment vs access, battery yard vs truck access, major MEP vs white space.
- Final pre‑review: full federation clash run 48 hrs before client draft deliverable.
- IFC QA: open exported IFC in BIM Vision or Solibri to confirm geometry and property sets.

**IFC & COBie**
- Export schema: IFC4. Include minimal property sets (Name, Type, Dimensions, Level, GUID). COBie not required for this sprint but include a CSV mapping template.
    

**Render Spec (Investor‑grade)**
- Resolution: **3000 × 2000 px** PNG. Two views: Aerial context + approach/entry shot. Provide camera/view settings (Revit view name + Enscape/Twinmotion camera JSON or exported glTF).
- Two review rounds (draft + final). Provide short captions for each view (1 sentence).

**Acceptance Criteria**
- Revit .rvt opens and levels/coordinates documented. IFC opens in viewer without major geometry loss. Renders readable and captioned. BoD contains numeric assumptions. Assumptions CSV lists rack U, MW per rack/row, PUE band, staging scenario.
    

**Quick Contacts & Responsibilities (for 6‑week sprint)**
- Coordination & schedule: [Project Coordinator / PM — Owner].
- Architectural & renders: BIM Architect.
- Electrical concept: Electrical Lead.
- Mechanical concept: MEP Lead.
- Ops & assumptions: Ops Lead.