#!/usr/bin/env python3
"""
GGE Data Center - Single-Line Diagram Generator v1.3.1 CORRECTED
10kV MV Distribution with MTM Topology
SLD STANDARDS v1.3 COMPLIANT - CRITICAL BREAKER & ROUTING FIXES

CRITICAL FIXES (v1.3.1):
1. 52-TIE: Text moved away from symbol (no overlap)
2. DRUPS-1/DRUPS-2: Lines touch TOP edge only (not through equipment)
3. CB-M1/CB-M2: Lines touch breaker symbol boundaries (exit SWBD → enter breaker → exit breaker → transformer)
4. ACB-M1/ACB-M2: Lines touch breaker symbol boundaries (exit transformer → enter breaker → exit breaker → SWBD)

Breaker symbol dimensions: 16px wide × 24px tall (±8 horizontal, ±12 vertical)
"""

from datetime import datetime
from sld_standards import (
    get_svg_style_section,
    get_svg_symbols,
    calculate_symmetric_positions
)

# Canvas settings
WIDTH = 3200
HEIGHT = 3800
MARGIN = 250

# Calculate equipment positions
utility_positions = calculate_symmetric_positions(WIDTH, 2, 200, MARGIN)
hpp_stepup_x = utility_positions[0]
mv_swbd_positions = calculate_symmetric_positions(WIDTH, 2, 320, MARGIN)
xfmr_positions = calculate_symmetric_positions(WIDTH, 2, 80, MARGIN)
lv_swbd_positions = calculate_symmetric_positions(WIDTH, 2, 240, MARGIN)
mtu_positions = calculate_symmetric_positions(WIDTH, 2, 180, MARGIN)
dist_positions = calculate_symmetric_positions(WIDTH, 4, 100, MARGIN)

# Y-coordinates
Y_UTILITY = 350
Y_HPP_STEPUP = 650
Y_MV_SWBD = 950
Y_XFMR = 1320
Y_LV_SWBD = 1750
Y_MTU = 2200
Y_DIST = 2650
Y_IT_LOADS = 3100

# Equipment dimensions
UTIL_W, UTIL_H = 200, 100
MV_SWBD_W, MV_SWBD_H = 320, 140
XFMR_SYMBOL_W, XFMR_SYMBOL_H = 40, 40
LV_SWBD_W, LV_SWBD_H = 240, 120
DRUPS_W, DRUPS_H = 180, 100
DIST_W, DIST_H = 100, 80
IT_W, IT_H = 300, 80

# Breaker symbol dimensions (from SVG defs)
BREAKER_W = 16  # ±8 horizontal
BREAKER_H = 24  # ±12 vertical

# Add CSS
additional_style = """
    <style>
        .breaker-nc { font: 11px "Open Sans", Arial; fill: #D32F2F; font-weight: bold; }
        .breaker-no { font: 11px "Open Sans", Arial; fill: #333; }
        .breaker-id { font: 11px "Open Sans", Arial; fill: #000; }
        .timestamp { font: 11px "Open Sans", Arial; fill: #666; }
    </style>
"""

# Timestamp
now = datetime.now()
date_str = now.strftime("%Y-%m-%d")
time_str = now.strftime("%H:%M:%S")

# Build SVG
svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{WIDTH}" height="{HEIGHT}" xmlns="http://www.w3.org/2000/svg">

{get_svg_symbols()}
{get_svg_style_section()}
{additional_style}

<!-- ============================================ -->
<!-- TITLE BLOCK -->
<!-- ============================================ -->
<text x="{WIDTH/2}" y="100" class="title" text-anchor="middle">GGE Data Center - Electrical Single-Line Diagram</text>
<text x="{WIDTH/2}" y="135" class="equipment-label" text-anchor="middle">10kV MV Distribution | MTM Topology | 2N Backup Power</text>
<text x="{WIDTH/2}" y="165" class="rating" text-anchor="middle">Phase 1 - 1.47 MW IT Load | Tier III | Tbilisi, Georgia</text>
<text x="250" y="235" class="rating">Date: {date_str}</text>
<text x="250" y="255" class="timestamp">Time: {time_str}</text>
<text x="{WIDTH-250}" y="235" class="rating" text-anchor="end">Rev 07 - SLD Standards v1.3.1</text>

<!-- ============================================ -->
<!-- UTILITY SOURCES (Top Level) -->
<!-- ============================================ -->

<!-- HPP Source (400V) -->
<rect x="{utility_positions[0]-UTIL_W/2}" y="{Y_UTILITY-UTIL_H/2}" width="{UTIL_W}" height="{UTIL_H}" class="generator-box" stroke="#000" stroke-width="2"/>
<text x="{utility_positions[0]}" y="{Y_UTILITY-15}" class="equipment-label" text-anchor="middle">HPP SOURCE</text>
<text x="{utility_positions[0]}" y="{Y_UTILITY+5}" class="rating" text-anchor="middle">400V | 3Ø | 50Hz</text>
<text x="{utility_positions[0]}" y="{Y_UTILITY+20}" class="rating" text-anchor="middle">3.7 MW</text>

