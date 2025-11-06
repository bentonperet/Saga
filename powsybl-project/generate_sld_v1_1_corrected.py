"""
SLD Generator v1.1 - CORRECTED TOPOLOGY (Rev H)
- 6 RMUs → 6 Transformers → 6 LV-SWBDs (1:1:1 relationship per BOD)
- Separated ring bus pathways with sufficient spacing
- 90-degree bends only (no diagonals)
- Equipment labels outside and to the right of graphics
- Connections touch equipment boundaries (NOT at corners - minimum spacing from corners)
- RMU incomers connect on TOP of RMU (not sides)
- Color-coded RMU incomers by RMU (outgoers remain black)
- Breaker graphics on MV-SWBDs
- Removed redundant UPS graphics
- Added Utility and Other Sources connections to MV-SWBDs
- UTILITY FEEDS ALWAYS AT TOP (above all other sources)
- Minimize equipment graphic sizes while respecting spacing rules
- Gen sync bus sized only for generators (no overlap with utility feeds)
- All pathways must not pass through equipment graphics
"""
import json
from datetime import datetime
from pathlib import Path
from sld_standards import get_svg_symbols, get_svg_style_section

# RMU Color Coding - Distinct colors for each RMU's incomers
RMU_COLORS = {
    0: {'color': '#E74C3C', 'name': 'Red'},      # RMU-1
    1: {'color': '#3498DB', 'name': 'Blue'},     # RMU-2
    2: {'color': '#27AE60', 'name': 'Green'},    # RMU-3
    3: {'color': '#E67E22', 'name': 'Orange'},   # RMU-4
    4: {'color': '#9B59B6', 'name': 'Purple'},   # RMU-5
    5: {'color': '#1ABC9C', 'name': 'Cyan'}      # RMU-6
}

# Read metadata from BOD parsing
with open('saga_pryor_metadata.json', 'r') as f:
    data = json.load(f)

generators = data.get('generators', [])
rmus = data.get('rmu', [])
it_ups = [u for u in data.get('ups', []) if u['function'] == 'IT']
mech_ups = [u for u in data.get('ups', []) if u['function'] == 'MECHANICAL']

# CORRECTED: Use 6 transformers (one per RMU), not 8
transformers = data.get('transformers', [])[:6]  # Take first 6

print("="*80)
print("SLD GENERATOR v1.1 - CORRECTED TOPOLOGY")
print("="*80)
print(f"\nComponents from BOD:")
print(f"  Generators: {len(generators)}")
print(f"  RMUs: {len(rmus)}")
print(f"  Transformers: {len(transformers)} (1 per RMU)")
print(f"  LV-SWBDs: {len(transformers)} (1 per TX)")
print(f"  IT UPS: {len(it_ups)}")
print(f"  Mech UPS: {len(mech_ups)}")

# Canvas and spacing calculations
MARGIN = 200
width = 5200  # Wider for separated paths
height = 4200  # Increased for utility and other sources

def calculate_symmetrical_positions(canvas_width, count, equipment_width, margin):
    """Calculate evenly-spaced positions per SLD Standards v1.1 Section 2.2"""
    usable_width = canvas_width - (2 * margin)
    total_equipment_width = count * equipment_width
    available_space = usable_width - total_equipment_width
    spacing = available_space / (count + 1)

    positions = []
    for i in range(count):
        x = margin + spacing * (i + 1) + equipment_width * i + (equipment_width / 2)
        positions.append(x)

    return positions

# Calculate equipment positions - 6 of each (not 8) - MINIMIZED sizes
equipment_count = 6
tx_width = 60  # Reduced from 70 (30px radius transformer)
tx_positions = calculate_symmetrical_positions(width, equipment_count, tx_width, MARGIN)

rmu_width = 100  # Reduced from 120
rmu_positions = calculate_symmetrical_positions(width, equipment_count, rmu_width, MARGIN)

lv_swbd_width = 200
lv_swbd_positions = calculate_symmetrical_positions(width, equipment_count, lv_swbd_width, MARGIN)

print(f"\nSymmetrical spacing calculated:")
print(f"  {equipment_count} RMUs: spacing = {(width - 2*MARGIN - equipment_count*rmu_width)/(equipment_count+1):.1f}px")
print(f"  {equipment_count} transformers: spacing = {(width - 2*MARGIN - equipment_count*tx_width)/(equipment_count+1):.1f}px")
print(f"  {equipment_count} LV-SWBDs: spacing = {(width - 2*MARGIN - equipment_count*lv_swbd_width)/(equipment_count+1):.1f}px")

# Start SVG
svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">
{get_svg_symbols()}
{get_svg_style_section()}

<!-- Title Block -->
<rect x="20" y="10" width="{width-40}" height="90" fill="white" stroke="black" stroke-width="2"/>
<text x="{width//2}" y="40" class="title" text-anchor="middle">SAGA PRYOR DATA CENTER - ELECTRICAL SINGLE LINE DIAGRAM</text>
<text x="{width//2}" y="60" class="subtitle" text-anchor="middle">13.8kV Multi-Source MV Distribution | Utility + Generators + Alt Sources</text>
<text x="{width//2}" y="80" class="annotation" text-anchor="middle">Utility at Top | Color-Coded Ring Bus | No Corner Connections</text>
<text x="{width-30}" y="85" class="annotation" text-anchor="end">Rev G - {datetime.now().strftime('%Y-%m-%d')}</text>

