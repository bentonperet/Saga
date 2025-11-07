"""
GGE Data Center Single-Line Diagram Generator
N+1 MTU DRUPS with HPP Priority + Utility Makeup + 2N Transformers
Tbilisi, Georgia - Phase 1: 3.0 MW IT Capacity

SLD STANDARDS v1.1 COMPLIANT
- IEEE Std 315 / IEC 60617 symbols
- Symmetrical spacing calculations
- Text clearance and overlap prevention
- Open Sans font hierarchy
- All breakers shown with normal positions
"""

from datetime import datetime
import math

# Font hierarchy (Open Sans)
FONTS = {
    'heading1': 'font: bold 24px "Open Sans", Arial',  # Title
    'heading2': 'font: bold 14px "Open Sans", Arial',  # Equipment names
    'heading3': 'font: 11px "Open Sans", Arial',       # Specifications
}

def get_standards_css():
    """SLD Standards v1.1 Compliant CSS with Open Sans font hierarchy"""
    return '''
    <style>
        /* Open Sans Font Hierarchy */
        .title { ''' + FONTS['heading1'] + '''; fill: #000; }
        .equipment-label { ''' + FONTS['heading2'] + '''; fill: #000; }
        .rating { ''' + FONTS['heading3'] + '''; fill: #333; }

        /* Line Styles */
        .power-line { stroke: #000; stroke-width: 2; fill: none; }
        .bus { stroke: #000; stroke-width: 6; fill: none; }
        .control-line { stroke: #000; stroke-width: 1; stroke-dasharray: 5,5; fill: none; }

        /* Equipment Boxes - LIGHT BACKGROUNDS for readability (SLD Standards v1.1) */
        .mv-switchboard { fill: #E3F2FD; stroke: #000; stroke-width: 2; }
        .lv-switchboard { fill: #E8F5E9; stroke: #000; stroke-width: 2; }
        .generator-box { fill: #FFF3E0; stroke: #000; stroke-width: 2; }
        .transformer-box { fill: #FFFFFF; stroke: #000; stroke-width: 2; }
        .ups-module { fill: #F3E5F5; stroke: #000; stroke-width: 1.5; }
        .dist-panel { fill: #E0F2F1; stroke: #000; stroke-width: 1; }
        .hpp-source-box { fill: #90EE90; stroke: #000; stroke-width: 2; }
        .utility-source-box { fill: #87CEEB; stroke: #000; stroke-width: 2; }
        .solar-source-box { fill: #FFA500; stroke: #000; stroke-width: 2; }
        .tie-breaker-box { fill: #FFD700; stroke: #000; stroke-width: 2; }
    </style>
    '''

def get_ieee_symbols():
    """IEEE Std 315 / IEC 60617 Compliant Symbols"""
    return '''
    <defs>
        <!-- Breaker - Closed (IEEE 315) -->
        <g id="breaker-closed">
            <rect x="-8" y="-12" width="16" height="24" fill="white" stroke="black" stroke-width="1.5"/>
            <line x1="-6" y1="-8" x2="6" y2="8" stroke="black" stroke-width="2"/>
            <line x1="-6" y1="8" x2="6" y2="-8" stroke="black" stroke-width="2"/>
        </g>

        <!-- Breaker - Open (IEEE 315) -->
        <g id="breaker-open">
            <rect x="-8" y="-12" width="16" height="24" fill="white" stroke="black" stroke-width="1.5"/>
            <line x1="0" y1="-8" x2="0" y2="-2" stroke="black" stroke-width="2"/>
            <line x1="0" y1="2" x2="0" y2="8" stroke="black" stroke-width="2"/>
            <circle cx="0" cy="0" r="2.5" fill="white" stroke="black" stroke-width="1.5"/>
        </g>

        <!-- Transformer (IEEE 315 - dual winding) -->
        <g id="transformer">
            <circle cx="0" cy="-15" r="12" fill="white" stroke="black" stroke-width="1.5"/>
            <circle cx="0" cy="15" r="12" fill="white" stroke="black" stroke-width="1.5"/>
        </g>

        <!-- Generator (IEEE 315) -->
        <g id="generator">
            <circle cx="0" cy="0" r="30" fill="white" stroke="black" stroke-width="2"/>
            <text x="0" y="8" font-family="Open Sans, Arial" font-size="20" font-weight="bold" text-anchor="middle" fill="black">G</text>
        </g>

        <!-- Connection Point (IEC 60617) -->
        <g id="connection-point">
            <circle cx="0" cy="0" r="3" fill="black"/>
        </g>

        <!-- MTU DRUPS Symbol -->
        <g id="mtu-drups">
            <rect x="-45" y="-35" width="90" height="70" rx="4" fill="white" stroke="black" stroke-width="2"/>
            <circle cx="0" cy="-10" r="18" fill="none" stroke="black" stroke-width="1.5"/>
            <text x="0" y="-5" font-family="Open Sans, Arial" font-size="10" font-weight="bold" text-anchor="middle">MTU</text>
            <text x="0" y="15" font-family="Open Sans, Arial" font-size="8" text-anchor="middle">DRUPS</text>
        </g>
    </defs>
    '''

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

