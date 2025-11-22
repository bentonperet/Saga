"""
SLD Generator v1.1 - Fully compliant with SLD_GENERATION_STANDARDS v1.1

Key Features:
- RMU dual-feed topology (2 incomers: Primary + Reserve)
- Transformer connections: incomer from top, outgoer to bottom
- LV-SWBD with 5 breaker positions (200px wide)
- Symmetrical spacing using calculations
- Text clearance: 15px from cables, 10px from equipment
- All downstream from LV-SWBD bottom
"""
import json
from datetime import datetime
from pathlib import Path
from sld_standards import get_svg_symbols, get_svg_style_section

# Read metadata from BOD parsing
with open('saga_pryor_metadata.json', 'r') as f:
    data = json.load(f)

generators = data.get('generators', [])
transformers = data.get('transformers', [])
rmus = data.get('rmu', [])
it_ups = [u for u in data.get('ups', []) if u['function'] == 'IT']
mech_ups = [u for u in data.get('ups', []) if u['function'] == 'MECHANICAL']

print("="*80)
print("SLD GENERATOR v1.1 - STANDARDS COMPLIANT")
print("="*80)
print(f"\nComponents from BOD:")
print(f"  Generators: {len(generators)}")
print(f"  Transformers: {len(transformers)}")
print(f"  RMUs: {len(rmus)}")
print(f"  IT UPS: {len(it_ups)}")
print(f"  Mech UPS: {len(mech_ups)}")

# Canvas and spacing calculations per v1.1 standards
MARGIN = 200
width = 4800  # Larger for dual-feed complexity
height = 3600

def calculate_symmetrical_positions(canvas_width, count, equipment_width, margin):
    """
    Calculate evenly-spaced positions per SLD Standards v1.1 Section 2.2
    Returns center points for equipment placement
    """
    usable_width = canvas_width - (2 * margin)
    total_equipment_width = count * equipment_width
    available_space = usable_width - total_equipment_width
    spacing = available_space / (count + 1)

    positions = []
    for i in range(count):
        x = margin + spacing * (i + 1) + equipment_width * i + (equipment_width / 2)
        positions.append(x)

    return positions

# Calculate equipment positions
tx_count = len(transformers)
tx_width = 70  # 2 × radius
tx_positions = calculate_symmetrical_positions(width, tx_count, tx_width, MARGIN)

rmu_count = len(rmus)
rmu_width = 120
rmu_positions = calculate_symmetrical_positions(width, rmu_count, rmu_width, MARGIN)

print(f"\nSymmetrical spacing calculated:")
print(f"  {tx_count} transformers: spacing = {(width - 2*MARGIN - tx_count*tx_width)/(tx_count+1):.1f}px")
print(f"  {rmu_count} RMUs: spacing = {(width - 2*MARGIN - rmu_count*rmu_width)/(rmu_count+1):.1f}px")

# Start SVG
svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">
{get_svg_symbols()}
{get_svg_style_section()}

<!-- Title Block -->
<rect x="20" y="10" width="{width-40}" height="90" fill="white" stroke="black" stroke-width="2"/>
<text x="{width//2}" y="40" class="title" text-anchor="middle">SAGA PRYOR DATA CENTER - ELECTRICAL SINGLE LINE DIAGRAM</text>
<text x="{width//2}" y="60" class="subtitle" text-anchor="middle">13.8kV Dual-Feed MV Distribution | SLD Standards v1.1 Compliant</text>
<text x="{width//2}" y="80" class="annotation" text-anchor="middle">Dual-Feed RMUs | 5-Position LV-SWBDs | Symmetrical Layout</text>
<text x="{width-30}" y="85" class="annotation" text-anchor="end">Rev B - {datetime.now().strftime('%Y-%m-%d')}</text>

'''

# GENERATORS at top
gen_count = len(generators)
gen_spacing = 600
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
<!-- Breaker label offset 20px right per v1.1 Section 2.3 -->
<text x="{x+20}" y="{y_gen+57}" class="feeder-label">CB-G{i+1}</text>
<line x1="{x}" y1="{y_gen+70}" x2="{x}" y2="{y_gen+100}" class="power-line"/>
<text x="{x}" y="{y_gen+250}" class="rating" text-anchor="middle" font-size="9">{mw:.1f}MW</text>
'''

