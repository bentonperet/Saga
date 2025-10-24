
# Terms & Definitions — Saga Energy 6-Week Investor Sprint

**Purpose:** a single reference to keep everyone—technical and non-technical—aligned on tools, file types, and project jargon. Use this in meetings, SOWs, and handoffs.

# Core tool & format definitions

### AutoCAD / DWG

- **AutoCAD:** a 2D/3D CAD authoring application widely used for drawings, details, and vendor-provided block geometry.
- **DWG:** the native file format produced by AutoCAD (and many other CAD tools). DWGs typically contain linework, blocks, annotations and can be linked into Revit as reference geometry.
- **Why it matters here:** Schneider Electric supplies DWG details. We _clean & prep_ DWGs (PURGE, AUDIT, flatten Z) and then **link** them into Revit as references for modeling.

### Revit

- **Revit:** a parametric BIM authoring tool used to create building information models: levels, walls, floors, families (objects), schedules, and view sets. Revit elements are “intelligent” (contain geometry + metadata) — unlike CAD lines.
- **Key abilities:** native parametric modeling, views/camera setups for renders, IFC export, worksharing, and LOD management.
- **Why it matters here:** Our LOD200 massing, plan/elevation PDFs, investor renders and IFC exports originate from the Revit model.
    

### IFC (Industry Foundation Classes)

- **IFC:** an open, neutral file format for exchanging BIM data between tools (Revit → other software). It carries geometry and property data.
- **IFC4 vs other versions:** IFC has versions (IFC2x3, IFC4, etc.). **IFC4** is newer and supports improved geometry and property handling; many viewers and platforms now prefer IFC4. Different versions can change what data transfers cleanly.
- **Why it matters here:** We deliver an **IFC4 LOD200** export so future architects and reviewers can open a neutral model without Revit.

### Navisworks
- **Navisworks:** a model federation and review tool used to combine multiple discipline models (NWC/NWD/IFC), run clash detection (Clash Detective), create 4D simulations (Timeliner), and produce coordinated snapshots.
- **Why it matters here:** Navisworks is primarily for _federating_ multiple Revit/IFC models and running automated clash checks — it’s optional now, but critical when multiple discipline Revit models exist.
- *note: we won't need this in our first phase.*

### BIM (Building Information Modeling)

- **BIM:** the process and technology of creating and using a digital representation of a building that contains geometry + metadata about elements. BIM supports coordination, scheduling (4D), costing (5D), and lifecycle handover.
- **Why it matters here:** BIM lets us quantify white-space, produce credible renders, and hand over structured data (IFC/COBie) to the future Architect and Operations teams.

### BEP (BIM Execution Plan)
- **BEP:** a short, project-level playbook that defines naming, coordinates, LOD, worksets, publish cadence, clash cadence, IFC export rules, and responsibilities.
- **Why it matters here:** A one-page Mini-BEP gives the small team consistent rules now; a fuller BEP is used later when many firms are collaborating.

---
# Project-specific concepts & jargon (quick definitions + why relevant)

- **LOD (Level of Development/Detail)**
    - **LOD200** (our target): approximate geometry and placeholders; _non-permitable_. Indicates scale, location and orientation but not full fabrication detail.
    - **LOD300+**: permit-level detail; would be produced by Architect of Record later.
    - _Relevance:_ We deliver LOD200 for investor evidence and handoff.
        
- **LOD200 IFC (Reference View)**
    - IFC export with minimal property sets (Name, Type, Level, Dimensions, GUID). Good for early-stage exchange.
        
- **COBie**
    - A spreadsheet-like format capturing asset information (for operations/O&M). Not required for this sprint, but relevant later for handover.
        
- **Federation / Federated model**
    - Combining multiple discipline models (arch, struct, MEP, elec) into one view (Navisworks or consolidated IFC) for coordination.
        
- **Clash detection / Clash log**
    - Automated checks (Navisworks) that find physical conflicts between elements (e.g., duct runs hitting structure). We will do light manual checks now; automated clash runs are for later.
        