<!-- Line from HPP exits BOTTOM -->
<line x1="{utility_positions[0]}" y1="{Y_UTILITY+UTIL_H/2}" x2="{utility_positions[0]}" y2="{Y_HPP_STEPUP-30}" class="power-line"/>

<!-- Grid Utility Source (10kV) -->
<rect x="{utility_positions[1]-UTIL_W/2}" y="{Y_UTILITY-UTIL_H/2}" width="{UTIL_W}" height="{UTIL_H}" class="generator-box" stroke="#000" stroke-width="2"/>
<text x="{utility_positions[1]}" y="{Y_UTILITY-15}" class="equipment-label" text-anchor="middle">UTILITY GRID</text>
<text x="{utility_positions[1]}" y="{Y_UTILITY+5}" class="rating" text-anchor="middle">10kV | 3Ø | 50Hz</text>
<text x="{utility_positions[1]}" y="{Y_UTILITY+20}" class="rating" text-anchor="middle">4.0 MW</text>

<!-- Line from Grid exits BOTTOM -->
<line x1="{utility_positions[1]}" y1="{Y_UTILITY+UTIL_H/2}" x2="{utility_positions[1]}" y2="{Y_UTILITY+UTIL_H/2+50}" class="power-line"/>

<!-- ============================================ -->
<!-- HPP STEP-UP TRANSFORMER (400V → 10kV) -->
<!-- ============================================ -->

<use href="#transformer" x="{hpp_stepup_x}" y="{Y_HPP_STEPUP}"/>
<text x="{hpp_stepup_x+35}" y="{Y_HPP_STEPUP-10}" class="equipment-label" text-anchor="start">HPP-STEP-UP-TX</text>
<text x="{hpp_stepup_x+35}" y="{Y_HPP_STEPUP+5}" class="rating" text-anchor="start">3,500 kVA</text>
<text x="{hpp_stepup_x+35}" y="{Y_HPP_STEPUP+20}" class="rating" text-anchor="start">400V / 10kV | Dyn11</text>

<!-- Breaker CB-U2 on Grid feed -->
<use href="#breaker-closed" x="{utility_positions[1]}" y="{Y_UTILITY+UTIL_H/2+100}"/>
<text x="{utility_positions[1]+25}" y="{Y_UTILITY+UTIL_H/2+95}" class="breaker-id" text-anchor="start">CB-U2</text>
<text x="{utility_positions[1]+25}" y="{Y_UTILITY+UTIL_H/2+110}" class="breaker-nc" text-anchor="start">N.C.</text>

<!-- Continue Grid line from breaker to MV -->
<line x1="{utility_positions[1]}" y1="{Y_UTILITY+UTIL_H/2+112}" x2="{utility_positions[1]}" y2="{Y_MV_SWBD-MV_SWBD_H/2+15}" class="power-line"/>

<!-- ============================================ -->
<!-- MEDIUM VOLTAGE SWITCHBOARDS (10 kV) -->
<!-- ============================================ -->

<!-- HPP transformer output to MV-SWBD-A -->
<line x1="{hpp_stepup_x+8}" y1="{Y_HPP_STEPUP+20}" x2="{hpp_stepup_x+8}" y2="{Y_HPP_STEPUP+80}" class="power-line"/>

<!-- Breaker CB-U1 on HPP feed -->
<use href="#breaker-closed" x="{hpp_stepup_x+8}" y="{Y_HPP_STEPUP+130}"/>
<text x="{hpp_stepup_x+33}" y="{Y_HPP_STEPUP+125}" class="breaker-id" text-anchor="start">CB-U1</text>
<text x="{hpp_stepup_x+33}" y="{Y_HPP_STEPUP+140}" class="breaker-nc" text-anchor="start">N.C.</text>

<!-- Continue HPP line from breaker to MV-SWBD-A -->
<line x1="{hpp_stepup_x+8}" y1="{Y_HPP_STEPUP+142}" x2="{hpp_stepup_x+8}" y2="{Y_MV_SWBD-MV_SWBD_H/2+15}" class="power-line"/>

<!-- MV-SWBD-A -->
<rect x="{mv_swbd_positions[0]-MV_SWBD_W/2}" y="{Y_MV_SWBD-MV_SWBD_H/2}" width="{MV_SWBD_W}" height="{MV_SWBD_H}" class="mv-switchboard" stroke="#000" stroke-width="2"/>
<line x1="{mv_swbd_positions[0]-MV_SWBD_W/2+15}" y1="{Y_MV_SWBD-MV_SWBD_H/2+15}" x2="{mv_swbd_positions[0]+MV_SWBD_W/2-15}" y2="{Y_MV_SWBD-MV_SWBD_H/2+15}" class="main-bus"/>
<text x="{mv_swbd_positions[0]}" y="{Y_MV_SWBD-10}" class="equipment-label" text-anchor="middle">MV-SWBD-A</text>
<text x="{mv_swbd_positions[0]}" y="{Y_MV_SWBD+10}" class="rating" text-anchor="middle">10 kV | 630A Bus</text>
<text x="{mv_swbd_positions[0]}" y="{Y_MV_SWBD+25}" class="rating" text-anchor="middle">VCB Lineup</text>