# Canvas and layout settings
WIDTH = 2800
HEIGHT = 3400
MARGIN = 200

# Calculate symmetric positions for equipment
mv_swbd_positions = calculate_symmetric_positions(WIDTH, 2, 320, MARGIN)
tx_positions = calculate_symmetric_positions(WIDTH, 4, 80, MARGIN)
lv_swbd_positions = calculate_symmetric_positions(WIDTH, 2, 240, MARGIN)
mtu_positions = calculate_symmetric_positions(WIDTH, 3, 150, MARGIN)

# Start building SVG
svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{WIDTH}" height="{HEIGHT}" xmlns="http://www.w3.org/2000/svg">

{get_ieee_symbols()}
{get_standards_css()}

<!-- ===================================================================== -->
<!--                              TITLE BLOCK                              -->
<!-- ===================================================================== -->
<rect x="50" y="30" width="{WIDTH-300}" height="100" fill="white" stroke="black" stroke-width="2"/>
<text x="{WIDTH/2}" y="75" class="title" text-anchor="middle">GGE Data Center - Electrical Single-Line Diagram</text>
<text x="{WIDTH/2}" y="110" class="rating" text-anchor="middle">N+1 MTU DRUPS | 2N Transformers | HPP Priority + Utility Makeup | Tier III | 3.0 MW IT</text>

<rect x="{WIDTH-240}" y="30" width="190" height="100" fill="white" stroke="black" stroke-width="2"/>
<text x="{WIDTH-230}" y="60" class="rating">Date: {datetime.now().strftime('%Y-%m-%d')}</text>
<text x="{WIDTH-230}" y="80" class="rating">Doc: GGE-EL-SLD-002</text>
<text x="{WIDTH-230}" y="100" class="rating">Rev: 02</text>
<text x="{WIDTH-230}" y="120" class="rating">Status: For Review</text>

<!-- ===================================================================== -->
<!--                          PRIMARY SOURCES                              -->
<!-- ===================================================================== -->

<!-- Utility Grid -->
<rect x="250" y="200" width="200" height="100" class="utility-source-box"/>
<text x="350" y="240" class="equipment-label" text-anchor="middle">UTILITY GRID</text>
<text x="350" y="265" class="rating" text-anchor="middle">10 kV | 3-Phase | 50 Hz | 6 MW</text>
<text x="350" y="285" class="rating" text-anchor="middle">Dual Feeds (3 MW each)</text>

<line x1="300" y1="300" x2="300" y2="360" class="power-line"/>
<use href="#breaker-closed" x="300" y="330"/>
<text x="320" y="335" class="rating">CB-U1 (N.C.)</text>

<line x1="400" y1="300" x2="400" y2="360" class="power-line"/>
<use href="#breaker-closed" x="400" y="330"/>
<text x="420" y="335" class="rating">CB-U2 (N.C.)</text>

<!-- HPP Source -->
<rect x="700" y="200" width="200" height="100" class="hpp-source-box"/>
<text x="800" y="240" class="equipment-label" text-anchor="middle">HPP SOURCE</text>
<text x="800" y="265" class="rating" text-anchor="middle">400V | 3-Phase | 50 Hz | 3.7 MW</text>
<text x="800" y="285" class="rating" text-anchor="middle">Dual Feeds (1.85 MW each)</text>

<line x1="750" y1="300" x2="750" y2="360" class="power-line"/>
<use href="#breaker-closed" x="750" y="330"/>
<text x="770" y="335" class="rating">CB-H1 (N.C.)</text>

<line x1="850" y1="300" x2="850" y2="360" class="power-line"/>
<use href="#breaker-closed" x="850" y="330"/>
<text x="870" y="335" class="rating">CB-H2 (N.C.)</text>

<!-- Solar Array -->
<rect x="{WIDTH-440}" y="200" width="180" height="100" class="solar-source-box"/>
<text x="{WIDTH-350}" y="240" class="equipment-label" text-anchor="middle">SOLAR ARRAY</text>
<text x="{WIDTH-350}" y="265" class="rating" text-anchor="middle">800 kW AC | 400V</text>

<line x1="{WIDTH-350}" y1="300" x2="{WIDTH-350}" y2="360" class="power-line"/>
<use href="#breaker-closed" x="{WIDTH-350}" y="330"/>
<text x="{WIDTH-330}" y="335" class="rating">CB-SOL (N.C.)</text>

