"""
Test script to generate SLD from actual Saga Pryor BOD document
Fixed encoding issues for Windows console
"""

import sys
from pathlib import Path
from pachyderm_bod_generator import build_network_from_description
import json

# Read the actual BOD file
bod_file = Path(r"C:\Users\eriks\Documents\Obsidian\Saga Pryor DC\Basis of Design\7BOD - Electrical (CSI Div 26).md")

print("=" * 80)
print("SAGA PRYOR DATA CENTER - BOD Parser Test")
print("=" * 80)

if not bod_file.exists():
    print(f"\nERROR: BOD file not found at {bod_file}")
    sys.exit(1)

print(f"\nReading BOD from: {bod_file.name}")

with open(bod_file, 'r', encoding='utf-8') as f:
    bod_text = f.read()

print(f"BOD file size: {len(bod_text):,} characters")
print("\nParsing BOD and building network model...")

try:
    network, metadata = build_network_from_description(bod_text, include_z_matrix=True)

    print(f"\nSUCCESS: Network Model Created")
    print(f"Network ID: {network.id}")
    print(f"Topology: {metadata['topology'].upper().replace('_', ' ')}")

    # Detailed component summary
    print("\n" + "=" * 80)
    print("COMPONENT SUMMARY")
    print("=" * 80)

    print(f"\nBuses: {len(metadata['buses'])}")
    for bus in metadata['buses'][:10]:  # Show first 10
        print(f"  {bus['id']}: {bus['voltage']} kV")
    if len(metadata['buses']) > 10:
        print(f"  ... and {len(metadata['buses']) - 10} more buses")

    print(f"\nGenerators: {len(metadata['generators'])}")
    for gen in metadata['generators']:
        print(f"  {gen['id']}: {gen['type']} {gen['fuel']} - {gen['kw']} kW / {gen['kva']} kVA")
        print(f"    Connected to: {gen['bus']}")

    print(f"\nTransformers: {len(metadata['transformers'])}")
    for tx in metadata['transformers']:
        print(f"  {tx['id']}: {tx['rated_s']} kVA ({tx['hv_voltage']}kV -> {tx['lv_voltage']}kV)")

    print(f"\nMV Switchboards: {len(metadata['mv_swbd'])}")
    for swbd in metadata['mv_swbd']:
        print(f"  {swbd['id']}: {swbd['voltage']} kV, {swbd['rating_a']}A, {swbd['interrupt_rating_ka']} kAIC")
        print(f"    Redundancy: {swbd['redundancy']}")

    print(f"\nRMUs (Ring Main Units): {len(metadata['rmu'])}")
    for rmu in metadata['rmu']:
        print(f"  {rmu}")

    print(f"\nUPS Systems: {len(metadata['ups'])}")
    for ups in metadata['ups']:
        print(f"  {ups['id']}: {ups['type']} {ups['battery']} ({ups['function']})")
        print(f"    Rating: {ups['kw']} kW / {ups['kva']} kVA")

    print(f"\nLV Switchboards: {len(metadata['lv_swbd'])}")
    for swbd in metadata['lv_swbd']:
        print(f"  {swbd['id']}: {swbd['voltage']} V, {swbd['rating_a']}A")

    print(f"\nPDUs: {len(metadata['pdus'])}")

    if metadata['earthing_tx']:
        print(f"\nEarthing Transformers: {len(metadata['earthing_tx'])}")
        for earth in metadata['earthing_tx']:
            print(f"  {earth['id']}: {earth['type']} - {earth['rated_kva']} kVA")

    # VALIDATION AGAINST ACTUAL BOD SPECS
    print("\n" + "=" * 80)
    print("VALIDATION AGAINST BOD SPECIFICATIONS")
    print("=" * 80)

    # Expected from BOD
    expected_specs = {
        'mv_voltage': 13.8,
        'generators': 6,
        'generator_kw': 4000,
        'transformers': 8,
        'transformer_kva': 3500,
        'rmu_count': 6,
        'it_ups_modules': 5,  # Phase 1
        'it_ups_kva': 1250,
        'mech_ups_modules': 8,  # Phase 1
        'mech_ups_kw': 250
    }

    # Check voltage
    print("\n1. VOLTAGE DETECTION:")
    detected_voltage = metadata['buses'][0]['voltage'] if metadata['buses'] else None
    print(f"   Expected MV: {expected_specs['mv_voltage']} kV")
    print(f"   Detected MV: {detected_voltage} kV")
    if detected_voltage == expected_specs['mv_voltage']:
        print("   STATUS: OK")
    else:
        print("   STATUS: WRONG - Bug in voltage detection!")
        print("   ISSUE: Parser picking up utility voltage (345kV) instead of MV distribution voltage")

    # Check generators
    print("\n2. GENERATOR COUNT:")
    print(f"   Expected: {expected_specs['generators']} generators")
    print(f"   Detected: {len(metadata['generators'])} generators")
    if len(metadata['generators']) == expected_specs['generators']:
        print("   STATUS: OK")
    else:
        print(f"   STATUS: WRONG - Off by {abs(len(metadata['generators']) - expected_specs['generators'])}")

    print("\n3. GENERATOR RATINGS:")
    print(f"   Expected: {expected_specs['generator_kw']} kW each")
    if metadata['generators']:
        actual_kw = metadata['generators'][0]['kw']
        print(f"   Detected: {actual_kw} kW each")
        if actual_kw == expected_specs['generator_kw']:
            print("   STATUS: OK")
        else:
            print("   STATUS: WRONG - Using default values instead of BOD specs")

    # Check transformers
    print("\n4. TRANSFORMER COUNT:")
    print(f"   Expected: {expected_specs['transformers']} transformers (Phase 1: 3, Phase 2: 8)")
    print(f"   Detected: {len(metadata['transformers'])} transformers")

    print("\n5. TRANSFORMER RATINGS:")
    print(f"   Expected: {expected_specs['transformer_kva']} kVA each")
    if metadata['transformers']:
        actual_kva = metadata['transformers'][0]['rated_s']
        print(f"   Detected: {actual_kva} kVA each")
        if actual_kva == expected_specs['transformer_kva']:
            print("   STATUS: OK")
        else:
            print("   STATUS: WRONG - Auto-calculated instead of BOD spec")

    # Check RMUs
    print("\n6. RMU COUNT:")
    print(f"   Expected: {expected_specs['rmu_count']} RMUs (3 per ring A/B)")
    print(f"   Detected: {len(metadata['rmu'])} RMUs")
    if len(metadata['rmu']) == expected_specs['rmu_count']:
        print("   STATUS: OK")
    else:
        print(f"   STATUS: WRONG - Ring topology defaults to 4 RMUs, not {expected_specs['rmu_count']}")

    # Check UPS
    print("\n7. UPS SYSTEMS:")
    print(f"   Expected IT UPS: {expected_specs['it_ups_modules']} x {expected_specs['it_ups_kva']} kVA")
    print(f"   Expected Mech UPS: {expected_specs['mech_ups_modules']} x {expected_specs['mech_ups_kw']} kW")
    print(f"   Detected Total: {len(metadata['ups'])} UPS units")

    it_ups = [u for u in metadata['ups'] if u['function'] == 'IT']
    mech_ups = [u for u in metadata['ups'] if u['function'] == 'MECHANICAL']

    print(f"   Detected IT UPS: {len(it_ups)} units")
    print(f"   Detected Mech UPS: {len(mech_ups)} units")

    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)

    issues = []
    if detected_voltage != expected_specs['mv_voltage']:
        issues.append("CRITICAL: Voltage detection bug (345kV instead of 13.8kV)")
    if len(metadata['generators']) != expected_specs['generators']:
        issues.append(f"Generator count wrong ({len(metadata['generators'])} vs {expected_specs['generators']})")
    if len(metadata['rmu']) != expected_specs['rmu_count']:
        issues.append(f"RMU count wrong ({len(metadata['rmu'])} vs {expected_specs['rmu_count']})")
    if metadata['transformers'] and metadata['transformers'][0]['rated_s'] != expected_specs['transformer_kva']:
        issues.append(f"Transformer sizing wrong ({metadata['transformers'][0]['rated_s']} kVA vs {expected_specs['transformer_kva']} kVA)")

    if issues:
        print("\nISSUES FOUND:")
        for i, issue in enumerate(issues, 1):
            print(f"  {i}. {issue}")
    else:
        print("\nAll specifications match BOD document!")

    print("\nMetadata saved to: pachyderm_metadata.json")
    print("\n" + "=" * 80)

except Exception as e:
    print(f"\nERROR during generation: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
