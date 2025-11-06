"""
Professional Single-Line Diagram Generator for Saga Pryor Data Center
Matches the format and style of the sample SLD with proper electrical symbols.
"""

import json
from datetime import datetime

# Read the metadata
with open('pachyderm_metadata.json', 'r') as f:
    data = json.load(f)

# SVG setup - larger for professional format
width = 1600
height = 2200

# Color scheme matching professional SLD
colors = {
    'a_feed': '#90EE90',  # Light green for A feed
    'b_feed': '#87CEEB',  # Light blue for B feed
    'neutral': '#FFD700',  # Gold/yellow for neutral/tie
    'line': '#000000',
    'box': '#FFFFFF',
    'text': '#000000'
}

svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
<defs>
    <!-- Transformer symbol -->
    <g id="transformer">
        <circle cx="0" cy="-15" r="12" fill="white" stroke="black" stroke-width="1.5"/>
        <circle cx="0" cy="15" r="12" fill="white" stroke="black" stroke-width="1.5"/>
    </g>
    
    <!-- Breaker symbol -->
    <g id="breaker">
        <rect x="-8" y="-3" width="16" height="6" fill="white" stroke="black" stroke-width="1.5"/>
        <line x1="-8" y1="0" x2="-15" y2="0" stroke="black" stroke-width="2"/>
        <line x1="8" y1="0" x2="15" y2="0" stroke="black" stroke-width="2"/>
    </g>
    
    <!-- Generator symbol -->
    <g id="generator">
        <circle cx="0" cy="0" r="20" fill="white" stroke="black" stroke-width="2"/>
        <text x="0" y="6" font-family="Arial" font-size="16" font-weight="bold" text-anchor="middle">G</text>
    </g>
    
    <!-- UPS symbol -->
    <g id="ups-symbol">
        <rect x="-25" y="-20" width="50" height="40" rx="3" fill="white" stroke="black" stroke-width="2"/>
        <text x="0" y="5" font-family="Arial" font-size="12" font-weight="bold" text-anchor="middle">UPS</text>
    </g>
</defs>

