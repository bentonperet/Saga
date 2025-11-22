#!/usr/bin/env python3
"""
GGE Data Center - Single-Line Diagram Generator v1.4
Based on test_standards_output.svg reference layout
10kV MV Distribution with MTM Topology + DRUPS backup

Layout: Vertical flow, side-by-side A/B paths, DRUPS as side branches
"""

from datetime import datetime
from sld_standards import get_svg_style_section, get_svg_symbols

# Canvas settings
WIDTH = 2400
HEIGHT = 3200
MARGIN = 150

# Equipment positions - side by side layout
X_PATH_A = 600   # Left path (HPP + DRUPS-1)
X_PATH_B = 1800  # Right path (Grid + DRUPS-2)
X_CENTER = (X_PATH_A + X_PATH_B) / 2

# Y-coordinates for vertical flow
Y_UTILITY = 200
Y_MV_SWBD = 500
Y_XFMR = 900
Y_LV_SWBD = 1400
Y_DRUPS = 1400   # Same level as LV-SWBD (side branches)
Y_DIST = 1900
Y_IT_LOADS = 2400

# Equipment dimensions
UTIL_W, UTIL_H = 150, 80
MV_SWBD_W, MV_SWBD_H = 240, 120
XFMR_BOX_W, XFMR_BOX_H = 100, 120
LV_SWBD_W, LV_SWBD_H = 200, 100
DRUPS_W, DRUPS_H = 180, 100
DIST_W, DIST_H = 90, 60

# Breaker symbol: ±8 horizontal, ±12 vertical
BREAKER_H = 24

# Timestamp
now = datetime.now()
date_str = now.strftime("%Y-%m-%d")
time_str = now.strftime("%H:%M:%S")

# Breaker CSS
breaker_css = """
    <style>
        .breaker-nc { font: 11px "Open Sans", Arial; fill: #D32F2F; font-weight: bold; }
        .breaker-no { font: 11px "Open Sans", Arial; fill: #333; }
        .breaker-id { font: 11px "Open Sans", Arial; fill: #000; }
        .timestamp { font: 11px "Open Sans", Arial; fill: #666; }
    </style>
"""

# Build SVG
svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{WIDTH}" height="{HEIGHT}" xmlns="http://www.w3.org/2000/svg">

{get_svg_symbols()}
{get_svg_style_section()}
{breaker_css}

<!-- ===================================================================== -->
<!--                              TITLE BLOCK                              -->
<!-- ===================================================================== -->
<rect x="50" y="30" width="{WIDTH-250}" height="80" fill="white" stroke="black" stroke-width="2"/>
<text x="{WIDTH/2}" y="65" class="title" text-anchor="middle">GGE Data Center - Electrical Single-Line Diagram</text>
<text x="{WIDTH/2}" y="90" class="rating" text-anchor="middle">10kV MV Distribution | MTM Topology | 2N DRUPS Backup | Tier III | Tbilisi, Georgia</text>

<rect x="{WIDTH-190}" y="30" width="140" height="80" fill="white" stroke="black" stroke-width="2"/>
<text x="{WIDTH-180}" y="55" class="rating">Date: {date_str}</text>
<text x="{WIDTH-180}" y="72" class="timestamp">Time: {time_str}</text>
<text x="{WIDTH-180}" y="92" class="rating">Rev: 08</text>

<!-- ===================================================================== -->
<!--                          UTILITY SOURCES                              -->
<!-- ===================================================================== -->

<!-- HPP Source (400V) - Path A -->
<rect x="{X_PATH_A-UTIL_W/2}" y="{Y_UTILITY}" width="{UTIL_W}" height="{UTIL_H}" fill="#87CEEB" stroke="black" stroke-width="2"/>
<text x="{X_PATH_A}" y="{Y_UTILITY+35}" class="equipment-label" text-anchor="middle">HPP SOURCE</text>
<text x="{X_PATH_A}" y="{Y_UTILITY+55}" class="rating" text-anchor="middle">400V | 3.7 MW</text>

<!-- Line from HPP → HPP Step-Up TX -->
<line x1="{X_PATH_A}" y1="{Y_UTILITY+UTIL_H}" x2="{X_PATH_A}" y2="{Y_UTILITY+UTIL_H+50}" class="power-line"/>
<use href="#breaker-closed" x="{X_PATH_A}" y="{Y_UTILITY+UTIL_H+30}"/>
<text x="{X_PATH_A+25}" y="{Y_UTILITY+UTIL_H+30}" class="breaker-id" text-anchor="start">CB-HPP</text>
<text x="{X_PATH_A+25}" y="{Y_UTILITY+UTIL_H+45}" class="breaker-nc" text-anchor="start">N.C.</text>