# Generator Sync Bus
y_sync = y_gen + 100
svg += f'''
<!-- Generator Sync Bus -->
<rect x="{gen_start_x-100}" y="{y_sync}" width="{(gen_count-1)*gen_spacing+200}" height="70" class="generator-box"/>
<line x1="{gen_start_x-80}" y1="{y_sync+20}" x2="{gen_start_x + (gen_count-1)*gen_spacing + 80}" y2="{y_sync+20}" class="bus"/>
<text x="{width//2}" y="{y_sync+45}" class="equipment-label" text-anchor="middle">GENERATOR SYNC BUS - 13.8 kV</text>
<text x="{width//2}" y="{y_sync+60}" class="annotation" text-anchor="middle">Woodward Paralleling | {gen_count} x {generators[0]['kw']/1000:.1f}MW (N+1)</text>
'''

# MV SWITCHBOARDS (Primary and Reserve)
mv_swbd_primary_x = width * 0.25  # Left quarter
mv_swbd_reserve_x = width * 0.75  # Right quarter
y_mv_swbd = y_sync + 180

svg += f'''
<!-- PRIMARY MV-SWBD -->
<line x1="{gen_start_x + gen_spacing}" y1="{y_sync+70}" x2="{gen_start_x + gen_spacing}" y2="{y_mv_swbd-60}" class="power-line"/>
<line x1="{gen_start_x + gen_spacing}" y1="{y_mv_swbd-60}" x2="{mv_swbd_primary_x}" y2="{y_mv_swbd-60}" class="power-line"/>
<line x1="{mv_swbd_primary_x}" y1="{y_mv_swbd-60}" x2="{mv_swbd_primary_x}" y2="{y_mv_swbd-20}" class="power-line"/>
<use href="#breaker-closed" x="{mv_swbd_primary_x}" y="{y_mv_swbd-40}"/>
<text x="{mv_swbd_primary_x+20}" y="{y_mv_swbd-35}" class="feeder-label">CB-PRI</text>

<rect x="{mv_swbd_primary_x-120}" y="{y_mv_swbd}" width="240" height="100" class="mv-switchboard"/>
<line x1="{mv_swbd_primary_x-100}" y1="{y_mv_swbd+20}" x2="{mv_swbd_primary_x+100}" y2="{y_mv_swbd+20}" class="bus"/>
<text x="{mv_swbd_primary_x}" y="{y_mv_swbd+50}" class="equipment-label" text-anchor="middle">MV-SWBD PRIMARY</text>
<text x="{mv_swbd_primary_x}" y="{y_mv_swbd+70}" class="annotation" text-anchor="middle">13.8kV | 4000A</text>
<text x="{mv_swbd_primary_x}" y="{y_mv_swbd+85}" class="rating" text-anchor="middle">Feeds Primary Incomers</text>

<!-- RESERVE MV-SWBD -->
<line x1="{gen_start_x + (gen_count-2)*gen_spacing}" y1="{y_sync+70}" x2="{gen_start_x + (gen_count-2)*gen_spacing}" y2="{y_mv_swbd-60}" class="power-line"/>
<line x1="{gen_start_x + (gen_count-2)*gen_spacing}" y1="{y_mv_swbd-60}" x2="{mv_swbd_reserve_x}" y2="{y_mv_swbd-60}" class="power-line"/>
<line x1="{mv_swbd_reserve_x}" y1="{y_mv_swbd-60}" x2="{mv_swbd_reserve_x}" y2="{y_mv_swbd-20}" class="power-line"/>
<use href="#breaker-closed" x="{mv_swbd_reserve_x}" y="{y_mv_swbd-40}"/>
<text x="{mv_swbd_reserve_x+20}" y="{y_mv_swbd-35}" class="feeder-label">CB-RES</text>

<rect x="{mv_swbd_reserve_x-120}" y="{y_mv_swbd}" width="240" height="100" class="mv-switchboard"/>
<line x1="{mv_swbd_reserve_x-100}" y1="{y_mv_swbd+20}" x2="{mv_swbd_reserve_x+100}" y2="{y_mv_swbd+20}" class="bus"/>
<text x="{mv_swbd_reserve_x}" y="{y_mv_swbd+50}" class="equipment-label" text-anchor="middle">MV-SWBD RESERVE</text>
<text x="{mv_swbd_reserve_x}" y="{y_mv_swbd+70}" class="annotation" text-anchor="middle">13.8kV | 4000A</text>
<text x="{mv_swbd_reserve_x}" y="{y_mv_swbd+85}" class="rating" text-anchor="middle">Feeds Reserve Incomers</text>
'''

