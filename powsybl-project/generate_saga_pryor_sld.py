#!/usr/bin/env python3
"""
Saga Pryor Data Center - Single-Line Diagram Generator
PACHYDERM GLOBAL - 24 MW IT Load
13.8 kV Dual-Ring MV Distribution with Self-Healing Topology
"""

from datetime import datetime
from sld_standards import get_svg_style_section, get_svg_symbols

# Canvas settings - larger for complex topology
WIDTH = 3200
HEIGHT = 4000

# Layout positions
X_CENTER = WIDTH / 2
X_RING_A = 800
X_RING_B = 2400
X_OFFSET = 600

# Y-coordinates
Y_UTILITY = 250
Y_SUBSTATION = 500
Y_RING_TOP = 850
Y_RING_MID = 1400
Y_RING_BOTTOM = 1950
Y_GEN_SOLAR = 2300
Y_LV_SWBD = 2750
Y_UPS = 3150
Y_IT = 3500

# Equipment dimensions
SUB_W, SUB_H = 120, 100
RMU_W, RMU_H = 80, 60
XFMR_W, XFMR_H = 90, 80
GEN_W, GEN_H = 100, 70
SWBD_W, SWBD_H = 180, 100
UPS_W, UPS_H = 150, 80

BREAKER_H_HALF = 12

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
        .ring-a-line { stroke: #E74C3C; stroke-width: 4; fill: none; }
        .ring-b-line { stroke: #3498DB; stroke-width: 4; fill: none; }
    </style>
"""

svg = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{WIDTH}" height="{HEIGHT}" xmlns="http://www.w3.org/2000/svg">

{get_svg_symbols()}
{get_svg_style_section()}
{breaker_css}

<!-- ===================================================================== -->
<!--                              TITLE BLOCK                              -->
<!-- ===================================================================== -->
<rect x="50" y="30" width="{WIDTH-250}" height="100" fill="white" stroke="black" stroke-width="2"/>
<text x="{X_CENTER}" y="70" class="title" text-anchor="middle">Saga Pryor Data Center - Electrical Single-Line Diagram</text>
<text x="{X_CENTER}" y="95" class="equipment-label" text-anchor="middle">13.8 kV Dual-Ring MV Distribution | N+1 Architecture | Tier III</text>
<text x="{X_CENTER}" y="115" class="rating" text-anchor="middle">24 MW IT Load | 30 MW Facility | PACHYDERM GLOBAL | Pryor, OK</text>

<rect x="{WIDTH-190}" y="30" width="140" height="100" fill="white" stroke="black" stroke-width="2"/>
<text x="{WIDTH-180}" y="60" class="rating">Date: {date_str}</text>
<text x="{WIDTH-180}" y="77" class="timestamp">Time: {time_str}</text>
<text x="{WIDTH-180}" y="97" class="rating">Rev: 01</text>
<text x="{WIDTH-180}" y="114" class="rating">Phase 4</text>

<!-- ===================================================================== -->
<!--                          UTILITY SERVICE                              -->
<!-- ===================================================================== -->

<!-- Utility Grid -->
<rect x="{X_CENTER-150}" y="{Y_UTILITY}" width="300" height="80" fill="#87CEEB" stroke="black" stroke-width="2"/>
<text x="{X_CENTER}" y="{Y_UTILITY+35}" class="equipment-label" text-anchor="middle">UTILITY GRID</text>
<text x="{X_CENTER}" y="{Y_UTILITY+55}" class="rating" text-anchor="middle">Kamo Power Electric Co-op</text>
<text x="{X_CENTER}" y="{Y_UTILITY+70}" class="rating" text-anchor="middle">345 kV or 161 kV</text>

<!-- Lines to substation transformers -->
<line x1="{X_CENTER-80}" y1="{Y_UTILITY+80}" x2="{X_CENTER-80}" y2="{Y_SUBSTATION-50}" class="power-line"/>
<line x1="{X_CENTER+80}" y1="{Y_UTILITY+80}" x2="{X_CENTER+80}" y2="{Y_SUBSTATION-50}" class="power-line"/>

<!-- ===================================================================== -->
<!--                      SUBSTATION TRANSFORMERS                          -->
<!-- ===================================================================== -->

<!-- XFMR-SUB-A -->
<use href="#transformer" x="{X_CENTER-80}" y="{Y_SUBSTATION}"/>
<rect x="{X_CENTER-80-SUB_W/2}" y="{Y_SUBSTATION-SUB_H/2}" width="{SUB_W}" height="{SUB_H}" class="transformer-box"/>
<text x="{X_CENTER-80}" y="{Y_SUBSTATION+70}" class="equipment-label" text-anchor="middle">XFMR-SUB-A</text>
<text x="{X_CENTER-80}" y="{Y_SUBSTATION+85}" class="rating" text-anchor="middle">35 MVA</text>
<text x="{X_CENTER-80}" y="{Y_SUBSTATION+100}" class="rating" text-anchor="middle">345kV/13.8kV</text>

<!-- XFMR-SUB-B -->
<use href="#transformer" x="{X_CENTER+80}" y="{Y_SUBSTATION}"/>
<rect x="{X_CENTER+80-SUB_W/2}" y="{Y_SUBSTATION-SUB_H/2}" width="{SUB_W}" height="{SUB_H}" class="transformer-box"/>
<text x="{X_CENTER+80}" y="{Y_SUBSTATION+70}" class="equipment-label" text-anchor="middle">XFMR-SUB-B</text>
<text x="{X_CENTER+80}" y="{Y_SUBSTATION+85}" class="rating" text-anchor="middle">35 MVA</text>
<text x="{X_CENTER+80}" y="{Y_SUBSTATION+100}" class="rating" text-anchor="middle">345kV/13.8kV</text>

<!-- Lines to dual-ring -->
<line x1="{X_CENTER-88}" y1="{Y_SUBSTATION+20}" x2="{X_CENTER-88}" y2="{Y_SUBSTATION+150}" class="power-line"/>
<line x1="{X_CENTER-88}" y1="{Y_SUBSTATION+150}" x2="{X_RING_A}" y2="{Y_SUBSTATION+150}" class="power-line"/>
<line x1="{X_RING_A}" y1="{Y_SUBSTATION+150}" x2="{X_RING_A}" y2="{Y_RING_TOP-30}" class="power-line"/>

<line x1="{X_CENTER+88}" y1="{Y_SUBSTATION+20}" x2="{X_CENTER+88}" y2="{Y_SUBSTATION+150}" class="power-line"/>
<line x1="{X_CENTER+88}" y1="{Y_SUBSTATION+150}" x2="{X_RING_B}" y2="{Y_SUBSTATION+150}" class="power-line"/>
<line x1="{X_RING_B}" y1="{Y_SUBSTATION+150}" x2="{X_RING_B}" y2="{Y_RING_TOP-30}" class="power-line"/>

<!-- ===================================================================== -->
<!--                    13.8 KV DUAL-RING DISTRIBUTION                     -->
<!-- ===================================================================== -->

<!-- RING A (RED) -->
<!-- RMU-1A -->
<rect x="{X_RING_A-RMU_W/2}" y="{Y_RING_TOP-RMU_H/2}" width="{RMU_W}" height="{RMU_H}" class="rmu-box"/>
<text x="{X_RING_A}" y="{Y_RING_TOP-5}" class="equipment-label" text-anchor="middle">RMU-1A</text>
<text x="{X_RING_A}" y="{Y_RING_TOP+10}" class="rating" text-anchor="middle">13.8kV</text>
<text x="{X_RING_A}" y="{Y_RING_TOP+23}" class="rating" text-anchor="middle">630A</text>

<!-- Ring A vertical segments -->
<line x1="{X_RING_A}" y1="{Y_RING_TOP+RMU_H/2}" x2="{X_RING_A}" y2="{Y_RING_MID-RMU_H/2-100}" class="ring-a-line"/>
<use href="#transformer" x="{X_RING_A}" y="{Y_RING_MID-150}"/>
<text x="{X_RING_A+60}" y="{Y_RING_MID-150}" class="rating" text-anchor="start">XFMR-A1</text>
<line x1="{X_RING_A}" y1="{Y_RING_MID-RMU_H/2-100+40}" x2="{X_RING_A}" y2="{Y_RING_MID-RMU_H/2}" class="ring-a-line"/>

<!-- RMU-3A -->
<rect x="{X_RING_A-RMU_W/2}" y="{Y_RING_MID-RMU_H/2}" width="{RMU_W}" height="{RMU_H}" class="rmu-box"/>
<text x="{X_RING_A}" y="{Y_RING_MID-5}" class="equipment-label" text-anchor="middle">RMU-3A</text>
<text x="{X_RING_A}" y="{Y_RING_MID+10}" class="rating" text-anchor="middle">13.8kV</text>

<line x1="{X_RING_A}" y1="{Y_RING_MID+RMU_H/2}" x2="{X_RING_A}" y2="{Y_RING_BOTTOM-RMU_H/2-100}" class="ring-a-line"/>
<use href="#transformer" x="{X_RING_A}" y="{Y_RING_BOTTOM-150}"/>
<text x="{X_RING_A+60}" y="{Y_RING_BOTTOM-150}" class="rating" text-anchor="start">XFMR-A3</text>
<line x1="{X_RING_A}" y1="{Y_RING_BOTTOM-RMU_H/2-100+40}" x2="{X_RING_A}" y2="{Y_RING_BOTTOM-RMU_H/2}" class="ring-a-line"/>

<!-- Horizontal ring connections -->
<line x1="{X_RING_A+RMU_W/2}" y1="{Y_RING_TOP}" x2="{X_RING_A+X_OFFSET-RMU_W/2}" y2="{Y_RING_TOP}" class="ring-a-line"/>
<line x1="{X_RING_A+RMU_W/2}" y1="{Y_RING_MID}" x2="{X_RING_A+X_OFFSET-RMU_W/2}" y2="{Y_RING_MID}" class="ring-a-line"/>

<!-- RMU-2A -->
<rect x="{X_RING_A+X_OFFSET-RMU_W/2}" y="{Y_RING_TOP-RMU_H/2}" width="{RMU_W}" height="{RMU_H}" class="rmu-box"/>
<text x="{X_RING_A+X_OFFSET}" y="{Y_RING_TOP-5}" class="equipment-label" text-anchor="middle">RMU-2A</text>
<text x="{X_RING_A+X_OFFSET}" y="{Y_RING_TOP+10}" class="rating" text-anchor="middle">13.8kV</text>

<line x1="{X_RING_A+X_OFFSET}" y1="{Y_RING_TOP+RMU_H/2}" x2="{X_RING_A+X_OFFSET}" y2="{Y_RING_MID-RMU_H/2-100}" class="ring-a-line"/>
<use href="#transformer" x="{X_RING_A+X_OFFSET}" y="{Y_RING_MID-150}"/>
<text x="{X_RING_A+X_OFFSET+60}" y="{Y_RING_MID-150}" class="rating" text-anchor="start">XFMR-A2</text>
<line x1="{X_RING_A+X_OFFSET}" y1="{Y_RING_MID-RMU_H/2-100+40}" x2="{X_RING_A+X_OFFSET}" y2="{Y_RING_MID-RMU_H/2}" class="ring-a-line"/>

<!-- RMU-4A -->
<rect x="{X_RING_A+X_OFFSET-RMU_W/2}" y="{Y_RING_MID-RMU_H/2}" width="{RMU_W}" height="{RMU_H}" class="rmu-box"/>
<text x="{X_RING_A+X_OFFSET}" y="{Y_RING_MID-5}" class="equipment-label" text-anchor="middle">RMU-4A</text>
<text x="{X_RING_A+X_OFFSET}" y="{Y_RING_MID+10}" class="rating" text-anchor="middle">13.8kV</text>

<line x1="{X_RING_A+X_OFFSET}" y1="{Y_RING_MID+RMU_H/2}" x2="{X_RING_A+X_OFFSET}" y2="{Y_RING_BOTTOM-RMU_H/2-100}" class="ring-a-line"/>
<use href="#transformer" x="{X_RING_A+X_OFFSET}" y="{Y_RING_BOTTOM-150}"/>
<text x="{X_RING_A+X_OFFSET+60}" y="{Y_RING_BOTTOM-150}" class="rating" text-anchor="start">XFMR-A4</text>

<!-- RING B (BLUE) - Mirror of Ring A -->
<!-- RMU-1B -->
<rect x="{X_RING_B-RMU_W/2}" y="{Y_RING_TOP-RMU_H/2}" width="{RMU_W}" height="{RMU_H}" class="rmu-box"/>
<text x="{X_RING_B}" y="{Y_RING_TOP-5}" class="equipment-label" text-anchor="middle">RMU-1B</text>
<text x="{X_RING_B}" y="{Y_RING_TOP+10}" class="rating" text-anchor="middle">13.8kV</text>
<text x="{X_RING_B}" y="{Y_RING_TOP+23}" class="rating" text-anchor="middle">630A</text>

<line x1="{X_RING_B}" y1="{Y_RING_TOP+RMU_H/2}" x2="{X_RING_B}" y2="{Y_RING_MID-RMU_H/2-100}" class="ring-b-line"/>
<use href="#transformer" x="{X_RING_B}" y="{Y_RING_MID-150}"/>
<text x="{X_RING_B-60}" y="{Y_RING_MID-150}" class="rating" text-anchor="end">XFMR-B1</text>
<line x1="{X_RING_B}" y1="{Y_RING_MID-RMU_H/2-100+40}" x2="{X_RING_B}" y2="{Y_RING_MID-RMU_H/2}" class="ring-b-line"/>

<!-- RMU-3B -->
<rect x="{X_RING_B-RMU_W/2}" y="{Y_RING_MID-RMU_H/2}" width="{RMU_W}" height="{RMU_H}" class="rmu-box"/>
<text x="{X_RING_B}" y="{Y_RING_MID-5}" class="equipment-label" text-anchor="middle">RMU-3B</text>
<text x="{X_RING_B}" y="{Y_RING_MID+10}" class="rating" text-anchor="middle">13.8kV</text>

<line x1="{X_RING_B}" y1="{Y_RING_MID+RMU_H/2}" x2="{X_RING_B}" y2="{Y_RING_BOTTOM-RMU_H/2-100}" class="ring-b-line"/>
<use href="#transformer" x="{X_RING_B}" y="{Y_RING_BOTTOM-150}"/>
<text x="{X_RING_B-60}" y="{Y_RING_BOTTOM-150}" class="rating" text-anchor="end">XFMR-B3</text>
<line x1="{X_RING_B}" y1="{Y_RING_BOTTOM-RMU_H/2-100+40}" x2="{X_RING_B}" y2="{Y_RING_BOTTOM-RMU_H/2}" class="ring-b-line"/>

<line x1="{X_RING_B-RMU_W/2}" y1="{Y_RING_TOP}" x2="{X_RING_B-X_OFFSET+RMU_W/2}" y2="{Y_RING_TOP}" class="ring-b-line"/>
<line x1="{X_RING_B-RMU_W/2}" y1="{Y_RING_MID}" x2="{X_RING_B-X_OFFSET+RMU_W/2}" y2="{Y_RING_MID}" class="ring-b-line"/>

<!-- RMU-2B -->
<rect x="{X_RING_B-X_OFFSET-RMU_W/2}" y="{Y_RING_TOP-RMU_H/2}" width="{RMU_W}" height="{RMU_H}" class="rmu-box"/>
<text x="{X_RING_B-X_OFFSET}" y="{Y_RING_TOP-5}" class="equipment-label" text-anchor="middle">RMU-2B</text>
<text x="{X_RING_B-X_OFFSET}" y="{Y_RING_TOP+10}" class="rating" text-anchor="middle">13.8kV</text>

<line x1="{X_RING_B-X_OFFSET}" y1="{Y_RING_TOP+RMU_H/2}" x2="{X_RING_B-X_OFFSET}" y2="{Y_RING_MID-RMU_H/2-100}" class="ring-b-line"/>
<use href="#transformer" x="{X_RING_B-X_OFFSET}" y="{Y_RING_MID-150}"/>
<text x="{X_RING_B-X_OFFSET-60}" y="{Y_RING_MID-150}" class="rating" text-anchor="end">XFMR-B2</text>
<line x1="{X_RING_B-X_OFFSET}" y1="{Y_RING_MID-RMU_H/2-100+40}" x2="{X_RING_B-X_OFFSET}" y2="{Y_RING_MID-RMU_H/2}" class="ring-b-line"/>

<!-- RMU-4B -->
<rect x="{X_RING_B-X_OFFSET-RMU_W/2}" y="{Y_RING_MID-RMU_H/2}" width="{RMU_W}" height="{RMU_H}" class="rmu-box"/>
<text x="{X_RING_B-X_OFFSET}" y="{Y_RING_MID-5}" class="equipment-label" text-anchor="middle">RMU-4B</text>
<text x="{X_RING_B-X_OFFSET}" y="{Y_RING_MID+10}" class="rating" text-anchor="middle">13.8kV</text>

<line x1="{X_RING_B-X_OFFSET}" y1="{Y_RING_MID+RMU_H/2}" x2="{X_RING_B-X_OFFSET}" y2="{Y_RING_BOTTOM-RMU_H/2-100}" class="ring-b-line"/>
<use href="#transformer" x="{X_RING_B-X_OFFSET}" y="{Y_RING_BOTTOM-150}"/>
<text x="{X_RING_B-X_OFFSET-60}" y="{Y_RING_BOTTOM-150}" class="rating" text-anchor="end">XFMR-B4</text>

<!-- ===================================================================== -->
<!--                  GENERATORS, SOLAR, BESS (13.8 KV)                    -->
<!-- ===================================================================== -->

<!-- Generators -->
<rect x="{X_CENTER-450}" y="{Y_GEN_SOLAR}" width="300" height="{GEN_H}" class="generator-box"/>
<text x="{X_CENTER-300}" y="{Y_GEN_SOLAR+30}" class="equipment-label" text-anchor="middle">GENERATORS (9×)</text>
<text x="{X_CENTER-300}" y="{Y_GEN_SOLAR+48}" class="rating" text-anchor="middle">4.0 MW ea @ 13.8 kV</text>
<text x="{X_CENTER-300}" y="{Y_GEN_SOLAR+62}" class="rating" text-anchor="middle">N+1 for 30 MW</text>

<!-- Solar + BESS -->
<rect x="{X_CENTER+150}" y="{Y_GEN_SOLAR}" width="300" height="{GEN_H}" class="generator-box"/>
<text x="{X_CENTER+300}" y="{Y_GEN_SOLAR+30}" class="equipment-label" text-anchor="middle">SOLAR + BESS</text>
<text x="{X_CENTER+300}" y="{Y_GEN_SOLAR+48}" class="rating" text-anchor="middle">8+ MW Solar</text>
<text x="{X_CENTER+300}" y="{Y_GEN_SOLAR+62}" class="rating" text-anchor="middle">4-8 MWh BESS @ 13.8kV</text>

<!-- Connection to dual-ring -->
<line x1="{X_CENTER-300}" y1="{Y_GEN_SOLAR}" x2="{X_CENTER-300}" y2="{Y_RING_BOTTOM+50}" class="power-line"/>
<line x1="{X_CENTER-300}" y1="{Y_RING_BOTTOM+50}" x2="{X_CENTER}" y2="{Y_RING_BOTTOM+50}" class="power-line"/>
<line x1="{X_CENTER+300}" y1="{Y_GEN_SOLAR}" x2="{X_CENTER+300}" y2="{Y_RING_BOTTOM+50}" class="power-line"/>
<line x1="{X_CENTER+300}" y1="{Y_RING_BOTTOM+50}" x2="{X_CENTER}" y2="{Y_RING_BOTTOM+50}" class="power-line"/>
<text x="{X_CENTER}" y="{Y_RING_BOTTOM+30}" class="rating" text-anchor="middle">13.8 kV Common Bus</text>

<!-- ===================================================================== -->
<!--                      LV SWITCHBOARDS (480V)                           -->
<!-- ===================================================================== -->

<!-- SWBD-A -->
<rect x="{X_RING_A+X_OFFSET/2-SWBD_W/2}" y="{Y_LV_SWBD-SWBD_H/2}" width="{SWBD_W}" height="{SWBD_H}" class="lv-switchboard"/>
<text x="{X_RING_A+X_OFFSET/2}" y="{Y_LV_SWBD-15}" class="equipment-label" text-anchor="middle">SWBD-A</text>
<text x="{X_RING_A+X_OFFSET/2}" y="{Y_LV_SWBD+5}" class="rating" text-anchor="middle">480V | Path A</text>
<text x="{X_RING_A+X_OFFSET/2}" y="{Y_LV_SWBD+20}" class="rating" text-anchor="middle">N+1 Transformers</text>

<!-- SWBD-B -->
<rect x="{X_RING_B-X_OFFSET/2-SWBD_W/2}" y="{Y_LV_SWBD-SWBD_H/2}" width="{SWBD_W}" height="{SWBD_H}" class="lv-switchboard"/>
<text x="{X_RING_B-X_OFFSET/2}" y="{Y_LV_SWBD-15}" class="equipment-label" text-anchor="middle">SWBD-B</text>
<text x="{X_RING_B-X_OFFSET/2}" y="{Y_LV_SWBD+5}" class="rating" text-anchor="middle">480V | Path B</text>
<text x="{X_RING_B-X_OFFSET/2}" y="{Y_LV_SWBD+20}" class="rating" text-anchor="middle">N+1 Transformers</text>

<!-- Connection from transformers to switchboards (simplified) -->
<line x1="{X_RING_A+X_OFFSET/2}" y1="{Y_RING_BOTTOM}" x2="{X_RING_A+X_OFFSET/2}" y2="{Y_LV_SWBD-SWBD_H/2}" class="power-line" stroke-dasharray="5,5"/>
<line x1="{X_RING_B-X_OFFSET/2}" y1="{Y_RING_BOTTOM}" x2="{X_RING_B-X_OFFSET/2}" y2="{Y_LV_SWBD-SWBD_H/2}" class="power-line" stroke-dasharray="5,5"/>

<!-- ===================================================================== -->
<!--                         UPS SYSTEM (N+1)                              -->
<!-- ===================================================================== -->

<rect x="{X_CENTER-UPS_W/2}" y="{Y_UPS-UPS_H/2}" width="{UPS_W}" height="{UPS_H}" class="ups-module"/>
<text x="{X_CENTER}" y="{Y_UPS-10}" class="equipment-label" text-anchor="middle">UPS MODULES</text>
<text x="{X_CENTER}" y="{Y_UPS+8}" class="rating" text-anchor="middle">25 × 1,250 kVA (N+1)</text>
<text x="{X_CENTER}" y="{Y_UPS+23}" class="rating" text-anchor="middle">24 MW IT Capacity</text>

<!-- Dual path connections -->
<line x1="{X_RING_A+X_OFFSET/2}" y1="{Y_LV_SWBD+SWBD_H/2}" x2="{X_RING_A+X_OFFSET/2}" y2="{Y_UPS}" class="power-line"/>
<line x1="{X_RING_A+X_OFFSET/2}" y1="{Y_UPS}" x2="{X_CENTER-UPS_W/2}" y2="{Y_UPS}" class="power-line"/>

<line x1="{X_RING_B-X_OFFSET/2}" y1="{Y_LV_SWBD+SWBD_H/2}" x2="{X_RING_B-X_OFFSET/2}" y2="{Y_UPS}" class="power-line"/>
<line x1="{X_RING_B-X_OFFSET/2}" y1="{Y_UPS}" x2="{X_CENTER+UPS_W/2}" y2="{Y_UPS}" class="power-line"/>

<!-- ===================================================================== -->
<!--                         IT EQUIPMENT                                  -->
<!-- ===================================================================== -->

<rect x="{X_CENTER-300}" y="{Y_IT-40}" width="600" height="80" fill="#E0F2F1" stroke="black" stroke-width="2"/>
<text x="{X_CENTER}" y="{Y_IT-5}" class="equipment-label" text-anchor="middle">IT EQUIPMENT</text>
<text x="{X_CENTER}" y="{Y_IT+15}" class="rating" text-anchor="middle">24 MW (Phase 4) | Dual-Corded (A+B Paths)</text>

<line x1="{X_CENTER}" y1="{Y_UPS+UPS_H/2}" x2="{X_CENTER}" y2="{Y_IT-40}" class="power-line"/>

<!-- ===================================================================== -->
<!--                              LEGEND                                   -->
<!-- ===================================================================== -->

<rect x="50" y="{Y_IT+80}" width="900" height="180" fill="#F5F5F5" stroke="black" stroke-width="1"/>
<text x="70" y="{Y_IT+110}" class="subtitle">DESIGN SUMMARY:</text>
<text x="70" y="{Y_IT+130}" class="rating">• IT Load: 24 MW (Phase 4), 30 MW Facility</text>
<text x="70" y="{Y_IT+148}" class="rating">• Utility: 2×35 MVA @ 345kV/13.8kV (N+1)</text>
<text x="70" y="{Y_IT+166}" class="rating">• MV Distribution: 13.8 kV Self-Healing Dual-Ring (8 RMUs)</text>
<text x="70" y="{Y_IT+184}" class="rating">• Transformers: 11×3,500 kVA (13.8kV/480V) N+1</text>
<text x="70" y="{Y_IT+202}" class="rating">• UPS: 25×1,250 kVA modular (N+1)</text>
<text x="70" y="{Y_IT+220}" class="rating">• Generators: 9×4.0 MW @ 13.8 kV (N+1 for 30 MW)</text>
<text x="70" y="{Y_IT+238}" class="rating">• Solar + BESS: 8+ MW Solar, 4-8 MWh BESS @ 13.8kV</text>

<rect x="1000" y="{Y_IT+80}" width="900" height="180" fill="#F5F5F5" stroke="black" stroke-width="1"/>
<text x="1020" y="{Y_IT+110}" class="subtitle">TIER III COMPLIANCE:</text>
<text x="1020" y="{Y_IT+130}" class="rating">• N+1 Component Redundancy: All major equipment</text>
<text x="1020" y="{Y_IT+148}" class="rating">• Path Redundancy: Dual-ring MV distribution (A/B paths)</text>
<text x="1020" y="{Y_IT+166}" class="rating">• Concurrent Maintainability: Self-healing ring topology</text>
<text x="1020" y="{Y_IT+184}" class="rating">• SCADA-Controlled: Automated switching, fault isolation</text>
<text x="1020" y="{Y_IT+202}" class="rating">• Dual-Corded IT Equipment: Path A + Path B</text>
<text x="1020" y="{Y_IT+220}" class="rating">• Phased Deployment: Infrastructure built for full 30 MW</text>
<text x="1020" y="{Y_IT+238}" class="rating">• Standards: IEC 60364, IEEE 315/IEC 60617, Tier III</text>

<!-- Ring legend -->
<line x1="2100" y1="{Y_IT+120}" x2="2180" y2="{Y_IT+120}" class="ring-a-line"/>
<text x="2190" y="{Y_IT+125}" class="rating">Ring A (Red)</text>
<line x1="2100" y1="{Y_IT+150}" x2="2180" y2="{Y_IT+150}" class="ring-b-line"/>
<text x="2190" y="{Y_IT+155}" class="rating">Ring B (Blue)</text>

</svg>'''

# Write output
output_file = 'saga_pryor_sld.svg'
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(svg)

print(f"[SUCCESS] Saga Pryor SLD generated: {output_file}")
print(f"[INFO] File size: {len(svg):,} bytes")
print(f"[INFO] Canvas: {WIDTH} x {HEIGHT} px")
print()
print("[SAGA PRYOR FEATURES]")
print("  - 13.8 kV Dual-Ring MV Distribution (self-healing)")
print("  - 8 RMUs (4 per ring) with SCADA control")
print("  - 2×35 MVA Substation Transformers (N+1)")
print("  - 11×3,500 kVA LV Transformers (shown simplified)")
print("  - 9×4.0 MW Generators @ 13.8 kV")
print("  - 8+ MW Solar + 4-8 MWh BESS")
print("  - 25×1,250 kVA UPS Modules (N+1)")
print("  - 24 MW IT Load (Phase 4)")
print("  - Tier III Concurrent Maintainability")