<!-- HPP Step-Up Transformer (400V → 10kV) -->
<line x1="{X_PATH_A}" y1="{Y_UTILITY+UTIL_H+50}" x2="{X_PATH_A}" y2="{Y_UTILITY+UTIL_H+100}" class="power-line"/>
<use href="#transformer" x="{X_PATH_A}" y="{Y_UTILITY+UTIL_H+130}"/>
<rect x="{X_PATH_A-XFMR_BOX_W/2}" y="{Y_UTILITY+UTIL_H+80}" width="{XFMR_BOX_W}" height="{XFMR_BOX_H}" class="transformer-box"/>
<text x="{X_PATH_A}" y="{Y_UTILITY+UTIL_H+215}" class="equipment-label" text-anchor="middle">HPP-TX</text>
<text x="{X_PATH_A}" y="{Y_UTILITY+UTIL_H+232}" class="rating" text-anchor="middle">3,500 kVA</text>
<text x="{X_PATH_A}" y="{Y_UTILITY+UTIL_H+247}" class="rating" text-anchor="middle">400V/10kV</text>

<!-- Line from HPP-TX → MV-SWBD-A -->
<line x1="{X_PATH_A}" y1="{Y_UTILITY+UTIL_H+157}" x2="{X_PATH_A}" y2="{Y_MV_SWBD-50}" class="power-line"/>
<use href="#breaker-closed" x="{X_PATH_A}" y="{Y_MV_SWBD-80}"/>
<text x="{X_PATH_A+25}" y="{Y_MV_SWBD-85}" class="breaker-id" text-anchor="start">CB-U1</text>
<text x="{X_PATH_A+25}" y="{Y_MV_SWBD-70}" class="breaker-nc" text-anchor="start">N.C.</text>

<!-- Grid Utility (10kV) - Path B -->
<rect x="{X_PATH_B-UTIL_W/2}" y="{Y_UTILITY}" width="{UTIL_W}" height="{UTIL_H}" fill="#87CEEB" stroke="black" stroke-width="2"/>
<text x="{X_PATH_B}" y="{Y_UTILITY+35}" class="equipment-label" text-anchor="middle">UTILITY GRID</text>
<text x="{X_PATH_B}" y="{Y_UTILITY+55}" class="rating" text-anchor="middle">10kV | 4.0 MW</text>

<!-- Line from Grid → MV-SWBD-B -->
<line x1="{X_PATH_B}" y1="{Y_UTILITY+UTIL_H}" x2="{X_PATH_B}" y2="{Y_MV_SWBD-50}" class="power-line"/>
<use href="#breaker-closed" x="{X_PATH_B}" y="{Y_UTILITY+UTIL_H+30}"/>
<text x="{X_PATH_B+25}" y="{Y_UTILITY+UTIL_H+30}" class="breaker-id" text-anchor="start">CB-U2</text>
<text x="{X_PATH_B+25}" y="{Y_UTILITY+UTIL_H+45}" class="breaker-nc" text-anchor="start">N.C.</text>

<!-- ===================================================================== -->
<!--                    MV SWITCHBOARDS (10 kV)                            -->
<!-- ===================================================================== -->

<!-- MV-SWBD-A -->
<line x1="{X_PATH_A}" y1="{Y_MV_SWBD-50}" x2="{X_PATH_A}" y2="{Y_MV_SWBD-30}" class="power-line"/>
<line x1="{X_PATH_A}" y1="{Y_MV_SWBD-30}" x2="{X_PATH_A-20}" y2="{Y_MV_SWBD-30}" class="power-line"/>
<line x1="{X_PATH_A-20}" y1="{Y_MV_SWBD-30}" x2="{X_PATH_A-20}" y2="{Y_MV_SWBD+12}" class="power-line"/>
<use href="#breaker-closed" x="{X_PATH_A-20}" y="{Y_MV_SWBD}"/>
<text x="{X_PATH_A+5}" y="{Y_MV_SWBD-5}" class="breaker-id" text-anchor="start">VCB-M1</text>
<text x="{X_PATH_A+5}" y="{Y_MV_SWBD+10}" class="breaker-nc" text-anchor="start">N.C.</text>

<rect x="{X_PATH_A-MV_SWBD_W/2}" y="{Y_MV_SWBD+12}" width="{MV_SWBD_W}" height="{MV_SWBD_H}" class="mv-switchboard"/>
<line x1="{X_PATH_A-MV_SWBD_W/2+15}" y1="{Y_MV_SWBD+27}" x2="{X_PATH_A+MV_SWBD_W/2-15}" y2="{Y_MV_SWBD+27}" class="bus"/>
<text x="{X_PATH_A}" y="{Y_MV_SWBD+60}" class="equipment-label" text-anchor="middle">MV-SWBD-A</text>
<text x="{X_PATH_A}" y="{Y_MV_SWBD+80}" class="rating" text-anchor="middle">10 kV | 630A Bus</text>
<text x="{X_PATH_A}" y="{Y_MV_SWBD+97}" class="rating" text-anchor="middle">VCB Lineup</text>

