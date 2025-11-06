"""
Generate single-line diagram for Pryor Data Center
Based on actual BOD specifications from 7BOD - Electrical (CSI Div 26).md
"""

from pachyderm_bod_generator import build_network_from_description
import json

# Pryor DC Electrical System Description (from BOD)
pryor_bod_text = """
Customer-owned 345 kV substation with two 25 MVA transformers (345kV/13.8kV) providing N+1 redundancy.
13.8 kV dual-ring MV distribution with 8 RMUs (Ring Main Units) for self-healing topology.
Six 4.0 MW diesel reciprocating generators at 13.8 kV (N+1 redundancy).
Phase 1: 3 generators, Phase 2: add 3 more generators.

Eight 3,500 kVA oil-filled transformers (13.8 kV/480V) with N+1 redundancy.
Phase 1: 3 transformers, Phase 2: add 5 transformers.

N+1 modular IT UPS architecture with 1,250 kVA modules.
Phase 1: 5 modules (approximately 5,000 kVA total).
Phase 2: 13 modules total (approximately 16,250 kVA total).
Static UPS with lithium-ion batteries providing 5-minute runtime.

Mechanical UPS for pumps and fans with N+1 redundancy.
Phase 1: 8 units at 250 kW each (2,000 kW total).
Phase 2: 20 units at 250 kW each (5,000 kW total).

Dual LV switchboards (SWBD-A and SWBD-B) fed from different MV ring segments.
Each cabinet has dual PDUs fed from different 480V distribution panels.
Phase 1: 30 cabinets at 100 kW each (3,000 kW IT load).
Phase 2: Same 30 cabinets upgraded to 400 kW each (12,000 kW IT load).

Ring bus topology with RMUs providing concurrent maintainability.
MV distribution at 13.8 kV with automated SCADA switching.
Path redundancy from dual-ring, component redundancy from N+1 architecture.
"""

print("="*60)
print("PRYOR DATA CENTER - ELECTRICAL SYSTEM GENERATOR")
print("="*60)
print("\nGenerating electrical model from BOD...")

# Generate network and metadata
try:
    network, metadata = build_network_from_description(
        pryor_bod_text,
        include_z_matrix=True
    )

    print("\n✓ Network model created successfully!")

    # Display summary
    print("\n" + "="*60)
    print("SYSTEM SUMMARY")
    print("="*60)
    print(f"Topology: {metadata['topology']}")
    print(f"Nominal Voltage: {metadata['buses'][0]['voltage']} kV")
    print(f"\nComponents Detected:")
    print(f"  • Buses: {len(metadata['buses'])}")
    print(f"  • Generators: {len(metadata['generators'])}")
    print(f"  • Transformers: {len(metadata['transformers'])}")
    print(f"  • RMUs: {len(metadata['rmu'])}")
    print(f"  • IT UPS Systems: {len([u for u in metadata['ups'] if u.get('function') == 'IT'])}")
    print(f"  • Mechanical UPS: {len([u for u in metadata['ups'] if u.get('function') == 'MECHANICAL'])}")
    print(f"  • MV Switchboards: {len(metadata['mv_swbd'])}")
    print(f"  • LV Switchboards: {len(metadata['lv_swbd'])}")

    # Generator details
    if metadata['generators']:
        print(f"\nGenerator Configuration:")
        for gen in metadata['generators'][:3]:  # Show first 3
            print(f"  • {gen['id']}: {gen['kw']} kW {gen['fuel']} {gen['type']} @ {metadata['buses'][0]['voltage']} kV")
        if len(metadata['generators']) > 3:
            print(f"  ... and {len(metadata['generators']) - 3} more")

    # Transformer details
    if metadata['transformers']:
        print(f"\nTransformer Configuration:")
        for tx in metadata['transformers'][:3]:  # Show first 3
            print(f"  • {tx['id']}: {tx['rated_kva']} kVA ({tx['voltage_primary']} kV / {tx['voltage_secondary']} kV)")
        if len(metadata['transformers']) > 3:
            print(f"  ... and {len(metadata['transformers']) - 3} more")

    # UPS details
    if metadata['ups']:
        print(f"\nUPS Configuration:")
        it_ups = [u for u in metadata['ups'] if u.get('function') == 'IT']
        mech_ups = [u for u in metadata['ups'] if u.get('function') == 'MECHANICAL']
        if it_ups:
            print(f"  • IT UPS: {len(it_ups)} × {it_ups[0]['kva']} kVA ({it_ups[0]['type']}, {it_ups[0]['battery']})")
        if mech_ups:
            print(f"  • Mechanical UPS: {len(mech_ups)} × {mech_ups[0]['kw']} kW")

    # Save metadata to JSON
    output_file = "pryor_dc_electrical_metadata.json"
    with open(output_file, 'w') as f:
        json.dump(metadata, f, indent=2)
    print(f"\n✓ Metadata saved to: {output_file}")

    # Try to generate diagram
    try:
        print("\nGenerating single-line diagram...")
        diagram_svg = network.get_single_line_diagram('SWGR_A')  # or whatever main bus
        with open('pryor_dc_sld.svg', 'w') as f:
            f.write(diagram_svg)
        print("✓ Diagram saved to: pryor_dc_sld.svg")
    except Exception as e:
        print(f"⚠ Diagram generation skipped: {e}")
        print("  (Network model and metadata are still valid)")

    print("\n" + "="*60)
    print("NEXT STEPS")
    print("="*60)
    print("1. Review metadata: pryor_dc_electrical_metadata.json")
    print("2. Run validation: python pachyderm_schema_validator.py")
    print("3. View diagram (if generated): pryor_dc_sld.svg")
    print("="*60)

except Exception as e:
    print(f"\n✗ Error generating network: {e}")
    import traceback
    traceback.print_exc()
