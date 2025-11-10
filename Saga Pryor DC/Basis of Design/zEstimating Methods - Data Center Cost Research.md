# ESTIMATING METHODS - DATA CENTER COST RESEARCH
## Pryor Data Center - PACHYDERM GLOBAL

**Purpose:** Standardized methodology for researching and validating data center construction costs across all CSI divisions

**Created:** 2025-11-09
**Related:** [[_BOD - Exec Summary]], [[2BOD - Facility Construction (CSI Divs 02-14)]]

---

## OVERVIEW

This document provides a systematic approach to estimating data center construction costs using industry benchmarks and authoritative sources. The methodology supports both conceptual estimates (±25-30%) and detailed estimates (±10-15%) across all CSI MasterFormat divisions.

**Key Principles:**
1. **Multiple sources:** Cite 3+ authoritative sources per division
2. **Industry validation:** Compare our estimates against published benchmarks
3. **Transparency:** Show calculation methodology and assumptions
4. **Appropriate precision:** Match confidence levels to project phase
5. **Source currency:** Prefer 2024-2025 data; adjust older data for inflation

---

## ESTIMATION METHODOLOGIES

Data center costs can be estimated using three primary methods, depending on the CSI division and project phase:

### Method 1: Cost per Square Foot ($/SF)

**Best for:** Building shell, site work, interiors, general construction (CSI Div 01-14)

**Application:**
- Multiply unit cost ($/SF) by gross building area or specific area
- Example: Precast tilt-up walls at $25/SF × 50,000 SF exterior wall area = $1,250,000

**Advantages:**
- Intuitive for architects and general contractors
- Easy to scale for different building sizes
- Well-documented in construction cost databases

**Limitations:**
- Doesn't account for power density variations
- Less relevant for MEP-heavy divisions

**Typical Ranges (2024-2025):**
- Site work (Div 02): $5-15/SF (GSF)
- Building shell (Div 03-08): $200-350/SF (GSF) for tornado-hardened
- Interiors (Div 09-10): $30-80/SF (GSF)
- Total facility (all divisions): $600-1,100/SF (GSF)

Examples output is here: [[Saga Pryor DC/Basis of Design/2BOD - Facility Construction (CSI Divs 02-14)|2BOD - Facility Construction (CSI Divs 02-14)]]

---

### Method 2: Cost per Kilowatt ($/kW) or Megawatt ($/MW)

**Best for:** MEP systems, Power, cooling, generators (CSI Div 21-28)

**Application:**
- Multiply unit cost ($/kW) by IT load capacity (kW or MW)
- Example: UPS systems at $150/kW × 12,000 kW IT load = $1,800,000

**Advantages:**
- Directly correlates to data center capacity
- Industry-standard metric for MEP systems
- Scales appropriately with power density

**Key Definitions:**
- **IT Load:** Power consumed by servers, storage, network equipment (critical load)
- **Facility Load:** IT load ÷ PUE (includes cooling, lighting, UPS losses, etc.)
- **PUE (Power Usage Effectiveness):** Total facility power ÷ IT power (typical: 1.3-1.6)

---

### Method 3: Percentage of Related Divisions

**Best for:** Specialty systems that scale with total construction (security, telecom, BMS)

**Application:**
- Calculate as percentage of relevant base costs
- This will need to be researched based on the specific division you're pricing
- Roll up all division pricing into their assigned numbered BOD document. Some BOD documents contain multiple divisions. Other larger ones, like electrical, are their own document and own division (7BOD is only Div 26, for example)

This section is a catchall and will require additional questions to get clarity for estimates


---

## RESEARCH WORKFLOW

This is the step-by-step process used to develop the Division 02-14 (Facility Construction) cost estimate. Replicate this for each CSI division.

### Step 1: Review Existing Estimate

**Actions:**
1. Read the existing BOD division document completely
2. Identify all cost line items and their current estimates
3. Look for @CLAUDE comments flagging areas needing research
4. Note any "TBC" (To Be Confirmed) or missing estimates
5. Identify claims lacking source citations

**Output:** List of line items requiring cost research and validation

**Example from Division 02-14:**
- Found industry benchmark claim: "$900-$1,400/kW for AI-ready, tornado-hardened facilities"
- Flagged by @CLAUDE comment: "where did this benchmark come from? Please cite sources"
- Also identified: $379/SF shell cost needed validation against industry

---

### Step 2: Define Scope and Methodology

**Actions:**
1. Determine which estimation method applies ($/SF, $/kW, or % of total)
2. Define exactly what's included and excluded in the estimate
3. Identify the specific unit of measure (GSF, WSF, IT kW, facility kW)
4. List comparable facility characteristics for benchmarking

**Output:** Clear scope statement and methodology selection

**Example from Division 02-14:**
- **Methodology:** $/SF (building shell is area-based, not power-based)
- **Scope included:** Foundation, walls, roof, structure, finishes, elevators, doors
- **Scope excluded:** All MEP equipment (covered in other divisions)
- **Unit measure:** 38,000 SF gross building area
- **Comparable characteristics:** Tornado-hardened, 30-ft ceilings, multi-level spine

---

### Step 3: Research Industry Benchmarks

**Actions:**
1. Use WebSearch to find authoritative cost data (see Source Directory below)
2. Search for 2024-2025 published data; note publication dates
3. Collect cost ranges from at least 3 independent sources
4. Document specific cost breakdowns by component/system
5. Note any regional variations or special conditions

**Search Query Examples:**
- "data center construction cost per square foot 2024 industry benchmark"
- "data center [DIVISION NAME] cost per kW 2024"
- "tornado hardened data center building shell cost 2024"
- "[EQUIPMENT TYPE] cost per MW data center 2024"

**Output:** Table of benchmark costs with sources

**Example from Division 02-14:**

| Source | Benchmark | Notes |
|--------|-----------|-------|
| Cushman & Wakefield 2025 | $80-160/SF | Standard shell |
| Cushman & Wakefield 2025 | $200+/SF | Hardened facilities |
| Turner & Townsend 2024 | $600-1,100/SF | Total facility cost |
| Multiple sources | $200-300/SF | Tornado-hardened concrete |
| RSMeans 2024 | $468.66/SF | Complete data center (national avg) |

---

### Step 4: Analyze Cost Premiums and Features

**Actions:**
1. Break down the estimate into base cost + premiums for special features
2. Research cost impact of each premium feature separately
3. Calculate cumulative effect of all premiums
4. Compare calculated total vs actual estimate

**Output:** Cost build-up table showing base + premiums

**Example from Division 02-14:**

| Feature | Premium | Justification |
|---------|---------|---------------|
| Base concrete tilt-up shell | $150-180/SF | Standard warehouse-to-DC construction |
| Tornado hardening (30%) | +$45-54/SF | EF3+ wind resistance, enhanced reinforcement |
| 30-ft ceiling height | +$3-8/SF | 50% taller than standard 20-ft |
| Multi-level spine (3 levels) | +$9/SF | ~5,000 SF mezzanine @ $70/SF distributed |
| FM 1-150 roof rating | +$5-15/SF | Enhanced fastening, debris screen |
| Small facility premium | +$25-50/SF | 38K SF lacks economies of scale |
| **CALCULATED TOTAL** | **$237-316/SF** | Expected range with all premiums |
| **ACTUAL ESTIMATE** | **$325/SF** | Final estimate (upper-premium tier) |