<!-- MV-SWBD-B -->
<line x1="{X_PATH_B}" y1="{Y_MV_SWBD-50}" x2="{X_PATH_B}" y2="{Y_MV_SWBD-30}" class="power-line"/>
<line x1="{X_PATH_B}" y1="{Y_MV_SWBD-30}" x2="{X_PATH_B+20}" y2="{Y_MV_SWBD-30}" class="power-line"/>
<line x1="{X_PATH_B+20}" y1="{Y_MV_SWBD-30}" x2="{X_PATH_B+20}" y2="{Y_MV_SWBD+12}" class="power-line"/>
<use href="#breaker-closed" x="{X_PATH_B+20}" y="{Y_MV_SWBD}"/>
<text x="{X_PATH_B+45}" y="{Y_MV_SWBD-5}" class="breaker-id" text-anchor="start">VCB-M2</text>
<text x="{X_PATH_B+45}" y="{Y_MV_SWBD+10}" class="breaker-nc" text-anchor="start">N.C.</text>

<rect x="{X_PATH_B-MV_SWBD_W/2}" y="{Y_MV_SWBD+12}" width="{MV_SWBD_W}" height="{MV_SWBD_H}" class="mv-switchboard"/>
<line x1="{X_PATH_B-MV_SWBD_W/2+15}" y1="{Y_MV_SWBD+27}" x2="{X_PATH_B+MV_SWBD_W/2-15}" y2="{Y_MV_SWBD+27}" class="bus"/>
<text x="{X_PATH_B}" y="{Y_MV_SWBD+60}" class="equipment-label" text-anchor="middle">MV-SWBD-B</text>
<text x="{X_PATH_B}" y="{Y_MV_SWBD+80}" class="rating" text-anchor="middle">10 kV | 630A Bus</text>
<text x="{X_PATH_B}" y="{Y_MV_SWBD+97}" class="rating" text-anchor="middle">VCB Lineup</text>

<!-- MV Tie Breaker (Normally Open) -->
<line x1="{X_PATH_A+MV_SWBD_W/2}" y1="{Y_MV_SWBD+70}" x2="{X_CENTER-40}" y2="{Y_MV_SWBD+70}" class="power-line" stroke-dasharray="10,5"/>
<line x1="{X_CENTER+40}" y1="{Y_MV_SWBD+70}" x2="{X_PATH_B-MV_SWBD_W/2}" y2="{Y_MV_SWBD+70}" class="power-line" stroke-dasharray="10,5"/>
<use href="#breaker-open" x="{X_CENTER}" y="{Y_MV_SWBD+70}"/>
<text x="{X_CENTER}" y="{Y_MV_SWBD+50}" class="breaker-id" text-anchor="middle">52-TIE-MV</text>
<text x="{X_CENTER}" y="{Y_MV_SWBD+100}" class="breaker-no" text-anchor="middle">N.O.</text>

<!-- ===================================================================== -->
<!--              STEP-DOWN TRANSFORMERS (10 kV → 400V)                   -->
<!-- ===================================================================== -->

<!-- XFMR-A from MV-SWBD-A -->
<line x1="{X_PATH_A}" y1="{Y_MV_SWBD+MV_SWBD_H+12}" x2="{X_PATH_A}" y2="{Y_XFMR-120}" class="power-line"/>
<line x1="{X_PATH_A}" y1="{Y_XFMR-120}" x2="{X_PATH_A+30}" y2="{Y_XFMR-120}" class="power-line"/>
<line x1="{X_PATH_A+30}" y1="{Y_XFMR-120}" x2="{X_PATH_A+30}" y2="{Y_XFMR-90}" class="power-line"/>
<use href="#breaker-closed" x="{X_PATH_A+30}" y="{Y_XFMR-110}"/>
<text x="{X_PATH_A+55}" y="{Y_XFMR-115}" class="breaker-id" text-anchor="start">CB-M1</text>
<text x="{X_PATH_A+55}" y="{Y_XFMR-100}" class="breaker-nc" text-anchor="start">N.C.</text>

<line x1="{X_PATH_A+30}" y1="{Y_XFMR-90}" x2="{X_PATH_A+30}" y2="{Y_XFMR-50}" class="power-line"/>
<line x1="{X_PATH_A+30}" y1="{Y_XFMR-50}" x2="{X_PATH_A+22}" y2="{Y_XFMR-50}" class="power-line"/>
<line x1="{X_PATH_A+22}" y1="{Y_XFMR-50}" x2="{X_PATH_A+22}" y2="{Y_XFMR-20}" class="power-line"/>

