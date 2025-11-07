# SLD Generation Standards v1.2 - CRITICAL FIXES

**Document Version:** 1.2
**Date:** 2025-11-06
**Purpose:** Critical corrections to prevent common SLD generation errors
**Status:** MANDATORY - All new SLDs must follow these rules

---

## 0. CRITICAL RULES (MANDATORY - MUST NOT VIOLATE)

### 0.1 **NO ELECTRICAL PATHS THROUGH EQUIPMENT**

**RULE:** Electrical power lines SHALL NOT pass through any equipment graphic boundaries.

**Problem:** Lines passing through equipment make diagrams confusing and unprofessional.

**Solution:**
```python
# BAD - Line passes through equipment box
<line x1="100" y1="200" x2="300" y2="400"/>  # Goes through equipment at (200,300)
<rect x="150" y="250" width="100" height="100"/>  # Equipment overlaps line

# GOOD - Line routes around equipment
<line x1="100" y1="200" x2="100" y2="350"/>   # Down to equipment level
<line x1="100" y1="350" x2="250" y2="350"/>   # Horizontal around equipment
<line x1="250" y1="350" x2="250" y2="400"/>   # Connect to next point
<rect x="150" y="250" width="100" height="100"/>  # Equipment clear of lines
```

**Implementation Rules:**
1. Calculate equipment boundaries: `x_min`, `x_max`, `y_min`, `y_max`
2. Lines must terminate at equipment edges, not pass through center
3. Use L-shaped or Z-shaped routing around equipment
4. Add 10px clearance buffer from equipment edges

**Example (DRUPS Connection):**
```python
# Connect LV switchboard to DRUPS (routed around)
# Exit from side of switchboard
line1: (swbd_x + swbd_width/2, swbd_y + swbd_height) → (swbd_x - 200, swbd_y + swbd_height)
# Down vertically in clear space
line2: (swbd_x - 200, swbd_y + swbd_height) → (swbd_x - 200, drups_y)
# Horizontal to DRUPS edge (stops at boundary)
line3: (swbd_x - 200, drups_y) → (drups_x - drups_width/2, drups_y)
```

### 0.2 **NO TEXT OVERLAPPING EQUIPMENT OR LINES**

**RULE:** Text SHALL NOT overlap or intersect with equipment boundaries or electrical paths.

**Problem:** Overlapping text is unreadable and unprofessional.

**Solution:**
```python
# BAD - Text overlaps equipment or line
<rect x="100" y="100" width="200" height="100"/>
<text x="150" y="150">EQUIPMENT</text>  # Overlaps rectangle
<line x1="100" y1="200" x2="300" y2="200"/>
<text x="200" y="200">LABEL</text>  # Overlaps line

# GOOD - Text placed with clearance
<rect x="100" y="100" width="200" height="100"/>
<text x="200" y="85">EQUIPMENT</text>  # 15px above equipment (100 - 15)
<line x1="100" y1="220" x2="300" y2="220"/>
<text x="200" y="235">LABEL</text>  # 15px below line (220 + 15)
```

**Clearance Requirements:**
- **From equipment boundaries:** 10px minimum
- **From power lines:** 15px minimum
- **From breaker symbols:** 15-20px offset to side
- **Text-to-text:** 5px minimum vertical spacing

**Text Placement Priority:**
1. **Above equipment:** Label above, ratings below
2. **To the side:** If vertical space constrained, place label to left/right with 10px clearance
3. **Never overlap:** If text doesn't fit, use smaller font or abbreviations

**Example (Breaker Labels):**
```python
# Breaker at (500, 300)
breaker_symbol: (500, 300)  # 16px wide, 24px tall

# ID text: Above breaker
text_id: (500, 280)  # 20px above center (300 - 20)

# State text: Below breaker
text_state: (500, 315)  # 15px below center (300 + 15)

# Rating text: To the side
text_rating: (535, 305)  # 35px to right (500 + 35)
```

### 0.3 **BREAKER TEXT FORMATTING (Centered, Below, Red for N.C.)**

