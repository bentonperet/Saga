"""
IEEE Std 315 / IEC 60617 Compliant Single-Line Diagram Standards
Universal configuration for all SLD topologies
"""

# Symbol Definitions - IEEE Std 315-1975 Compliant
SYMBOLS = {
    'breaker_closed': '''
        <g id="breaker-closed">
            <rect x="-8" y="-12" width="16" height="24" fill="white" stroke="black" stroke-width="1.5"/>
            <line x1="-6" y1="-8" x2="6" y2="8" stroke="black" stroke-width="2"/>
            <line x1="-6" y1="8" x2="6" y2="-8" stroke="black" stroke-width="2"/>
        </g>
    ''',
    
    'breaker_open': '''
        <g id="breaker-open">
            <rect x="-8" y="-12" width="16" height="24" fill="white" stroke="black" stroke-width="1.5"/>
            <line x1="0" y1="-8" x2="0" y2="-2" stroke="black" stroke-width="2"/>
            <line x1="0" y1="2" x2="0" y2="8" stroke="black" stroke-width="2"/>
            <circle cx="0" cy="0" r="2.5" fill="white" stroke="black" stroke-width="1.5"/>
        </g>
    ''',
    
    'transformer': '''
        <g id="transformer">
            <circle cx="-8" cy="0" r="10" fill="white" stroke="black" stroke-width="1.5"/>
            <circle cx="8" cy="0" r="10" fill="white" stroke="black" stroke-width="1.5"/>
            <line x1="-8" y1="-10" x2="-8" y2="-20" stroke="black" stroke-width="2"/>
            <line x1="8" y1="10" x2="8" y2="20" stroke="black" stroke-width="2"/>
        </g>
    ''',
    
    'generator': '''
        <g id="generator">
            <circle cx="0" cy="0" r="30" fill="white" stroke="black" stroke-width="2"/>
            <text x="0" y="8" font-family="Arial" font-size="20" font-weight="bold" text-anchor="middle" fill="black">G</text>
        </g>
    ''',
    
    'connection_point': '''
        <g id="connection-point">
            <circle cx="0" cy="0" r="3" fill="black"/>
        </g>
    ''',
    
    'fuse': '''
        <g id="fuse">
            <rect x="-6" y="-10" width="12" height="20" fill="white" stroke="black" stroke-width="1.5"/>
            <line x1="0" y1="-6" x2="0" y2="6" stroke="black" stroke-width="2"/>
            <circle cx="0" cy="0" r="3" fill="white" stroke="black" stroke-width="1.5"/>
        </g>
    ''',
    
    'disconnect_switch_closed': '''
        <g id="disconnect-closed">
            <line x1="0" y1="-12" x2="0" y2="12" stroke="black" stroke-width="2"/>
            <circle cx="0" cy="-12" r="2" fill="black"/>
            <circle cx="0" cy="12" r="2" fill="black"/>
        </g>
    ''',
    
    'disconnect_switch_open': '''
        <g id="disconnect-open">
            <line x1="0" y1="-12" x2="4" y2="0" stroke="black" stroke-width="2"/>
            <circle cx="0" cy="-12" r="2" fill="black"/>
            <circle cx="0" cy="12" r="2" fill="black"/>
        </g>
    '''
}

# Line Styles - IEEE 315 Compliant
LINE_STYLES = {
    'power_line': {
        'stroke': '#000000',
        'stroke-width': '2',
        'fill': 'none'
    },
    'bus': {
        'stroke': '#000000',
        'stroke-width': '6',
        'fill': 'none'
    },
    'control_circuit': {
        'stroke': '#000000',
        'stroke-width': '1',
        'stroke-dasharray': '5,5',
        'fill': 'none'
    },
    'ground': {
        'stroke': '#000000',
        'stroke-width': '2',
        'fill': 'none'
    },
    'neutral': {
        'stroke': '#000000',
        'stroke-width': '1.5',
        'fill': 'none'
    }
}