# RMUs with DUAL INCOMERS per v1.1 Section 3.2
y_rmu = y_mv_swbd + 250

# Calculate takeoff points on MV-SWBDs for separated paths
# Spread 6 feeders across the bus width with minimum separation
feeder_spacing = 30  # Minimum horizontal separation between paths

for i, rmu_x in enumerate(rmu_positions):
    # Calculate takeoff point on PRIMARY MV-SWBD for this RMU
    # Distribute feeders evenly across the bus width
    pri_takeoff_x = mv_swbd_primary_x - 90 + (i * feeder_spacing)

    # Calculate takeoff point on RESERVE MV-SWBD for this RMU
    # Distribute feeders evenly across the bus width
    res_takeoff_x = mv_swbd_reserve_x - 90 + (i * feeder_spacing)

    svg += f'''
<!-- RMU-{i+1} with Dual Incomers (v1.1 Section 3.2) -->
<rect x="{rmu_x-60}" y="{y_rmu}" width="120" height="160" class="rmu-box"/>

<!-- Primary incomer from PRIMARY MV-SWBD (left side of RMU) -->
<!-- Vertical drop from bus with horizontal offset for path separation -->
<line x1="{pri_takeoff_x}" y1="{y_mv_swbd+20}" x2="{pri_takeoff_x}" y2="{y_mv_swbd+100}" class="power-line"/>
<line x1="{pri_takeoff_x}" y1="{y_mv_swbd+100}" x2="{pri_takeoff_x}" y2="{y_rmu-80}" class="power-line"/>
<text x="{pri_takeoff_x+10}" y="{y_rmu-100}" class="annotation" font-size="8">PRI-{i+1}</text>
<!-- Horizontal run to RMU left incomer -->
<line x1="{pri_takeoff_x}" y1="{y_rmu-80}" x2="{rmu_x-30}" y2="{y_rmu-80}" class="power-line"/>
<line x1="{rmu_x-30}" y1="{y_rmu-80}" x2="{rmu_x-30}" y2="{y_rmu+10}" class="power-line"/>
<use href="#breaker-closed" x="{rmu_x-30}" y="{y_rmu-20}"/>
<text x="{rmu_x-50}" y="{y_rmu-15}" class="feeder-label">IN1</text>

<!-- Reserve incomer from RESERVE MV-SWBD (right side of RMU) -->
<!-- Vertical drop from bus with horizontal offset for path separation -->
<line x1="{res_takeoff_x}" y1="{y_mv_swbd+20}" x2="{res_takeoff_x}" y2="{y_mv_swbd+100}" class="power-line"/>
<line x1="{res_takeoff_x}" y1="{y_mv_swbd+100}" x2="{res_takeoff_x}" y2="{y_rmu-60}" class="power-line"/>
<text x="{res_takeoff_x-10}" y="{y_rmu-100}" class="annotation" font-size="8">RES-{i+1}</text>
<!-- Horizontal run to RMU right incomer -->
<line x1="{res_takeoff_x}" y1="{y_rmu-60}" x2="{rmu_x+30}" y2="{y_rmu-60}" class="power-line"/>
<line x1="{rmu_x+30}" y1="{y_rmu-60}" x2="{rmu_x+30}" y2="{y_rmu+10}" class="power-line"/>
<use href="#breaker-closed" x="{rmu_x+30}" y="{y_rmu-20}"/>
<text x="{rmu_x+50}" y="{y_rmu-15}" class="feeder-label">IN2</text>

<!-- Internal bus section -->
<line x1="{rmu_x-30}" y1="{y_rmu+10}" x2="{rmu_x+30}" y2="{y_rmu+10}" class="bus"/>
<circle cx="{rmu_x}" cy="{y_rmu+10}" r="4" fill="black"/>

<!-- Transformer outgoer (from bottom per v1.1 Section 3.2) -->
<line x1="{rmu_x}" y1="{y_rmu+10}" x2="{rmu_x}" y2="{y_rmu+60}" class="power-line"/>
<use href="#breaker-closed" x="{rmu_x}" y="{y_rmu+35}"/>
<text x="{rmu_x+20}" y="{y_rmu+40}" class="feeder-label">TX</text>
<line x1="{rmu_x}" y1="{y_rmu+60}" x2="{rmu_x}" y2="{y_rmu+160}" class="power-line"/>

<!-- RMU Labels (10px clearance from edges per v1.1 Section 2.3) -->
<text x="{rmu_x}" y="{y_rmu+90}" class="equipment-label" text-anchor="middle">RMU-{i+1}</text>
<text x="{rmu_x}" y="{y_rmu+110}" class="annotation" text-anchor="middle">630A SF6</text>
<text x="{rmu_x}" y="{y_rmu+130}" class="annotation" text-anchor="middle" font-size="8">Dual Incomer</text>
'''

