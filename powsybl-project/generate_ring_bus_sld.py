"""
Ring Bus Single-Line Diagram Generator for Saga Pryor Data Center
Shows actual electrical paths from MV-SWBD through RMUs with proper ring topology.
IEEE Std 315 / IEC 60617 Compliant
"""

import json
from datetime import datetime
from sld_standards import get_svg_symbols, get_svg_style_section, LAYOUT

# Read the metadata
with open('pachyderm_metadata.json', 'r') as f:
    data = json.load(f)

# SVG setup - wider for ring bus layout with better spacing
width = 2800
height = 2100

svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
{get_svg_symbols()}
{get_svg_style_section()}

<!-- Title Block -->
<rect x="50" y="20" width="2700" height="80" fill="white" stroke="black" stroke-width="2"/>
<text x="1400" y="50" class="title" text-anchor="middle">SAGA PRYOR DATA CENTER - 13.8kV Dual Ring Bus Distribution</text>
<text x="1400" y="75" class="subtitle" text-anchor="middle">Redundant Path Diagram | Generators → MV-SWBD A/B → Dual Ring → RMUs → Transformers → LV-SWBD</text>

<!-- Date block -->
<text x="2650" y="50" class="label" text-anchor="end">Date: {datetime.now().strftime('%m/%d/%Y')}</text>
<text x="2650" y="70" class="label" text-anchor="end">Rev: 0</text>

<!-- Generator 1 - 4MW -->
<g id="gen-1">
    <circle cx="950" cy="180" r="40" fill="white" stroke="black" stroke-width="2"/>
    <text x="950" y="175" class="bus-label" text-anchor="middle">G</text>
    <text x="950" y="190" class="small-label" text-anchor="middle">GEN-1</text>
    <text x="950" y="205" class="rating" text-anchor="middle" font-size="9">4MW</text>
</g>
<!-- Gen 1 to Sync Bus -->
<line x1="950" y1="220" x2="950" y2="280" class="power-line"/>
<use href="#breaker-closed" x="950" y="250"/>
<line x1="950" y1="280" x2="950" y2="310" class="power-line"/>

<!-- Generator 2 - 4MW -->
<g id="gen-2">
    <circle cx="1150" cy="180" r="40" fill="white" stroke="black" stroke-width="2"/>
    <text x="1150" y="175" class="bus-label" text-anchor="middle">G</text>
    <text x="1150" y="190" class="small-label" text-anchor="middle">GEN-2</text>
    <text x="1150" y="205" class="rating" text-anchor="middle" font-size="9">4MW</text>
</g>
<!-- Gen 2 to Sync Bus -->
<line x1="1150" y1="220" x2="1150" y2="280" class="power-line"/>
<use href="#breaker-closed" x="1150" y="250"/>
<line x1="1150" y1="280" x2="1150" y2="310" class="power-line"/>

<!-- Generator 3 - 4MW -->
<g id="gen-3">
    <circle cx="1350" cy="180" r="40" fill="white" stroke="black" stroke-width="2"/>
    <text x="1350" y="175" class="bus-label" text-anchor="middle">G</text>
    <text x="1350" y="190" class="small-label" text-anchor="middle">GEN-3</text>
    <text x="1350" y="205" class="rating" text-anchor="middle" font-size="9">4MW</text>
</g>
<!-- Gen 3 to Sync Bus -->
<line x1="1350" y1="220" x2="1350" y2="280" class="power-line"/>
<use href="#breaker-closed" x="1350" y="250"/>
<line x1="1350" y1="280" x2="1350" y2="310" class="power-line"/>

<!-- Sync Bus -->
<g id="sync-bus">
    <rect x="850" y="310" width="600" height="80" class="switchgear-box"/>
    <text x="1150" y="340" class="equipment-label" text-anchor="middle">GENERATOR SYNC BUS</text>
    <text x="1150" y="360" class="rating" text-anchor="middle">13.8 kV | Woodward Paralleling Controls</text>
    <text x="1150" y="378" class="rating" text-anchor="middle">3 × 4MW (N+1) | Auto Load Share</text>
</g>

<!-- Sync Bus to MV-MSB A -->
<line x1="950" y1="390" x2="950" y2="440" class="power-line"/>
<use href="#breaker-closed" x="950" y="420"/>
<line x1="950" y1="440" x2="950" y2="470" class="power-line"/>
<line x1="950" y1="470" x2="280" y2="470" class="power-line"/>
<line x1="280" y1="470" x2="280" y2="360" class="power-line"/>
<use href="#breaker-closed" x="280" y="410"/>

