"""
GGE Data Center Single-Line Diagram Generator
N+1 MTU DRUPS with HPP Priority + Utility Makeup + 2N Transformers
Tbilisi, Georgia - Phase 1: 3.0 MW IT Capacity
"""

from datetime import datetime

# SVG setup
width = 2600
height = 3200

# Color scheme
colors = {
    'utility': '#87CEEB',       # Light blue for Utility
    'hpp': '#90EE90',           # Light green for HPP
    'mtu': '#FFB6C1',           # Light pink for MTU
    'solar': '#FFA500',         # Orange for solar
    'tie': '#FFD700',           # Gold for tie breaker
    'xfmr_2n': '#E6E6FA',       # Lavender for 2N transformers
    'line': '#000000',
    'box': '#FFFFFF',
    'text': '#000000'
}

svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
<defs>
    <!-- Step-up Transformer -->
    <g id="transformer-up">
        <circle cx="0" cy="-18" r="15" fill="white" stroke="black" stroke-width="2"/>
        <circle cx="0" cy="18" r="15" fill="white" stroke="black" stroke-width="2"/>
        <text x="0" y="-12" font-family="Arial" font-size="9" text-anchor="middle">400V</text>
        <text x="0" y="24" font-family="Arial" font-size="9" text-anchor="middle">10kV</text>
    </g>

    <!-- Step-down Transformer -->
    <g id="transformer-down">
        <circle cx="0" cy="-18" r="15" fill="white" stroke="black" stroke-width="2"/>
        <circle cx="0" cy="18" r="15" fill="white" stroke="black" stroke-width="2"/>
        <text x="0" y="-12" font-family="Arial" font-size="9" text-anchor="middle">10kV</text>
        <text x="0" y="24" font-family="Arial" font-size="9" text-anchor="middle">400V</text>
    </g>

    <!-- Circuit Breaker -->
    <g id="breaker">
        <rect x="-10" y="-4" width="20" height="8" fill="white" stroke="black" stroke-width="2"/>
        <line x1="-10" y1="0" x2="-18" y2="0" stroke="black" stroke-width="2"/>
        <line x1="10" y1="0" x2="18" y2="0" stroke="black" stroke-width="2"/>
    </g>

    <!-- MTU DRUPS Symbol -->
    <g id="mtu-symbol">
        <rect x="-45" y="-35" width="90" height="70" rx="4" fill="white" stroke="black" stroke-width="2"/>
        <text x="0" y="-12" font-family="Arial" font-size="13" font-weight="bold" text-anchor="middle">MTU DRUPS</text>
        <text x="0" y="5" font-family="Arial" font-size="10" text-anchor="middle">2,750 kVA</text>
        <text x="0" y="20" font-family="Arial" font-size="10" text-anchor="middle">Diesel+Flywheel</text>
    </g>

    <!-- Solar Symbol -->
    <g id="solar-symbol">
        <rect x="-35" y="-25" width="70" height="50" rx="3" fill="white" stroke="black" stroke-width="2"/>
        <text x="0" y="-5" font-family="Arial" font-size="12" font-weight="bold" text-anchor="middle">SOLAR</text>
        <text x="0" y="10" font-family="Arial" font-size="10" text-anchor="middle">800kW AC</text>
    </g>
</defs>