# Equipment Box Styles
EQUIPMENT_STYLES = {
    'switchgear': {
        'fill': '#F5F5F5',
        'stroke': 'black',
        'stroke-width': '2'
    },
    'transformer_box': {
        'fill': '#FAFAFA',
        'stroke': 'black',
        'stroke-width': '2'
    },
    'generator_enclosure': {
        'fill': '#F0F0F0',
        'stroke': 'black',
        'stroke-width': '2'
    },
    'rmu': {
        'fill': '#F8F8F8',
        'stroke': 'black',
        'stroke-width': '2'
    },
    'ups': {
        'fill': '#FCFCFC',
        'stroke': 'black',
        'stroke-width': '2'
    }
}

# Text Styles - Open Sans Font Hierarchy (Updated 2025-11-02)
TEXT_STYLES = {
    'title': {
        'font-family': '"Open Sans", Arial',
        'font-size': '24',
        'font-weight': 'bold',
        'fill': '#000000'
    },
    'subtitle': {
        'font-family': '"Open Sans", Arial',
        'font-size': '14',
        'font-weight': 'bold',
        'fill': '#000000'
    },
    'equipment_label': {
        'font-family': '"Open Sans", Arial',
        'font-size': '14',
        'font-weight': 'bold',
        'fill': '#000000'
    },
    'rating': {
        'font-family': '"Open Sans", Arial',
        'font-size': '11',
        'font-weight': 'normal',
        'fill': '#333333'
    },
    'annotation': {
        'font-family': '"Open Sans", Arial',
        'font-size': '11',
        'font-weight': 'normal',
        'fill': '#000000'
    },
    'note': {
        'font-family': '"Open Sans", Arial',
        'font-size': '11',
        'font-weight': 'normal',
        'fill': '#000000',
        'font-style': 'italic'
    }
}

# Layout Rules
LAYOUT = {
    'flow_direction': 'top_to_bottom',
    'voltage_hierarchy': 'descending',  # Higher voltage at top
    'minimum_spacing': 50,  # Pixels between equipment
    'equipment_alignment': 'grid',  # Snap to grid
    'routing': 'orthogonal',  # Only 90-degree angles
    'clearance_from_equipment': 30,  # Minimum distance for breakers/connections from equipment
    'bus_vertical_spacing': 100,  # Vertical space between bus levels
    'phase_spacing': 20  # For three-phase representations
}

# Annotation Rules
ANNOTATIONS = {
    'breaker_status': 'symbol_only',  # Don't add text labels
    'equipment_names': 'inside_or_adjacent',
    'ratings_position': 'below_equipment',
    'voltage_display': 'prominent',
    'protection_settings': 'optional',
    'notes_section': 'bottom_right',
    'legend': 'required_if_non_standard'
}

# Title Block Requirements (ANSI Y14.1)
TITLE_BLOCK = {
    'required_fields': [
        'project_name',
        'drawing_title',
        'date',
        'revision',
        'drawn_by',
        'approved_by',
        'sheet_number'
    ],
    'position': 'top_center',  # Or 'bottom_right' per company standard
    'border': True,
    'width': 'full_width',
    'height': 100
}

# Voltage Level Colors (Optional - for voltage differentiation only)
# Note: Use sparingly and only when multiple voltage levels need clear distinction
VOLTAGE_COLORS = {
    'use_color': False,  # Set to True only if needed for clarity
    'high_voltage': '#B8E0D2',  # Light green
    'medium_voltage': '#D6EAF8',  # Light blue
    'low_voltage': '#FCE4EC'  # Light pink
}

# Redundancy Representation
REDUNDANCY = {
    'method': 'spatial_duplication',  # Show both paths
    'path_differentiation': 'spatial_only',  # Use position, not color
    'breaker_states': 'normal_operation',  # Show normal (not all possible) states
    'notes_required': True,  # Explain operating philosophy
    'alternate_paths': 'clearly_visible'
}

# Grid Settings
GRID = {
    'base_unit': 10,  # All coordinates should be multiples of 10
    'snap_enabled': True,
    'visible': False  # Don't render grid in final output
}

# Standards References
STANDARDS = {
    'primary': 'IEEE Std 315-1975',
    'international': 'IEC 60617',
    'drafting': 'ANSI Y14.1',
    'electrical': 'IEEE Std 141 (Red Book)',
    'notes': 'Symbols and conventions follow IEEE/IEC standards for electrical power distribution'
}