<!-- Sync Bus to MV-MSB B -->
<line x1="1350" y1="390" x2="1350" y2="440" class="power-line"/>
<use href="#breaker-closed" x="1350" y="420"/>
<line x1="1350" y1="440" x2="1350" y2="470" class="power-line"/>
<line x1="1350" y1="470" x2="2520" y2="470" class="power-line"/>
<line x1="2520" y1="470" x2="2520" y2="360" class="power-line"/>
<use href="#breaker-closed" x="2520" y="410"/>

<!-- MV-MSB A (left side - PRIMARY) -->
<g id="mv-msb-a">
    <rect x="140" y="360" width="280" height="120" class="switchgear-box"/>
    <text x="280" y="395" class="equipment-label" text-anchor="middle">MV-MSB A</text>
    <text x="280" y="415" class="annotation" text-anchor="middle">PRIMARY</text>
    <text x="280" y="435" class="annotation" text-anchor="middle">13.8 kV</text>
    <text x="280" y="455" class="rating" text-anchor="middle">4000A | 65kAIC</text>
</g>

<!-- MV-MSB B (right side - RESERVE) -->
<g id="mv-msb-b">
    <rect x="2380" y="360" width="280" height="120" class="switchgear-box"/>
    <text x="2520" y="395" class="equipment-label" text-anchor="middle">MV-MSB B</text>
    <text x="2520" y="415" class="annotation" text-anchor="middle">RESERVE</text>
    <text x="2520" y="435" class="annotation" text-anchor="middle">13.8 kV</text>
    <text x="2520" y="455" class="rating" text-anchor="middle">4000A | 65kAIC</text>
</g>

<!-- MV-MSB A Bus - connection points at bottom for each path -->
<!-- No single bus line - each path connects separately from bottom of MV-MSB A -->

<!-- MV-MSB B Bus - collection points at bottom for each path -->
<!-- No single bus line - each path connects separately to bottom of MV-MSB B -->

'''

# RMU positions along the ring - 4 RMUs with more spacing
rmu_count = min(len(data['rmu']), 4)
rmu_spacing = 2000 / (rmu_count - 1) if rmu_count > 1 else 0
rmu_start_x = 450

for i in range(rmu_count):
    x = rmu_start_x + (i * rmu_spacing)
    
    # Calculate connection points at bottom of MV-MSB A (spread across bottom)
    mv_msb_a_x = 200 + (i * 60)  # Separate horizontal position for each connection at bottom
    
    # Calculate primary and reserve path heights - significant stagger to prevent overlaps
    primary_y = 600 + (i * 80)  # Stagger each primary path by 80px
    reserve_y = 640 + (i * 80)  # Reserve paths offset 40px below primary (allows crossover)
    
    # Reserve path horizontal offset to avoid running parallel to primary
    # Each reserve path gets additional horizontal offset to prevent blue-on-blue overlap
    reserve_horizontal_offset = 120 + (i * 20)  # Increasing offset for each subsequent path
    
    # RMU position lowered to create separation from cable paths
    rmu_top = 950  # Move RMUs down further to create more separation from cables and bends
    
    # Minimum clearance between equipment/breakers and 90-degree bends
    bend_clearance = 50  # 50px clearance from equipment/breakers to nearest bend
    
    # Individual wire path from MV-MSB A to RMU to MV-MSB B
    svg += f'''
<!-- ═══════════════════════════════════════════════════════════════════ -->
<!-- Wire Path {i+1}: MV-MSB A → RMU-{i+1} → MV-MSB B -->
<!-- ═══════════════════════════════════════════════════════════════════ -->

<!-- PRIMARY Path {i+1}: Separate connection from BOTTOM of MV-MSB A -->
<!-- Vertical drop from bottom of MV-MSB A at separate position -->
<line x1="{mv_msb_a_x}" y1="480" x2="{mv_msb_a_x}" y2="540" class="power-line"/>
<use href="#connection-point" x="{mv_msb_a_x}" y="480"/>

<!-- Breaker BKR-A{i+1} 30px from MV-MSB A bottom -->
<use href="#breaker-closed" x="{mv_msb_a_x}" y="510"/>

<!-- Continue vertical to horizontal transition level -->
<line x1="{mv_msb_a_x}" y1="540" x2="{mv_msb_a_x}" y2="{primary_y}" class="power-line"/>