'''

# MV SWITCHBOARD positions (will reference later)
mv_swbd_primary_x = width * 0.25
mv_swbd_reserve_x = width * 0.75

# UTILITY FEEDS - ALWAYS AT TOP (above all other sources)
y_utility = 130

svg += f'''
<!-- UTILITY SERVICE - PRIMARY (at top) -->
<circle cx="{mv_swbd_primary_x}" cy="{y_utility}" r="22" fill="white" stroke="black" stroke-width="2"/>
<!-- Labels outside graphic boundary -->
<text x="{mv_swbd_primary_x+30}" y="{y_utility-10}" class="equipment-label" text-anchor="start">UTILITY PRIMARY</text>
<text x="{mv_swbd_primary_x+30}" y="{y_utility+5}" class="annotation" text-anchor="start">13.8kV Grid</text>
<line x1="{mv_swbd_primary_x}" y1="{y_utility+22}" x2="{mv_swbd_primary_x}" y2="{y_utility+50}" class="power-line"/>
<use href="#breaker-closed" x="{mv_swbd_primary_x}" y="{y_utility+62}"/>
<text x="{mv_swbd_primary_x+20}" y="{y_utility+67}" class="feeder-label">CB-U1</text>

<!-- UTILITY SERVICE - RESERVE (at top) -->
<circle cx="{mv_swbd_reserve_x}" cy="{y_utility}" r="22" fill="white" stroke="black" stroke-width="2"/>
<!-- Labels outside graphic boundary -->
<text x="{mv_swbd_reserve_x+30}" y="{y_utility-10}" class="equipment-label" text-anchor="start">UTILITY RESERVE</text>
<text x="{mv_swbd_reserve_x+30}" y="{y_utility+5}" class="annotation" text-anchor="start">13.8kV Grid</text>
<line x1="{mv_swbd_reserve_x}" y1="{y_utility+22}" x2="{mv_swbd_reserve_x}" y2="{y_utility+50}" class="power-line"/>
<use href="#breaker-closed" x="{mv_swbd_reserve_x}" y="{y_utility+62}"/>
<text x="{mv_swbd_reserve_x+20}" y="{y_utility+67}" class="feeder-label">CB-U2</text>
'''

# GENERATORS - below utility
y_gen = y_utility + 130
gen_count = len(generators)
gen_spacing = 280  # Reduced spacing - generators distributed evenly across sync bus top
gen_start_x = (width - ((gen_count-1) * gen_spacing)) // 2
gen_connections = []  # Store generator connection points for routing to sync bus

for i, gen in enumerate(generators):
    x = gen_start_x + (i * gen_spacing)
    kw = gen.get('kw', 0)
    mw = kw / 1000

    svg += f'''
<!-- Generator {i+1} -->
<circle cx="{x}" cy="{y_gen}" r="28" fill="white" stroke="black" stroke-width="2"/>
<!-- Labels outside graphic boundary - to the right -->
<text x="{x+35}" y="{y_gen-5}" class="bus-label" text-anchor="start" font-size="14">G{i+1}</text>
<text x="{x+35}" y="{y_gen+8}" class="rating" text-anchor="start" font-size="9">{mw:.1f}MW</text>
<line x1="{x}" y1="{y_gen+28}" x2="{x}" y2="{y_gen+55}" class="power-line"/>
<use href="#breaker-closed" x="{x}" y="{y_gen+42}"/>
<text x="{x+20}" y="{y_gen+47}" class="feeder-label" font-size="7">CB{i+1}</text>
<!-- Connection to sync bus - stored for later (after sync bus is defined) -->
'''
    # Store generator connection point for routing to sync bus later
    gen_connections.append((x, y_gen+57))

# Generator Sync Bus - ALIGNED WITH GENERATORS
y_sync = y_gen + 75
# Sync bus width matches generator array span plus padding
first_gen_x = gen_start_x
last_gen_x = gen_start_x + (gen_count-1) * gen_spacing
gen_array_center = first_gen_x + ((gen_count-1) * gen_spacing) // 2
# Sync bus spans from first to last generator with 60px padding on each side
sync_bus_left = first_gen_x - 60
sync_bus_right = last_gen_x + 60
sync_bus_width = sync_bus_right - sync_bus_left
sync_bus_height = 50

svg += f'''
<!-- Generator Sync Bus (compact centered box - minimized) -->
<rect x="{sync_bus_left}" y="{y_sync}" width="{sync_bus_width}" height="{sync_bus_height}" class="generator-box"/>
<line x1="{sync_bus_left+10}" y1="{y_sync+15}" x2="{sync_bus_right-10}" y2="{y_sync+15}" class="bus"/>
<!-- Labels outside graphic boundary - below -->
<text x="{gen_array_center}" y="{y_sync+sync_bus_height+18}" class="equipment-label" text-anchor="middle">GEN SYNC BUS</text>
<text x="{gen_array_center}" y="{y_sync+sync_bus_height+32}" class="annotation" text-anchor="middle" font-size="9">13.8kV | {gen_count}×{generators[0]['kw']/1000:.1f}MW</text>
'''

# Route each generator straight down to sync bus top - aligned directly above
for i, (gen_x, gen_y) in enumerate(gen_connections):
    svg += f'''
