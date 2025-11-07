"""
GGE Data Center Single-Line Diagram Generator
Main-Tie-Main (MTM) Topology with HPP 400V Step-Up + Redundant MV Switchboards
Tbilisi, Georgia - Phase 1: 1.47 MW IT Capacity
"""

from datetime import datetime

# SVG setup
width = 2000
height = 2400

# Color scheme
colors = {
    'hpp_feed': '#90EE90',      # Light green for HPP feed (A)
    'grid_feed': '#87CEEB',     # Light blue for Grid feed (B)
    'neutral': '#FFD700',       # Gold for tie breaker
    'mtu': '#FFB6C1',           # Light pink for MTU backup
    'solar': '#FFA500',         # Orange for solar
    'line': '#000000',
    'box': '#FFFFFF',
    'text': '#000000'
}

svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
<defs>
    <!-- Step-up Transformer symbol -->
    <g id="transformer-up">
        <circle cx="0" cy="-18" r="15" fill="white" stroke="black" stroke-width="2"/>
        <circle cx="0" cy="18" r="15" fill="white" stroke="black" stroke-width="2"/>
        <text x="0" y="-12" font-family="Arial" font-size="10" text-anchor="middle">400V</text>
        <text x="0" y="24" font-family="Arial" font-size="10" text-anchor="middle">11kV</text>
    </g>

    <!-- Step-down Transformer symbol -->
    <g id="transformer-down">
        <circle cx="0" cy="-18" r="15" fill="white" stroke="black" stroke-width="2"/>
        <circle cx="0" cy="18" r="15" fill="white" stroke="black" stroke-width="2"/>
        <text x="0" y="-12" font-family="Arial" font-size="10" text-anchor="middle">11kV</text>
        <text x="0" y="24" font-family="Arial" font-size="10" text-anchor="middle">400V</text>
    </g>

    <!-- Circuit Breaker symbol -->
    <g id="breaker">
        <rect x="-10" y="-4" width="20" height="8" fill="white" stroke="black" stroke-width="2"/>
        <line x1="-10" y1="0" x2="-18" y2="0" stroke="black" stroke-width="2"/>
        <line x1="10" y1="0" x2="18" y2="0" stroke="black" stroke-width="2"/>
    </g>

    <!-- MTU Kinetic PowerPack symbol -->
    <g id="mtu-symbol">
        <rect x="-40" y="-30" width="80" height="60" rx="4" fill="white" stroke="black" stroke-width="2"/>
        <text x="0" y="-8" font-family="Arial" font-size="12" font-weight="bold" text-anchor="middle">MTU KP7</text>
        <text x="0" y="8" font-family="Arial" font-size="10" text-anchor="middle">Diesel+</text>
        <text x="0" y="20" font-family="Arial" font-size="10" text-anchor="middle">Flywheel</text>
    </g>

    <!-- Solar Inverter symbol -->
    <g id="solar-symbol">
        <rect x="-35" y="-25" width="70" height="50" rx="3" fill="white" stroke="black" stroke-width="2"/>
        <text x="0" y="-5" font-family="Arial" font-size="12" font-weight="bold" text-anchor="middle">SOLAR</text>
        <text x="0" y="10" font-family="Arial" font-size="10" text-anchor="middle">700kW AC</text>
    </g>
</defs>