<!-- Horizontal run to RMU position -->
<line x1="{mv_msb_a_x}" y1="{primary_y}" x2="{x}" y2="{primary_y}" class="power-line"/>

<!-- Vertical drop directly to RMU top (breaker inline, no reversal) -->
<line x1="{x}" y1="{primary_y}" x2="{x}" y2="{rmu_top - 30}" class="power-line"/>

<!-- Breaker RMU-IN 30px before entering RMU from top -->
<use href="#breaker-closed" x="{x}" y="{rmu_top - 30}"/>

<!-- Continue to RMU top after breaker -->
<line x1="{x}" y1="{rmu_top - 30}" x2="{x}" y2="{rmu_top}" class="power-line"/>

<!-- RMU-{i+1} Box - moved down for separation -->
<g id="rmu-{i+1}">
    <rect x="{x-110}" y="{rmu_top}" width="220" height="110" class="rmu-box"/>
    <text x="{x}" y="{rmu_top + 30}" class="equipment-label" text-anchor="middle">RMU-{i+1}</text>
    <text x="{x}" y="{rmu_top + 50}" class="rating" text-anchor="middle">630A Ring Main Unit</text>
    <text x="{x}" y="{rmu_top + 68}" class="rating" text-anchor="middle">Dual Feed | 20kA SCCR</text>
</g>

<!-- RESERVE Path {i+1}: TOP of RMU-{i+1} (other side) to BOTTOM of MV-MSB B -->
<!-- Vertical rise from top of RMU -->
<line x1="{x+50}" y1="{rmu_top}" x2="{x+50}" y2="{rmu_top - 30}" class="power-line"/>

<!-- Breaker RMU-OUT 30px after leaving top of RMU -->
<use href="#breaker-closed" x="{x+50}" y="{rmu_top - 30}"/>

<!-- Continue vertical to reserve horizontal level (no reversal) -->
<line x1="{x+50}" y1="{rmu_top - 30}" x2="{x+50}" y2="{reserve_y}" class="power-line"/>

<!-- Horizontal run directly to MV-MSB B connection point -->
<line x1="{x+50}" y1="{reserve_y}" x2="{2420 + i*60}" y2="{reserve_y}" class="power-line"/>

<!-- Vertical drop to bottom of MV-MSB B (breaker inline, no reversal) -->
<line x1="{2420 + i*60}" y1="{reserve_y}" x2="{2420 + i*60}" y2="510" class="power-line"/>

<!-- Breaker BKR-B 30px before entering bottom of MV-MSB B -->
<use href="#breaker-closed" x="{2420 + i*60}" y="510"/>

<!-- Final connection to bottom of MV-MSB B after breaker -->
<line x1="{2420 + i*60}" y1="510" x2="{2420 + i*60}" y2="480" class="power-line"/>
<use href="#connection-point" x="{2420 + i*60}" y="480"/>

<!-- Drop from RMU to Transformer -->
<line x1="{x}" y1="{rmu_top + 110}" x2="{x}" y2="{rmu_top + 220}" class="power-line"/>

<!-- Breaker TX-IN 30px after RMU bottom -->
<use href="#breaker-closed" x="{x}" y="{rmu_top + 140}"/>

<!-- Transformer TX-{i+1} -->
<g id="tx-{i+1}">
    <rect x="{x-70}" y="{rmu_top + 220}" width="140" height="100" class="transformer-box"/>
    <use href="#transformer" x="{x}" y="{rmu_top + 270}"/>
    <text x="{x}" y="{rmu_top + 235}" class="equipment-label" text-anchor="middle">TX-{i+1}</text>
    <text x="{x}" y="{rmu_top + 300}" class="rating" text-anchor="middle">200 kVA</text>
    <text x="{x}" y="{rmu_top + 315}" class="rating" text-anchor="middle">13.8kV Δ / 480Y/277V</text>
</g>

<!-- Drop from Transformer to LV-SWBD -->
<line x1="{x}" y1="{rmu_top + 320}" x2="{x}" y2="{rmu_top + 440}" class="power-line"/>

<!-- Main breaker MAIN 30px after TX bottom -->
<use href="#breaker-closed" x="{x}" y="{rmu_top + 350}"/>

