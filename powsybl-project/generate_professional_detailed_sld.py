"""
Professional detailed SLD with proper ring topology and downstream distribution
Shows RMU incomer/outgoer paths, individual UPS modules, and distribution circuits
"""
import json
from datetime import datetime
from pathlib import Path
from sld_standards import get_svg_symbols, get_svg_style_section

# Read metadata
with open('saga_pryor_metadata.json', 'r') as f:
    data = json.load(f)

generators = data.get('generators', [])
transformers = data.get('transformers', [])
rmus = data.get('rmu', [])
it_ups = [u for u in data.get('ups', []) if u['function'] == 'IT']
mech_ups = [u for u in data.get('ups', []) if u['function'] == 'MECHANICAL']

print(f"Creating professional SLD with:")
print(f"  {len(generators)} generators")
print(f"  {len(transformers)} transformers")
print(f"  {len(rmus)} RMUs (3 per ring)")
print(f"  {len(it_ups)} IT UPS modules")
print(f"  {len(mech_ups)} Mechanical UPS modules")

# Large format for detail
width = 4000
height = 3200

# Calculate even spacing
rmus_per_ring = 3
tx_per_ring = len(transformers) // 2  # 4 per ring

# Horizontal spacing - distribute evenly across width
margin = 200
usable_width = width - (2 * margin)
tx_spacing = usable_width // (tx_per_ring + 1)

svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">
{get_svg_symbols()}
{get_svg_style_section()}