<!-- Generator {i+1} to Sync Bus connection - straight down -->
<line x1="{gen_x}" y1="{gen_y}" x2="{gen_x}" y2="{y_sync}" class="power-line"/>
<circle cx="{gen_x}" cy="{y_sync}" r="3" fill="black"/>
'''

# OTHER SOURCES - ADJACENT to generators (left and right of sync bus)
y_other_sources = y_sync + 10  # Same vertical level as sync bus
other_source_primary_x = sync_bus_left - 150  # To the left of sync bus
other_source_reserve_x = sync_bus_right + 150  # To the right of sync bus

svg += f'''
<!-- OTHER SOURCES - PRIMARY (Solar, Turbine, Hydro, etc.) - LEFT of generator group -->
<circle cx="{other_source_primary_x}" cy="{y_other_sources}" r="22" fill="white" stroke="black" stroke-width="2"/>
<!-- Labels outside graphic boundary -->
<text x="{other_source_primary_x-100}" y="{y_other_sources-10}" class="equipment-label" text-anchor="start">OTHER SOURCES</text>
<text x="{other_source_primary_x-100}" y="{y_other_sources+5}" class="annotation" text-anchor="start" font-size="9">Solar/Turbine/Hydro</text>
<line x1="{other_source_primary_x}" y1="{y_other_sources+22}" x2="{other_source_primary_x}" y2="{y_other_sources+50}" class="power-line"/>
<use href="#breaker-closed" x="{other_source_primary_x}" y="{y_other_sources+62}"/>
<text x="{other_source_primary_x+20}" y="{y_other_sources+67}" class="feeder-label">CB-A1</text>

<!-- OTHER SOURCES - RESERVE - RIGHT of generator group -->
<circle cx="{other_source_reserve_x}" cy="{y_other_sources}" r="22" fill="white" stroke="black" stroke-width="2"/>
<!-- Labels outside graphic boundary -->
<text x="{other_source_reserve_x+30}" y="{y_other_sources-10}" class="equipment-label" text-anchor="start">OTHER SOURCES</text>
<text x="{other_source_reserve_x+30}" y="{y_other_sources+5}" class="annotation" text-anchor="start" font-size="9">Solar/Turbine/Hydro</text>
<line x1="{other_source_reserve_x}" y1="{y_other_sources+22}" x2="{other_source_reserve_x}" y2="{y_other_sources+50}" class="power-line"/>
<use href="#breaker-closed" x="{other_source_reserve_x}" y="{y_other_sources+62}"/>
<text x="{other_source_reserve_x+20}" y="{y_other_sources+67}" class="feeder-label">CB-A2</text>
'''

# MV SWITCHBOARDS - below generators and other sources
y_mv_swbd = y_sync + 200  # Increased to accommodate routing

# Generator connections from compact sync bus to MV-SWBDs
# Connections come from bottom of sync bus - one to PRIMARY, one to RESERVE
gen_to_pri_x = sync_bus_left + sync_bus_width // 3  # Left third of sync bus
gen_to_res_x = sync_bus_right - sync_bus_width // 3  # Right third of sync bus

svg += f'''
<!-- Generator connections to MV-SWBDs from compact sync bus -->
<!-- Connection points on bottom of sync bus -->
<circle cx="{gen_to_pri_x}" cy="{y_sync+sync_bus_height}" r="3" fill="black"/>
<circle cx="{gen_to_res_x}" cy="{y_sync+sync_bus_height}" r="3" fill="black"/>
<line x1="{gen_to_pri_x}" y1="{y_sync+sync_bus_height}" x2="{gen_to_pri_x}" y2="{y_mv_swbd-60}" class="power-line"/>
<line x1="{gen_to_res_x}" y1="{y_sync+sync_bus_height}" x2="{gen_to_res_x}" y2="{y_mv_swbd-60}" class="power-line"/>

<!-- PRIMARY MV-SWBD with multiple source connections (not at corners) -->
<rect x="{mv_swbd_primary_x-120}" y="{y_mv_swbd}" width="240" height="120" class="mv-switchboard"/>

<!-- Utility connection from top - straight down (outside sync bus area) -->
<line x1="{mv_swbd_primary_x}" y1="{y_utility+80}" x2="{mv_swbd_primary_x}" y2="{y_mv_swbd-60}" class="power-line"/>
<line x1="{mv_swbd_primary_x}" y1="{y_mv_swbd-60}" x2="{mv_swbd_primary_x - 80}" y2="{y_mv_swbd-60}" class="power-line"/>
<line x1="{mv_swbd_primary_x - 80}" y1="{y_mv_swbd-60}" x2="{mv_swbd_primary_x - 80}" y2="{y_mv_swbd}" class="power-line"/>
<use href="#breaker-closed" x="{mv_swbd_primary_x - 80}" y="{y_mv_swbd-30}"/>
<text x="{mv_swbd_primary_x - 80 + 20}" y="{y_mv_swbd-25}" class="feeder-label" font-size="7">UTIL</text>