<style>
    .title {{ font: bold 22px Arial; fill: #000; }}
    .subtitle {{ font: bold 17px Arial; fill: #000; }}
    .label {{ font: 12px Arial; fill: #000; }}
    .rating {{ font: 10px Arial; fill: #333; }}
    .bus-label {{ font: bold 15px Arial; fill: #000; }}
    .line {{ stroke: #000; stroke-width: 2.5; fill: none; }}
    .thin-line {{ stroke: #000; stroke-width: 1.5; fill: none; }}
    .dashed-line {{ stroke: #666; stroke-width: 1.5; fill: none; stroke-dasharray: 5,5; }}
    .box {{ fill: white; stroke: black; stroke-width: 2; }}
    .utility-feed {{ fill: {colors['utility']}; stroke: black; stroke-width: 2; }}
    .hpp-feed {{ fill: {colors['hpp']}; stroke: black; stroke-width: 2; }}
    .mtu-feed {{ fill: {colors['mtu']}; stroke: black; stroke-width: 2; }}
    .tie-feed {{ fill: {colors['tie']}; stroke: black; stroke-width: 2; }}
    .solar-feed {{ fill: {colors['solar']}; stroke: black; stroke-width: 2; }}
    .xfmr-2n-feed {{ fill: {colors['xfmr_2n']}; stroke: black; stroke-width: 2; }}
</style>

<!-- Title Block -->
<rect x="50" y="30" width="2500" height="130" fill="white" stroke="black" stroke-width="2"/>
<text x="1300" y="70" class="title" text-anchor="middle">GGE DATA CENTER - TBILISI, GEORGIA</text>
<text x="1300" y="105" class="subtitle" text-anchor="middle">Electrical Single-Line Diagram - N+1 MTU DRUPS with HPP Priority + 2N Transformers</text>
<text x="1300" y="135" class="rating" text-anchor="middle">Phase 1: 3.0 MW IT | 3 x 2,750 kVA MTU (2 Running + 1 Standby) | 4 x 5,000 kVA XFMR (2N) | HPP 3.7 MW + Utility 0.7 MW | Tier III</text>

<!-- Revision Block -->
<g id="revision-block">
    <rect x="2350" y="30" width="200" height="130" fill="white" stroke="black" stroke-width="2"/>
    <text x="2360" y="60" class="label">Date: {datetime.now().strftime('%Y-%m-%d')}</text>
    <text x="2360" y="85" class="label">Doc: GGE-EL-SLD-002</text>
    <text x="2360" y="110" class="label">Rev: 02</text>
    <text x="2360" y="135" class="label">Status: For Review</text>
    <text x="2360" y="155" class="rating">EVS/GGE Engineering</text>
</g>

<!-- ==================================================================================== -->
<!--                          PRIMARY SOURCES                                             -->
<!-- ==================================================================================== -->

<text x="1300" y="220" class="bus-label" text-anchor="middle">PRIMARY POWER SOURCES</text>

<!-- Utility Source -->
<g id="utility-source">
    <rect x="200" y="250" width="220" height="120" class="utility-feed"/>
    <text x="310" y="285" class="bus-label" text-anchor="middle">UTILITY GRID</text>
    <text x="310" y="310" class="label" text-anchor="middle">10 kV, 3Ø, 50Hz</text>
    <text x="310" y="330" class="rating" text-anchor="middle">6 MW Total Capacity</text>
    <text x="310" y="350" class="rating" text-anchor="middle">Dual Feeds (3 MW each)</text>
    <line x1="250" y1="370" x2="250" y2="420" class="line"/>
    <line x1="370" y1="370" x2="370" y2="420" class="line"/>
    <text x="250" y="410" class="rating" text-anchor="middle">Feed 1</text>
    <text x="370" y="410" class="rating" text-anchor="middle">Feed 2</text>
</g>

<!-- HPP Source -->
<g id="hpp-source">
    <rect x="650" y="250" width="220" height="120" class="hpp-feed"/>
    <text x="760" y="285" class="bus-label" text-anchor="middle">HPP SOURCE</text>
    <text x="760" y="310" class="label" text-anchor="middle">400V, 3Ø, 50Hz</text>
    <text x="760" y="330" class="rating" text-anchor="middle">3.7 MW Total Capacity</text>
    <text x="760" y="350" class="rating" text-anchor="middle">Dual Feeds (1.85 MW each)</text>
    <line x1="700" y1="370" x2="700" y2="420" class="line"/>
    <line x1="820" y1="370" x2="820" y2="420" class="line"/>
    <text x="700" y="410" class="rating" text-anchor="middle">Feed 1</text>
    <text x="820" y="410" class="rating" text-anchor="middle">Feed 2</text>
</g>

<!-- Solar Source (Office) -->
<g id="solar-source">
    <rect x="2180" y="250" width="180" height="120" class="solar-feed"/>
    <use href="#solar-symbol" x="2270" y="295"/>
    <text x="2270" y="350" class="label" text-anchor="middle">Solar Array</text>
    <text x="2270" y="365" class="rating" text-anchor="middle">(Office Only)</text>
    <line x1="2270" y1="370" x2="2270" y2="420" class="line"/>
</g>

<!-- ==================================================================================== -->
<!--                          HPP STEP-UP TRANSFORMERS                                    -->
<!-- ==================================================================================== -->

<g id="hpp-step-up-1">
    <use href="#transformer-up" x="700" y="460"/>
    <rect x="640" y="420" width="120" height="80" class="hpp-feed"/>
    <text x="700" y="510" class="label" text-anchor="middle">XFMR-H1</text>
    <text x="700" y="525" class="rating" text-anchor="middle">2,500 kVA</text>
    <text x="700" y="540" class="rating" text-anchor="middle">400V/10kV</text>
    <line x1="700" y1="498" x2="700" y2="580" class="line"/>
</g>

<g id="hpp-step-up-2">
    <use href="#transformer-up" x="820" y="460"/>
    <rect x="760" y="420" width="120" height="80" class="hpp-feed"/>
    <text x="820" y="510" class="label" text-anchor="middle">XFMR-H2</text>
    <text x="820" y="525" class="rating" text-anchor="middle">2,500 kVA</text>
    <text x="820" y="540" class="rating" text-anchor="middle">400V/10kV</text>
    <line x1="820" y1="498" x2="820" y2="580" class="line"/>
</g>

<!-- ==================================================================================== -->
<!--                          MV SWITCHBOARDS (10 kV)                                     -->
<!-- ==================================================================================== -->

<text x="1300" y="630" class="bus-label" text-anchor="middle">MEDIUM VOLTAGE SWITCHBOARDS (10 kV)</text>

<!-- MV-SWBD-A -->
<g id="mv-swbd-a">
    <rect x="150" y="660" width="320" height="200" class="utility-feed"/>
    <text x="310" y="695" class="bus-label" text-anchor="middle">MV-SWBD-A</text>
    <text x="310" y="720" class="label" text-anchor="middle">10 kV Bus | 630A</text>

    <!-- VCB labels -->
    <text x="200" y="750" class="rating">VCB-UA</text>
    <text x="200" y="765" class="rating">(Utility 1)</text>
    <text x="200" y="780" class="rating">N.C.</text>

    <text x="310" y="750" class="rating" text-anchor="middle">HPP Priority:</text>
    <text x="310" y="765" class="rating" text-anchor="middle">Utility 0.35 MW</text>
    <text x="310" y="780" class="rating" text-anchor="middle">HPP 1.85 MW</text>

    <text x="420" y="750" class="rating" text-anchor="end">VCB-HA</text>
    <text x="420" y="765" class="rating" text-anchor="end">(HPP 1)</text>
    <text x="420" y="780" class="rating" text-anchor="end">N.C.</text>
    <text x="420" y="795" class="rating" text-anchor="end" font-weight="bold">AUTO-OPEN</text>
    <text x="420" y="810" class="rating" text-anchor="end" font-weight="bold">on Util Fail</text>

    <!-- Outgoing feeders (2N) -->
    <text x="200" y="835" class="rating" font-size="9">VCB-1A</text>
    <text x="200" y="850" class="rating" font-size="9">to XFMR-1A</text>
    <text x="420" y="835" class="rating" text-anchor="end" font-size="9">VCB-1B</text>
    <text x="420" y="850" class="rating" text-anchor="end" font-size="9">to XFMR-1B</text>

    <!-- Input connections -->
    <line x1="250" y1="580" x2="250" y2="660" class="line"/>
    <circle cx="250" cy="620" r="8" fill="white" stroke="black" stroke-width="2"/>
    <text x="250" y="625" class="rating" text-anchor="middle" font-size="9">VCB</text>

    <line x1="700" y1="580" x2="420" y2="580" class="line"/>
    <line x1="420" y1="580" x2="420" y2="660" class="line"/>
    <circle cx="420" cy="620" r="8" fill="white" stroke="black" stroke-width="2"/>
    <text x="420" y="625" class="rating" text-anchor="middle" font-size="9">VCB</text>

    <!-- Output connections (2 feeders) -->
    <line x1="250" y1="860" x2="250" y2="920" class="line"/>
    <line x1="370" y1="860" x2="370" y2="920" class="line"/>
</g>

<!-- MV-SWBD-B -->
<g id="mv-swbd-b">
    <rect x="1130" y="660" width="320" height="200" class="utility-feed"/>
    <text x="1290" y="695" class="bus-label" text-anchor="middle">MV-SWBD-B</text>
    <text x="1290" y="720" class="label" text-anchor="middle">10 kV Bus | 630A</text>

    <!-- VCB labels -->
    <text x="1180" y="750" class="rating">VCB-UB</text>
    <text x="1180" y="765" class="rating">(Utility 2)</text>
    <text x="1180" y="780" class="rating">N.C.</text>

    <text x="1290" y="750" class="rating" text-anchor="middle">HPP Priority:</text>
    <text x="1290" y="765" class="rating" text-anchor="middle">Utility 0.35 MW</text>
    <text x="1290" y="780" class="rating" text-anchor="middle">HPP 1.85 MW</text>

    <text x="1400" y="750" class="rating" text-anchor="end">VCB-HB</text>
    <text x="1400" y="765" class="rating" text-anchor="end">(HPP 2)</text>
    <text x="1400" y="780" class="rating" text-anchor="end">N.C.</text>
    <text x="1400" y="795" class="rating" text-anchor="end" font-weight="bold">AUTO-OPEN</text>
    <text x="1400" y="810" class="rating" text-anchor="end" font-weight="bold">on Util Fail</text>

    <!-- Outgoing feeders (2N) -->
    <text x="1180" y="835" class="rating" font-size="9">VCB-2A</text>
    <text x="1180" y="850" class="rating" font-size="9">to XFMR-2A</text>
    <text x="1400" y="835" class="rating" text-anchor="end" font-size="9">VCB-2B</text>
    <text x="1400" y="850" class="rating" text-anchor="end" font-size="9">to XFMR-2B</text>

    <!-- Input connections -->
    <line x1="370" y1="420" x2="1230" y2="420" class="line"/>
    <line x1="1230" y1="420" x2="1230" y2="660" class="line"/>
    <circle cx="1230" cy="620" r="8" fill="white" stroke="black" stroke-width="2"/>
    <text x="1230" y="625" class="rating" text-anchor="middle" font-size="9">VCB</text>

    <line x1="820" y1="580" x2="1400" y2="580" class="line"/>
    <line x1="1400" y1="580" x2="1400" y2="660" class="line"/>
    <circle cx="1400" cy="620" r="8" fill="white" stroke="black" stroke-width="2"/>
    <text x="1400" y="625" class="rating" text-anchor="middle" font-size="9">VCB</text>

    <!-- Output connections (2 feeders) -->
    <line x1="1230" y1="860" x2="1230" y2="920" class="line"/>
    <line x1="1350" y1="860" x2="1350" y2="920" class="line"/>
</g>

<!-- ==================================================================================== -->
<!--                          STEP-DOWN TRANSFORMERS (2N CONFIGURATION)                   -->
<!-- ==================================================================================== -->

<text x="800" y="990" class="bus-label" text-anchor="middle">2N TRANSFORMER CONFIGURATION</text>
<text x="800" y="1010" class="rating" text-anchor="middle">(Each LV SWBD receives power from BOTH MV switchboards)</text>

<!-- XFMR-1A: MV-SWBD-A to LV-SWBD-A -->
<g id="step-down-xfmr-1a">
    <use href="#transformer-down" x="250" y="1060"/>
    <rect x="190" y="1020" width="120" height="80" class="xfmr-2n-feed"/>
    <text x="250" y="1110" class="label" text-anchor="middle">XFMR-1A</text>
    <text x="250" y="1125" class="rating" text-anchor="middle">5,000 kVA</text>
    <text x="250" y="1140" class="rating" text-anchor="middle">10kV/400V</text>
    <line x1="250" y1="920" x2="250" y2="1042" class="line"/>
    <line x1="250" y1="1098" x2="250" y2="1180" class="line"/>
    <text x="250" y="1000" class="rating" text-anchor="middle" font-size="9">MV-A to LV-A</text>
</g>

<!-- XFMR-1B: MV-SWBD-A to LV-SWBD-B (Cross-tie) -->
<g id="step-down-xfmr-1b">
    <use href="#transformer-down" x="550" y="1060"/>
    <rect x="490" y="1020" width="120" height="80" class="xfmr-2n-feed"/>
    <text x="550" y="1110" class="label" text-anchor="middle">XFMR-1B</text>
    <text x="550" y="1125" class="rating" text-anchor="middle">5,000 kVA</text>
    <text x="550" y="1140" class="rating" text-anchor="middle">10kV/400V</text>
    <line x1="370" y1="920" x2="370" y2="980" class="line"/>
    <line x1="370" y1="980" x2="550" y2="980" class="line"/>
    <line x1="550" y1="980" x2="550" y2="1042" class="line"/>
    <line x1="550" y1="1098" x2="550" y2="1180" class="line"/>
    <text x="450" y="970" class="rating" text-anchor="middle" font-size="9">MV-A to LV-B</text>
</g>

<!-- XFMR-2A: MV-SWBD-B to LV-SWBD-A (Cross-tie) -->
<g id="step-down-xfmr-2a">
    <use href="#transformer-down" x="1050" y="1060"/>
    <rect x="990" y="1020" width="120" height="80" class="xfmr-2n-feed"/>
    <text x="1050" y="1110" class="label" text-anchor="middle">XFMR-2A</text>
    <text x="1050" y="1125" class="rating" text-anchor="middle">5,000 kVA</text>
    <text x="1050" y="1140" class="rating" text-anchor="middle">10kV/400V</text>
    <line x1="1230" y1="920" x2="1230" y2="980" class="line"/>
    <line x1="1230" y1="980" x2="1050" y2="980" class="line"/>
    <line x1="1050" y1="980" x2="1050" y2="1042" class="line"/>
    <line x1="1050" y1="1098" x2="1050" y2="1180" class="line"/>
    <text x="1140" y="970" class="rating" text-anchor="middle" font-size="9">MV-B to LV-A</text>
</g>

<!-- XFMR-2B: MV-SWBD-B to LV-SWBD-B -->
<g id="step-down-xfmr-2b">
    <use href="#transformer-down" x="1350" y="1060"/>
    <rect x="1290" y="1020" width="120" height="80" class="xfmr-2n-feed"/>
    <text x="1350" y="1110" class="label" text-anchor="middle">XFMR-2B</text>
    <text x="1350" y="1125" class="rating" text-anchor="middle">5,000 kVA</text>
    <text x="1350" y="1140" class="rating" text-anchor="middle">10kV/400V</text>
    <line x1="1350" y1="920" x2="1350" y2="1042" class="line"/>
    <line x1="1350" y1="1098" x2="1350" y2="1180" class="line"/>
    <text x="1350" y="1000" class="rating" text-anchor="middle" font-size="9">MV-B to LV-B</text>
</g>

<!-- 2N Configuration Note -->
<rect x="700" y="1150" width="400" height="80" fill="white" stroke="black" stroke-width="2"/>
<text x="900" y="1175" class="label" text-anchor="middle" font-weight="bold">2N TIER III DESIGN</text>
<text x="900" y="1195" class="rating" text-anchor="middle">Each LV bus fed from BOTH MV buses</text>
<text x="900" y="1210" class="rating" text-anchor="middle">Any transformer can be removed for maintenance</text>
<text x="900" y="1225" class="rating" text-anchor="middle">without capacity loss - True concurrent maintainability</text>

<!-- ==================================================================================== -->
<!--                          MTU DRUPS (N+1 CONFIGURATION)                              -->
<!-- ==================================================================================== -->

<text x="1300" y="1280" class="bus-label" text-anchor="middle">MTU KINETIC DRUPS (N+1 REDUNDANCY)</text>

<!-- MTU-1 (Running - Bus A) -->
<g id="mtu-1">
    <use href="#mtu-symbol" x="400" y="1350"/>
    <rect x="330" y="1300" width="140" height="100" class="mtu-feed"/>
    <text x="400" y="1410" class="label" text-anchor="middle">MTU-1</text>
    <text x="400" y="1425" class="rating" text-anchor="middle">(Running)</text>
    <text x="400" y="1440" class="rating" text-anchor="middle">Load: 2,200 kW</text>
    <!-- Dual inputs from XFMR-1A and XFMR-2A -->
    <line x1="250" y1="1180" x2="250" y2="1260" class="thin-line"/>
    <line x1="250" y1="1260" x2="380" y2="1260" class="thin-line"/>
    <line x1="380" y1="1260" x2="380" y2="1315" class="thin-line"/>
    <line x1="1050" y1="1180" x2="1050" y2="1260" class="thin-line"/>
    <line x1="1050" y1="1260" x2="420" y2="1260" class="thin-line"/>
    <line x1="420" y1="1260" x2="420" y2="1315" class="thin-line"/>
    <line x1="400" y1="1385" x2="400" y2="1480" class="line"/>
</g>

<!-- MTU-2 (Running - Bus B) -->
<g id="mtu-2">
    <use href="#mtu-symbol" x="950" y="1350"/>
    <rect x="880" y="1300" width="140" height="100" class="mtu-feed"/>
    <text x="950" y="1410" class="label" text-anchor="middle">MTU-2</text>
    <text x="950" y="1425" class="rating" text-anchor="middle">(Running)</text>
    <text x="950" y="1440" class="rating" text-anchor="middle">Load: 2,200 kW</text>
    <!-- Dual inputs from XFMR-1B and XFMR-2B -->
    <line x1="550" y1="1180" x2="550" y2="1260" class="thin-line"/>
    <line x1="550" y1="1260" x2="930" y2="1260" class="thin-line"/>
    <line x1="930" y1="1260" x2="930" y2="1315" class="thin-line"/>
    <line x1="1350" y1="1180" x2="1350" y2="1260" class="thin-line"/>
    <line x1="1350" y1="1260" x2="970" y2="1260" class="thin-line"/>
    <line x1="970" y1="1260" x2="970" y2="1315" class="thin-line"/>
    <line x1="950" y1="1385" x2="950" y2="1480" class="line"/>
</g>

<!-- MTU-3 (Standby - N+1) -->
<g id="mtu-3">
    <use href="#mtu-symbol" x="675" y="1350"/>
    <rect x="605" y="1300" width="140" height="100" class="mtu-feed"/>
    <text x="675" y="1410" class="label" text-anchor="middle">MTU-3</text>
    <text x="675" y="1425" class="label" text-anchor="middle" font-weight="bold">(STANDBY)</text>
    <text x="675" y="1440" class="rating" text-anchor="middle">N+1 Redundancy</text>

    <!-- Bypass connections (dashed) -->
    <line x1="605" y1="1350" x2="470" y2="1350" class="dashed-line"/>
    <line x1="470" y1="1350" x2="470" y2="1560" class="dashed-line"/>
    <text x="520" y="1345" class="rating" font-size="8">Bypass to Bus A</text>

    <line x1="745" y1="1350" x2="880" y2="1350" class="dashed-line"/>
    <line x1="880" y1="1350" x2="880" y2="1560" class="dashed-line"/>
    <text x="800" y="1345" class="rating" font-size="8">Bypass to Bus B</text>
</g>

<!-- ==================================================================================== -->
<!--                          LV SWITCHBOARDS (400V)                                      -->
<!-- ==================================================================================== -->

<!-- Bus A -->
<g id="bus-a">
    <rect x="290" y="1480" width="220" height="180" class="utility-feed"/>
    <text x="400" y="1515" class="bus-label" text-anchor="middle">BUS A</text>
    <text x="400" y="1540" class="label" text-anchor="middle">(LV-SWBD-A)</text>
    <text x="400" y="1565" class="label" text-anchor="middle">400V, 3Ø, 50Hz</text>
    <text x="400" y="1585" class="rating" text-anchor="middle">5,000A Bus</text>
    <text x="400" y="1605" class="rating" text-anchor="middle">Dual Input:</text>
    <text x="400" y="1620" class="rating" text-anchor="middle">XFMR-1A + XFMR-2A</text>
    <text x="400" y="1640" class="rating" text-anchor="middle">Load: 2,200 kW</text>
</g>

<!-- Bus B -->
<g id="bus-b">
    <rect x="840" y="1480" width="220" height="180" class="utility-feed"/>
    <text x="950" y="1515" class="bus-label" text-anchor="middle">BUS B</text>
    <text x="950" y="1540" class="label" text-anchor="middle">(LV-SWBD-B)</text>
    <text x="950" y="1565" class="label" text-anchor="middle">400V, 3Ø, 50Hz</text>
    <text x="950" y="1585" class="rating" text-anchor="middle">5,000A Bus</text>
    <text x="950" y="1605" class="rating" text-anchor="middle">Dual Input:</text>
    <text x="950" y="1620" class="rating" text-anchor="middle">XFMR-1B + XFMR-2B</text>
    <text x="950" y="1640" class="rating" text-anchor="middle">Load: 2,200 kW</text>
</g>

<!-- Tie Breaker -->
<line x1="510" y1="1560" x2="590" y2="1560" class="line"/>
<line x1="710" y1="1560" x2="840" y2="1560" class="line"/>

<g id="tie-breaker">
    <use href="#breaker" x="650" y="1560"/>
    <rect x="580" y="1520" width="140" height="80" class="tie-feed"/>
    <text x="650" y="1550" class="bus-label" text-anchor="middle">52-TIE</text>
    <text x="650" y="1585" class="rating" text-anchor="middle">6,300A Frame</text>
    <text x="650" y="1600" class="rating" text-anchor="middle" font-weight="bold">Normally OPEN</text>
</g>

<!-- ==================================================================================== -->
<!--                          DISTRIBUTION PANELS                                         -->
<!-- ==================================================================================== -->

<!-- Bus A Distribution -->
<line x1="400" y1="1660" x2="340" y2="1660" class="thin-line"/>
<line x1="340" y1="1660" x2="340" y2="1740" class="thin-line"/>
<line x1="400" y1="1660" x2="460" y2="1660" class="thin-line"/>
<line x1="460" y1="1660" x2="460" y2="1740" class="thin-line"/>

<g id="panel-a-it">
    <rect x="270" y="1740" width="140" height="90" class="utility-feed"/>
    <text x="340" y="1770" class="label" text-anchor="middle">A-IT-1</text>
    <text x="340" y="1790" class="rating" text-anchor="middle">3,200A MCCB</text>
    <text x="340" y="1810" class="rating" text-anchor="middle">IT: 1,466 kW</text>
    <text x="340" y="1825" class="rating" text-anchor="middle">(2,497 A)</text>
</g>

<g id="panel-a-cool">
    <rect x="390" y="1740" width="140" height="90" class="utility-feed"/>
    <text x="460" y="1770" class="label" text-anchor="middle">A-COOL-1</text>
    <text x="460" y="1790" class="rating" text-anchor="middle">4,000A MCCB</text>
    <text x="460" y="1810" class="rating" text-anchor="middle">Cooling: 500 kW</text>
    <text x="460" y="1825" class="rating" text-anchor="middle">(851 A)</text>
</g>

<!-- Bus B Distribution -->
<line x1="950" y1="1660" x2="890" y2="1660" class="thin-line"/>
<line x1="890" y1="1660" x2="890" y2="1740" class="thin-line"/>
<line x1="950" y1="1660" x2="1010" y2="1660" class="thin-line"/>
<line x1="1010" y1="1660" x2="1010" y2="1740" class="thin-line"/>

<g id="panel-b-it">
    <rect x="820" y="1740" width="140" height="90" class="utility-feed"/>
    <text x="890" y="1770" class="label" text-anchor="middle">B-IT-1</text>
    <text x="890" y="1790" class="rating" text-anchor="middle">3,200A MCCB</text>
    <text x="890" y="1810" class="rating" text-anchor="middle">IT: 1,467 kW</text>
    <text x="890" y="1825" class="rating" text-anchor="middle">(2,498 A)</text>
</g>

<g id="panel-b-cool">
    <rect x="940" y="1740" width="140" height="90" class="utility-feed"/>
    <text x="1010" y="1770" class="label" text-anchor="middle">B-COOL-1</text>
    <text x="1010" y="1790" class="rating" text-anchor="middle">4,000A MCCB</text>
    <text x="1010" y="1810" class="rating" text-anchor="middle">Cooling: 500 kW</text>
    <text x="1010" y="1825" class="rating" text-anchor="middle">(851 A)</text>
</g>

<!-- ==================================================================================== -->
<!--                          IT LOADS (DUAL-CORDED)                                      -->
<!-- ==================================================================================== -->

<text x="650" y="1920" class="bus-label" text-anchor="middle">IT EQUIPMENT - DUAL-CORDED POWER</text>

<rect x="420" y="1950" width="460" height="100" class="box"/>
<text x="650" y="1980" class="label" text-anchor="middle">IT Equipment Racks with Dual Power Supplies (PSU)</text>
<text x="650" y="2005" class="rating" text-anchor="middle">PDU-A (from Bus A) + PDU-B (from Bus B)</text>
<text x="650" y="2025" class="rating" text-anchor="middle">Automatic failover if either PDU fails</text>
<text x="650" y="2040" class="rating" text-anchor="middle">Total IT Load: 2,933 kW (1,466 kW per side)</text>

<line x1="340" y1="1830" x2="340" y2="1890" class="thin-line"/>
<line x1="340" y1="1890" x2="490" y2="1890" class="thin-line"/>
<line x1="490" y1="1890" x2="490" y2="1950" class="thin-line"/>
<text x="400" y="1880" class="rating" font-size="9">A-side PDUs</text>

<line x1="890" y1="1830" x2="890" y2="1890" class="thin-line"/>
<line x1="890" y1="1890" x2="810" y2="1890" class="thin-line"/>
<line x1="810" y1="1890" x2="810" y2="1950" class="thin-line"/>
<text x="860" y="1880" class="rating" font-size="9" text-anchor="end">B-side PDUs</text>

<!-- ==================================================================================== -->
<!--                          OFFICE LOADS (SOLAR + UTILITY)                              -->
<!-- ==================================================================================== -->

<text x="2270" y="480" class="bus-label" text-anchor="middle">OFFICE LOADS</text>
<text x="2270" y="500" class="rating" text-anchor="middle">(Separated from Critical)</text>

<g id="office-utility">
    <rect x="2080" y="520" width="120" height="80" class="box"/>
    <text x="2140" y="550" class="label" text-anchor="middle">Grid 10kV</text>
    <text x="2140" y="570" class="rating" text-anchor="middle">250 kVA</text>
    <text x="2140" y="585" class="rating" text-anchor="middle">Transformer</text>
    <line x1="2140" y1="600" x2="2140" y2="660" class="line"/>
</g>

<g id="office-ats">
    <rect x="2140" y="660" width="140" height="60" class="solar-feed"/>
    <text x="2210" y="685" class="label" text-anchor="middle">ATS-OFFICE</text>
    <text x="2210" y="705" class="rating" text-anchor="middle">Solar Priority</text>
    <line x1="2210" y1="720" x2="2210" y2="760" class="line"/>
</g>

<g id="office-swbd">
    <rect x="2140" y="760" width="140" height="100" class="box"/>
    <text x="2210" y="790" class="label" text-anchor="middle">SWBD-OFFICE</text>
    <text x="2210" y="810" class="rating" text-anchor="middle">630A @ 400V</text>
    <text x="2210" y="830" class="rating" text-anchor="middle">103 kW Office Load</text>
    <text x="2210" y="850" class="rating" text-anchor="middle">No UPS/MTU</text>
</g>

<line x1="2270" y1="420" x2="2270" y2="660" class="line"/>
<line x1="2270" y1="660" x2="2280" y2="690" class="thin-line"/>
<line x1="2140" y1="660" x2="2140" y2="690" class="thin-line"/>

<!-- ==================================================================================== -->
<!--                          OPERATING MODE ANNOTATIONS                                  -->
<!-- ==================================================================================== -->

<rect x="50" y="2130" width="600" height="200" fill="white" stroke="black" stroke-width="2"/>
<text x="60" y="2160" class="subtitle">NORMAL OPERATION:</text>
<text x="60" y="2185" class="rating">• HPP Priority: 3.7 MW (84% of load)</text>
<text x="60" y="2205" class="rating">• Utility Makeup: 0.7 MW (16% of load)</text>
<text x="60" y="2225" class="rating">• Total Load: 4.4 MW</text>
<text x="60" y="2245" class="rating">• MTU-1 + MTU-2: Running (pass-through)</text>
<text x="60" y="2265" class="rating">• MTU-3: Standby (N+1)</text>
<text x="60" y="2285" class="rating">• Diesel Engines: OFF (flywheel spinning)</text>
<text x="60" y="2305" class="rating">• VCB-HA, VCB-HB: CLOSED (HPP connected)</text>

<rect x="700" y="2130" width="600" height="200" fill="white" stroke="black" stroke-width="2"/>
<text x="710" y="2160" class="subtitle">UTILITY FAILURE MODE:</text>
<text x="710" y="2185" class="rating">• T+0ms: Utility loss detected</text>
<text x="710" y="2205" class="rating">• T+50ms: VCB-HA, VCB-HB OPEN (HPP disconnect)</text>
<text x="710" y="2225" class="rating">• T+0-15s: MTU flywheel bridge (no interruption)</text>
<text x="710" y="2245" class="rating">• T+10-15s: MTU diesel engines start</text>
<text x="710" y="2265" class="rating">• T+15s+: MTU-1 + MTU-2 carry full 4.4 MW</text>
<text x="710" y="2285" class="rating">• MTU-3 available for N+1 backup</text>
<text x="710" y="2305" class="rating">• HPP remains disconnected (protection)</text>

<!-- ==================================================================================== -->
<!--                          LEGEND                                                      -->
<!-- ==================================================================================== -->

<g id="legend">
    <rect x="50" y="2380" width="500" height="340" fill="white" stroke="black" stroke-width="2"/>
    <text x="60" y="2415" class="subtitle">LEGEND:</text>

    <rect x="60" y="2435" width="60" height="30" class="utility-feed"/>
    <text x="130" y="2455" class="rating">Utility Source/Path</text>

    <rect x="60" y="2475" width="60" height="30" class="hpp-feed"/>
    <text x="130" y="2495" class="rating">HPP Source/Path</text>

    <rect x="60" y="2515" width="60" height="30" class="xfmr-2n-feed"/>
    <text x="130" y="2535" class="rating">2N Transformers (Tier III)</text>

    <rect x="60" y="2555" width="60" height="30" class="mtu-feed"/>
    <text x="130" y="2575" class="rating">MTU DRUPS</text>

    <rect x="60" y="2595" width="60" height="30" class="tie-feed"/>
    <text x="130" y="2615" class="rating">Tie Breaker</text>

    <rect x="60" y="2635" width="60" height="30" class="solar-feed"/>
    <text x="130" y="2655" class="rating">Solar (Office Only)</text>

    <circle cx="330" cy="2450" r="8" fill="white" stroke="black" stroke-width="2"/>
    <text x="350" y="2455" class="rating">VCB (Vacuum Circuit Breaker)</text>

    <text x="330" y="2485" class="rating">N.C. - Normally Closed</text>
    <text x="330" y="2505" class="rating">N.O. - Normally Open</text>

    <line x1="320" y1="2525" x2="380" y2="2525" class="line"/>
    <text x="390" y="2530" class="rating">Solid Line: Power Flow</text>

    <line x1="320" y1="2555" x2="380" y2="2555" class="dashed-line"/>
    <text x="390" y="2560" class="rating">Dashed Line: Bypass/Standby</text>
</g>

<!-- ==================================================================================== -->
<!--                          SYSTEM NOTES                                                -->
<!-- ==================================================================================== -->

<g id="notes">
    <rect x="600" y="2380" width="1950" height="340" fill="white" stroke="black" stroke-width="2"/>
    <text x="610" y="2415" class="subtitle">SYSTEM NOTES:</text>
    <text x="610" y="2445" class="rating">1. Primary Sources: Utility 6 MW @ 10kV (dual feeds) + HPP 3.7 MW @ 400V (via step-up transformers)</text>
    <text x="610" y="2465" class="rating">2. Operating Strategy: HPP Priority (3.7 MW = 84%) + Utility Makeup (0.7 MW = 16%) for maximum renewable utilization</text>
    <text x="610" y="2485" class="rating">3. Generator Protection: HPP auto-disconnect (&lt;50ms) on utility failure protects MTU diesels from unstable HPP source</text>
    <text x="610" y="2505" class="rating">4. 2N Transformer Configuration: 4 x 5,000 kVA transformers provide true Tier III concurrent maintainability</text>
    <text x="610" y="2525" class="rating">   - MV-SWBD-A feeds: XFMR-1A (to LV-A) + XFMR-1B (to LV-B) | MV-SWBD-B feeds: XFMR-2A (to LV-A) + XFMR-2B (to LV-B)</text>
    <text x="610" y="2545" class="rating">   - Each LV switchboard receives power from BOTH MV switchboards via separate transformers</text>
    <text x="610" y="2565" class="rating">   - Any single transformer can be removed for maintenance without capacity loss (remaining 3 at 37% utilization)</text>
    <text x="610" y="2585" class="rating">5. MTU Configuration: 3 × 2,750 kVA DRUPS (N+1) - 2 running + 1 standby | Each unit: Diesel + Flywheel (15-20s bridge)</text>
    <text x="610" y="2605" class="rating">6. IT Capacity: 3.0 MW (Phase 1) | Total Facility: 4.4 MW | PUE: 1.50 design max, 1.30 annual average with river free cooling</text>
    <text x="610" y="2625" class="rating">7. Cooling: 3 × 1,800 kW water-cooled chillers (N+1) with Kura River indirect cooling via plate heat exchangers</text>
    <text x="610" y="2645" class="rating">8. LV Distribution: 400V throughout | Dual-path A+B | Tie breaker (52-TIE) normally open for concurrent maintainability</text>
    <text x="610" y="2665" class="rating">9. IT Equipment: Dual-corded with PDU-A (Bus A) + PDU-B (Bus B) for automatic failover</text>
    <text x="610" y="2685" class="rating">10. Office Loads: Separate SWBD with 800 kW solar (priority) + 250 kVA utility backup | No UPS/MTU (non-critical)</text>
    <text x="610" y="2705" class="rating">11. Tier III Compliance: 2N transformers + N+1 MTU DRUPS + Dual MV/LV switchboards + No single points of failure</text>
</g>

<!-- ==================================================================================== -->
<!--                          FOOTER                                                      -->
<!-- ==================================================================================== -->

<text x="1300" y="2780" class="rating" text-anchor="middle">GGE DATA CENTER TBILISI | EVS/GGE ENGINEERING TEAM | DOCUMENT: GGE-EL-SLD-002 REV 02 (2N TRANSFORMERS) | {datetime.now().strftime('%Y-%m-%d')}</text>

</svg>'''

# Save the file
output_file = 'gge_n+1_mtu_hpp_priority_sld.svg'
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(svg)

print("=" * 80)
print("[SUCCESS] GGE N+1 MTU ELECTRICAL SINGLE-LINE DIAGRAM GENERATED")
print("=" * 80)
print(f"\nFile: {output_file}")
print(f"Size: {len(svg):,} bytes")
print(f"\nDesign Configuration:")
print(f"  - IT Capacity: 3.0 MW (Phase 1)")
print(f"  - Transformers: 4 x 5,000 kVA (2N Configuration)")
print(f"  - MTU DRUPS: 3 x 2,750 kVA (N+1: 2 running + 1 standby)")
print(f"  - HPP Priority: 3.7 MW (84% of load)")
print(f"  - Utility Makeup: 0.7 MW (16% of load)")
print(f"  - HPP Auto-Disconnect: <50ms on utility failure")
print(f"  - MV Switchboards: Dual source integration (Utility + HPP)")
print(f"  - LV Distribution: 400V dual-path with tie breaker")
print(f"  - Solar: 800 kW for office loads (separate SWBD)")
print(f"\nKey Features:")
print(f"  - 2N Transformer Tier III Design")
print(f"  - Each LV bus receives power from BOTH MV buses")
print(f"  - Any transformer can be removed for maintenance")
print(f"  - Maximum renewable utilization (84% HPP)")
print(f"  - Generator protection (HPP disconnect on utility fail)")
print(f"  - No interruption (flywheel bridge + diesel backup)")
print(f"  - Full concurrent maintainability (Tier III)")
print("=" * 80)