<use href="#transformer" x="{X_PATH_A+30}" y="{Y_XFMR}"/>
<rect x="{X_PATH_A+30-XFMR_BOX_W/2}" y="{Y_XFMR-XFMR_BOX_H/2}" width="{XFMR_BOX_W}" height="{XFMR_BOX_H}" class="transformer-box"/>
<text x="{X_PATH_A+30}" y="{Y_XFMR+75}" class="equipment-label" text-anchor="middle">XFMR-A</text>
<text x="{X_PATH_A+30}" y="{Y_XFMR+92}" class="rating" text-anchor="middle">3,500 kVA</text>
<text x="{X_PATH_A+30}" y="{Y_XFMR+107}" class="rating" text-anchor="middle">10kV/400V</text>

<line x1="{X_PATH_A+38}" y1="{Y_XFMR+20}" x2="{X_PATH_A+38}" y2="{Y_XFMR+50}" class="power-line"/>
<use href="#breaker-closed" x="{X_PATH_A+38}" y="{Y_XFMR+80}"/>
<text x="{X_PATH_A+63}" y="{Y_XFMR+75}" class="breaker-id" text-anchor="start">ACB-M1</text>
<text x="{X_PATH_A+63}" y="{Y_XFMR+90}" class="breaker-nc" text-anchor="start">N.C.</text>
<text x="{X_PATH_A+140}" y="{Y_XFMR+80}" class="rating" text-anchor="start">6,300A/5,000A</text>

<!-- XFMR-B from MV-SWBD-B -->
<line x1="{X_PATH_B}" y1="{Y_MV_SWBD+MV_SWBD_H+12}" x2="{X_PATH_B}" y2="{Y_XFMR-120}" class="power-line"/>
<line x1="{X_PATH_B}" y1="{Y_XFMR-120}" x2="{X_PATH_B-30}" y2="{Y_XFMR-120}" class="power-line"/>
<line x1="{X_PATH_B-30}" y1="{Y_XFMR-120}" x2="{X_PATH_B-30}" y2="{Y_XFMR-90}" class="power-line"/>
<use href="#breaker-closed" x="{X_PATH_B-30}" y="{Y_XFMR-110}"/>
<text x="{X_PATH_B-5}" y="{Y_XFMR-115}" class="breaker-id" text-anchor="start">CB-M2</text>
<text x="{X_PATH_B-5}" y="{Y_XFMR-100}" class="breaker-nc" text-anchor="start">N.C.</text>

<line x1="{X_PATH_B-30}" y1="{Y_XFMR-90}" x2="{X_PATH_B-30}" y2="{Y_XFMR-50}" class="power-line"/>
<line x1="{X_PATH_B-30}" y1="{Y_XFMR-50}" x2="{X_PATH_B-22}" y2="{Y_XFMR-50}" class="power-line"/>
<line x1="{X_PATH_B-22}" y1="{Y_XFMR-50}" x2="{X_PATH_B-22}" y2="{Y_XFMR-20}" class="power-line"/>

<use href="#transformer" x="{X_PATH_B-30}" y="{Y_XFMR}"/>
<rect x="{X_PATH_B-30-XFMR_BOX_W/2}" y="{Y_XFMR-XFMR_BOX_H/2}" width="{XFMR_BOX_W}" height="{XFMR_BOX_H}" class="transformer-box"/>
<text x="{X_PATH_B-30}" y="{Y_XFMR+75}" class="equipment-label" text-anchor="middle">XFMR-B</text>
<text x="{X_PATH_B-30}" y="{Y_XFMR+92}" class="rating" text-anchor="middle">3,500 kVA</text>
<text x="{X_PATH_B-30}" y="{Y_XFMR+107}" class="rating" text-anchor="middle">10kV/400V</text>

<line x1="{X_PATH_B-38}" y1="{Y_XFMR+20}" x2="{X_PATH_B-38}" y2="{Y_XFMR+50}" class="power-line"/>
<use href="#breaker-closed" x="{X_PATH_B-38}" y="{Y_XFMR+80}"/>
<text x="{X_PATH_B-13}" y="{Y_XFMR+75}" class="breaker-id" text-anchor="start">ACB-M2</text>
<text x="{X_PATH_B-13}" y="{Y_XFMR+90}" class="breaker-nc" text-anchor="start">N.C.</text>
<text x="{X_PATH_B+60}" y="{Y_XFMR+80}" class="rating" text-anchor="start">6,300A/5,000A</text>

<!-- ===================================================================== -->
<!--                    LV SWITCHBOARDS (400V)                             -->
<!-- ===================================================================== -->

