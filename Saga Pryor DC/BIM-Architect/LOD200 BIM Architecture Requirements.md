
# Critical things to do now so the future architect can pick up immediately

(These are non-negotiable handoff items — produce these during the 6-week sprint)

1. **Cleaned source CAD/topo & survey**
    - Purged DWG, flattened Z, single origin, LandXML for topo if available.
2. **Shared coordinates + levels + grids (in Revit)**
    - Document the coordinate transform (method and origin). Provide a short README.
3. **Revit native model (not just DWG)**
    - Revit file (.rvt) containing massing, levels, grids, basic walls, roofs, and generic families for major equipment (switchgear, gensets, chillers, battery blocks, rack blocks). Use separate worksets for “visual” elements.
4. **IFC export (LOD200)**
    - Ensure IFC opens in a third-party viewer; include which IFC schema/version used.
5. **Federation snapshot**
    - NWC/NWD or consolidated IFC snapshot used for clash/clearance checks (one file).
6. **Assumptions table + BoD**
    - Clear numeric assumptions (rack U, MW per row, PUE band, up to 3 staging scenarios), single-line options, and the Basis of Design.
7. **Equipment schedules & footprints**
    - Simple CSV or schedule listing major equipment types, dimensions, weight, electrical demand, and long-lead status.
8. **Render files + view settings**
    - PNG/JPEG renders plus the Revit/Enscape camera settings or exported glTF so an architect can reproduce style.
9. **Model cleanup rules doc (mini-BEP)**
    - Naming conventions, levels, worksets, family guidelines, coordinate notes, required viewers, and accepted LOD.
10. **One-page “Architect Onboarding”**
    - Who to call, file locations, missing items (geotech, exact survey), and top three risks.

# Minimal “handoff package” checklist you can deliver to the architect (copy/paste)
- Cleaned DWG & LandXML topo.
- Native Revit file (.rvt) with Levels, Grids, massing, worksets.
- IFC LOD200 export + note on IFC schema.
- NWC/NWD federation snapshot (or consolidated IFC).
- Assumptions table (CSV) and BoD (PDF).
- Major equipment schedule (CSV) & conceptual single-line (PDF).
- 2 investor renders (PNG) + view settings.
- Mini-BEP / model rules (1 page).
- README: coordinates/origin, file versions, viewer recommendations, contact list.

---
# Minimal BEP items you must enforce (one-page)

- File naming convention + versioning.
- Shared coordinate origin and levels naming.
- LOD target = Revit LOD200 (non-permit). IFC export settings.
- Workset rule: Visualization vs Coordination vs Discipline families.
- Publish cadence: WIP daily, federation Tue/Thu, client packet Fridays.
- Clash cadence: one light Navisworks run per week and last run before each client review.
- Render spec: 3000×2000 PNG, aerial + approach, two rounds of comments.
- Delivery formats: PDF plans/elevations, .rvt, .ifc, .nwc, renders, BoD PDF, schedules CSV.