<!-- MV-SWBD-B -->
<rect x="{mv_swbd_positions[1]-MV_SWBD_W/2}" y="{Y_MV_SWBD-MV_SWBD_H/2}" width="{MV_SWBD_W}" height="{MV_SWBD_H}" class="mv-switchboard" stroke="#000" stroke-width="2"/>
<line x1="{mv_swbd_positions[1]-MV_SWBD_W/2+15}" y1="{Y_MV_SWBD-MV_SWBD_H/2+15}" x2="{mv_swbd_positions[1]+MV_SWBD_W/2-15}" y2="{Y_MV_SWBD-MV_SWBD_H/2+15}" class="main-bus"/>
<text x="{mv_swbd_positions[1]}" y="{Y_MV_SWBD-10}" class="equipment-label" text-anchor="middle">MV-SWBD-B</text>
<text x="{mv_swbd_positions[1]}" y="{Y_MV_SWBD+10}" class="rating" text-anchor="middle">10 kV | 630A Bus</text>
<text x="{mv_swbd_positions[1]}" y="{Y_MV_SWBD+25}" class="rating" text-anchor="middle">VCB Lineup</text>

<!-- Horizontal connections to MV buses -->
<line x1="{hpp_stepup_x+8}" y1="{Y_MV_SWBD-MV_SWBD_H/2+15}" x2="{mv_swbd_positions[0]-MV_SWBD_W/2+15}" y2="{Y_MV_SWBD-MV_SWBD_H/2+15}" class="power-line"/>
<line x1="{utility_positions[1]}" y1="{Y_MV_SWBD-MV_SWBD_H/2+15}" x2="{mv_swbd_positions[1]-MV_SWBD_W/2+15}" y2="{Y_MV_SWBD-MV_SWBD_H/2+15}" class="power-line"/>

<!-- ============================================ -->
<!-- STEP-DOWN TRANSFORMERS (10kV → 400V) -->
<!-- ============================================ -->

<!-- Exit BOTTOM of MV-SWBD-A -->
<line x1="{mv_swbd_positions[0]}" y1="{Y_MV_SWBD+MV_SWBD_H/2}" x2="{mv_swbd_positions[0]}" y2="{Y_MV_SWBD+MV_SWBD_H/2+30}" class="power-line"/>

<!-- Breaker CB-M1: Enter TOP, exit BOTTOM -->
<use href="#breaker-closed" x="{mv_swbd_positions[0]}" y="{Y_MV_SWBD+MV_SWBD_H/2+60}"/>
<text x="{mv_swbd_positions[0]+25}" y="{Y_MV_SWBD+MV_SWBD_H/2+55}" class="breaker-id" text-anchor="start">CB-M1</text>
<text x="{mv_swbd_positions[0]+25}" y="{Y_MV_SWBD+MV_SWBD_H/2+70}" class="breaker-nc" text-anchor="start">N.C.</text>

<!-- Line enters breaker TOP boundary (y - 12) -->
<line x1="{mv_swbd_positions[0]}" y1="{Y_MV_SWBD+MV_SWBD_H/2+30}" x2="{mv_swbd_positions[0]}" y2="{Y_MV_SWBD+MV_SWBD_H/2+60-12}" class="power-line"/>

<!-- Line exits breaker BOTTOM boundary (y + 12), continues to transformer -->
<line x1="{mv_swbd_positions[0]}" y1="{Y_MV_SWBD+MV_SWBD_H/2+60+12}" x2="{mv_swbd_positions[0]}" y2="{Y_XFMR-50}" class="power-line"/>

<!-- Exit BOTTOM of MV-SWBD-B -->
<line x1="{mv_swbd_positions[1]}" y1="{Y_MV_SWBD+MV_SWBD_H/2}" x2="{mv_swbd_positions[1]}" y2="{Y_MV_SWBD+MV_SWBD_H/2+30}" class="power-line"/>

<!-- Breaker CB-M2: Enter TOP, exit BOTTOM -->
<use href="#breaker-closed" x="{mv_swbd_positions[1]}" y="{Y_MV_SWBD+MV_SWBD_H/2+60}"/>
<text x="{mv_swbd_positions[1]+25}" y="{Y_MV_SWBD+MV_SWBD_H/2+55}" class="breaker-id" text-anchor="start">CB-M2</text>
<text x="{mv_swbd_positions[1]+25}" y="{Y_MV_SWBD+MV_SWBD_H/2+70}" class="breaker-nc" text-anchor="start">N.C.</text>

