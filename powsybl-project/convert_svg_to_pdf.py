"""
Convert SVG to PDF using available Python libraries
"""
from pathlib import Path
import subprocess
import sys

svg_file = Path('saga_pryor_sld_from_bod.svg')
pdf_file = Path('saga_pryor_sld_from_bod.pdf')

if not svg_file.exists():
    print(f"ERROR: {svg_file} not found!")
    sys.exit(1)

print(f"Converting {svg_file} to PDF...")

# Try method 1: cairosvg (if installed)
try:
    import cairosvg
    cairosvg.svg2pdf(url=str(svg_file), write_to=str(pdf_file))
    print(f"SUCCESS: Created {pdf_file} using cairosvg")
    sys.exit(0)
except ImportError:
    print("cairosvg not installed (pip install cairosvg)")
except Exception as e:
    print(f"cairosvg failed: {e}")

# Try method 2: svglib + reportlab (if installed)
try:
    from svglib.svglib import renderPDF
    from reportlab.graphics import renderPDF as rlRenderPDF

    drawing = renderPDF.svg2rlg(str(svg_file))
    rlRenderPDF.drawToFile(drawing, str(pdf_file))
    print(f"SUCCESS: Created {pdf_file} using svglib")
    sys.exit(0)
except ImportError:
    print("svglib not installed (pip install svglib reportlab)")
except Exception as e:
    print(f"svglib failed: {e}")

# Try method 3: Inkscape command line (if installed)
try:
    result = subprocess.run(
        ['inkscape', '--export-type=pdf', str(svg_file)],
        capture_output=True,
        text=True
    )
    if result.returncode == 0:
        print(f"SUCCESS: Created {pdf_file} using Inkscape CLI")
        sys.exit(0)
    else:
        print(f"Inkscape failed: {result.stderr}")
except FileNotFoundError:
    print("Inkscape not found in PATH")
except Exception as e:
    print(f"Inkscape failed: {e}")

# All methods failed
print("\n" + "=" * 80)
print("MANUAL CONVERSION OPTIONS:")
print("=" * 80)
print("\nOption 1: Install Python library")
print("  pip install cairosvg")
print("  Then run this script again")

print("\nOption 2: Use web browser")
print("  1. Open saga_pryor_sld_from_bod.svg in Chrome/Edge/Firefox")
print("  2. Press Ctrl+P (Print)")
print("  3. Select 'Save as PDF'")
print("  4. Choose landscape orientation")

print("\nOption 3: Install Inkscape (free)")
print("  1. Download from https://inkscape.org")
print("  2. File > Save As > PDF")

print(f"\n{'='*80}")
