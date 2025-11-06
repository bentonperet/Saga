# SLD Generation Command

When the user requests generation of a Single-Line Diagram (SLD), follow these steps:

## 1. Standards Compliance - MANDATORY

You MUST use the established SLD standards:

**Primary Standards Documents:**
- `SLD_GENERATION_STANDARDS.md` - Complete 875-line reference document
- `sld_standards.py` - Python module with reusable components

**Python Module Usage:**
```python
from sld_standards import (
    get_svg_style_section,
    get_svg_symbols,
    TEXT_STYLES,
    EQUIPMENT_STYLES,
    LAYOUT,
    SYMBOLS
)
```

## 2. Font Hierarchy (CRITICAL)

**Open Sans font family with 3-tier hierarchy:**
```python
FONTS = {
    'heading1': 'font: bold 24px "Open Sans", Arial',  # Titles
    'heading2': 'font: bold 14px "Open Sans", Arial',  # Equipment names
    'heading3': 'font: 11px "Open Sans", Arial',       # Specifications
}
```

**Application:**
- Heading 1: SLD title, project name
- Heading 2: All equipment names (MV-SWBD-A, XFMR-1, MTU-1, etc.)
- Heading 3: All ratings and specifications (400V, 5,000 kVA, etc.)

## 3. Symmetrical Spacing (MANDATORY)