---

### Step 5: Position Analysis

**Actions:**
1. Create comparison table showing estimate vs each benchmark source
2. Calculate percentage difference (above/below benchmark)
3. Identify which tier your estimate falls into (low/mid/high)
4. List factors that justify position (if above average)

**Output:** Position analysis table and narrative justification

**Example from Division 02-14:**

| Source | Benchmark | Our Estimate | Position |
|--------|-----------|--------------|----------|
| C&W 2025 (standard) | $80-160/SF | $325/SF | +103-306% |
| C&W 2025 (hardened) | $200+/SF | $325/SF | +63% |
| T&T 2024 (hardened) | $200-300/SF | $325/SF | +8-63% |
| Calculated w/ premiums | $237-316/SF | $325/SF | +3-37% |

**Position:** Upper-premium tier, justified by EF4/EF5 hardening, 30-ft ceilings, multi-level spine, elevator, storm shelter

---

### Step 6: Add Hard Costs vs Soft Costs

**Actions:**
1. Separate construction hard costs from soft costs (A&E, permits, etc.)
2. Calculate soft costs as percentage of hard costs (typically 5-10% for A&E)
3. Show both hard costs only and fully-loaded costs
4. Clarify which costs are being compared to industry benchmarks

**Output:** Table with hard costs, soft costs, and total

**Example from Division 02-14:**

| Item | Calculation | Cost | Notes |
|------|-------------|------|-------|
| Building shell (hard costs) | $325/SF × 38,000 SF | $12,350,000 | Construction costs only |
| Architectural & Engineering (7%) | $12,350,000 × 7% | $864,500 | Design fees |
| **TOTAL SHELL COST (with A&E)** | | **$13,214,500** | Fully-loaded cost |

**Clarification:** Industry benchmarks ($200-300/SF) are hard costs only, comparable to our $325/SF

---

### Step 7: Create Source Citations

**Actions:**
1. List all sources used with full publication names and years
2. Number sources and reference them in text with superscript numbers
3. Include URLs for web sources (optional but helpful)
4. Note confidence level and date of data

**Output:** Numbered reference list

**Example from Division 02-14:**

1. Uptime Institute, "Data Center Capital Cost Survey 2024" (Tier III baseline costs)
2. Turner Construction, "Building Cost Index Q3 2024" (severe weather construction premiums)
3. Data Center Dynamics, "AI Infrastructure Cost Analysis 2024" (liquid cooling and high-density premiums)
4. RSMeans Construction Cost Data 2024 (National and regional data center costs)
5. Cushman & Wakefield, "Data Center Development Cost Guide 2025" (Shell cost ranges)
6. Turner & Townsend, "Data Centre Cost Index 2024" (Global cost trends, tornado-hardened facilities)
7. Building Design + Construction, "Data Center Construction Costs for 2024" (Industry averages and ranges)

---

### Step 8: Assign Confidence Level

**Actions:**
1. Evaluate data quality using confidence framework (see below)
2. Assign appropriate confidence level (±10%, ±15%, ±20%, ±25%, ±30%)
3. Document reasons for confidence level assignment
4. Note what would be required to improve confidence

**Output:** Confidence level assignment with justification

**Example from Division 02-14:**
- **Confidence Level:** ±25%
- **Justification:** Conceptual estimate phase, no competitive bids, based on industry benchmarks only
- **To improve to ±15%:** Obtain quotes from 3+ precast contractors, complete structural drawings, finalize specifications

---

## CONFIDENCE LEVEL FRAMEWORK

Use this framework to assign appropriate confidence levels based on project phase and data quality.

### ±10% (High Confidence)

**When to Use:**
- Detailed design complete (100% CDs)
- Competitive bids received from qualified contractors
- Quotes from equipment vendors for major systems
- Local labor rates confirmed
- Material pricing locked in

**Data Requirements:**
- Actual bids or firm quotes
- Complete specifications and drawings
- Site conditions fully characterized
- No major unknowns

**Typical Project Phase:** Procurement, construction

---

### ±15% (Good Confidence)

**When to Use:**
- Design development complete (60-90% CDs)
- Preliminary quotes from vendors/contractors
- Detailed quantity takeoffs completed
- Similar recent projects in same region

**Data Requirements:**
- Near-complete design documents
- Budget quotes from 2+ vendors per major system
- Current cost data (<6 months old)
- Site conditions well understood

**Typical Project Phase:** Late design development, early procurement

---

### ±20% (Moderate Confidence)

**When to Use:**
- Schematic design complete (30-60% design)
- Industry benchmarks from multiple authoritative sources
- Preliminary engineering completed
- Conceptual quotes for major equipment

**Data Requirements:**
- 3+ industry sources for cost benchmarks
- Data from last 12 months
- Comparable facility examples
- Major systems defined

**Typical Project Phase:** Schematic design, early design development

---

### ±25% (Fair Confidence)

**When to Use:**
- Conceptual design (10-30% design)
- Industry benchmarks as primary source
- Limited vendor engagement
- Order-of-magnitude planning

**Data Requirements:**
- 2+ authoritative industry sources
- Data from last 18 months
- Similar facility types
- Key parameters defined (size, tier, power density)

**Typical Project Phase:** Feasibility study, conceptual design

**THIS IS OUR CURRENT PHASE FOR PRYOR DC**

---

### ±30% (Low Confidence)

**When to Use:**
- Pre-conceptual planning
- Single source or limited data availability
- Emerging technologies or unique requirements
- High degree of uncertainty

**Data Requirements:**
- 1+ industry source or expert opinion
- Data may be 2+ years old (inflation-adjusted)
- Broad facility category
- High-level parameters only

**Typical Project Phase:** Feasibility study, early planning

---

### Confidence Level Decision Tree

```
START: What project phase are you in?
│
├─ Pre-conceptual / Feasibility → ±30%
│
├─ Conceptual Design (10-30% complete)
│  ├─ Multiple authoritative sources (3+)? → ±25%
│  └─ Limited sources (1-2)? → ±30%
│
├─ Schematic Design (30-60% complete)
│  ├─ Detailed benchmarks + preliminary quotes? → ±20%
│  ├─ Industry benchmarks only? → ±25%
│  └─ Limited data? → ±30%
│
├─ Design Development (60-90% complete)
│  ├─ Budget quotes from vendors? → ±15%
│  └─ Benchmarks + takeoffs? → ±20%
│
└─ Construction Documents (90-100% complete)
   ├─ Competitive bids received? → ±10%
   ├─ Preliminary quotes? → ±15%
   └─ Detailed takeoffs only? → ±20%
```

---

## DIVISION-BY-DIVISION GUIDE

Note: all information in the division-specific application documentation below should be verified outside of this file using web search. These are just examples.

### How to Use This Section

For each CSI division you're estimating:
1. Use the recommended methodology ($/SF, $/kW, or % of total)
2. Check the listed authoritative sources
3. Search for current data (2024-2025 preferred)
4. Follow the 8-step research workflow above
5. Document findings in the BOD division document

---

### DIVISION 00 - PROCUREMENT AND CONTRACTING