<style>
.ring-bus {{ stroke: #E74C3C; stroke-width: 4; fill: none; }}
.ring-bus-b {{ stroke: #3498DB; stroke-width: 4; fill: none; }}
.ups-module {{ fill: #FFF9E6; stroke: #000; stroke-width: 1.5; }}
.dist-panel {{ fill: #E8F8F5; stroke: #000; stroke-width: 1; }}
</style>

<!-- Title Block -->
<rect x="20" y="10" width="{width-40}" height="90" fill="white" stroke="black" stroke-width="2"/>
<text x="{width//2}" y="40" class="title" text-anchor="middle">SAGA PRYOR DATA CENTER - ELECTRICAL SINGLE LINE DIAGRAM</text>
<text x="{width//2}" y="60" class="subtitle" text-anchor="middle">13.8kV Dual Ring MV Distribution - Detailed Breaker and Connection Layout</text>
<text x="{width//2}" y="80" class="annotation" text-anchor="middle">From BOD: 6x4MW Gen | 8x3.5MVA TX | 6 RMUs | Dual Ring Topology</text>
<text x="{width-30}" y="90" class="annotation" text-anchor="end">Rev A - {datetime.now().strftime('%Y-%m-%d')}</text>

'''

# GENERATORS at top
gen_count = len(generators)
gen_spacing = 500
gen_start_x = (width - ((gen_count-1) * gen_spacing)) // 2

y_gen = 150
for i, gen in enumerate(generators):
    x = gen_start_x + (i * gen_spacing)
    kw = gen.get('kw', 0)
    mw = kw / 1000

    svg += f'''
<!-- Generator {i+1} -->
<circle cx="{x}" cy="{y_gen}" r="35" fill="white" stroke="black" stroke-width="2"/>
<text x="{x}" y="{y_gen-5}" class="bus-label" text-anchor="middle">G</text>
<text x="{x}" y="{y_gen+10}" class="annotation" text-anchor="middle" font-size="10">GEN-{i+1}</text>
<line x1="{x}" y1="{y_gen+35}" x2="{x}" y2="{y_gen+70}" class="power-line"/>
<use href="#breaker-closed" x="{x}" y="{y_gen+52}"/>
<text x="{x+15}" y="{y_gen+58}" class="annotation" font-size="8">CB-G{i+1}</text>
<line x1="{x}" y1="{y_gen+70}" x2="{x}" y2="{y_gen+100}" class="power-line"/>
<text x="{x}" y="{y_gen+240}" class="rating" text-anchor="middle" font-size="9">{mw:.1f}MW</text>
'''

# Generator Sync Bus
y_sync = y_gen + 100
svg += f'''
<!-- Generator Sync Bus -->
<rect x="{gen_start_x-100}" y="{y_sync}" width="{(gen_count-1)*gen_spacing+200}" height="70" class="switchgear-box"/>
<line x1="{gen_start_x-80}" y1="{y_sync+20}" x2="{gen_start_x + (gen_count-1)*gen_spacing + 80}" y2="{y_sync+20}" class="bus"/>
<text x="{width//2}" y="{y_sync+45}" class="equipment-label" text-anchor="middle">GENERATOR SYNC BUS - 13.8 kV</text>
<text x="{width//2}" y="{y_sync+60}" class="annotation" text-anchor="middle">Woodward Paralleling | {gen_count} x {generators[0]['kw']/1000:.1f}MW (N+1)</text>
'''

# MV SWITCHBOARDS
mv_swbd_a_x = 600
mv_swbd_b_x = width - 600
y_mv_swbd = y_sync + 150

svg += f'''
<!-- Main Tie from Sync Bus to MV-SWBD A -->
<line x1="{gen_start_x + gen_spacing}" y1="{y_sync+70}" x2="{gen_start_x + gen_spacing}" y2="{y_mv_swbd-60}" class="power-line"/>
<line x1="{gen_start_x + gen_spacing}" y1="{y_mv_swbd-60}" x2="{mv_swbd_a_x}" y2="{y_mv_swbd-60}" class="power-line"/>
<line x1="{mv_swbd_a_x}" y1="{y_mv_swbd-60}" x2="{mv_swbd_a_x}" y2="{y_mv_swbd-20}" class="power-line"/>
<use href="#breaker-closed" x="{mv_swbd_a_x}" y="{y_mv_swbd-40}"/>
<text x="{mv_swbd_a_x+20}" y="{y_mv_swbd-35}" class="annotation" font-size="8">CB-MA</text>

<!-- MV-SWBD A -->
<rect x="{mv_swbd_a_x-120}" y="{y_mv_swbd}" width="240" height="100" class="mv-switchboard"/>
<line x1="{mv_swbd_a_x-100}" y1="{y_mv_swbd+20}" x2="{mv_swbd_a_x+100}" y2="{y_mv_swbd+20}" class="bus"/>
<text x="{mv_swbd_a_x}" y="{y_mv_swbd+50}" class="equipment-label" text-anchor="middle">MV-SWBD A</text>
<text x="{mv_swbd_a_x}" y="{y_mv_swbd+70}" class="annotation" text-anchor="middle">13.8kV | RING A</text>
<text x="{mv_swbd_a_x}" y="{y_mv_swbd+85}" class="rating" text-anchor="middle">4000A | 65kAIC</text>

<!-- Main Tie from Sync Bus to MV-SWBD B -->
<line x1="{gen_start_x + (gen_count-2)*gen_spacing}" y1="{y_sync+70}" x2="{gen_start_x + (gen_count-2)*gen_spacing}" y2="{y_mv_swbd-60}" class="power-line"/>
<line x1="{gen_start_x + (gen_count-2)*gen_spacing}" y1="{y_mv_swbd-60}" x2="{mv_swbd_b_x}" y2="{y_mv_swbd-60}" class="power-line"/>
<line x1="{mv_swbd_b_x}" y1="{y_mv_swbd-60}" x2="{mv_swbd_b_x}" y2="{y_mv_swbd-20}" class="power-line"/>
<use href="#breaker-closed" x="{mv_swbd_b_x}" y="{y_mv_swbd-40}"/>
<text x="{mv_swbd_b_x+20}" y="{y_mv_swbd-35}" class="annotation" font-size="8">CB-MB</text>

<!-- MV-SWBD B -->
<rect x="{mv_swbd_b_x-120}" y="{y_mv_swbd}" width="240" height="100" class="mv-switchboard"/>
<line x1="{mv_swbd_b_x-100}" y1="{y_mv_swbd+20}" x2="{mv_swbd_b_x+100}" y2="{y_mv_swbd+20}" class="bus"/>
<text x="{mv_swbd_b_x}" y="{y_mv_swbd+50}" class="equipment-label" text-anchor="middle">MV-SWBD B</text>
<text x="{mv_swbd_b_x}" y="{y_mv_swbd+70}" class="annotation" text-anchor="middle">13.8kV | RING B</text>
<text x="{mv_swbd_b_x}" y="{y_mv_swbd+85}" class="rating" text-anchor="middle">4000A | 65kAIC</text>
'''

# RING A with RMUs
y_ring_a = y_mv_swbd + 200
rmu_positions_a = []
for i in range(rmus_per_ring):
    rmu_x = margin + (i + 1) * (usable_width // (rmus_per_ring + 1))
    rmu_positions_a.append(rmu_x)

svg += f'''
<!-- RING A -->
<text x="{width//2}" y="{y_ring_a-20}" class="equipment-label" text-anchor="middle" fill="#E74C3C">RING A - 13.8 kV (3 RMUs)</text>

<!-- Ring A path: MV-SWBD A -> RMU-A1 -> RMU-A2 -> RMU-A3 -> back to MV-SWBD A -->
<line x1="{mv_swbd_a_x}" y1="{y_mv_swbd+100}" x2="{mv_swbd_a_x}" y2="{y_ring_a}" class="power-line"/>
<use href="#breaker-closed" x="{mv_swbd_a_x}" y="{y_mv_swbd+120}"/>
<text x="{mv_swbd_a_x+20}" y="{y_mv_swbd+125}" class="annotation" font-size="8">CB-RA1</text>
<line x1="{mv_swbd_a_x}" y1="{y_ring_a}" x2="{rmu_positions_a[0]}" y2="{y_ring_a}" class="ring-bus"/>
'''

# RMUs on Ring A with incomer/outgoer
for i, rmu_x in enumerate(rmu_positions_a):
    next_x = rmu_positions_a[i+1] if i < len(rmu_positions_a)-1 else mv_swbd_a_x

    svg += f'''
<!-- RMU-A{i+1} with incomer/outgoer -->
<rect x="{rmu_x-50}" y="{y_ring_a-60}" width="100" height="120" class="rmu-box"/>
<text x="{rmu_x}" y="{y_ring_a-30}" class="equipment-label" text-anchor="middle">RMU-A{i+1}</text>
<text x="{rmu_x}" y="{y_ring_a-10}" class="annotation" text-anchor="middle" font-size="9">630A SF6</text>

<!-- Incomer breaker -->
<use href="#breaker-closed" x="{rmu_x-25}" y="{y_ring_a}"/>
<text x="{rmu_x-25}" y="{y_ring_a-15}" class="annotation" font-size="7">IN</text>

<!-- Bus section inside RMU -->
<line x1="{rmu_x-25}" y1="{y_ring_a}" x2="{rmu_x+25}" y2="{y_ring_a}" stroke="black" stroke-width="3"/>
<circle cx="{rmu_x}" cy="{y_ring_a}" r="4" fill="black"/>

<!-- Outgoer breaker -->
<use href="#breaker-closed" x="{rmu_x+25}" y="{y_ring_a}"/>
<text x="{rmu_x+25}" y="{y_ring_a-15}" class="annotation" font-size="7">OUT</text>

<!-- Transformer feeder (tee-off) -->
<line x1="{rmu_x}" y1="{y_ring_a}" x2="{rmu_x}" y2="{y_ring_a+30}" class="power-line"/>
<use href="#breaker-closed" x="{rmu_x}" y="{y_ring_a+15}"/>
<text x="{rmu_x+20}" y="{y_ring_a+20}" class="annotation" font-size="7">TX</text>
<line x1="{rmu_x}" y1="{y_ring_a+30}" x2="{rmu_x}" y2="{y_ring_a+60}" class="power-line"/>

<!-- Ring continuation -->
<line x1="{rmu_x+25}" y1="{y_ring_a}" x2="{next_x if i < len(rmu_positions_a)-1 else next_x}" y2="{y_ring_a}" class="ring-bus"/>
'''

# Close Ring A back to MV-SWBD A
svg += f'''
<use href="#breaker-closed" x="{mv_swbd_a_x}" y="{y_ring_a}"/>
<text x="{mv_swbd_a_x-25}" y="{y_ring_a+5}" class="annotation" font-size="8">CB-RA2</text>
<line x1="{mv_swbd_a_x}" y1="{y_ring_a}" x2="{mv_swbd_a_x}" y2="{y_mv_swbd+100}" class="power-line"/>
'''

# RING B with RMUs
y_ring_b = y_ring_a + 900  # Space for Ring A transformers and LV distribution
rmu_positions_b = []
for i in range(rmus_per_ring):
    rmu_x = margin + (i + 1) * (usable_width // (rmus_per_ring + 1))
    rmu_positions_b.append(rmu_x)

svg += f'''
<!-- RING B -->
<text x="{width//2}" y="{y_ring_b-20}" class="equipment-label" text-anchor="middle" fill="#3498DB">RING B - 13.8 kV (3 RMUs)</text>

<!-- Ring B path: MV-SWBD B -> RMU-B1 -> RMU-B2 -> RMU-B3 -> back to MV-SWBD B -->
<line x1="{mv_swbd_b_x}" y1="{y_mv_swbd+100}" x2="{mv_swbd_b_x}" y2="{y_ring_b}" class="power-line"/>
<use href="#breaker-closed" x="{mv_swbd_b_x}" y="{y_mv_swbd+120}"/>
<text x="{mv_swbd_b_x+20}" y="{y_mv_swbd+125}" class="annotation" font-size="8">CB-RB1</text>
<line x1="{mv_swbd_b_x}" y1="{y_ring_b}" x2="{rmu_positions_b[-1]}" y2="{y_ring_b}" class="ring-bus-b"/>
'''

# RMUs on Ring B (reverse order for layout)
for i in range(len(rmu_positions_b)-1, -1, -1):
    rmu_x = rmu_positions_b[i]
    prev_x = rmu_positions_b[i-1] if i > 0 else mv_swbd_b_x

    svg += f'''
<!-- RMU-B{rmus_per_ring+i+1} with incomer/outgoer -->
<rect x="{rmu_x-50}" y="{y_ring_b-60}" width="100" height="120" class="rmu-box"/>
<text x="{rmu_x}" y="{y_ring_b-30}" class="equipment-label" text-anchor="middle">RMU-B{i+1}</text>
<text x="{rmu_x}" y="{y_ring_b-10}" class="annotation" text-anchor="middle" font-size="9">630A SF6</text>

<!-- Incomer breaker -->
<use href="#breaker-closed" x="{rmu_x+25}" y="{y_ring_b}"/>
<text x="{rmu_x+25}" y="{y_ring_b-15}" class="annotation" font-size="7">IN</text>

<!-- Bus section inside RMU -->
<line x1="{rmu_x-25}" y1="{y_ring_b}" x2="{rmu_x+25}" y2="{y_ring_b}" stroke="black" stroke-width="3"/>
<circle cx="{rmu_x}" cy="{y_ring_b}" r="4" fill="black"/>

<!-- Outgoer breaker -->
<use href="#breaker-closed" x="{rmu_x-25}" y="{y_ring_b}"/>
<text x="{rmu_x-25}" y="{y_ring_b-15}" class="annotation" font-size="7">OUT</text>

<!-- Transformer feeder (tee-off) -->
<line x1="{rmu_x}" y1="{y_ring_b}" x2="{rmu_x}" y2="{y_ring_b+30}" class="power-line"/>
<use href="#breaker-closed" x="{rmu_x}" y="{y_ring_b+15}"/>
<text x="{rmu_x+20}" y="{y_ring_b+20}" class="annotation" font-size="7">TX</text>
<line x1="{rmu_x}" y1="{y_ring_b+30}" x2="{rmu_x}" y2="{y_ring_b+60}" class="power-line"/>

<!-- Ring continuation -->
<line x1="{rmu_x-25}" y1="{y_ring_b}" x2="{prev_x}" y2="{y_ring_b}" class="ring-bus-b"/>
'''

# Close Ring B
svg += f'''
<use href="#breaker-closed" x="{mv_swbd_b_x}" y="{y_ring_b}"/>
<text x="{mv_swbd_b_x-25}" y="{y_ring_b+5}" class="annotation" font-size="8">CB-RB2</text>
<line x1="{mv_swbd_b_x}" y1="{y_ring_b}" x2="{mv_swbd_b_x}" y2="{y_mv_swbd+100}" class="power-line"/>
'''

# TRANSFORMERS and LV DISTRIBUTION for Ring A
y_tx_a = y_ring_a + 60
for i in range(tx_per_ring):
    # Distribute transformers evenly across width
    tx_x = margin + (i + 1) * tx_spacing
    tx = transformers[i]
    kva = tx.get('rated_s', 0)

    svg += f'''
<!-- Transformer TX-{i+1} (Ring A) -->
<circle cx="{tx_x}" cy="{y_tx_a+50}" r="35" fill="white" stroke="black" stroke-width="2"/>
<circle cx="{tx_x}" cy="{y_tx_a+50}" r="28" fill="none" stroke="black" stroke-width="1"/>
<text x="{tx_x}" y="{y_tx_a+45}" class="annotation" text-anchor="middle" font-size="10">TX-{i+1}</text>
<text x="{tx_x}" y="{y_tx_a+58}" class="rating" text-anchor="middle" font-size="9">{kva}kVA</text>
<text x="{tx_x}" y="{y_tx_a+105}" class="annotation" text-anchor="middle" font-size="8">13.8kV/480V</text>

<!-- TX to LV-SWBD -->
<line x1="{tx_x}" y1="{y_tx_a+85}" x2="{tx_x}" y2="{y_tx_a+130}" class="power-line"/>
<use href="#breaker-closed" x="{tx_x}" y="{y_tx_a+110}"/>
<text x="{tx_x+20}" y="{y_tx_a+115}" class="annotation" font-size="7">CB-L{i+1}</text>

<!-- LV-SWBD-{i+1} -->
<rect x="{tx_x-60}" y="{y_tx_a+150}" width="120" height="80" class="lv-switchboard"/>
<line x1="{tx_x-50}" y1="{y_tx_a+165}" x2="{tx_x+50}" y2="{y_tx_a+165}" class="bus"/>
<text x="{tx_x}" y="{y_tx_a+190}" class="equipment-label" text-anchor="middle">LV-SWBD-{i+1}</text>
<text x="{tx_x}" y="{y_tx_a+210}" class="annotation" text-anchor="middle" font-size="9">480V | 2000A</text>

<!-- Distribution Panels downstream -->
<line x1="{tx_x-40}" y1="{y_tx_a+165}" x2="{tx_x-40}" y2="{y_tx_a+250}" class="power-line"/>
<use href="#breaker-closed" x="{tx_x-40}" y="{y_tx_a+235}"/>
<rect x="{tx_x-70}" y="{y_tx_a+260}" width="60" height="50" class="dist-panel"/>
<text x="{tx_x-40}" y="{y_tx_a+280}" class="annotation" text-anchor="middle" font-size="8">DP-{i+1}A</text>
<text x="{tx_x-40}" y="{y_tx_a+295}" class="annotation" text-anchor="middle" font-size="7">IT UPS</text>

<line x1="{tx_x}" y1="{y_tx_a+165}" x2="{tx_x}" y2="{y_tx_a+250}" class="power-line"/>
<use href="#breaker-closed" x="{tx_x}" y="{y_tx_a+235}"/>
<rect x="{tx_x-30}" y="{y_tx_a+260}" width="60" height="50" class="dist-panel"/>
<text x="{tx_x}" y="{y_tx_a+280}" class="annotation" text-anchor="middle" font-size="8">DP-{i+1}B</text>
<text x="{tx_x}" y="{y_tx_a+295}" class="annotation" text-anchor="middle" font-size="7">Mech UPS</text>

<line x1="{tx_x+40}" y1="{y_tx_a+165}" x2="{tx_x+40}" y2="{y_tx_a+250}" class="power-line"/>
<use href="#breaker-closed" x="{tx_x+40}" y="{y_tx_a+235}"/>
<rect x="{tx_x+10}" y="{y_tx_a+260}" width="60" height="50" class="dist-panel"/>
<text x="{tx_x+40}" y="{y_tx_a+280}" class="annotation" text-anchor="middle" font-size="8">DP-{i+1}C</text>
<text x="{tx_x+40}" y="{y_tx_a+295}" class="annotation" text-anchor="middle" font-size="7">Lighting</text>
'''

# TRANSFORMERS and LV DISTRIBUTION for Ring B
y_tx_b = y_ring_b + 60
for i in range(tx_per_ring):
    tx_idx = tx_per_ring + i
    tx_x = margin + (i + 1) * tx_spacing
    tx = transformers[tx_idx]
    kva = tx.get('rated_s', 0)

    svg += f'''
<!-- Transformer TX-{tx_idx+1} (Ring B) -->
<circle cx="{tx_x}" cy="{y_tx_b+50}" r="35" fill="white" stroke="black" stroke-width="2"/>
<circle cx="{tx_x}" cy="{y_tx_b+50}" r="28" fill="none" stroke="black" stroke-width="1"/>
<text x="{tx_x}" y="{y_tx_b+45}" class="annotation" text-anchor="middle" font-size="10">TX-{tx_idx+1}</text>
<text x="{tx_x}" y="{y_tx_b+58}" class="rating" text-anchor="middle" font-size="9">{kva}kVA</text>
<text x="{tx_x}" y="{y_tx_b+105}" class="annotation" text-anchor="middle" font-size="8">13.8kV/480V</text>

<!-- TX to LV-SWBD -->
<line x1="{tx_x}" y1="{y_tx_b+85}" x2="{tx_x}" y2="{y_tx_b+130}" class="power-line"/>
<use href="#breaker-closed" x="{tx_x}" y="{y_tx_b+110}"/>
<text x="{tx_x+20}" y="{y_tx_b+115}" class="annotation" font-size="7">CB-L{tx_idx+1}</text>

<!-- LV-SWBD-{tx_idx+1} -->
<rect x="{tx_x-60}" y="{y_tx_b+150}" width="120" height="80" class="lv-switchboard"/>
<line x1="{tx_x-50}" y1="{y_tx_b+165}" x2="{tx_x+50}" y2="{y_tx_b+165}" class="bus"/>
<text x="{tx_x}" y="{y_tx_b+190}" class="equipment-label" text-anchor="middle">LV-SWBD-{tx_idx+1}</text>
<text x="{tx_x}" y="{y_tx_b+210}" class="annotation" text-anchor="middle" font-size="9">480V | 2000A</text>

<!-- Distribution Panels downstream -->
<line x1="{tx_x-40}" y1="{y_tx_b+165}" x2="{tx_x-40}" y2="{y_tx_b+250}" class="power-line"/>
<use href="#breaker-closed" x="{tx_x-40}" y="{y_tx_b+235}"/>
<rect x="{tx_x-70}" y="{y_tx_b+260}" width="60" height="50" class="dist-panel"/>
<text x="{tx_x-40}" y="{y_tx_b+280}" class="annotation" text-anchor="middle" font-size="8">DP-{tx_idx+1}A</text>
<text x="{tx_x-40}" y="{y_tx_b+295}" class="annotation" text-anchor="middle" font-size="7">IT UPS</text>

<line x1="{tx_x}" y1="{y_tx_b+165}" x2="{tx_x}" y2="{y_tx_b+250}" class="power-line"/>
<use href="#breaker-closed" x="{tx_x}" y="{y_tx_b+235}"/>
<rect x="{tx_x-30}" y="{y_tx_b+260}" width="60" height="50" class="dist-panel"/>
<text x="{tx_x}" y="{y_tx_b+280}" class="annotation" text-anchor="middle" font-size="8">DP-{tx_idx+1}B</text>
<text x="{tx_x}" y="{y_tx_b+295}" class="annotation" text-anchor="middle" font-size="7">Mech UPS</text>

<line x1="{tx_x+40}" y1="{y_tx_b+165}" x2="{tx_x+40}" y2="{y_tx_b+250}" class="power-line"/>
<use href="#breaker-closed" x="{tx_x+40}" y="{y_tx_b+235}"/>
<rect x="{tx_x+10}" y="{y_tx_b+260}" width="60" height="50" class="dist-panel"/>
<text x="{tx_x+40}" y="{y_tx_b+280}" class="annotation" text-anchor="middle" font-size="8">DP-{tx_idx+1}C</text>
<text x="{tx_x+40}" y="{y_tx_b+295}" class="annotation" text-anchor="middle" font-size="7">Lighting</text>
'''

# INDIVIDUAL UPS MODULES at bottom
y_ups = y_tx_b + 400
ups_module_width = 70
ups_module_height = 80

# IT UPS modules
it_ups_start_x = 300
svg += f'''
<text x="{it_ups_start_x}" y="{y_ups-10}" class="equipment-label">IT UPS SYSTEM (N+1):</text>
'''

for i, ups in enumerate(it_ups):
    x = it_ups_start_x + (i * (ups_module_width + 20))
    kva = ups.get('kva', 0)

    svg += f'''
<rect x="{x}" y="{y_ups}" width="{ups_module_width}" height="{ups_module_height}" class="ups-module"/>
<text x="{x+ups_module_width//2}" y="{y_ups+25}" class="annotation" text-anchor="middle" font-size="9">IT-UPS-{i+1}</text>
<text x="{x+ups_module_width//2}" y="{y_ups+45}" class="rating" text-anchor="middle" font-size="8">{kva}kVA</text>
<text x="{x+ups_module_width//2}" y="{y_ups+60}" class="annotation" text-anchor="middle" font-size="7">Li-Ion</text>
<text x="{x+ups_module_width//2}" y="{y_ups+72}" class="annotation" text-anchor="middle" font-size="7">5-min</text>
'''

# Mechanical UPS modules
mech_ups_start_x = it_ups_start_x + (len(it_ups) * (ups_module_width + 20)) + 100
svg += f'''
<text x="{mech_ups_start_x}" y="{y_ups-10}" class="equipment-label">MECHANICAL UPS SYSTEM (N+1):</text>
'''

for i, ups in enumerate(mech_ups):
    x = mech_ups_start_x + (i * (ups_module_width + 20))
    kw = ups.get('kw', 0)

    svg += f'''
<rect x="{x}" y="{y_ups}" width="{ups_module_width}" height="{ups_module_height}" class="ups-module"/>
<text x="{x+ups_module_width//2}" y="{y_ups+25}" class="annotation" text-anchor="middle" font-size="9">M-UPS-{i+1}</text>
<text x="{x+ups_module_width//2}" y="{y_ups+45}" class="rating" text-anchor="middle" font-size="8">{kw}kW</text>
<text x="{x+ups_module_width//2}" y="{y_ups+60}" class="annotation" text-anchor="middle" font-size="7">Static</text>
<text x="{x+ups_module_width//2}" y="{y_ups+72}" class="annotation" text-anchor="middle" font-size="7">Mech Ld</text>
'''

# Notes
svg += f'''
<!-- Notes -->
<text x="50" y="{y_ups+150}" class="equipment-label">NOTES:</text>
<text x="50" y="{y_ups+170}" class="annotation">1. Ring topology: Each RMU shows INCOMER and OUTGOER breakers with transformer feeder tee-off</text>
<text x="50" y="{y_ups+190}" class="annotation">2. Each LV-SWBD feeds 3 distribution panels: IT UPS loads, Mechanical UPS loads, and Lighting/Receptacles</text>
<text x="50" y="{y_ups+210}" class="annotation">3. All breaker positions shown at each connection point</text>
<text x="50" y="{y_ups+230}" class="annotation">4. Ring A (red) and Ring B (blue) operate independently for N path redundancy</text>
<text x="50" y="{y_ups+250}" class="annotation">5. Individual UPS modules shown: {len(it_ups)} IT UPS modules + {len(mech_ups)} Mechanical UPS modules</text>

</svg>'''

output = Path('saga_pryor_sld_PROFESSIONAL.svg')
with open(output, 'w', encoding='utf-8') as f:
    f.write(svg)

print(f"\nCreated professional detailed SLD: {output}")
print(f"Size: {width} x {height} pixels")
print(f"\nKey features:")
print(f"  ✓ RMU incomer/outgoer connections shown")
print(f"  ✓ Ring topology paths clearly marked (Ring A/Ring B)")
print(f"  ✓ Each LV-SWBD with 3 downstream distribution panels")
print(f"  ✓ Equal spacing: {tx_spacing}px between equipment")
print(f"  ✓ Individual UPS modules: {len(it_ups)} IT + {len(mech_ups)} Mech")
print(f"  ✓ All breaker positions labeled")
print(f"\nOpening in browser...")