<style>
    .title {{ font: bold 20px Arial; fill: #000; }}
    .subtitle {{ font: bold 16px Arial; fill: #000; }}
    .label {{ font: 12px Arial; fill: #000; }}
    .rating {{ font: 10px Arial; fill: #333; }}
    .bus-label {{ font: bold 14px Arial; fill: #000; }}
    .line {{ stroke: #000; stroke-width: 2.5; fill: none; }}
    .thin-line {{ stroke: #000; stroke-width: 1.5; fill: none; }}
    .box {{ fill: white; stroke: black; stroke-width: 2; }}
    .hpp-feed {{ fill: {colors['hpp_feed']}; stroke: black; stroke-width: 2; }}
    .grid-feed {{ fill: {colors['grid_feed']}; stroke: black; stroke-width: 2; }}
    .tie-feed {{ fill: {colors['neutral']}; stroke: black; stroke-width: 2; }}
    .mtu-feed {{ fill: {colors['mtu']}; stroke: black; stroke-width: 2; }}
    .solar-feed {{ fill: {colors['solar']}; stroke: black; stroke-width: 2; }}
</style>

<!-- Title Block -->
<rect x="50" y="30" width="1900" height="120" fill="white" stroke="black" stroke-width="2"/>
<text x="1000" y="65" class="title" text-anchor="middle">GGE DATA CENTER - TBILISI, GEORGIA</text>
<text x="1000" y="95" class="subtitle" text-anchor="middle">Electrical Single-Line Diagram - Main-Tie-Main (MTM) Topology</text>
<text x="1000" y="120" class="rating" text-anchor="middle">Phase 1: 1.47 MW IT Capacity | Tier III Concurrent Maintainability | HPP 400V Step-Up + Grid 11kV Direct</text>

<!-- Revision Block -->
<g id="revision-block">
    <rect x="1750" y="30" width="200" height="120" fill="white" stroke="black" stroke-width="2"/>
    <text x="1760" y="55" class="label">Date: {datetime.now().strftime('%Y-%m-%d')}</text>
    <text x="1760" y="75" class="label">Doc: GGE-EL-SLD-001</text>
    <text x="1760" y="95" class="label">Rev: 03</text>
    <text x="1760" y="115" class="label">Status: For Construction</text>
    <text x="1760" y="135" class="rating">EVS/GGE Engineering</text>
</g>

<!-- =============================================================================== -->
<!--                          PRIMARY SOURCES (DIFFERENT VOLTAGES)                   -->
<!-- =============================================================================== -->

<!-- HPP Source (400V) - LEFT SIDE -->
<g id="hpp-source">
    <rect x="150" y="200" width="200" height="100" class="hpp-feed"/>
    <text x="250" y="230" class="bus-label" text-anchor="middle">HPP SOURCE</text>
    <text x="250" y="250" class="label" text-anchor="middle">400V, 3Ø, 50Hz</text>
    <text x="250" y="270" class="rating" text-anchor="middle">3.7 MW Capacity</text>
    <text x="250" y="285" class="rating" text-anchor="middle">(Low Voltage)</text>
    <line x1="250" y1="300" x2="250" y2="340" class="line"/>
</g>

<!-- Grid Source (11kV) - RIGHT SIDE -->
<g id="grid-source">
    <rect x="1650" y="200" width="200" height="100" class="grid-feed"/>
    <text x="1750" y="230" class="bus-label" text-anchor="middle">UTILITY GRID</text>
    <text x="1750" y="250" class="label" text-anchor="middle">11 kV, 3Ø, 50Hz</text>
    <text x="1750" y="270" class="rating" text-anchor="middle">4.0 MW Capacity</text>
    <text x="1750" y="285" class="rating" text-anchor="middle">(Medium Voltage)</text>
    <line x1="1750" y1="300" x2="1750" y2="340" class="line"/>
</g>

<!-- =============================================================================== -->
<!--                          HPP STEP-UP TRANSFORMER (400V → 11kV)                  -->
<!-- =============================================================================== -->

<g id="step-up-transformer">
    <use href="#transformer-up" x="250" y="380"/>
    <rect x="190" y="340" width="120" height="80" class="hpp-feed"/>
    <text x="250" y="440" class="label" text-anchor="middle">XFMR-STEP-UP</text>
    <text x="250" y="455" class="rating" text-anchor="middle">3,500 kVA</text>
    <text x="250" y="470" class="rating" text-anchor="middle">400V / 11kV</text>
    <text x="250" y="485" class="rating" text-anchor="middle">Dyn11, ONAN</text>
    <line x1="250" y1="418" x2="250" y2="520" class="line"/>
</g>

<!-- Grid 11kV VCB -->
<g id="grid-vcb">
    <use href="#breaker" x="1750" y="360"/>
    <text x="1680" y="340" class="rating">VCB-GRID</text>
    <text x="1680" y="355" class="rating">630A, 40kA</text>
    <line x1="1750" y1="340" x2="1750" y2="378" class="line"/>
    <line x1="1750" y1="378" x2="1750" y2="520" class="line"/>
</g>

<!-- =============================================================================== -->
<!--                     REDUNDANT MV SWITCHBOARDS (11 kV)                          -->
<!-- =============================================================================== -->

<g id="mv-swbd-a">
    <rect x="150" y="520" width="200" height="120" class="hpp-feed"/>
    <text x="250" y="555" class="bus-label" text-anchor="middle">MV-SWBD-A</text>
    <text x="250" y="580" class="label" text-anchor="middle">11 kV Bus</text>
    <text x="250" y="600" class="rating" text-anchor="middle">630A | VCB Lineup</text>
    <text x="250" y="620" class="rating" text-anchor="middle">Fed from HPP</text>
    <line x1="250" y1="640" x2="250" y2="680" class="line"/>
</g>

<g id="mv-swbd-b">
    <rect x="1650" y="520" width="200" height="120" class="grid-feed"/>
    <text x="1750" y="555" class="bus-label" text-anchor="middle">MV-SWBD-B</text>
    <text x="1750" y="580" class="label" text-anchor="middle">11 kV Bus</text>
    <text x="1750" y="600" class="rating" text-anchor="middle">630A | VCB Lineup</text>
    <text x="1750" y="620" class="rating" text-anchor="middle">Fed from Grid</text>
    <line x1="1750" y1="640" x2="1750" y2="680" class="line"/>
</g>

<!-- =============================================================================== -->
<!--                     STEP-DOWN TRANSFORMERS (11 kV → 400V)                      -->
<!-- =============================================================================== -->

<g id="step-down-transformer-a">
    <use href="#transformer-down" x="250" y="720"/>
    <rect x="190" y="680" width="120" height="80" class="hpp-feed"/>
    <text x="250" y="780" class="label" text-anchor="middle">XFMR-A</text>
    <text x="250" y="795" class="rating" text-anchor="middle">3,500 kVA</text>
    <text x="250" y="810" class="rating" text-anchor="middle">11kV / 400V</text>
    <text x="250" y="825" class="rating" text-anchor="middle">Dyn11, ONAN</text>
    <line x1="250" y1="758" x2="250" y2="860" class="line"/>
</g>

<g id="step-down-transformer-b">
    <use href="#transformer-down" x="1750" y="720"/>
    <rect x="1690" y="680" width="120" height="80" class="grid-feed"/>
    <text x="1750" y="780" class="label" text-anchor="middle">XFMR-B</text>
    <text x="1750" y="795" class="rating" text-anchor="middle">3,500 kVA</text>
    <text x="1750" y="810" class="rating" text-anchor="middle">11kV / 400V</text>
    <text x="1750" y="825" class="rating" text-anchor="middle">Dyn11, ONAN</text>
    <line x1="1750" y1="758" x2="1750" y2="860" class="line"/>
</g>

<!-- =============================================================================== -->
<!--                     MAIN BREAKERS (400V LV)                                    -->
<!-- =============================================================================== -->

<g id="acb-m1">
    <use href="#breaker" x="250" y="880"/>
    <text x="180" y="860" class="rating">ACB-M1</text>
    <text x="180" y="875" class="rating">6,300A Frame</text>
    <text x="180" y="890" class="rating">5,000A Trip</text>
    <text x="180" y="905" class="rating">Drawout</text>
    <line x1="250" y1="860" x2="250" y2="898" class="line"/>
    <line x1="250" y1="898" x2="250" y2="960" class="line"/>
</g>

<g id="acb-m2">
    <use href="#breaker" x="1750" y="880"/>
    <text x="1820" y="860" class="rating">ACB-M2</text>
    <text x="1820" y="875" class="rating">6,300A Frame</text>
    <text x="1820" y="890" class="rating">5,000A Trip</text>
    <text x="1820" y="905" class="rating">Drawout</text>
    <line x1="1750" y1="860" x2="1750" y2="898" class="line"/>
    <line x1="1750" y1="898" x2="1750" y2="960" class="line"/>
</g>

<!-- =============================================================================== -->
<!--                     LOW VOLTAGE SWITCHBOARDS - MTM TOPOLOGY                    -->
<!-- =============================================================================== -->

<g id="bus-a">
    <rect x="150" y="960" width="200" height="140" class="hpp-feed"/>
    <text x="250" y="995" class="bus-label" text-anchor="middle">BUS A</text>
    <text x="250" y="1015" class="label" text-anchor="middle">(SWBD-A)</text>
    <text x="250" y="1035" class="label" text-anchor="middle">400V, 3Ø, 50Hz</text>
    <text x="250" y="1055" class="rating" text-anchor="middle">2,500A Bus</text>
    <text x="250" y="1075" class="rating" text-anchor="middle">Normal: 1,039 kW</text>
    <text x="250" y="1090" class="rating" text-anchor="middle">Failure: 2,078 kW</text>
</g>

<g id="bus-b">
    <rect x="1650" y="960" width="200" height="140" class="grid-feed"/>
    <text x="1750" y="995" class="bus-label" text-anchor="middle">BUS B</text>
    <text x="1750" y="1015" class="label" text-anchor="middle">(SWBD-B)</text>
    <text x="1750" y="1035" class="label" text-anchor="middle">400V, 3Ø, 50Hz</text>
    <text x="1750" y="1055" class="rating" text-anchor="middle">2,500A Bus</text>
    <text x="1750" y="1075" class="rating" text-anchor="middle">Normal: 1,096 kW</text>
    <text x="1750" y="1090" class="rating" text-anchor="middle">Failure: 2,078 kW</text>
</g>

<!-- Tie Breaker Connection -->
<line x1="350" y1="1030" x2="900" y2="1030" class="line"/>
<line x1="1100" y1="1030" x2="1650" y2="1030" class="line"/>

<g id="tie-breaker">
    <use href="#breaker" x="1000" y="1030"/>
    <rect x="930" y="990" width="140" height="80" class="tie-feed"/>
    <text x="1000" y="1010" class="bus-label" text-anchor="middle">52-TIE</text>
    <text x="1000" y="1055" class="rating" text-anchor="middle">6,300A Frame</text>
    <text x="1000" y="1070" class="rating" text-anchor="middle">Normally OPEN</text>
</g>

<!-- =============================================================================== -->
<!--                     MTU KINETIC POWERPACK BACKUP (2N)                          -->
<!-- =============================================================================== -->

<g id="mtu-1">
    <line x1="250" y1="1100" x2="250" y2="1140" class="line"/>
    <line x1="250" y1="1140" x2="450" y2="1140" class="line"/>
    <line x1="450" y1="1140" x2="450" y2="1180" class="line"/>

    <use href="#mtu-symbol" x="450" y="1230"/>
    <rect x="380" y="1180" width="140" height="100" class="mtu-feed"/>
    <text x="450" y="1295" class="label" text-anchor="middle">MTU-1</text>
    <text x="450" y="1310" class="rating" text-anchor="middle">2,200 kW / 2,750 kVA</text>
    <text x="450" y="1325" class="rating" text-anchor="middle">400V Output</text>

    <line x1="450" y1="1280" x2="450" y2="1350" class="line"/>

    <use href="#breaker" x="450" y="1370"/>
    <text x="380" y="1350" class="rating">ACB-MTU1</text>
    <text x="380" y="1365" class="rating">5,000A</text>
    <text x="380" y="1380" class="rating">w/ ATS</text>

    <line x1="450" y1="1388" x2="450" y2="1420" class="line"/>
    <line x1="450" y1="1420" x2="250" y2="1420" class="line"/>
    <line x1="250" y1="1420" x2="250" y2="1100" class="line"/>
    <circle cx="250" cy="1100" r="5" fill="black"/>
</g>

<g id="mtu-2">
    <line x1="1750" y1="1100" x2="1750" y2="1140" class="line"/>
    <line x1="1750" y1="1140" x2="1550" y2="1140" class="line"/>
    <line x1="1550" y1="1140" x2="1550" y2="1180" class="line"/>

    <use href="#mtu-symbol" x="1550" y="1230"/>
    <rect x="1480" y="1180" width="140" height="100" class="mtu-feed"/>
    <text x="1550" y="1295" class="label" text-anchor="middle">MTU-2</text>
    <text x="1550" y="1310" class="rating" text-anchor="middle">2,200 kW / 2,750 kVA</text>
    <text x="1550" y="1325" class="rating" text-anchor="middle">400V Output</text>

    <line x1="1550" y1="1280" x2="1550" y2="1350" class="line"/>

    <use href="#breaker" x="1550" y="1370"/>
    <text x="1620" y="1350" class="rating">ACB-MTU2</text>
    <text x="1620" y="1365" class="rating">5,000A</text>
    <text x="1620" y="1380" class="rating">w/ ATS</text>

    <line x1="1550" y1="1388" x2="1550" y2="1420" class="line"/>
    <line x1="1550" y1="1420" x2="1750" y2="1420" class="line"/>
    <line x1="1750" y1="1420" x2="1750" y2="1100" class="line"/>
    <circle cx="1750" cy="1100" r="5" fill="black"/>
</g>

<!-- =============================================================================== -->
<!--                     DISTRIBUTION PANELS (IT + COOLING)                         -->
<!-- =============================================================================== -->

<!-- Bus A Distribution -->
<line x1="250" y1="1100" x2="150" y2="1100" class="thin-line"/>
<line x1="150" y1="1100" x2="150" y2="1500" class="thin-line"/>

<g id="panel-a-it">
    <rect x="80" y="1500" width="140" height="90" class="hpp-feed"/>
    <text x="150" y="1530" class="label" text-anchor="middle">A-IT-1</text>
    <text x="150" y="1550" class="rating" text-anchor="middle">2,500A MCCB</text>
    <text x="150" y="1570" class="rating" text-anchor="middle">IT Loads: 735 kW</text>
    <text x="150" y="1585" class="rating" text-anchor="middle">(1,248 A)</text>
</g>

<line x1="250" y1="1100" x2="420" y2="1100" class="thin-line"/>
<line x1="420" y1="1100" x2="420" y2="1500" class="thin-line"/>

<g id="panel-a-cool">
    <rect x="350" y="1500" width="140" height="90" class="hpp-feed"/>
    <text x="420" y="1530" class="label" text-anchor="middle">A-COOL-1</text>
    <text x="420" y="1550" class="rating" text-anchor="middle">3,200A MCCB</text>
    <text x="420" y="1570" class="rating" text-anchor="middle">Cooling: 304 kW</text>
    <text x="420" y="1585" class="rating" text-anchor="middle">(515 A)</text>
</g>

<!-- Bus B Distribution -->
<line x1="1750" y1="1100" x2="1850" y2="1100" class="thin-line"/>
<line x1="1850" y1="1100" x2="1850" y2="1500" class="thin-line"/>

<g id="panel-b-it">
    <rect x="1780" y="1500" width="140" height="90" class="grid-feed"/>
    <text x="1850" y="1530" class="label" text-anchor="middle">B-IT-1</text>
    <text x="1850" y="1550" class="rating" text-anchor="middle">2,500A MCCB</text>
    <text x="1850" y="1570" class="rating" text-anchor="middle">IT Loads: 735 kW</text>
    <text x="1850" y="1585" class="rating" text-anchor="middle">(1,248 A)</text>
</g>

<line x1="1750" y1="1100" x2="1580" y2="1100" class="thin-line"/>
<line x1="1580" y1="1100" x2="1580" y2="1500" class="thin-line"/>

<g id="panel-b-cool">
    <rect x="1510" y="1500" width="140" height="90" class="grid-feed"/>
    <text x="1580" y="1530" class="label" text-anchor="middle">B-COOL-1</text>
    <text x="1580" y="1550" class="rating" text-anchor="middle">3,200A MCCB</text>
    <text x="1580" y="1570" class="rating" text-anchor="middle">Cooling: 361 kW</text>
    <text x="1580" y="1585" class="rating" text-anchor="middle">(613 A)</text>
</g>

<!-- =============================================================================== -->
<!--                     OFFICE LOADS (SOLAR + UTILITY)                             -->
<!-- =============================================================================== -->

<g id="office-solar">
    <use href="#solar-symbol" x="700" y="280"/>
    <rect x="640" y="230" width="120" height="80" class="solar-feed"/>
    <text x="700" y="325" class="label" text-anchor="middle">Solar Array</text>
    <text x="700" y="340" class="rating" text-anchor="middle">700 kW AC</text>
    <line x1="700" y1="310" x2="700" y2="380" class="line"/>
</g>

<g id="office-utility">
    <rect x="900" y="230" width="120" height="80" class="box"/>
    <text x="960" y="260" class="label" text-anchor="middle">Grid 11kV</text>
    <text x="960" y="280" class="rating" text-anchor="middle">250 kVA</text>
    <text x="960" y="295" class="rating" text-anchor="middle">Transformer</text>
    <line x1="960" y1="310" x2="960" y2="380" class="line"/>
</g>

<g id="office-ats">
    <rect x="760" y="380" width="140" height="60" class="solar-feed"/>
    <text x="830" y="405" class="label" text-anchor="middle">ATS-OFFICE</text>
    <text x="830" y="425" class="rating" text-anchor="middle">Solar Priority</text>
    <line x1="830" y1="440" x2="830" y2="480" class="line"/>
</g>

<g id="office-swbd">
    <rect x="760" y="480" width="140" height="80" class="box"/>
    <text x="830" y="510" class="label" text-anchor="middle">SWBD-OFFICE</text>
    <text x="830" y="530" class="rating" text-anchor="middle">630A Bus</text>
    <text x="830" y="550" class="rating" text-anchor="middle">103 kW (Office)</text>
    <text x="830" y="565" class="rating" text-anchor="middle">No UPS/MTU</text>
</g>

<line x1="700" y1="380" x2="760" y2="410" class="thin-line"/>
<line x1="960" y1="380" x2="900" y2="410" class="thin-line"/>

<!-- =============================================================================== -->
<!--                     LOAD DESCRIPTIONS                                          -->
<!-- =============================================================================== -->

<g id="it-loads">
    <rect x="80" y="1620" width="140" height="100" class="box"/>
    <text x="150" y="1645" class="rating" text-anchor="middle" font-size="9">IT Equipment:</text>
    <text x="150" y="1660" class="rating" text-anchor="middle" font-size="9">• Dual-corded PDUs</text>
    <text x="150" y="1675" class="rating" text-anchor="middle" font-size="9">• A+B power feeds</text>
    <text x="150" y="1690" class="rating" text-anchor="middle" font-size="9">• Auto-failover</text>
    <text x="150" y="1705" class="rating" text-anchor="middle" font-size="9">• 230V 1Ø output</text>
</g>

<g id="cooling-loads-a">
    <rect x="350" y="1620" width="140" height="130" class="box"/>
    <text x="420" y="1645" class="rating" text-anchor="middle" font-size="9">Bus A Cooling:</text>
    <text x="420" y="1660" class="rating" text-anchor="middle" font-size="9">• CHW Pump #1 (30kW)</text>
    <text x="420" y="1675" class="rating" text-anchor="middle" font-size="9">• CW Pump #1 (45kW)</text>
    <text x="420" y="1690" class="rating" text-anchor="middle" font-size="9">• River Pump #1 (30kW)</text>
    <text x="420" y="1705" class="rating" text-anchor="middle" font-size="9">• In-Row #1-6 (75kW)</text>
    <text x="420" y="1720" class="rating" text-anchor="middle" font-size="9">• Chiller #1 (124kW)</text>
    <text x="420" y="1735" class="rating" text-anchor="middle" font-size="9">Total: 304 kW</text>
</g>

<g id="cooling-loads-b">
    <rect x="1510" y="1620" width="140" height="145" class="box"/>
    <text x="1580" y="1645" class="rating" text-anchor="middle" font-size="9">Bus B Cooling:</text>
    <text x="1580" y="1660" class="rating" text-anchor="middle" font-size="9">• CHW Pump #2 (30kW)</text>
    <text x="1580" y="1675" class="rating" text-anchor="middle" font-size="9">• CW Pump #2 (45kW)</text>
    <text x="1580" y="1690" class="rating" text-anchor="middle" font-size="9">• River Pump #2 (30kW)</text>
    <text x="1580" y="1705" class="rating" text-anchor="middle" font-size="9">• In-Row #7-12 (75kW)</text>
    <text x="1580" y="1720" class="rating" text-anchor="middle" font-size="9">• Chiller #2 (124kW)</text>
    <text x="1580" y="1735" class="rating" text-anchor="middle" font-size="9">• Chiller #3 (57kW)</text>
    <text x="1580" y="1750" class="rating" text-anchor="middle" font-size="9">Total: 361 kW</text>
</g>

<g id="it-loads-b">
    <rect x="1780" y="1620" width="140" height="100" class="box"/>
    <text x="1850" y="1645" class="rating" text-anchor="middle" font-size="9">IT Equipment:</text>
    <text x="1850" y="1660" class="rating" text-anchor="middle" font-size="9">• Dual-corded PDUs</text>
    <text x="1850" y="1675" class="rating" text-anchor="middle" font-size="9">• A+B power feeds</text>
    <text x="1850" y="1690" class="rating" text-anchor="middle" font-size="9">• Auto-failover</text>
    <text x="1850" y="1705" class="rating" text-anchor="middle" font-size="9">• 230V 1Ø output</text>
</g>

<!-- =============================================================================== -->
<!--                     LEGEND                                                     -->
<!-- =============================================================================== -->

<g id="legend">
    <rect x="50" y="1850" width="400" height="240" fill="white" stroke="black" stroke-width="2"/>
    <text x="60" y="1880" class="subtitle">LEGEND:</text>

    <rect x="60" y="1900" width="50" height="25" class="hpp-feed"/>
    <text x="120" y="1918" class="rating">HPP Feed (Path A)</text>

    <rect x="60" y="1935" width="50" height="25" class="grid-feed"/>
    <text x="120" y="1953" class="rating">Grid Feed (Path B)</text>

    <rect x="60" y="1970" width="50" height="25" class="tie-feed"/>
    <text x="120" y="1988" class="rating">Tie Breaker</text>

    <rect x="60" y="2005" width="50" height="25" class="mtu-feed"/>
    <text x="120" y="2023" class="rating">MTU Backup Power</text>

    <rect x="60" y="2040" width="50" height="25" class="solar-feed"/>
    <text x="120" y="2058" class="rating">Solar (Office Only)</text>
</g>

<!-- =============================================================================== -->
<!--                     SYSTEM NOTES                                               -->
<!-- =============================================================================== -->

<g id="notes">
    <rect x="500" y="1850" width="1450" height="240" fill="white" stroke="black" stroke-width="2"/>
    <text x="510" y="1880" class="subtitle">SYSTEM NOTES:</text>
    <text x="510" y="1910" class="rating">1. Primary Sources: HPP @ 400V (3.7 MW) + Utility Grid @ 11kV (4.0 MW) - Dual diverse sources</text>
    <text x="510" y="1930" class="rating">2. HPP Path: 400V → Step-Up XFMR (3,500 kVA) → MV-SWBD-A (11kV) → Step-Down XFMR-A → BUS A (400V)</text>
    <text x="510" y="1950" class="rating">3. Grid Path: 11kV → MV-SWBD-B (11kV) → Step-Down XFMR-B → BUS B (400V)</text>
    <text x="510" y="1970" class="rating">4. MTM Topology: 52-TIE breaker (normally OPEN) at 400V LV level for automatic failover</text>
    <text x="510" y="1990" class="rating">5. Backup Power: 2 × MTU KP7 Kinetic PowerPack (2,200 kW each, 2N redundancy) - Diesel + Flywheel UPS</text>
    <text x="510" y="2010" class="rating">6. Cooling: 3 × 800kW water-cooled chillers (N+1) with Kura River indirect cooling via plate heat exchangers</text>
    <text x="510" y="2030" class="rating">7. Office Loads: Separate SWBD with 700 kW solar array (priority) + 250 kVA utility backup (no UPS/MTU)</text>
    <text x="510" y="2050" class="rating">8. Tier III Compliance: Concurrent maintainability - any component can be maintained without shutdown</text>
    <text x="510" y="2070" class="rating">9. Standards: IEC 60364 (Georgia), TN-S grounding, 400V distribution throughout critical loads</text>
</g>

<!-- =============================================================================== -->
<!--                     FOOTER                                                     -->
<!-- =============================================================================== -->

<text x="1000" y="2140" class="rating" text-anchor="middle">GGE DATA CENTER TBILISI | EVS/GGE ENGINEERING TEAM | DOCUMENT: GGE-EL-SLD-001 REV 03 | {datetime.now().strftime('%Y-%m-%d')}</text>

</svg>'''

# Save the file
output_file = 'gge_mtm_sld.svg'
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(svg)

print("=" * 80)
print("[SUCCESS] GGE MTM ELECTRICAL SINGLE-LINE DIAGRAM GENERATED")
print("=" * 80)
print(f"\nFile: {output_file}")
print(f"Size: {len(svg):,} bytes")
print(f"\nDesign Configuration:")
print(f"  - HPP Source: 400V -> 11kV step-up (3.7 MW)")
print(f"  - Grid Source: 11kV direct (4.0 MW)")
print(f"  - Redundant MV Switchboards: MV-SWBD-A + MV-SWBD-B (11kV)")
print(f"  - Step-down Transformers: 2 x 3,500 kVA (11kV -> 400V)")
print(f"  - MTM Topology: 52-TIE at 400V (normally open)")
print(f"  - Backup: 2 x MTU KP7 (2,200 kW each, 2N)")
print(f"  - IT Capacity: 1.47 MW (Phase 1)")
print(f"  - Distribution Panels: IT + Cooling (A-side + B-side)")
print(f"  - Office: Solar 700kW + Utility 250kVA (separate SWBD)")
print(f"\nTier III Features:")
print(f"  - Dual utility sources (HPP + Grid)")
print(f"  - Redundant MV switchboards")
print(f"  - 2N transformers (step-up + step-downs)")
print(f"  - MTM with automatic tie breaker")
print(f"  - 2N MTU backup power")
print(f"  - Concurrent maintainability")
print("=" * 80)
