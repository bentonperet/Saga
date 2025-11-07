"""
Generate detailed SLD with individual breaker positions and feeders
Matches professional SLD format with all breaker connection points shown
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

print(f"Creating detailed SLD with:")
print(f"  {len(generators)} generators")
print(f"  {len(transformers)} transformers")
print(f"  {len(rmus)} RMUs")

# Large layout to accommodate detail
width = 3400
height = 3000

svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">
{get_svg_symbols()}
{get_svg_style_section()}

<style>
.mv-switchboard {{ fill: #E8F4F8; stroke: #000; stroke-width: 2; }}
.lv-switchboard {{ fill: #F0F8E8; stroke: #000; stroke-width: 2; }}
.rmu-box {{ fill: #FFF8E8; stroke: #000; stroke-width: 2; }}
.feeder-label {{ font: 9px Arial; fill: #666; }}
</style>

<!-- Title -->
<rect x="20" y="10" width="{width-40}" height="80" fill="white" stroke="black" stroke-width="2"/>
<text x="{width//2}" y="40" class="title" text-anchor="middle">SAGA PRYOR DATA CENTER - ELECTRICAL SINGLE LINE DIAGRAM</text>
<text x="{width//2}" y="60" class="subtitle" text-anchor="middle">13.8kV Dual Ring MV Distribution with Individual Breaker Positions</text>
<text x="{width-30}" y="80" class="annotation" text-anchor="end">Rev A - {datetime.now().strftime('%Y-%m-%d')}</text>

'''

# Generators at top - spread evenly
gen_count = len(generators)
gen_spacing = 400
gen_start_x = (width - (gen_count * gen_spacing)) // 2 + 200

y_gen = 150
for i, gen in enumerate(generators):
    x = gen_start_x + (i * gen_spacing)
    kw = gen.get('kw', 0)
    mw = kw / 1000

    svg += f'''
<!-- Generator {i+1} -->
<circle cx="{x}" cy="{y_gen}" r="40" fill="white" stroke="black" stroke-width="2"/>
<text x="{x}" y="{y_gen-5}" class="bus-label" text-anchor="middle">G</text>
<text x="{x}" y="{y_gen+10}" class="small-label" text-anchor="middle">GEN-{i+1}</text>
<text x="{x}" y="{y_gen+25}" class="rating" text-anchor="middle" font-size="9">{mw:.1f}MW</text>
<line x1="{x}" y1="{y_gen+40}" x2="{x}" y2="{y_gen+80}" class="power-line"/>
<use href="#breaker-closed" x="{x}" y="{y_gen+60}"/>
<line x1="{x}" y1="{y_gen+80}" x2="{x}" y2="{y_gen+110}" class="power-line"/>
'''

# Generator Sync Bus
y_sync = y_gen + 110
svg += f'''
<!-- Generator Sync Bus -->
<rect x="{gen_start_x-80}" y="{y_sync}" width="{gen_count * gen_spacing + 80}" height="80" class="switchgear-box"/>
<text x="{width//2}" y="{y_sync+30}" class="equipment-label" text-anchor="middle">GENERATOR SYNC BUS</text>
<text x="{width//2}" y="{y_sync+50}" class="rating" text-anchor="middle">13.8 kV | {gen_count} x {generators[0]['kw']/1000:.1f}MW (N+1)</text>
<text x="{width//2}" y="{y_sync+65}" class="annotation" text-anchor="middle">Woodward Paralleling Controls | Auto Load Share</text>
'''

# MV Switchboards - one on each side
mv_swbd_a_x = 500
mv_swbd_b_x = width - 500
y_mv_swbd = y_sync + 150

# Feeder positions (4 feeders per MV switchboard for the 8 transformers via RMUs)
feeders_per_swbd = 4
feeder_spacing = 120

# MV-SWBD A (LEFT)
svg += f'''
<!-- Connection from Sync Bus to MV-SWBD A -->
<line x1="{gen_start_x + gen_spacing}" y1="{y_sync+80}" x2="{gen_start_x + gen_spacing}" y2="{y_mv_swbd-80}" class="power-line"/>
<line x1="{gen_start_x + gen_spacing}" y1="{y_mv_swbd-80}" x2="{mv_swbd_a_x}" y2="{y_mv_swbd-80}" class="power-line"/>
<line x1="{mv_swbd_a_x}" y1="{y_mv_swbd-80}" x2="{mv_swbd_a_x}" y2="{y_mv_swbd-30}" class="power-line"/>
<use href="#breaker-closed" x="{mv_swbd_a_x}" y="{y_mv_swbd-50}"/>
<line x1="{mv_swbd_a_x}" y1="{y_mv_swbd-30}" x2="{mv_swbd_a_x}" y2="{y_mv_swbd}" class="power-line"/>

<!-- MV-SWBD A -->
<rect x="{mv_swbd_a_x - feeder_spacing*2 - 20}" y="{y_mv_swbd}" width="{feeder_spacing * feeders_per_swbd + 40}" height="120" class="mv-switchboard"/>
<text x="{mv_swbd_a_x}" y="{y_mv_swbd+35}" class="equipment-label" text-anchor="middle">MV-SWBD A</text>
<text x="{mv_swbd_a_x}" y="{y_mv_swbd+55}" class="annotation" text-anchor="middle">RING A PRIMARY</text>
<text x="{mv_swbd_a_x}" y="{y_mv_swbd+75}" class="annotation" text-anchor="middle">13.8 kV</text>
<text x="{mv_swbd_a_x}" y="{y_mv_swbd+95}" class="rating" text-anchor="middle">4000A | 65kAIC</text>

<!-- MV-SWBD A Main Bus (horizontal inside box) -->
<line x1="{mv_swbd_a_x - feeder_spacing*2}" y1="{y_mv_swbd+15}" x2="{mv_swbd_a_x + feeder_spacing*2}" y2="{y_mv_swbd+15}" class="bus"/>
'''

# Add feeder positions on MV-SWBD A
for i in range(feeders_per_swbd):
    feeder_x = mv_swbd_a_x - feeder_spacing*1.5 + (i * feeder_spacing)
    svg += f'''
<!-- MV-SWBD A - Feeder {i+1} -->
<line x1="{feeder_x}" y1="{y_mv_swbd+15}" x2="{feeder_x}" y2="{y_mv_swbd+120}" class="power-line"/>
<use href="#breaker-closed" x="{feeder_x}" y="{y_mv_swbd+140}"/>
<text x="{feeder_x}" y="{y_mv_swbd+108}" class="feeder-label" text-anchor="middle">Feeder A{i+1}</text>
'''

# MV-SWBD B (RIGHT)
svg += f'''
<!-- Connection from Sync Bus to MV-SWBD B -->
<line x1="{gen_start_x + (gen_count-2) * gen_spacing}" y1="{y_sync+80}" x2="{gen_start_x + (gen_count-2) * gen_spacing}" y2="{y_mv_swbd-80}" class="power-line"/>
<line x1="{gen_start_x + (gen_count-2) * gen_spacing}" y1="{y_mv_swbd-80}" x2="{mv_swbd_b_x}" y2="{y_mv_swbd-80}" class="power-line"/>
<line x1="{mv_swbd_b_x}" y1="{y_mv_swbd-80}" x2="{mv_swbd_b_x}" y2="{y_mv_swbd-30}" class="power-line"/>
<use href="#breaker-closed" x="{mv_swbd_b_x}" y="{y_mv_swbd-50}"/>
<line x1="{mv_swbd_b_x}" y1="{y_mv_swbd-30}" x2="{mv_swbd_b_x}" y2="{y_mv_swbd}" class="power-line"/>

<!-- MV-SWBD B -->
<rect x="{mv_swbd_b_x - feeder_spacing*2 - 20}" y="{y_mv_swbd}" width="{feeder_spacing * feeders_per_swbd + 40}" height="120" class="mv-switchboard"/>
<text x="{mv_swbd_b_x}" y="{y_mv_swbd+35}" class="equipment-label" text-anchor="middle">MV-SWBD B</text>
<text x="{mv_swbd_b_x}" y="{y_mv_swbd+55}" class="annotation" text-anchor="middle">RING B PRIMARY</text>
<text x="{mv_swbd_b_x}" y="{y_mv_swbd+75}" class="annotation" text-anchor="middle">13.8 kV</text>
<text x="{mv_swbd_b_x}" y="{y_mv_swbd+95}" class="rating" text-anchor="middle">4000A | 65kAIC</text>

<!-- MV-SWBD B Main Bus -->
<line x1="{mv_swbd_b_x - feeder_spacing*2}" y1="{y_mv_swbd+15}" x2="{mv_swbd_b_x + feeder_spacing*2}" y2="{y_mv_swbd+15}" class="bus"/>
'''

# Add feeder positions on MV-SWBD B
for i in range(feeders_per_swbd):
    feeder_x = mv_swbd_b_x - feeder_spacing*1.5 + (i * feeder_spacing)
    svg += f'''
<!-- MV-SWBD B - Feeder {i+1} -->
<line x1="{feeder_x}" y1="{y_mv_swbd+15}" x2="{feeder_x}" y2="{y_mv_swbd+120}" class="power-line"/>
<use href="#breaker-closed" x="{feeder_x}" y="{y_mv_swbd+140}"/>
<text x="{feeder_x}" y="{y_mv_swbd+108}" class="feeder-label" text-anchor="middle">Feeder B{i+1}</text>
'''

# RMUs, Transformers, and LV Switchboards
# Layout: 4 on left (from MV-SWBD A), 4 on right (from MV-SWBD B)
y_rmu = y_mv_swbd + 250

for i in range(len(transformers)):
    if i < feeders_per_swbd:
        # Left side - from MV-SWBD A
        feeder_x = mv_swbd_a_x - feeder_spacing*1.5 + (i * feeder_spacing)
        side = "A"
    else:
        # Right side - from MV-SWBD B
        feeder_x = mv_swbd_b_x - feeder_spacing*1.5 + ((i-feeders_per_swbd) * feeder_spacing)
        side = "B"

    tx = transformers[i]
    kva = tx.get('rated_s', 0)
    hv = tx.get('hv_voltage', 13.8)
    lv = tx.get('lv_voltage', 0.48)

    # Feeder from MV switchboard to RMU
    svg += f'''
<!-- Feeder {side}{(i%feeders_per_swbd)+1} to RMU-{i+1} -->
<line x1="{feeder_x}" y1="{y_mv_swbd+160}" x2="{feeder_x}" y2="{y_rmu-30}" class="power-line"/>

<!-- RMU-{i+1} -->
<rect x="{feeder_x-60}" y="{y_rmu}" width="120" height="100" class="rmu-box"/>
<text x="{feeder_x}" y="{y_rmu+30}" class="equipment-label" text-anchor="middle">RMU-{i+1}</text>
<text x="{feeder_x}" y="{y_rmu+50}" class="annotation" text-anchor="middle">Ring Main Unit</text>
<text x="{feeder_x}" y="{y_rmu+70}" class="rating" text-anchor="middle">13.8kV | 630A</text>
<text x="{feeder_x}" y="{y_rmu+85}" class="annotation" text-anchor="middle">SF6 Breakers</text>

<!-- RMU to Transformer -->
<line x1="{feeder_x}" y1="{y_rmu+100}" x2="{feeder_x}" y2="{y_rmu+130}" class="power-line"/>
<use href="#breaker-closed" x="{feeder_x}" y="{y_rmu+115}"/>

<!-- Transformer TX-{i+1} -->
<circle cx="{feeder_x}" cy="{y_rmu+180}" r="40" fill="white" stroke="black" stroke-width="2"/>
<circle cx="{feeder_x}" cy="{y_rmu+180}" r="32" fill="none" stroke="black" stroke-width="1"/>
<text x="{feeder_x}" y="{y_rmu+170}" class="small-label" text-anchor="middle">TX-{i+1}</text>
<text x="{feeder_x}" y="{y_rmu+187}" class="rating" text-anchor="middle" font-size="9">{kva}kVA</text>
<text x="{feeder_x}" y="{y_rmu+240}" class="annotation" text-anchor="middle">{hv}kV/{lv}kV</text>

<!-- Transformer to LV Switchboard -->
<line x1="{feeder_x}" y1="{y_rmu+220}" x2="{feeder_x}" y2="{y_rmu+270}" class="power-line"/>
<use href="#breaker-closed" x="{feeder_x}" y="{y_rmu+250}"/>

<!-- LV-SWBD-{i+1} -->
<rect x="{feeder_x-60}" y="{y_rmu+290}" width="120" height="120" class="lv-switchboard"/>
<text x="{feeder_x}" y="{y_rmu+320}" class="equipment-label" text-anchor="middle">LV-SWBD-{i+1}</text>
<text x="{feeder_x}" y="{y_rmu+340}" class="annotation" text-anchor="middle">480V/277V</text>
<text x="{feeder_x}" y="{y_rmu+360}" class="rating" text-anchor="middle">Distribution Panel</text>
<text x="{feeder_x}" y="{y_rmu+380}" class="annotation" text-anchor="middle">Dual-Fed Loads</text>

<!-- LV Feeder -->
<line x1="{feeder_x}" y1="{y_rmu+410}" x2="{feeder_x}" y2="{y_rmu+450}" class="power-line"/>
<use href="#breaker-closed" x="{feeder_x}" y="{y_rmu+430}"/>
<line x1="{feeder_x}" y1="{y_rmu+450}" x2="{feeder_x}" y2="{y_rmu+480}" class="power-line"/>
'''

# UPS and additional info
y_ups = y_rmu + 530
svg += f'''
<!-- IT UPS System -->
<rect x="300" y="{y_ups}" width="600" height="120" fill="#FFFFCC" stroke="black" stroke-width="2"/>
<text x="600" y="{y_ups+35}" class="equipment-label" text-anchor="middle">IT UPS SYSTEM (N+1)</text>
<text x="600" y="{y_ups+55}" class="rating" text-anchor="middle">{len(it_ups)} x {it_ups[0]['kva'] if it_ups else 0} kVA Modular UPS</text>
<text x="600" y="{y_ups+75}" class="annotation" text-anchor="middle">Li-Ion Battery | 5-min Runtime</text>
<text x="600" y="{y_ups+95}" class="annotation" text-anchor="middle">Online Double-Conversion | Feeds IT Cabinets</text>

<!-- Mechanical UPS System -->
<rect x="1000" y="{y_ups}" width="600" height="120" fill="#CCFFCC" stroke="black" stroke-width="2"/>
<text x="1300" y="{y_ups+35}" class="equipment-label" text-anchor="middle">MECHANICAL UPS SYSTEM (N+1)</text>
<text x="1300" y="{y_ups+55}" class="rating" text-anchor="middle">{len(mech_ups)} x {mech_ups[0]['kw'] if mech_ups else 0} kW Static UPS</text>
<text x="1300" y="{y_ups+75}" class="annotation" text-anchor="middle">Protects Chillers, Pumps, CDUs, CRAH Units</text>
<text x="1300" y="{y_ups+95}" class="annotation" text-anchor="middle">Covers Generator Start/Sync Time (~30-60 sec)</text>

<!-- Notes -->
<text x="50" y="{y_ups+180}" class="equipment-label">NOTES:</text>
<text x="50" y="{y_ups+200}" class="annotation">1. All breaker positions shown with breaker symbols at each connection point</text>
<text x="50" y="{y_ups+220}" class="annotation">2. Each RMU enables ring reconfiguration for concurrent maintainability</text>
<text x="50" y="{y_ups+240}" class="annotation">3. Dual ring topology (Ring A/Ring B) provides N path redundancy</text>
<text x="50" y="{y_ups+260}" class="annotation">4. N+1 redundancy for generators, transformers, and UPS systems</text>
<text x="50" y="{y_ups+280}" class="annotation">5. Each LV switchboard serves dual-fed distribution panels for cabinet PDUs</text>
<text x="50" y="{y_ups+300}" class="annotation">6. Total IT capacity: {sum(u['kva'] for u in it_ups)/1000:.1f} MVA | Total mechanical: {sum(u['kw'] for u in mech_ups)/1000:.1f} MW</text>

</svg>'''

output = Path('saga_pryor_sld_DETAILED.svg')
with open(output, 'w', encoding='utf-8') as f:
    f.write(svg)

print(f"\nCreated detailed SLD: {output}")
print(f"Size: {width} x {height} pixels")
print(f"\nFeatures:")
print(f"  - Individual breaker positions on MV switchboards")
print(f"  - {feeders_per_swbd} feeders per MV switchboard")
print(f"  - Breaker symbols at every connection point")
print(f"  - {len(transformers)} complete vertical paths (RMU -> TX -> LV-SWBD)")
print(f"  - Professional single-line format")
print(f"\nOpening in browser...")