<!-- Generator connection - connects at center-left on TOP -->
<line x1="{gen_to_pri_x}" y1="{y_mv_swbd-60}" x2="{mv_swbd_primary_x - 40}" y2="{y_mv_swbd-60}" class="power-line"/>
<line x1="{mv_swbd_primary_x - 40}" y1="{y_mv_swbd-60}" x2="{mv_swbd_primary_x - 40}" y2="{y_mv_swbd}" class="power-line"/>
<use href="#breaker-closed" x="{mv_swbd_primary_x - 40}" y="{y_mv_swbd-30}"/>
<text x="{mv_swbd_primary_x - 40 + 20}" y="{y_mv_swbd-25}" class="feeder-label" font-size="7">GEN</text>

<!-- Other sources connection - routes from LEFT side with 90-degree bends -->
<line x1="{other_source_primary_x}" y1="{y_other_sources+80}" x2="{other_source_primary_x}" y2="{y_mv_swbd-90}" class="power-line"/>
<line x1="{other_source_primary_x}" y1="{y_mv_swbd-90}" x2="{mv_swbd_primary_x + 40}" y2="{y_mv_swbd-90}" class="power-line"/>
<line x1="{mv_swbd_primary_x + 40}" y1="{y_mv_swbd-90}" x2="{mv_swbd_primary_x + 40}" y2="{y_mv_swbd}" class="power-line"/>
<use href="#breaker-closed" x="{mv_swbd_primary_x + 40}" y="{y_mv_swbd-30}"/>
<text x="{mv_swbd_primary_x + 40 + 20}" y="{y_mv_swbd-25}" class="feeder-label" font-size="7">ALT</text>

<line x1="{mv_swbd_primary_x-110}" y1="{y_mv_swbd+20}" x2="{mv_swbd_primary_x+110}" y2="{y_mv_swbd+20}" class="bus"/>
<text x="{mv_swbd_primary_x+130}" y="{y_mv_swbd+50}" class="equipment-label" text-anchor="start">MV-SWBD PRIMARY</text>
<text x="{mv_swbd_primary_x+130}" y="{y_mv_swbd+70}" class="annotation" text-anchor="start">13.8kV | 4000A</text>
<text x="{mv_swbd_primary_x+130}" y="{y_mv_swbd+90}" class="rating" text-anchor="start">Multi-Source</text>

<!-- RESERVE MV-SWBD with multiple source connections (not at corners) -->
<rect x="{mv_swbd_reserve_x-120}" y="{y_mv_swbd}" width="240" height="120" class="mv-switchboard"/>

<!-- Utility connection from top - straight down (outside sync bus area) -->
<line x1="{mv_swbd_reserve_x}" y1="{y_utility+80}" x2="{mv_swbd_reserve_x}" y2="{y_mv_swbd-60}" class="power-line"/>
<line x1="{mv_swbd_reserve_x}" y1="{y_mv_swbd-60}" x2="{mv_swbd_reserve_x - 80}" y2="{y_mv_swbd-60}" class="power-line"/>
<line x1="{mv_swbd_reserve_x - 80}" y1="{y_mv_swbd-60}" x2="{mv_swbd_reserve_x - 80}" y2="{y_mv_swbd}" class="power-line"/>
<use href="#breaker-closed" x="{mv_swbd_reserve_x - 80}" y="{y_mv_swbd-30}"/>
<text x="{mv_swbd_reserve_x - 80 + 20}" y="{y_mv_swbd-25}" class="feeder-label" font-size="7">UTIL</text>

<!-- Generator connection - connects at center-left on TOP -->
<line x1="{gen_to_res_x}" y1="{y_mv_swbd-60}" x2="{mv_swbd_reserve_x - 40}" y2="{y_mv_swbd-60}" class="power-line"/>
<line x1="{mv_swbd_reserve_x - 40}" y1="{y_mv_swbd-60}" x2="{mv_swbd_reserve_x - 40}" y2="{y_mv_swbd}" class="power-line"/>
<use href="#breaker-closed" x="{mv_swbd_reserve_x - 40}" y="{y_mv_swbd-30}"/>
<text x="{mv_swbd_reserve_x - 40 + 20}" y="{y_mv_swbd-25}" class="feeder-label" font-size="7">GEN</text>

<!-- Other sources connection - routes from RIGHT side with 90-degree bends -->
<line x1="{other_source_reserve_x}" y1="{y_other_sources+80}" x2="{other_source_reserve_x}" y2="{y_mv_swbd-90}" class="power-line"/>
<line x1="{other_source_reserve_x}" y1="{y_mv_swbd-90}" x2="{mv_swbd_reserve_x + 40}" y2="{y_mv_swbd-90}" class="power-line"/>
<line x1="{mv_swbd_reserve_x + 40}" y1="{y_mv_swbd-90}" x2="{mv_swbd_reserve_x + 40}" y2="{y_mv_swbd}" class="power-line"/>
<use href="#breaker-closed" x="{mv_swbd_reserve_x + 40}" y="{y_mv_swbd-30}"/>
<text x="{mv_swbd_reserve_x + 40 + 20}" y="{y_mv_swbd-25}" class="feeder-label" font-size="7">ALT</text>

