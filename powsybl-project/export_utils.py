"""
Multi-Format Export Utilities for Single-Line Diagrams
Converts SVG drawings to PNG, PDF, and DXF formats
"""

import os
from pathlib import Path
try:
    import cairosvg
    CAIRO_AVAILABLE = True
except (ImportError, OSError):
    CAIRO_AVAILABLE = False

# Use svglib for PDF conversion
try:
    from svglib.svglib import svg2rlg
    SVGLIB_AVAILABLE = True
except ImportError:
    SVGLIB_AVAILABLE = False

from reportlab.lib.pagesizes import landscape, letter, A3, A2, A1, A0
from reportlab.pdfgen import canvas as pdf_canvas
from reportlab.lib.utils import ImageReader
from reportlab.graphics import renderPDF
import ezdxf
from ezdxf import units
from xml.etree import ElementTree as ET
import re


def svg_to_png(svg_file, png_file=None, scale=2.0):
    """
    Convert SVG to high-resolution PNG
    
    Args:
        svg_file: Path to input SVG file
        png_file: Path to output PNG file (optional, defaults to same name)
        scale: Resolution scale factor (2.0 = 2x resolution for crisp output)
    
    Returns:
        Path to created PNG file
    """
    if png_file is None:
        png_file = Path(svg_file).with_suffix('.png')
    
    # Parse SVG to get dimensions
    tree = ET.parse(svg_file)
    root = tree.getroot()
    width = float(root.get('width', 1000))
    height = float(root.get('height', 800))
    
    if CAIRO_AVAILABLE:
        # Use CairoSVG if available
        cairosvg.svg2png(
            url=str(svg_file),
            write_to=str(png_file),
            output_width=int(width * scale),
            output_height=int(height * scale)
        )
    elif SVGLIB_AVAILABLE:
        # Use svglib + reportlab as fallback
        drawing = svg2rlg(str(svg_file))
        drawing.width = width * scale
        drawing.height = height * scale
        drawing.scale(scale, scale)
        renderPM.drawToFile(drawing, str(png_file), fmt='PNG', dpi=72*scale)
    else:
        raise ImportError("Neither CairoSVG nor svglib is available. Install one of them: pip install cairosvg OR pip install svglib")
    
    print(f"✅ PNG created: {png_file} ({int(width * scale)}x{int(height * scale)})")
    return png_file


def svg_to_pdf(svg_file, pdf_file=None, page_size='A1'):
    """
    Convert SVG to PDF with proper page sizing
    
    Args:
        svg_file: Path to input SVG file
        pdf_file: Path to output PDF file (optional)
        page_size: Page size ('A0', 'A1', 'A2', 'A3', 'letter', or tuple of (width, height) in points)
    
    Returns:
        Path to created PDF file
    """
    if pdf_file is None:
        pdf_file = Path(svg_file).with_suffix('.pdf')
    
    # Define page sizes (width, height in points, 1 point = 1/72 inch)
    page_sizes = {
        'A0': (3370, 2384),  # Landscape
        'A1': (2384, 1684),  # Landscape  
        'A2': (1684, 1191),  # Landscape
        'A3': (1191, 842),   # Landscape
        'letter': landscape(letter)
    }
    
    if isinstance(page_size, str):
        page_size = page_sizes.get(page_size.upper(), page_sizes['A1'])
    
    # Use svglib to render SVG directly to PDF
    from svglib.svglib import svg2rlg
    drawing = svg2rlg(str(svg_file))
    
    # Create PDF and render
    renderPDF.drawToFile(drawing, str(pdf_file))
    
    print(f"✅ PDF created: {pdf_file}")
    print(f"   Note: PDF uses SVG's original dimensions. Open in PDF viewer to print at desired scale.")
    return pdf_file


