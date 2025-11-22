#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test SLD Standards Module Integration
Verifies that sld_standards.py provides all required components
"""

import sys
import io
from datetime import datetime

# Fix Windows console encoding
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
from sld_standards import (
    get_svg_style_section,
    get_svg_symbols,
    calculate_symmetric_positions,
    TEXT_STYLES,
    EQUIPMENT_STYLES,
    LAYOUT
)

def test_standards_integration():
    """Test that all standards components work correctly"""

    print("=" * 80)
    print("SLD STANDARDS MODULE INTEGRATION TEST")
    print("=" * 80)

    # Test 1: Style section generation
    print("\n[TEST 1] Generating CSS styles...")
    styles = get_svg_style_section()
    assert 'Open Sans' in styles, "❌ Open Sans fonts not found in styles"
    assert '.title' in styles, "❌ Title class not found"
    assert '.equipment-label' in styles, "❌ Equipment label class not found"
    assert '.rating' in styles, "❌ Rating class not found"
    print("✓ CSS styles generated with Open Sans fonts")

    # Test 2: Symbol definitions
    print("\n[TEST 2] Generating IEEE symbols...")
    symbols = get_svg_symbols()
    assert '<defs>' in symbols, "❌ Defs tag not found"
    assert 'breaker-closed' in symbols, "❌ Breaker symbol not found"
    assert 'transformer' in symbols, "❌ Transformer symbol not found"
    assert 'generator' in symbols, "❌ Generator symbol not found"
    print("✓ IEEE Std 315 symbols generated")

    # Test 3: Symmetrical positioning
    print("\n[TEST 3] Testing symmetrical position calculation...")
    positions = calculate_symmetric_positions(2800, 4, 80, 200)
    assert len(positions) == 4, f"❌ Expected 4 positions, got {len(positions)}"
    assert positions[0] < positions[1] < positions[2] < positions[3], "❌ Positions not in ascending order"

    # Check spacing between positions
    spacing1 = positions[1] - positions[0]
    spacing2 = positions[2] - positions[1]
    spacing3 = positions[3] - positions[2]
    assert abs(spacing1 - spacing2) < 0.1, f"❌ Uneven spacing: {spacing1} vs {spacing2}"
    assert abs(spacing2 - spacing3) < 0.1, f"❌ Uneven spacing: {spacing2} vs {spacing3}"
    print(f"✓ Symmetric positions: {[round(p, 1) for p in positions]}")
    print(f"  Spacing: {round(spacing1, 1)}px (equal across all)")

    # Test 4: Text styles dictionary
    print("\n[TEST 4] Checking TEXT_STYLES dictionary...")
    assert 'title' in TEXT_STYLES, "❌ Title style not found"
    assert 'equipment_label' in TEXT_STYLES, "❌ Equipment label style not found"
    assert 'rating' in TEXT_STYLES, "❌ Rating style not found"
    assert TEXT_STYLES['title']['font-family'] == '"Open Sans", Arial', "❌ Title font not Open Sans"
    assert TEXT_STYLES['title']['font-size'] == '24', "❌ Title size not 24px"
    assert TEXT_STYLES['equipment_label']['font-size'] == '14', "❌ Equipment label size not 14px"
    assert TEXT_STYLES['rating']['font-size'] == '11', "❌ Rating size not 11px"
    print("✓ TEXT_STYLES dictionary correct (Open Sans, 3-tier hierarchy)")

    # Test 5: Equipment styles
    print("\n[TEST 5] Checking EQUIPMENT_STYLES dictionary...")
    assert 'switchgear' in EQUIPMENT_STYLES, "❌ Switchgear style not found"
    assert 'transformer_box' in EQUIPMENT_STYLES, "❌ Transformer style not found"
    print("✓ EQUIPMENT_STYLES dictionary available")

    # Test 6: Layout constants
    print("\n[TEST 6] Checking LAYOUT constants...")
    assert LAYOUT['flow_direction'] == 'top_to_bottom', "❌ Flow direction not top_to_bottom"
    assert LAYOUT['minimum_spacing'] == 50, "❌ Minimum spacing not 50px"
    print("✓ LAYOUT constants available")

    # Test 7: Generate complete mini-SLD with full topology
    print("\n[TEST 7] Generating complete mini-SLD with full topology...")

    # Canvas settings
    WIDTH = 1600
    HEIGHT = 2000
    MARGIN = 150

    # Calculate symmetric positions for equipment
    utility_positions = calculate_symmetric_positions(WIDTH, 2, 150, MARGIN)
    mv_positions = calculate_symmetric_positions(WIDTH, 2, 240, MARGIN)
    tx_positions = calculate_symmetric_positions(WIDTH, 2, 80, MARGIN)
    lv_positions = calculate_symmetric_positions(WIDTH, 2, 200, MARGIN)

    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{WIDTH}" height="{HEIGHT}" xmlns="http://www.w3.org/2000/svg">

{get_svg_symbols()}
{get_svg_style_section()}

<!-- ===================================================================== -->
<!--                              TITLE BLOCK                              -->
<!-- ===================================================================== -->
<rect x="50" y="30" width="{WIDTH-250}" height="80" fill="white" stroke="black" stroke-width="2"/>
<text x="{WIDTH/2}" y="65" class="title" text-anchor="middle">SLD Standards Test - Complete Mini Topology</text>
<text x="{WIDTH/2}" y="90" class="rating" text-anchor="middle">Dual-Feed Architecture | N+1 | IEEE Std 315 / IEC 60617</text>

<rect x="{WIDTH-190}" y="30" width="140" height="80" fill="white" stroke="black" stroke-width="2"/>
<text x="{WIDTH-180}" y="55" class="rating">Date: {datetime.now().strftime('%Y-%m-%d')}</text>
<text x="{WIDTH-180}" y="75" class="rating">Doc: TEST-SLD-001</text>
<text x="{WIDTH-180}" y="95" class="rating">Rev: A</text>

<!-- ===================================================================== -->
<!--                          UTILITY SOURCES                              -->
<!-- ===================================================================== -->

<!-- Utility Feed 1 -->
<rect x="{utility_positions[0]-75}" y="160" width="150" height="80" fill="#87CEEB" stroke="black" stroke-width="2"/>
<text x="{utility_positions[0]}" y="195" class="equipment-label" text-anchor="middle">UTILITY-1</text>
<text x="{utility_positions[0]}" y="215" class="rating" text-anchor="middle">10 kV | 3 MW</text>

<line x1="{utility_positions[0]}" y1="240" x2="{utility_positions[0]}" y2="300" class="power-line"/>
<use href="#breaker-closed" x="{utility_positions[0]}" y="270"/>
<text x="{utility_positions[0]+25}" y="275" class="rating">CB-U1 (N.C.)</text>

<!-- Utility Feed 2 -->
<rect x="{utility_positions[1]-75}" y="160" width="150" height="80" fill="#87CEEB" stroke="black" stroke-width="2"/>
<text x="{utility_positions[1]}" y="195" class="equipment-label" text-anchor="middle">UTILITY-2</text>
<text x="{utility_positions[1]}" y="215" class="rating" text-anchor="middle">10 kV | 3 MW</text>

<line x1="{utility_positions[1]}" y1="240" x2="{utility_positions[1]}" y2="300" class="power-line"/>
<use href="#breaker-closed" x="{utility_positions[1]}" y="270"/>
<text x="{utility_positions[1]+25}" y="275" class="rating">CB-U2 (N.C.)</text>

<!-- ===================================================================== -->
<!--                    MV SWITCHBOARDS (10 kV)                            -->
<!-- ===================================================================== -->

<!-- MV-SWBD-A -->
<line x1="{utility_positions[0]}" y1="300" x2="{utility_positions[0]}" y2="350" class="power-line"/>
<line x1="{utility_positions[0]}" y1="350" x2="{mv_positions[0]}" y2="350" class="power-line"/>
<line x1="{mv_positions[0]}" y1="350" x2="{mv_positions[0]}" y2="400" class="power-line"/>
<use href="#breaker-closed" x="{mv_positions[0]}" y="375"/>
<text x="{mv_positions[0]+25}" y="380" class="rating">VCB-1 (N.C.)</text>

<rect x="{mv_positions[0]-120}" y="400" width="240" height="120" class="mv-switchboard"/>
<line x1="{mv_positions[0]-105}" y1="415" x2="{mv_positions[0]+105}" y2="415" class="bus"/>

<text x="{mv_positions[0]}" y="450" class="equipment-label" text-anchor="middle">MV-SWBD-A</text>
<text x="{mv_positions[0]}" y="470" class="rating" text-anchor="middle">10 kV | 3-Phase | 50 Hz</text>
<text x="{mv_positions[0]}" y="490" class="rating" text-anchor="middle">630A | 40 kA</text>

<!-- MV-SWBD-B -->
<line x1="{utility_positions[1]}" y1="300" x2="{utility_positions[1]}" y2="350" class="power-line"/>
<line x1="{utility_positions[1]}" y1="350" x2="{mv_positions[1]}" y2="350" class="power-line"/>
<line x1="{mv_positions[1]}" y1="350" x2="{mv_positions[1]}" y2="400" class="power-line"/>
<use href="#breaker-closed" x="{mv_positions[1]}" y="375"/>
<text x="{mv_positions[1]+25}" y="380" class="rating">VCB-2 (N.C.)</text>

<rect x="{mv_positions[1]-120}" y="400" width="240" height="120" class="mv-switchboard"/>
<line x1="{mv_positions[1]-105}" y1="415" x2="{mv_positions[1]+105}" y2="415" class="bus"/>

<text x="{mv_positions[1]}" y="450" class="equipment-label" text-anchor="middle">MV-SWBD-B</text>
<text x="{mv_positions[1]}" y="470" class="rating" text-anchor="middle">10 kV | 3-Phase | 50 Hz</text>
<text x="{mv_positions[1]}" y="490" class="rating" text-anchor="middle">630A | 40 kA</text>

<!-- Tie Breaker -->
<line x1="{mv_positions[0]+120}" y1="460" x2="{WIDTH/2-40}" y2="460" class="power-line"/>
<line x1="{WIDTH/2+40}" y1="460" x2="{mv_positions[1]-120}" y2="460" class="power-line"/>
<use href="#breaker-open" x="{WIDTH/2}" y="460"/>
<text x="{WIDTH/2}" y="440" class="rating" text-anchor="middle">TIE (N.O.)</text>

<!-- ===================================================================== -->
<!--              STEP-DOWN TRANSFORMERS (10 kV → 400V)                   -->
<!-- ===================================================================== -->

<!-- TX-1 from MV-A -->
<line x1="{mv_positions[0]}" y1="520" x2="{mv_positions[0]}" y2="580" class="power-line"/>
<line x1="{mv_positions[0]}" y1="580" x2="{tx_positions[0]}" y2="580" class="power-line"/>
<line x1="{tx_positions[0]}" y1="580" x2="{tx_positions[0]}" y2="663" class="power-line"/>
<use href="#breaker-closed" x="{tx_positions[0]}" y="620"/>
<text x="{tx_positions[0]+25}" y="625" class="rating">VCB-T1 (N.C.)</text>

<use href="#transformer" x="{tx_positions[0]}" y="690"/>
<rect x="{tx_positions[0]-40}" y="650" width="80" height="90" class="transformer-box"/>
<text x="{tx_positions[0]}" y="750" class="equipment-label" text-anchor="middle">TX-1</text>
<text x="{tx_positions[0]}" y="770" class="rating" text-anchor="middle">2,500 kVA</text>
<text x="{tx_positions[0]}" y="785" class="rating" text-anchor="middle">10kV/400V</text>

<line x1="{tx_positions[0]}" y1="717" x2="{tx_positions[0]}" y2="800" class="power-line"/>
<use href="#breaker-closed" x="{tx_positions[0]}" y="760"/>
<text x="{tx_positions[0]+25}" y="765" class="rating">CB-T1 (N.C.)</text>

<!-- TX-2 from MV-B -->
<line x1="{mv_positions[1]}" y1="520" x2="{mv_positions[1]}" y2="580" class="power-line"/>
<line x1="{mv_positions[1]}" y1="580" x2="{tx_positions[1]}" y2="580" class="power-line"/>
<line x1="{tx_positions[1]}" y1="580" x2="{tx_positions[1]}" y2="663" class="power-line"/>
<use href="#breaker-closed" x="{tx_positions[1]}" y="620"/>
<text x="{tx_positions[1]+25}" y="625" class="rating">VCB-T2 (N.C.)</text>

<use href="#transformer" x="{tx_positions[1]}" y="690"/>
<rect x="{tx_positions[1]-40}" y="650" width="80" height="90" class="transformer-box"/>
<text x="{tx_positions[1]}" y="750" class="equipment-label" text-anchor="middle">TX-2</text>
<text x="{tx_positions[1]}" y="770" class="rating" text-anchor="middle">2,500 kVA</text>
<text x="{tx_positions[1]}" y="785" class="rating" text-anchor="middle">10kV/400V</text>

<line x1="{tx_positions[1]}" y1="717" x2="{tx_positions[1]}" y2="800" class="power-line"/>
<use href="#breaker-closed" x="{tx_positions[1]}" y="760"/>
<text x="{tx_positions[1]+25}" y="765" class="rating">CB-T2 (N.C.)</text>

<!-- ===================================================================== -->
<!--                    LV SWITCHBOARDS (400V)                             -->
<!-- ===================================================================== -->

<!-- LV-SWBD-A -->
<line x1="{tx_positions[0]}" y1="800" x2="{tx_positions[0]}" y2="850" class="power-line"/>
<line x1="{tx_positions[0]}" y1="850" x2="{lv_positions[0]}" y2="850" class="power-line"/>
<line x1="{lv_positions[0]}" y1="850" x2="{lv_positions[0]}" y2="900" class="power-line"/>
<use href="#breaker-closed" x="{lv_positions[0]}" y="875"/>
<text x="{lv_positions[0]+25}" y="880" class="rating">CB-L1 (N.C.)</text>

<rect x="{lv_positions[0]-100}" y="900" width="200" height="100" class="lv-switchboard"/>
<line x1="{lv_positions[0]-85}" y1="915" x2="{lv_positions[0]+85}" y2="915" class="bus"/>

<text x="{lv_positions[0]}" y="945" class="equipment-label" text-anchor="middle">LV-SWBD-A</text>
<text x="{lv_positions[0]}" y="965" class="rating" text-anchor="middle">400V | 3-Phase | 50 Hz</text>
<text x="{lv_positions[0]}" y="980" class="rating" text-anchor="middle">2,000A | 5 Positions</text>

<!-- LV-SWBD-B -->
<line x1="{tx_positions[1]}" y1="800" x2="{tx_positions[1]}" y2="850" class="power-line"/>
<line x1="{tx_positions[1]}" y1="850" x2="{lv_positions[1]}" y2="850" class="power-line"/>
<line x1="{lv_positions[1]}" y1="850" x2="{lv_positions[1]}" y2="900" class="power-line"/>
<use href="#breaker-closed" x="{lv_positions[1]}" y="875"/>
<text x="{lv_positions[1]+25}" y="880" class="rating">CB-L2 (N.C.)</text>

<rect x="{lv_positions[1]-100}" y="900" width="200" height="100" class="lv-switchboard"/>
<line x1="{lv_positions[1]-85}" y1="915" x2="{lv_positions[1]+85}" y2="915" class="bus"/>

<text x="{lv_positions[1]}" y="945" class="equipment-label" text-anchor="middle">LV-SWBD-B</text>
<text x="{lv_positions[1]}" y="965" class="rating" text-anchor="middle">400V | 3-Phase | 50 Hz</text>
<text x="{lv_positions[1]}" y="980" class="rating" text-anchor="middle">2,000A | 5 Positions</text>

<!-- ===================================================================== -->
<!--                    DOWNSTREAM DISTRIBUTION                            -->
<!-- ===================================================================== -->

<!-- Distribution from LV-A -->
<line x1="{lv_positions[0]-50}" y1="1000" x2="{lv_positions[0]-50}" y2="1060" class="power-line"/>
<use href="#breaker-closed" x="{lv_positions[0]-50}" y="1030"/>
<text x="{lv_positions[0]-25}" y="1035" class="rating">CB-DP1 (N.C.)</text>

<rect x="{lv_positions[0]-95}" y="1060" width="90" height="60" class="dist-panel"/>
<text x="{lv_positions[0]-50}" y="1085" class="equipment-label" text-anchor="middle">DP-A-IT</text>
<text x="{lv_positions[0]-50}" y="1105" class="rating" text-anchor="middle">IT Loads</text>

<line x1="{lv_positions[0]+50}" y1="1000" x2="{lv_positions[0]+50}" y2="1060" class="power-line"/>
<use href="#breaker-closed" x="{lv_positions[0]+50}" y="1030"/>
<text x="{lv_positions[0]+75}" y="1035" class="rating">CB-DP2 (N.C.)</text>

<rect x="{lv_positions[0]+5}" y="1060" width="90" height="60" class="dist-panel"/>
<text x="{lv_positions[0]+50}" y="1085" class="equipment-label" text-anchor="middle">DP-A-MEP</text>
<text x="{lv_positions[0]+50}" y="1105" class="rating" text-anchor="middle">MEP Loads</text>

<!-- Distribution from LV-B -->
<line x1="{lv_positions[1]-50}" y1="1000" x2="{lv_positions[1]-50}" y2="1060" class="power-line"/>
<use href="#breaker-closed" x="{lv_positions[1]-50}" y="1030"/>
<text x="{lv_positions[1]-25}" y="1035" class="rating">CB-DP3 (N.C.)</text>

<rect x="{lv_positions[1]-95}" y="1060" width="90" height="60" class="dist-panel"/>
<text x="{lv_positions[1]-50}" y="1085" class="equipment-label" text-anchor="middle">DP-B-IT</text>
<text x="{lv_positions[1]-50}" y="1105" class="rating" text-anchor="middle">IT Loads</text>

<line x1="{lv_positions[1]+50}" y1="1000" x2="{lv_positions[1]+50}" y2="1060" class="power-line"/>
<use href="#breaker-closed" x="{lv_positions[1]+50}" y="1030"/>
<text x="{lv_positions[1]+75}" y="1035" class="rating">CB-DP4 (N.C.)</text>

<rect x="{lv_positions[1]+5}" y="1060" width="90" height="60" class="dist-panel"/>
<text x="{lv_positions[1]+50}" y="1085" class="equipment-label" text-anchor="middle">DP-B-MEP</text>
<text x="{lv_positions[1]+50}" y="1105" class="rating" text-anchor="middle">MEP Loads</text>

<!-- IT Equipment Box -->
<rect x="{WIDTH/2-250}" y="1180" width="500" height="80" fill="#F5F5F5" stroke="black" stroke-width="2"/>
<text x="{WIDTH/2}" y="1215" class="equipment-label" text-anchor="middle">IT EQUIPMENT</text>
<text x="{WIDTH/2}" y="1235" class="rating" text-anchor="middle">Dual-Corded Servers | 5.0 MW Critical Load</text>

<!-- Connections to IT Equipment -->
<line x1="{lv_positions[0]-50}" y1="1120" x2="{lv_positions[0]-50}" y2="1160" class="power-line"/>
<line x1="{lv_positions[0]-50}" y1="1160" x2="{WIDTH/2-100}" y2="1160" class="power-line"/>
<line x1="{WIDTH/2-100}" y1="1160" x2="{WIDTH/2-100}" y2="1180" class="power-line"/>

<line x1="{lv_positions[1]-50}" y1="1120" x2="{lv_positions[1]-50}" y2="1160" class="power-line"/>
<line x1="{lv_positions[1]-50}" y1="1160" x2="{WIDTH/2+100}" y2="1160" class="power-line"/>
<line x1="{WIDTH/2+100}" y1="1160" x2="{WIDTH/2+100}" y2="1180" class="power-line"/>

<!-- Notes Section -->
<rect x="50" y="1350" width="700" height="200" fill="#FFFEF0" stroke="black" stroke-width="1"/>
<text x="60" y="1375" class="subtitle">NOTES:</text>
<text x="60" y="1395" class="annotation">1. Dual-feed topology with N+1 transformer redundancy</text>
<text x="60" y="1413" class="annotation">2. All breakers shown in normal operating position</text>
<text x="60" y="1431" class="annotation">3. MV tie breaker normally open (N.O.) for selective operation</text>
<text x="60" y="1449" class="annotation">4. Power flow: TOP to BOTTOM per IEEE conventions</text>
<text x="60" y="1467" class="annotation">5. Symmetrical equipment spacing calculated per SLD Standards v1.1</text>
<text x="60" y="1485" class="annotation">6. Open Sans font hierarchy: 24px (titles) / 14px (equipment) / 11px (specs)</text>
<text x="60" y="1503" class="annotation">7. Text clearance: 15px from lines, 10px from equipment boundaries</text>
<text x="60" y="1521" class="annotation">8. IEEE Std 315 / IEC 60617 compliant symbols</text>

<!-- Equipment Summary -->
<rect x="800" y="1350" width="750" height="200" fill="#FFFEF0" stroke="black" stroke-width="1"/>
<text x="810" y="1375" class="subtitle">EQUIPMENT SUMMARY:</text>
<text x="810" y="1395" class="annotation">Utility Sources:      2 × 3 MW @ 10 kV (dual feeds)</text>
<text x="810" y="1413" class="annotation">MV Switchboards:      2 × 630A @ 10 kV (40 kA SCCR)</text>
<text x="810" y="1431" class="annotation">Transformers:         2 × 2,500 kVA (10kV/400V) - N+1 redundancy</text>
<text x="810" y="1449" class="annotation">LV Switchboards:      2 × 2,000A @ 400V (5 positions each)</text>
<text x="810" y="1467" class="annotation">Distribution Panels:  4 panels (2 IT, 2 MEP)</text>
<text x="810" y="1485" class="annotation">IT Load:              5.0 MW (dual-corded)</text>
<text x="810" y="1503" class="annotation">Redundancy:           N+1 at all levels</text>
<text x="810" y="1521" class="annotation">Standards:            SLD Standards v1.1.1 compliant</text>

<!-- Footer -->
<text x="{WIDTH/2}" y="{HEIGHT-30}" class="rating" text-anchor="middle">SLD STANDARDS TEST | IEEE 315 / IEC 60617 | Open Sans Typography | Generated {datetime.now().strftime('%Y-%m-%d %H:%M')}</text>

</svg>'''

    # Basic validation
    assert '<?xml' in svg, "❌ XML declaration missing"
    assert '<svg' in svg, "❌ SVG tag missing"
    assert 'Open Sans' in svg, "❌ Open Sans fonts not in SVG"
    assert 'breaker-closed' in svg, "❌ Breaker symbol reference not in SVG"

    # Save test SVG
    with open('test_standards_output.svg', 'w', encoding='utf-8') as f:
        f.write(svg)

    print("✓ Complete SVG generated successfully")
    print(f"  Output: test_standards_output.svg ({len(svg):,} bytes)")

    print("\n" + "=" * 80)
    print("ALL TESTS PASSED ✓")
    print("=" * 80)
    print("\nSLD Standards Module Status:")
    print("  ✓ CSS styles with Open Sans fonts")
    print("  ✓ IEEE Std 315 symbols")
    print("  ✓ Symmetrical positioning function")
    print("  ✓ Text style hierarchy (24px/14px/11px)")
    print("  ✓ Equipment and layout constants")
    print("\nThe module is ready for use in SLD generators!")

if __name__ == '__main__':
    test_standards_integration()