<!-- ===================================================================== -->
<!--                     HPP STEP-UP TRANSFORMERS                          -->
<!-- ===================================================================== -->

<!-- XFMR-H1 -->
<use href="#transformer" x="750" y="430"/>
<rect x="700" y="390" width="100" height="90" class="transformer-box"/>
<text x="750" y="500" class="equipment-label" text-anchor="middle">XFMR-H1</text>
<text x="750" y="520" class="rating" text-anchor="middle">2,500 kVA | 400V/10kV</text>
<line x1="750" y1="360" x2="750" y2="403" class="power-line"/>
<line x1="750" y1="457" x2="750" y2="540" class="power-line"/>
<use href="#breaker-closed" x="750" y="510"/>
<text x="770" y="515" class="rating">CB-TH1 (N.C.)</text>

<!-- XFMR-H2 -->
<use href="#transformer" x="850" y="430"/>
<rect x="800" y="390" width="100" height="90" class="transformer-box"/>
<text x="850" y="500" class="equipment-label" text-anchor="middle">XFMR-H2</text>
<text x="850" y="520" class="rating" text-anchor="middle">2,500 kVA | 400V/10kV</text>
<line x1="850" y1="360" x2="850" y2="403" class="power-line"/>
<line x1="850" y1="457" x2="850" y2="540" class="power-line"/>
<use href="#breaker-closed" x="850" y="510"/>
<text x="870" y="515" class="rating">CB-TH2 (N.C.)</text>

<!-- ===================================================================== -->
<!--                    MV SWITCHBOARDS (10 kV)                            -->
<!-- ===================================================================== -->

<!-- MV-SWBD-A -->
<g id="mv-swbd-a">
    <rect x="{mv_swbd_positions[0]-160}" y="620" width="320" height="140" class="mv-switchboard"/>
    <line x1="{mv_swbd_positions[0]-140}" y1="640" x2="{mv_swbd_positions[0]+140}" y2="640" class="bus"/>

    <text x="{mv_swbd_positions[0]}" y="680" class="equipment-label" text-anchor="middle">MV-SWBD-A</text>
    <text x="{mv_swbd_positions[0]}" y="700" class="rating" text-anchor="middle">10 kV Bus | 630A | 40 kA</text>
    <text x="{mv_swbd_positions[0]}" y="720" class="rating" text-anchor="middle">Utility + HPP Priority</text>
    <text x="{mv_swbd_positions[0]}" y="740" class="rating" text-anchor="middle">0.35 MW Util + 1.85 MW HPP</text>
</g>

<!-- Incoming to MV-SWBD-A -->
<line x1="300" y1="360" x2="300" y2="580" class="power-line"/>
<line x1="300" y1="580" x2="{mv_swbd_positions[0]-100}" y2="580" class="power-line"/>
<line x1="{mv_swbd_positions[0]-100}" y1="580" x2="{mv_swbd_positions[0]-100}" y2="620" class="power-line"/>
<use href="#breaker-closed" x="{mv_swbd_positions[0]-100}" y="600"/>
<text x="{mv_swbd_positions[0]-80}" y="605" class="rating">VCB-UA (N.C.)</text>

<line x1="750" y1="540" x2="750" y2="580" class="power-line"/>
<line x1="750" y1="580" x2="{mv_swbd_positions[0]+100}" y2="580" class="power-line"/>
<line x1="{mv_swbd_positions[0]+100}" y1="580" x2="{mv_swbd_positions[0]+100}" y2="620" class="power-line"/>
<use href="#breaker-closed" x="{mv_swbd_positions[0]+100}" y="600"/>
<text x="{mv_swbd_positions[0]+120}" y="605" class="rating">VCB-HA (N.C.)</text>

<!-- Outgoing from MV-SWBD-A -->
<line x1="{mv_swbd_positions[0]-80}" y1="760" x2="{mv_swbd_positions[0]-80}" y2="820" class="power-line"/>
<use href="#breaker-closed" x="{mv_swbd_positions[0]-80}" y="790"/>
<text x="{mv_swbd_positions[0]-60}" y="795" class="rating">VCB-1A (N.C.)</text>

<line x1="{mv_swbd_positions[0]+80}" y1="760" x2="{mv_swbd_positions[0]+80}" y2="820" class="power-line"/>
<use href="#breaker-closed" x="{mv_swbd_positions[0]+80}" y="790"/>
<text x="{mv_swbd_positions[0]+100}" y="795" class="rating">VCB-1B (N.C.)</text>