- **NWC / NWD**
    - **NWC:** Navisworks cache file (export from Revit).
    - **NWD:** published Navisworks snapshot for distribution.
    - _Relevance:_ Used later for fast federation and sharing.
        
- **Workset**
    - Revit logical grouping (e.g., VISUALIZATION, COORDINATION, ARCH, MEP). Keeps visual-only geometry separate so IFC exports remain clean.
        
- **Families**
    - Revit’s parametric objects (e.g., doors, racks, chillers). We use simple/placeholder families for LOD200.
        
- **Shared coordinates**
    - A single site origin & coordinate transform so DWG, Revit and IFC align. Must be documented (README_COORDINATES.md).
        
- **Placeholders**
    - Simplified generic family blocks representing equipment (switchgear, genset, chiller, racks) with footprint L×W and clearance notes.
        
- **Hot aisle / Cold aisle**
    - Data-hall thermal containment concept: arrange racks to manage airflow. Important for rack layout and cooling strategy.
        
- **White space**
    - The area reserved for IT equipment (server racks). We quantify white-space capacity in the BoD.
        
- **Busway**
    - Overhead/side power distribution system used in data centers (connects switchgear to PDUs). Requires routing space and affects layout.
        
- **Switchgear / Genset / UPS**
    - **Switchgear:** main electrical distribution cabinets.
    - **Genset:** backup diesel/gas generator.
    - **UPS:** Uninterruptible Power Supply — provides clean power and short-term backup.
    - _Relevance:_ Their footprints and clearances are long-lead and change layout.
        
- **PUE (Power Usage Effectiveness)**
    - Ratio of total facility energy to IT energy. Used as a KPI in BoD (target PUE band).
        
- **N+1 / 2N**
    - **N+1:** redundancy with one extra module (e.g., 3 modules for 2 required).
    - **2N:** fully redundant independent paths (double capacity).
    - _Relevance:_ Electrical architecture options we diagram in the BoD.
        
- **Assumptions CSV**
    - A simple table listing numeric assumptions (rack U, MW/rack, PUE band, confidence). The future architect uses this to scope LOD300.
        
- **BoD (Basis of Design)**
    - Concise narrative plus diagrams that justify design choices, KPIs, single-line electrical options, cooling strategy, and staging.
        
- **LandXML**
    - Civil export format for contours/topo that imports cleanly into Revit (better than raw DWG contours).
        
- **Enscape / Twinmotion / V-Ray / Lumion**
    - Visualization tools that can render Revit models into investor-quality images. We’ll use one for the two required renders.
        
- **glTF**
    - Lightweight 3D export format that can be used for interactive models or to transfer camera/view settings for renders.
        
- **IFC schema / GUID**
    - **Schema:** the IFC version/structure (IFC2x3 vs IFC4).
    - **GUID:** globally-unique identifier for objects in IFC useful for asset mapping.
        
- **ACC / BIM360**
    - Autodesk Construction Cloud / BIM360 — platforms for document control and model storage. Useful later for multi-party collaboration.
        
- **Solibri**
    - Model-checking tool (similar to Navisworks) used for validation and rules-based QA.
        
- **Timeliner / 4D / 5D**
    - **4D:** linking model geometry to schedule (time).
    - **5D:** adding cost to that schedule for budget phasing. Mostly out-of-scope now.
        

---


# Quick reference abbreviations

- **CAD** — Computer Aided Design (DWG files).
- **BIM** — Building Information Modeling.
- **BEP** — BIM Execution Plan.
- **IFC** — Industry Foundation Classes.
- **PUE** — Power Usage Effectiveness.
- **MEP** — Mechanical, Electrical, Plumbing.
- **LOD** — Level of Development / Detail.
- **NWC / NWD** — Navisworks cache / published file.
- **BoD** — Basis of Design.
- **ACC** — Autodesk Construction Cloud (aka BIM360).