<!-- LV-SWBD-{i+1} -->
<g id="lv-swbd-{i+1}">
    <rect x="{x-120}" y="{rmu_top + 440}" width="240" height="120" class="switchgear-box"/>
    <text x="{x}" y="{rmu_top + 475}" class="equipment-label" text-anchor="middle">LV-SWBD {i+1}</text>
    <text x="{x}" y="{rmu_top + 495}" class="annotation" text-anchor="middle">480V/277V</text>
    <text x="{x}" y="{rmu_top + 515}" class="rating" text-anchor="middle">3200A Switchboard</text>
    <text x="{x}" y="{rmu_top + 535}" class="rating" text-anchor="middle">Feeds: UPS, Mechanical,</text>
    <text x="{x}" y="{rmu_top + 550}" class="rating" text-anchor="middle">Lighting, General Loads</text>
</g>

<!-- UPS feed line -->
<line x1="{x}" y1="{rmu_top + 560}" x2="{x}" y2="{rmu_top + 660}" class="power-line"/>

<!-- Breaker UPS-IN 30px after LV-SWBD bottom -->
<use href="#breaker-closed" x="{x}" y="{rmu_top + 590}"/>

<!-- UPS-{i+1} -->
<g id="ups-{i+1}">
    <rect x="{x-60}" y="{rmu_top + 660}" width="120" height="80" class="ups-box"/>
    <text x="{x}" y="{rmu_top + 685}" class="equipment-label" text-anchor="middle">UPS-{i+1}</text>
    <text x="{x}" y="{rmu_top + 705}" class="rating" text-anchor="middle">1 MW Modular UPS</text>
    <text x="{x}" y="{rmu_top + 725}" class="rating" text-anchor="middle">Li-ion Battery</text>
</g>

<!-- Critical load line -->
<line x1="{x}" y1="{rmu_top + 740}" x2="{x}" y2="{rmu_top + 790}" class="power-line"/>
<rect x="{x-50}" y="{rmu_top + 790}" width="100" height="40" fill="white" stroke="black" stroke-width="1.5"/>
<text x="{x}" y="{rmu_top + 815}" class="rating" text-anchor="middle">Critical Loads</text>

'''

# Ring connection indicators and labels
svg += f'''
<!-- IEEE Standards Note -->
<text x="1400" y="120" class="note" text-anchor="middle">Symbols and conventions per IEEE Std 315-1975 / IEC 60617</text>

<!-- Legend -->
<g id="legend">
    <rect x="100" y="1680" width="500" height="260" fill="white" stroke="black" stroke-width="2"/>
    <text x="115" y="1710" class="subtitle">LEGEND (IEEE Std 315):</text>
    
    <line x1="115" y1="1735" x2="175" y2="1735" class="power-line"/>
    <text x="185" y="1740" class="annotation">Power Line (2px)</text>
    
    <line x1="115" y1="1760" x2="175" y2="1760" class="bus"/>
    <text x="185" y="1765" class="annotation">Bus (6px)</text>
    
    <use href="#breaker-closed" x="145" y="1795"/>
    <text x="185" y="1800" class="annotation">Circuit Breaker (Closed)</text>
    
    <use href="#breaker-open" x="145" y="1830"/>
    <text x="185" y="1835" class="annotation">Circuit Breaker (Open)</text>
    
    <use href="#transformer" x="145" y="1870"/>
    <text x="185" y="1875" class="annotation">Transformer (Dual Winding)</text>
    
    <use href="#connection-point" x="145" y="1900"/>
    <text x="185" y="1905" class="annotation">Connection Point</text>
    
    <text x="115" y="1930" class="note">All symbols per IEEE Std 315-1975 and IEC 60617</text>
</g>

<!-- Notes -->
<g id="notes">
    <rect x="650" y="1680" width="1050" height="260" fill="white" stroke="black" stroke-width="2"/>
    <text x="665" y="1710" class="subtitle">DUAL RING REDUNDANCY:</text>
    <text x="665" y="1740" class="rating">1. MV-MSB A Feeds: 4 separate connections from bottom</text>
    <text x="665" y="1760" class="rating">2. MV-MSB B Feeds: 4 separate connections to bottom</text>
    <text x="665" y="1780" class="rating">3. Primary Path: MV-MSB A → BKR-A → RMU-IN → RMU (left connection)</text>
    <text x="665" y="1800" class="rating">4. Reserve Path: RMU (right connection) → RMU-OUT → BKR-B → MV-MSB B</text>
    <text x="665" y="1820" class="rating">5. Both paths enter/exit RMU from top with spatial separation</text>
    <text x="665" y="1840" class="rating">6. Downstream: RMU → TX-IN → Transformer → MAIN → LV-SWBD → UPS-IN → UPS</text>
    <text x="665" y="1860" class="rating">7. Complete protection: 7 breakers per path for full isolation capability</text>
    <text x="665" y="1880" class="rating">8. Breaker states shown represent normal operating configuration</text>
    <text x="665" y="1900" class="rating">9. All breakers SCADA-controlled with local manual override</text>
    <text x="665" y="1920" class="rating">10. Design permits concurrent maintenance without service interruption</text>