def svg_to_dxf(svg_file, dxf_file=None):
    """
    Convert SVG to DXF format for CAD applications
    Converts basic SVG elements (lines, rectangles, circles, text) to DXF entities
    
    Args:
        svg_file: Path to input SVG file
        dxf_file: Path to output DXF file (optional)
    
    Returns:
        Path to created DXF file
    """
    if dxf_file is None:
        dxf_file = Path(svg_file).with_suffix('.dxf')
    
    # Create new DXF document
    doc = ezdxf.new('R2010')
    doc.units = units.MM
    msp = doc.modelspace()
    
    # Parse SVG
    tree = ET.parse(svg_file)
    root = tree.getroot()
    
    # Extract namespace
    ns = {'svg': 'http://www.w3.org/2000/svg'}
    
    # Helper function to parse stroke width
    def get_stroke_width(element):
        style = element.get('style', '')
        stroke_match = re.search(r'stroke-width:\s*(\d+)', style)
        if stroke_match:
            return float(stroke_match.group(1)) * 0.3  # Convert px to mm approximation
        stroke_width = element.get('stroke-width', '1')
        return float(stroke_width) * 0.3
    
    # Helper function to get color from element
    def get_color(element, attr='stroke'):
        style = element.get('style', '')
        color_match = re.search(f'{attr}:\\s*#([0-9a-fA-F]{{6}})', style)
        if color_match:
            return int(color_match.group(1), 16)
        color = element.get(attr, '#000000')
        if color.startswith('#'):
            return int(color[1:], 16)
        return 7  # Default AutoCAD white/black
    
    # Convert lines
    for line in root.findall('.//svg:line', ns):
        x1 = float(line.get('x1', 0)) * 0.3
        y1 = -float(line.get('y1', 0)) * 0.3  # Flip Y axis
        x2 = float(line.get('x2', 0)) * 0.3
        y2 = -float(line.get('y2', 0)) * 0.3
        
        dxf_line = msp.add_line((x1, y1), (x2, y2))
        dxf_line.dxf.lineweight = int(get_stroke_width(line) * 100)
    
    # Convert rectangles
    for rect in root.findall('.//svg:rect', ns):
        x = float(rect.get('x', 0)) * 0.3
        y = -float(rect.get('y', 0)) * 0.3
        width = float(rect.get('width', 0)) * 0.3
        height = float(rect.get('height', 0)) * 0.3
        
        # Create rectangle as polyline
        points = [
            (x, y),
            (x + width, y),
            (x + width, y - height),
            (x, y - height),
            (x, y)
        ]
        msp.add_lwpolyline(points, close=True)
    
    # Convert circles
    for circle in root.findall('.//svg:circle', ns):
        cx = float(circle.get('cx', 0)) * 0.3
        cy = -float(circle.get('cy', 0)) * 0.3
        r = float(circle.get('r', 0)) * 0.3
        
        msp.add_circle((cx, cy), r)
    
    # Convert text (basic - positioning may need adjustment)
    for text in root.findall('.//svg:text', ns):
        x = float(text.get('x', 0)) * 0.3
        y = -float(text.get('y', 0)) * 0.3
        content = text.text or ''
        
        if content.strip():
            msp.add_text(
                content,
                dxfattribs={
                    'insert': (x, y),
                    'height': 3,  # Default text height in mm
                }
            )
    
    # Save DXF
    doc.saveas(str(dxf_file))
    
    print(f"✅ DXF created: {dxf_file}")
    print(f"   Note: DXF is a simplified conversion. Complex symbols may need manual adjustment in CAD.")
    return dxf_file


def export_all_formats(svg_file, output_dir=None, formats=['png', 'pdf', 'dxf']):
    """
    Export SVG to multiple formats at once
    
    Args:
        svg_file: Path to input SVG file
        output_dir: Directory for output files (optional, defaults to same as SVG)
        formats: List of formats to export ('png', 'pdf', 'dxf')
    
    Returns:
        Dictionary of format: filepath pairs
    """
    if output_dir:
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
    else:
        output_dir = Path(svg_file).parent
    
    base_name = Path(svg_file).stem
    results = {'svg': svg_file}
    
    if 'png' in formats:
        png_file = output_dir / f"{base_name}.png"
        results['png'] = svg_to_png(svg_file, png_file)
    
    if 'pdf' in formats:
        pdf_file = output_dir / f"{base_name}.pdf"
        results['pdf'] = svg_to_pdf(svg_file, pdf_file)
    
    if 'dxf' in formats:
        dxf_file = output_dir / f"{base_name}.dxf"
        results['dxf'] = svg_to_dxf(svg_file, dxf_file)
    
    return results


if __name__ == "__main__":
    # Test with existing SVG
    test_svg = "saga_pryor_ring_bus_sld.svg"
    if Path(test_svg).exists():
        print("Testing export utilities...")
        results = export_all_formats(test_svg)
        print("\n✅ All exports completed!")
        for fmt, path in results.items():
            print(f"   {fmt.upper()}: {path}")