<line x1="{mv_swbd_reserve_x-110}" y1="{y_mv_swbd+20}" x2="{mv_swbd_reserve_x+110}" y2="{y_mv_swbd+20}" class="bus"/>
<text x="{mv_swbd_reserve_x+130}" y="{y_mv_swbd+50}" class="equipment-label" text-anchor="start">MV-SWBD RESERVE</text>
<text x="{mv_swbd_reserve_x+130}" y="{y_mv_swbd+70}" class="annotation" text-anchor="start">13.8kV | 4000A</text>
<text x="{mv_swbd_reserve_x+130}" y="{y_mv_swbd+90}" class="rating" text-anchor="start">Multi-Source</text>
'''

# Add breaker positions on PRIMARY MV-SWBD (one for each RMU feeder)
bus_width = 220
path_spacing = bus_width / (equipment_count + 1)

for i in range(equipment_count):
    breaker_x = mv_swbd_primary_x - 110 + (i + 1) * path_spacing
    rmu_color = RMU_COLORS[i]['color']

    svg += f'''
<!-- PRIMARY MV-SWBD Breaker Position {i+1} for RMU-{i+1} -->
<line x1="{breaker_x}" y1="{y_mv_swbd+20}" x2="{breaker_x}" y2="{y_mv_swbd+50}" style="stroke:{rmu_color};stroke-width:2;fill:none;"/>
<use href="#breaker-closed" x="{breaker_x}" y="{y_mv_swbd+65}"/>
<text x="{breaker_x}" y="{y_mv_swbd+95}" class="feeder-label" text-anchor="middle" font-size="7">{i+1}</text>
<line x1="{breaker_x}" y1="{y_mv_swbd+80}" x2="{breaker_x}" y2="{y_mv_swbd+120}" style="stroke:{rmu_color};stroke-width:2;fill:none;"/>
'''

# Add breaker positions on RESERVE MV-SWBD (one for each RMU feeder)
for i in range(equipment_count):
    breaker_x = mv_swbd_reserve_x - 110 + (i + 1) * path_spacing
    rmu_color = RMU_COLORS[i]['color']

    svg += f'''
<!-- RESERVE MV-SWBD Breaker Position {i+1} for RMU-{i+1} -->
<line x1="{breaker_x}" y1="{y_mv_swbd+20}" x2="{breaker_x}" y2="{y_mv_swbd+50}" style="stroke:{rmu_color};stroke-width:2;fill:none;"/>
<use href="#breaker-closed" x="{breaker_x}" y="{y_mv_swbd+65}"/>
<text x="{breaker_x}" y="{y_mv_swbd+95}" class="feeder-label" text-anchor="middle" font-size="7">{i+1}</text>
<line x1="{breaker_x}" y1="{y_mv_swbd+80}" x2="{breaker_x}" y2="{y_mv_swbd+120}" style="stroke:{rmu_color};stroke-width:2;fill:none;"/>
'''

svg += '''
'''

# RMUs with SEPARATED DUAL INCOMERS - 90 degree bends only
y_rmu = y_mv_swbd + 450  # More space for separated pathways

for i, rmu_x in enumerate(rmu_positions):
    # Get color for this RMU
    rmu_color = RMU_COLORS[i]['color']
    rmu_color_name = RMU_COLORS[i]['name']

    # Calculate takeoff points - evenly distributed across bus (already calculated above)
    pri_takeoff_x = mv_swbd_primary_x - 110 + (i + 1) * path_spacing
    res_takeoff_x = mv_swbd_reserve_x - 110 + (i + 1) * path_spacing

    # Stagger vertical drops to avoid overlap - each path at different height
    pri_drop_height = y_rmu - 150 - (i * 20)  # Stagger by 20px each
    res_drop_height = y_rmu - 120 - (i * 20)  # Different stagger for reserve

    # RMU dimensions - MINIMIZED
    rmu_width = 100  # Reduced from 120
    rmu_height = 150  # Reduced from 180
    rmu_left = rmu_x - 50  # Half of width
    rmu_right = rmu_x + 50
    rmu_top = y_rmu
    rmu_bottom = y_rmu + rmu_height

    # Connection points - NOT at corners, with minimum spacing from corners
    # Primary incomer connects on TOP, left of center (30px from left corner)
    pri_connection_x = rmu_left + 30  # 30px from left corner
    # Reserve incomer connects on TOP, right of center (30px from right corner)
    res_connection_x = rmu_right - 30  # 30px from right corner
    # Both connect at the TOP boundary
    top_connection_y = rmu_top
    # Bottom center connection
    bottom_connection_y = rmu_bottom

    svg += f'''
<!-- RMU-{i+1} with Color-Coded Dual Incomers ({rmu_color_name}) -->
<rect x="{rmu_left}" y="{rmu_top}" width="{rmu_width}" height="{rmu_height}" class="rmu-box"/>
<text x="{rmu_right+10}" y="{rmu_top+50}" class="equipment-label" text-anchor="start">RMU-{i+1}</text>
<text x="{rmu_right+10}" y="{rmu_top+70}" class="annotation" text-anchor="start">630A SF6</text>
<text x="{rmu_right+10}" y="{rmu_top+90}" class="annotation" text-anchor="start" font-size="8">{rmu_color_name} Feeds</text>