<!-- LV-SWBD-A -->
<line x1="{X_PATH_A+38}" y1="{Y_XFMR+92}" x2="{X_PATH_A+38}" y2="{Y_LV_SWBD-50}" class="power-line"/>
<line x1="{X_PATH_A+38}" y1="{Y_LV_SWBD-50}" x2="{X_PATH_A+20}" y2="{Y_LV_SWBD-50}" class="power-line"/>
<line x1="{X_PATH_A+20}" y1="{Y_LV_SWBD-50}" x2="{X_PATH_A+20}" y2="{Y_LV_SWBD+12}" class="power-line"/>
<use href="#breaker-closed" x="{X_PATH_A+20}" y="{Y_LV_SWBD-20}"/>
<text x="{X_PATH_A+45}" y="{Y_LV_SWBD-25}" class="breaker-id" text-anchor="start">CB-L1</text>
<text x="{X_PATH_A+45}" y="{Y_LV_SWBD-10}" class="breaker-nc" text-anchor="start">N.C.</text>

<rect x="{X_PATH_A-LV_SWBD_W/2}" y="{Y_LV_SWBD+12}" width="{LV_SWBD_W}" height="{LV_SWBD_H}" class="lv-switchboard"/>
<line x1="{X_PATH_A-LV_SWBD_W/2+15}" y1="{Y_LV_SWBD+27}" x2="{X_PATH_A+LV_SWBD_W/2-15}" y2="{Y_LV_SWBD+27}" class="bus"/>
<text x="{X_PATH_A}" y="{Y_LV_SWBD+55}" class="equipment-label" text-anchor="middle">SWBD-A</text>
<text x="{X_PATH_A}" y="{Y_LV_SWBD+75}" class="rating" text-anchor="middle">400V | 2,500A Bus</text>
<text x="{X_PATH_A}" y="{Y_LV_SWBD+90}" class="rating" text-anchor="middle">Normal: 1,039 kW</text>

<!-- LV-SWBD-B -->
<line x1="{X_PATH_B-38}" y1="{Y_XFMR+92}" x2="{X_PATH_B-38}" y2="{Y_LV_SWBD-50}" class="power-line"/>
<line x1="{X_PATH_B-38}" y1="{Y_LV_SWBD-50}" x2="{X_PATH_B-20}" y2="{Y_LV_SWBD-50}" class="power-line"/>
<line x1="{X_PATH_B-20}" y1="{Y_LV_SWBD-50}" x2="{X_PATH_B-20}" y2="{Y_LV_SWBD+12}" class="power-line"/>
<use href="#breaker-closed" x="{X_PATH_B-20}" y="{Y_LV_SWBD-20}"/>
<text x="{X_PATH_B+5}" y="{Y_LV_SWBD-25}" class="breaker-id" text-anchor="start">CB-L2</text>
<text x="{X_PATH_B+5}" y="{Y_LV_SWBD-10}" class="breaker-nc" text-anchor="start">N.C.</text>

<rect x="{X_PATH_B-LV_SWBD_W/2}" y="{Y_LV_SWBD+12}" width="{LV_SWBD_W}" height="{LV_SWBD_H}" class="lv-switchboard"/>
<line x1="{X_PATH_B-LV_SWBD_W/2+15}" y1="{Y_LV_SWBD+27}" x2="{X_PATH_B+LV_SWBD_W/2-15}" y2="{Y_LV_SWBD+27}" class="bus"/>
<text x="{X_PATH_B}" y="{Y_LV_SWBD+55}" class="equipment-label" text-anchor="middle">SWBD-B</text>
<text x="{X_PATH_B}" y="{Y_LV_SWBD+75}" class="rating" text-anchor="middle">400V | 2,500A Bus</text>
<text x="{X_PATH_B}" y="{Y_LV_SWBD+90}" class="rating" text-anchor="middle">Normal: 1,096 kW</text>

<!-- LV Tie Breaker (Normally Open) -->
<line x1="{X_PATH_A+LV_SWBD_W/2}" y1="{Y_LV_SWBD+60}" x2="{X_CENTER-40}" y2="{Y_LV_SWBD+60}" class="power-line" stroke-dasharray="10,5"/>
<line x1="{X_CENTER+40}" y1="{Y_LV_SWBD+60}" x2="{X_PATH_B-LV_SWBD_W/2}" y2="{Y_LV_SWBD+60}" class="power-line" stroke-dasharray="10,5"/>
<use href="#breaker-open" x="{X_CENTER}" y="{Y_LV_SWBD+60}"/>
<text x="{X_CENTER}" y="{Y_LV_SWBD+20}" class="breaker-id" text-anchor="middle">52-TIE</text>
<text x="{X_CENTER}" y="{Y_LV_SWBD+35}" class="breaker-no" text-anchor="middle">N.O.</text>
<text x="{X_CENTER}" y="{Y_LV_SWBD+90}" class="rating" text-anchor="middle">6,300A/5,000A</text>