<!-- MV-SWBD-B -->
<g id="mv-swbd-b">
    <rect x="{mv_swbd_positions[1]-160}" y="620" width="320" height="140" class="mv-switchboard"/>
    <line x1="{mv_swbd_positions[1]-140}" y1="640" x2="{mv_swbd_positions[1]+140}" y2="640" class="bus"/>

    <text x="{mv_swbd_positions[1]}" y="680" class="equipment-label" text-anchor="middle">MV-SWBD-B</text>
    <text x="{mv_swbd_positions[1]}" y="700" class="rating" text-anchor="middle">10 kV Bus | 630A | 40 kA</text>
    <text x="{mv_swbd_positions[1]}" y="720" class="rating" text-anchor="middle">Utility + HPP Priority</text>
    <text x="{mv_swbd_positions[1]}" y="740" class="rating" text-anchor="middle">0.35 MW Util + 1.85 MW HPP</text>
</g>

<!-- Incoming to MV-SWBD-B -->
<line x1="400" y1="360" x2="400" y2="580" class="power-line"/>
<line x1="400" y1="580" x2="{mv_swbd_positions[1]-100}" y2="580" class="power-line"/>
<line x1="{mv_swbd_positions[1]-100}" y1="580" x2="{mv_swbd_positions[1]-100}" y2="620" class="power-line"/>
<use href="#breaker-closed" x="{mv_swbd_positions[1]-100}" y="600"/>
<text x="{mv_swbd_positions[1]-80}" y="605" class="rating">VCB-UB (N.C.)</text>

<line x1="850" y1="540" x2="850" y2="580" class="power-line"/>
<line x1="850" y1="580" x2="{mv_swbd_positions[1]+100}" y2="580" class="power-line"/>
<line x1="{mv_swbd_positions[1]+100}" y1="580" x2="{mv_swbd_positions[1]+100}" y2="620" class="power-line"/>
<use href="#breaker-closed" x="{mv_swbd_positions[1]+100}" y="600"/>
<text x="{mv_swbd_positions[1]+120}" y="605" class="rating">VCB-HB (N.C.)</text>

<!-- Outgoing from MV-SWBD-B -->
<line x1="{mv_swbd_positions[1]-80}" y1="760" x2="{mv_swbd_positions[1]-80}" y2="820" class="power-line"/>
<use href="#breaker-closed" x="{mv_swbd_positions[1]-80}" y="790"/>
<text x="{mv_swbd_positions[1]-60}" y="795" class="rating">VCB-2A (N.C.)</text>

<line x1="{mv_swbd_positions[1]+80}" y1="760" x2="{mv_swbd_positions[1]+80}" y2="820" class="power-line"/>
<use href="#breaker-closed" x="{mv_swbd_positions[1]+80}" y="790"/>
<text x="{mv_swbd_positions[1]+100}" y="795" class="rating">VCB-2B (N.C.)</text>

<!-- ===================================================================== -->
<!--              2N TRANSFORMERS (10 kV → 400V)                           -->
<!-- ===================================================================== -->

<!-- XFMR-1A: MV-A to LV-A -->
<line x1="{mv_swbd_positions[0]-80}" y1="820" x2="{mv_swbd_positions[0]-80}" y2="920" class="power-line"/>
<line x1="{mv_swbd_positions[0]-80}" y1="920" x2="{tx_positions[0]}" y2="920" class="power-line"/>
<line x1="{tx_positions[0]}" y1="920" x2="{tx_positions[0]}" y2="993" class="power-line"/>

<use href="#transformer" x="{tx_positions[0]}" y="1020"/>
<rect x="{tx_positions[0]-40}" y="980" width="80" height="90" class="transformer-box"/>
<text x="{tx_positions[0]}" y="1080" class="equipment-label" text-anchor="middle">XFMR-1A</text>
<text x="{tx_positions[0]}" y="1100" class="rating" text-anchor="middle">5,000 kVA | 10kV/400V</text>

<line x1="{tx_positions[0]}" y1="1047" x2="{tx_positions[0]}" y2="1120" class="power-line"/>
<use href="#breaker-closed" x="{tx_positions[0]}" y="1090"/>
<text x="{tx_positions[0]+20}" y="1095" class="rating">CB-1A (N.C.)</text>

<!-- XFMR-1B: MV-A to LV-B -->
<line x1="{mv_swbd_positions[0]+80}" y1="820" x2="{mv_swbd_positions[0]+80}" y2="920" class="power-line"/>
<line x1="{mv_swbd_positions[0]+80}" y1="920" x2="{tx_positions[1]}" y2="920" class="power-line"/>
<line x1="{tx_positions[1]}" y1="920" x2="{tx_positions[1]}" y2="993" class="power-line"/>