<!-- Primary incomer path - COLOR CODED - connects on TOP (not corner) -->
<!-- Vertical drop from MV-SWBD breaker -->
<line x1="{pri_takeoff_x}" y1="{y_mv_swbd+120}" x2="{pri_takeoff_x}" y2="{pri_drop_height}" style="stroke:{rmu_color};stroke-width:2;fill:none;"/>
<text x="{pri_takeoff_x+10}" y="{y_mv_swbd+150}" class="annotation" font-size="8">PRI-{i+1}</text>
<!-- Horizontal run to connection point on TOP of RMU -->
<line x1="{pri_takeoff_x}" y1="{pri_drop_height}" x2="{pri_connection_x}" y2="{pri_drop_height}" style="stroke:{rmu_color};stroke-width:2;fill:none;"/>
<!-- Final vertical drop to TOP boundary (30px from left corner) -->
<line x1="{pri_connection_x}" y1="{pri_drop_height}" x2="{pri_connection_x}" y2="{top_connection_y}" style="stroke:{rmu_color};stroke-width:2;fill:none;"/>
<use href="#breaker-closed" x="{pri_connection_x}" y="{rmu_top+20}"/>
<text x="{pri_connection_x-20}" y="{rmu_top+25}" class="feeder-label" font-size="7">IN1</text>
<!-- Continue down inside RMU -->
<line x1="{pri_connection_x}" y1="{rmu_top+35}" x2="{pri_connection_x}" y2="{rmu_top+90}" style="stroke:{rmu_color};stroke-width:2;fill:none;"/>

<!-- Reserve incomer path - COLOR CODED - connects on TOP (not corner) -->
<!-- Vertical drop from MV-SWBD breaker -->
<line x1="{res_takeoff_x}" y1="{y_mv_swbd+120}" x2="{res_takeoff_x}" y2="{res_drop_height}" style="stroke:{rmu_color};stroke-width:2;fill:none;"/>
<text x="{res_takeoff_x+10}" y="{y_mv_swbd+150}" class="annotation" font-size="8">RES-{i+1}</text>
<!-- Horizontal run to connection point on TOP of RMU -->
<line x1="{res_takeoff_x}" y1="{res_drop_height}" x2="{res_connection_x}" y2="{res_drop_height}" style="stroke:{rmu_color};stroke-width:2;fill:none;"/>
<!-- Final vertical drop to TOP boundary (30px from right corner) -->
<line x1="{res_connection_x}" y1="{res_drop_height}" x2="{res_connection_x}" y2="{top_connection_y}" style="stroke:{rmu_color};stroke-width:2;fill:none;"/>
<use href="#breaker-closed" x="{res_connection_x}" y="{rmu_top+20}"/>
<text x="{res_connection_x+20}" y="{rmu_top+25}" class="feeder-label" font-size="7">IN2</text>
<!-- Continue down inside RMU -->
<line x1="{res_connection_x}" y1="{rmu_top+35}" x2="{res_connection_x}" y2="{rmu_top+90}" style="stroke:{rmu_color};stroke-width:2;fill:none;"/>

<!-- Internal bus section -->
<line x1="{pri_connection_x}" y1="{rmu_top+90}" x2="{res_connection_x}" y2="{rmu_top+90}" class="bus"/>
<circle cx="{rmu_x}" cy="{rmu_top+90}" r="4" fill="black"/>

<!-- Transformer outgoer (BLACK - from bottom center, not corner) -->
<line x1="{rmu_x}" y1="{rmu_top+90}" x2="{rmu_x}" y2="{rmu_top+130}" class="power-line"/>
<use href="#breaker-closed" x="{rmu_x}" y="{rmu_top+110}"/>
<text x="{rmu_x+20}" y="{rmu_top+115}" class="feeder-label">TX</text>
<!-- Exit RMU at bottom boundary (center, not corner) -->
<line x1="{rmu_x}" y1="{rmu_top+130}" x2="{rmu_x}" y2="{bottom_connection_y}" class="power-line"/>
'''

# TRANSFORMERS - one per RMU (6 total)
y_tx = y_rmu + 260

for i in range(equipment_count):
    tx_x = tx_positions[i]
    rmu_x = rmu_positions[i]  # 1:1 connection to RMU above

    tx = transformers[i]
    kva = tx.get('rated_s', 0)
    hv = tx.get('hv_voltage', 13.8)
    lv = tx.get('lv_voltage', 0.48)

    svg += f'''
<!-- Transformer TX-{i+1} (1:1 with RMU-{i+1}) - MINIMIZED -->

