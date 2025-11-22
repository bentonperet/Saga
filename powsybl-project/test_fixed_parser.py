"""
Test the FIXED parser against actual Saga Pryor BOD
Compare results with expected specifications
"""

import sys
from pathlib import Path
from pachyderm_bod_generator_fixed import build_network_from_description
import json

# Read the actual BOD file
bod_file = Path(r"C:\Users\eriks\Documents\Obsidian\Saga Pryor DC\Basis of Design\7BOD - Electrical (CSI Div 26).md")

print("=" * 80)
print("TESTING FIXED PARSER - Saga Pryor BOD")
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

    # Component summary
    print("\n" + "=" * 80)
    print("COMPONENT SUMMARY (FIXED PARSER)")
    print("=" * 80)

    print(f"\nGenerators: {len(metadata['generators'])}")
    if metadata['generators']:
        print(f"  Sample: {metadata['generators'][0]['id']}")
        print(f"    Type: {metadata['generators'][0]['type']}")
        print(f"    Fuel: {metadata['generators'][0]['fuel']}")
        print(f"    Rating: {metadata['generators'][0]['kw']} kW / {metadata['generators'][0]['kva']} kVA")

    print(f"\nTransformers: {len(metadata['transformers'])}")
    if metadata['transformers']:
        print(f"  Sample: {metadata['transformers'][0]['id']}")
        print(f"    Rating: {metadata['transformers'][0]['rated_s']} kVA")
        print(f"    Voltages: {metadata['transformers'][0]['hv_voltage']} kV -> {metadata['transformers'][0]['lv_voltage']} kV")

    print(f"\nRMUs: {len(metadata['rmu'])}")
    print(f"\nMV Switchboards: {len(metadata['mv_swbd'])}")
    print(f"\nLV Switchboards: {len(metadata['lv_swbd'])}")

    print(f"\nUPS Systems: {len(metadata['ups'])}")
    it_ups = [u for u in metadata['ups'] if u['function'] == 'IT']
    mech_ups = [u for u in metadata['ups'] if u['function'] == 'MECHANICAL']
    print(f"  IT UPS: {len(it_ups)}")
    print(f"  Mechanical UPS: {len(mech_ups)}")

    if it_ups:
        print(f"  IT UPS Sample: {it_ups[0]['id']}")
        print(f"    Rating: {it_ups[0]['kw']} kW / {it_ups[0]['kva']} kVA")
        print(f"    Battery: {it_ups[0]['battery']}")

    if mech_ups:
        print(f"  Mech UPS Sample: {mech_ups[0]['id']}")
        print(f"    Rating: {mech_ups[0]['kw']} kW / {mech_ups[0]['kva']} kVA")

    print(f"\nPDUs: {len(metadata['pdus'])}")

    # VALIDATION AGAINST ACTUAL BOD SPECS
    print("\n" + "=" * 80)
    print("VALIDATION AGAINST BOD SPECIFICATIONS")
    print("=" * 80)

    # Expected from BOD (Phase 1 or total)
    expected_specs = {
        'mv_voltage': 13.8,
        'generators': 6,  # Total Phase 1+2
        'generator_kw': 4000,
        'generator_fuel': 'DIESEL',
        'transformers': 8,  # Total Phase 1+2
        'transformer_kva': 3500,
        'rmu_count': 6,  # 3 per ring
        'it_ups_modules_p1': 5,  # Phase 1
        'it_ups_kva': 1250,
        'mech_ups_modules_p1': 8,  # Phase 1
        'mech_ups_kw': 250
    }

    passed = 0
    failed = 0

    # Check voltage
    print("\n1. VOLTAGE DETECTION:")
    detected_voltage = metadata['buses'][0]['voltage'] if metadata['buses'] else None
    print(f"   Expected: {expected_specs['mv_voltage']} kV")
    print(f"   Detected: {detected_voltage} kV")
    if abs(detected_voltage - expected_specs['mv_voltage']) < 0.1:
        print("   [PASS]")
        passed += 1
    else:
        print("   [FAIL]")
        failed += 1

    # Check generators
    print("\n2. GENERATOR COUNT:")
    print(f"   Expected: {expected_specs['generators']}")
    print(f"   Detected: {len(metadata['generators'])}")
    if len(metadata['generators']) == expected_specs['generators']:
        print("   [PASS]")
        passed += 1
    else:
        print(f"   [FAIL] - Off by {abs(len(metadata['generators']) - expected_specs['generators'])}")
        failed += 1

    print("\n3. GENERATOR RATINGS:")
    print(f"   Expected: {expected_specs['generator_kw']} kW each")
    if metadata['generators']:
        actual_kw = metadata['generators'][0]['kw']
        print(f"   Detected: {actual_kw} kW each")
        if actual_kw == expected_specs['generator_kw']:
            print("   [PASS]")
            passed += 1
        else:
            print(f"   [FAIL] - Off by {abs(actual_kw - expected_specs['generator_kw'])} kW")
            failed += 1
    else:
        print("   [FAIL] - No generators detected")
        failed += 1

    print("\n4. GENERATOR FUEL TYPE:")
    print(f"   Expected: {expected_specs['generator_fuel']}")
    if metadata['generators']:
        actual_fuel = metadata['generators'][0]['fuel']
        print(f"   Detected: {actual_fuel}")
        if actual_fuel == expected_specs['generator_fuel']:
            print("   [PASS]")
            passed += 1
        else:
            print("   [FAIL]")
            failed += 1
    else:
        print("   [FAIL] - No generators detected")
        failed += 1

    # Check transformers
    print("\n5. TRANSFORMER COUNT:")
    print(f"   Expected: {expected_specs['transformers']} (total for Phase 1+2)")
    print(f"   Detected: {len(metadata['transformers'])}")
    if len(metadata['transformers']) == expected_specs['transformers']:
        print("   [PASS]")
        passed += 1
    else:
        print(f"   [FAIL] - Off by {abs(len(metadata['transformers']) - expected_specs['transformers'])}")
        failed += 1

    print("\n6. TRANSFORMER RATINGS:")
    print(f"   Expected: {expected_specs['transformer_kva']} kVA each")
    if metadata['transformers']:
        actual_kva = metadata['transformers'][0]['rated_s']
        print(f"   Detected: {actual_kva} kVA each")
        if actual_kva == expected_specs['transformer_kva']:
            print("   [PASS]")
            passed += 1
        else:
            print(f"   [FAIL] - Off by {abs(actual_kva - expected_specs['transformer_kva'])} kVA")
            failed += 1
    else:
        print("   [FAIL] - No transformers detected")
        failed += 1

    # Check RMUs
    print("\n7. RMU COUNT:")
    print(f"   Expected: {expected_specs['rmu_count']} (3 per ring A/B)")
    print(f"   Detected: {len(metadata['rmu'])}")
    if len(metadata['rmu']) == expected_specs['rmu_count']:
        print("   [PASS]")
        passed += 1
    else:
        print(f"   [FAIL] - Off by {abs(len(metadata['rmu']) - expected_specs['rmu_count'])}")
        failed += 1

    # Check UPS
    print("\n8. IT UPS COUNT:")
    print(f"   Expected (Phase 1): {expected_specs['it_ups_modules_p1']} modules")
    print(f"   Detected: {len(it_ups)} modules")
    if len(it_ups) == expected_specs['it_ups_modules_p1']:
        print("   [PASS]")
        passed += 1
    else:
        print(f"   [FAIL] - Off by {abs(len(it_ups) - expected_specs['it_ups_modules_p1'])}")
        failed += 1

    print("\n9. IT UPS RATINGS:")
    print(f"   Expected: {expected_specs['it_ups_kva']} kVA per module")
    if it_ups:
        actual_kva = it_ups[0]['kva']
        print(f"   Detected: {actual_kva} kVA per module")
        if actual_kva == expected_specs['it_ups_kva']:
            print("   [PASS]")
            passed += 1
        else:
            print(f"   [FAIL] - Off by {abs(actual_kva - expected_specs['it_ups_kva'])} kVA")
            failed += 1
    else:
        print("   [FAIL] - No IT UPS detected")
        failed += 1

    print("\n10. MECHANICAL UPS COUNT:")
    print(f"   Expected (Phase 1): {expected_specs['mech_ups_modules_p1']} modules")
    print(f"   Detected: {len(mech_ups)} modules")
    if len(mech_ups) == expected_specs['mech_ups_modules_p1']:
        print("   [PASS]")
        passed += 1
    else:
        print(f"   [FAIL] - Off by {abs(len(mech_ups) - expected_specs['mech_ups_modules_p1'])}")
        failed += 1

    print("\n11. MECHANICAL UPS RATINGS:")
    print(f"   Expected: {expected_specs['mech_ups_kw']} kW per module")
    if mech_ups:
        actual_kw = mech_ups[0]['kw']
        print(f"   Detected: {actual_kw} kW per module")
        if actual_kw == expected_specs['mech_ups_kw']:
            print("   [PASS]")
            passed += 1
        else:
            print(f"   [FAIL] - Off by {abs(actual_kw - expected_specs['mech_ups_kw'])} kW")
            failed += 1
    else:
        print("   [FAIL] - No Mechanical UPS detected")
        failed += 1

    # Summary
    print("\n" + "=" * 80)
    print("TEST SUMMARY")
    print("=" * 80)

    total_tests = passed + failed
    accuracy = (passed / total_tests * 100) if total_tests > 0 else 0

    print(f"\nTests Passed: {passed}/{total_tests}")
    print(f"Tests Failed: {failed}/{total_tests}")
    print(f"Accuracy: {accuracy:.1f}%")

    if accuracy >= 90:
        print("\nSTATUS: EXCELLENT - Parser working correctly!")
    elif accuracy >= 70:
        print("\nSTATUS: GOOD - Minor issues remaining")
    elif accuracy >= 50:
        print("\nSTATUS: FAIR - Significant improvements made")
    else:
        print("\nSTATUS: POOR - Major issues remain")

    # Run validation
    print("\n" + "=" * 80)
    print("RUNNING SEMANTIC VALIDATION")
    print("=" * 80)

    from pachyderm_schema_validator_fixed import validate_metadata

    is_valid, alerts = validate_metadata("pachyderm_metadata.json")

    if alerts:
        print(f"\nValidation found {len(alerts)} alert(s):")
        errors = [a for a in alerts if a.severity == "ERROR"]
        warnings = [a for a in alerts if a.severity == "WARNING"]
        infos = [a for a in alerts if a.severity == "INFO"]

        print(f"  Errors: {len(errors)}")
        print(f"  Warnings: {len(warnings)}")
        print(f"  Info: {len(infos)}")

        if warnings:
            print("\nSample warnings:")
            for alert in warnings[:3]:
                print(f"  - [{alert.component}] {alert.message}")
    else:
        print("\nNo validation issues found!")

    print("\n" + "=" * 80)
    print("TEST COMPLETE")
    print("=" * 80)

except Exception as e:
    print(f"\nERROR during generation: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