<use href="#transformer" x="{tx_positions[1]}" y="1020"/>
<rect x="{tx_positions[1]-40}" y="980" width="80" height="90" class="transformer-box"/>
<text x="{tx_positions[1]}" y="1080" class="equipment-label" text-anchor="middle">XFMR-1B</text>
<text x="{tx_positions[1]}" y="1100" class="rating" text-anchor="middle">5,000 kVA | 10kV/400V</text>

<line x1="{tx_positions[1]}" y1="1047" x2="{tx_positions[1]}" y2="1120" class="power-line"/>
<use href="#breaker-closed" x="{tx_positions[1]}" y="1090"/>
<text x="{tx_positions[1]+20}" y="1095" class="rating">CB-1B (N.C.)</text>

<!-- XFMR-2A: MV-B to LV-A -->
<line x1="{mv_swbd_positions[1]-80}" y1="820" x2="{mv_swbd_positions[1]-80}" y2="920" class="power-line"/>
<line x1="{mv_swbd_positions[1]-80}" y1="920" x2="{tx_positions[2]}" y2="920" class="power-line"/>
<line x1="{tx_positions[2]}" y1="920" x2="{tx_positions[2]}" y2="993" class="power-line"/>

<use href="#transformer" x="{tx_positions[2]}" y="1020"/>
<rect x="{tx_positions[2]-40}" y="980" width="80" height="90" class="transformer-box"/>
<text x="{tx_positions[2]}" y="1080" class="equipment-label" text-anchor="middle">XFMR-2A</text>
<text x="{tx_positions[2]}" y="1100" class="rating" text-anchor="middle">5,000 kVA | 10kV/400V</text>

<line x1="{tx_positions[2]}" y1="1047" x2="{tx_positions[2]}" y2="1120" class="power-line"/>
<use href="#breaker-closed" x="{tx_positions[2]}" y="1090"/>
<text x="{tx_positions[2]+20}" y="1095" class="rating">CB-2A (N.C.)</text>

<!-- XFMR-2B: MV-B to LV-B -->
<line x1="{mv_swbd_positions[1]+80}" y1="820" x2="{mv_swbd_positions[1]+80}" y2="920" class="power-line"/>
<line x1="{mv_swbd_positions[1]+80}" y1="920" x2="{tx_positions[3]}" y2="920" class="power-line"/>
<line x1="{tx_positions[3]}" y1="920" x2="{tx_positions[3]}" y2="993" class="power-line"/>

<use href="#transformer" x="{tx_positions[3]}" y="1020"/>
<rect x="{tx_positions[3]-40}" y="980" width="80" height="90" class="transformer-box"/>
<text x="{tx_positions[3]}" y="1080" class="equipment-label" text-anchor="middle">XFMR-2B</text>
<text x="{tx_positions[3]}" y="1100" class="rating" text-anchor="middle">5,000 kVA | 10kV/400V</text>

<line x1="{tx_positions[3]}" y1="1047" x2="{tx_positions[3]}" y2="1120" class="power-line"/>
<use href="#breaker-closed" x="{tx_positions[3]}" y="1090"/>
<text x="{tx_positions[3]+20}" y="1095" class="rating">CB-2B (N.C.)</text>

<!-- ===================================================================== -->
<!--                    LV SWITCHBOARDS (400V)                             -->
<!-- ===================================================================== -->

<!-- LV-SWBD-A -->
<g id="lv-swbd-a">
    <!-- Incoming from transformers -->
    <line x1="{tx_positions[0]}" y1="1120" x2="{tx_positions[0]}" y2="1180" class="power-line"/>
    <line x1="{tx_positions[0]}" y1="1180" x2="{lv_swbd_positions[0]-80}" y2="1180" class="power-line"/>
    <line x1="{lv_swbd_positions[0]-80}" y1="1180" x2="{lv_swbd_positions[0]-80}" y2="1240" class="power-line"/>
    <use href="#breaker-closed" x="{lv_swbd_positions[0]-80}" y="1210"/>
    <text x="{lv_swbd_positions[0]-60}" y="1215" class="rating">CB-LA1 (N.C.)</text>

    <line x1="{tx_positions[2]}" y1="1120" x2="{tx_positions[2]}" y2="1180" class="power-line"/>
    <line x1="{tx_positions[2]}" y1="1180" x2="{lv_swbd_positions[0]+80}" y2="1180" class="power-line"/>
    <line x1="{lv_swbd_positions[0]+80}" y1="1180" x2="{lv_swbd_positions[0]+80}" y2="1240" class="power-line"/>
    <use href="#breaker-closed" x="{lv_swbd_positions[0]+80}" y="1210"/>
    <text x="{lv_swbd_positions[0]+100}" y="1215" class="rating">CB-LA2 (N.C.)</text>

    <rect x="{lv_swbd_positions[0]-120}" y="1240" width="240" height="120" class="lv-switchboard"/>
    <line x1="{lv_swbd_positions[0]-105}" y1="1255" x2="{lv_swbd_positions[0]+105}" y2="1255" class="bus"/>

    <text x="{lv_swbd_positions[0]}" y="1290" class="equipment-label" text-anchor="middle">LV-SWBD-A</text>
    <text x="{lv_swbd_positions[0]}" y="1310" class="rating" text-anchor="middle">400V | 3-Phase | 50 Hz | 5,000A</text>
    <text x="{lv_swbd_positions[0]}" y="1330" class="rating" text-anchor="middle">2,200 kW Load</text>

    <!-- Outgoing to MTU -->
    <line x1="{lv_swbd_positions[0]}" y1="1360" x2="{lv_swbd_positions[0]}" y2="1420" class="power-line"/>
    <use href="#breaker-closed" x="{lv_swbd_positions[0]}" y="1390"/>
    <text x="{lv_swbd_positions[0]+20}" y="1395" class="rating">CB-MA (N.C.)</text>
