# SLD Generation Quick Reference v1.2

**Standards Version:** 1.2 (2025-11-06)
**Compliance:** MANDATORY

---

## 🚨 CRITICAL RULES (DO NOT VIOLATE)

### 1. NO Lines Through Equipment
```python
# ❌ WRONG
<line x1="100" y1="200" x2="300" y2="400"/>  # Passes through equipment

# ✅ CORRECT - Route around equipment
<line x1="100" y1="200" x2="100" y2="350"/>   # Down
<line x1="100" y1="350" x2="250" y2="350"/>   # Around
<line x1="250" y1="350" x2="250" y2="400"/>   # Continue
```

### 2. NO Text Overlaps
```python
# Clearance requirements
FROM_EQUIPMENT = 10px minimum
FROM_POWER_LINE = 15px minimum

# ✅ Text above equipment
<text x="{x}" y="{y - 15}">LABEL</text>

# ✅ Text beside line
<text x="{x + 20}" y="{y}">LABEL</text>
```

### 3. Breaker Text Format
```xml
<!-- ✅ CORRECT Format -->
<use href="#breaker-closed" x="{x}" y="{y}"/>
<text x="{x}" y="{y-20}" class="breaker-id" text-anchor="middle">CB-M1</text>
<text x="{x}" y="{y+15}" class="breaker-nc" text-anchor="middle">N.C.</text>

<!-- RED for N.C., Gray for N.O., Centered below ID -->
```

### 4. All Breakers Required
```
✅ Utility entrance: CB-U1, CB-U2
✅ MV feeders: CB-M1, CB-M2
✅ LV mains: ACB-M1, ACB-M2
✅ Tie breaker: 52-TIE
✅ DRUPS/UPS: ACB-DRUPS1, ACB-DRUPS2
✅ Distribution: Panel MCCBs
```

---

## 📐 Standard Dimensions

### Equipment Sizes
```
Utility Sources:     200 × 100 px
MV Switchboards:     320 × 140 px
Transformers:         80 × 80 px
LV Switchboards:     240 × 120 px
DRUPS/Generators:    180 × 100 px
Distribution Panels: 100 × 80 px
```

### Vertical Spacing
```
Y_UTILITY   = 300
Y_STEP_UP   = 580    (+280)
Y_MV_SWBD   = 880    (+300)
Y_XFMR      = 1220   (+340)
Y_LV_SWBD   = 1600   (+380)
Y_DRUPS     = 2000   (+400)
Y_DIST      = 2450   (+450)
Y_IT_LOADS  = 2850   (+400)
HEIGHT      = 3600
```

---

## 🎨 CSS Classes (v1.2)

```css
/* Text Styles */
.title              { font: bold 24px "Open Sans", Arial; fill: #000; }
.equipment-label    { font: bold 14px "Open Sans", Arial; fill: #000; }
.rating             { font: 11px "Open Sans", Arial; fill: #333; }

/* Breaker Styles - v1.2 NEW */
.breaker-id         { font: 11px "Open Sans", Arial; fill: #000; }
.breaker-nc         { font: 11px "Open Sans", Arial; fill: #D32F2F; font-weight: bold; }  /* RED */
.breaker-no         { font: 11px "Open Sans", Arial; fill: #333; }

/* Equipment Boxes */
.mv-switchboard     { fill: #E3F2FD; stroke: #000; stroke-width: 2; }
.lv-switchboard     { fill: #E8F5E9; stroke: #000; stroke-width: 2; }
.generator-box      { fill: #FFF3E0; stroke: #000; stroke-width: 2; }
.dist-panel         { fill: #E0F2F1; stroke: #000; stroke-width: 1; }
```

---

## ⚡ Line Routing Pattern

```python
# L-Shaped Routing (2 segments)
def route_l_shape(start_x, start_y, end_x, end_y, vertical_first=True):
    if vertical_first:
        # Down then across
        path = [
            (start_x, start_y, start_x, end_y),      # Vertical
            (start_x, end_y, end_x, end_y)            # Horizontal
        ]
    else:
        # Across then down
        path = [
            (start_x, start_y, end_x, start_y),      # Horizontal
            (end_x, start_y, end_x, end_y)            # Vertical
        ]
    return path

# Z-Shaped Routing (3 segments)
def route_z_shape(start_x, start_y, end_x, end_y, clear_x):
    path = [
        (start_x, start_y, clear_x, start_y),        # Horizontal to clear space
        (clear_x, start_y, clear_x, end_y),           # Vertical in clear space
        (clear_x, end_y, end_x, end_y)                # Horizontal to destination
    ]
    return path
```

---

## ✅ Pre-Generation Checklist

```python
# Import standards
from sld_standards import (
    get_svg_style_section,
    get_svg_symbols,
    calculate_symmetric_positions
)

# Define breaker CSS
additional_style = """
    <style>
        .breaker-nc { font: 11px "Open Sans", Arial; fill: #D32F2F; font-weight: bold; }
        .breaker-no { font: 11px "Open Sans", Arial; fill: #333; }
        .breaker-id { font: 11px "Open Sans", Arial; fill: #000; }
    </style>
"""

# Calculate positions (not manual)
positions = calculate_symmetric_positions(WIDTH, count, equip_width, MARGIN)

# Plan routing around equipment
# Check text clearances
# Include all breakers
```

---

## 🔍 Post-Generation Validation

```bash
# Open SVG and check:
☐ NO lines pass through equipment boxes
☐ NO text overlaps lines or equipment
☐ Breaker IDs: Centered above symbols
☐ Breaker states: Centered below symbols
☐ N.C. text is RED and bold
☐ N.O. text is gray
☐ All required breakers present
☐ Symmetrical spacing
☐ Professional appearance
```

---

## 🚀 Quick Start Template

```python
#!/usr/bin/env python3
from datetime import datetime
from sld_standards import get_svg_style_section, get_svg_symbols, calculate_symmetric_positions

WIDTH, HEIGHT, MARGIN = 2800, 3600, 200

# Calculate positions
mv_pos = calculate_symmetric_positions(WIDTH, 2, 320, MARGIN)

# Add breaker CSS
breaker_css = """
<style>
    .breaker-nc { font: 11px "Open Sans", Arial; fill: #D32F2F; font-weight: bold; }
    .breaker-no { font: 11px "Open Sans", Arial; fill: #333; }
    .breaker-id { font: 11px "Open Sans", Arial; fill: #000; }
</style>
"""

# Build SVG
svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{WIDTH}" height="{HEIGHT}" xmlns="http://www.w3.org/2000/svg">
{get_svg_symbols()}
{get_svg_style_section()}
{breaker_css}

<!-- Equipment and connections here -->

</svg>'''

# Save
with open('output.svg', 'w', encoding='utf-8') as f:
    f.write(svg)
```

---

## 📚 Reference Documents

1. **SLD_GENERATION_STANDARDS_v1.2_CRITICAL_FIXES.md** - Complete standards
2. **generate_gge_10kv_sld_corrected.py** - Working example
3. **SLD_CORRECTIONS_SUMMARY.md** - Detailed error fixes
4. **sld_standards.py** - Python module

---

## ⚠️ Common Mistakes

| Mistake | Fix |
|---------|-----|
| Line through equipment | Route around with L-shape |
| Text on equipment | Offset 10-15px from boundary |
| Breaker state beside symbol | Center below symbol (y+15) |
| N.C. text is black | Use `.breaker-nc` class (RED) |
| Missing breakers | Add all utility, MV, LV, DRUPS breakers |

---

**Last Updated:** 2025-11-06
**Compliance:** MANDATORY for all new SLDs
