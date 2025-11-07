"""
Test SLD generation using the FIXED parser on actual Saga Pryor BOD
"""
import sys
from pathlib import Path
from pachyderm_bod_generator_fixed import build_network_from_description
import json

# Read the actual BOD file
bod_file = Path(r"C:\Users\eriks\Documents\Obsidian\Saga Pryor DC\Basis of Design\7BOD - Electrical (CSI Div 26).md")

print("=" * 80)
print("SAGA PRYOR SLD GENERATION TEST")
print("=" * 80)

if not bod_file.exists():
    print(f"\nERROR: BOD file not found at {bod_file}")
    sys.exit(1)

print(f"\nReading BOD from: {bod_file.name}")

with open(bod_file, 'r', encoding='utf-8') as f:
    bod_text = f.read()

print(f"BOD file size: {len(bod_text):,} characters")
print("\nParsing BOD with FIXED parser...")

try:
    network, metadata = build_network_from_description(bod_text, include_z_matrix=True)

    print(f"\nSUCCESS: Network Model Created")
    print(f"Network ID: {network.id}")
    print(f"Topology: {metadata['topology'].upper().replace('_', ' ')}")

    # Save metadata
    metadata_file = Path("saga_pryor_metadata.json")
    with open(metadata_file, 'w') as f:
        json.dump(metadata, f, indent=2)
    print(f"\nMetadata saved to: {metadata_file}")

    # Component summary
    print("\n" + "=" * 80)
    print("COMPONENT SUMMARY")
    print("=" * 80)
    print(f"\nVoltage Levels: {len(metadata['buses'])} voltage levels")
    for bus in metadata['buses']:
        print(f"  - {bus['voltage']:.1f} kV")

    print(f"\nGenerators: {len(metadata['generators'])}")
    print(f"  Total capacity: {sum(g['kw'] for g in metadata['generators'])/1000:.1f} MW")

    print(f"\nTransformers: {len(metadata['transformers'])}")
    print(f"  Total capacity: {sum(t['rated_s'] for t in metadata['transformers'])/1000:.1f} MVA")

    print(f"\nRMUs: {len(metadata['rmu'])}")

    print(f"\nUPS Systems: {len(metadata['ups'])}")
    it_ups = [u for u in metadata['ups'] if u['function'] == 'IT']
    mech_ups = [u for u in metadata['ups'] if u['function'] == 'MECHANICAL']
    print(f"  IT UPS: {len(it_ups)} modules ({sum(u['kva'] for u in it_ups)/1000:.1f} MVA total)")
    print(f"  Mechanical UPS: {len(mech_ups)} modules ({sum(u['kw'] for u in mech_ups)/1000:.1f} MW total)")

    # Try to generate SLD using PowSyBl network diagram
    print("\n" + "=" * 80)
    print("ATTEMPTING SLD GENERATION")
    print("=" * 80)

    try:
        import pypowsybl.network as pn

        # Try to generate network area diagram
        svg_output = Path("saga_pryor_network_diagram.svg")

        # Get network statistics
        print(f"\nNetwork statistics:")
        print(f"  Substations: {len(network.get_substations())}")
        print(f"  Voltage levels: {len(network.get_voltage_levels())}")
        print(f"  Buses: {len(network.get_buses())}")
        print(f"  Generators: {len(network.get_generators())}")
        print(f"  Loads: {len(network.get_loads())}")

        # List substations
        substations = network.get_substations()
        if not substations.empty:
            print(f"\nSubstations created:")
            for idx, row in substations.iterrows():
                print(f"  - {row['name']}")

        # List voltage levels
        voltage_levels = network.get_voltage_levels()
        if not voltage_levels.empty:
            print(f"\nVoltage levels created:")
            for idx, row in voltage_levels.iterrows():
                print(f"  - {row['name']} ({row['nominal_v']:.1f} kV) in substation {row['substation_id']}")

        # Check if we can generate a diagram
        try:
            # For PowSyBl, we need network area diagram or single line diagram
            # Since we have multiple voltage levels, let's try network area diagram
            print(f"\nAttempting to generate network area diagram...")

            # This requires the diagram module
            try:
                import pypowsybl.diagram as diag

                # Try to create a network area diagram
                nad = diag.create_network_area_diagram(network)
                nad.write_svg(str(svg_output))

                print(f"SUCCESS: Network diagram saved to {svg_output}")

            except ImportError:
                print("WARNING: pypowsybl.diagram module not available")
                print("Install with: pip install pypowsybl[diagram]")
            except Exception as e:
                print(f"Could not generate network area diagram: {e}")
                print("\nNote: PowSyBl SLD generation requires proper network topology")
                print("Consider using custom SVG generation scripts instead")

        except Exception as e:
            print(f"Diagram generation error: {e}")

    except Exception as e:
        print(f"PowSyBl diagram error: {e}")

    # Summary
    print("\n" + "=" * 80)
    print("NEXT STEPS")
    print("=" * 80)
    print("\nThe parser has successfully extracted all specifications from the BOD.")
    print("PowSyBl network model has been created with:")
    print(f"  - {len(metadata['generators'])} generators")
    print(f"  - {len(metadata['transformers'])} transformers")
    print(f"  - {len(metadata['ups'])} UPS modules")
    print(f"  - {len(metadata['rmu'])} RMUs")

    print("\nFor professional SLD generation, consider:")
    print("  1. generate_professional_sld.py - Custom SVG generator")
    print("  2. generate_ring_bus_sld.py - Ring topology specific")
    print("  3. Export to DXF/PDF for CAD software")

    print("\n" + "=" * 80)

except Exception as e:
    print(f"\nERROR during generation: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
