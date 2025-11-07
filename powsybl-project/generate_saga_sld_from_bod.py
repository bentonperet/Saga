"""
Generate Saga Pryor SLD from actual BOD-extracted metadata
Uses saga_pryor_metadata.json generated from the real BOD file
"""
import json
from datetime import datetime
from pathlib import Path
from sld_standards import get_svg_symbols, get_svg_style_section

# Read the metadata generated from actual BOD
metadata_file = Path('saga_pryor_metadata.json')
if not metadata_file.exists():
    print("ERROR: saga_pryor_metadata.json not found!")
    print("Run test_sld_generator.py first to generate metadata from BOD")
    exit(1)

with open(metadata_file, 'r') as f:
    data = json.load(f)

print("=" * 80)
print("GENERATING SAGA PRYOR SLD FROM ACTUAL BOD")
print("=" * 80)

# Extract counts from metadata
generators = data.get('generators', [])
transformers = data.get('transformers', [])
rmus = data.get('rmu', [])
ups_systems = data.get('ups', [])
it_ups = [u for u in ups_systems if u['function'] == 'IT']
mech_ups = [u for u in ups_systems if u['function'] == 'MECHANICAL']

print(f"\nComponents from BOD:")
print(f"  Generators: {len(generators)}")
print(f"  Transformers: {len(transformers)}")
print(f"  RMUs: {len(rmus)}")
print(f"  IT UPS: {len(it_ups)}")
print(f"  Mechanical UPS: {len(mech_ups)}")

# SVG setup - ring bus layout
width = 3200
height = 2400

svg_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
{get_svg_symbols()}
{get_svg_style_section()}

<!-- Title Block -->
<rect x="50" y="20" width="3100" height="100" fill="white" stroke="black" stroke-width="2"/>
<text x="1600" y="55" class="title" text-anchor="middle">SAGA PRYOR DATA CENTER - ELECTRICAL SINGLE LINE DIAGRAM</text>
<text x="1600" y="80" class="subtitle" text-anchor="middle">13.8kV Dual Ring Bus Distribution | Tier III Architecture</text>
<text x="1600" y="100" class="annotation" text-anchor="middle">From Basis of Design: 7BOD - Electrical (CSI Div 26)</text>

<!-- Date/Revision Block -->
<text x="3050" y="50" class="label" text-anchor="end">Date: {datetime.now().strftime('%Y-%m-%d')}</text>
<text x="3050" y="70" class="label" text-anchor="end">Rev: A</text>
<text x="3050" y="90" class="annotation" text-anchor="end">Auto-generated from BOD</text>

'''

# Calculate generator positions
gen_count = len(generators)
gen_spacing = 180
gen_start_x = (width - (gen_count * gen_spacing)) // 2

# Add generators
print(f"\nAdding {gen_count} generators...")
y_gen = 180
for i, gen in enumerate(generators):
    x = gen_start_x + (i * gen_spacing)
    kw = gen.get('kw', 0)
    mw = kw / 1000
    fuel = gen.get('fuel', 'DIESEL')

    svg_content += f'''
<!-- Generator {i+1} -->
<g id="gen-{i+1}">
    <circle cx="{x}" cy="{y_gen}" r="40" fill="white" stroke="black" stroke-width="2"/>
    <text x="{x}" y="{y_gen-5}" class="bus-label" text-anchor="middle">G</text>
    <text x="{x}" y="{y_gen+10}" class="small-label" text-anchor="middle">GEN-{i+1}</text>
    <text x="{x}" y="{y_gen+25}" class="rating" text-anchor="middle" font-size="9">{mw:.1f}MW</text>
    <text x="{x}" y="{y_gen+38}" class="annotation" text-anchor="middle" font-size="8">{fuel}</text>
</g>
<!-- Gen {i+1} to Sync Bus -->
<line x1="{x}" y1="{y_gen+40}" x2="{x}" y2="{y_gen+100}" class="power-line"/>
<use href="#breaker-closed" x="{x}" y="{y_gen+70}"/>
<line x1="{x}" y1="{y_gen+100}" x2="{x}" y2="{y_gen+130}" class="power-line"/>
'''

# Generator sync bus
y_sync_bus = y_gen + 130
svg_content += f'''
<!-- Generator Sync Bus -->
<g id="sync-bus">
    <rect x="{gen_start_x - 80}" y="{y_sync_bus}" width="{gen_count * gen_spacing + 80}" height="90" class="switchgear-box"/>
    <text x="{width//2}" y="{y_sync_bus + 30}" class="equipment-label" text-anchor="middle">GENERATOR SYNC BUS</text>
    <text x="{width//2}" y="{y_sync_bus + 50}" class="rating" text-anchor="middle">13.8 kV | Woodward Paralleling Controls</text>
    <text x="{width//2}" y="{y_sync_bus + 70}" class="rating" text-anchor="middle">{gen_count} × {generators[0]['kw']/1000:.1f}MW (N+1) | Auto Load Share</text>
