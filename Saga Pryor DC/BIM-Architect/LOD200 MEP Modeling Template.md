
# MEP Modelling Template — LOD200

Purpose: Give the BIM Architect a single, practical cheat-sheet to model MEP/electrical at **LOD200** so the model proves fit, supports renders, and hands off cleanly for LOD300. Keep families simple, put everything reproducible in the right worksets, and include the key parameters that the Architect of Record will need.

---

## 1) Worksets & Organization (must do)

- **Worksets (minimum):**
    
    - `ARCH` — architectural massing & building shell
    - `COORDINATION` — generic placeholders & equipment blocks used for spatial coordination (included in IFC)
    - `MEP` — mechanical/plumbing conceptual elements (if discipline-owned)
    - `ELEC` — electrical conceptual elements (switchgear/UPS footprints)
    - `VISUALIZATION` — trees, people, high-poly entourage, detailed furnishings (_**exclude**_ from IFC)
    - `SITE` — topo, battery yard, external equipment
- **Rule:** Visual-only families → `VISUALIZATION`. Anything intended for IFC/handoff → `COORDINATION` or discipline workset.

## 2) Family naming & placeholders (copy/paste convention)

- Format: `PLACEHOLDER_<DISC>_<TYPE>_<LxW>[_H<H>]_v#`    
    - Examples:
        - `PLACEHOLDER_ELEC_SWITCHGEAR_3.0x2.0_v1            
        - `PLACEHOLDER_BESS_CONTAINER_6.0x2.5_H2.8_v1` 
        - `PLACEHOLDER_CHILLER_4.0x3.0_v1`            
- Tag **all** placeholder families with the word `PLACEHOLDER` so they can be filtered/removed easily.
- Keep geometry minimal (box or simple extrusion), not manufacturer detail.

## 3) Required Revit Project Parameters (add as Project Parameters)

Add these parameters to every placeholder family (recommended parameter type in parentheses):
- `Placeholder_Type` (Text) — e.g., `Switchgear / UPS / BESS / Chiller`
- `Footprint_L_m` (Number) — length in meters
- `Footprint_W_m` (Number) — width in meters
- `Height_m` (Number) — overall height (optional)
- `Electrical_kW` (Number) — connected demand (kW) or design kW
- `Cooling_kW` (Number) — if applicable (kW / ton)
- `Weight_kg` (Number) — gross/unit weight (if known)
- `LeadTime_wks` (Number) — vendor lead time in weeks (if known)
- `Assumption_Confidence` (Text / select) — `High / Medium / Low`
- `Placeholder_Notes` (Text) — short free text (fire, ventilation, special clearances)

**Why:** these drive Assumptions CSV and help future AOR scope LOD300.

## 4) Riser, Penetration & Corridor conventions

- **Risers:** place a simple shaft family `PLACEHOLDER_RISER_<ID>_v1` (min. L×W) at each vertical stack location. Tag with `Riser_ID` and `Reserved_for` (ELEC/MEP/COMM).
- **Penetrations:** model slab/wall void boxes `PENETRATION_ZONE_<TYPE>_<size>_v1` in `COORDINATION` to mark required openings.
- **Routing corridors:** represent major tray/busway corridors as thin extruded solids or filled regions (`CORRIDOR_TRAY_600mm_v1`) with parameter `Corridor_Width_mm`.

## 5) IFC / Export properties (IFC4 LOD200 minimal set)

Map Revit params to IFC properties for export. Minimum required property sets:

- `Name` → Revit Family Instance Name
- `Type` → `Placeholder_Type`
- `Footprint` → `Footprint_L_m` × `Footprint_W_m` (include both fields separately)
- `Height` → `Height_m`
- `Electrical` → `Electrical_kW`
- `Cooling` → `Cooling_kW`
- `Weight` → `Weight_kg`
- `LeadTime` → `LeadTime_wks`
- `Confidence` → `Assumption_Confidence`
- `Notes` → `Placeholder_Notes`

**Export note:** exclude `VISUALIZATION` workset from IFC. Use IFC4 Reference View; test open in BIM Vision and save screenshot.

## 6) White-space & Rack placeholders

- Create rack family `PLACEHOLDER_RACK_0.6x1.0_v1` and assemble rows as expected.
- Tag rows with `Row_ID`, `Racks_Per_Row`, `kW_per_rack` (or kW_per_row).
- Define hot/cold aisles with simple extrusion families `AISLE_HOT/COLD` and label containment approach in `Placeholder_Notes`.

## 7) Minimum deliverable items from BIM Architect (for MEP placeholders)

- Native `.rvt` with Levels/Grids, Worksets, named views used for renders.
- `COORDINATION` workset contains all placeholders, risers, corridor volumes.
- IFC4 LOD200 export (opens in BIM Vision) + 1 screenshot.
- Equipment Schedule CSV auto-generated from Revit parameters (columns below).
- Short `README_MEP.md` with coordinate origin, workset list, and where placeholders live.

## 8) Equipment Schedule CSV columns (auto-export from Revit)

- `Item_ID`, `Placeholder_Name`, `Placeholder_Type`, `Footprint_L_m`, `Footprint_W_m`, `Height_m`, `Electrical_kW`, `Cooling_kW`, `Weight_kg`, `LeadTime_wks`, `Assumption_Confidence`, `Placeholder_Notes`, `Model_File_Link`

(You’ll get this automatically from Revit schedules—export to CSV.)

## 9) Best practices & quick QC checklist (do before publishing)

- Verify shared coordinates and Levels/Grids documented in `README_COORDINATES.md`.
- Confirm all visualization props are in `VISUALIZATION` and excluded from IFC export.
- Run IFC export → open in BIM Vision → check that: footprints align with topo, parameters are present, and riser positions are visible. Save 3 screenshots (plan, section, 3D).
- Produce one-page `Assumptions_SAGA_DC.csv` (from exported schedule) and attach to BoD.
- Keep family versions small and name with `_v1` so updates are traceable.

## 10) Quick examples (copy into project folder)

- `PLACEHOLDER_BESS_CONTAINER_6.0x2.5_H2.8_v1.rfa` — params: Footprint_L=6.0, Footprint_W=2.5, Height=2.8, Electrical_kW=2000, LeadTime_wks=16, Confidence=Medium.
- `PLACEHOLDER_SWITCHGEAR_3.0x2.0_v1.rfa` — params: Footprint_L=3.0, Footprint_W=2.0, Electrical_kW=0 (panel-level), Notes: “Allow 1m front clearance.”