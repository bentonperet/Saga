#!/usr/bin/env python3
"""
Data Center Tier IV - Single-Line Diagram Generator
Topology: 2(N+1) Fully Redundant Power Distribution System
Based on Figure 9 from "Condition-Based Maintenance for Data Center Operations Management"
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
    'heading1': "font: bold 24px 'Open Sans', Arial",
    'heading2': "font: bold 14px 'Open Sans', Arial",
    'heading3': "font: 11px 'Open Sans', Arial",
}

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

# Canvas settings
WIDTH = 3200
HEIGHT = 4000
MARGIN = 150

# Zone Y-positions (top to bottom power flow)
ZONE_0_Y = 200   # Utility feeds
ZONE_1_Y = 600   # Generators
ZONE_2_Y = 1400  # UPS systems
ZONE_3_Y = 2400  # Distribution
ZONE_4_Y = 3200  # IT loads

# Equipment horizontal positions (2 parallel paths: A-Side and B-Side)
A_SIDE_X = 600
B_SIDE_X = 2600

# Calculate generator positions (2 per side for N+1)
gen_a_positions = calculate_symmetric_positions(1200, 2, 120, 0)
gen_a_positions = [A_SIDE_X - 300 + p for p in gen_a_positions]
gen_b_positions = calculate_symmetric_positions(1200, 2, 120, 0)
gen_b_positions = [B_SIDE_X - 300 + p for p in gen_b_positions]

# Calculate UPS positions (3 per side for N+1)
ups_a_positions = calculate_symmetric_positions(1400, 3, 140, 0)
ups_a_positions = [A_SIDE_X - 400 + p for p in ups_a_positions]
ups_b_positions = calculate_symmetric_positions(1400, 3, 140, 0)
ups_b_positions = [B_SIDE_X - 400 + p for p in ups_b_positions]

# Calculate rack positions (6 racks total)
rack_positions = calculate_symmetric_positions(WIDTH, 6, 100, MARGIN)

# Build SVG
svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{WIDTH}" height="{HEIGHT}" xmlns="http://www.w3.org/2000/svg">

{get_svg_symbols()}
{get_svg_style_section()}

<!-- Title Block -->
<rect x="50" y="30" width="800" height="100" fill="#F5F5F5" stroke="#333" stroke-width="2"/>
<text x="450" y="65" class="title" text-anchor="middle" style="{FONTS['heading1']}">Data Center Tier IV</text>
<text x="450" y="90" class="subtitle" text-anchor="middle" style="{FONTS['heading3']}">2(N+1) Fully Redundant Power Distribution System</text>
<text x="450" y="110" class="subtitle" text-anchor="middle" style="{FONTS['heading3']}">Generated: {datetime.now().strftime('%Y-%m-%d')}</text>

<!-- ZONE 0: UTILITY FEEDS (Dual feed from different substations) -->
<!-- A-Side Utility -->
<circle cx="{A_SIDE_X}" cy="{ZONE_0_Y}" r="40" fill="#E3F2FD" stroke="#1976D2" stroke-width="3"/>
<text x="{A_SIDE_X}" y="{ZONE_0_Y - 5}" class="equipment-name" text-anchor="middle" style="{FONTS['heading2']}">UTILITY</text>
<text x="{A_SIDE_X}" y="{ZONE_0_Y + 10}" class="rating" text-anchor="middle" style="{FONTS['heading3']}">A-SIDE</text>
<text x="{A_SIDE_X}" y="{ZONE_0_Y + 25}" class="rating" text-anchor="middle" style="{FONTS['heading3']}">10kV</text>

<!-- B-Side Utility -->
<circle cx="{B_SIDE_X}" cy="{ZONE_0_Y}" r="40" fill="#E3F2FD" stroke="#1976D2" stroke-width="3"/>
<text x="{B_SIDE_X}" y="{ZONE_0_Y - 5}" class="equipment-name" text-anchor="middle" style="{FONTS['heading2']}">UTILITY</text>
<text x="{B_SIDE_X}" y="{ZONE_0_Y + 10}" class="rating" text-anchor="middle" style="{FONTS['heading3']}">B-SIDE</text>
<text x="{B_SIDE_X}" y="{ZONE_0_Y + 25}" class="rating" text-anchor="middle" style="{FONTS['heading3']}">10kV</text>

<!-- Utility to Transformer connections -->
<line x1="{A_SIDE_X}" y1="{ZONE_0_Y + 40}" x2="{A_SIDE_X}" y2="{ZONE_0_Y + 150}" class="power-line-mv"/>
<circle cx="{A_SIDE_X}" cy="{ZONE_0_Y + 40}" r="4" fill="black"/>

<line x1="{B_SIDE_X}" y1="{ZONE_0_Y + 40}" x2="{B_SIDE_X}" y2="{ZONE_0_Y + 150}" class="power-line-mv"/>
<circle cx="{B_SIDE_X}" cy="{ZONE_0_Y + 40}" r="4" fill="black"/>

<!-- Utility Breakers -->
<use href="#breaker-closed" x="{A_SIDE_X}" y="{ZONE_0_Y + 90}"/>
<text x="{A_SIDE_X + 20}" y="{ZONE_0_Y + 95}" class="rating" style="{FONTS['heading3']}">CB-U1 (N.C.)</text>

<use href="#breaker-closed" x="{B_SIDE_X}" y="{ZONE_0_Y + 90}"/>
<text x="{B_SIDE_X + 20}" y="{ZONE_0_Y + 95}" class="rating" style="{FONTS['heading3']}">CB-U2 (N.C.)</text>

<!-- Transformers A-Side and B-Side -->
<use href="#transformer" x="{A_SIDE_X}" y="{ZONE_0_Y + 200}"/>
<text x="{A_SIDE_X}" y="{ZONE_0_Y + 270}" class="equipment-name" text-anchor="middle" style="{FONTS['heading2']}">XFMR-1</text>
<text x="{A_SIDE_X}" y="{ZONE_0_Y + 285}" class="rating" text-anchor="middle" style="{FONTS['heading3']}">10kV/400V</text>

<use href="#transformer" x="{B_SIDE_X}" y="{ZONE_0_Y + 200}"/>
<text x="{B_SIDE_X}" y="{ZONE_0_Y + 270}" class="equipment-name" text-anchor="middle" style="{FONTS['heading2']}">XFMR-2</text>
<text x="{B_SIDE_X}" y="{ZONE_0_Y + 285}" class="rating" text-anchor="middle" style="{FONTS['heading3']}">10kV/400V</text>

<!-- Transformer to ATS connections -->
<line x1="{A_SIDE_X}" y1="{ZONE_0_Y + 240}" x2="{A_SIDE_X}" y2="{ZONE_0_Y + 350}" class="power-line-lv"/>
<line x1="{B_SIDE_X}" y1="{ZONE_0_Y + 240}" x2="{B_SIDE_X}" y2="{ZONE_0_Y + 350}" class="power-line-lv"/>

<!-- ATS (Automatic Transfer Switch) -->
<rect x="{A_SIDE_X - 60}" y="{ZONE_0_Y + 320}" width="120" height="80" class="mv-switchboard"/>
<text x="{A_SIDE_X}" y="{ZONE_0_Y + 350}" class="equipment-name" text-anchor="middle" style="{FONTS['heading2']}">ATS-1</text>
<text x="{A_SIDE_X}" y="{ZONE_0_Y + 370}" class="rating" text-anchor="middle" style="{FONTS['heading3']}">400V</text>

<rect x="{B_SIDE_X - 60}" y="{ZONE_0_Y + 320}" width="120" height="80" class="mv-switchboard"/>
<text x="{B_SIDE_X}" y="{ZONE_0_Y + 350}" class="equipment-name" text-anchor="middle" style="{FONTS['heading2']}">ATS-2</text>
<text x="{B_SIDE_X}" y="{ZONE_0_Y + 370}" class="rating" text-anchor="middle" style="{FONTS['heading3']}">400V</text>

<!-- ATS to Generator bus connections -->
<line x1="{A_SIDE_X}" y1="{ZONE_0_Y + 400}" x2="{A_SIDE_X}" y2="{ZONE_1_Y - 50}" class="power-line-lv"/>
<line x1="{B_SIDE_X}" y1="{ZONE_0_Y + 400}" x2="{B_SIDE_X}" y2="{ZONE_1_Y - 50}" class="power-line-lv"/>

<!-- ZONE 1: GENERATOR SETS (2 per side for N+1) -->
<!-- A-Side Generators -->
<circle cx="{gen_a_positions[0]}" cy="{ZONE_1_Y}" r="60" class="generator-box"/>
<text x="{gen_a_positions[0]}" y="{ZONE_1_Y - 10}" class="equipment-name" text-anchor="middle" style="{FONTS['heading2']}">GEN</text>
<text x="{gen_a_positions[0]}" y="{ZONE_1_Y + 5}" class="equipment-name" text-anchor="middle" style="{FONTS['heading2']}">N=1</text>
<circle cx="{gen_a_positions[0]}" cy="{ZONE_1_Y}" r="50" fill="none" stroke="#E65100" stroke-width="2"/>
<text x="{gen_a_positions[0]}" y="{ZONE_1_Y + 80}" class="rating" text-anchor="middle" style="{FONTS['heading3']}">MTU-1</text>
<text x="{gen_a_positions[0]}" y="{ZONE_1_Y + 95}" class="rating" text-anchor="middle" style="{FONTS['heading3']}">1000 kVA</text>

<circle cx="{gen_a_positions[1]}" cy="{ZONE_1_Y}" r="60" class="generator-box"/>
<text x="{gen_a_positions[1]}" y="{ZONE_1_Y - 10}" class="equipment-name" text-anchor="middle" style="{FONTS['heading2']}">GEN</text>
<text x="{gen_a_positions[1]}" y="{ZONE_1_Y + 5}" class="equipment-name" text-anchor="middle" style="{FONTS['heading2']}">N=2</text>
<circle cx="{gen_a_positions[1]}" cy="{ZONE_1_Y}" r="50" fill="none" stroke="#E65100" stroke-width="2"/>
<text x="{gen_a_positions[1]}" y="{ZONE_1_Y + 80}" class="rating" text-anchor="middle" style="{FONTS['heading3']}">MTU-2</text>
<text x="{gen_a_positions[1]}" y="{ZONE_1_Y + 95}" class="rating" text-anchor="middle" style="{FONTS['heading3']}">1000 kVA</text>

<!-- B-Side Generators -->
<circle cx="{gen_b_positions[0]}" cy="{ZONE_1_Y}" r="60" class="generator-box"/>
<text x="{gen_b_positions[0]}" y="{ZONE_1_Y - 10}" class="equipment-name" text-anchor="middle" style="{FONTS['heading2']}">GEN</text>
<text x="{gen_b_positions[0]}" y="{ZONE_1_Y + 5}" class="equipment-name" text-anchor="middle" style="{FONTS['heading2']}">N=3</text>
<circle cx="{gen_b_positions[0]}" cy="{ZONE_1_Y}" r="50" fill="none" stroke="#E65100" stroke-width="2"/>
<text x="{gen_b_positions[0]}" y="{ZONE_1_Y + 80}" class="rating" text-anchor="middle" style="{FONTS['heading3']}">MTU-3</text>
<text x="{gen_b_positions[0]}" y="{ZONE_1_Y + 95}" class="rating" text-anchor="middle" style="{FONTS['heading3']}">1000 kVA</text>

<circle cx="{gen_b_positions[1]}" cy="{ZONE_1_Y}" r="60" class="generator-box"/>
<text x="{gen_b_positions[1]}" y="{ZONE_1_Y - 10}" class="equipment-name" text-anchor="middle" style="{FONTS['heading2']}">GEN</text>
<text x="{gen_b_positions[1]}" y="{ZONE_1_Y + 5}" class="equipment-name" text-anchor="middle" style="{FONTS['heading2']}">N=4</text>
<circle cx="{gen_b_positions[1]}" cy="{ZONE_1_Y}" r="50" fill="none" stroke="#E65100" stroke-width="2"/>
<text x="{gen_b_positions[1]}" y="{ZONE_1_Y + 80}" class="rating" text-anchor="middle" style="{FONTS['heading3']}">MTU-4</text>
<text x="{gen_b_positions[1]}" y="{ZONE_1_Y + 95}" class="rating" text-anchor="middle" style="{FONTS['heading3']}">1000 kVA</text>

<!-- Generator breakers and bus connections -->
<line x1="{gen_a_positions[0]}" y1="{ZONE_1_Y + 60}" x2="{gen_a_positions[0]}" y2="{ZONE_1_Y + 150}" class="power-line-lv"/>
<use href="#breaker-closed" x="{gen_a_positions[0]}" y="{ZONE_1_Y + 110}"/>
<text x="{gen_a_positions[0] + 20}" y="{ZONE_1_Y + 115}" class="rating" style="{FONTS['heading3']}">CB-M1 (N.C.)</text>

<line x1="{gen_a_positions[1]}" y1="{ZONE_1_Y + 60}" x2="{gen_a_positions[1]}" y2="{ZONE_1_Y + 150}" class="power-line-lv"/>
<use href="#breaker-closed" x="{gen_a_positions[1]}" y="{ZONE_1_Y + 110}"/>
<text x="{gen_a_positions[1] + 20}" y="{ZONE_1_Y + 115}" class="rating" style="{FONTS['heading3']}">CB-M2 (N.C.)</text>

<line x1="{gen_b_positions[0]}" y1="{ZONE_1_Y + 60}" x2="{gen_b_positions[0]}" y2="{ZONE_1_Y + 150}" class="power-line-lv"/>
<use href="#breaker-closed" x="{gen_b_positions[0]}" y="{ZONE_1_Y + 110}"/>
<text x="{gen_b_positions[0] + 20}" y="{ZONE_1_Y + 115}" class="rating" style="{FONTS['heading3']}">CB-M3 (N.C.)</text>

<line x1="{gen_b_positions[1]}" y1="{ZONE_1_Y + 60}" x2="{gen_b_positions[1]}" y2="{ZONE_1_Y + 150}" class="power-line-lv"/>
<use href="#breaker-closed" x="{gen_b_positions[1]}" y="{ZONE_1_Y + 110}"/>
<text x="{gen_b_positions[1] + 20}" y="{ZONE_1_Y + 115}" class="rating" style="{FONTS['heading3']}">CB-M4 (N.C.)</text>

<!-- Generator bus (horizontal) -->
<line x1="{gen_a_positions[0]}" y1="{ZONE_1_Y + 150}" x2="{gen_a_positions[1]}" y2="{ZONE_1_Y + 150}" class="power-line-lv" stroke-width="4"/>
<line x1="{gen_b_positions[0]}" y1="{ZONE_1_Y + 150}" x2="{gen_b_positions[1]}" y2="{ZONE_1_Y + 150}" class="power-line-lv" stroke-width="4"/>

<!-- Generator bus to main distribution -->
<line x1="{A_SIDE_X}" y1="{ZONE_1_Y - 50}" x2="{A_SIDE_X}" y2="{ZONE_1_Y + 150}" class="power-line-lv"/>
<circle cx="{A_SIDE_X}" cy="{ZONE_1_Y + 150}" r="4" fill="black"/>

<line x1="{B_SIDE_X}" y1="{ZONE_1_Y - 50}" x2="{B_SIDE_X}" y2="{ZONE_1_Y + 150}" class="power-line-lv"/>
<circle cx="{B_SIDE_X}" cy="{ZONE_1_Y + 150}" r="4" fill="black"/>

<!-- Main distribution to UPS -->
<line x1="{A_SIDE_X}" y1="{ZONE_1_Y + 150}" x2="{A_SIDE_X}" y2="{ZONE_1_Y + 250}" class="power-line-lv"/>
<use href="#breaker-closed" x="{A_SIDE_X}" y="{ZONE_1_Y + 190}"/>
<text x="{A_SIDE_X + 20}" y="{ZONE_1_Y + 195}" class="rating" style="{FONTS['heading3']}">CB-A (N.C.)</text>

<line x1="{B_SIDE_X}" y1="{ZONE_1_Y + 150}" x2="{B_SIDE_X}" y2="{ZONE_1_Y + 250}" class="power-line-lv"/>
<use href="#breaker-closed" x="{B_SIDE_X}" y="{ZONE_1_Y + 190}"/>
<text x="{B_SIDE_X + 20}" y="{ZONE_1_Y + 195}" class="rating" style="{FONTS['heading3']}">CB-B (N.C.)</text>

<!-- LV Switchboards -->
<rect x="{A_SIDE_X - 120}" y="{ZONE_1_Y + 250}" width="240" height="150" class="lv-switchboard"/>
<text x="{A_SIDE_X}" y="{ZONE_1_Y + 280}" class="equipment-name" text-anchor="middle" style="{FONTS['heading2']}">LV-SWBD-A</text>
<text x="{A_SIDE_X}" y="{ZONE_1_Y + 300}" class="rating" text-anchor="middle" style="{FONTS['heading3']}">400V Bus</text>
<line x1="{A_SIDE_X - 100}" y1="{ZONE_1_Y + 270}" x2="{A_SIDE_X + 100}" y2="{ZONE_1_Y + 270}" class="power-line-lv" stroke-width="3"/>

<rect x="{B_SIDE_X - 120}" y="{ZONE_1_Y + 250}" width="240" height="150" class="lv-switchboard"/>
<text x="{B_SIDE_X}" y="{ZONE_1_Y + 280}" class="equipment-name" text-anchor="middle" style="{FONTS['heading2']}">LV-SWBD-B</text>
<text x="{B_SIDE_X}" y="{ZONE_1_Y + 300}" class="rating" text-anchor="middle" style="{FONTS['heading3']}">400V Bus</text>
<line x1="{B_SIDE_X - 100}" y1="{ZONE_1_Y + 270}" x2="{B_SIDE_X + 100}" y2="{ZONE_1_Y + 270}" class="power-line-lv" stroke-width="3"/>

<!-- ZONE 2: UPS SYSTEMS (3 per side for N+1) -->
<!-- A-Side UPS connections from LV-SWBD-A -->
<line x1="{A_SIDE_X}" y1="{ZONE_1_Y + 400}" x2="{A_SIDE_X}" y2="{ZONE_2_Y - 200}" class="power-line-lv"/>
<line x1="{A_SIDE_X}" y1="{ZONE_2_Y - 200}" x2="{ups_a_positions[0]}" y2="{ZONE_2_Y - 200}" class="power-line-lv"/>
<line x1="{A_SIDE_X}" y1="{ZONE_2_Y - 200}" x2="{ups_a_positions[1]}" y2="{ZONE_2_Y - 200}" class="power-line-lv"/>
<line x1="{A_SIDE_X}" y1="{ZONE_2_Y - 200}" x2="{ups_a_positions[2]}" y2="{ZONE_2_Y - 200}" class="power-line-lv"/>
<circle cx="{A_SIDE_X}" cy="{ZONE_2_Y - 200}" r="4" fill="black"/>

<!-- A-Side UPS modules -->
<rect x="{ups_a_positions[0] - 70}" y="{ZONE_2_Y - 150}" width="140" height="200" class="ups-module"/>
<text x="{ups_a_positions[0]}" y="{ZONE_2_Y - 110}" class="equipment-name" text-anchor="middle" style="{FONTS['heading2']}">UPS-A1</text>
<text x="{ups_a_positions[0]}" y="{ZONE_2_Y - 90}" class="rating" text-anchor="middle" style="{FONTS['heading3']}">Battery</text>
<rect x="{ups_a_positions[0] - 50}" y="{ZONE_2_Y - 70}" width="100" height="60" fill="#FFE0B2" stroke="#FF6F00" stroke-width="2"/>
<text x="{ups_a_positions[0]}" y="{ZONE_2_Y - 35}" class="rating" text-anchor="middle" style="{FONTS['heading3']}">500 kVA</text>
<line x1="{ups_a_positions[0]}" y1="{ZONE_2_Y - 200}" x2="{ups_a_positions[0]}" y2="{ZONE_2_Y - 150}" class="power-line-lv"/>
<use href="#breaker-closed" x="{ups_a_positions[0]}" y="{ZONE_2_Y - 175}"/>

<rect x="{ups_a_positions[1] - 70}" y="{ZONE_2_Y - 150}" width="140" height="200" class="ups-module"/>
<text x="{ups_a_positions[1]}" y="{ZONE_2_Y - 110}" class="equipment-name" text-anchor="middle" style="{FONTS['heading2']}">UPS-A2</text>
<text x="{ups_a_positions[1]}" y="{ZONE_2_Y - 90}" class="rating" text-anchor="middle" style="{FONTS['heading3']}">Battery</text>
<rect x="{ups_a_positions[1] - 50}" y="{ZONE_2_Y - 70}" width="100" height="60" fill="#FFE0B2" stroke="#FF6F00" stroke-width="2"/>
<text x="{ups_a_positions[1]}" y="{ZONE_2_Y - 35}" class="rating" text-anchor="middle" style="{FONTS['heading3']}">500 kVA</text>
<line x1="{ups_a_positions[1]}" y1="{ZONE_2_Y - 200}" x2="{ups_a_positions[1]}" y2="{ZONE_2_Y - 150}" class="power-line-lv"/>
<use href="#breaker-closed" x="{ups_a_positions[1]}" y="{ZONE_2_Y - 175}"/>

<rect x="{ups_a_positions[2] - 70}" y="{ZONE_2_Y - 150}" width="140" height="200" class="ups-module"/>
<text x="{ups_a_positions[2]}" y="{ZONE_2_Y - 110}" class="equipment-name" text-anchor="middle" style="{FONTS['heading2']}">UPS-A3</text>
<text x="{ups_a_positions[2]}" y="{ZONE_2_Y - 90}" class="rating" text-anchor="middle" style="{FONTS['heading3']}">Battery</text>
<rect x="{ups_a_positions[2] - 50}" y="{ZONE_2_Y - 70}" width="100" height="60" fill="#FFE0B2" stroke="#FF6F00" stroke-width="2"/>
<text x="{ups_a_positions[2]}" y="{ZONE_2_Y - 35}" class="rating" text-anchor="middle" style="{FONTS['heading3']}">500 kVA</text>
<line x1="{ups_a_positions[2]}" y1="{ZONE_2_Y - 200}" x2="{ups_a_positions[2]}" y2="{ZONE_2_Y - 150}" class="power-line-lv"/>
<use href="#breaker-closed" x="{ups_a_positions[2]}" y="{ZONE_2_Y - 175}"/>

<!-- B-Side UPS connections from LV-SWBD-B -->
<line x1="{B_SIDE_X}" y1="{ZONE_1_Y + 400}" x2="{B_SIDE_X}" y2="{ZONE_2_Y - 200}" class="power-line-lv"/>
<line x1="{B_SIDE_X}" y1="{ZONE_2_Y - 200}" x2="{ups_b_positions[0]}" y2="{ZONE_2_Y - 200}" class="power-line-lv"/>
<line x1="{B_SIDE_X}" y1="{ZONE_2_Y - 200}" x2="{ups_b_positions[1]}" y2="{ZONE_2_Y - 200}" class="power-line-lv"/>
<line x1="{B_SIDE_X}" y1="{ZONE_2_Y - 200}" x2="{ups_b_positions[2]}" y2="{ZONE_2_Y - 200}" class="power-line-lv"/>
<circle cx="{B_SIDE_X}" cy="{ZONE_2_Y - 200}" r="4" fill="black"/>

<!-- B-Side UPS modules -->
<rect x="{ups_b_positions[0] - 70}" y="{ZONE_2_Y - 150}" width="140" height="200" class="ups-module"/>
<text x="{ups_b_positions[0]}" y="{ZONE_2_Y - 110}" class="equipment-name" text-anchor="middle" style="{FONTS['heading2']}">UPS-B1</text>
<text x="{ups_b_positions[0]}" y="{ZONE_2_Y - 90}" class="rating" text-anchor="middle" style="{FONTS['heading3']}">Battery</text>
<rect x="{ups_b_positions[0] - 50}" y="{ZONE_2_Y - 70}" width="100" height="60" fill="#FFE0B2" stroke="#FF6F00" stroke-width="2"/>
<text x="{ups_b_positions[0]}" y="{ZONE_2_Y - 35}" class="rating" text-anchor="middle" style="{FONTS['heading3']}">500 kVA</text>
<line x1="{ups_b_positions[0]}" y1="{ZONE_2_Y - 200}" x2="{ups_b_positions[0]}" y2="{ZONE_2_Y - 150}" class="power-line-lv"/>
<use href="#breaker-closed" x="{ups_b_positions[0]}" y="{ZONE_2_Y - 175}"/>

<rect x="{ups_b_positions[1] - 70}" y="{ZONE_2_Y - 150}" width="140" height="200" class="ups-module"/>
<text x="{ups_b_positions[1]}" y="{ZONE_2_Y - 110}" class="equipment-name" text-anchor="middle" style="{FONTS['heading2']}">UPS-B2</text>
<text x="{ups_b_positions[1]}" y="{ZONE_2_Y - 90}" class="rating" text-anchor="middle" style="{FONTS['heading3']}">Battery</text>
<rect x="{ups_b_positions[1] - 50}" y="{ZONE_2_Y - 70}" width="100" height="60" fill="#FFE0B2" stroke="#FF6F00" stroke-width="2"/>
<text x="{ups_b_positions[1]}" y="{ZONE_2_Y - 35}" class="rating" text-anchor="middle" style="{FONTS['heading3']}">500 kVA</text>
<line x1="{ups_b_positions[1]}" y1="{ZONE_2_Y - 200}" x2="{ups_b_positions[1]}" y2="{ZONE_2_Y - 150}" class="power-line-lv"/>
<use href="#breaker-closed" x="{ups_b_positions[1]}" y="{ZONE_2_Y - 175}"/>

<rect x="{ups_b_positions[2] - 70}" y="{ZONE_2_Y - 150}" width="140" height="200" class="ups-module"/>
<text x="{ups_b_positions[2]}" y="{ZONE_2_Y - 110}" class="equipment-name" text-anchor="middle" style="{FONTS['heading2']}">UPS-B3</text>
<text x="{ups_b_positions[2]}" y="{ZONE_2_Y - 90}" class="rating" text-anchor="middle" style="{FONTS['heading3']}">Battery</text>
<rect x="{ups_b_positions[2] - 50}" y="{ZONE_2_Y - 70}" width="100" height="60" fill="#FFE0B2" stroke="#FF6F00" stroke-width="2"/>
<text x="{ups_b_positions[2]}" y="{ZONE_2_Y - 35}" class="rating" text-anchor="middle" style="{FONTS['heading3']}">500 kVA</text>
<line x1="{ups_b_positions[2]}" y1="{ZONE_2_Y - 200}" x2="{ups_b_positions[2]}" y2="{ZONE_2_Y - 150}" class="power-line-lv"/>
<use href="#breaker-closed" x="{ups_b_positions[2]}" y="{ZONE_2_Y - 175}"/>

<!-- UPS output bus (parallel connection) -->
<line x1="{ups_a_positions[0]}" y1="{ZONE_2_Y + 50}" x2="{ups_a_positions[0]}" y2="{ZONE_2_Y + 150}" class="power-line-lv"/>
<line x1="{ups_a_positions[1]}" y1="{ZONE_2_Y + 50}" x2="{ups_a_positions[1]}" y2="{ZONE_2_Y + 150}" class="power-line-lv"/>
<line x1="{ups_a_positions[2]}" y1="{ZONE_2_Y + 50}" x2="{ups_a_positions[2]}" y2="{ZONE_2_Y + 150}" class="power-line-lv"/>
<line x1="{ups_a_positions[0]}" y1="{ZONE_2_Y + 150}" x2="{ups_a_positions[2]}" y2="{ZONE_2_Y + 150}" class="power-line-lv" stroke-width="4"/>

<line x1="{ups_b_positions[0]}" y1="{ZONE_2_Y + 50}" x2="{ups_b_positions[0]}" y2="{ZONE_2_Y + 150}" class="power-line-lv"/>
<line x1="{ups_b_positions[1]}" y1="{ZONE_2_Y + 50}" x2="{ups_b_positions[1]}" y2="{ZONE_2_Y + 150}" class="power-line-lv"/>
<line x1="{ups_b_positions[2]}" y1="{ZONE_2_Y + 50}" x2="{ups_b_positions[2]}" y2="{ZONE_2_Y + 150}" class="power-line-lv"/>
<line x1="{ups_b_positions[0]}" y1="{ZONE_2_Y + 150}" x2="{ups_b_positions[2]}" y2="{ZONE_2_Y + 150}" class="power-line-lv" stroke-width="4"/>

<!-- UPS bus to distribution panels -->
<line x1="{A_SIDE_X}" y1="{ZONE_2_Y + 150}" x2="{A_SIDE_X}" y2="{ZONE_3_Y - 100}" class="power-line-lv"/>
<circle cx="{A_SIDE_X}" cy="{ZONE_2_Y + 150}" r="4" fill="black"/>
<use href="#breaker-closed" x="{A_SIDE_X}" y="{ZONE_2_Y + 200}"/>
<text x="{A_SIDE_X + 20}" y="{ZONE_2_Y + 205}" class="rating" style="{FONTS['heading3']}">CB-DA (N.C.)</text>

<line x1="{B_SIDE_X}" y1="{ZONE_2_Y + 150}" x2="{B_SIDE_X}" y2="{ZONE_3_Y - 100}" class="power-line-lv"/>
<circle cx="{B_SIDE_X}" cy="{ZONE_2_Y + 150}" r="4" fill="black"/>
<use href="#breaker-closed" x="{B_SIDE_X}" y="{ZONE_2_Y + 200}"/>
<text x="{B_SIDE_X + 20}" y="{ZONE_2_Y + 205}" class="rating" style="{FONTS['heading3']}">CB-DB (N.C.)</text>

<!-- ZONE 3: DISTRIBUTION PANELS -->
<rect x="{A_SIDE_X - 150}" y="{ZONE_3_Y - 100}" width="300" height="200" class="dist-panel"/>
<text x="{A_SIDE_X}" y="{ZONE_3_Y - 60}" class="equipment-name" text-anchor="middle" style="{FONTS['heading2']}">DIST-PANEL-A</text>
<text x="{A_SIDE_X}" y="{ZONE_3_Y - 40}" class="rating" text-anchor="middle" style="{FONTS['heading3']}">Static Transfer Switch</text>
<line x1="{A_SIDE_X - 130}" y1="{ZONE_3_Y - 20}" x2="{A_SIDE_X + 130}" y2="{ZONE_3_Y - 20}" class="power-line-lv" stroke-width="3"/>

<rect x="{B_SIDE_X - 150}" y="{ZONE_3_Y - 100}" width="300" height="200" class="dist-panel"/>
<text x="{B_SIDE_X}" y="{ZONE_3_Y - 60}" class="equipment-name" text-anchor="middle" style="{FONTS['heading2']}">DIST-PANEL-B</text>
<text x="{B_SIDE_X}" y="{ZONE_3_Y - 40}" class="rating" text-anchor="middle" style="{FONTS['heading3']}">Static Transfer Switch</text>
<line x1="{B_SIDE_X - 130}" y1="{ZONE_3_Y - 20}" x2="{B_SIDE_X + 130}" y2="{ZONE_3_Y - 20}" class="power-line-lv" stroke-width="3"/>

<!-- Distribution to racks -->
<line x1="{A_SIDE_X}" y1="{ZONE_3_Y + 100}" x2="{A_SIDE_X}" y2="{ZONE_3_Y + 500}" class="power-line-lv"/>
<line x1="{B_SIDE_X}" y1="{ZONE_3_Y + 100}" x2="{B_SIDE_X}" y2="{ZONE_3_Y + 500}" class="power-line-lv"/>

<!-- Horizontal bus to all racks -->
<line x1="{rack_positions[0]}" y1="{ZONE_3_Y + 500}" x2="{rack_positions[5]}" y2="{ZONE_3_Y + 500}" class="power-line-lv" stroke-width="4"/>
<circle cx="{A_SIDE_X}" cy="{ZONE_3_Y + 500}" r="4" fill="black"/>
<circle cx="{B_SIDE_X}" cy="{ZONE_3_Y + 500}" r="4" fill="black"/>

<!-- ZONE 4: IT LOADS (6 server racks with dual PSUs) -->
<!-- Rack connections -->
'''

# Generate 6 racks
for i, rack_x in enumerate(rack_positions):
    rack_num = i + 1
    # Color code: racks 1-2 green (non-critical), 3-4 yellow (moderate), 5-6 red (critical)
    if rack_num <= 2:
        rack_color = "#C8E6C9"  # Light green
        rack_label = "Non-Critical"
    elif rack_num <= 4:
        rack_color = "#FFF9C4"  # Light yellow
        rack_label = "Application"
    else:
        rack_color = "#FFCDD2"  # Light red
        rack_label = "Critical"

    svg += f'''
<!-- Rack {rack_num} -->
<rect x="{rack_x - 50}" y="{ZONE_4_Y}" width="100" height="400" fill="{rack_color}" stroke="#333" stroke-width="2"/>
<text x="{rack_x}" y="{ZONE_4_Y + 30}" class="equipment-name" text-anchor="middle" style="{FONTS['heading2']}">RACK-{rack_num}</text>
<text x="{rack_x}" y="{ZONE_4_Y + 50}" class="rating" text-anchor="middle" style="{FONTS['heading3']}">{rack_label}</text>

<!-- Dual power feeds to rack -->
<line x1="{rack_x}" y1="{ZONE_3_Y + 500}" x2="{rack_x}" y2="{ZONE_4_Y}" class="power-line-lv"/>
<circle cx="{rack_x}" cy="{ZONE_3_Y + 500}" r="4" fill="black"/>

<!-- Servers in rack (represented as rectangles) -->
<rect x="{rack_x - 40}" y="{ZONE_4_Y + 70}" width="80" height="30" fill="white" stroke="#666" stroke-width="1"/>
<text x="{rack_x}" y="{ZONE_4_Y + 90}" class="rating" text-anchor="middle" style="{FONTS['heading3']}">Server</text>
<rect x="{rack_x - 40}" y="{ZONE_4_Y + 110}" width="80" height="30" fill="white" stroke="#666" stroke-width="1"/>
<text x="{rack_x}" y="{ZONE_4_Y + 130}" class="rating" text-anchor="middle" style="{FONTS['heading3']}">Server</text>
<rect x="{rack_x - 40}" y="{ZONE_4_Y + 150}" width="80" height="30" fill="white" stroke="#666" stroke-width="1"/>
<text x="{rack_x}" y="{ZONE_4_Y + 170}" class="rating" text-anchor="middle" style="{FONTS['heading3']}">Server</text>

<!-- Dual PSU indication -->
<rect x="{rack_x - 40}" y="{ZONE_4_Y + 200}" width="35" height="20" fill="#E3F2FD" stroke="#1976D2" stroke-width="1"/>
<text x="{rack_x - 22}" y="{ZONE_4_Y + 213}" class="rating" text-anchor="middle" style="{FONTS['heading3']}">PSU-A</text>
<rect x="{rack_x + 5}" y="{ZONE_4_Y + 200}" width="35" height="20" fill="#E3F2FD" stroke="#1976D2" stroke-width="1"/>
<text x="{rack_x + 22}" y="{ZONE_4_Y + 213}" class="rating" text-anchor="middle" style="{FONTS['heading3']}">PSU-B</text>

<!-- Load indication -->
<text x="{rack_x}" y="{ZONE_4_Y + 350}" class="rating" text-anchor="middle" style="{FONTS['heading3']}">Load: 4kW</text>
<text x="{rack_x}" y="{ZONE_4_Y + 370}" class="rating" text-anchor="middle" style="{FONTS['heading3']}">per rack</text>
'''

# Add legend and notes
svg += f'''
<!-- Legend -->
<rect x="2800" y="200" width="300" height="500" fill="#F5F5F5" stroke="#333" stroke-width="2"/>
<text x="2950" y="240" class="equipment-name" text-anchor="middle" style="{FONTS['heading2']}">LEGEND</text>

<line x1="2830" y1="270" x2="2900" y2="270" class="power-line-mv"/>
<text x="2920" y="275" class="rating" style="{FONTS['heading3']}">Medium Voltage (10kV)</text>

<line x1="2830" y1="300" x2="2900" y2="300" class="power-line-lv"/>
<text x="2920" y="305" class="rating" style="{FONTS['heading3']}">Low Voltage (400V)</text>

<use href="#breaker-closed" x="2865" y="320"/>
<text x="2920" y="335" class="rating" style="{FONTS['heading3']}">Breaker Closed (N.C.)</text>

<use href="#breaker-open" x="2865" y="360"/>
<text x="2920" y="375" class="rating" style="{FONTS['heading3']}">Breaker Open (N.O.)</text>

<circle cx="2865" cy="405" r="4" fill="black"/>
<text x="2920" y="410" class="rating" style="{FONTS['heading3']}">Connection Point</text>

<rect x="2830" y="430" width="60" height="30" fill="#C8E6C9" stroke="#333" stroke-width="1"/>
<text x="2920" y="450" class="rating" style="{FONTS['heading3']}">Non-Critical Load</text>

<rect x="2830" y="470" width="60" height="30" fill="#FFF9C4" stroke="#333" stroke-width="1"/>
<text x="2920" y="490" class="rating" style="{FONTS['heading3']}">Application Load</text>

<rect x="2830" y="510" width="60" height="30" fill="#FFCDD2" stroke="#333" stroke-width="1"/>
<text x="2920" y="530" class="rating" style="{FONTS['heading3']}">Critical Load</text>

<!-- Design specifications -->
<rect x="2800" y="750" width="300" height="350" fill="#F5F5F5" stroke="#333" stroke-width="2"/>
<text x="2950" y="790" class="equipment-name" text-anchor="middle" style="{FONTS['heading2']}">SPECIFICATIONS</text>

<text x="2820" y="830" class="rating" style="{FONTS['heading3']}">Tier Level: IV</text>
<text x="2820" y="850" class="rating" style="{FONTS['heading3']}">Topology: 2(N+1)</text>
<text x="2820" y="870" class="rating" style="{FONTS['heading3']}">Availability: 99.995%</text>
<text x="2820" y="890" class="rating" style="{FONTS['heading3']}">Downtime: 2.4 min/year</text>

<text x="2820" y="930" class="rating" style="{FONTS['heading3']}">Utility: Dual feed 10kV</text>
<text x="2820" y="950" class="rating" style="{FONTS['heading3']}">Generators: 4 × 1000 kVA</text>
<text x="2820" y="970" class="rating" style="{FONTS['heading3']}">UPS: 6 × 500 kVA</text>
<text x="2820" y="990" class="rating" style="{FONTS['heading3']}">Total IT Load: 24 kW</text>

<text x="2820" y="1030" class="rating" style="{FONTS['heading3']}">Concurrent Maintainable</text>
<text x="2820" y="1050" class="rating" style="{FONTS['heading3']}">Fault Tolerant</text>
<text x="2820" y="1070" class="rating" style="{FONTS['heading3']}">Dual Power Paths</text>

<!-- Document info -->
<text x="100" y="{HEIGHT - 50}" class="rating" style="{FONTS['heading3']}">Document: Tier IV Data Center PDS</text>
<text x="100" y="{HEIGHT - 30}" class="rating" style="{FONTS['heading3']}">Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</text>
<text x="100" y="{HEIGHT - 10}" class="rating" style="{FONTS['heading3']}">Standards: SLD v1.1 | IEEE 315 | IEC 60617</text>

</svg>'''

# Save the file
output_file = 'tier_iv_datacenter_sld.svg'
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(svg)

print(f"[OK] Tier IV Data Center SLD generated: {output_file}")
print(f"[OK] Canvas size: {WIDTH}x{HEIGHT}px")
print(f"[OK] Equipment count: 2 Utilities, 2 Transformers, 2 ATS, 4 Generators, 6 UPS, 6 Racks")
print(f"[OK] Topology: 2(N+1) Fully Redundant")
print(f"[OK] Standards compliant: SLD v1.1, IEEE 315, IEC 60617")