</g>

'''

# MV Switchboards (Ring A and Ring B)
y_mv_swbd = y_sync_bus + 150
mv_swbd_a_x = 400
mv_swbd_b_x = width - 400

svg_content += f'''
<!-- Connection from Sync Bus to MV-SWBD A -->
<line x1="{gen_start_x + gen_spacing}" y1="{y_sync_bus + 90}" x2="{gen_start_x + gen_spacing}" y2="{y_mv_swbd - 50}" class="power-line"/>
<line x1="{gen_start_x + gen_spacing}" y1="{y_mv_swbd - 50}" x2="{mv_swbd_a_x}" y2="{y_mv_swbd - 50}" class="power-line"/>
<line x1="{mv_swbd_a_x}" y1="{y_mv_swbd - 50}" x2="{mv_swbd_a_x}" y2="{y_mv_swbd}" class="power-line"/>
<use href="#breaker-closed" x="{mv_swbd_a_x}" y="{y_mv_swbd - 30}"/>

<!-- Connection from Sync Bus to MV-SWBD B -->
<line x1="{gen_start_x + (gen_count-2) * gen_spacing}" y1="{y_sync_bus + 90}" x2="{gen_start_x + (gen_count-2) * gen_spacing}" y2="{y_mv_swbd - 50}" class="power-line"/>
<line x1="{gen_start_x + (gen_count-2) * gen_spacing}" y1="{y_mv_swbd - 50}" x2="{mv_swbd_b_x}" y2="{y_mv_swbd - 50}" class="power-line"/>
<line x1="{mv_swbd_b_x}" y1="{y_mv_swbd - 50}" x2="{mv_swbd_b_x}" y2="{y_mv_swbd}" class="power-line"/>
<use href="#breaker-closed" x="{mv_swbd_b_x}" y="{y_mv_swbd - 30}"/>

<!-- MV-SWBD A (Ring A) -->
<g id="mv-swbd-a">
    <rect x="{mv_swbd_a_x - 150}" y="{y_mv_swbd}" width="300" height="120" class="switchgear-box"/>
    <text x="{mv_swbd_a_x}" y="{y_mv_swbd + 35}" class="equipment-label" text-anchor="middle">MV-SWBD A</text>
    <text x="{mv_swbd_a_x}" y="{y_mv_swbd + 55}" class="annotation" text-anchor="middle">RING A PRIMARY</text>
    <text x="{mv_swbd_a_x}" y="{y_mv_swbd + 75}" class="annotation" text-anchor="middle">13.8 kV</text>
    <text x="{mv_swbd_a_x}" y="{y_mv_swbd + 95}" class="rating" text-anchor="middle">4000A | 65kAIC</text>
</g>

<!-- MV-SWBD B (Ring B) -->
<g id="mv-swbd-b">
    <rect x="{mv_swbd_b_x - 150}" y="{y_mv_swbd}" width="300" height="120" class="switchgear-box"/>
    <text x="{mv_swbd_b_x}" y="{y_mv_swbd + 35}" class="equipment-label" text-anchor="middle">MV-SWBD B</text>
    <text x="{mv_swbd_b_x}" y="{y_mv_swbd + 55}" class="annotation" text-anchor="middle">RING B PRIMARY</text>
    <text x="{mv_swbd_b_x}" y="{y_mv_swbd + 75}" class="annotation" text-anchor="middle">13.8 kV</text>
    <text x="{mv_swbd_b_x}" y="{y_mv_swbd + 95}" class="rating" text-anchor="middle">4000A | 65kAIC</text>
</g>

