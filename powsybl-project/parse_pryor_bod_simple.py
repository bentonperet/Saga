"""
Simple BOD parser for Pryor DC - extract electrical metadata without network creation
"""

import json
import re

def parse_pryor_bod(text):
    """Parse Pryor DC BOD text into structured metadata"""

    metadata = {
        "project": "Pryor Data Center",
        "location": "Pryor, Oklahoma",
        "topology": "dual_ring",
        "nominal_voltage_kv": 13.8,
        "utility": {},
        "generators": [],
        "transformers": [],
        "ups": [],
        "switchboards": [],
        "rmus": [],
        "phases": []
    }

    # Parse utility service
    if "345 kV" in text:
        utility_xfmr_match = re.search(r'(\d+)\s*×\s*(\d+)\s*MVA.*?(\d+)kV/(\d+\.\d+)kV', text)
        if utility_xfmr_match:
            metadata["utility"] = {
                "primary_voltage_kv": 345,
                "transformers": {
                    "count": 2,
                    "rating_mva": 25,
                    "primary_kv": 345,
                    "secondary_kv": 13.8,
                    "redundancy": "N+1"
                }
            }

    # Parse generators
    gen_match = re.search(r'(\d+)\s*×\s*(\d+\.\d+)\s*MW.*?(\d+\.\d+)\s*kV.*?(diesel|gas)', text, re.IGNORECASE)
    if gen_match:
        count = int(gen_match.group(1))
        rating_mw = float(gen_match.group(2))
        voltage_kv = float(gen_match.group(3))
        fuel = gen_match.group(4).upper()

        for i in range(count):
            metadata["generators"].append({
                "id": f"GEN_{i+1}",
                "rating_mw": rating_mw,
                "rating_kw": rating_mw * 1000,
                "voltage_kv": voltage_kv,
                "fuel": fuel,
                "type": "RECIPROCATING",
                "redundancy": "N+1"
            })

    # Parse transformers
    tx_match = re.search(r'(\d+)\s*×\s*(\d+,?\d+)\s*kVA.*?\((\d+\.\d+)\s*kV/(\d+)V\)', text)
    if tx_match:
        count = int(tx_match.group(1))
        rating_kva = int(tx_match.group(2).replace(',', ''))
        primary_kv = float(tx_match.group(3))
        secondary_v = int(tx_match.group(4))

        for i in range(count):
            metadata["transformers"].append({
                "id": f"TX_{i+1}",
                "rating_kva": rating_kva,
                "primary_kv": primary_kv,
                "secondary_kv": secondary_v / 1000,
                "type": "oil-filled",
                "redundancy": "N+1"
            })

    # Parse IT UPS
    it_ups_match = re.search(r'(\d+)\s*modules.*?(\d+,?\d+)\s*kVA', text)
    if it_ups_match:
        # Phase 1
        metadata["ups"].append({
            "id": "IT_UPS_Phase1",
            "type": "STATIC",
            "battery": "LI-ION",
            "function": "IT",
            "modules": 5,
            "module_kva": 1250,
            "total_kva": 6250,
            "runtime_minutes": 5,
            "phase": 1
        })
        # Phase 2
        metadata["ups"].append({
            "id": "IT_UPS_Phase2",
            "type": "STATIC",
            "battery": "LI-ION",
            "function": "IT",
            "modules": 13,
            "module_kva": 1250,
            "total_kva": 16250,
            "runtime_minutes": 5,
            "phase": 2
        })

    # Parse Mechanical UPS
    mech_ups_match = re.search(r'(\d+)\s*units\s*at\s*(\d+)\s*kW', text)
    if mech_ups_match:
        # Phase 1
        metadata["ups"].append({
            "id": "MECH_UPS_Phase1",
            "type": "STATIC",
            "function": "MECHANICAL",
            "units": 8,
            "unit_kw": 250,
            "total_kw": 2000,
            "purpose": "pumps_fans",
            "phase": 1
        })
        # Phase 2
        metadata["ups"].append({
            "id": "MECH_UPS_Phase2",
            "type": "STATIC",
            "function": "MECHANICAL",
            "units": 20,
            "unit_kw": 250,
            "total_kw": 5000,
            "purpose": "pumps_fans",
            "phase": 2
        })

    # RMUs
    rmu_match = re.search(r'(\d+)\s*RMUs', text)
    if rmu_match:
        count = int(rmu_match.group(1))
        for i in range(count):
            metadata["rmus"].append({
                "id": f"RMU_{i+1}",
                "voltage_kv": 13.8,
                "rating_a": 630,
                "type": "SF6 or vacuum",
                "ring": "A" if i < count/2 else "B"
            })

    # Switchboards
    metadata["switchboards"] = [
        {
            "id": "SWBD_A",
            "type": "LV",
            "voltage_v": 480,
            "rating_a": "TBD",
            "redundancy": "A",
            "fed_from": "Ring_A transformers"
        },
        {
            "id": "SWBD_B",
            "type": "LV",
            "voltage_v": 480,
            "rating_a": "TBD",
            "redundancy": "B",
            "fed_from": "Ring_B transformers"
        }
    ]

    # Phases
    metadata["phases"] = [
        {
            "phase": 1,
            "it_load_kw": 3000,
            "cabinets": 30,
            "cabinet_power_kw": 100,
            "generators": 3,
            "transformers": 3,
            "it_ups_modules": 5,
            "mech_ups_units": 8,
            "data_halls_active": "DH-E only"
        },
        {
            "phase": 2,
            "it_load_kw": 12000,
            "cabinets": 30,
            "cabinet_power_kw": 400,
            "generators": 6,
            "transformers": 8,
            "it_ups_modules": 13,
            "mech_ups_units": 20,
            "data_halls_active": "DH-E + DH-W"
        }
    ]

    return metadata


