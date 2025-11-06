# SLD Generation Standards for BOD-to-Diagram Automation

**Document Version:** 1.0
**Date:** 2025-11-02
**Purpose:** Define consistent rules for generating professional single-line diagrams from Basis of Design documents

---

## 1. VISUAL STANDARDS

### 1.1 Color Palette (Ensure Readability)

**Equipment Colors (Light backgrounds for dark text):**
```css
MV Switchboards:    #E3F2FD  (Light Blue - Material Design Blue 50)
LV Switchboards:    #E8F5E9  (Light Green - Material Design Green 50)
Generators:         #FFF3E0  (Light Orange - Material Design Orange 50)
Transformers:       WHITE    (#FFFFFF)
RMUs:               #FFF9C4  (Light Yellow - Material Design Yellow 100)
UPS Modules:        #F3E5F5  (Light Purple - Material Design Purple 50)
Distribution:       #E0F2F1  (Light Teal - Material Design Teal 50)
```

**Contrast Requirements:**
- **RULE:** Light backgrounds (#E0-#FF range) MUST use dark text (#000000)
- **RULE:** Dark backgrounds (#00-#80 range) MUST use light text (#FFFFFF)
- **RULE:** Minimum contrast ratio: 4.5:1 (WCAG AA compliance)

**Ring/Bus Line Colors:**
```css
Ring A:             #E74C3C  (Red - distinct identification)
Ring B:             #3498DB  (Blue - distinct identification)
Utility Feed:       #27AE60  (Green)
Generator Feed:     #F39C12  (Orange)
Standard Bus:       #000000  (Black - 6px width)
Power Lines:        #000000  (Black - 2px width)
Control Lines:      #000000  (Black - 1px dashed)
```

### 1.2 Text Styles

```css
/* Title Block */
.title {
    font: bold 18px Arial;
    fill: #000;
}

.subtitle {
    font: bold 14px Arial;
    fill: #000;
}

/* Equipment Labels */
.equipment-label {
    font: bold 13px Arial;
    fill: #000;
}

.bus-label {
    font: bold 12px Arial;
    fill: #000;
}

.small-label {
    font: 10px Arial;
    fill: #000;
}

/* Ratings and Technical Data */
.rating {
    font: 10px Arial;
    fill: #333;
}

.annotation {
    font: 9px Arial;
    fill: #000;
}

/* Breaker/Feeder Labels */
.feeder-label {
    font: 8px Arial;
    fill: #666;
}

.note {
    font: italic 9px Arial;
    fill: #000;
}
```

**RULE:** Never use font sizes smaller than 7px (unreadable when printed)

### 1.3 Line Weights

```
Power Lines (3-phase):      2px
Bus (main distribution):    6px
Ring Bus:                   4px
Control Circuits:           1px (dashed 5,5)
Ground:                     2px
Neutral:                    1.5px
```

### 1.4 Symbol Standards (IEEE 315 / IEC 60617)

**Breaker (Closed):**
- Rectangle 16×24px with X pattern
- White fill, black stroke

**Breaker (Open):**
- Rectangle with gap and circle

**Transformer:**
- Two overlapping circles (dual-winding)
- Single circle for specific types

**Generator:**
- Circle with "G" symbol
- Typical radius: 30-40px

**Connection Point:**
- Solid black circle, 3-4px radius

---

## 2. LAYOUT STANDARDS

### 2.1 Power Flow Direction
**RULE:** Power flows TOP to BOTTOM (gravity model)

```
SOURCES (Top)
    ↓
GENERATION
    ↓
MV DISTRIBUTION
    ↓
TRANSFORMATION
    ↓
LV DISTRIBUTION
    ↓
LOADS (Bottom)
```

### 2.2 Spacing Requirements - SYMMETRICAL LAYOUT MANDATORY

**All spacing MUST be symmetrical and evenly distributed.**

```
Minimum Margins:              200px from canvas edge
Equipment Horizontal Spacing: 150px between items (must be equal)
Equipment Vertical Spacing:   250px between voltage levels (must be equal)
RMU Spacing:                  EQUAL distribution across width
Transformer Spacing:          EQUAL distribution across width
LV-SWBD Spacing:             EQUAL distribution (align under transformers)
Text Clearance:               15px MINIMUM from equipment boundaries
Cable Path Clearance:         15px MINIMUM from text
```

**Symmetry Rules (CRITICAL):**

1. **Horizontal Symmetry:**
   - Equipment must be centered on vertical axis
   - Left-side spacing = Right-side spacing
   - If N equipment items, spacing = `(canvas_width - total_equipment_width) / (N + 1)`

2. **Vertical Symmetry:**
   - Vertical spacing between levels must be equal
   - Top margin = Bottom margin (when feasible)
   - Breakers centered on power lines

3. **Equipment Distribution:**
   ```python
   # Calculate equal spacing
   def calculate_positions(canvas_width, equipment_count, equipment_width, margin):
       usable_width = canvas_width - (2 * margin)
       total_equipment_width = equipment_count * equipment_width
       available_space = usable_width - total_equipment_width
       spacing = available_space / (equipment_count + 1)

       positions = []
       for i in range(equipment_count):
           x = margin + spacing * (i + 1) + equipment_width * i + (equipment_width / 2)
           positions.append(x)

       return positions  # Returns center points, evenly spaced
   ```

**Example - 8 Transformers:**
```
Canvas: 4000px wide
Margin: 200px
TX width: 70px (2 × radius)
Equipment count: 8

Usable width = 4000 - 400 = 3600px
Total TX width = 8 × 70 = 560px
Available space = 3600 - 560 = 3040px
Spacing = 3040 / 9 = 337.8px

Position 1: 200 + 337.8 + 35 = 572.8px
Position 2: 572.8 + 70 + 337.8 = 980.6px
... (equal spacing between all)
```

**RULE:** Manual spacing adjustment NOT allowed - must use calculation

### 2.3 Text Clearance and Overlap Prevention (CRITICAL)

**MANDATORY RULE:** Text MUST NOT overlap or be obscured by:
- Cable pathways (power lines)
- Equipment graphic boundaries
- Other text labels
- Breaker symbols

**Text Placement Rules:**

1. **Equipment Labels:**
   - Position: Inside equipment box, centered
   - Clearance: 10px from all edges of box
   - If text too large → reduce font size or abbreviate
   - Never allow text to extend outside equipment boundary

2. **Breaker Labels:**
   - Position: **Offset 15-20px** to the side of breaker symbol
   - Never directly on top of breaker
   - Never overlapping power line
   - Typical position: `x = breaker_x + 20, y = breaker_y + 5`

3. **Cable Path Labels:**
   - Position: **15px minimum** offset from cable path
   - Placement: Above or to side of line (never on line)
   - For vertical lines: place to left or right
   - For horizontal lines: place above or below

4. **Rating Labels:**
   - Position: Below equipment, centered
   - Clearance: 15px below equipment boundary
   - Must not overlap with outgoing cable paths

**SVG Text Positioning Examples:**

```svg
<!-- CORRECT: Breaker label offset to side -->
<use href="#breaker-closed" x="500" y="300"/>
<text x="520" y="305" class="feeder-label">CB-1</text>
<!-- 20px offset to right, 5px down for alignment -->

<!-- WRONG: Label on top of breaker -->
<use href="#breaker-closed" x="500" y="300"/>
<text x="500" y="300" class="feeder-label">CB-1</text> ❌

<!-- CORRECT: Cable label offset from line -->
<line x1="500" y1="100" x2="500" y2="200" class="power-line"/>
<text x="520" y="150" class="annotation">PRIMARY</text>
<!-- 20px offset to right of vertical line -->

<!-- WRONG: Label on cable path -->
<line x1="500" y1="100" x2="500" y2="200" class="power-line"/>
<text x="500" y="150" class="annotation">PRIMARY</text> ❌
```

**Text Sizing Priority:**
1. **Try standard size** first (defined in CSS)
2. If overlap detected → **reduce font size** by 1-2px
3. If still overlaps → **abbreviate text** (e.g., "DISTRIBUTION" → "DIST")
4. If still overlaps → **reposition** equipment (increase spacing)

**Overlap Detection Checklist:**
Before finalizing diagram, verify:
- [ ] No text overlaps power lines
- [ ] No text overlaps equipment boxes
- [ ] No text overlaps breaker symbols
- [ ] No text overlaps other text
- [ ] All text is at least 15px from cable paths
- [ ] All text is at least 10px from equipment edges
- [ ] All text is readable at 100% zoom

### 2.4 Alignment Rules

- **Vertical equipment** (transformers, generators): Center-aligned on X-axis
- **Horizontal buses**: Perfectly horizontal lines (no slant)
- **Labels**: Center-aligned with equipment
- **Breakers**: Centered on power lines (not offset)
- **Text anchors**: Use `text-anchor="middle"` for centered text

### 2.4 Canvas Sizing

```
Compact Layout:     1600 × 1800 px
Standard Layout:    2400 × 2400 px
Detailed Layout:    3400 × 3200 px
Large Complex:      4000 × 3200 px
```

**RULE:** Choose canvas size based on equipment count:
- < 20 components: Compact
- 20-50 components: Standard
- 50-100 components: Detailed
- 100+ components: Large Complex

---

## 3. EQUIPMENT REPRESENTATION RULES

### 3.1 Switchboard Representation

**MV Switchboards:**
```svg
<rect width="240" height="100" class="mv-switchboard"/>
<line y1="20" y2="20" class="bus"/> <!-- Main bus inside -->
<text class="equipment-label">MV-SWBD-X</text>
<text class="annotation">13.8 kV</text>
<text class="rating">4000A | 65kAIC</text>
```

**LV Switchboards:**

**Critical Requirements:**

1. **Width:** Must accommodate **5 BREAKER POSITIONS** minimum
2. **Main bus:** Horizontal bus shown inside at top of box
3. **Connections:** ALL downstream connections from BOTTOM of graphic
4. **Incomer:** Connection from TOP (from transformer)

**Sizing:**
- **Width:** 200px minimum (40px per breaker position × 5 positions)
- **Height:** 100px minimum
- **Bus position:** 15px from top edge
- **Breaker positions:** Evenly spaced along bus

**SVG Implementation:**
```svg
<!-- LV Switchboard with 5 breaker positions -->

<!-- Incomer from transformer (from top) -->
<line x1="{x}" y1="{y-50}" x2="{x}" y2="{y}"/>
<use href="#breaker-closed" x="{x}" y="{y-25}"/>
<text x="{x+20}" y="{y-20}" class="feeder-label">CB-MAIN</text>

<!-- Switchboard box -->
<rect x="{x-100}" y="{y}" width="200" height="100" class="lv-switchboard"/>

<!-- Main bus inside (horizontal at top) -->
<line x1="{x-90}" y1="{y+15}" x2="{x+90}" y2="{y+15}" class="bus"/>

<!-- Labels -->
<text x="{x}" y="{y+45}" class="equipment-label" text-anchor="middle">LV-SWBD-N</text>
<text x="{x}" y="{y+65}" class="annotation" text-anchor="middle">480V/277V</text>
<text x="{x}" y="{y+85}" class="rating" text-anchor="middle">2000A | 5 Positions</text>

<!-- 5 Breaker positions (downstream from bottom) -->
<!-- Position 1 (leftmost) -->
<line x1="{x-80}" y1="{y+15}" x2="{x-80}" y2="{y+100}"/>
<use href="#breaker-closed" x="{x-80}" y="{y+120}"/>
<line x1="{x-80}" y1="{y+135}" x2="{x-80}" y2="{y+180}"/>
<text x="{x-80}" y="{y+110}" class="feeder-label" text-anchor="middle">1</text>

<!-- Position 2 -->
<line x1="{x-40}" y1="{y+15}" x2="{x-40}" y2="{y+100}"/>
<use href="#breaker-closed" x="{x-40}" y="{y+120}"/>
<line x1="{x-40}" y1="{y+135}" x2="{x-40}" y2="{y+180}"/>
<text x="{x-40}" y="{y+110}" class="feeder-label" text-anchor="middle">2</text>

<!-- Position 3 (center) -->
<line x1="{x}" y1="{y+15}" x2="{x}" y2="{y+100}"/>
<use href="#breaker-closed" x="{x}" y="{y+120}"/>
<line x1="{x}" y1="{y+135}" x2="{x}" y2="{y+180}"/>
<text x="{x}" y="{y+110}" class="feeder-label" text-anchor="middle">3</text>

<!-- Position 4 -->
<line x1="{x+40}" y1="{y+15}" x2="{x+40}" y2="{y+100}"/>
<use href="#breaker-closed" x="{x+40}" y="{y+120}"/>
<line x1="{x+40}" y1="{y+135}" x2="{x+40}" y2="{y+180}"/>
<text x="{x+40}" y="{y+110}" class="feeder-label" text-anchor="middle">4</text>

<!-- Position 5 (rightmost) -->
<line x1="{x+80}" y1="{y+15}" x2="{x+80}" y2="{y+100}"/>
<use href="#breaker-closed" x="{x+80}" y="{y+120}"/>
<line x1="{x+80}" y1="{y+135}" x2="{x+80}" y2="{y+180}"/>
<text x="{x+80}" y="{y+110}" class="feeder-label" text-anchor="middle">5</text>
```

**Downstream Connection Types:**
Each breaker position can feed:
- Distribution panels (DP)
- UPS systems (IT-UPS, M-UPS)
- Additional switchboards
- Direct equipment (pumps, chillers, etc.)
- PDUs (power distribution units)

**RULE:** ALL connections from LV-SWBD **MUST** originate from BOTTOM of graphic

### 3.2 RMU (Ring Main Unit) Representation - DUAL-FEED TOPOLOGY

**Critical Requirements:**

Each RMU **MUST** show:

1. **TWO MV INCOMERS at TOP of graphic:**
   - Primary incomer (from primary MV-SWBD)
   - Reserve incomer (from reserve MV-SWBD)
   - Both with breakers clearly labeled
   - Cable pathways shown from both sources

2. **Internal bus section:**
   - Horizontal bus connecting both incomers
   - Connection point (black dot) where transformer feeder tees off

3. **ONE OUTGOER at BOTTOM of graphic:**
   - Single feeder to transformer
   - Breaker labeled "TX" or "FEEDER"
   - Vertical path downward to transformer

**RMU Layout (Vertical Orientation):**
```
        PRIMARY          RESERVE
        MV-SWBD          MV-SWBD
           │                │
           │ (cable path)   │ (cable path)
           ↓                ↓
        [CB-IN1]        [CB-IN2]
           │                │
           └────[BUS]───────┘
                  │
                [Tee]
                  │
               [CB-TX]
                  │
                  ↓ (to transformer)
```

**SVG Implementation:**
```svg
<!-- RMU with dual incomers -->
<rect x="{x-60}" y="{y}" width="120" height="140" class="rmu-box"/>

<!-- Primary incomer from left MV-SWBD -->
<line x1="{x-30}" y1="{y-50}" x2="{x-30}" y2="{y+10}"/>
<use href="#breaker-closed" x="{x-30}" y="{y-20}"/>
<text x="{x-45}" y="{y-15}" class="feeder-label">PRI</text>

<!-- Reserve incomer from right MV-SWBD -->
<line x1="{x+30}" y1="{y-50}" x2="{x+30}" y2="{y+10}"/>
<use href="#breaker-closed" x="{x+30}" y="{y-20}"/>
<text x="{x+45}" y="{y-15}" class="feeder-label">RES</text>

<!-- Internal bus section -->
<line x1="{x-30}" y1="{y+10}" x2="{x+30}" y2="{y+10}" class="bus"/>
<circle cx="{x}" cy="{y+10}" r="4" fill="black"/>

<!-- Transformer outgoer -->
<line x1="{x}" y1="{y+10}" x2="{x}" y2="{y+60}"/>
<use href="#breaker-closed" x="{x}" y="{y+35}"/>
<text x="{x+15}" y="{y+40}" class="feeder-label">TX</text>
<line x1="{x}" y1="{y+60}" x2="{x}" y2="{y+140}"/>

<!-- RMU Labels -->
<text x="{x}" y="{y+80}" class="equipment-label">RMU-X</text>
<text x="{x}" y="{y+100}" class="annotation">630A SF6</text>
<text x="{x}" y="{y+115}" class="annotation">Dual Incomer</text>
```

**Cable Path Requirements:**
- **Primary path:** Solid line from primary MV-SWBD to RMU primary incomer
- **Reserve path:** Solid line from reserve MV-SWBD to RMU reserve incomer
- Both paths must be clearly visible and not overlap
- Label each path near the source: "PRIMARY" / "RESERVE"

**Spacing Requirements:**
- Minimum 80px vertical clearance above RMU for incomer paths
- Minimum 100px horizontal spacing between RMUs
- Incomer breakers: 30px from RMU top edge
- Internal bus: 10px below incomer breakers

### 3.3 Transformer Representation - CONNECTION ORIENTATION

**Critical Requirements:**

1. **INCOMER connection:** From TOP or LEFT of graphic (choose for symmetry)
2. **OUTGOER connection:** From BOTTOM or RIGHT of graphic (opposite of incomer)
3. **Path to LV-SWBD:** Connects to TOP of LV-SWBD graphic

**Orientation Rules:**

**Vertical Layout (Preferred):**
```
     RMU
      ↓ (incomer from top)
   [CB-HV]
      ↓
  ┌───────┐
  │  TX   │  (transformer circles)
  └───────┘
      ↓
   [CB-LV]
      ↓ (outgoer from bottom)
   LV-SWBD
```

**Horizontal Layout (when space constrained):**
```
RMU → [CB-HV] → ┌─TX─┐ → [CB-LV] → LV-SWBD
              (incomer)         (outgoer)
              from left         to right
```

**SVG Implementation (Vertical - Preferred):**
```svg
<!-- Transformer with connections -->

<!-- Incomer from RMU (from top) -->
<line x1="{x}" y1="{y-80}" x2="{x}" y2="{y-50}"/>
<use href="#breaker-closed" x="{x}" y="{y-65}"/>
<text x="{x+20}" y="{y-60}" class="feeder-label">CB-HV</text>
<line x1="{x}" y1="{y-50}" x2="{x}" y2="{y-35}"/>

<!-- Transformer symbol -->
<circle cx="{x}" cy="{y}" r="35" fill="white" stroke="black" stroke-width="2"/>
<circle cx="{x}" cy="{y}" r="28" fill="none" stroke="black" stroke-width="1"/>
<text x="{x}" y="{y-5}" class="annotation" text-anchor="middle">TX-N</text>
<text x="{x}" y="{y+8}" class="rating" text-anchor="middle">{kva}kVA</text>

<!-- Rating below transformer -->
<text x="{x}" y="{y+50}" class="annotation" text-anchor="middle">{hv}kV/{lv}kV</text>

<!-- Outgoer to LV-SWBD (from bottom) -->
<line x1="{x}" y1="{y+35}" x2="{x}" y2="{y+70}"/>
<use href="#breaker-closed" x="{x}" y="{y+85}"/>
<text x="{x+20}" y="{y+90}" class="feeder-label">CB-LV</text>
<line x1="{x}" y1="{y+100}" x2="{x}" y2="{y+150}"/>
```

**Sizing Based on Rating:**
- < 1,000 kVA: r=30px
- 1,000-5,000 kVA: r=35px (Saga Pryor - 3,500 kVA)
- > 5,000 kVA: r=40px

**Symmetry Rule:**
- If incomer is from TOP → outgoer to BOTTOM (vertical symmetry)
- If incomer is from LEFT → outgoer to RIGHT (horizontal symmetry)
- Never diagonal connections (breaks symmetry)

### 3.4 UPS Module Representation

**Individual modules** (not combined boxes):
```svg
<rect width="70" height="80" class="ups-module"/>
<text>IT-UPS-N</text>
<text>{kva} kVA</text>
<text>Li-Ion</text>
<text>5-min</text>
```

**RULE:** Show individual modules, not aggregated capacity

---

## 4. TOPOLOGY-SPECIFIC RULES

### 4.1 Ring Bus Topology

**Must show:**
1. Complete ring path (closed loop)
2. Each RMU with incomer/outgoer
3. Ring A and Ring B in different colors
4. Direction arrows optional but helpful
5. Tie breakers back to source MV switchboards

**Path Example:**
```
MV-SWBD-A → RMU-A1 → RMU-A2 → RMU-A3 → MV-SWBD-A (closed)
```

### 4.2 Radial Topology

**Must show:**
1. Single source point
2. Tree structure (no loops)
3. Clear branch points
4. Load at endpoints

### 4.3 Dual-Fed Topology

**Must show:**
1. Two independent sources
2. Automatic Transfer Switch (ATS) or tie breaker
3. Normally open/closed positions
4. Selectivity coordination

---

## 5. LABELING STANDARDS

### 5.1 Equipment Naming Convention

```
Generators:       GEN-1, GEN-2, GEN-3...
MV Switchboards:  MV-SWBD-A, MV-SWBD-B (by ring)
LV Switchboards:  LV-SWBD-1, LV-SWBD-2... (sequential)
Transformers:     TX-1, TX-2, TX-3... (sequential)
RMUs:             RMU-A1, RMU-A2 (ring letter + number)
UPS:              IT-UPS-1, M-UPS-1 (function prefix)
Distribution:     DP-1A, DP-1B (switchboard number + circuit)
```

### 5.2 Breaker Naming Convention

```
Main Breakers:      CB-MA (MV-SWBD A main)
Ring Breakers:      CB-RA1, CB-RA2 (Ring A tie)
Feeder Breakers:    CB-F1, CB-F2 (feeder number)
Transformer:        CB-TX1 (transformer number)
LV Breakers:        CB-L1, CB-L2 (LV circuit number)
```

### 5.3 Rating Display Format

```
Voltage:       13.8 kV (space before unit)
Current:       4000A (no space before unit)
Power kW:      4.0 MW or 4,000 kW (commas for thousands)
Power kVA:     3,500 kVA (commas for thousands)
Short Circuit: 65kAIC (no space)
Frequency:     60 Hz (space before unit)
```

---

## 6. BOD EXTRACTION RULES

### 6.1 Pattern Matching Priority

**Order of patterns to try:**
1. Heading format: `### Phase 1: N × rating unit`
2. Bold format: `**N × rating unit**`
3. Plain format: `N × rating unit Equipment`
4. Table format: `| **Parameter** | Value |`
5. Narrative format: "N units of rating each"

### 6.2 Section Extraction Rules

**CRITICAL:** Use proper section boundaries
```python
# CORRECT - matches only level-2 headers
r'##\s+SECTION NAME.*?(?=\n## [A-Z]|\Z)'

# WRONG - matches level-3 headers too
r'##\s*SECTION NAME.*?(?=##|\Z)'
```

**Section hierarchy:**
```
## MAIN SECTION          (Level 2 - extract from here)
### Sub-section          (Level 3 - included in extraction)
#### Detail             (Level 4 - included in extraction)
```

### 6.3 Default Values (when BOD missing info)

```python
DEFAULTS = {
    'mv_voltage': 13.8,        # kV (US data center standard)
    'lv_voltage': 0.48,        # kV (480V/277V standard)
    'generator_pf': 0.8,       # Power factor
    'ups_pf': 0.9,            # UPS power factor
    'transformer_count': 4,    # Minimum for N+1
    'rmu_count': 6,           # 3 per ring typical
    'rmu_rating': 630,        # Amps (standard RMU)
}
```

**RULE:** Always document assumptions in notes section

### 6.4 Validation Rules

**Must validate:**
- Generator count is reasonable (1-20 typical)
- Transformer sizing matches load
- UPS capacity matches IT load
- Voltage levels are standard (13.8kV, 4.16kV, 480V, 208V)
- Redundancy levels make sense (N, N+1, 2N)

**Warnings to issue:**
- Generator count > 20: "Unusually high"
- Transformer < 500 kVA: "Small for data center"
- UPS count = 0: "No UPS detected"
- Fuel type mismatch: "Check BOD section"

---

## 7. DOWNSTREAM DISTRIBUTION RULES

### 7.1 Distribution from Each LV-SWBD

**Standard configuration:**
Each LV switchboard should show **3 downstream circuits**:

```
LV-SWBD-N
    ├─ DP-NA (IT UPS fed loads)
    ├─ DP-NB (Mechanical UPS fed loads)
    └─ DP-NC (Lighting/Receptacles)
```

**RULE:** Show at least 3 typical load types per LV switchboard

### 7.2 Load Types to Show

```
IT Loads:          Cabinet PDUs (via IT UPS)
Mechanical Loads:  Chillers, Pumps, CDUs, CRAH (via Mech UPS)
Lighting:          Building lighting and receptacles
HVAC:              Building HVAC (non-critical)
Life Safety:       Emergency lighting, fire alarm
```

---

## 8. NOTES AND DOCUMENTATION

### 8.1 Required Notes Section

**Every SLD must include:**
1. Topology description
2. Redundancy levels
3. Key assumptions
4. Voltage levels
5. Standards compliance (IEEE 315, IEC 60617)
6. BOD source document reference

**Example:**
```
NOTES:
1. Dual ring topology provides N path redundancy
2. N+1 redundancy for generators, transformers, and UPS
3. Ring A (red) and Ring B (blue) operate independently
4. All ratings from BOD: 7BOD - Electrical (CSI Div 26)
5. IEEE Std 315 / IEC 60617 compliant symbols
6. Total IT capacity: 6.25 MVA | Mechanical: 2.0 MW
```

### 8.2 Title Block Requirements

```
Title:          PROJECT NAME - ELECTRICAL SINGLE LINE DIAGRAM
Subtitle:       Topology description | Key features
Reference:      BOD document name
Date:           YYYY-MM-DD
Revision:       Letter (A, B, C...)
Status:         FOR CONSTRUCTION / FOR REVIEW / PRELIMINARY
```

---

## 9. FILE NAMING CONVENTIONS

```
{project}_{topology}_sld_{detail-level}.svg

Examples:
saga_pryor_ring_sld_detailed.svg
datacenter_radial_sld_compact.svg
facility_dual-feed_sld_professional.svg
```

---

## 10. QUALITY CHECKLIST

Before finalizing any SLD, verify:

- [ ] All text is readable (minimum 7px font, good contrast)
- [ ] All equipment counts match BOD specifications
- [ ] All ratings displayed correctly (kW, kVA, voltage)
- [ ] All breakers shown at connection points
- [ ] Power flow is top-to-bottom
- [ ] Ring topology shows complete loop (if applicable)
- [ ] RMUs show incomer/outgoer (if applicable)
- [ ] Individual UPS modules shown (not aggregated)
- [ ] Downstream distribution shown for each LV-SWBD
- [ ] Equipment spacing is even and professional
- [ ] Color contrast meets WCAG AA (4.5:1 minimum)
- [ ] Notes section includes all required information
- [ ] Title block is complete
- [ ] IEEE 315 / IEC 60617 symbols used correctly
- [ ] No overlapping lines or text
- [ ] Canvas size appropriate for content

---

## 11. IMPLEMENTATION IN CODE

### 11.1 CSS Template (copy to all generators)

```css
<style>
/* Text Styles */
.title { font: bold 18px Arial; fill: #000; }
.subtitle { font: bold 14px Arial; fill: #000; }
.equipment-label { font: bold 13px Arial; fill: #000; }
.bus-label { font: bold 12px Arial; fill: #000; }
.small-label { font: 10px Arial; fill: #000; }
.rating { font: 10px Arial; fill: #333; }
.annotation { font: 9px Arial; fill: #000; }
.feeder-label { font: 8px Arial; fill: #666; }
.note { font: italic 9px Arial; fill: #000; }

/* Line Styles */
.power-line { stroke: #000; stroke-width: 2; fill: none; }
.bus { stroke: #000; stroke-width: 6; fill: none; }
.control-line { stroke: #000; stroke-width: 1; stroke-dasharray: 5,5; fill: none; }

/* Equipment Boxes - LIGHT BACKGROUNDS for readability */
.mv-switchboard { fill: #E3F2FD; stroke: #000; stroke-width: 2; }
.lv-switchboard { fill: #E8F5E9; stroke: #000; stroke-width: 2; }
.generator-box { fill: #FFF3E0; stroke: #000; stroke-width: 2; }
.transformer-box { fill: #FFFFFF; stroke: #000; stroke-width: 2; }
.rmu-box { fill: #FFF9C4; stroke: #000; stroke-width: 2; }
.ups-module { fill: #F3E5F5; stroke: #000; stroke-width: 1.5; }
.dist-panel { fill: #E0F2F1; stroke: #000; stroke-width: 1; }

/* Ring Bus Colors */
.ring-bus-a { stroke: #E74C3C; stroke-width: 4; fill: none; }
.ring-bus-b { stroke: #3498DB; stroke-width: 4; fill: none; }
</style>
```

### 11.2 Validation Function Template

```python
def validate_diagram_quality(metadata):
    """Validate SLD meets quality standards before generation"""
    issues = []

    # Check equipment counts
    if len(metadata['generators']) > 20:
        issues.append("WARNING: Generator count unusually high")

    if len(metadata['ups']) == 0:
        issues.append("ERROR: No UPS systems detected")

    # Check ratings
    for tx in metadata['transformers']:
        if tx['rated_s'] < 500:
            issues.append(f"WARNING: {tx['id']} rating seems low ({tx['rated_s']} kVA)")

    # Check voltage levels
    valid_mv = [4.16, 13.2, 13.8, 34.5]
    valid_lv = [0.208, 0.48, 0.6]

    for bus in metadata['buses']:
        if bus['voltage'] not in valid_mv and bus['voltage'] not in valid_lv:
            issues.append(f"WARNING: Non-standard voltage {bus['voltage']} kV")

    return issues
```

---

## REVISION HISTORY

| Rev | Date | Description |
|-----|------|-------------|
| 1.0 | 2025-11-02 | Initial standards document |
| 1.1 | 2025-11-02 | **Major update:** Added dual-feed RMU topology requirements, LV-SWBD 5-position layout, transformer connection orientation rules, text clearance/overlap prevention, symmetrical spacing calculations |

---

**End of Standards Document**

These standards ensure professional, readable, and accurate single-line diagrams that meet electrical engineering documentation requirements.