<!-- ===================================================================== -->
<!--                DRUPS (SIDE BRANCHES FROM LV-SWBD)                     -->
<!-- ===================================================================== -->

<!-- DRUPS-1 Branch from SWBD-A (LEFT side) -->
<line x1="{X_PATH_A-LV_SWBD_W/2}" y1="{Y_LV_SWBD+40}" x2="{X_PATH_A-LV_SWBD_W/2-180}" y2="{Y_LV_SWBD+40}" class="power-line"/>
<use href="#breaker-closed" x="{X_PATH_A-LV_SWBD_W/2-80}" y="{Y_LV_SWBD+40}"/>
<text x="{X_PATH_A-LV_SWBD_W/2-55}" y="{Y_LV_SWBD+35}" class="breaker-id" text-anchor="start">ACB-DRUPS1</text>
<text x="{X_PATH_A-LV_SWBD_W/2-55}" y="{Y_LV_SWBD+50}" class="breaker-nc" text-anchor="start">N.C.</text>

<rect x="{X_PATH_A-LV_SWBD_W/2-180-DRUPS_W/2}" y="{Y_DRUPS-DRUPS_H/2}" width="{DRUPS_W}" height="{DRUPS_H}" class="generator-box"/>
<text x="{X_PATH_A-LV_SWBD_W/2-180}" y="{Y_DRUPS-15}" class="equipment-label" text-anchor="middle">DRUPS-1</text>
<text x="{X_PATH_A-LV_SWBD_W/2-180}" y="{Y_DRUPS+2}" class="rating" text-anchor="middle">MTU KP7</text>
<text x="{X_PATH_A-LV_SWBD_W/2-180}" y="{Y_DRUPS+17}" class="rating" text-anchor="middle">2,750 kVA</text>
<text x="{X_PATH_A-LV_SWBD_W/2-180}" y="{Y_DRUPS+32}" class="rating" text-anchor="middle">2,200 kW</text>

<!-- DRUPS-2 Branch from SWBD-B (RIGHT side) -->
<line x1="{X_PATH_B+LV_SWBD_W/2}" y1="{Y_LV_SWBD+40}" x2="{X_PATH_B+LV_SWBD_W/2+180}" y2="{Y_LV_SWBD+40}" class="power-line"/>
<use href="#breaker-closed" x="{X_PATH_B+LV_SWBD_W/2+80}" y="{Y_LV_SWBD+40}"/>
<text x="{X_PATH_B+LV_SWBD_W/2+105}" y="{Y_LV_SWBD+35}" class="breaker-id" text-anchor="start">ACB-DRUPS2</text>
<text x="{X_PATH_B+LV_SWBD_W/2+105}" y="{Y_LV_SWBD+50}" class="breaker-nc" text-anchor="start">N.C.</text>

<rect x="{X_PATH_B+LV_SWBD_W/2+180-DRUPS_W/2}" y="{Y_DRUPS-DRUPS_H/2}" width="{DRUPS_W}" height="{DRUPS_H}" class="generator-box"/>
<text x="{X_PATH_B+LV_SWBD_W/2+180}" y="{Y_DRUPS-15}" class="equipment-label" text-anchor="middle">DRUPS-2</text>
<text x="{X_PATH_B+LV_SWBD_W/2+180}" y="{Y_DRUPS+2}" class="rating" text-anchor="middle">MTU KP7</text>
<text x="{X_PATH_B+LV_SWBD_W/2+180}" y="{Y_DRUPS+17}" class="rating" text-anchor="middle">2,750 kVA</text>
<text x="{X_PATH_B+LV_SWBD_W/2+180}" y="{Y_DRUPS+32}" class="rating" text-anchor="middle">2,200 kW</text>

<!-- ===================================================================== -->
<!--                    DOWNSTREAM DISTRIBUTION                            -->
<!-- ===================================================================== -->

<!-- Distribution from SWBD-A -->
<line x1="{X_PATH_A-50}" y1="{Y_LV_SWBD+LV_SWBD_H+12}" x2="{X_PATH_A-50}" y2="{Y_DIST-80}" class="power-line"/>
<use href="#breaker-closed" x="{X_PATH_A-50}" y="{Y_DIST-50}"/>
<text x="{X_PATH_A-25}" y="{Y_DIST-55}" class="breaker-id" text-anchor="start">CB-IT-A</text>
<text x="{X_PATH_A-25}" y="{Y_DIST-40}" class="breaker-nc" text-anchor="start">N.C.</text>