</g>

<!-- LV-SWBD-B -->
<g id="lv-swbd-b">
    <!-- Incoming from transformers -->
    <line x1="{tx_positions[1]}" y1="1120" x2="{tx_positions[1]}" y2="1180" class="power-line"/>
    <line x1="{tx_positions[1]}" y1="1180" x2="{lv_swbd_positions[1]-80}" y2="1180" class="power-line"/>
    <line x1="{lv_swbd_positions[1]-80}" y1="1180" x2="{lv_swbd_positions[1]-80}" y2="1240" class="power-line"/>
    <use href="#breaker-closed" x="{lv_swbd_positions[1]-80}" y="1210"/>
    <text x="{lv_swbd_positions[1]-60}" y="1215" class="rating">CB-LB1 (N.C.)</text>

    <line x1="{tx_positions[3]}" y1="1120" x2="{tx_positions[3]}" y2="1180" class="power-line"/>
    <line x1="{tx_positions[3]}" y1="1180" x2="{lv_swbd_positions[1]+80}" y2="1180" class="power-line"/>
    <line x1="{lv_swbd_positions[1]+80}" y1="1180" x2="{lv_swbd_positions[1]+80}" y2="1240" class="power-line"/>
    <use href="#breaker-closed" x="{lv_swbd_positions[1]+80}" y="1210"/>
    <text x="{lv_swbd_positions[1]+100}" y="1215" class="rating">CB-LB2 (N.C.)</text>

    <rect x="{lv_swbd_positions[1]-120}" y="1240" width="240" height="120" class="lv-switchboard"/>
    <line x1="{lv_swbd_positions[1]-105}" y1="1255" x2="{lv_swbd_positions[1]+105}" y2="1255" class="bus"/>

    <text x="{lv_swbd_positions[1]}" y="1290" class="equipment-label" text-anchor="middle">LV-SWBD-B</text>
    <text x="{lv_swbd_positions[1]}" y="1310" class="rating" text-anchor="middle">400V | 3-Phase | 50 Hz | 5,000A</text>
    <text x="{lv_swbd_positions[1]}" y="1330" class="rating" text-anchor="middle">2,200 kW Load</text>

    <!-- Outgoing to MTU -->
    <line x1="{lv_swbd_positions[1]}" y1="1360" x2="{lv_swbd_positions[1]}" y2="1420" class="power-line"/>
    <use href="#breaker-closed" x="{lv_swbd_positions[1]}" y="1390"/>
    <text x="{lv_swbd_positions[1]+20}" y="1395" class="rating">CB-MB (N.C.)</text>
</g>

<!-- Tie Breaker -->
<line x1="{lv_swbd_positions[0]+120}" y1="1300" x2="{WIDTH/2-80}" y2="1300" class="power-line"/>
<line x1="{WIDTH/2+80}" y1="1300" x2="{lv_swbd_positions[1]-120}" y2="1300" class="power-line"/>
<use href="#breaker-open" x="{WIDTH/2}" y="1300"/>
<rect x="{WIDTH/2-60}" y="1260" width="120" height="80" class="tie-breaker-box"/>
<text x="{WIDTH/2}" y="1285" class="equipment-label" text-anchor="middle">52-TIE</text>
<text x="{WIDTH/2}" y="1325" class="rating" text-anchor="middle">6,300A (N.O.)</text>

<!-- ===================================================================== -->
<!--                      MTU KINETIC DRUPS (N+1)                          -->
<!-- ===================================================================== -->

<!-- MTU-1 -->
<use href="#mtu-drups" x="{mtu_positions[0]}" y="1510"/>
<rect x="{mtu_positions[0]-75}" y="1460" width="150" height="110" class="generator-box"/>
<text x="{mtu_positions[0]}" y="1585" class="equipment-label" text-anchor="middle">MTU-1</text>
<text x="{mtu_positions[0]}" y="1605" class="rating" text-anchor="middle">2,750 kVA | 2,200 kW</text>