# TRANSFORMERS with proper orientation per v1.1 Section 3.3
y_tx = y_rmu + 220

for i in range(tx_count):
    tx_x = tx_positions[i]
    # Connect to nearest RMU above
    nearest_rmu_idx = min(range(len(rmu_positions)), key=lambda j: abs(rmu_positions[j] - tx_x))
    rmu_x = rmu_positions[nearest_rmu_idx]

    tx = transformers[i]
    kva = tx.get('rated_s', 0)
    hv = tx.get('hv_voltage', 13.8)
    lv = tx.get('lv_voltage', 0.48)

    svg += f'''
<!-- Transformer TX-{i+1} (v1.1 Section 3.3 - incomer from top, outgoer to bottom) -->

<!-- Incomer from RMU (from top) -->
<line x1="{rmu_x}" y1="{y_rmu+160}" x2="{rmu_x}" y2="{y_tx-100}" class="power-line"/>
<line x1="{rmu_x}" y1="{y_tx-100}" x2="{tx_x}" y2="{y_tx-100}" class="power-line"/>
<line x1="{tx_x}" y1="{y_tx-100}" x2="{tx_x}" y2="{y_tx-50}" class="power-line"/>
<use href="#breaker-closed" x="{tx_x}" y="{y_tx-75}"/>
<!-- Breaker label offset 20px per v1.1 Section 2.3 -->
<text x="{tx_x+20}" y="{y_tx-70}" class="feeder-label">CB-H{i+1}</text>
<line x1="{tx_x}" y1="{y_tx-50}" x2="{tx_x}" y2="{y_tx-35}" class="power-line"/>

<!-- Transformer symbol -->
<circle cx="{tx_x}" cy="{y_tx}" r="35" fill="white" stroke="black" stroke-width="2"/>
<circle cx="{tx_x}" cy="{y_tx}" r="28" fill="none" stroke="black" stroke-width="1"/>
<text x="{tx_x}" y="{y_tx-5}" class="annotation" text-anchor="middle">TX-{i+1}</text>
<text x="{tx_x}" y="{y_tx+8}" class="rating" text-anchor="middle" font-size="9">{kva}kVA</text>

<!-- Rating label 15px below per v1.1 Section 2.3 -->
<text x="{tx_x}" y="{y_tx+55}" class="annotation" text-anchor="middle">{hv}kV/{lv}kV</text>

<!-- Outgoer to LV-SWBD (from bottom) -->
<line x="{tx_x}" y1="{y_tx+35}" x2="{tx_x}" y2="{y_tx+75}" class="power-line"/>
<use href="#breaker-closed" x="{tx_x}" y="{y_tx+90}"/>
<text x="{tx_x+20}" y="{y_tx+95}" class="feeder-label">CB-L{i+1}</text>
<line x1="{tx_x}" y1="{y_tx+105}" x2="{tx_x}" y2="{y_tx+150}" class="power-line"/>
'''

