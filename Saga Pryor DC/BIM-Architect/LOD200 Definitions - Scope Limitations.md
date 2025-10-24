For an LOD200 investor/BoD package you are _not_  expected to fully map mechanical and electrical runs (detailed ducts, trays, conduits, piping) in Revit. Instead provide _accurate placeholders, footprints, single-line concepts and reserved routing corridors/penetration zones_ so a future Architect/MEP team can pick up at LOD300. 

Below I explain exactly what LOD200 covers, what you should include for MEP and interiors for this project, what to _not_ do, and a copyable checklist you can deliver now so the next architect can hit the ground running.

---

# What LOD200 means (practical, short)
- **Geometry:** approximate size, location, orientation — representative generic elements, not fabrication-ready.
- **Information:** basic metadata (name, type, approximate dimensions, maybe a capacity number).
- **Use:** proof of fit, massing, capacity counts, high-level clash avoidance, cost/area estimates, and investor visuals.
- **Not included:** precise fabrication geometry, final routing, conduit/duct/piping sizes for construction (that’s LOD300+).

# For MEP & electrical on an LOD200 investor package — what _you should_ provide

(These are the things investors and the next Architect will expect.)
1. **Major equipment footprints (native Revit / generic families)**
    - Switchgear, transformer pad, UPS room footprint, genset containers, chillers, AHU/CRAH/CRAC footprint, battery enclosures (container size L×W×H), fuel storage footprint.
    - Tag each with metadata: footprint L×W×H, weight (if known), electrical or cooling demand (kW/kVA or kW/ton), and lead-time flag.

2. **Single-line electrical concepts (PDF + Revit annotation)**
    - N+1 vs 2N options, high-level single-line schematic, approximate switchgear / distribution room locations, and busway routing _corridors_ (space reservations), not individual cable runs.

3. **Reserved routing corridors / keep-outs**
    - Indicate overhead/underfloor tray corridors, vertical shaft locations, and penetration zones through slabs/walls (as zones or simple extrusions). These can be simple 3D void families or shaded areas.
        
4. **Cooling strategy blocks**
    - Conceptual HVAC plant area, chilled-water plant footprint or reasonable ‘plant envelope’, and data-hall cooling clearances (hot/cold aisle geometry). State cooling approach (air-side containment, direct expansion, water-cooled chillers).
        
5. **Telecom / Meet-Me Room (MMR) location & ingress path**
    - Show MMR location, preferred entry points for fiber (conduit run corridor) and groundings/space for meet-me equipment.
        
6. **Rack / white-space layout (conceptual)**
    - Row and rack placeholders with U/rack assumptions, hot/cold aisle planning, and approximate spacing. Tag with IT load assumptions (kW/rack or kW/row).
        
7. **Basic vertical service risers**
    - General riser locations (where electrical, mechanical and telecom stack vertically) and reserved shaft sizes.
        
8. **Assumptions CSV & Equipment Schedule**
    - A simple table listing each placeholder item, dimensions, electrical demand, source of data, and confidence level. Vital for later LOD300 work.
        
9. **Render / Visual-only models on separate workset**
    - Visual entourage and high-poly props in `VISUALIZATION` workset only — ensure they’re excluded from IFC(so future architects don’t import junk).

# What _not_ to do at LOD200 (don’t waste time here)
- Don’t model **detailed ductwork, piping runs, cable tray routing, conduit runs or exact rack-level power connections**.
- Don’t build manufacturer-specific, fully-parametric families for everything (leave that for LOD300).
- Don’t attempt precise coordination of MEP service penetrations or in-slab conduit runs for foundation design.
- Don’t add detailed room finish or door hardware beyond what visually communicates scale.

# Why this level of work is right for investors & a future architect
- Investors need confidence that the building fits, that the white-space capacity is credible, and that long-lead items/spatial conflicts are visible.
- The future Architect of Record needs clean, documented placeholders and assumptions so they can move to LOD300 without redoing conceptual work. If you supply footprints, riser locations, single-line concepts, and an Assumptions CSV, they can pick up the model and add detailed routing.

# Practical modelling tips for the hybrid BIM Architect role
- Use **generic families** named with `PLACEHOLDER_<TYPE>_<V#>` (e.g., `PLACEHOLDER_SWITCHGEAR_3.0x2.0_v1`). Include a parameter `Placeholder_Comment` describing required clearances or notes.
- Put all visual-only props in a `VISUALIZATION` workset and exclude it from IFC export.
- Use _void_ families to mark penetration zones through slabs and walls.
- Add a Revit project parameter for `Assumption_Confidence` (High/Med/Low) on equipment placeholders.
- Export IFC4 Reference View with minimal property sets: Name, Type, Level, Dimensions, GUID, and a link to your Assumptions CSV.

# Acceptance checklist for the LOD200 deliverable (copy into your handoff README)
-  Native `.rvt` with Levels/Grids and documented shared origin.
-  Major equipment placeholders (switchgear, gensets, UPS, chillers, battery units) with L×W×H & kW values where known.
-  Concept single-line electrical PDF(s) (N+1 & 2N options).
-  Reserved routing corridors and riser locations (3D zones or extrusions).
-  Conceptual white-space layout with rack counts and IT load assumptions.
-  MMR location and telecom ingress corridor.
-  IFC4 LOD200 export that opens in BIM Vision / Solibri (screenshot proof).
-  Assumptions CSV & Equipment Schedule CSV (with owner and confidence).
-  Two investor renders (aerial + approach) — visualization workset excluded from IFC.
-  Mini-BEP / README_COORDINATES.md describing naming, worksets, ICC export settings, and how to reproduce renders.

# Quick wording you can use in the BoD / SOWs to set expectations

> “Deliverable LOD: Revit LOD200 (non-permit). LOD200 deliverables will include representative equipment footprints, single-line electrical concepts, reserved routing corridors and conceptual white-space layout. Detailed MEP routing (ductwork, cable tray/conduit runs, pipe routing) and manufacturer-specific family production are out of scope and will be provided at LOD300+ by the Architect of Record or MEP contractors.”