<style>
    .title {{ font: bold 18px Arial; fill: #000; }}
    .subtitle {{ font: bold 14px Arial; fill: #000; }}
    .label {{ font: 11px Arial; fill: #000; }}
    .rating {{ font: 10px Arial; fill: #333; }}
    .bus-label {{ font: bold 12px Arial; fill: #000; }}
    .line {{ stroke: #000; stroke-width: 2; fill: none; }}
    .thin-line {{ stroke: #000; stroke-width: 1; fill: none; }}
    .box {{ fill: white; stroke: black; stroke-width: 1.5; }}
    .feed-a {{ fill: {colors['a_feed']}; stroke: black; stroke-width: 1.5; }}
    .feed-b {{ fill: {colors['b_feed']}; stroke: black; stroke-width: 1.5; }}
    .feed-tie {{ fill: {colors['neutral']}; stroke: black; stroke-width: 1.5; }}
</style>

<!-- Title Block -->
<rect x="50" y="30" width="1500" height="100" fill="white" stroke="black" stroke-width="2"/>
<text x="800" y="60" class="title" text-anchor="middle">SAGA PRYOR DATA CENTER - Phase 1</text>
<text x="800" y="85" class="subtitle" text-anchor="middle">Electrical Single-Line Diagram - 345kV/13.8kV Ring Bus Distribution</text>
<text x="800" y="110" class="rating" text-anchor="middle">PACHYDERM GLOBAL | Tier III | N+1 Redundancy</text>

<!-- Revision Block -->
<g id="revision-block">
    <rect x="1350" y="30" width="200" height="100" fill="white" stroke="black" stroke-width="1.5"/>
    <text x="1360" y="50" class="label">Date: {datetime.now().strftime('%m/%d/%Y')}</text>
    <text x="1360" y="70" class="label">Doc: SAGA-EL-SLD-001</text>
    <text x="1360" y="90" class="label">Rev: 0</text>
    <text x="1360" y="110" class="label">Status: Issued for Review</text>
</g>

<!-- 345kV Utility Service -->
<g id="utility-service">
    <rect x="200" y="180" width="150" height="80" class="box"/>
    <text x="275" y="210" class="bus-label" text-anchor="middle">345kV</text>
    <text x="275" y="230" class="bus-label" text-anchor="middle">UTILITY</text>
    <text x="275" y="250" class="rating" text-anchor="middle">2 × 25MVA TX</text>
    <line x1="275" y1="260" x2="275" y2="300" class="line"/>
</g>

<g id="utility-service-2">
    <rect x="1250" y="180" width="150" height="80" class="box"/>
    <text x="1325" y="210" class="bus-label" text-anchor="middle">345kV</text>
    <text x="1325" y="230" class="bus-label" text-anchor="middle">UTILITY</text>
    <text x="1325" y="250" class="rating" text-anchor="middle">2 × 25MVA TX</text>
    <line x1="1325" y1="260" x2="1325" y2="300" class="line"/>
</g>

<!-- Generator Distribution Board -->
<g id="generator-db">
    <rect x="700" y="180" width="200" height="80" class="box"/>
    <text x="800" y="210" class="bus-label" text-anchor="middle">Generator DB</text>
    <text x="800" y="230" class="label" text-anchor="middle">3 × 4MW (N+1)</text>
    <text x="800" y="250" class="rating" text-anchor="middle">Parallel Sync</text>
    <line x1="800" y1="260" x2="800" y2="300" class="line"/>
</g>

<!-- MV Main Switchboards -->
<g id="mv-msb-a">
    <rect x="150" y="320" width="250" height="100" class="feed-a"/>
    <text x="275" y="355" class="bus-label" text-anchor="middle">MV-MSB A</text>
    <text x="275" y="375" class="label" text-anchor="middle">13.8 kV</text>
    <text x="275" y="395" class="rating" text-anchor="middle">4000A | 65kAIC</text>
    <text x="275" y="410" class="rating" text-anchor="middle">Ring A Feed</text>
</g>

<g id="mv-msb-b">
    <rect x="1200" y="320" width="250" height="100" class="feed-b"/>
    <text x="1325" y="355" class="bus-label" text-anchor="middle">MV-MSB B</text>
    <text x="1325" y="375" class="label" text-anchor="middle">13.8 kV</text>
    <text x="1325" y="395" class="rating" text-anchor="middle">4000A | 65kAIC</text>
    <text x="1325" y="410" class="rating" text-anchor="middle">Ring B Feed</text>
</g>

<!-- Ring Bus Connection -->
<line x1="275" y1="420" x2="275" y2="480" class="line"/>
<line x1="1325" y1="420" x2="1325" y2="480" class="line"/>
<line x1="275" y1="480" x2="1325" y2="480" class="line"/>
<text x="800" y="470" class="rating" text-anchor="middle">13.8kV DUAL RING BUS</text>

<!-- RMUs positioned across -->
'''

# RMU positions - 6 units across
rmu_x_positions = [180, 380, 580, 1020, 1220, 1420]
rmu_labels = ['RMU-1', 'RMU-2', 'RMU-3', 'RMU-4', 'RMU-5', 'RMU-6']
rmu_feeds = ['A', 'A', 'A', 'B', 'B', 'B']

for i, (x, label, feed) in enumerate(zip(rmu_x_positions, rmu_labels, rmu_feeds)):
    feed_class = 'feed-a' if feed == 'A' else 'feed-b'
    svg += f'''
<!-- {label} -->
<g id="rmu-{i+1}">
    <line x1="{x+60}" y1="480" x2="{x+60}" y2="520" class="line"/>
    <rect x="{x}" y="520" width="120" height="70" class="{feed_class}"/>
    <text x="{x+60}" y="545" class="bus-label" text-anchor="middle">{label}</text>
    <text x="{x+60}" y="565" class="rating" text-anchor="middle">630A</text>
    <text x="{x+60}" y="580" class="rating" text-anchor="middle">20kA SCCR</text>
    <line x1="{x+60}" y1="590" x2="{x+60}" y2="630" class="line"/>
    
    <!-- Breaker symbols -->
    <circle cx="{x+30}" cy="555" r="5" fill="white" stroke="black" stroke-width="1"/>
    <text x="{x+30}" y="575" class="rating" font-size="8" text-anchor="middle">NC</text>
    
    <circle cx="{x+60}" cy="555" r="5" fill="white" stroke="black" stroke-width="1"/>
    <text x="{x+60}" y="575" class="rating" font-size="8" text-anchor="middle">NC</text>
    
    <circle cx="{x+90}" cy="555" r="5" fill="white" stroke="black" stroke-width="1"/>
    <text x="{x+90}" y="575" class="rating" font-size="8" text-anchor="middle">{'NO' if i % 2 == 1 else 'NC'}</text>
</g>
'''

# Transformers below RMUs
tx_data = [
    (180, 'LV Tx\n2.5 MVA', 'A'),
    (380, 'LV Tx\n2.5 MVA', 'A'),
    (580, 'LV Tx\n2.5 MVA', 'A'),
    (1020, 'LV Tx\n2.5 MVA', 'B'),
    (1220, 'LV Tx\n2.5 MVA', 'B'),
    (1420, 'LV Tx\n2.5 MVA', 'B'),
]

for i, (x, label, feed) in enumerate(tx_data[:len(data['transformers'])]):
    feed_class = 'feed-a' if feed == 'A' else 'feed-b'
    svg += f'''
<!-- Transformer {i+1} -->
<g id="tx-{i+1}">
    <use href="#transformer" x="{x+60}" y="660"/>
    <rect x="{x+20}" y="630" width="80" height="60" class="{feed_class}"/>
    <text x="{x+60}" y="655" class="label" text-anchor="middle" font-size="9">LV Tx</text>
    <text x="{x+60}" y="675" class="rating" text-anchor="middle">200kVA</text>
    <line x1="{x+60}" y1="690" x2="{x+60}" y2="730" class="line"/>
</g>
'''

# Main Breaker Boards (MBB)
for i, (x, label, feed) in enumerate(tx_data[:len(data['lv_swbd'])]):
    feed_class = 'feed-a' if feed == 'A' else 'feed-b'
    svg += f'''
<!-- MBB {i+1} -->
<g id="mbb-{i+1}">
    <rect x="{x+10}" y="730" width="100" height="50" class="{feed_class}"/>
    <text x="{x+60}" y="750" class="label" text-anchor="middle">MBB</text>
    <text x="{x+60}" y="770" class="rating" text-anchor="middle">480V</text>
    <line x1="{x+60}" y1="780" x2="{x+60}" y2="820" class="line"/>
</g>
'''

# LV-MDB (LV Main Distribution Boards)
for i, (x, label, feed) in enumerate(tx_data[:len(data['lv_swbd'])]):
    feed_class = 'feed-a' if feed == 'A' else 'feed-b'
    svg += f'''
<!-- LV-MDB {i+1} -->
<g id="lv-mdb-{i+1}">
    <rect x="{x}" y="820" width="120" height="70" class="{feed_class}"/>
    <text x="{x+60}" y="845" class="bus-label" text-anchor="middle">LV-MDB</text>
    <text x="{x+60}" y="865" class="rating" text-anchor="middle">3200A</text>
    <text x="{x+60}" y="880" class="rating" text-anchor="middle">Feed {feed}</text>
    <line x1="{x+60}" y1="890" x2="{x+60}" y2="930" class="line"/>
</g>
'''

# UPS Systems
for i, (x, label, feed) in enumerate(tx_data[:len(data['ups'])]):
    svg += f'''
<!-- UPS {i+1} -->
<g id="ups-{i+1}">
    <use href="#ups-symbol" x="{x+60}" y="960"/>
    <rect x="{x+10}" y="930" width="100" height="60" class="box"/>
    <text x="{x+60}" y="955" class="label" text-anchor="middle">1 MW UPS</text>
    <text x="{x+60}" y="975" class="rating" text-anchor="middle">Li-ion</text>
    <line x1="{x+60}" y1="990" x2="{x+60}" y2="1030" class="line"/>
</g>
'''

# Load Distribution Boxes
load_labels = [
    ['Mechanical\nSystems and\nGeneral DBs', 'Other Critical\nSystems (BMS,\nPumps)'],
    ['Mechanical\nSystems and\nGeneral DBs', 'Other Critical\nSystems (BMS,\nPumps)'],
    ['Mechanical\nSystems and\nGeneral DBs', 'Other Critical\nSystems (BMS,\nPumps)'],
    ['Mechanical\nSystems and\nGeneral DBs', 'Other Critical\nSystems (BMS,\nPumps)'],
    ['Mechanical\nSystems and\nGeneral DBs', 'Other Critical\nSystems (BMS,\nPumps)'],
    ['Mechanical\nSystems and\nGeneral DBs', 'Other Critical\nSystems (BMS,\nPumps)'],
]

for i, (x, label, feed) in enumerate(tx_data[:4]):
    for j, load_label in enumerate(load_labels[i][:2]):
        x_offset = x + (j * 60) - 30
        svg += f'''
<!-- Load Box {i+1}-{j+1} -->
<g id="load-{i+1}-{j+1}">
    <rect x="{x_offset}" y="1030" width="55" height="80" class="box"/>
    <text x="{x_offset+27}" y="1050" class="rating" text-anchor="middle" font-size="7">{load_label.split(chr(10))[0]}</text>
    <text x="{x_offset+27}" y="1065" class="rating" text-anchor="middle" font-size="7">{load_label.split(chr(10))[1] if chr(10) in load_label else ''}</text>
    <text x="{x_offset+27}" y="1080" class="rating" text-anchor="middle" font-size="7">{load_label.split(chr(10))[2] if load_label.count(chr(10)) > 1 else ''}</text>
</g>
'''

# Data Hall Labels
data_halls = [
    (340, 'VIP'),
    (740, 'Enterprise A'),
    (940, 'Enterprise B'),
    (1340, 'Hub'),
]

for i, (x, hall_name) in enumerate(data_halls[:3]):
    svg += f'''
<g id="data-hall-{i+1}">
    <rect x="{x-40}" y="1150" width="120" height="50" fill="white" stroke="black" stroke-width="2"/>
    <text x="{x+20}" y="1180" class="bus-label" text-anchor="middle">{hall_name}</text>
</g>
'''

# Legend
svg += f'''
<!-- Legend -->
<g id="legend">
    <rect x="50" y="1950" width="300" height="180" fill="white" stroke="black" stroke-width="2"/>
    <text x="60" y="1975" class="subtitle">LEGEND:</text>
    
    <rect x="60" y="1990" width="40" height="20" class="feed-a"/>
    <text x="110" y="2005" class="rating">A Feed</text>
    
    <rect x="60" y="2020" width="40" height="20" class="feed-b"/>
    <text x="110" y="2035" class="rating">B Feed</text>
    
    <rect x="60" y="2050" width="40" height="20" class="feed-tie"/>
    <text x="110" y="2065" class="rating">Tie/Neutral</text>
    
    <circle cx="80" cy="2095" r="5" fill="white" stroke="black"/>
    <text x="95" y="2100" class="rating">NC - Normally Closed</text>
    
    <circle cx="80" cy="2115" r="5" fill="black" stroke="black"/>
    <text x="95" y="2120" class="rating">NO - Normally Open</text>
</g>

<!-- Notes -->
<g id="notes">
    <rect x="400" y="1950" width="1150" height="180" fill="white" stroke="black" stroke-width="2"/>
    <text x="410" y="1975" class="subtitle">SYSTEM NOTES:</text>
    <text x="410" y="2000" class="rating">1. Topology: Ring Bus with Dual 13.8kV MV Distribution (Self-Healing SCADA)</text>
    <text x="410" y="2020" class="rating">2. Generators: {len(data['generators'])} × {data['generators'][0]['kw']}kW @ 13.8kV (N+1, Parallel Sync via Woodward Controls)</text>
    <text x="410" y="2040" class="rating">3. RMUs: {len(data['rmu'])} Ring Main Units (630A, 20kA SCCR, SF6/Vacuum Breakers)</text>
    <text x="410" y="2060" class="rating">4. Transformers: {len(data['transformers'])} × 200kVA (13.8kV Delta / 480Y/277V, ONAN Cooling)</text>
    <text x="410" y="2080" class="rating">5. UPS: N+1 Modular Static UPS ({len(data['ups'])} modules @ {data['ups'][0]['kw']}kW, Li-ion Battery, 5min Runtime)</text>
    <text x="410" y="2100" class="rating">6. Redundancy: N+1 for all critical components | Tier III Concurrent Maintainability</text>
    <text x="410" y="2120" class="rating">7. Source: Generated from 7BOD - Electrical (CSI Div 26).md | PACHYDERM BOD Generator v1.0</text>
</g>

<!-- Footer -->
<text x="800" y="2180" class="rating" text-anchor="middle">SAGA PRYOR DATA CENTER | PACHYDERM GLOBAL | Document: GE01-PGC-EL-ST-DR-0001-C01 | {datetime.now().strftime('%m/%d/%Y')}</text>

</svg>'''

# Save
output_file = 'saga_pryor_professional_sld.svg'
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(svg)

print("=" * 80)
print("✅ PROFESSIONAL SLD GENERATED (Matching Sample Format)")
print("=" * 80)
print(f"\nFile: {output_file}")
print(f"Size: {len(svg):,} bytes")
print(f"\nStyle:")
print(f"  • Professional electrical symbols (transformers, breakers)")
print(f"  • Color-coded A/B feeds (green/blue)")
print(f"  • Proper title block and revision control")
print(f"  • NC/NO breaker states")
print(f"  • Legend and system notes")
print(f"  • Matches sample SLD layout")
print(f"\nComponents:")
print(f"  • 345kV Utility (2×25MVA)")
print(f"  • {len(data['rmu'])} RMUs with breaker states")
print(f"  • {len(data['transformers'])} Transformers")
print(f"  • {len(data['lv_swbd'])} LV-MDBs")
print(f"  • {len(data['ups'])} UPS modules")
print("=" * 80)