<rect x="{X_PATH_A-50-DIST_W/2}" y="{Y_DIST-80+BREAKER_H+12}" width="{DIST_W}" height="{DIST_H}" class="dist-panel"/>
<text x="{X_PATH_A-50}" y="{Y_DIST-35}" class="equipment-label" text-anchor="middle">A-IT-1</text>
<text x="{X_PATH_A-50}" y="{Y_DIST-20}" class="rating" text-anchor="middle">2,500A MCCB</text>
<text x="{X_PATH_A-50}" y="{Y_DIST-7}" class="rating" text-anchor="middle">735 kW</text>

<line x1="{X_PATH_A+50}" y1="{Y_LV_SWBD+LV_SWBD_H+12}" x2="{X_PATH_A+50}" y2="{Y_DIST-80}" class="power-line"/>
<use href="#breaker-closed" x="{X_PATH_A+50}" y="{Y_DIST-50}"/>
<text x="{X_PATH_A+75}" y="{Y_DIST-55}" class="breaker-id" text-anchor="start">CB-COOL-A</text>
<text x="{X_PATH_A+75}" y="{Y_DIST-40}" class="breaker-nc" text-anchor="start">N.C.</text>

<rect x="{X_PATH_A+50-DIST_W/2}" y="{Y_DIST-80+BREAKER_H+12}" width="{DIST_W}" height="{DIST_H}" class="dist-panel"/>
<text x="{X_PATH_A+50}" y="{Y_DIST-35}" class="equipment-label" text-anchor="middle">A-COOL-1</text>
<text x="{X_PATH_A+50}" y="{Y_DIST-20}" class="rating" text-anchor="middle">3,200A MCCB</text>
<text x="{X_PATH_A+50}" y="{Y_DIST-7}" class="rating" text-anchor="middle">304 kW</text>

<!-- Distribution from SWBD-B -->
<line x1="{X_PATH_B-50}" y1="{Y_LV_SWBD+LV_SWBD_H+12}" x2="{X_PATH_B-50}" y2="{Y_DIST-80}" class="power-line"/>
<use href="#breaker-closed" x="{X_PATH_B-50}" y="{Y_DIST-50}"/>
<text x="{X_PATH_B-25}" y="{Y_DIST-55}" class="breaker-id" text-anchor="start">CB-IT-B</text>
<text x="{X_PATH_B-25}" y="{Y_DIST-40}" class="breaker-nc" text-anchor="start">N.C.</text>

<rect x="{X_PATH_B-50-DIST_W/2}" y="{Y_DIST-80+BREAKER_H+12}" width="{DIST_W}" height="{DIST_H}" class="dist-panel"/>
<text x="{X_PATH_B-50}" y="{Y_DIST-35}" class="equipment-label" text-anchor="middle">B-IT-1</text>
<text x="{X_PATH_B-50}" y="{Y_DIST-20}" class="rating" text-anchor="middle">2,500A MCCB</text>
<text x="{X_PATH_B-50}" y="{Y_DIST-7}" class="rating" text-anchor="middle">735 kW</text>

<line x1="{X_PATH_B+50}" y1="{Y_LV_SWBD+LV_SWBD_H+12}" x2="{X_PATH_B+50}" y2="{Y_DIST-80}" class="power-line"/>
<use href="#breaker-closed" x="{X_PATH_B+50}" y="{Y_DIST-50}"/>
<text x="{X_PATH_B+75}" y="{Y_DIST-55}" class="breaker-id" text-anchor="start">CB-COOL-B</text>
<text x="{X_PATH_B+75}" y="{Y_DIST-40}" class="breaker-nc" text-anchor="start">N.C.</text>

<rect x="{X_PATH_B+50-DIST_W/2}" y="{Y_DIST-80+BREAKER_H+12}" width="{DIST_W}" height="{DIST_H}" class="dist-panel"/>
<text x="{X_PATH_B+50}" y="{Y_DIST-35}" class="equipment-label" text-anchor="middle">B-COOL-1</text>
<text x="{X_PATH_B+50}" y="{Y_DIST-20}" class="rating" text-anchor="middle">3,200A MCCB</text>
<text x="{X_PATH_B+50}" y="{Y_DIST-7}" class="rating" text-anchor="middle">361 kW</text>

<!-- ===================================================================== -->
<!--                         IT EQUIPMENT                                  -->
<!-- ===================================================================== -->

<!-- IT Equipment Box -->
<rect x="{X_CENTER-250}" y="{Y_IT_LOADS-40}" width="500" height="80" fill="#E0F2F1" stroke="black" stroke-width="2"/>
<text x="{X_CENTER}" y="{Y_IT_LOADS-5}" class="equipment-label" text-anchor="middle">IT EQUIPMENT</text>
<text x="{X_CENTER}" y="{Y_IT_LOADS+15}" class="rating" text-anchor="middle">1,467 kW (1.47 MW) | Dual-Corded (A+B)</text>

