"""
Custom SVG Single-Line Diagram Generator for Saga Pryor Data Center
Creates a visual representation of the electrical system from the metadata.
"""

import json

# Read the metadata
with open('pachyderm_metadata.json', 'r') as f:
    data = json.load(f)

# SVG dimensions
width = 1400
height = 1800
margin = 50

# Create SVG with electrical symbols
svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
<style>
    .title {{ font: bold 24px sans-serif; fill: #1a1a1a; }}
    .subtitle {{ font: bold 16px sans-serif; fill: #333; }}
    .label {{ font: 12px monospace; fill: #000; }}
    .rating {{ font: 11px sans-serif; fill: #666; }}
    .bus {{ stroke: #2c5aa0; stroke-width: 4; fill: none; }}
    .gen {{ fill: #4CAF50; stroke: #2e7d32; stroke-width: 2; }}
    .tx {{ fill: #FF9800; stroke: #F57C00; stroke-width: 2; }}
    .ups {{ fill: #9C27B0; stroke: #6A1B9A; stroke-width: 2; }}
    .rmu {{ fill: #2196F3; stroke: #1565C0; stroke-width: 2; }}
    .swbd {{ fill: #607D8B; stroke: #37474F; stroke-width: 2; }}
    .line {{ stroke: #333; stroke-width: 2; fill: none; }}
    .breaker {{ fill: white; stroke: #333; stroke-width: 2; }}
</style>

<!-- Title -->
<text x="{width/2}" y="40" class="title" text-anchor="middle">SAGA PRYOR DATA CENTER</text>
<text x="{width/2}" y="65" class="subtitle" text-anchor="middle">Electrical Single-Line Diagram - Ring Bus Topology</text>
<text x="{width/2}" y="85" class="rating" text-anchor="middle">PACHYDERM GLOBAL | Tier III | 345kV/13.8kV</text>

<!-- 345kV Utility -->
<g id="utility">
    <rect x="600" y="120" width="200" height="60" class="swbd"/>
    <text x="700" y="145" class="label" text-anchor="middle">345kV UTILITY</text>
    <text x="700" y="165" class="rating" text-anchor="middle">2 × 25MVA Transformers</text>
</g>

<!-- 13.8kV Ring Bus -->
<g id="ring-bus">
    <!-- Ring outline -->
    <ellipse cx="700" cy="400" rx="350" ry="200" class="bus"/>
    
    <!-- Ring segments labels -->
    <text x="700" y="220" class="subtitle" text-anchor="middle">13.8 kV DUAL-RING DISTRIBUTION</text>
</g>

<!-- Connection from utility to ring -->
<line x1="700" y1="180" x2="700" y2="200" class="line"/>

<!-- RMUs around the ring -->
'''

# RMU positions (around the ellipse)
rmu_positions = [
    (700, 200),   # Top - RMU_1
    (1050, 400),  # Right - RMU_2
    (700, 600),   # Bottom - RMU_3
    (350, 400),   # Left - RMU_4
]

for i, (rmu_id, pos) in enumerate(zip(data['rmu'], rmu_positions)):
    x, y = pos
    svg += f'''
<!-- {rmu_id} -->
<g id="{rmu_id}">
    <rect x="{x-40}" y="{y-25}" width="80" height="50" class="rmu"/>
    <text x="{x}" y="{y-5}" class="label" text-anchor="middle">{rmu_id}</text>
    <text x="{x}" y="{y+10}" class="rating" text-anchor="middle">630A</text>
    <text x="{x}" y="{y+23}" class="rating" text-anchor="middle">20kA</text>
</g>
'''

# Generators with parallel sync bus
svg += '''
<!-- Sync Bus for Parallel Generators -->
<g id="sync-bus">
    <rect x="100" y="350" width="150" height="100" class="swbd"/>
    <text x="175" y="390" class="label" text-anchor="middle">SYNC BUS</text>
    <text x="175" y="410" class="rating" text-anchor="middle">Parallel Gen</text>
    <text x="175" y="430" class="rating" text-anchor="middle">Woodward</text>
</g>
'''

# Generators
gen_y_start = 250
for i, gen in enumerate(data['generators'][:5]):
    y = gen_y_start + (i * 60)
    svg += f'''
<!-- {gen['id']} -->
<g id="{gen['id']}">
    <circle cx="50" cy="{y}" r="25" class="gen"/>
    <text x="50" y="{y+5}" class="label" text-anchor="middle" font-size="10">G{i+1}</text>
    <line x1="75" y1="{y}" x2="100" y2="{y}" class="line"/>
    <text x="10" y="{y-30}" class="rating">{gen['kw']}kW</text>
    <text x="10" y="{y-15}" class="rating">{gen['fuel']}</text>
</g>
'''

# Connect sync bus to ring
svg += '''
<line x1="250" y1="400" x2="350" y2="400" class="line"/>
<text x="300" y="390" class="rating" text-anchor="middle">To Ring</text>
'''

# Transformers connected to RMUs
tx_positions = [
    (700, 670),   # TX_1 from RMU_1
    (1120, 400),  # TX_2 from RMU_2
    (700, 730),   # TX_3 from RMU_3
    (280, 400),   # TX_4 from RMU_4
]

for i, (tx, pos) in enumerate(zip(data['transformers'], tx_positions)):
    x, y = pos
    rmu_id = tx['hv_bus'].replace('_BUS', '')
    
    svg += f'''
<!-- {tx['id']} -->
<g id="{tx['id']}">
    <circle cx="{x}" cy="{y}" r="30" class="tx"/>
    <text x="{x}" y="{y+5}" class="label" text-anchor="middle" font-size="10">TX{i+1}</text>
    <text x="{x+45}" y="{y-10}" class="rating">{tx['rated_s']}kVA</text>
    <text x="{x+45}" y="{y+5}" class="rating">13.8kV/</text>
    <text x="{x+45}" y="{y+20}" class="rating">480V</text>
</g>
'''

# LV Switchboards
lv_y_base = 830
for i, swbd in enumerate(data['lv_swbd']):
    x = 300 + (i * 280)
    
    svg += f'''
<!-- {swbd['id']} -->
<g id="{swbd['id']}">
    <rect x="{x-60}" y="{lv_y_base}" width="120" height="60" class="swbd"/>
    <text x="{x}" y="{lv_y_base+25}" class="label" text-anchor="middle">{swbd['id']}</text>
    <text x="{x}" y="{lv_y_base+45}" class="rating" text-anchor="middle">480V | {swbd['rating_a']}A</text>
</g>
'''

# UPS Systems
ups_y = 950
for i, ups in enumerate(data['ups']):
    x = 300 + (i * 280)
    
    svg += f'''
<!-- {ups['id']} -->
<g id="{ups['id']}">
    <rect x="{x-50}" y="{ups_y}" width="100" height="70" class="ups"/>
    <text x="{x}" y="{ups_y+25}" class="label" text-anchor="middle">{ups['id']}</text>
    <text x="{x}" y="{ups_y+40}" class="rating" text-anchor="middle">{ups['type']}</text>
    <text x="{x}" y="{ups_y+55}" class="rating" text-anchor="middle">{ups['kw']}kW</text>
    <text x="{x}" y="{ups_y+65}" class="rating" text-anchor="middle">{ups['battery']}</text>
</g>
'''

# PDUs
pdu_y = 1080
for i, pdu in enumerate(data['pdus']):
    x = 300 + (i * 280)
    
    svg += f'''
<!-- {pdu['id']} -->
<g id="{pdu['id']}">
    <rect x="{x-40}" y="{pdu_y}" width="80" height="40" rx="5" ry="5" fill="#00BCD4" stroke="#006064" stroke-width="2"/>
    <text x="{x}" y="{pdu_y+25}" class="label" text-anchor="middle" font-size="10">{pdu['id']}</text>
</g>
'''

# Earthing Transformer
if data['earthing_tx']:
    earth = data['earthing_tx'][0]
    svg += f'''
<!-- Earthing Transformer -->
<g id="earthing">
    <rect x="1100" y="250" width="150" height="80" fill="#FFC107" stroke="#F57F17" stroke-width="2"/>
    <text x="1175" y="275" class="label" text-anchor="middle">{earth['id']}</text>
    <text x="1175" y="295" class="rating" text-anchor="middle">{earth['type']}</text>
    <text x="1175" y="310" class="rating" text-anchor="middle">{earth['rated_kva']} kVA</text>
    <text x="1175" y="325" class="rating" text-anchor="middle">R={earth['impedance']['r_ohm']:.1f}Ω</text>
</g>
'''

# Legend
svg += f'''
<!-- Legend -->
<g id="legend">
    <text x="50" y="1200" class="subtitle">LEGEND:</text>
    
    <circle cx="70" cy="1230" r="15" class="gen"/>
    <text x="100" y="1235" class="rating">Generator (N+1)</text>
    
    <rect x="55" y="1250" width="30" height="20" class="rmu"/>
    <text x="100" y="1265" class="rating">Ring Main Unit (RMU)</text>
    
    <circle cx="70" cy="1290" r="15" class="tx"/>
    <text x="100" y="1295" class="rating">Transformer</text>
    
    <rect x="55" y="1310" width="30" height="20" class="swbd"/>
    <text x="100" y="1325" class="rating">Switchboard</text>
    
    <rect x="55" y="1340" width="30" height="20" class="ups"/>
    <text x="100" y="1355" class="rating">UPS Module</text>
</g>

<!-- System Info -->
<g id="info">
    <text x="400" y="1220" class="subtitle">SYSTEM SPECIFICATIONS:</text>
    <text x="400" y="1245" class="rating">• Topology: Ring Bus with Dual 13.8kV Distribution</text>
    <text x="400" y="1265" class="rating">• Generators: {len(data['generators'])} × {data['generators'][0]['kw']}kW @ 13.8kV (Parallel)</text>
    <text x="400" y="1285" class="rating">• Transformers: {len(data['transformers'])} × {data['transformers'][0]['rated_s']}kVA (13.8kV/480V)</text>
    <text x="400" y="1305" class="rating">• RMUs: {len(data['rmu'])} units (630A, 20kA SCCR)</text>
    <text x="400" y="1325" class="rating">• UPS: {len(data['ups'])} modules @ {data['ups'][0]['kw']}kW each</text>
    <text x="400" y="1345" class="rating">• Redundancy: N+1 (Generators, TX, UPS)</text>
    <text x="400" y="1365" class="rating">• Tier: III (Concurrent Maintainability)</text>
</g>

<!-- Footer -->
<text x="{width/2}" y="1450" class="rating" text-anchor="middle">Generated from: 7BOD - Electrical (CSI Div 26).md</text>
<text x="{width/2}" y="1470" class="rating" text-anchor="middle">PACHYDERM BOD Generator | {data['topology'].upper()} Topology | Auto-generated {len(data['buses'])} buses, {len(data['generators'])} generators, {len(data['transformers'])} transformers</text>

</svg>'''

# Save the SVG
output_file = 'saga_pryor_electrical_sld.svg'
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(svg)

print("=" * 80)
print("✅ SVG SINGLE-LINE DIAGRAM GENERATED")
print("=" * 80)
print(f"\nFile: {output_file}")
print(f"Size: {len(svg):,} bytes")
print(f"\nComponents visualized:")
print(f"  • {len(data['generators'])} Generators")
print(f"  • {len(data['rmu'])} RMUs")
print(f"  • {len(data['transformers'])} Transformers")
print(f"  • {len(data['lv_swbd'])} LV Switchboards")
print(f"  • {len(data['ups'])} UPS Modules")
print(f"  • {len(data['pdus'])} PDUs")
print(f"  • {len(data['earthing_tx'])} Earthing Transformer")
print(f"\nTopology: {data['topology'].upper()}")
print(f"\nOpen in browser: {output_file}")
print("=" * 80)