'''

# Ring bus with RMUs
y_ring = y_mv_swbd + 200
ring_a_y = y_ring
ring_b_y = y_ring + 300
rmu_count = len(rmus)
rmus_per_ring = rmu_count // 2

svg_content += f'''
<!-- RING A (Top) -->
<line x1="{mv_swbd_a_x}" y1="{y_mv_swbd + 120}" x2="{mv_swbd_a_x}" y2="{ring_a_y}" class="power-line"/>
<line x1="{mv_swbd_a_x}" y1="{ring_a_y}" x2="{mv_swbd_b_x}" y2="{ring_a_y}" class="power-line"/>
<text x="{width//2}" y="{ring_a_y - 10}" class="bus-label" text-anchor="middle">RING A - 13.8 kV</text>

<!-- RING B (Bottom) -->
<line x1="{mv_swbd_a_x}" y1="{y_mv_swbd + 120}" x2="{mv_swbd_a_x}" y2="{ring_b_y}" class="power-line"/>
<line x1="{mv_swbd_a_x}" y1="{ring_b_y}" x2="{mv_swbd_b_x}" y2="{ring_b_y}" class="power-line"/>
<text x="{width//2}" y="{ring_b_y + 25}" class="bus-label" text-anchor="middle">RING B - 13.8 kV</text>

'''

# Add RMUs on rings
print(f"\nAdding {rmu_count} RMUs ({rmus_per_ring} per ring)...")
rmu_spacing = (mv_swbd_b_x - mv_swbd_a_x) // (rmus_per_ring + 1)

for i in range(rmus_per_ring):
    x = mv_swbd_a_x + (i + 1) * rmu_spacing

    # Ring A RMU
    svg_content += f'''
<!-- RMU A-{i+1} -->
<g id="rmu-a-{i+1}">
    <rect x="{x-30}" y="{ring_a_y-40}" width="60" height="80" fill="lightblue" stroke="black" stroke-width="2"/>
    <text x="{x}" y="{ring_a_y-10}" class="small-label" text-anchor="middle">RMU</text>
    <text x="{x}" y="{ring_a_y+5}" class="small-label" text-anchor="middle">A-{i+1}</text>
    <text x="{x}" y="{ring_a_y+20}" class="annotation" text-anchor="middle" font-size="8">630A</text>
</g>
'''

    # Ring B RMU
    svg_content += f'''
<!-- RMU B-{i+1} -->
<g id="rmu-b-{i+1}">
    <rect x="{x-30}" y="{ring_b_y}" width="60" height="80" fill="lightblue" stroke="black" stroke-width="2"/>
    <text x="{x}" y="{ring_b_y+30}" class="small-label" text-anchor="middle">RMU</text>
    <text x="{x}" y="{ring_b_y+45}" class="small-label" text-anchor="middle">B-{i+1}</text>
    <text x="{x}" y="{ring_b_y+60}" class="annotation" text-anchor="middle" font-size="8">630A</text>
</g>
'''

# Add transformers
print(f"\nAdding {len(transformers)} transformers...")
tx_count = len(transformers)
tx_per_side = tx_count // 2
y_transformer = ring_b_y + 150

for i, tx in enumerate(transformers):
    if i < tx_per_side:
        # Left side transformers from Ring A
        x = mv_swbd_a_x + (i * 200)
        ring_y = ring_a_y
        ring = "A"
    else:
        # Right side transformers from Ring B
        x = mv_swbd_a_x + ((i - tx_per_side) * 200)
        ring_y = ring_b_y
        ring = "B"

    kva = tx.get('rated_s', 0)
    hv = tx.get('hv_voltage', 13.8)
    lv = tx.get('lv_voltage', 0.48)

    svg_content += f'''
<!-- Transformer {i+1} from Ring {ring} -->
<line x1="{x}" y1="{ring_y if ring=='A' else ring_y+80}" x2="{x}" y2="{y_transformer}" class="power-line"/>
<use href="#breaker-closed" x="{x}" y="{(ring_y if ring=='A' else ring_y+80) + 30}"/>
<g id="tx-{i+1}">
    <circle cx="{x}" cy="{y_transformer+20}" r="35" fill="white" stroke="black" stroke-width="2"/>
    <circle cx="{x}" cy="{y_transformer+20}" r="28" fill="none" stroke="black" stroke-width="1"/>
    <text x="{x}" y="{y_transformer+10}" class="small-label" text-anchor="middle">TX-{i+1}</text>
    <text x="{x}" y="{y_transformer+25}" class="rating" text-anchor="middle" font-size="8">{kva}kVA</text>
    <text x="{x}" y="{y_transformer+70}" class="annotation" text-anchor="middle" font-size="8">{hv}kV/{lv}kV</text>