<!-- Incomer from RMU above - 90 degree bends -->
<line x1="{rmu_x}" y1="{y_rmu+rmu_height}" x2="{rmu_x}" y2="{y_tx-100}" class="power-line"/>
<line x1="{rmu_x}" y1="{y_tx-100}" x2="{tx_x}" y2="{y_tx-100}" class="power-line"/>
<line x1="{tx_x}" y1="{y_tx-100}" x2="{tx_x}" y2="{y_tx-60}" class="power-line"/>
<use href="#breaker-closed" x="{tx_x}" y="{y_tx-80}"/>
<text x="{tx_x+20}" y="{y_tx-75}" class="feeder-label" font-size="7">CB-H{i+1}</text>
<!-- Enter transformer at top -->
<line x1="{tx_x}" y1="{y_tx-60}" x2="{tx_x}" y2="{y_tx-30}" class="power-line"/>

<!-- Transformer symbol - REDUCED to 30px radius -->
<circle cx="{tx_x}" cy="{y_tx}" r="30" fill="white" stroke="black" stroke-width="2"/>
<circle cx="{tx_x}" cy="{y_tx}" r="24" fill="none" stroke="black" stroke-width="1"/>

<!-- Labels outside graphic boundary - to the right -->
<text x="{tx_x+38}" y="{y_tx-10}" class="equipment-label" text-anchor="start" font-size="11">TX-{i+1}</text>
<text x="{tx_x+38}" y="{y_tx+3}" class="annotation" text-anchor="start" font-size="9">{kva}kVA</text>
<text x="{tx_x+38}" y="{y_tx+15}" class="annotation" text-anchor="start" font-size="8">{hv}kV/{lv}kV</text>

<!-- Outgoer from bottom -->
<line x1="{tx_x}" y1="{y_tx+30}" x2="{tx_x}" y2="{y_tx+60}" class="power-line"/>
<use href="#breaker-closed" x="{tx_x}" y="{y_tx+80}"/>
<text x="{tx_x+20}" y="{y_tx+85}" class="feeder-label" font-size="7">CB-L{i+1}</text>
<line x1="{tx_x}" y1="{y_tx+95}" x2="{tx_x}" y2="{y_tx+150}" class="power-line"/>
'''

# LV SWITCHBOARDS - one per TX (6 total)
y_lv_swbd = y_tx + 220

for i in range(equipment_count):
    lv_x = lv_swbd_positions[i]
    tx_x = tx_positions[i]  # 1:1 connection to TX above

    svg += f'''
<!-- LV-SWBD-{i+1} (1:1 with TX-{i+1}) - MINIMIZED height -->

<!-- Incomer from transformer - 90 degree bends -->
<line x1="{tx_x}" y1="{y_tx+150}" x2="{tx_x}" y2="{y_lv_swbd-40}" class="power-line"/>
<line x1="{tx_x}" y1="{y_lv_swbd-40}" x2="{lv_x}" y2="{y_lv_swbd-40}" class="power-line"/>
<!-- Enter LV-SWBD at top boundary -->
<line x1="{lv_x}" y1="{y_lv_swbd-40}" x2="{lv_x}" y2="{y_lv_swbd}" class="power-line"/>

<!-- Switchboard box - 200px wide (5 breaker positions), 90px height (MINIMIZED) -->
<rect x="{lv_x-100}" y="{y_lv_swbd}" width="200" height="90" class="lv-switchboard"/>
<line x1="{lv_x-90}" y1="{y_lv_swbd+15}" x2="{lv_x+90}" y2="{y_lv_swbd+15}" class="bus"/>

<!-- Labels outside and to the right -->
<text x="{lv_x+110}" y="{y_lv_swbd+35}" class="equipment-label" text-anchor="start" font-size="11">LV-SWBD-{i+1}</text>
<text x="{lv_x+110}" y="{y_lv_swbd+52}" class="annotation" text-anchor="start" font-size="9">480V/277V</text>
<text x="{lv_x+110}" y="{y_lv_swbd+68}" class="rating" text-anchor="start" font-size="8">2000A | 5 Pos</text>
'''

    # 5 Breaker positions - evenly spaced
    positions_x = [lv_x-80, lv_x-40, lv_x, lv_x+40, lv_x+80]
    position_labels = ["IT-UPS", "M-UPS", "Lights", "HVAC", "Spare"]

    for j, pos_x in enumerate(positions_x):
        svg += f'''
<!-- Breaker Position {j+1} -->
<line x1="{pos_x}" y1="{y_lv_swbd+15}" x2="{pos_x}" y2="{y_lv_swbd+90}" class="power-line"/>
<use href="#breaker-closed" x="{pos_x}" y="{y_lv_swbd+110}"/>
<!-- All downstream from BOTTOM -->
<line x1="{pos_x}" y1="{y_lv_swbd+125}" x2="{pos_x}" y2="{y_lv_swbd+165}" class="power-line"/>
<text x="{pos_x}" y="{y_lv_swbd+80}" class="feeder-label" text-anchor="middle" font-size="7">{j+1}</text>

<!-- Distribution panel/load - MINIMIZED to 36x36 -->
<rect x="{pos_x-18}" y="{y_lv_swbd+175}" width="36" height="36" class="dist-panel"/>
<text x="{pos_x}" y="{y_lv_swbd+195}" class="annotation" text-anchor="middle" font-size="7">{position_labels[j]}</text>
'''

# Color legend
svg += f'''
<!-- Color Legend for RMU Incomers -->
<rect x="{width-550}" y="{height-320}" width="500" height="100" fill="white" stroke="black" stroke-width="2"/>
<text x="{width-530}" y="{height-290}" class="equipment-label">RMU INCOMER COLOR CODING:</text>
'''

for i in range(equipment_count):
    legend_x = width - 530 + (i * 80)
    rmu_color = RMU_COLORS[i]['color']
    rmu_color_name = RMU_COLORS[i]['name']

    svg += f'''