<!-- Connections from distribution to IT -->
<line x1="{X_PATH_A-50}" y1="{Y_DIST}" x2="{X_PATH_A-50}" y2="{Y_IT_LOADS-100}" class="power-line"/>
<line x1="{X_PATH_A-50}" y1="{Y_IT_LOADS-100}" x2="{X_CENTER-250}" y2="{Y_IT_LOADS-100}" class="power-line"/>
<line x1="{X_CENTER-250}" y1="{Y_IT_LOADS-100}" x2="{X_CENTER-250}" y2="{Y_IT_LOADS-40}" class="power-line"/>

<line x1="{X_PATH_B-50}" y1="{Y_DIST}" x2="{X_PATH_B-50}" y2="{Y_IT_LOADS-100}" class="power-line"/>
<line x1="{X_PATH_B-50}" y1="{Y_IT_LOADS-100}" x2="{X_CENTER+250}" y2="{Y_IT_LOADS-100}" class="power-line"/>
<line x1="{X_CENTER+250}" y1="{Y_IT_LOADS-100}" x2="{X_CENTER+250}" y2="{Y_IT_LOADS-40}" class="power-line"/>

<text x="{X_PATH_A-100}" y="{Y_IT_LOADS-110}" class="rating">Path A</text>
<text x="{X_PATH_B+50}" y="{Y_IT_LOADS-110}" class="rating">Path B</text>

<!-- ===================================================================== -->
<!--                              LEGEND                                   -->
<!-- ===================================================================== -->

<rect x="50" y="{Y_IT_LOADS+100}" width="700" height="200" fill="#F5F5F5" stroke="black" stroke-width="1"/>
<text x="70" y="{Y_IT_LOADS+130}" class="subtitle">DESIGN NOTES:</text>
<text x="70" y="{Y_IT_LOADS+150}" class="rating">• Tier III: 2N DRUPS backup, N+1 mechanical</text>
<text x="70" y="{Y_IT_LOADS+168}" class="rating">• MTM topology at MV (10kV) and LV (400V)</text>
<text x="70" y="{Y_IT_LOADS+186}" class="rating">• Dual sources: HPP (3.7MW) + Grid (4.0MW)</text>
<text x="70" y="{Y_IT_LOADS+204}" class="rating">• HPP step-up: 400V → 10kV (3,500 kVA)</text>
<text x="70" y="{Y_IT_LOADS+222}" class="rating">• Step-down transformers: 10kV → 400V (2 × 3,500 kVA)</text>
<text x="70" y="{Y_IT_LOADS+240}" class="rating">• DRUPS: 2 × MTU KP7 (2,750 kVA each)</text>
<text x="70" y="{Y_IT_LOADS+258}" class="rating">• 52-TIE breakers: N.O. (main-tie-main failover)</text>
<text x="70" y="{Y_IT_LOADS+276}" class="rating">• IT loads: Dual-corded (Path A + Path B)</text>

<rect x="800" y="{Y_IT_LOADS+100}" width="700" height="200" fill="#F5F5F5" stroke="black" stroke-width="1"/>
<text x="820" y="{Y_IT_LOADS+130}" class="subtitle">BREAKER LEGEND:</text>
<use href="#breaker-closed" x="840" y="{Y_IT_LOADS+160}"/>
<text x="870" y="{Y_IT_LOADS+165}" class="rating">N.C. (Normally Closed - RED label)</text>
<use href="#breaker-open" x="840" y="{Y_IT_LOADS+200}"/>
<text x="870" y="{Y_IT_LOADS+205}" class="rating">N.O. (Normally Open - Gray label)</text>
<text x="820" y="{Y_IT_LOADS+240}" class="rating">All breakers shown in normal operating state</text>
<text x="820" y="{Y_IT_LOADS+258}" class="rating">Standards: IEC 60364, IEEE 315/IEC 60617</text>
<text x="820" y="{Y_IT_LOADS+276}" class="rating">Location: Tbilisi, Georgia</text>

</svg>'''

# Write output
output_file = 'gge_10kv_sld.svg'
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(svg)

print(f"[SUCCESS] GGE SLD v1.4 generated: {output_file}")
print(f"[INFO] File size: {len(svg):,} bytes")
print(f"[INFO] Canvas: {WIDTH} x {HEIGHT} px")
print(f"[INFO] Layout: Reference-based (test_standards_output.svg)")
print()
print("[FEATURES]")
print("  - Side-by-side A/B paths (HPP + Grid)")
print("  - DRUPS as horizontal side branches from LV-SWBD")
print("  - All breakers with proper boundaries")
print("  - MV and LV tie breakers (N.O.)")
print("  - GGE naming convention")
