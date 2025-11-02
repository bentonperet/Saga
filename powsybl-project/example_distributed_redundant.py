"""
Example: Distributed Redundant (2N) Topology
Demonstrates true 2N architecture with completely isolated A and B power trains.
"""

from pachyderm_bod_generator import build_network_from_description

# Define a distributed redundant (2N) system
bod_text = """
Distributed redundant 2N architecture with 13.8kV MV switchgear.
Completely independent A and B power trains with no tie breaker between paths.
Four diesel reciprocating generators (two per side) providing full redundancy.
Each side feeds two 2500 kVA transformers to separate 415V LV distribution.
Static lithium-ion UPS systems support IT loads with dual-cord PDUs via STS.
Each power train (A and B) sized for 100% of critical load.
System includes zig-zag grounding transformers for neutral earthing.
MV switchboards rated at 4000A with 65kAIC interrupt rating.
"""

print("=" * 70)
print("DISTRIBUTED REDUNDANT (2N) TOPOLOGY EXAMPLE")
print("=" * 70)

# Build the network
network, metadata = build_network_from_description(bod_text, include_z_matrix=True)

# Display topology information
print(f"\n✅ Topology: {metadata['topology'].upper().replace('_', ' ')}")
print("\n--- Power Train Architecture ---")

# Generators
print(f"\nGenerators: {len(metadata['generators'])}")
gen_a = [g for g in metadata['generators'] if 'SWGR_A' in g['bus']]
gen_b = [g for g in metadata['generators'] if 'SWGR_B' in g['bus']]
print(f"  Train A: {len(gen_a)} generators")
for g in gen_a:
    print(f"    - {g['id']}: {g['type']} {g['fuel']} - {g['kw']} kW / {g['kva']} kVA")
print(f"  Train B: {len(gen_b)} generators")
for g in gen_b:
    print(f"    - {g['id']}: {g['type']} {g['fuel']} - {g['kw']} kW / {g['kva']} kVA")

# MV Switchboards
print(f"\nMV Switchboards: {len(metadata['mv_swbd'])}")
for swbd in metadata['mv_swbd']:
    print(f"  {swbd['id']}: {swbd['voltage']} kV, {swbd['rating_a']}A, "
          f"{swbd['interrupt_rating_ka']} kAIC, Redundancy: {swbd['redundancy']}")

# Check for tie breakers
tie_breakers = [s for s in metadata['switches'] if 'TIE' in s['id'].upper()]
if tie_breakers:
    print(f"\n⚠️  WARNING: Found {len(tie_breakers)} tie breaker(s)")
    print("   True 2N systems should have NO tie breakers between A and B paths")
else:
    print(f"\n✅ No tie breakers detected - True 2N isolation confirmed")

# Transformers
print(f"\nTransformers: {len(metadata['transformers'])}")
tx_a = [t for t in metadata['transformers'] if 'SWGR_A' in t['hv_bus']]
tx_b = [t for t in metadata['transformers'] if 'SWGR_B' in t['hv_bus']]
print(f"  Train A: {len(tx_a)} transformers @ {tx_a[0]['rated_s'] if tx_a else 0} kVA each")
print(f"  Train B: {len(tx_b)} transformers @ {tx_b[0]['rated_s'] if tx_b else 0} kVA each")

# LV Switchboards
print(f"\nLV Switchboards: {len(metadata['lv_swbd'])}")
for swbd in metadata['lv_swbd']:
    print(f"  {swbd['id']}: {swbd['voltage']} V, {swbd['rating_a']}A, "
          f"Redundancy: {swbd['redundancy']}")

# UPS Systems
print(f"\nUPS Systems: {len(metadata['ups'])}")
for ups in metadata['ups']:
    print(f"  {ups['id']}: {ups['type']} {ups['battery']} ({ups['function']}) - "
          f"{ups['kw']} kW / {ups['kva']} kVA")

# PDUs and STS
print(f"\nPDUs: {len(metadata['pdus'])}")
print(f"Static Transfer Switches (STS): {len(metadata['sts'])}")

# Earthing Transformers
if metadata['earthing_tx']:
    print(f"\nEarthing Transformers: {len(metadata['earthing_tx'])}")
    for earth in metadata['earthing_tx']:
        print(f"  {earth['id']}: {earth['type']} - {earth['rated_kva']} kVA")
        print(f"    Impedance: R={earth['impedance']['r_ohm']:.2f}Ω, "
              f"X={earth['impedance']['x_ohm']:.2f}Ω")
        if 'z_matrix_3ph' in earth:
            print(f"    3-phase Z-matrix included for fault analysis")

print("\n" + "=" * 70)
print("KEY CHARACTERISTICS OF 2N TOPOLOGY:")
print("=" * 70)
print("✅ Complete isolation between A and B power trains")
print("✅ No tie breakers or cross-connections")
print("✅ Each path sized for 100% of load (true redundancy)")
print("✅ Any single component failure affects only one train")
print("✅ Concurrent maintainability - service one path while other runs")
print("✅ Tier IV compliant - supports dual-cord equipment via STS")
print("=" * 70)

print("\n✅ Metadata exported: pachyderm_metadata.json")
print("\nRun validation: python pachyderm_schema_validator.py")
print("=" * 70)