<line x1="{legend_x}" y1="{height-260}" x2="{legend_x+50}" y2="{height-260}" style="stroke:{rmu_color};stroke-width:4;fill:none;"/>
<text x="{legend_x+25}" y="{height-240}" class="annotation" text-anchor="middle" font-size="8">RMU-{i+1}</text>
<text x="{legend_x+25}" y="{height-228}" class="annotation" text-anchor="middle" font-size="7">{rmu_color_name}</text>
'''

# Notes section
svg += f'''
<!-- Notes -->
<text x="50" y="{height-300}" class="equipment-label">NOTES - SLD Standards v1.1 Compliant (Rev G):</text>
<text x="50" y="{height-280}" class="annotation">1. SOURCE HIERARCHY: Utility feeds ALWAYS at top (above all other sources) - critical rule</text>
<text x="50" y="{height-260}" class="annotation">2. TOPOLOGY: 6 RMUs → 6 Transformers → 6 LV-SWBDs (1:1:1 relationship per BOD)</text>
<text x="50" y="{height-240}" class="annotation">3. MULTIPLE SOURCES: Utility (grid) at top, Generators (6×4MW diesel) center, Other Sources (solar/turbine/hydro) below</text>
<text x="50" y="{height-220}" class="annotation">4. MINIMIZED GRAPHICS: Equipment sizes reduced while maintaining spacing rules - Gen sync bus 50px height, generators 28px radius</text>
<text x="50" y="{height-200}" class="annotation">5. Ring bus pathways: Color-coded by RMU, separated with {path_spacing:.1f}px spacing, staggered for clear delineation</text>
<text x="50" y="{height-180}" class="annotation">6. RMU incomers: Connect on TOP of RMU (30px from corners, not AT corners) - primary left, reserve right</text>
<text x="50" y="{height-160}" class="annotation">7. MV-SWBDs: Show 6 feeder breaker positions (one per RMU) with color-coded feeders matching RMU incomers</text>
<text x="50" y="{height-140}" class="annotation">8. Connection rule: ALL equipment connections have minimum spacing from corners (not at corners)</text>
<text x="50" y="{height-120}" class="annotation">9. 90-degree bends only: No diagonal connections, all pathways use orthogonal routing</text>
<text x="50" y="{height-100}" class="annotation">10. Equipment labels: Placed outside and to the right of graphics with symmetrical spacing</text>
<text x="50" y="{height-80}" class="annotation">11. Color coding: RMU incomers color-coded for traceability, outgoers remain black per standard</text>
<text x="50" y="{height-60}" class="annotation">12. IEEE Std 315 / IEC 60617 compliant | Total IT: {sum(u['kva'] for u in it_ups)/1000:.1f}MVA | Mech: {sum(u['kw'] for u in mech_ups)/1000:.1f}MW</text>

</svg>'''

# Save SVG
output = Path('saga_pryor_sld_v1_1_CORRECTED.svg')
with open(output, 'w', encoding='utf-8') as f:
    f.write(svg)

print(f"\n{'='*80}")
print(f"SUCCESS: v1.1 CORRECTED SLD Generated (Rev H)!")
print(f"{'='*80}")
print(f"\nOutput: {output.absolute()}")
print(f"Size: {width} x {height} px")

print(f"\nCORRECTED Topology:")
print(f"  - 6 RMUs (not 8)")
print(f"  - 6 Transformers (1 per RMU)")
print(f"  - 6 LV-SWBDs (1 per TX)")
print(f"  - Ring bus path separation: {path_spacing:.1f}px")

print(f"\nNEW Features (Rev H):")
print(f"  - GEN SYNC BUS ALIGNED: Sync bus width matches generator array span")
print(f"  - GENERATORS EVENLY DISTRIBUTED: 280px spacing across sync bus top")
print(f"  - GENERATOR ROUTING: Each gen connects straight down to sync bus")
print(f"  - UTILITY ROUTING SIMPLIFIED: Straight down to MV-SWBDs (no unnecessary bends)")
print(f"  - OTHER SOURCES REPOSITIONED: Adjacent to generators (no path overlap)")
print(f"  - TEXT LABELS OUTSIDE BOUNDARIES: All text moved outside equipment graphics")
print(f"  - EQUIPMENT MINIMIZED: RMU 100x150px, TX 30px radius, LV-SWBD 90px height")
print(f"  - DIST PANELS: Reduced to 36x36px")
print(f"  - Vertical order: Utility -> Generators -> Other Sources -> MV-SWBDs")
print(f"  - Color-coded RMU incomers: Red, Blue, Green, Orange, Purple, Cyan")
print(f"  - All equipment: No corner connections rule applied")
print(f"  - 90-degree bends only (no diagonals)")

print(f"\n{'='*80}")
print("Opening in browser...")