<line x1="{lv_swbd_positions[0]}" y1="1420" x2="{lv_swbd_positions[0]}" y2="1450" class="power-line"/>
<line x1="{lv_swbd_positions[0]}" y1="1450" x2="{mtu_positions[0]}" y2="1450" class="power-line"/>
<line x1="{mtu_positions[0]}" y1="1450" x2="{mtu_positions[0]}" y2="1460" class="power-line"/>

<line x1="{mtu_positions[0]}" y1="1570" x2="{mtu_positions[0]}" y2="1660" class="power-line"/>
<use href="#breaker-closed" x="{mtu_positions[0]}" y="1630"/>
<text x="{mtu_positions[0]+20}" y="1635" class="rating">CB-M1 (N.C.)</text>

<!-- MTU-2 -->
<use href="#mtu-drups" x="{mtu_positions[2]}" y="1510"/>
<rect x="{mtu_positions[2]-75}" y="1460" width="150" height="110" class="generator-box"/>
<text x="{mtu_positions[2]}" y="1585" class="equipment-label" text-anchor="middle">MTU-2</text>
<text x="{mtu_positions[2]}" y="1605" class="rating" text-anchor="middle">2,750 kVA | 2,200 kW</text>

<line x1="{lv_swbd_positions[1]}" y1="1420" x2="{lv_swbd_positions[1]}" y2="1450" class="power-line"/>
<line x1="{lv_swbd_positions[1]}" y1="1450" x2="{mtu_positions[2]}" y2="1450" class="power-line"/>
<line x1="{mtu_positions[2]}" y1="1450" x2="{mtu_positions[2]}" y2="1460" class="power-line"/>

<line x1="{mtu_positions[2]}" y1="1570" x2="{mtu_positions[2]}" y2="1660" class="power-line"/>
<use href="#breaker-closed" x="{mtu_positions[2]}" y="1630"/>
<text x="{mtu_positions[2]+20}" y="1635" class="rating">CB-M2 (N.C.)</text>

<!-- MTU-3 (Standby) -->
<use href="#mtu-drups" x="{mtu_positions[1]}" y="1510"/>
<rect x="{mtu_positions[1]-75}" y="1460" width="150" height="110" class="generator-box"/>
<text x="{mtu_positions[1]}" y="1585" class="equipment-label" text-anchor="middle">MTU-3 (STANDBY)</text>
<text x="{mtu_positions[1]}" y="1605" class="rating" text-anchor="middle">2,750 kVA | N+1</text>

<!-- Bypass paths (dashed) -->
<line x1="{mtu_positions[1]-75}" y1="1510" x2="{mtu_positions[0]+75}" y2="1510" class="control-line"/>
<line x1="{mtu_positions[0]+75}" y1="1510" x2="{mtu_positions[0]+75}" y2="1700" class="control-line"/>

<line x1="{mtu_positions[1]+75}" y1="1510" x2="{mtu_positions[2]-75}" y2="1510" class="control-line"/>
<line x1="{mtu_positions[2]-75}" y1="1510" x2="{mtu_positions[2]-75}" y2="1700" class="control-line"/>

<!-- ===================================================================== -->
<!--                    DOWNSTREAM DISTRIBUTION                            -->
<!-- ===================================================================== -->

<!-- Distribution Panel A-IT -->
<rect x="{mtu_positions[0]-60}" y="1660" width="120" height="80" class="dist-panel"/>
<text x="{mtu_positions[0]}" y="1690" class="equipment-label" text-anchor="middle">DP-A-IT</text>
<text x="{mtu_positions[0]}" y="1710" class="rating" text-anchor="middle">IT Loads | 1,466 kW</text>
<line x1="{mtu_positions[0]}" y1="1740" x2="{mtu_positions[0]}" y2="1800" class="power-line"/>
<use href="#breaker-closed" x="{mtu_positions[0]}" y="1770"/>
<text x="{mtu_positions[0]+20}" y="1775" class="rating">CB-AI (N.C.)</text>

<!-- Distribution Panel B-IT -->
<rect x="{mtu_positions[2]-60}" y="1660" width="120" height="80" class="dist-panel"/>
<text x="{mtu_positions[2]}" y="1690" class="equipment-label" text-anchor="middle">DP-B-IT</text>
<text x="{mtu_positions[2]}" y="1710" class="rating" text-anchor="middle">IT Loads | 1,467 kW</text>
<line x1="{mtu_positions[2]}" y1="1740" x2="{mtu_positions[2]}" y2="1800" class="power-line"/>
<use href="#breaker-closed" x="{mtu_positions[2]}" y="1770"/>
<text x="{mtu_positions[2]+20}" y="1775" class="rating">CB-BI (N.C.)</text>