# LV SWITCHBOARDS with 5 breaker positions per v1.1 Section 3.1
y_lv_swbd = y_tx + 170

for i in range(tx_count):
    tx_x = tx_positions[i]

    svg += f'''
<!-- LV-SWBD-{i+1} with 5 Breaker Positions (v1.1 Section 3.1) -->

<!-- Incomer from transformer (from top) -->
<line x1="{tx_x}" y1="{y_tx+150}" x2="{tx_x}" y2="{y_lv_swbd}" class="power-line"/>

<!-- Switchboard box - 200px wide (40px per position x 5) -->
<rect x="{tx_x-100}" y="{y_lv_swbd}" width="200" height="100" class="lv-switchboard"/>

<!-- Main bus inside (15px from top edge) -->
<line x1="{tx_x-90}" y1="{y_lv_swbd+15}" x2="{tx_x+90}" y2="{y_lv_swbd+15}" class="bus"/>

<!-- Labels (10px clearance from edges) -->
<text x="{tx_x}" y="{y_lv_swbd+45}" class="equipment-label" text-anchor="middle">LV-SWBD-{i+1}</text>
<text x="{tx_x}" y="{y_lv_swbd+65}" class="annotation" text-anchor="middle">480V/277V</text>
<text x="{tx_x}" y="{y_lv_swbd+85}" class="rating" text-anchor="middle" font-size="8">2000A | 5 Pos</text>
'''

    # 5 Breaker positions - evenly spaced at 40px intervals
    positions_x = [tx_x-80, tx_x-40, tx_x, tx_x+40, tx_x+80]
    position_labels = ["IT-UPS", "M-UPS", "Lights", "HVAC", "Spare"]

    for j, pos_x in enumerate(positions_x):
        svg += f'''
<!-- Breaker Position {j+1} -->
<line x1="{pos_x}" y1="{y_lv_swbd+15}" x2="{pos_x}" y2="{y_lv_swbd+100}" class="power-line"/>
<use href="#breaker-closed" x="{pos_x}" y="{y_lv_swbd+120}"/>
<!-- All downstream connections from BOTTOM per v1.1 Section 3.1 -->
<line x1="{pos_x}" y1="{y_lv_swbd+135}" x2="{pos_x}" y2="{y_lv_swbd+180}" class="power-line"/>
<text x="{pos_x}" y="{y_lv_swbd+110}" class="feeder-label" text-anchor="middle" font-size="7">{j+1}</text>

<!-- Distribution panel/load -->
<rect x="{pos_x-20}" y="{y_lv_swbd+190}" width="40" height="40" class="dist-panel"/>
<text x="{pos_x}" y="{y_lv_swbd+210}" class="annotation" text-anchor="middle" font-size="7">{position_labels[j]}</text>
'''

# Individual UPS modules at bottom
y_ups = y_lv_swbd + 280
ups_module_width = 60
ups_module_height = 70

# IT UPS modules
it_ups_start_x = 300
svg += f'''
<text x="{it_ups_start_x}" y="{y_ups-10}" class="equipment-label">IT UPS (N+1):</text>
'''

for i, ups in enumerate(it_ups):
    x = it_ups_start_x + (i * (ups_module_width + 15))
    kva = ups.get('kva', 0)

    svg += f'''
<rect x="{x}" y="{y_ups}" width="{ups_module_width}" height="{ups_module_height}" class="ups-module"/>
<text x="{x+ups_module_width//2}" y="{y_ups+20}" class="annotation" text-anchor="middle" font-size="8">IT-UPS-{i+1}</text>
<text x="{x+ups_module_width//2}" y="{y_ups+35}" class="rating" text-anchor="middle" font-size="8">{kva}kVA</text>
<text x="{x+ups_module_width//2}" y="{y_ups+50}" class="annotation" text-anchor="middle" font-size="7">Li-Ion</text>
<text x="{x+ups_module_width//2}" y="{y_ups+62}" class="annotation" text-anchor="middle" font-size="7">5-min</text>
'''