**RULE:** All breakers must show:
1. **Breaker ID:** Centered above breaker symbol
2. **Breaker State:** Centered below breaker symbol
3. **N.C. (Normally Closed) in RED color** (#D32F2F)
4. **N.O. (Normally Open) in default color** (#333)

**Problem:** Inconsistent breaker labeling causes confusion about normal operating states.

**Solution:**
```python
# Define breaker text styles
.breaker-id { font: 11px "Open Sans", Arial; fill: #000; }
.breaker-nc { font: 11px "Open Sans", Arial; fill: #D32F2F; font-weight: bold; }  # RED
.breaker-no { font: 11px "Open Sans", Arial; fill: #333; }  # Dark gray

# Breaker symbol at (x, y) - symbol is 16px wide × 24px tall
<use href="#breaker-closed" x="{x}" y="{y}"/>

# ID text: 20px above center, centered
<text x="{x}" y="{y - 20}" class="breaker-id" text-anchor="middle">CB-M1</text>

# State text: 15px below center, centered
<text x="{x}" y="{y + 15}" class="breaker-nc" text-anchor="middle">N.C.</text>  # RED for closed

# OR for normally open breaker
<text x="{x}" y="{y + 15}" class="breaker-no" text-anchor="middle">N.O.</text>  # Gray for open
```

**Visual Layout:**
```
      CB-M1          ← Breaker ID (black, 11px, centered above)
        ┌─┐
        │X│          ← Breaker symbol (closed)
        └─┘
       N.C.          ← Breaker state (RED, 11px, centered below)
```

**Color Coding Rationale:**
- **RED (N.C.):** Indicates energized/active circuit - critical for safety
- **Gray (N.O.):** Indicates de-energized/standby circuit
- **Bold font:** Makes critical N.C. breakers stand out

### 0.4 **ALL REQUIRED BREAKERS MUST BE SHOWN**

**RULE:** Every equipment connection requiring overcurrent protection SHALL display a breaker symbol.

**Problem:** Missing breakers create incomplete diagrams that don't match actual installations.

**Required Breaker Locations:**
1. **Utility Service Entrance:** CB-U1, CB-U2 (one per utility feed)
2. **Generator Connections:** CB-G1, CB-G2, etc. (one per generator)
3. **MV Switchboard Feeders:** CB-M1, CB-M2, etc. (transformer feeders)
4. **LV Main Breakers:** ACB-M1, ACB-M2 (main incoming breakers)
5. **Tie Breakers:** 52-TIE (between buses)
6. **DRUPS/UPS Breakers:** ACB-DRUPS1, ACB-UPS1, etc. (one per unit)
7. **Distribution Feeders:** Panel main breakers (MCCB ratings)

**Breaker Placement Rules:**
1. **Near equipment:** Breakers placed on line nearest to protected equipment
2. **Visible labels:** ID and state clearly shown
3. **Logical grouping:** Related breakers visually grouped (e.g., all MV breakers near MV-SWBD)

**Example (Complete Breaker Set):**
```python
# Utility entrance
CB-U1 (N.C.) - HPP utility feed
CB-U2 (N.C.) - Grid utility feed

# MV switchboard feeders
CB-M1 (N.C.) - MV-SWBD-A to XFMR-A
CB-M2 (N.C.) - MV-SWBD-B to XFMR-B

# LV main breakers
ACB-M1 (N.C.) - XFMR-A to SWBD-A
ACB-M2 (N.C.) - XFMR-B to SWBD-B

# Tie breaker
52-TIE (N.O.) - Between SWBD-A and SWBD-B

# DRUPS breakers
ACB-DRUPS1 (N.C.) - DRUPS-1 to SWBD-A
ACB-DRUPS2 (N.C.) - DRUPS-2 to SWBD-B

# Distribution panel main breakers (shown as MCCB in panel box)
A-IT-1: 2,500A MCCB
B-IT-1: 2,500A MCCB
A-COOL-1: 3,200A MCCB
B-COOL-1: 3,200A MCCB
```

---

## 1. LAYOUT RULES (Preventing Overlaps)

### 1.1 Vertical Spacing

**Minimum vertical spacing between equipment levels:**
```
Y_UTILITY = 300        # Top level
Y_STEP_UP = 580        # +280px from utility
Y_MV_SWBD = 880        # +300px from step-up
Y_XFMR = 1220          # +340px from MV switchboards
Y_LV_SWBD = 1600       # +380px from transformers
Y_DRUPS = 2000         # +400px from LV switchboards
Y_DIST = 2450          # +450px from DRUPS
Y_IT_LOADS = 2850      # +400px from distribution

TOTAL_HEIGHT = 3600    # Increased from 3400 for better spacing
```

**Rationale:** Increased spacing prevents line/text overlaps when routing around equipment.

### 1.2 Horizontal Equipment Spacing

**Use symmetrical spacing algorithm:**
```python
def calculate_symmetric_positions(canvas_width, equipment_count, equipment_width, margin):
    usable_width = canvas_width - (2 * margin)
    total_equipment_width = equipment_count * equipment_width
    available_space = usable_width - total_equipment_width
    spacing = available_space / (equipment_count + 1)

    positions = []
    for i in range(equipment_count):
        x = margin + spacing * (i + 1) + equipment_width * i + (equipment_width / 2)
        positions.append(x)

    return positions
```

**Minimum margins:**
- Left/right canvas margins: 200px
- Equipment-to-equipment: Calculated by algorithm (typically 400-600px)

### 1.3 Line Routing Strategy

**L-Shaped Routing (2 segments):**
```
Equipment A → (vertical) → (horizontal) → Equipment B
```

**Z-Shaped Routing (3 segments):**
```
Equipment A → (horizontal to clear space) → (vertical) → (horizontal) → Equipment B
```

**Rules:**
1. Exit equipment from nearest edge (top/bottom/left/right)
2. Route in clear space (no equipment zones)
3. Use right angles (90° bends)
4. Minimize line crossings

---

## 2. EQUIPMENT REPRESENTATION RULES

### 2.1 Equipment Boundaries

**All equipment must define clear boundaries:**
```python
# Rectangle equipment
x_min = center_x - width/2
x_max = center_x + width/2
y_min = center_y - height/2
y_max = center_y + height/2

# Connection points on edges (not through center)
top_connection = (center_x, y_min)
bottom_connection = (center_x, y_max)
left_connection = (x_min, center_y)
right_connection = (x_max, center_y)
```

### 2.2 Equipment Sizing Standards

```
Utility Sources:    200px × 100px
MV Switchboards:    320px × 140px
Transformers:       80px × 80px (symbol)
LV Switchboards:    240px × 120px
DRUPS/Generators:   180px × 100px
Distribution Panels: 100px × 80px
IT Equipment Box:   300px × 80px
```

### 2.3 Equipment Label Placement

**Standard positions (relative to equipment):**
```
Equipment Label:     Center, Y = y_center - 10
Rating Line 1:       Center, Y = y_center + 10
Rating Line 2:       Center, Y = y_center + 25
Additional Info:     Center, Y = y_center + 40
```

**Text must not overlap equipment boundary:**
- If equipment height < 80px, place labels above/below equipment
- If equipment width < 120px, place labels to side

---

## 3. BREAKER SYMBOL STANDARDS

### 3.1 Breaker Dimensions

```
Breaker (Closed):    16px wide × 24px tall
Breaker (Open):      16px wide × 24px tall
Symbol center:       (x, y) where x,y is provided to <use> tag
```

### 3.2 Breaker Label Positions

**Fixed positions relative to breaker center (x, y):**
```python
# Breaker ID: 20px above center
id_position = (x, y - 20)

# Breaker State: 15px below center
state_position = (x, y + 15)

# Breaker Rating (if shown): 35px to right
rating_position = (x + 35, y + 5)
```

**Text anchoring:**
```xml
<text x="{x}" y="{y-20}" text-anchor="middle" class="breaker-id">CB-M1</text>
<text x="{x}" y="{y+15}" text-anchor="middle" class="breaker-nc">N.C.</text>
<text x="{x+35}" y="{y+5}" text-anchor="start" class="rating">6,300A/5,000A</text>
```

---

## 4. CSS STYLES (Updated for v1.2)

```css
/* Text Styles - SLD Standards v1.2 */
.title { font: bold 24px "Open Sans", Arial; fill: #000; }
.subtitle { font: bold 14px "Open Sans", Arial; fill: #000; }
.equipment-label { font: bold 14px "Open Sans", Arial; fill: #000; }
.bus-label { font: bold 12px "Open Sans", Arial; fill: #000; }
.small-label { font: 11px "Open Sans", Arial; fill: #000; }
.rating { font: 11px "Open Sans", Arial; fill: #333; }
.annotation { font: 11px "Open Sans", Arial; fill: #000; }
.feeder-label { font: 10px "Open Sans", Arial; fill: #666; }
.note { font: italic 11px "Open Sans", Arial; fill: #000; }

/* Breaker Text Styles - v1.2 NEW */
.breaker-id { font: 11px "Open Sans", Arial; fill: #000; }
.breaker-nc { font: 11px "Open Sans", Arial; fill: #D32F2F; font-weight: bold; }  /* RED */
.breaker-no { font: 11px "Open Sans", Arial; fill: #333; }  /* Dark gray */

/* Line Styles */
.power-line { stroke: #000; stroke-width: 2; fill: none; }
.bus { stroke: #000; stroke-width: 6; fill: none; }
.main-bus { stroke: #000; stroke-width: 6; fill: none; }
.control-line { stroke: #000; stroke-width: 1; stroke-dasharray: 5,5; fill: none; }

/* Equipment Boxes - LIGHT BACKGROUNDS */
.mv-switchboard { fill: #E3F2FD; stroke: #000; stroke-width: 2; }
.lv-switchboard { fill: #E8F5E9; stroke: #000; stroke-width: 2; }
.generator-box { fill: #FFF3E0; stroke: #000; stroke-width: 2; }
.transformer-box { fill: #FFFFFF; stroke: #000; stroke-width: 2; }
.rmu-box { fill: #FFF9C4; stroke: #000; stroke-width: 2; }
.ups-module { fill: #F3E5F5; stroke: #000; stroke-width: 1.5; }
.dist-panel { fill: #E0F2F1; stroke: #000; stroke-width: 1; }
```

---

## 5. PRE-GENERATION CHECKLIST (v1.2)

Before generating SVG, verify:
- [x] Imported `sld_standards.py` module
- [x] Using `get_svg_style_section()` for CSS
- [x] Using `get_svg_symbols()` for IEEE symbols
- [x] Open Sans fonts applied (3-tier hierarchy)
- [x] Symmetrical spacing calculated (not manual)
- [x] **NO lines route through equipment graphics**
- [x] **NO text overlaps with equipment or lines**
- [x] **Breaker IDs centered above, states centered below**
- [x] **N.C. breaker text is RED (#D32F2F)**
- [x] **All required breakers shown in appropriate locations**
- [x] All breakers show normal positions (N.C./N.O.)
- [x] Power flow is top-to-bottom
- [x] Equipment-only labels (no annotations)
- [x] Direct transformer-to-LV-SWBD connections

---

## 6. POST-GENERATION VALIDATION (v1.2)

After generating SVG:
- [ ] Open the file visually to check
- [ ] **Verify NO lines pass through equipment boxes**
- [ ] **Verify NO text overlaps lines or equipment**
- [ ] **Verify breaker states: N.C. is RED and centered below ID**
- [ ] Verify symmetrical spacing (visual check)
- [ ] Verify all breakers visible with labels
- [ ] Verify font hierarchy consistent
- [ ] Verify color palette matches standards
- [ ] Check for line crossings (minimize)
- [ ] Verify connection points terminate at equipment edges

---

## 7. COMMON ERRORS TO AVOID

### Error 1: Lines Through Equipment
**Problem:** `<line x1="100" y1="200" x2="300" y2="400"/>` passes through equipment at (200, 300)
**Fix:** Route around equipment using L-shaped or Z-shaped paths

### Error 2: Text Overlapping Equipment
**Problem:** Text placed at equipment center overlaps equipment boundary
**Fix:** Place text above (y - 15px) or below (y + height + 15px) equipment

### Error 3: Text Overlapping Lines
**Problem:** Label placed directly on power line
**Fix:** Offset label 15px perpendicular to line direction

### Error 4: Breaker State Not RED
**Problem:** Using `.rating` class for N.C. text (appears gray)
**Fix:** Use `.breaker-nc` class for N.C. text (appears red)

### Error 5: Breaker State Left/Right of Symbol
**Problem:** State text placed beside breaker instead of below
**Fix:** Center state text 15px below breaker center

### Error 6: Missing Breakers
**Problem:** Connections shown without breakers (unrealistic)
**Fix:** Add breaker symbols on all protective device locations

---

## 8. VERSION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-11-02 | Initial standards (Arial fonts, IEEE symbols, basic layout) |
| 1.1 | 2025-11-02 | Added RMU topology, LV-SWBD layout, text clearance, symmetrical spacing |
| 1.1.1 | 2025-11-05 | Updated to Open Sans fonts, added Python module integration |
| **1.2** | **2025-11-06** | **CRITICAL FIXES: No lines through equipment, no text overlaps, breaker text formatting (RED for N.C., centered below), all breakers shown** |

---

## 9. MANDATORY COMPLIANCE

**All SLDs generated after 2025-11-06 MUST comply with v1.2 standards.**

**Non-compliance indicators:**
- ❌ Lines passing through equipment
- ❌ Text overlapping equipment or lines
- ❌ Breaker states not centered below breaker ID
- ❌ N.C. breaker text not RED
- ❌ Missing breakers at connection points

**To report standards violations or suggest improvements:**
- Document issue with screenshot
- Reference section number
- Propose specific fix with code example

---

**Document Status:** ACTIVE - MANDATORY COMPLIANCE
**Compliance:** IEEE Std 315 / IEC 60617 + Critical Layout Fixes
**Last Updated:** 2025-11-06