**All equipment must be symmetrically distributed using calculation:**
```python
def calculate_symmetric_positions(canvas_width, equipment_count, equipment_width, margin):
    """Calculate symmetrically spaced positions per SLD Standards v1.1 Section 2.2"""
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

**NEVER use manual spacing** - always calculate!

## 4. Text Clearance (CRITICAL)

**Text MUST NOT overlap:**
- Cable pathways: 15px minimum clearance
- Equipment boundaries: 10px minimum clearance
- Breaker symbols: Offset 15-20px to side
- Other text: 15px minimum clearance

**Breaker Label Pattern:**
```svg
<use href="#breaker-closed" x="500" y="300"/>
<text x="520" y="305" class="rating">CB-1 (N.C.)</text>
<!-- 20px offset right, 5px down for alignment -->
```

## 5. Equipment Standards

### LV Switchboards:
- Width: 200px minimum (5 breaker positions)
- Incomer: From TOP (from transformer)
- Outgoing: ALL from BOTTOM
- Main bus: Horizontal at top (15px from edge)

### RMUs (Ring Main Units):
- TWO incomers at TOP (primary + reserve)
- ONE outgoer at BOTTOM (to transformer)
- Internal bus connecting both incomers
- Clear labeling: PRI / RES

### Transformers:
- Incomer: From TOP
- Outgoer: From BOTTOM
- Vertical symmetry (never diagonal)
- Connect directly to LV-SWBD (not through other equipment)

## 6. Breaker Normal Positions

**All breakers must show normal operating state:**
- Normally closed: `(N.C.)`
- Normally open: `(N.O.)`

Examples:
- `CB-U1 (N.C.)` - Utility incomer
- `52-TIE (N.O.)` - Tie breaker
- `CB-M1 (N.C.)` - MTU breaker

## 7. Color Palette (SLD Standards v1.1)

**Light backgrounds for readability:**
```css
.mv-switchboard { fill: #E3F2FD; }    /* Light Blue */
.lv-switchboard { fill: #E8F5E9; }    /* Light Green */
.generator-box { fill: #FFF3E0; }     /* Light Orange */
.transformer-box { fill: #FFFFFF; }   /* White */
.ups-module { fill: #F3E5F5; }        /* Light Purple */
.dist-panel { fill: #E0F2F1; }        /* Light Teal */
```

## 8. Power Flow Direction

**Always TOP to BOTTOM:**
```
SOURCES (Utility/HPP/Solar)
    ↓
MV SWITCHBOARDS
    ↓
TRANSFORMERS
    ↓
LV SWITCHBOARDS
    ↓
UPS/DRUPS
    ↓
DISTRIBUTION
    ↓
IT LOADS
```

## 9. Equipment Labels Only

**Remove all annotation labels that don't define equipment:**
- ✓ Keep: Equipment names, ratings, specifications
- ✗ Remove: "PRIMARY SOURCES", "TIER III", "DOWNSTREAM", etc.
- ✗ Remove: Descriptive boxes, callouts, section headers

## 10. IEEE/IEC Symbol Compliance

**Use symbols from `sld_standards.py`:**
- Breaker (closed): Rectangle with X pattern
- Breaker (open): Rectangle with gap and circle
- Transformer: Dual overlapping circles
- Generator: Circle with "G"
- Connection point: Solid black dot (3px radius)

## 11. Pre-Generation Checklist

Before generating SVG, verify:
- [ ] Imported `sld_standards.py` module
- [ ] Using `get_svg_style_section()` for CSS
- [ ] Using `get_svg_symbols()` for IEEE symbols
- [ ] Open Sans fonts applied (3-tier hierarchy)
- [ ] Symmetrical spacing calculated (not manual)
- [ ] Text clearance rules applied (15px from lines)
- [ ] All breakers show normal positions (N.C./N.O.)
- [ ] Power flow is top-to-bottom
- [ ] Equipment-only labels (no annotations)
- [ ] Direct transformer-to-LV-SWBD connections

## 12. Post-Generation Validation

After generating SVG:
- [ ] Open the file visually to check
- [ ] Verify no text overlaps lines or equipment
- [ ] Verify symmetrical spacing (visual check)
- [ ] Verify all breakers visible with labels
- [ ] Verify font hierarchy consistent
- [ ] Verify color palette matches standards

## Example Generator Template

```python
#!/usr/bin/env python3
"""
Project Name - Single-Line Diagram Generator
Description of topology and configuration
SLD STANDARDS v1.1 COMPLIANT
"""

from datetime import datetime
from sld_standards import (
    get_svg_style_section,
    get_svg_symbols,
    LAYOUT
)

# Open Sans Font Hierarchy
FONTS = {
    'heading1': 'font: bold 24px "Open Sans", Arial',
    'heading2': 'font: bold 14px "Open Sans", Arial',
    'heading3': 'font: 11px "Open Sans", Arial',
}

def calculate_symmetric_positions(canvas_width, equipment_count, equipment_width, margin):
    """Calculate symmetrically spaced positions per SLD Standards v1.1"""
    usable_width = canvas_width - (2 * margin)
    total_equipment_width = equipment_count * equipment_width
    available_space = usable_width - total_equipment_width
    spacing = available_space / (equipment_count + 1)

    positions = []
    for i in range(equipment_count):
        x = margin + spacing * (i + 1) + equipment_width * i + (equipment_width / 2)
        positions.append(x)

    return positions

# Canvas settings
WIDTH = 2800
HEIGHT = 3400
MARGIN = 200

# Calculate equipment positions
mv_positions = calculate_symmetric_positions(WIDTH, 2, 320, MARGIN)
tx_positions = calculate_symmetric_positions(WIDTH, 4, 80, MARGIN)
lv_positions = calculate_symmetric_positions(WIDTH, 2, 240, MARGIN)

# Build SVG
svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{WIDTH}" height="{HEIGHT}" xmlns="http://www.w3.org/2000/svg">

{get_svg_symbols()}
{get_svg_style_section()}

<!-- Your SLD content here -->

</svg>'''

# Save
with open('output.svg', 'w', encoding='utf-8') as f:
    f.write(svg)
```

## Standards Version

**Current Version:** SLD Standards v1.1
**Last Updated:** 2025-11-02
**Compliance:** IEEE Std 315 / IEC 60617

---

**IMPORTANT:** These standards are MANDATORY for all SLD generation. Non-compliance will result in unprofessional diagrams that require rework.