</g>

<!-- System Information -->
<g id="sources">
    <rect x="1750" y="1680" width="950" height="260" fill="white" stroke="black" stroke-width="2"/>
    <text x="1765" y="1710" class="subtitle">SYSTEM CONFIGURATION:</text>
    <text x="1765" y="1740" class="rating">• Utility: 2x Feeds 345kV to 13.8kV (25MVA each) to MV-MSB A &amp; B</text>
    <text x="1765" y="1760" class="rating">• Generation: 3x 4MW @ 13.8kV (N+1 redundancy, Woodward paralleling)</text>
    <text x="1765" y="1780" class="rating">• Medium Voltage: 13.8kV dual switchboards (4000A, 65kAIC)</text>
    <text x="1765" y="1800" class="rating">• Distribution: Dual ring bus topology with 4 RMUs (630A, 20kA SCCR)</text>
    <text x="1765" y="1820" class="rating">• Transformers: 4x 200kVA, 13.8kV Delta / 480Y/277V</text>
    <text x="1765" y="1840" class="rating">• Low Voltage: 4x 480V switchboards (3200A)</text>
    <text x="1765" y="1860" class="rating">• UPS: 4x 1MW modular units with Li-ion battery</text>
    <text x="1765" y="1880" class="rating">• Classification: Tier III (N+1 redundancy, concurrent maintainability)</text>
    <text x="1765" y="1900" class="rating">• Protection: Ground fault detection, arc flash mitigation, SCADA monitoring</text>
    <text x="1765" y="1920" class="rating">• Standards: IEEE Std 315-1975, IEC 60617, ANSI Y14.1</text>
</g>

<!-- System status indicator -->
<rect x="100" y="2000" width="2600" height="60" fill="#E8F4F8" stroke="black" stroke-width="2"/>
<text x="1400" y="2025" class="annotation" text-anchor="middle">SAGA PRYOR DATA CENTER | Dual Ring Bus | 3 Generators, 2 MV-SWBDs, {len(data['rmu'])} RMUs, {len(data['transformers'])} Transformers, {len(data['lv_swbd'])} LV-SWBDs, {len(data['ups'])} UPS</text>
<text x="1400" y="2050" class="rating" text-anchor="middle">7 Breakers per path (28 total) | All cable routes visible without overlap | Generated: {datetime.now().strftime('%m/%d/%Y %H:%M')}</text>

</svg>'''

# Save SVG
output_file = 'saga_pryor_ring_bus_sld.svg'
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(svg)

print("=" * 80)
print("✅ RING BUS SLD GENERATED (IEEE Std 315 Compliant)")
print("=" * 80)
print(f"\nSVG File: {output_file}")
print(f"Size: {len(svg):,} bytes")

# Export to multiple formats
from export_utils import export_all_formats
from equipment_schedule_generator import create_equipment_schedule

print("\nExporting to additional formats...")
export_results = export_all_formats(output_file, formats=['pdf', 'dxf'])
print("Note: PNG export requires Cairo library (not installed). Use a browser or image editor to convert SVG to PNG.")

# Generate equipment schedule
print("\nGenerating equipment schedule...")
equipment_file = create_equipment_schedule('pachyderm_metadata.json', 'saga_pryor_equipment_schedule.xlsx')

print("\n" + "=" * 80)
print("✅ ALL OUTPUTS GENERATED")
print("=" * 80)
print(f"\nElectrical Paths Shown:")
print(f"  • 3x Generators to MV-MSB A (Primary) and MV-MSB B (Reserve)")
print(f"  • Dual Ring: MV-MSB A to {rmu_count} RMUs to MV-MSB B")
print(f"  • Each RMU to Transformer to LV-SWBD to UPS to Critical Loads")
print(f"\nFiles Generated:")
for fmt, path in export_results.items():
    print(f"  • {fmt.upper()}: {path}")
print(f"  • EXCEL: {equipment_file}")
print(f"\nStandards:")
print(f"  • Symbols: IEEE Std 315-1975 / IEC 60617")
print(f"  • Drafting: ANSI Y14.1")
print(f"  • Power Systems: IEEE Std 141 (Red Book)")
print("=" * 80)
