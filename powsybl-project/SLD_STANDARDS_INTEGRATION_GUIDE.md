# SLD Standards Integration Guide

**Date:** 2025-11-05
**Version:** 1.1
**Status:** ✅ Active

---

## Overview

The SLD (Single-Line Diagram) generation standards are now available through **two complementary approaches**:

1. **Python Module** (`sld_standards.py`) - For programmatic use in generator scripts
2. **Claude Command** (`.claude/commands/sld-generate.md`) - For AI-assisted generation

This dual approach provides:
- **Single source of truth** - Python module is canonical
- **Easy updates** - Change once, applies everywhere
- **AI awareness** - Claude automatically references the command
- **Code reusability** - Import functions instead of redefining

---

## Approach 1: Python Module (`sld_standards.py`)

### Purpose
Provides reusable Python functions and constants for SLD generation scripts.

### Key Components

#### 1. Style Generation
```python
from sld_standards import get_svg_style_section

svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="2800" height="3400" xmlns="http://www.w3.org/2000/svg">

{get_svg_style_section()}

<!-- Your SLD content -->

</svg>'''
```

**Returns:**
- Open Sans font hierarchy (24px title / 14px equipment / 11px ratings)
- Material Design color palette (light backgrounds)
- IEEE 315/IEC 60617 compliant line styles
- Equipment box styles

#### 2. IEEE Symbols
```python
from sld_standards import get_svg_symbols

svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="2800" height="3400" xmlns="http://www.w3.org/2000/svg">

{get_svg_symbols()}

<!-- Use symbols -->
<use href="#breaker-closed" x="500" y="300"/>
<use href="#transformer" x="600" y="500"/>
<use href="#generator" x="700" y="200"/>

</svg>'''
```

**Provides:**
- `#breaker-closed` - Closed breaker (X pattern)
- `#breaker-open` - Open breaker (gap + circle)
- `#transformer` - Dual-winding transformer
- `#generator` - Generator symbol (circle with G)
- `#connection-point` - Connection dot
- `#fuse` - Fuse symbol
- `#disconnect-closed` / `#disconnect-open` - Disconnect switches

#### 3. Symmetrical Positioning
```python
from sld_standards import calculate_symmetric_positions

# Position 4 transformers on 2800px canvas
tx_positions = calculate_symmetric_positions(
    canvas_width=2800,
    equipment_count=4,
    equipment_width=80,
    margin=200
)
# Returns: [656.0, 1152.0, 1648.0, 2144.0] - evenly spaced centers
```

**Algorithm:**
```
usable_width = canvas_width - (2 × margin)
total_equipment_width = equipment_count × equipment_width
available_space = usable_width - total_equipment_width
spacing = available_space / (equipment_count + 1)

For each equipment i:
    x = margin + spacing × (i + 1) + equipment_width × i + (equipment_width / 2)
```

#### 4. Constants and Dictionaries
```python
from sld_standards import TEXT_STYLES, EQUIPMENT_STYLES, LAYOUT, SYMBOLS

# Text styling
title_font = TEXT_STYLES['title']['font-family']  # "Open Sans", Arial
title_size = TEXT_STYLES['title']['font-size']    # 24

# Equipment colors
mv_color = EQUIPMENT_STYLES['switchgear']['fill']  # #F5F5F5

# Layout rules
flow = LAYOUT['flow_direction']  # 'top_to_bottom'
spacing = LAYOUT['minimum_spacing']  # 50
```

### Complete Example
```python
#!/usr/bin/env python3
"""
Project SLD Generator - Standards v1.1 Compliant
"""

from datetime import datetime
from sld_standards import (
    get_svg_style_section,
    get_svg_symbols,
    calculate_symmetric_positions
)

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

<!-- Title Block -->
<text x="{WIDTH/2}" y="75" class="title" text-anchor="middle">Project Name - SLD</text>

<!-- MV Switchboard -->
<rect x="{mv_positions[0]-160}" y="200" width="320" height="140" class="mv-switchboard"/>
<text x="{mv_positions[0]}" y="260" class="equipment-label" text-anchor="middle">MV-SWBD-A</text>
<text x="{mv_positions[0]}" y="280" class="rating" text-anchor="middle">10 kV | 630A</text>

<!-- Transformer -->
<use href="#transformer" x="{tx_positions[0]}" y="500"/>
<text x="{tx_positions[0]}" y="570" class="equipment-label" text-anchor="middle">XFMR-1</text>
<text x="{tx_positions[0]}" y="590" class="rating" text-anchor="middle">5,000 kVA</text>

<!-- Power line with breaker -->
<line x1="{mv_positions[0]}" y1="340" x2="{mv_positions[0]}" y2="450" class="power-line"/>
<use href="#breaker-closed" x="{mv_positions[0]}" y="395"/>
<text x="{mv_positions[0]+20}" y="400" class="rating">CB-1 (N.C.)</text>

</svg>'''

# Save
with open('output_sld.svg', 'w', encoding='utf-8') as f:
    f.write(svg)

print(f"[SUCCESS] SLD generated: output_sld.svg ({len(svg):,} bytes)")
```