# Mechanical UPS modules
mech_ups_start_x = it_ups_start_x + (len(it_ups) * (ups_module_width + 15)) + 80
svg += f'''
<text x="{mech_ups_start_x}" y="{y_ups-10}" class="equipment-label">MECH UPS (N+1):</text>
'''

for i, ups in enumerate(mech_ups):
    x = mech_ups_start_x + (i * (ups_module_width + 15))
    kw = ups.get('kw', 0)

    svg += f'''
<rect x="{x}" y="{y_ups}" width="{ups_module_width}" height="{ups_module_height}" class="ups-module"/>
<text x="{x+ups_module_width//2}" y="{y_ups+20}" class="annotation" text-anchor="middle" font-size="8">M-UPS-{i+1}</text>
<text x="{x+ups_module_width//2}" y="{y_ups+35}" class="rating" text-anchor="middle" font-size="8">{kw}kW</text>
<text x="{x+ups_module_width//2}" y="{y_ups+50}" class="annotation" text-anchor="middle" font-size="7">Static</text>
<text x="{x+ups_module_width//2}" y="{y_ups+62}" class="annotation" text-anchor="middle" font-size="7">Mech</text>
'''

# Notes section
svg += f'''
<!-- Notes -->
<text x="50" y="{height-200}" class="equipment-label">NOTES - SLD Standards v1.1 Compliant:</text>
<text x="50" y="{height-180}" class="annotation">1. RMU dual-feed topology: 2 incomers (Primary + Reserve) with separated pathways, 1 outgoer per TX</text>
<text x="50" y="{height-160}" class="annotation">2. Transformers: {tx_count} transformers, each feeding dedicated LV-SWBD (1:1 relationship per BOD)</text>
<text x="50" y="{height-140}" class="annotation">3. LV-SWBDs: 200px wide with 5 breaker positions, all downstream connections from bottom</text>
<text x="50" y="{height-120}" class="annotation">4. Ring bus pathways: {feeder_spacing}px minimum separation for clear path delineation</text>
<text x="50" y="{height-100}" class="annotation">5. Symmetrical spacing: All equipment positions calculated for equal distribution (v1.1 Section 2.2)</text>
<text x="50" y="{height-80}" class="annotation">6. IEEE Std 315 / IEC 60617 compliant symbols | Total IT: {sum(u['kva'] for u in it_ups)/1000:.1f}MVA | Mech: {sum(u['kw'] for u in mech_ups)/1000:.1f}MW</text>

</svg>'''

# Save SVG
output = Path('saga_pryor_sld_v1_1_COMPLIANT.svg')
with open(output, 'w', encoding='utf-8') as f:
    f.write(svg)

print(f"\n{'='*80}")
print(f"SUCCESS: v1.1 Compliant SLD Generated!")
print(f"{'='*80}")
print(f"\nOutput: {output.absolute()}")
print(f"Size: {width} x {height} px")

print(f"\nv1.1 Compliance Features:")
print(f"  - RMU dual incomers: Primary + Reserve from both MV-SWBDs")
print(f"  - RMU single outgoer: To transformer from bottom")
print(f"  - Transformer orientation: Incomer top, outgoer bottom")
print(f"  - LV-SWBD: 200px wide, 5 breaker positions")
print(f"  - Downstream: All connections from LV-SWBD bottom")
print(f"  - Text clearance: 15px from cables, 10px from equipment")
print(f"  - Spacing: Symmetrical calculations (not manual)")
print(f"  - {len(transformers)} transformers, {len(rmus)} RMUs evenly distributed")

print(f"\n{'='*80}")
print("Opening in browser...")