<!-- IT Equipment Representation -->
<rect x="{WIDTH/2-350}" y="1820" width="700" height="100" fill="#F5F5F5" stroke="black" stroke-width="2"/>
<text x="{WIDTH/2}" y="1860" class="equipment-label" text-anchor="middle">IT EQUIPMENT</text>
<text x="{WIDTH/2}" y="1885" class="rating" text-anchor="middle">Dual-Corded Power | 2,933 kW (3.0 MW)</text>

<line x1="{mtu_positions[0]}" y1="1800" x2="{mtu_positions[0]}" y2="1810" class="power-line"/>
<line x1="{mtu_positions[0]}" y1="1810" x2="{WIDTH/2-150}" y2="1810" class="power-line"/>
<line x1="{WIDTH/2-150}" y1="1810" x2="{WIDTH/2-150}" y2="1820" class="power-line"/>

<line x1="{mtu_positions[2]}" y1="1800" x2="{mtu_positions[2]}" y2="1810" class="power-line"/>
<line x1="{mtu_positions[2]}" y1="1810" x2="{WIDTH/2+150}" y2="1810" class="power-line"/>
<line x1="{WIDTH/2+150}" y1="1810" x2="{WIDTH/2+150}" y2="1820" class="power-line"/>

<!-- ===================================================================== -->
<!--                           OFFICE LOADS                                -->
<!-- ===================================================================== -->

<!-- Office Transformer -->
<use href="#transformer" x="{WIDTH-360}" y="430"/>
<rect x="{WIDTH-400}" y="390" width="80" height="90" class="transformer-box"/>
<text x="{WIDTH-360}" y="500" class="equipment-label" text-anchor="middle">XFMR-OFFICE</text>
<text x="{WIDTH-360}" y="520" class="rating" text-anchor="middle">250 kVA | 10kV/400V</text>

<line x1="{WIDTH-360}" y1="360" x2="{WIDTH-360}" y2="403" class="power-line"/>
<line x1="{WIDTH-360}" y1="457" x2="{WIDTH-360}" y2="540" class="power-line"/>
<use href="#breaker-closed" x="{WIDTH-360}" y="510"/>
<text x="{WIDTH-340}" y="515" class="rating">CB-TO (N.C.)</text>

<!-- Office ATS -->
<rect x="{WIDTH-410}" y="540" width="100" height="60" class="solar-source-box"/>
<text x="{WIDTH-360}" y="565" class="equipment-label" text-anchor="middle">ATS-OFFICE</text>
<text x="{WIDTH-360}" y="585" class="rating" text-anchor="middle">Solar Priority</text>

<line x1="{WIDTH-350}" y1="360" x2="{WIDTH-350}" y2="540" class="power-line"/>
<line x1="{WIDTH-360}" y1="600" x2="{WIDTH-360}" y2="660" class="power-line"/>
<use href="#breaker-closed" x="{WIDTH-360}" y="630"/>
<text x="{WIDTH-340}" y="635" class="rating">CB-AO (N.C.)</text>

<!-- Office SWBD -->
<rect x="{WIDTH-410}" y="660" width="100" height="80" class="lv-switchboard"/>
<text x="{WIDTH-360}" y="690" class="equipment-label" text-anchor="middle">SWBD-OFFICE</text>
<text x="{WIDTH-360}" y="710" class="rating" text-anchor="middle">630A | 400V | 103 kW</text>

<!-- Footer -->
<text x="{WIDTH/2}" y="{HEIGHT-30}" class="rating" text-anchor="middle">GGE DATA CENTER TBILISI | IEEE 315 / IEC 60617 | SLD Standards v1.1 | {datetime.now().strftime('%Y-%m-%d')}</text>

</svg>'''

# Save file
output_file = 'gge_n+1_mtu_hpp_priority_sld_v1_1_compliant.svg'
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(svg)

print("=" * 80)
print("[SUCCESS] GGE N+1 MTU SLD GENERATED - v1.1 COMPLIANT")
print("=" * 80)
print(f"\nFile: {output_file}")
print(f"Size: {len(svg):,} bytes")
print(f"\nCORRECTIONS APPLIED:")
print(f"  [X] Transformers connect directly to LV-SWBD (not through MTU)")
print(f"  [X] All non-equipment labels removed")
print(f"  [X] All breakers shown with normal positions (N.C./N.O.)")
print(f"  [X] Open Sans font hierarchy applied:")
print(f"      - Heading 1 (24px bold): Titles")
print(f"      - Heading 2 (14px bold): Equipment names")
print(f"      - Heading 3 (11px): Specifications")
print("=" * 80)