---

## Approach 2: Claude Command (`/sld-generate`)

### Purpose
Provides comprehensive instructions to Claude Code when generating SLDs.

### Usage

When working with Claude Code, simply type:
```
/sld-generate
```

This loads the complete standards document into Claude's context, ensuring:
- ✅ Open Sans font hierarchy applied
- ✅ Symmetrical spacing calculations used
- ✅ Text clearance rules followed
- ✅ IEEE 315/IEC 60617 symbols used
- ✅ Equipment-only labels (no annotations)
- ✅ Breaker normal positions shown
- ✅ Direct transformer connections
- ✅ Proper power flow (top-to-bottom)

### What It Contains

The command file includes:
1. **Mandatory standards compliance checklist**
2. **Font hierarchy specifications**
3. **Symmetrical spacing algorithm**
4. **Text clearance rules** (15px from lines, 10px from equipment)
5. **Equipment representation standards** (LV-SWBD, RMU, Transformers)
6. **Breaker normal position requirements**
7. **Color palette definitions**
8. **Power flow direction rules**
9. **Pre-generation checklist**
10. **Post-generation validation steps**
11. **Complete example generator template**

### When to Use

Use `/sld-generate` whenever:
- Starting a new SLD generator script
- Unsure about standards compliance
- Need to verify existing generator follows standards
- Want Claude to check your SLD for issues

---

## Standards Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2025-11-02 | Initial standards (Arial fonts, IEEE symbols, basic layout) |
| 1.1 | 2025-11-02 | Added RMU dual-feed topology, LV-SWBD 5-position layout, transformer orientation, text clearance, symmetrical spacing |
| 1.1.1 | 2025-11-05 | **Updated to Open Sans fonts**, added Python module integration, created Claude command |

---

## Current Standards (v1.1.1)

### Font Hierarchy - Open Sans
```
Heading 1 (Titles):         bold 24px "Open Sans", Arial
Heading 2 (Equipment):      bold 14px "Open Sans", Arial
Heading 3 (Specifications): 11px "Open Sans", Arial
```

### Color Palette - Material Design Light
```css
MV Switchboards:    #E3F2FD  (Light Blue)
LV Switchboards:    #E8F5E9  (Light Green)
Generators:         #FFF3E0  (Light Orange)
Transformers:       #FFFFFF  (White)
RMUs:               #FFF9C4  (Light Yellow)
UPS Modules:        #F3E5F5  (Light Purple)
Distribution:       #E0F2F1  (Light Teal)
```

### Line Styles - IEEE 315
```
Power Lines:        2px black
Main Bus:           6px black
Ring Bus:           4px (Ring A: #E74C3C red, Ring B: #3498DB blue)
Control Circuits:   1px black dashed (5,5)
```

### Spacing Rules
```
Minimum Margins:            200px from canvas edge
Equipment Horizontal:       CALCULATED (equal distribution)
Equipment Vertical:         250px between voltage levels
Text from Power Lines:      15px minimum
Text from Equipment:        10px minimum
Breaker Label Offset:       15-20px to side
```

### Equipment Standards

**LV Switchboards:**
- Width: 200px minimum (5 breaker positions)
- Height: 100px minimum
- Main bus: Horizontal at top (15px from edge)
- Incomer: From TOP
- Outgoing: ALL from BOTTOM

**RMUs (Ring Main Units):**
- TWO incomers at TOP (primary + reserve)
- ONE outgoer at BOTTOM (to transformer)
- Internal horizontal bus
- Clear PRI/RES labeling

**Transformers:**
- Incomer: From TOP
- Outgoer: From BOTTOM
- Vertical symmetry
- Direct connection to LV-SWBD

**Breakers:**
- All show normal position: (N.C.) or (N.O.)
- Labels offset 15-20px to side (never on symbol)
- IEEE 315 symbols (closed: X pattern, open: gap + circle)

---

## File Locations

```
powsybl-project/
├── sld_standards.py                          # Python module (canonical source)
├── SLD_GENERATION_STANDARDS.md               # Comprehensive reference (875 lines)
├── SLD_STANDARDS_UPDATE_SUMMARY.md           # v1.1 update notes
├── SLD_STANDARDS_INTEGRATION_GUIDE.md        # This file
├── .claude/
│   └── commands/
│       └── sld-generate.md                   # Claude command
└── test_sld_standards_integration.py         # Module validation test
```

---

## Testing

To verify the Python module works correctly:

```bash
cd powsybl-project
python test_sld_standards_integration.py
```

Expected output:
```
================================================================================
SLD STANDARDS MODULE INTEGRATION TEST
================================================================================

[TEST 1] Generating CSS styles...
✓ CSS styles generated with Open Sans fonts

[TEST 2] Generating IEEE symbols...
✓ IEEE Std 315 symbols generated

[TEST 3] Testing symmetrical position calculation...
✓ Symmetric positions: [656.0, 1152.0, 1648.0, 2144.0]
  Spacing: 496.0px (equal across all)

[TEST 4] Checking TEXT_STYLES dictionary...
✓ TEXT_STYLES dictionary correct (Open Sans, 3-tier hierarchy)

[TEST 5] Checking EQUIPMENT_STYLES dictionary...
✓ EQUIPMENT_STYLES dictionary available

[TEST 6] Checking LAYOUT constants...
✓ LAYOUT constants available

[TEST 7] Generating complete minimal SVG...
✓ Complete SVG generated successfully
  Output: test_standards_output.svg (4,775 bytes)

================================================================================
ALL TESTS PASSED ✓
================================================================================
```