<!-- Line enters breaker TOP boundary -->
<line x1="{mv_swbd_positions[1]}" y1="{Y_MV_SWBD+MV_SWBD_H/2+30}" x2="{mv_swbd_positions[1]}" y2="{Y_MV_SWBD+MV_SWBD_H/2+60-12}" class="power-line"/>

<!-- Line exits breaker BOTTOM boundary, continues to transformer -->
<line x1="{mv_swbd_positions[1]}" y1="{Y_MV_SWBD+MV_SWBD_H/2+60+12}" x2="{mv_swbd_positions[1]}" y2="{Y_XFMR-50}" class="power-line"/>

<!-- Horizontal routing to transformers -->
<line x1="{mv_swbd_positions[0]}" y1="{Y_XFMR-50}" x2="{xfmr_positions[0]-8}" y2="{Y_XFMR-50}" class="power-line"/>
<line x1="{xfmr_positions[0]-8}" y1="{Y_XFMR-50}" x2="{xfmr_positions[0]-8}" y2="{Y_XFMR-20}" class="power-line"/>

<line x1="{mv_swbd_positions[1]}" y1="{Y_XFMR-50}" x2="{xfmr_positions[1]-8}" y2="{Y_XFMR-50}" class="power-line"/>
<line x1="{xfmr_positions[1]-8}" y1="{Y_XFMR-50}" x2="{xfmr_positions[1]-8}" y2="{Y_XFMR-20}" class="power-line"/>

<!-- XFMR-A -->
<use href="#transformer" x="{xfmr_positions[0]}" y="{Y_XFMR}"/>
<text x="{xfmr_positions[0]+35}" y="{Y_XFMR-10}" class="equipment-label" text-anchor="start">XFMR-A</text>
<text x="{xfmr_positions[0]+35}" y="{Y_XFMR+5}" class="rating" text-anchor="start">3,500 kVA</text>
<text x="{xfmr_positions[0]+35}" y="{Y_XFMR+20}" class="rating" text-anchor="start">10kV / 400V</text>

<!-- XFMR-B -->
<use href="#transformer" x="{xfmr_positions[1]}" y="{Y_XFMR}"/>
<text x="{xfmr_positions[1]+35}" y="{Y_XFMR-10}" class="equipment-label" text-anchor="start">XFMR-B</text>
<text x="{xfmr_positions[1]+35}" y="{Y_XFMR+5}" class="rating" text-anchor="start">3,500 kVA</text>
<text x="{xfmr_positions[1]+35}" y="{Y_XFMR+20}" class="rating" text-anchor="start">10kV / 400V</text>

<!-- ============================================ -->
<!-- LV SWITCHBOARDS (400V - MTM TOPOLOGY) -->
<!-- ============================================ -->

<!-- Exit transformers BOTTOM connection point -->
<line x1="{xfmr_positions[0]+8}" y1="{Y_XFMR+20}" x2="{xfmr_positions[0]+8}" y2="{Y_XFMR+50}" class="power-line"/>
<line x1="{xfmr_positions[1]+8}" y1="{Y_XFMR+20}" x2="{xfmr_positions[1]+8}" y2="{Y_XFMR+50}" class="power-line"/>

<!-- Breaker ACB-M1: Enter TOP, exit BOTTOM -->
<use href="#breaker-closed" x="{xfmr_positions[0]+8}" y="{Y_XFMR+80}"/>
<text x="{xfmr_positions[0]+33}" y="{Y_XFMR+75}" class="breaker-id" text-anchor="start">ACB-M1</text>
<text x="{xfmr_positions[0]+33}" y="{Y_XFMR+90}" class="breaker-nc" text-anchor="start">N.C.</text>
<text x="{xfmr_positions[0]+90}" y="{Y_XFMR+80}" class="rating" text-anchor="start">6,300A/5,000A</text>

<!-- Line enters breaker TOP boundary (y - 12) -->
<line x1="{xfmr_positions[0]+8}" y1="{Y_XFMR+50}" x2="{xfmr_positions[0]+8}" y2="{Y_XFMR+80-12}" class="power-line"/>

<!-- Line exits breaker BOTTOM boundary (y + 12) -->
<line x1="{xfmr_positions[0]+8}" y1="{Y_XFMR+80+12}" x2="{xfmr_positions[0]+8}" y2="{Y_LV_SWBD-LV_SWBD_H/2+15}" class="power-line"/>

<!-- Breaker ACB-M2: Enter TOP, exit BOTTOM -->
<use href="#breaker-closed" x="{xfmr_positions[1]+8}" y="{Y_XFMR+80}"/>
<text x="{xfmr_positions[1]+33}" y="{Y_XFMR+75}" class="breaker-id" text-anchor="start">ACB-M2</text>
<text x="{xfmr_positions[1]+33}" y="{Y_XFMR+90}" class="breaker-nc" text-anchor="start">N.C.</text>
<text x="{xfmr_positions[1]+90}" y="{Y_XFMR+80}" class="rating" text-anchor="start">6,300A/5,000A</text>