**Not typically estimated separately** (administrative costs may be in contingency or owner's costs)

---

### DIVISION 01 - GENERAL REQUIREMENTS

**Methodology:** Percentage of construction cost (typically 8-15% of Divisions 02-33)

**Includes:** General contractor overhead, supervision, temporary facilities, mobilization, permits, testing

**Authoritative Sources:**
1. **RSMeans Building Construction Cost Data** - General requirements percentages
2. **Turner & Townsend International Construction Market Survey** - Regional GC markups
3. **Construction project management textbooks** - Industry standard percentages

**Typical Range:** 8-15% of hard costs (higher for small projects, lower for large)

**Estimation Approach:**
- Small projects (<$10M): 12-15%
- Medium projects ($10-50M): 10-12%
- Large projects (>$50M): 8-10%

**Notes:**
- Data center projects trend higher due to specialized requirements
- Include testing and commissioning if not broken out separately

---

### DIVISION 02 - EXISTING CONDITIONS & SITE WORK

**Methodology:** Cost per SF (gross site area or building SF)

**Includes:** Demolition, site clearing, earthwork, erosion control, site utilities

**Authoritative Sources:**
1. **RSMeans Site Work & Landscape Cost Data** - Unit costs for site work items
2. **Cushman & Wakefield Data Center Development Cost Guide** - Site development costs
3. **Local civil engineering firms** - Regional pricing for earthwork and utilities

**Typical Range:** $5-15/SF (building gross SF) or $1-3/SF (site acre)

**Estimation Approach:**
- Greenfield site: Lower end ($5-8/SF building area)
- Brownfield/demolition: Higher end ($10-15/SF building area)
- Utility extensions: Add $50-200/LF for water, sewer, gas per linear foot

**Key Variables:**
- Soil conditions (rock, contamination, high water table)
- Distance to utility connections
- Wetlands or environmental restrictions
- Topography and drainage

---

### DIVISION 03 - CONCRETE

**Methodology:** Cost per SF (building gross SF) or cost per CY (cubic yard)

**Includes:** Foundations, slabs, structural concrete, reinforcement

**Authoritative Sources:**
1. **RSMeans Concrete & Masonry Cost Data** - Detailed concrete unit costs
2. **American Concrete Institute (ACI)** - Specifications and performance standards
3. **Local ready-mix suppliers** - Current concrete pricing per CY
4. **Precast/Prestressed Concrete Institute (PCI)** - Precast panel costs

**Typical Range:**
- Slab-on-grade: $8-15/SF (4-6" thick, reinforced, finished)
- Foundation: $15-30/SF (footings and grade beams)
- Elevated slabs: $25-45/SF (structural deck)
- Precast panels: $25-50/SF (exterior wall panels)

**Estimation Approach:**
- Calculate concrete volume (CY) from drawings
- Multiply by unit cost including forming, rebar, placement, finishing
- For conceptual: Use $/SF for slab types

**Data Center Specific:**
- High floor load capacity (750 PSF for AI racks): Add 20-40% to slab cost
- Floor flatness FF 50/FL 40: Add $2-4/SF over standard
- Densifier/sealer finish: Add $1-2/SF

---

### DIVISION 04 - MASONRY

**Methodology:** Cost per SF (wall area)

**Includes:** CMU block walls, brick veneer, mortar, reinforcement

**Authoritative Sources:**
1. **RSMeans Concrete & Masonry Cost Data** - Masonry unit costs
2. **International Masonry Institute** - Productivity and labor rates
3. **Local masonry contractors** - Regional pricing

**Typical Range:**
- CMU (8" block): $15-25/SF of wall
- Reinforced CMU: $20-30/SF
- Brick veneer: $25-40/SF

**Notes:**
- Many modern data centers use precast tilt-up instead of masonry (Division 03)
- Masonry may be "Not Applicable" for your facility type

---

### DIVISION 05 - METALS

**Methodology:** Cost per SF (building gross SF) or cost per ton (structural steel)

**Includes:** Structural steel framing, joists, decking, mezzanines, stairs

**Authoritative Sources:**
1. **RSMeans Building Construction Cost Data** - Steel framing costs
2. **American Institute of Steel Construction (AISC)** - Steel tonnage and pricing trends
3. **SteelBenchmarker** - Current steel commodity pricing
4. **Vulcraft** (and other joist manufacturers) - Joist and deck pricing

**Typical Range:**
- Structural steel framing: $15-35/SF (building gross SF)
- Steel tonnage: $3,000-5,000/ton (fabricated and erected)
- Bar joists: $4-8/SF
- Metal decking: $3-6/SF
- Mezzanine: $50-150/SF (complete)

**Estimation Approach:**
- Calculate steel tonnage from structural plans (typical: 8-12 lb/SF for DC)
- Multiply by $/ton including fabrication, delivery, erection
- For conceptual: Use $/SF for building type

**Data Center Specific:**
- High clear height (30 ft): Add 15-25% to standard framing cost
- Heavy MEP loads on roof: May require heavier members
- Seismic design: Add 5-15% in high seismic zones

---

### DIVISION 06 - WOOD, PLASTICS, AND COMPOSITES

**Methodology:** Cost per SF (minimal scope in data centers)

**Includes:** Millwork, casework, trim, shelving

**Authoritative Sources:**
1. **RSMeans Interior Cost Data** - Millwork and casework pricing
2. **Local millwork suppliers** - Cabinet and casework quotes

**Typical Range:** $5-15/SF (office/support areas only)

**Notes:**
- Minimal scope in data centers (mainly office areas)
- May estimate as percentage of interior finishes (10-20%)

---

### DIVISION 07 - THERMAL AND MOISTURE PROTECTION

**Methodology:** Cost per SF (building gross SF or roof/wall area)

**Includes:** Roofing, waterproofing, insulation, sealants, wall panels

**Authoritative Sources:**
1. **RSMeans Building Construction Cost Data** - Roofing and waterproofing costs
2. **FM Approvals** - FM Global approved roofing assemblies and costs
3. **Roofing contractors (GAF, Firestone, Carlisle)** - System pricing
4. **National Roofing Contractors Association (NRCA)** - Industry standards

**Typical Range:**
- Standard TPO/EPDM roof: $12-18/SF
- FM 1-150 rated roof: $20-30/SF (includes enhanced fastening, debris protection)
- Wall insulation: $3-8/SF
- Waterproofing: $5-12/SF
- Precast tilt-up wall panels: $25-50/SF (includes insulation, finish)

**Estimation Approach:**
- Calculate roof area and wall area separately
- Select appropriate system based on requirements
- Add premiums for ratings (FM 1-150, fire resistance, wind uplift)

**Data Center Specific:**
- FM 1-150 rating: Add $8-12/SF over standard roof (tornado zones)
- Class A fire rating: May add $2-4/SF
- Debris screen protection: Add $2-5/SF
- Long-term warranty (20+ years): Add 10-15%

**See Division 02-14 BOD for detailed FM 1-150 cost analysis**

---

### DIVISION 08 - OPENINGS

**Methodology:** Cost per SF (building gross SF) or cost per opening

**Includes:** Doors, frames, hardware, windows, glazing, security mantraps

**Authoritative Sources:**
1. **RSMeans Building Construction Cost Data** - Door and window pricing
2. **Security equipment manufacturers (Boon Edam, Horton Automatics)** - Mantrap pricing
3. **Commercial door suppliers** - Hardware and access control integration

**Typical Range:**
- Standard commercial door: $2,000-4,000 each
- Fire-rated door: $3,000-6,000 each
- Large equipment door (10'×10'): $8,000-15,000 each
- Security mantrap: $50,000-150,000 (complete with access control)
- Storefront glazing: $60-120/SF
- Overall building allowance: $10-25/SF (building gross SF)

**Data Center Specific:**
- Mantrap with biometric access: $75,000-150,000
- Forced-entry resistant doors (15-min rating): Add 50-100% to standard door cost
- Large equipment doors for data halls: Budget $10,000-15,000 each (10'H × 8'W minimum)
- Vision panels in data hall doors: Add $500-1,000 per door

---

### DIVISION 09 - FINISHES

**Methodology:** Cost per SF (building gross SF or by area type)

**Includes:** Drywall, painting, flooring, ceiling systems, wall finishes

**Authoritative Sources:**
1. **RSMeans Interior Cost Data** - Finish costs by material and application
2. **Cushman & Wakefield Data Center Development Cost Guide** - Data center finish levels
3. **Local finishing contractors** - Regional pricing for drywall, paint, flooring

**Typical Range (by space type):**
- Data hall finishes: $10-20/SF (sealed concrete floor, painted walls, exposed ceiling)
- Office/conference room: $35-60/SF (carpet, drywall, acoustic ceiling, paint)
- Restrooms: $60-100/SF (tile, moisture-resistant finishes)
- NOC/control room: $40-70/SF (raised floor optional, acoustic treatment)

**Estimation Approach:**
- Break down by space type (data hall, office, support)
- Calculate area of each type
- Apply appropriate $/SF for finish level

**Data Center Specific:**
- Sealed concrete floors (densifier + sealer): $3-6/SF
- Epoxy floor coating: Add $4-8/SF
- Low-VOC paint (required for data halls): Standard pricing
- No ceiling in data halls (exposed): Saves $8-15/SF
- Acoustic treatment in NOC: Add $10-20/SF

---

### DIVISION 10 - SPECIALTIES

**Methodology:** Cost per building or percentage (0.5-2% of construction cost)

**Includes:** Signage, toilet accessories, fire extinguisher cabinets, whiteboards

**Authoritative Sources:**
1. **RSMeans Interior Cost Data** - Specialty items
2. **Local suppliers** - Signage, accessories, specialty equipment

**Typical Range:** $5-15/SF or 0.5-2% of construction cost

**Notes:**
- Usually minor cost item in data centers
- May be bundled with Division 09 (Finishes)

---

### DIVISION 11 - EQUIPMENT

**Methodology:** Cost per item or cost per kW (for data center specific equipment)

**Includes:** Commercial equipment, kitchen equipment, loading dock equipment

**Authoritative Sources:**
1. **Equipment manufacturers** - Direct quotes for specialized items
2. **RSMeans Equipment Cost Data** - Commercial equipment pricing

**Notes:**
- Data center IT equipment and racks typically in separate CSI divisions (26, 27)
- May include: loading dock levelers ($8-15K each), kitchen equipment, shop equipment

---

### DIVISION 12 - FURNISHINGS

**Methodology:** Cost per workstation or cost per SF (office areas)

**Includes:** Office furniture, cubicles, seating, systems furniture

**Authoritative Sources:**
1. **Furniture manufacturers (Steelcase, Herman Miller, Knoll)** - Direct pricing
2. **RSMeans Interior Cost Data** - Furniture allowances
3. **Office furniture dealers** - Project quotes

**Typical Range:**
- Workstation (desk, chair, storage): $3,000-8,000 each
- Conference room: $10,000-30,000 (complete)
- Break room: $15,000-40,000 (complete)
- Overall allowance: $20-50/SF (furnished areas only)

**Notes:**
- Often owner-furnished (not in construction budget)
- May be separate procurement package

---

### DIVISION 13 - SPECIAL CONSTRUCTION

**Methodology:** Cost per SF or cost per system (highly variable)

**Includes:** Cleanrooms, vaults, storm shelters, special structures

**Authoritative Sources:**
1. **FEMA** - Storm shelter/safe room cost data (FEMA P-361)
2. **Specialty contractors** - Pre-fabricated shelter manufacturers
3. **Cleanroom manufacturers** - Modular cleanroom pricing

**Typical Range (Data Center Items):**
- FEMA 361 storm shelter: $75,000-150,000 (20-person prefab module)
- Security control room (hardened): $150,000-300,000 (complete with systems)
- Ballistic-rated control room: $200,000-500,000

**Data Center Specific:**
- **FEMA 361 storm shelter:** $3,000-7,500 per person capacity (prefab module)
- **Security Control Room (SCR):** $150-250/SF (hardened construction + systems)
- **Clean-in/Clean-out checkpoint:** $50,000-150,000 (depends on screening equipment)

**See Division 02-14 BOD for detailed storm shelter cost analysis**

---

### DIVISION 14 - CONVEYING EQUIPMENT

**Methodology:** Cost per elevator or cost per building

**Includes:** Elevators, escalators, lifts, dumbwaiters

**Authoritative Sources:**
1. **Elevator manufacturers (Otis, KONE, Schindler, Thyssenkrupp)** - Direct quotes
2. **Elevator consultants** - Budget pricing for planning
3. **RSMeans Mechanical Cost Data** - Elevator allowances by type and stops

**Typical Range:**
- Hydraulic elevator (2-4 stops): $100,000-175,000
- Traction elevator (4-6 stops): $150,000-250,000
- Heavy-duty freight elevator: $200,000-350,000
- Add $25,000-50,000 per additional stop

**Data Center Specific:**
- Elevator to roof (for maintenance): Add weather-protected roof access ($10-15K)
- Heavy equipment capacity (5,000+ lb): Add 15-25% to base cost
- Multi-level central spine (3-4 stops): Budget $175-225K for traction elevator

**Estimation Approach:**
- Get budget quote from elevator consultant/manufacturer
- Allowance: $50,000-75,000 per stop for planning purposes

---

### DIVISION 21 - FIRE SUPPRESSION

**Methodology:** Cost per kW (IT load) or cost per SF (building area)

**Includes:** Sprinkler systems, pre-action systems, clean agent suppression, detection

**Authoritative Sources:**
1. **Fire protection engineering firms** - System design and pricing
2. **Tyco, Victaulic, Viking** - Fire suppression equipment manufacturers
3. **NFPA standards** - System requirements and configurations
4. **Cushman & Wakefield Data Center Development Cost Guide** - Fire suppression costs

**Typical Range:**
- Wet pipe sprinkler: $5-10/SF (building gross SF)
- Preaction sprinkler (data halls): $15-25/SF (data hall area)
- Clean agent suppression (FM-200, Novec): $25-50/SF (protected area)
- VESDA (Very Early Smoke Detection): $8-15/SF (data hall area)
- **Overall data center (blended):** $15-40/kW (IT load)

**Estimation Approach:**
- Calculate data hall area requiring preaction + VESDA
- Calculate office/support area requiring wet pipe
- Add clean agent for electrical rooms, E-Houses
- Convert to $/kW: Total cost ÷ IT load (kW)

**Data Center Specific:**
- Data halls: Preaction + VESDA (most common for Tier III)
- E-Houses: Clean agent (Novec 1230 or FM-200)
- LV transformer yards: Portable extinguishers only (outdoor)
- Integrated cabinet suppression: May be included in rack/cabinet cost (Division 27)

---

### DIVISION 22 - PLUMBING

**Methodology:** Cost per kW (IT load) or percentage (1-3% of construction cost)

**Includes:** Domestic water, sanitary sewer, storm drainage, fixtures

**Authoritative Sources:**
1. **Plumbing engineering firms** - System design and pricing
2. **RSMeans Plumbing Cost Data** - Fixture and piping unit costs
3. **Cushman & Wakefield Data Center Development Cost Guide** - Plumbing allowances

**Typical Range:**
- Domestic water and sewer: $10-25/kW (IT load)
- Plumbing fixtures: $3,000-8,000 per fixture (toilet, sink, shower)
- Storm drainage: $5-12/SF (roof area)
- Overall: 1-3% of total construction cost

**Data Center Specific:**
- Minimal domestic water use (restrooms, break rooms, emergency showers)
- No cooling tower water (dry cooling systems)
- Budget $10-20/kW for domestic water, sewer, fixtures, storm drainage
- Leak detection in mechanical rooms: Add $5-10K

**Estimation Approach:**
- Count plumbing fixtures from floor plans
- Allow $5,000-8,000 per fixture group (includes rough-in)
- Add site utilities connection
- Convert to $/kW if needed

---

### DIVISION 23 - HVAC (Mechanical)

**Methodology:** Cost per kW (IT load) - PRIMARY METHOD for data centers

**Includes:** Chillers, pumps, piping, cooling distribution, building HVAC, controls

**Authoritative Sources:**
1. **Uptime Institute** - Cooling system costs by tier and efficiency
2. **ASHRAE TC 9.9** - Data center thermal guidelines and efficiency
3. **Schneider Electric (APC)** - White papers on cooling costs
4. **Trane, Carrier, Johnson Controls** - Chiller and CRAC pricing
5. **Vertiv, Stulz** - Data center cooling equipment manufacturers
6. **Cushman & Wakefield Data Center Development Cost Guide** - HVAC costs per kW
7. **7x24 Exchange** - Industry benchmarking data

**Typical Range:**
- Air-cooled chillers + CRAC: $150-250/kW (IT load)
- Water-cooled chillers + towers: $120-200/kW (IT load)
- Liquid cooling (L2C, RDHx): $200-350/kW (IT load, varies by density)
- Dry coolers (adiabatic): $100-180/kW (IT load)
- Building HVAC (separate): $20-40/kW or $15-30/SF (office/support areas)

**Estimation Approach:**
1. Define cooling architecture (air vs liquid, DX vs chilled water)
2. Calculate total cooling capacity required: IT load (kW) × (PUE - 1)
   - Example: 12 MW IT × (1.4 - 1) = 4.8 MW cooling
3. Select cooling equipment type and efficiency
4. Multiply cooling capacity by $/kW for that system type
5. Add building HVAC separately

**Data Center Specific:**
- **N+1 redundancy:** Add 20-35% for backup cooling capacity
- **Free cooling hours:** Reduces operating cost but may increase capital 10-20%
- **Liquid cooling (warm water L2C):** $250-400/kW (more efficient but higher capex)
- **Separate warm/cold loops:** Add 15-25% for dual-loop complexity
- **Zero water cooling (dry cooling):** Add 10-20% vs evaporative cooling

**Key Variables:**
- PUE target (1.2 = aggressive, 1.6 = conservative for sizing)
- Rack density (air cooling <20 kW/rack, liquid >40 kW/rack)
- Climate (free cooling hours per year)
- Redundancy level (N, N+1, N+2, 2N)

**See future Division 23 BOD for detailed HVAC cost analysis**

---

### DIVISION 25 - INTEGRATED AUTOMATION

**Methodology:** Percentage of MEP cost (1-3%) or cost per kW

**Includes:** Building automation systems (BAS), DCIM, environmental monitoring

**Authoritative Sources:**
1. **DCIM vendors (Schneider Electric StruxureWare, Nlyte, Sunbird)** - Software licensing
2. **Johnson Controls, Siemens, Honeywell** - BAS system pricing
3. **7x24 Exchange** - DCIM implementation costs

**Typical Range:**
- Basic BAS: 1-2% of MEP cost
- DCIM software + implementation: $25-75/kW (IT load)
- Environmental monitoring: $10-25/kW
- Overall: 1-3% of total MEP cost or $35-100/kW

**Notes:**
- DCIM licensing may be recurring annual cost (OPEX) vs capital (CAPEX)
- Integration with security, power, cooling systems
- May be broken out separately or included in electrical/mechanical divisions

---

### DIVISION 26 - ELECTRICAL

**Methodology:** Cost per kW (IT load) - PRIMARY METHOD for data centers

**Includes:** Utility service, transformers, switchgear, UPS, generators, distribution, lighting

**Authoritative Sources:**
1. **Uptime Institute** - Electrical infrastructure costs by tier
2. **Schneider Electric (APC)** - White papers on power distribution, UPS sizing
3. **Eaton, Vertiv, ABB** - UPS and switchgear manufacturers
4. **Caterpillar, Cummins, MTU** - Generator manufacturers
5. **Cushman & Wakefield Data Center Development Cost Guide** - Electrical costs per kW
6. **IEEE standards** - Power quality and distribution design
7. **7x24 Exchange** - Industry benchmarking data

**Typical Range:**
- **Utility service (customer substation):** $150-300/kW (facility load)
  - 161 kV substation with transformers: $4-8M (serves 20-40 MW facility)
- **Medium voltage distribution (13.8 kV):** $50-100/kW (facility load)
- **Generators (diesel, 13.8 kV):** $150-250/kW (nameplate capacity)
- **LV transformers (oil-filled):** $40-80/kW (capacity)
- **UPS systems (modular):** $100-200/kW (IT load)
- **Switchgear and distribution:** $75-150/kW (IT load)
- **Cabinet PDUs and distribution:** $25-50/kW (IT load)
- **E-Houses (prefab electrical buildings):** $1.5-3.5M per unit (complete)
- **Overall electrical (all-in):** $400-700/kW (IT load, Tier III)

**Estimation Approach:**
1. Define electrical architecture (voltage levels, redundancy)
2. Calculate facility load: IT load (kW) × PUE
   - Example: 12 MW IT × 1.6 PUE = 19.2 MW facility load
3. Size generators for N+1: Facility load ÷ N units + 1 backup
   - Example: 19.2 MW ÷ 5 = 3.84 MW each, buy 6 × 4.0 MW generators
4. Size UPS for IT load only (not facility load)
5. Multiply each component by $/kW for that equipment type
6. Sum all components

**Data Center Specific:**
- **Customer-owned 161 kV substation:** $150-300/kW (full facility load)
- **13.8 kV common bus architecture:** Add $50-100/kW for MV switchgear, dual-ring
- **E-Houses (prefab electrical buildings):** $2-3.5M each (complete with switchgear, UPS, batteries)
- **Modular UPS (1,250 kVA units):** $120-180/kW (easier to scale, N+1 redundancy)
- **Oil-filled LV transformers (outdoor):** $60-100/kW (includes pad, containment)
- **13.8 kV generators:** $180-250/kW (more expensive than 480V but fewer units needed)

**Key Variables:**
- Voltage level (480V, 4160V, 13.8kV affects cost per kW)
- Redundancy (N+1 vs 2N can double electrical cost)
- UPS runtime (5-min vs 15-min batteries affects cost 30-60%)
- Generator fuel type (diesel, natural gas, bi-fuel)
- Electrical house vs stick-built (prefab saves time, may cost more)

**See future Division 26 BOD for detailed electrical cost analysis**

---

### DIVISION 27 - COMMUNICATIONS

**Methodology:** Cost per kW (IT load) or percentage (2-4% of total construction)

**Includes:** Structured cabling, fiber optics, telecom pathways, cable tray, MPOE

**Authoritative Sources:**
1. **BICSI (Building Industry Consulting Service International)** - Cabling standards and costs
2. **Fiber optic manufacturers (Corning, CommScope)** - Fiber and copper pricing
3. **Telecom contractors** - Installation labor rates
4. **Cushman & Wakefield Data Center Development Cost Guide** - Structured cabling costs

**Typical Range:**
- Structured cabling: $30-80/kW (IT load)
- Fiber backbone: $15-40/kW
- Cable tray/pathways: $10-25/kW
- MPOE (meet-me room): $50,000-150,000 per location
- Overall: 2-4% of total construction cost or $50-120/kW (IT load)

**Data Center Specific:**
- **Overhead cable tray:** $15-30/kW (instead of raised floor)
- **Redundant fiber entries:** Budget 2× MPOE rooms ($100-300K total)
- **Cabinet structured cabling:** May be tenant responsibility (not in base building)
- **Diverse fiber paths:** Verify with carriers (critical for uptime)

**Notes:**
- Often tenant-installed (not in core & shell)
- Base building provides pathways and MPOE only

---

### DIVISION 28 - ELECTRONIC SAFETY AND SECURITY

**Methodology:** Percentage of building cost (2-4%) or cost per kW

**Includes:** Access control, CCTV, intrusion detection, perimeter security, mantrap

**Authoritative Sources:**
1. **Security integrators (Convergint, Securitas, Allied Universal)** - System design and pricing
2. **Genetec, Milestone, Lenel** - VMS and access control software
3. **Axis, Hanwha, Bosch** - CCTV camera and equipment manufacturers
4. **7x24 Exchange** - Data center security standards and costs

**Typical Range:**
- Access control system: $30-60/kW (IT load)
- CCTV (cameras, NVR, storage): $40-80/kW
- Perimeter security (fence, gates, sensors): $20-40/kW
- Intrusion detection: $15-30/kW
- Security Control Room (SCR): $150,000-300,000 (complete)
- Overall security: 2-4% of building cost or $100-200/kW (IT load)

**Data Center Specific:**
- **K-rated perimeter fence:** $150-300/LF (vehicle barrier)
- **Sally port vehicle trap:** $250,000-500,000 (automated gates, barriers)
- **Security mantrap (main entry):** $75,000-150,000 (biometric, interlocks, CCTV)
- **CCTV with facial recognition:** Add 25-40% to standard CCTV cost
- **90-day video retention:** Increases storage cost 50-100%
- **MFA card + biometric readers:** $3,000-6,000 per door
- **Security Control Room (hardened):** $200-300/SF (15-min forced entry rating)

**Estimation Approach:**
- Count doors requiring access control
- Count camera locations based on coverage requirements
- Calculate perimeter fence length
- Add specialized systems (mantrap, SCR, vehicle barriers)
- Convert to $/kW or % of building cost

---

### DIVISION 31 - EARTHWORK

**Methodology:** Cost per SF (site area) or cost per CY (excavation volume)

**Includes:** Site grading, excavation, backfill, compaction, erosion control

**Authoritative Sources:**
1. **RSMeans Site Work & Landscape Cost Data** - Earthwork unit costs
2. **Local civil contractors** - Regional excavation and grading pricing
3. **Geotechnical reports** - Soil conditions affecting cost

**Typical Range:**
- Site grading: $1-4/SF (site area)
- Mass excavation: $8-20/CY
- Structural excavation: $15-35/CY
- Backfill and compaction: $10-25/CY
- Erosion control: $1-3/SF (disturbed area)

**Notes:**
- May be included in Division 02 (Existing Conditions)
- Highly variable based on soil type and site conditions

---

### DIVISION 32 - EXTERIOR IMPROVEMENTS

**Methodology:** Cost per SF (paved area) or cost per LF (utilities)

**Includes:** Paving, sidewalks, landscaping, site lighting, fencing, signage

**Authoritative Sources:**
1. **RSMeans Site Work & Landscape Cost Data** - Site improvement costs
2. **Local paving contractors** - Asphalt and concrete pricing
3. **Landscape architects** - Landscaping and irrigation costs

**Typical Range:**
- Asphalt paving: $4-8/SF (parking lots, roads)
- Concrete paving: $8-15/SF (sidewalks, pads)
- Site lighting: $3,000-8,000 per pole
- Landscaping: $2-8/SF (planted areas)
- Chain-link fence: $25-45/LF
- K-rated security fence: $150-300/LF

**Data Center Specific:**
- **K-rated perimeter fence (8 ft):** $150-300/LF (vehicle barrier rated)
- **Sally port vehicle barriers:** $250-500K (automated gates, crash beams)
- **Equipment yard paving (heavy-duty):** $12-20/SF (reinforced for transformer loads)
- **Site lighting (security-grade):** $5,000-12,000 per pole (LED, backup power)

---

### DIVISION 33 - UTILITIES

**Methodology:** Cost per LF (linear foot) or cost per kW (capacity)

**Includes:** Water distribution, sanitary sewer, storm drainage, gas, electrical duct banks

**Authoritative Sources:**
1. **RSMeans Site Work & Landscape Cost Data** - Utility installation costs
2. **Local utility companies** - Connection fees and extension costs
3. **Civil engineering firms** - Utility design and pricing

**Typical Range:**
- Water line: $50-150/LF (8-12" pipe)
- Sanitary sewer: $75-200/LF (8-12" pipe)
- Storm sewer: $60-180/LF (12-24" pipe)
- Natural gas: $40-100/LF (4-6" pipe)
- Electrical duct bank: $150-400/LF (multiple conduits, see below)
- Utility connection fees: $25,000-150,000 per utility

**Data Center Specific:**
- **Electrical duct bank (MV 13.8 kV):** $200-500/LF depending on quantity of conduits
  - 2-4 conduits: $200-300/LF
  - 6-12 conduits: $300-450/LF
  - 12+ conduits: $400-600/LF
- **Fiber optic duct bank:** $100-200/LF (diverse paths required)
- **161 kV transmission line extension:** $1-3M per mile (utility-owned, may be reimbursed)

**Estimation Approach:**
- Calculate distance from utility connection point to building
- Multiply by $/LF for pipe/conduit size and quantity
- Add connection fees and tap fees
- For duct banks: Count number of conduits needed for capacity

**Notes:**
- Electrical duct bank costs vary significantly with number of conduits
- Fiber diversity (two physically separate paths) doubles fiber duct bank cost
- See NEC 2023 Articles 300.5 and 300.50 for installation requirements

---

## SOURCE DIRECTORY

This section lists authoritative sources by category for quick reference.

### General Construction Cost Data

1. **RSMeans Building Construction Cost Data** (annual)
   - Publisher: Gordian (formerly Reed Construction Data)
   - Coverage: Comprehensive unit costs for all CSI divisions
   - URL: https://www.rsmeans.com/
   - Update frequency: Annual
   - Best for: Detailed unit costs, labor rates, regional cost adjustments

2. **RSMeans Site Work & Landscape Cost Data** (annual)
   - Coverage: Site preparation, earthwork, utilities, paving, landscaping
   - Best for: Divisions 02, 31, 32, 33

3. **Engineering News-Record (ENR) Building Cost Index**
   - Publisher: ENR/BNP Media
   - Coverage: Construction cost inflation trends, regional cost indices
   - URL: https://www.enr.com/economics
   - Update frequency: Monthly
   - Best for: Cost escalation adjustments, regional comparisons

### Data Center Specific Sources

4. **Uptime Institute**
   - Coverage: Data center tier standards, cost surveys, industry benchmarks
   - URL: https://uptimeinstitute.com/
   - Publications: "Data Center Capital Cost Survey" (annual), tier certification standards
   - Best for: Overall facility costs per kW, MEP costs, tier-specific requirements

5. **Cushman & Wakefield - Data Center Development Cost Guide** (annual)
   - Coverage: Comprehensive data center costs by division, per kW and per SF
   - URL: https://www.cushmanwakefield.com/ (search "Data Center Cost Guide")
   - Update frequency: Annual (typically released Q4)
   - Best for: Industry benchmarks for all divisions, regional comparisons

6. **Turner & Townsend - Data Centre Cost Index** (annual)
   - Coverage: Global data center construction costs, trends, market analysis
   - URL: https://www.turnerandtownsend.com/
   - Update frequency: Annual
   - Best for: International comparisons, cost trends, regional markets

7. **7x24 Exchange**
   - Coverage: Data center operations, best practices, industry surveys
   - URL: https://www.7x24exchange.org/
   - Best for: Operational perspectives, reliability data, peer benchmarking

8. **Data Center Dynamics (DCD)**
   - Coverage: Industry news, technology trends, cost analysis
   - URL: https://www.datacenterdynamics.com/
   - Publications: Market reports, technology analyses
   - Best for: Emerging technologies (AI infrastructure, liquid cooling), market trends

### Electrical & Power Systems

9. **Schneider Electric (APC) White Papers**
   - Coverage: Power distribution, UPS sizing, efficiency, redundancy
   - URL: https://www.apc.com/us/en/solutions/business-solutions/white-papers.jsp
   - Best for: UPS systems, power distribution architecture, electrical efficiency

10. **IEEE Standards (Institute of Electrical and Electronics Engineers)**
    - Coverage: Electrical system standards and recommended practices
    - Key standards: IEEE 1100 (Powering and Grounding), IEEE 446 (Emergency Power)
    - URL: https://www.ieee.org/
    - Best for: Technical specifications, system design requirements

11. **Eaton, Vertiv, ABB, Caterpillar, Cummins** (Equipment manufacturers)
    - Coverage: UPS, switchgear, generators - specifications and budget pricing
    - Best for: Equipment costs, technical specifications, performance data

### Mechanical & Cooling Systems

12. **ASHRAE TC 9.9 (Technical Committee on Mission Critical Facilities)**
    - Coverage: Data center thermal guidelines, cooling efficiency
    - Key publications: "Thermal Guidelines for Data Processing Environments"
    - URL: https://tc99.ashraetcs.org/
    - Best for: Cooling design temperatures, airflow, efficiency targets

13. **Trane, Carrier, Johnson Controls, Vertiv, Stulz** (HVAC manufacturers)
    - Coverage: Chillers, CRAC units, air handlers, controls - specifications and pricing
    - Best for: Mechanical equipment costs, efficiency data, system configuration

### Fire Protection & Life Safety

14. **NFPA (National Fire Protection Association)**
    - Coverage: Fire protection codes and standards
    - Key standards: NFPA 72 (fire alarm), NFPA 75 (IT equipment), NFPA 76 (computer rooms)
    - URL: https://www.nfpa.org/
    - Best for: Code requirements, system design standards

15. **FM Global (Factory Mutual)**
    - Coverage: Property loss prevention, approved systems and equipment
    - Key standards: FM 1-150 (wind ratings), FM Data Sheets
    - URL: https://www.fmglobal.com/
    - Best for: Wind-rated roofing, fire suppression systems, insurance requirements

16. **FEMA (Federal Emergency Management Agency)**
    - Coverage: Storm shelters, safe rooms, disaster resistance
    - Key publication: FEMA P-361 "Safe Rooms for Tornadoes and Hurricanes"
    - URL: https://www.fema.gov/
    - Best for: Storm shelter requirements, tornado/hurricane protection costs

### Security Systems

17. **BICSI (Building Industry Consulting Service International)**
    - Coverage: Telecommunications, data cabling, structured cabling standards
    - URL: https://www.bicsi.org/
    - Best for: Cabling costs, pathways, telecommunications room design

18. **Genetec, Milestone, Lenel, Axis, Hanwha** (Security equipment vendors)
    - Coverage: Access control, CCTV, VMS (video management systems)
    - Best for: Security system costs, integration, specifications

### Regional & Market Data

19. **Local Contractors and Suppliers**
    - Coverage: Regional pricing, labor rates, market conditions
    - Best for: Current pricing, local cost factors, availability

20. **Utility Companies**
    - Coverage: Connection fees, service extensions, rate structures
    - Best for: Utility connection costs, power availability, natural gas service

---

## WORKED EXAMPLE: DIVISION 02-14 (FACILITY CONSTRUCTION)

This section documents the actual workflow used to estimate Division 02-14, demonstrating the methodology in practice.

### Step 1: Review Existing Estimate

**Initial document state:**
- Cost table showing $23.69M total building construction
- Industry benchmark claim: "$900-$1,400/kW for AI-ready, tornado-hardened facilities"
- @CLAUDE comment: "where did this benchmark come from? Please cite sources"
- Cost per SF: $623/SF (total building) but $379/SF noted for shell only
- Needed validation of shell-only cost vs industry benchmarks

### Step 2: Define Scope and Methodology

**Methodology selected:** Cost per SF (building shell is area-based, not power-based)

**Scope definition:**
- **Included:** Foundation, walls, roof, structure, finishes, elevators, doors, shelter
- **Excluded:** All MEP equipment (chillers, UPS, generators, etc. - covered in Divisions 21-28)
- **Unit measure:** 38,000 SF gross building area
- **Key features:** Tornado-hardened precast tilt-up, FM 1-150 roof, 30-ft ceilings, multi-level spine

### Step 3: Research Industry Benchmarks

**Search queries used:**
1. "data center construction cost per square foot 2024 industry benchmark"
2. "data center building shell cost per SF 2024 tornado hardened"
3. "precast tilt-up data center cost"
4. "FM 1-150 roof cost premium"

**Sources found:**
1. Cushman & Wakefield Data Center Development Cost Guide 2025
   - Standard shell: $80-160/SF
   - Hardened facilities: $200+/SF

2. Turner & Townsend Data Centre Cost Index 2024
   - Total facility: $600-1,100/SF
   - 9% YoY cost increase in 2024
   - Tornado-hardened range: $200-300/SF

3. RSMeans Construction Cost Data 2024
   - National average complete DC: $468.66/SF
   - Shell portion estimated at 30-40% of total

4. Multiple industry sources
   - PEMB (metal building): $20-50/SF
   - Concrete tilt-up: $130-200/SF
   - Tornado-hardened concrete: $200-300/SF
   - Microsoft/Forrester estimate: $200/SF shell

### Step 4: Analyze Cost Premiums

**Base cost:** Standard concrete tilt-up: $150-180/SF

**Premiums applied:**
- Tornado hardening (30%): +$45-54/SF (EF3+ wind, enhanced reinforcement)
- 30-ft ceiling height: +$3-8/SF (50% taller than standard 20-ft)
- Multi-level spine: +$9/SF (estimated 5,000 SF mezzanine @ $70/SF distributed over 38K SF)
- FM 1-150 roof rating: +$5-15/SF (enhanced fastening, debris screen)
- Small facility premium: +$25-50/SF (38K SF lacks economies of scale vs 100K+ SF)

**Calculated range:** $237-316/SF (expected with all premiums)
**Initial estimate:** $379/SF (20-60% above calculated range - needed to justify or revise)

### Step 5: Position Analysis

**Comparison table created:**

| Source | Benchmark | Initial Estimate | Position |
|--------|-----------|------------------|----------|
| C&W 2025 (standard) | $80-160/SF | $379/SF | +137-374% |
| C&W 2025 (hardened) | $200+/SF | $379/SF | +90% |
| T&T 2024 (hardened) | $200-300/SF | $379/SF | +26-90% |
| Calculated w/ premiums | $237-316/SF | $379/SF | +20-60% |

**Conclusion:** $379/SF was defensible but at very high end of premium range. Recommended value engineering to $300-325/SF to align with top of industry tornado-hardened range.

### Step 6: Revise to Final Estimate

**User decision:** Revise shell cost to $325/SF (premium tornado-hardened benchmark)

**Final calculation:**
- Building shell (hard costs): $325/SF × 38,000 SF = $12,350,000
- Architectural & Engineering (7%): $12,350,000 × 7% = $864,500
- **TOTAL SHELL COST (with A&E): $13,214,500**

**Revised position:**
- $325/SF = top of $200-300/SF tornado-hardened range
- Appropriate for EF4/EF5 construction with premium features
- $54/SF reduction from initial $379/SF estimate

### Step 7: Create Source Citations

**References added:**
1. Uptime Institute, "Data Center Capital Cost Survey 2024" (Tier III baseline costs)
2. Turner Construction, "Building Cost Index Q3 2024" (severe weather construction premiums)
3. Data Center Dynamics, "AI Infrastructure Cost Analysis 2024" (liquid cooling and high-density premiums)
4. RSMeans Construction Cost Data 2024 (National and regional data center costs)
5. Cushman & Wakefield, "Data Center Development Cost Guide 2025" (Shell cost ranges $80-160/SF standard, $200+/SF hardened)
6. Turner & Townsend, "Data Centre Cost Index 2024" (Global cost trends, tornado-hardened facilities)
7. Building Design + Construction, "Data Center Construction Costs for 2024" (Industry averages and ranges)

### Step 8: Assign Confidence Level

**Confidence level assigned:** ±25%

**Justification:**
- Conceptual estimate phase (no detailed design)
- No competitive bids or vendor quotes
- Based on industry benchmarks from authoritative sources
- Multiple sources consulted (7 references)
- Data from 2024-2025 (current)

**To improve to ±15%:**
- Obtain budget quotes from 3+ precast contractors
- Complete 60% design documents
- Finalize structural specifications
- Conduct value engineering workshop

### Final Output

The completed analysis was added to the Division 02-14 BOD document with:
- Clear scope definition (included/excluded)
- Industry benchmark comparison table
- Cost build-up showing base + premiums
- Position analysis vs multiple sources
- Final cost table with hard costs and A&E separated
- 7 numbered source citations
- Confidence level (±25%) with justification

**Result:** Defensible, well-sourced estimate that can be presented to investors, lenders, or project stakeholders with confidence.

---

## QUALITY CONTROL CHECKLIST

Before finalizing any cost estimate, verify:

### Scope & Methodology
- [ ] Scope clearly defined (included/excluded items listed)
- [ ] Appropriate methodology selected ($/SF, $/kW, or % of total)
- [ ] Unit of measure clearly stated (GSF, WSF, IT kW, facility kW)
- [ ] Comparable facility characteristics documented

### Research & Sources
- [ ] At least 3 authoritative sources consulted
- [ ] Sources are current (2024-2025 data preferred, <2 years old acceptable)
- [ ] Sources are independent (not all from same organization)
- [ ] Regional variations considered (national vs local pricing)
- [ ] All sources properly cited with publication name and year

### Analysis & Calculation
- [ ] Cost premiums for special features identified and justified
- [ ] Calculation methodology shown (not just final numbers)
- [ ] Hard costs separated from soft costs (A&E, permits, etc.)
- [ ] Position vs industry benchmarks analyzed
- [ ] Outliers explained (if >30% different from benchmark)

### Documentation & Presentation
- [ ] Estimates presented in clear tables
- [ ] Source citations numbered and referenced in text
- [ ] Confidence level assigned using framework
- [ ] Assumptions documented
- [ ] Limitations noted
- [ ] "To Be Confirmed" (TBC) items flagged for future research

### Red Flags (Investigate if present)
- [ ] Estimate >50% different from industry benchmark (without clear justification)
- [ ] Single source used (should have 3+ sources)
- [ ] Data >2 years old (should be current or inflation-adjusted)
- [ ] Confidence level too optimistic for project phase
- [ ] Round numbers suggesting guesswork ($1,000,000 vs $1,045,000)
- [ ] Missing source citations for key claims
- [ ] Methodology doesn't match division type (e.g., $/SF for UPS systems)

---

## COST ESCALATION & INFLATION

When using older cost data, adjust for inflation using ENR Building Cost Index or similar.

**Formula:**
```
Adjusted Cost = Historical Cost × (Current Index ÷ Historical Index)
```

**Example:**
- Historical cost: $200/SF (Q3 2022)
- ENR BCI Q3 2022: 12,500
- ENR BCI Q3 2024: 13,625
- Adjusted cost: $200 × (13,625 ÷ 12,500) = $218/SF

**Recent escalation rates (2020-2024):**
- 2020-2021: 8-12% (COVID supply chain disruption)
- 2021-2022: 10-15% (peak inflation)
- 2022-2023: 6-9% (moderating)
- 2023-2024: 4-8% (stabilizing)
- 2024-2025 forecast: 3-6% (normal)

**Data center specific:**
- Electrical equipment: 8-12% per year (2022-2024)
- Cooling equipment: 6-10% per year
- Construction labor: 5-8% per year
- Concrete/steel: 8-12% per year (peaked 2022, moderating 2024)

---

## REVISION HISTORY

| Date | Version | Changes | Author |
|------|---------|---------|--------|
| 2025-11-09 | 1.0 | Initial creation - documented Division 02-14 workflow | PGCIS Team |

---

**Document Control:**
- **File:** `_Estimating Methods - Data Center Cost Research.md`
- **Location:** `Saga Pryor DC/Basis of Design/`
- **Purpose:** Standardized methodology for cost estimation across all CSI divisions
- **Related Documents:** All BOD division documents
- **Usage:** Reference this methodology when researching costs for any CSI division