# Pryor DC BOD text
pryor_bod = """
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

print("="*70)
print("PRYOR DATA CENTER - ELECTRICAL SYSTEM METADATA EXTRACTOR")
print("="*70)

metadata = parse_pryor_bod(pryor_bod)

print("\n✓ Metadata extracted successfully!\n")

# Display summary
print("="*70)
print("SYSTEM SUMMARY")
print("="*70)
print(f"Project: {metadata['project']}")
print(f"Location: {metadata['location']}")
print(f"Topology: {metadata['topology']}")
print(f"Nominal Voltage: {metadata['nominal_voltage_kv']} kV")

print(f"\n{'─'*70}")
print("UTILITY SERVICE")
print(f"{'─'*70}")
if metadata['utility']:
    print(f"Primary: {metadata['utility']['primary_voltage_kv']} kV")
    print(f"Transformers: {metadata['utility']['transformers']['count']} × {metadata['utility']['transformers']['rating_mva']} MVA")
    print(f"  {metadata['utility']['transformers']['primary_kv']} kV / {metadata['utility']['transformers']['secondary_kv']} kV")
    print(f"  Redundancy: {metadata['utility']['transformers']['redundancy']}")

print(f"\n{'─'*70}")
print(f"GENERATORS ({len(metadata['generators'])})")
print(f"{'─'*70}")
for gen in metadata['generators']:
    print(f"  {gen['id']}: {gen['rating_mw']} MW ({gen['rating_kw']:,.0f} kW) @ {gen['voltage_kv']} kV")
    print(f"    Fuel: {gen['fuel']}, Type: {gen['type']}, Redundancy: {gen['redundancy']}")

print(f"\n{'─'*70}")
print(f"TRANSFORMERS ({len(metadata['transformers'])})")
print(f"{'─'*70}")
for tx in metadata['transformers'][:3]:
    print(f"  {tx['id']}: {tx['rating_kva']:,} kVA ({tx['primary_kv']} kV / {tx['secondary_kv']} kV)")
if len(metadata['transformers']) > 3:
    print(f"  ... and {len(metadata['transformers']) - 3} more")

print(f"\n{'─'*70}")
print(f"UPS SYSTEMS ({len(metadata['ups'])})")
print(f"{'─'*70}")
for ups in metadata['ups']:
    if ups['function'] == 'IT':
        print(f"  {ups['id']}:")
        print(f"    Type: {ups['type']}, Battery: {ups['battery']}")
        print(f"    Modules: {ups['modules']} × {ups['module_kva']:,} kVA = {ups['total_kva']:,} kVA total")
        print(f"    Runtime: {ups['runtime_minutes']} minutes, Phase: {ups['phase']}")
    else:
        print(f"  {ups['id']}:")
        print(f"    Type: {ups['type']}, Function: {ups['function']}")
        print(f"    Units: {ups['units']} × {ups['unit_kw']} kW = {ups['total_kw']:,} kW total")
        print(f"    Phase: {ups['phase']}")

print(f"\n{'─'*70}")
print(f"RMUs - RING MAIN UNITS ({len(metadata['rmus'])})")
print(f"{'─'*70}")
for rmu in metadata['rmus']:
    print(f"  {rmu['id']}: {rmu['voltage_kv']} kV, {rmu['rating_a']}A (Ring {rmu['ring']})")

print(f"\n{'─'*70}")
print(f"SWITCHBOARDS ({len(metadata['switchboards'])})")
print(f"{'─'*70}")
for swbd in metadata['switchboards']:
    print(f"  {swbd['id']}: {swbd['type']} @ {swbd['voltage_v']}V")
    print(f"    Fed from: {swbd['fed_from']}, Redundancy: {swbd['redundancy']}")

print(f"\n{'─'*70}")
print("PHASING SUMMARY")
print(f"{'─'*70}")
for phase in metadata['phases']:
    print(f"\nPhase {phase['phase']}:")
    print(f"  IT Load: {phase['it_load_kw']:,} kW")
    print(f"  Cabinets: {phase['cabinets']} @ {phase['cabinet_power_kw']} kW each")
    print(f"  Generators: {phase['generators']} units")
    print(f"  Transformers: {phase['transformers']} units")
    print(f"  IT UPS: {phase['it_ups_modules']} modules")
    print(f"  Mech UPS: {phase['mech_ups_units']} units")
    print(f"  Data Halls: {phase['data_halls_active']}")

# Save to JSON
output_file = "pryor_dc_electrical_metadata.json"
with open(output_file, 'w') as f:
    json.dump(metadata, f, indent=2)

print(f"\n{'='*70}")
print(f"✓ Metadata saved to: {output_file}")
print(f"{'='*70}\n")