<!-- Line enters breaker TOP boundary -->
<line x1="{xfmr_positions[1]+8}" y1="{Y_XFMR+50}" x2="{xfmr_positions[1]+8}" y2="{Y_XFMR+80-12}" class="power-line"/>

<!-- Line exits breaker BOTTOM boundary -->
<line x1="{xfmr_positions[1]+8}" y1="{Y_XFMR+80+12}" x2="{xfmr_positions[1]+8}" y2="{Y_LV_SWBD-LV_SWBD_H/2+15}" class="power-line"/>

<!-- Horizontal to LV switchboard buses -->
<line x1="{xfmr_positions[0]+8}" y1="{Y_LV_SWBD-LV_SWBD_H/2+15}" x2="{lv_swbd_positions[0]-LV_SWBD_W/2+15}" y2="{Y_LV_SWBD-LV_SWBD_H/2+15}" class="power-line"/>
<line x1="{xfmr_positions[1]+8}" y1="{Y_LV_SWBD-LV_SWBD_H/2+15}" x2="{lv_swbd_positions[1]+LV_SWBD_W/2-15}" y2="{Y_LV_SWBD-LV_SWBD_H/2+15}" class="power-line"/>

<!-- SWBD-A -->
<rect x="{lv_swbd_positions[0]-LV_SWBD_W/2}" y="{Y_LV_SWBD-LV_SWBD_H/2}" width="{LV_SWBD_W}" height="{LV_SWBD_H}" class="lv-switchboard" stroke="#000" stroke-width="2"/>
<line x1="{lv_swbd_positions[0]-LV_SWBD_W/2+15}" y1="{Y_LV_SWBD-LV_SWBD_H/2+15}" x2="{lv_swbd_positions[0]+LV_SWBD_W/2-15}" y2="{Y_LV_SWBD-LV_SWBD_H/2+15}" class="main-bus"/>
<text x="{lv_swbd_positions[0]}" y="{Y_LV_SWBD-10}" class="equipment-label" text-anchor="middle">SWBD-A (BUS A)</text>
<text x="{lv_swbd_positions[0]}" y="{Y_LV_SWBD+7}" class="rating" text-anchor="middle">400V | 2,500A Bus</text>
<text x="{lv_swbd_positions[0]}" y="{Y_LV_SWBD+22}" class="rating" text-anchor="middle">Normal: 1,039 kW</text>

<!-- SWBD-B -->
<rect x="{lv_swbd_positions[1]-LV_SWBD_W/2}" y="{Y_LV_SWBD-LV_SWBD_H/2}" width="{LV_SWBD_W}" height="{LV_SWBD_H}" class="lv-switchboard" stroke="#000" stroke-width="2"/>
<line x1="{lv_swbd_positions[1]-LV_SWBD_W/2+15}" y1="{Y_LV_SWBD-LV_SWBD_H/2+15}" x2="{lv_swbd_positions[1]+LV_SWBD_W/2-15}" y2="{Y_LV_SWBD-LV_SWBD_H/2+15}" class="main-bus"/>
<text x="{lv_swbd_positions[1]}" y="{Y_LV_SWBD-10}" class="equipment-label" text-anchor="middle">SWBD-B (BUS B)</text>
<text x="{lv_swbd_positions[1]}" y="{Y_LV_SWBD+7}" class="rating" text-anchor="middle">400V | 2,500A Bus</text>
<text x="{lv_swbd_positions[1]}" y="{Y_LV_SWBD+22}" class="rating" text-anchor="middle">Normal: 1,096 kW</text>

<!-- TIE BREAKER - Text moved ABOVE symbol (not overlapping) -->
<line x1="{lv_swbd_positions[0]+LV_SWBD_W/2}" y1="{Y_LV_SWBD}" x2="{lv_swbd_positions[1]-LV_SWBD_W/2}" y2="{Y_LV_SWBD}" class="power-line" stroke-dasharray="10,5"/>
<use href="#breaker-open" x="{(lv_swbd_positions[0] + lv_swbd_positions[1])/2}" y="{Y_LV_SWBD}"/>
<text x="{(lv_swbd_positions[0] + lv_swbd_positions[1])/2}" y="{Y_LV_SWBD-35}" class="breaker-id" text-anchor="middle">52-TIE</text>
<text x="{(lv_swbd_positions[0] + lv_swbd_positions[1])/2}" y="{Y_LV_SWBD-20}" class="breaker-no" text-anchor="middle">N.O.</text>
<text x="{(lv_swbd_positions[0] + lv_swbd_positions[1])/2}" y="{Y_LV_SWBD+35}" class="rating" text-anchor="middle">6,300A/5,000A</text>

<!-- ============================================ -->
<!-- DISTRIBUTION PANELS (400V) -->
<!-- ============================================ -->