def get_svg_style_section():
    """Generate CSS styles for SVG - SLD Standards v1.1 Compliant (Open Sans fonts)"""
    return f'''
    <style>
        /* Text Styles - SLD Standards v1.1 - Open Sans Font Hierarchy */
        .title {{ font: bold 24px "Open Sans", Arial; fill: #000; }}
        .subtitle {{ font: bold 14px "Open Sans", Arial; fill: #000; }}
        .equipment-label {{ font: bold 14px "Open Sans", Arial; fill: #000; }}
        .bus-label {{ font: bold 12px "Open Sans", Arial; fill: #000; }}
        .small-label {{ font: 11px "Open Sans", Arial; fill: #000; }}
        .rating {{ font: 11px "Open Sans", Arial; fill: #333; }}
        .annotation {{ font: 11px "Open Sans", Arial; fill: #000; }}
        .feeder-label {{ font: 10px "Open Sans", Arial; fill: #666; }}
        .note {{ font: italic 11px "Open Sans", Arial; fill: #000; }}

        /* Line Styles */
        .power-line {{ stroke: #000; stroke-width: 2; fill: none; }}
        .bus {{ stroke: #000; stroke-width: 6; fill: none; }}
        .control-line {{ stroke: #000; stroke-width: 1; stroke-dasharray: 5,5; fill: none; }}

        /* Equipment Boxes - LIGHT BACKGROUNDS for readability */
        .mv-switchboard {{ fill: #E3F2FD; stroke: #000; stroke-width: 2; }}
        .lv-switchboard {{ fill: #E8F5E9; stroke: #000; stroke-width: 2; }}
        .generator-box {{ fill: #FFF3E0; stroke: #000; stroke-width: 2; }}
        .transformer-box {{ fill: #FFFFFF; stroke: #000; stroke-width: 2; }}
        .rmu-box {{ fill: #FFF9C4; stroke: #000; stroke-width: 2; }}
        .ups-module {{ fill: #F3E5F5; stroke: #000; stroke-width: 1.5; }}
        .dist-panel {{ fill: #E0F2F1; stroke: #000; stroke-width: 1; }}

        /* Legacy aliases for backwards compatibility */
        .switchgear-box {{ fill: #E3F2FD; stroke: black; stroke-width: 2; }}
        .ups-box {{ fill: #F3E5F5; stroke: black; stroke-width: 2; }}

        /* Ring Bus Colors */
        .ring-bus-a {{ stroke: #E74C3C; stroke-width: 4; fill: none; }}
        .ring-bus-b {{ stroke: #3498DB; stroke-width: 4; fill: none; }}
    </style>
    '''

def get_svg_symbols():
    """Return all standard symbols as SVG defs"""
    symbols_svg = '<defs>\n'
    for symbol_id, symbol_def in SYMBOLS.items():
        symbols_svg += symbol_def + '\n'
    symbols_svg += '</defs>\n'
    return symbols_svg

def validate_layout(x, y):
    """Ensure coordinates snap to grid"""
    if GRID['snap_enabled']:
        base = GRID['base_unit']
        return (round(x / base) * base, round(y / base) * base)
    return (x, y)

def calculate_symmetric_positions(canvas_width, equipment_count, equipment_width, margin):
    """
    Calculate symmetrically spaced positions per SLD Standards v1.1 Section 2.2

    Returns center points for equipment, evenly distributed across canvas width.

    Args:
        canvas_width: Total canvas width in pixels
        equipment_count: Number of equipment items to position
        equipment_width: Width of each equipment item in pixels
        margin: Margin from canvas edges in pixels

    Returns:
        List of x-coordinates (center points) for each equipment item

    Example:
        # Position 4 transformers on 2800px canvas with 200px margins
        tx_positions = calculate_symmetric_positions(2800, 4, 80, 200)
        # Returns [495.0, 995.0, 1495.0, 1995.0] - evenly spaced centers
    """
    usable_width = canvas_width - (2 * margin)
    total_equipment_width = equipment_count * equipment_width
    available_space = usable_width - total_equipment_width
    spacing = available_space / (equipment_count + 1)

    positions = []
    for i in range(equipment_count):
        x = margin + spacing * (i + 1) + equipment_width * i + (equipment_width / 2)
        positions.append(x)

    return positions