---

## Migration Guide

### Updating Existing Generators

To update an existing SLD generator to use the standards module:

**Before:**
```python
# Manual definitions
FONTS = {
    'heading1': 'font: bold 24px "Open Sans", Arial',
    'heading2': 'font: bold 14px "Open Sans", Arial',
    'heading3': 'font: 11px "Open Sans", Arial',
}

def get_standards_css():
    return '''
    <style>
        .title { font: bold 24px "Open Sans", Arial; fill: #000; }
        .equipment-label { font: bold 14px "Open Sans", Arial; fill: #000; }
        .rating { font: 11px "Open Sans", Arial; fill: #333; }
        ...
    </style>
    '''

def get_ieee_symbols():
    return '''
    <defs>
        <g id="breaker-closed">
            ...
        </g>
    </defs>
    '''

def calculate_symmetric_positions(canvas_width, equipment_count, equipment_width, margin):
    # Manual implementation
    ...
```

**After:**
```python
# Import from module
from sld_standards import (
    get_svg_style_section,
    get_svg_symbols,
    calculate_symmetric_positions
)

# Use directly
svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{WIDTH}" height="{HEIGHT}" xmlns="http://www.w3.org/2000/svg">

{get_svg_symbols()}
{get_svg_style_section()}

<!-- Your SLD content -->

</svg>'''
```

**Benefits:**
- 🔧 Reduced code duplication
- ✅ Automatic standards compliance
- 🔄 Easy updates (change module, all generators update)
- 📦 Smaller script files

---

## Best Practices

### When Writing New Generators

1. **Always import the standards module first**
   ```python
   from sld_standards import (
       get_svg_style_section,
       get_svg_symbols,
       calculate_symmetric_positions
   )
   ```

2. **Use `/sld-generate` command with Claude**
   - Type `/sld-generate` at start of generation task
   - Claude will reference all standards automatically

3. **Calculate spacing, don't hardcode**
   ```python
   # GOOD
   positions = calculate_symmetric_positions(WIDTH, 4, 80, MARGIN)

   # BAD
   positions = [500, 1000, 1500, 2000]  # Manual spacing
   ```

4. **Validate after generation**
   - Open SVG visually
   - Check text doesn't overlap lines/equipment
   - Verify breakers show (N.C.) or (N.O.)
   - Confirm symmetrical spacing

### When Updating Standards

1. **Edit `sld_standards.py` first** (single source of truth)
2. **Update `.claude/commands/sld-generate.md`** to match
3. **Update `SLD_GENERATION_STANDARDS.md`** documentation
4. **Run test:** `python test_sld_standards_integration.py`
5. **Update version history** in all documents

---

## FAQ

**Q: Which approach should I use - Python module or Claude command?**
A: Use **both**! Import the Python module in your scripts, and use `/sld-generate` when working with Claude.

**Q: Can I still customize my SLD beyond the standards?**
A: Yes! The standards provide the base (fonts, colors, symbols, spacing). You add project-specific equipment and topology.

**Q: What if I need a different font size?**
A: The 3-tier hierarchy (24px/14px/11px) is standard. If you need variation, use the existing tiers for different purposes rather than adding new sizes.

**Q: How do I add a new equipment type?**
A: Add the color definition to `EQUIPMENT_STYLES` in `sld_standards.py`, then use that class in your SVG. Update the command file documentation.

**Q: Can I use Arial instead of Open Sans?**
A: Open Sans is the standard (v1.1.1+). Arial is the fallback. If Open Sans isn't available, Arial will be used automatically.

**Q: What if symmetrical spacing doesn't look good for my layout?**
A: The algorithm works for most cases. If truly necessary, you can override for specific equipment, but document why in code comments.

---

## Summary

✅ **Two complementary approaches:**
- Python module (`sld_standards.py`) for code reusability
- Claude command (`/sld-generate`) for AI-assisted generation

✅ **Single source of truth:**
- Update `sld_standards.py` → all generators inherit changes

✅ **Standards compliance guaranteed:**
- Import functions instead of redefining
- Claude automatically references command

✅ **Version 1.1.1 features:**
- Open Sans font hierarchy (24px/14px/11px)
- Material Design light color palette
- IEEE 315/IEC 60617 symbols
- Symmetrical spacing algorithm
- Text clearance rules (15px from lines)
- Equipment representation standards

---

**Document Version:** 1.0
**Standards Version:** SLD Standards v1.1.1
**Last Updated:** 2025-11-05
**Compliance:** IEEE Std 315 / IEC 60617 + Open Sans Typography