</g>
<line x1="{x}" y1="{y_transformer+55}" x2="{x}" y2="{y_transformer+120}" class="power-line"/>
'''

# Add LV switchboards
y_lv_swbd = y_transformer + 150
svg_content += f'''
<!-- LV Switchboards -->
<rect x="{mv_swbd_a_x-150}" y="{y_lv_swbd}" width="300" height="100" class="switchgear-box"/>
<text x="{mv_swbd_a_x}" y="{y_lv_swbd+35}" class="equipment-label" text-anchor="middle">LV-SWBD-A</text>
<text x="{mv_swbd_a_x}" y="{y_lv_swbd+55}" class="annotation" text-anchor="middle">480V/277V</text>
<text x="{mv_swbd_a_x}" y="{y_lv_swbd+75}" class="rating" text-anchor="middle">4000A | Copper Bus</text>

<rect x="{mv_swbd_b_x-150}" y="{y_lv_swbd}" width="300" height="100" class="switchgear-box"/>
<text x="{mv_swbd_b_x}" y="{y_lv_swbd+35}" class="equipment-label" text-anchor="middle">LV-SWBD-B</text>
<text x="{mv_swbd_b_x}" y="{y_lv_swbd+55}" class="annotation" text-anchor="middle">480V/277V</text>
<text x="{mv_swbd_b_x}" y="{y_lv_swbd+75}" class="rating" text-anchor="middle">4000A | Copper Bus</text>

<!-- UPS Systems -->
<rect x="{width//2 - 200}" y="{y_lv_swbd + 150}" width="400" height="120" fill="#ffffcc" stroke="black" stroke-width="2"/>
<text x="{width//2}" y="{y_lv_swbd + 185}" class="equipment-label" text-anchor="middle">IT UPS SYSTEM (N+1)</text>
<text x="{width//2}" y="{y_lv_swbd + 205}" class="rating" text-anchor="middle">{len(it_ups)} × {it_ups[0]['kva'] if it_ups else 1250} kVA Modules</text>
<text x="{width//2}" y="{y_lv_swbd + 225}" class="annotation" text-anchor="middle">Li-Ion Battery | 5-min Runtime</text>
<text x="{width//2}" y="{y_lv_swbd + 245}" class="annotation" text-anchor="middle">Online Double-Conversion</text>

<rect x="{width//2 + 250}" y="{y_lv_swbd + 150}" width="400" height="120" fill="#ccffcc" stroke="black" stroke-width="2"/>
<text x="{width//2 + 450}" y="{y_lv_swbd + 185}" class="equipment-label" text-anchor="middle">MECH UPS SYSTEM (N+1)</text>
<text x="{width//2 + 450}" y="{y_lv_swbd + 205}" class="rating" text-anchor="middle">{len(mech_ups)} × {mech_ups[0]['kw'] if mech_ups else 250} kW Modules</text>
<text x="{width//2 + 450}" y="{y_lv_swbd + 225}" class="annotation" text-anchor="middle">Protects Chillers/Pumps/CDUs</text>
<text x="{width//2 + 450}" y="{y_lv_swbd + 245}" class="annotation" text-anchor="middle">Static UPS</text>

<!-- Notes -->
<text x="100" y="{height - 100}" class="annotation">NOTES:</text>
<text x="100" y="{height - 80}" class="annotation">1. Dual ring topology provides N path redundancy</text>
<text x="100" y="{height - 60}" class="annotation">2. N+1 redundancy for generators, transformers, and UPS</text>
<text x="100" y="{height - 40}" class="annotation">3. RMUs enable automatic SCADA-controlled ring reconfiguration</text>
<text x="100" y="{height - 20}" class="annotation">4. IEEE Std 315 / IEC 60617 compliant symbols</text>

</svg>'''

# Save SVG
output_file = Path('saga_pryor_sld_from_bod.svg')
with open(output_file, 'w') as f:
    f.write(svg_content)

print(f"\n{'='*80}")
print(f"SUCCESS: SLD generated from actual BOD!")
print(f"{'='*80}")
print(f"\nOutput file: {output_file.absolute()}")
print(f"File size: {output_file.stat().st_size:,} bytes")
print(f"\nOpen with:")
print(f"  - Web browser (Chrome, Firefox, Edge)")
print(f"  - Inkscape for editing")
print(f"  - Adobe Illustrator")
print(f"\nTo convert to PDF:")
print(f"  - Open in browser and print to PDF")
print(f"  - Use Inkscape: File > Save As > PDF")
print(f"{'='*80}")