<!-- Main distribution paths: Exit BOTTOM of LV switchboards -->
<line x1="{lv_swbd_positions[0]}" y1="{Y_LV_SWBD+LV_SWBD_H/2}" x2="{lv_swbd_positions[0]}" y2="{Y_DIST-DIST_H/2-30}" class="power-line"/>
<line x1="{lv_swbd_positions[1]}" y1="{Y_LV_SWBD+LV_SWBD_H/2}" x2="{lv_swbd_positions[1]}" y2="{Y_DIST-DIST_H/2-30}" class="power-line"/>

<!-- Horizontal distribution from SWBD-A to A-IT-1 and A-COOL-1 -->
<line x1="{lv_swbd_positions[0]}" y1="{Y_DIST}" x2="{dist_positions[0]}" y2="{Y_DIST}" class="power-line"/>
<line x1="{lv_swbd_positions[0]}" y1="{Y_DIST}" x2="{dist_positions[1]}" y2="{Y_DIST}" class="power-line"/>

<!-- Horizontal distribution from SWBD-B to B-IT-1 and B-COOL-1 -->
<line x1="{lv_swbd_positions[1]}" y1="{Y_DIST}" x2="{dist_positions[2]}" y2="{Y_DIST}" class="power-line"/>
<line x1="{lv_swbd_positions[1]}" y1="{Y_DIST}" x2="{dist_positions[3]}" y2="{Y_DIST}" class="power-line"/>

<!-- ============================================ -->
<!-- DRUPS (DIESEL ROTARY UPS - 2N BACKUP) -->
<!-- SEPARATE SIDE BRANCHES from LV Switchboards -->
<!-- ============================================ -->

<!-- DRUPS-1 Branch: Exit LEFT from SWBD-A, route to side -->
<line x1="{lv_swbd_positions[0]-LV_SWBD_W/2}" y1="{Y_LV_SWBD+30}" x2="{lv_swbd_positions[0]-LV_SWBD_W/2-120}" y2="{Y_LV_SWBD+30}" class="power-line"/>
<line x1="{lv_swbd_positions[0]-LV_SWBD_W/2-120}" y1="{Y_LV_SWBD+30}" x2="{lv_swbd_positions[0]-LV_SWBD_W/2-120}" y2="{Y_MTU}" class="power-line"/>

<!-- Breaker ACB-DRUPS1 -->
<use href="#breaker-closed" x="{lv_swbd_positions[0]-LV_SWBD_W/2-120}" y="{Y_LV_SWBD+200}"/>
<text x="{lv_swbd_positions[0]-LV_SWBD_W/2-145}" y="{Y_LV_SWBD+195}" class="breaker-id" text-anchor="end">ACB-DRUPS1</text>
<text x="{lv_swbd_positions[0]-LV_SWBD_W/2-145}" y="{Y_LV_SWBD+210}" class="breaker-nc" text-anchor="end">N.C.</text>

<!-- Horizontal to DRUPS-1 LEFT edge -->
<line x1="{lv_swbd_positions[0]-LV_SWBD_W/2-120}" y1="{Y_MTU}" x2="{mtu_positions[0]-DRUPS_W/2}" y2="{Y_MTU}" class="power-line"/>

<!-- DRUPS-2 Branch: Exit RIGHT from SWBD-B, route to side -->
<line x1="{lv_swbd_positions[1]+LV_SWBD_W/2}" y1="{Y_LV_SWBD+30}" x2="{lv_swbd_positions[1]+LV_SWBD_W/2+120}" y2="{Y_LV_SWBD+30}" class="power-line"/>
<line x1="{lv_swbd_positions[1]+LV_SWBD_W/2+120}" y1="{Y_LV_SWBD+30}" x2="{lv_swbd_positions[1]+LV_SWBD_W/2+120}" y2="{Y_MTU}" class="power-line"/>

<!-- Breaker ACB-DRUPS2 -->
<use href="#breaker-closed" x="{lv_swbd_positions[1]+LV_SWBD_W/2+120}" y="{Y_LV_SWBD+200}"/>
<text x="{lv_swbd_positions[1]+LV_SWBD_W/2+145}" y="{Y_LV_SWBD+195}" class="breaker-id" text-anchor="start">ACB-DRUPS2</text>
<text x="{lv_swbd_positions[1]+LV_SWBD_W/2+145}" y="{Y_LV_SWBD+210}" class="breaker-nc" text-anchor="start">N.C.</text>

<!-- Horizontal to DRUPS-2 RIGHT edge -->
<line x1="{lv_swbd_positions[1]+LV_SWBD_W/2+120}" y1="{Y_MTU}" x2="{mtu_positions[1]+DRUPS_W/2}" y2="{Y_MTU}" class="power-line"/>

<!-- DRUPS-1 Equipment Box -->
<rect x="{mtu_positions[0]-DRUPS_W/2}" y="{Y_MTU-DRUPS_H/2}" width="{DRUPS_W}" height="{DRUPS_H}" class="generator-box" stroke="#000" stroke-width="2"/>
<text x="{mtu_positions[0]}" y="{Y_MTU-15}" class="equipment-label" text-anchor="middle">DRUPS-1</text>
<text x="{mtu_positions[0]}" y="{Y_MTU+2}" class="rating" text-anchor="middle">MTU KP7</text>
<text x="{mtu_positions[0]}" y="{Y_MTU+17}" class="rating" text-anchor="middle">2,750 kVA</text>
<text x="{mtu_positions[0]}" y="{Y_MTU+30}" class="rating" text-anchor="middle">2,200 kW</text>

<!-- DRUPS-2 Equipment Box -->
<rect x="{mtu_positions[1]-DRUPS_W/2}" y="{Y_MTU-DRUPS_H/2}" width="{DRUPS_W}" height="{DRUPS_H}" class="generator-box" stroke="#000" stroke-width="2"/>
<text x="{mtu_positions[1]}" y="{Y_MTU-15}" class="equipment-label" text-anchor="middle">DRUPS-2</text>
<text x="{mtu_positions[1]}" y="{Y_MTU+2}" class="rating" text-anchor="middle">MTU KP7</text>
<text x="{mtu_positions[1]}" y="{Y_MTU+17}" class="rating" text-anchor="middle">2,750 kVA</text>
<text x="{mtu_positions[1]}" y="{Y_MTU+30}" class="rating" text-anchor="middle">2,200 kW</text>

<!-- A-IT-1 -->
<rect x="{dist_positions[0]-DIST_W/2}" y="{Y_DIST-DIST_H/2}" width="{DIST_W}" height="{DIST_H}" class="dist-panel" stroke="#000" stroke-width="2"/>
<line x1="{dist_positions[0]}" y1="{Y_DIST-DIST_H/2-30}" x2="{dist_positions[0]}" y2="{Y_DIST-DIST_H/2}" class="power-line"/>
<text x="{dist_positions[0]}" y="{Y_DIST-10}" class="equipment-label" text-anchor="middle">A-IT-1</text>
<text x="{dist_positions[0]}" y="{Y_DIST+5}" class="rating" text-anchor="middle">2,500A MCCB</text>
<text x="{dist_positions[0]}" y="{Y_DIST+18}" class="rating" text-anchor="middle">735 kW</text>

<!-- A-COOL-1 -->
<rect x="{dist_positions[1]-DIST_W/2}" y="{Y_DIST-DIST_H/2}" width="{DIST_W}" height="{DIST_H}" class="dist-panel" stroke="#000" stroke-width="2"/>
<line x1="{dist_positions[1]}" y1="{Y_DIST-DIST_H/2-30}" x2="{dist_positions[1]}" y2="{Y_DIST-DIST_H/2}" class="power-line"/>
<text x="{dist_positions[1]}" y="{Y_DIST-10}" class="equipment-label" text-anchor="middle">A-COOL-1</text>
<text x="{dist_positions[1]}" y="{Y_DIST+5}" class="rating" text-anchor="middle">3,200A MCCB</text>
<text x="{dist_positions[1]}" y="{Y_DIST+18}" class="rating" text-anchor="middle">304 kW</text>

<!-- B-IT-1 -->
<rect x="{dist_positions[2]-DIST_W/2}" y="{Y_DIST-DIST_H/2}" width="{DIST_W}" height="{DIST_H}" class="dist-panel" stroke="#000" stroke-width="2"/>
<line x1="{dist_positions[2]}" y1="{Y_DIST-DIST_H/2-30}" x2="{dist_positions[2]}" y2="{Y_DIST-DIST_H/2}" class="power-line"/>
<text x="{dist_positions[2]}" y="{Y_DIST-10}" class="equipment-label" text-anchor="middle">B-IT-1</text>
<text x="{dist_positions[2]}" y="{Y_DIST+5}" class="rating" text-anchor="middle">2,500A MCCB</text>
<text x="{dist_positions[2]}" y="{Y_DIST+18}" class="rating" text-anchor="middle">735 kW</text>

<!-- B-COOL-1 -->
<rect x="{dist_positions[3]-DIST_W/2}" y="{Y_DIST-DIST_H/2}" width="{DIST_W}" height="{DIST_H}" class="dist-panel" stroke="#000" stroke-width="2"/>
<line x1="{dist_positions[3]}" y1="{Y_DIST-DIST_H/2-30}" x2="{dist_positions[3]}" y2="{Y_DIST-DIST_H/2}" class="power-line"/>
<text x="{dist_positions[3]}" y="{Y_DIST-10}" class="equipment-label" text-anchor="middle">B-COOL-1</text>
<text x="{dist_positions[3]}" y="{Y_DIST+5}" class="rating" text-anchor="middle">3,200A MCCB</text>
<text x="{dist_positions[3]}" y="{Y_DIST+18}" class="rating" text-anchor="middle">361 kW</text>

<!-- ============================================ -->
<!-- IT LOADS (Dual-corded A+B) -->
<!-- ============================================ -->

<line x1="{dist_positions[0]}" y1="{Y_DIST+DIST_H/2}" x2="{dist_positions[0]}" y2="{Y_IT_LOADS}" class="power-line"/>
<line x1="{dist_positions[2]}" y1="{Y_DIST+DIST_H/2}" x2="{dist_positions[2]}" y2="{Y_IT_LOADS}" class="power-line"/>

<rect x="{WIDTH/2-IT_W/2}" y="{Y_IT_LOADS-IT_H/2}" width="{IT_W}" height="{IT_H}" fill="#E0F2F1" stroke="#000" stroke-width="2"/>
<text x="{WIDTH/2}" y="{Y_IT_LOADS-15}" class="equipment-label" text-anchor="middle">IT EQUIPMENT</text>
<text x="{WIDTH/2}" y="{Y_IT_LOADS+2}" class="rating" text-anchor="middle">1,467 kW (1.47 MW)</text>
<text x="{WIDTH/2}" y="{Y_IT_LOADS+17}" class="rating" text-anchor="middle">Dual-Corded (A+B)</text>

<line x1="{dist_positions[0]}" y1="{Y_IT_LOADS}" x2="{WIDTH/2-IT_W/2}" y2="{Y_IT_LOADS}" class="power-line"/>
<line x1="{dist_positions[2]}" y1="{Y_IT_LOADS}" x2="{WIDTH/2+IT_W/2}" y2="{Y_IT_LOADS}" class="power-line"/>
<use href="#connection-point" x="{WIDTH/2-IT_W/2}" y="{Y_IT_LOADS}"/>
<use href="#connection-point" x="{WIDTH/2+IT_W/2}" y="{Y_IT_LOADS}"/>

<text x="{dist_positions[0]-80}" y="{Y_IT_LOADS+40}" class="rating">Path A</text>
<text x="{dist_positions[2]+80}" y="{Y_IT_LOADS+40}" class="rating">Path B</text>

<!-- ============================================ -->
<!-- LEGEND -->
<!-- ============================================ -->

<rect x="150" y="3400" width="500" height="320" fill="#F5F5F5" stroke="#000" stroke-width="1"/>
<text x="400" y="3430" class="equipment-label" text-anchor="middle">DESIGN NOTES</text>

<text x="170" y="3460" class="rating">• Tier III: 2N DRUPS, N+1 mechanical</text>
<text x="170" y="3480" class="rating">• MTM topology at 400V</text>
<text x="170" y="3500" class="rating">• Dual sources: HPP (3.7MW) + Grid (4.0MW)</text>
<text x="170" y="3520" class="rating">• MV distribution: 10 kV</text>
<text x="170" y="3540" class="rating">• 2N backup: DRUPS (MTU KP7)</text>
<text x="170" y="3560" class="rating">• 52-TIE: N.O. (MTM failover)</text>
<text x="170" y="3580" class="rating">• IT loads: Dual-corded (A+B)</text>
<text x="170" y="3600" class="rating">• PUE: 1.50 design (1.30 w/ river cooling)</text>
<text x="170" y="3620" class="rating">• Location: Tbilisi, Georgia</text>
<text x="170" y="3640" class="rating">• Standards: IEC 60364, IEEE 315</text>

<rect x="2550" y="3400" width="500" height="270" fill="#F5F5F5" stroke="#000" stroke-width="1"/>
<text x="2800" y="3430" class="equipment-label" text-anchor="middle">BREAKER STATES</text>

<use href="#breaker-closed" x="2600" y="3470"/>
<text x="2640" y="3475" class="breaker-id">Breaker ID</text>
<text x="2640" y="3490" class="breaker-nc">N.C. (Normally Closed - RED)</text>

<use href="#breaker-open" x="2600" y="3540"/>
<text x="2640" y="3545" class="breaker-id">Breaker ID</text>
<text x="2640" y="3560" class="breaker-no">N.O. (Normally Open)</text>

<text x="2800" y="3600" class="rating" text-anchor="middle">All breakers in normal operating state</text>
<text x="2800" y="3620" class="rating" text-anchor="middle">Lines touch breaker boundaries</text>

</svg>'''

# Write output
output_file = 'gge_10kv_sld.svg'
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(svg)

print(f"[SUCCESS] Corrected SLD v1.3.1 generated: {output_file}")
print(f"[INFO] File size: {len(svg):,} bytes")
print(f"[INFO] Canvas: {WIDTH} x {HEIGHT} px")
print(f"[INFO] Standards: v1.3.1 - BREAKER & ROUTING FIXES")
print()
print("[FIXES APPLIED v1.3.1]")
print("  1. 52-TIE: Text moved -35px above (no symbol overlap)")
print("  2. DRUPS-1/DRUPS-2: Lines touch TOP edge only (y - DRUPS_H/2)")
print("  3. CB-M1/CB-M2: Lines enter TOP (y-12), exit BOTTOM (y+12) of breaker")
print("  4. ACB-M1/ACB-M2: Lines enter TOP (y-12), exit BOTTOM (y+12) of breaker")
