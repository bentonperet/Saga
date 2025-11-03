"""
PACHYDERM GLOBAL - Data Center Electrical Model Generator
Parses Basis of Design (BOD) text and generates PowSyBl single-line diagrams
with comprehensive metadata for Tier III/IV data center electrical systems.

Features:
- Generator classification (Recip/Turbine, Diesel/Gas)
- UPS classification (Static/Rotary, Li-ion/VRLA/Flywheel, IT/Mechanical)
- Transformer auto-sizing based on load
- RMU (Ring Main Unit) support for ring bus topologies
- MV/LV Switchboard definitions with ratings
- Earthing transformer detection and 3-phase Z-matrix
- STS (Static Transfer Switch) for dual-cord loads
- Parallel generator synchronization
- Topologies: Radial, Dual-feed (A/B), Ring Bus, and Distributed Redundant (2N)
"""

import re
import math
import json
import pypowsybl as pp
try:
    from pypowsybl import diagram
    DIAGRAM_AVAILABLE = True
except ImportError:
    DIAGRAM_AVAILABLE = False
    print("Note: pypowsybl-diagram not available. Diagram generation will be skipped.")
from datetime import datetime


def parse_bod_description(text, include_z_matrix=True):
    """
    Parse Basis of Design text into structured electrical components.
    
    Args:
        text: BOD text description
        include_z_matrix: If True, generate 3x3 impedance matrices for earthing transformers
        
    Returns:
        Dictionary with all parsed components
    """
    elements = {
        "buses": [],
        "generators": [],
        "transformers": [],
        "ups": [],
        "pdus": [],
        "switches": [],
        "sts": [],
        "rmu": [],
        "mv_swbd": [],
        "lv_swbd": [],
        "earthing_tx": [],
        "parallel_groups": [],
        "topology": "radial",
        "include_z_matrix": include_z_matrix
    }
    
    # --- Voltage detection ---
    voltage_match = re.search(r'(\d+(\.\d+)?)\s*kV', text)
    nominal_voltage = float(voltage_match.group(1)) if voltage_match else 13.8
    
    # --- Detect topology ---
    if "ring" in text.lower() or "ring bus" in text.lower():
        elements["topology"] = "ring"
    elif "dual" in text.lower() or "a/b" in text.lower() or "dual-feed" in text.lower():
        elements["topology"] = "dual"
    elif "distributed" in text.lower() or "2n" in text.lower() or "distributed redundant" in text.lower():
        elements["topology"] = "distributed_redundant"
    
    # --- Create MV Buses ---
    if elements["topology"] == "ring":
        for i in range(4):
            elements["buses"].append({"id": f"RING_BUS_{i+1}", "voltage": nominal_voltage})
    elif elements["topology"] == "dual":
        elements["buses"].extend([
            {"id": "SWGR_A", "voltage": nominal_voltage},
            {"id": "SWGR_B", "voltage": nominal_voltage}
        ])
        elements["switches"].append({
            "id": "BUS_TIE",
            "bus1": "SWGR_A",
            "bus2": "SWGR_B",
            "kind": "BREAKER",
            "open": False
        })
    elif elements["topology"] == "distributed_redundant":
        # 2N architecture: completely independent A and B power trains
        elements["buses"].extend([
            {"id": "SWGR_A", "voltage": nominal_voltage},
            {"id": "SWGR_B", "voltage": nominal_voltage}
        ])
        # No tie breaker in true 2N - completely isolated paths
    else:
        elements["buses"].append({"id": "MAIN_SWGR", "voltage": nominal_voltage})
    
    # --- Generator Detection and Classification ---
    gen_count = len(re.findall(r'generator', text.lower())) or 4
    paralleled = any(k in text.lower() for k in ["paralleled", "parallel", "sync", "common bus"])
    
    for i in range(gen_count):
        g_type = "RECIP"
        fuel = "DIESEL"
        rating_kw = 2000
        rating_kva = 2500
        
        if "turbine" in text.lower() or "gas turbine" in text.lower():
            g_type = "TURBINE"
            fuel = "GAS"
            rating_kw = 10000
            rating_kva = 12500
        elif "natural gas" in text.lower() or "nat gas" in text.lower():
            fuel = "NAT_GAS"
        elif "biodiesel" in text.lower():
            fuel = "BIODIESEL"
        
        bus_target = (
            f"RING_BUS_{(i % 4) + 1}" if elements["topology"] == "ring"
            else "SWGR_A" if i % 2 == 0 and elements["topology"] in ["dual", "distributed_redundant"]
            else "SWGR_B" if elements["topology"] in ["dual", "distributed_redundant"]
            else "MAIN_SWGR"
        )
        
        elements["generators"].append({
            "id": f"GEN_{i+1}",
            "bus": bus_target,
            "type": g_type,
            "fuel": fuel,
            "kw": rating_kw,
            "kva": rating_kva
        })
    
    # Handle parallel generators
    if paralleled:
        elements["buses"].append({"id": "SYNC_BUS", "voltage": nominal_voltage})
        for g in elements["generators"]:
            elements["switches"].append({
                "id": f"{g['id']}_SYNC",
                "bus1": g["bus"],
                "bus2": "SYNC_BUS",
                "kind": "BREAKER",
                "open": False
            })
    
    # --- MV Switchboard Detection ---
    if "mv switchboard" in text.lower() or "mv switchgear" in text.lower() or elements["topology"] != "radial":
        if elements["topology"] in ["dual", "distributed_redundant"]:
            for section in ["A", "B"]:
                elements["mv_swbd"].append({
                    "id": f"MV_SWBD_{section}",
                    "voltage": nominal_voltage,
                    "rating_a": 4000,
                    "interrupt_rating_ka": 65,
                    "redundancy": "2N" if elements["topology"] == "distributed_redundant" else section,
                    "feeds": []
                })
        else:
            elements["mv_swbd"].append({
                "id": "MV_SWBD_A",
                "voltage": nominal_voltage,
                "rating_a": 4000,
                "interrupt_rating_ka": 65,
                "redundancy": "N+1",
                "feeds": []
            })
    
    # --- RMU Detection (Ring Main Units) ---
    if "rmu" in text.lower() or "ring main" in text.lower() or elements["topology"] == "ring":
        rmu_count = 4 if elements["topology"] == "ring" else 2
        for i in range(rmu_count):
            rmu_id = f"RMU_{i+1}"
            elements["rmu"].append(rmu_id)
            elements["buses"].append({"id": f"{rmu_id}_BUS", "voltage": nominal_voltage})
            
            # RMU switches: IN, OUT, FEEDER
            if elements["topology"] == "ring":
                elements["switches"].extend([
                    {"id": f"{rmu_id}_IN", "bus1": f"RING_BUS_{i+1}",
                     "bus2": f"{rmu_id}_BUS", "kind": "DISCONNECTOR", "open": False},
                    {"id": f"{rmu_id}_OUT", "bus1": f"{rmu_id}_BUS",
                     "bus2": f"RING_BUS_{1 if i == 3 else i+2}", "kind": "DISCONNECTOR", "open": False}
                ])
    
    # --- Transformer Sizing ---
    pdu_count = len(re.findall(r'pdu|rpp', text.lower())) or 8
    total_load_kw = pdu_count * 100  # 100 kW per PDU
    efficiency = 0.97
    pf = 0.9
    xfmr_count = len(elements["rmu"]) or 4
    load_per_tx = total_load_kw / xfmr_count
    tx_kva = math.ceil((load_per_tx / (efficiency * pf)) / 100) * 100
    
    for i in range(xfmr_count):
        hv_bus = f"RMU_{i+1}_BUS" if elements["rmu"] else (
            "SWGR_A" if i % 2 == 0 and elements["topology"] in ["dual", "distributed_redundant"]
            else "SWGR_B" if elements["topology"] in ["dual", "distributed_redundant"]
            else "MAIN_SWGR"
        )
        lv_bus = f"LV_BUS_{i+1}"
        elements["buses"].append({"id": lv_bus, "voltage": 0.415})
        elements["transformers"].append({
            "id": f"TX_{i+1}",
            "hv_bus": hv_bus,
            "lv_bus": lv_bus,
            "hv_voltage": nominal_voltage,
            "lv_voltage": 0.415,
            "rated_s": tx_kva
        })
    
    # --- LV Switchboard Creation ---
    for i in range(xfmr_count):
        redundancy_type = (
            "2N" if elements["topology"] == "distributed_redundant"
            else "A/B" if elements["topology"] in ["dual", "ring"]
            else "N+1"
        )
        elements["lv_swbd"].append({
            "id": f"LV_SWBD_{i+1}",
            "voltage": 0.415,
            "rating_a": 3200,
            "interrupt_rating_ka": 65,
            "redundancy": redundancy_type,
            "feeds": []
        })
    
    # --- UPS Detection (type, battery, function) ---
    ups_count = len(re.findall(r'ups', text.lower())) or xfmr_count
    
    for i in range(ups_count):
        lv_bus = f"LV_BUS_{(i % xfmr_count) + 1}"
        ups_type = "STATIC"
        battery = "VRLA"
        function = "IT"
        kw = 500
        kva = 550
        
        # Detect UPS type
        if "rotary" in text.lower() or "flywheel" in text.lower():
            ups_type = "ROTARY"
            battery = "FLYWHEEL"
        
        # Detect battery type
        if "lithium" in text.lower() or "li-ion" in text.lower():
            battery = "LI-ION"
        elif "nicd" in text.lower() or "nicad" in text.lower():
            battery = "NICD"
        
        # Detect function
        if "mechanical" in text.lower() or "fan" in text.lower() or "pump" in text.lower():
            function = "MECHANICAL"
        elif "control" in text.lower():
            function = "CONTROL"
        
        elements["ups"].append({
            "id": f"UPS_{i+1}",
            "bus": lv_bus,
            "type": ups_type,
            "battery": battery,
            "function": function,
            "kw": kw,
            "kva": kva
        })
    
    # --- PDUs and STS ---
    for i in range(pdu_count):
        a_source = f"UPS_{(i % ups_count) + 1}"
        b_source = f"UPS_{((i + 1) % ups_count) + 1}"
        
        elements["pdus"].append({"id": f"PDU_{i+1}"})
        
        if elements["topology"] != "radial":
            elements["sts"].append({
                "id": f"STS_{i+1}",
                "source_a": a_source,
                "source_b": b_source,
                "load": f"PDU_{i+1}"
            })
    
    # --- Earthing Transformer Detection ---
    if any(term in text.lower() for term in ["zig-zag", "zigzag", "grounding transformer", "earthing", "ngr"]):
        earth_type = "ZIG-ZAG"
        neutral_r = 10.0
        neutral_x = 2.0
        
        if "wye-delta" in text.lower() or "auxiliary isolation" in text.lower():
            earth_type = "WYE-DELTA"
            neutral_r = 0.0
            neutral_x = 0.0
        elif "ngr" in text.lower() or "neutral grounding resistor" in text.lower():
            earth_type = "RESISTOR-GROUNDED"
            neutral_r = 15.0
            neutral_x = 3.0
        
        # Auto-scale earthing transformer
        total_tx_kva = sum(t["rated_s"] for t in elements["transformers"])
        earth_kva = math.ceil(total_tx_kva * 0.01)
        
        # Scale impedance
        scale_factor = math.sqrt(total_tx_kva / 10000)
        r_scaled = neutral_r * scale_factor
        x_scaled = neutral_x * scale_factor
        r_mutual = 0.2 * r_scaled
        x_mutual = 0.05 * r_scaled
        
        earth_tx = {
            "id": "EARTH_TX_1",
            "type": earth_type,
            "rated_kva": earth_kva,
            "impedance": {"r_ohm": r_scaled, "x_ohm": x_scaled},
            "neutral_resistance_ohm": neutral_r,
            "connected_bus": elements["buses"][0]["id"],
            "grounding_connection": {
                "type": "RESISTIVE" if earth_type != "WYE-DELTA" else "SOLID",
                "neutral_to_ground_path": f"{neutral_r} Ω NGR" if earth_type != "WYE-DELTA" else "Direct",
                "connection_impedance": f"Z = {r_scaled:.1f} + j{x_scaled:.1f} Ω",
                "ground_bus": "EARTH"
            }
        }
        
        # Add 3x3 Z-matrix if requested
        if include_z_matrix:
            earth_tx["z_matrix_3ph"] = [
                [f"{r_scaled:.1f} + j{x_scaled:.1f}", f"{r_mutual:.1f} + j{x_mutual:.1f}", f"{r_mutual:.1f} + j{x_mutual:.1f}"],
                [f"{r_mutual:.1f} + j{x_mutual:.1f}", f"{r_scaled:.1f} + j{x_scaled:.1f}", f"{r_mutual:.1f} + j{x_mutual:.1f}"],
                [f"{r_mutual:.1f} + j{x_mutual:.1f}", f"{r_mutual:.1f} + j{x_mutual:.1f}", f"{r_scaled:.1f} + j{x_scaled:.1f}"]
            ]
        
        elements["earthing_tx"].append(earth_tx)
    
    return elements


def build_network_from_description(text, include_z_matrix=True):
    """
    Build PowSyBl network from BOD text description.
    
    Args:
        text: BOD text description
        include_z_matrix: If True, include 3x3 impedance matrices in metadata
        
    Returns:
        Tuple of (network, metadata_dict)
    """
    data = parse_bod_description(text, include_z_matrix)
    net = pp.network.create_empty("PACHYDERM_TierIV")
    
    # Create all buses
    bus_map = {}
    for b in data["buses"]:
        bus_map[b["id"]] = net.create_voltage_level(
            id=b["id"],
            topology_kind='BUS_BREAKER',
            nominal_v=b["voltage"]
        )
        net.create_buses(id=[f"{b['id']}_BUS"], voltage_level_id=[b["id"]])
        bus_map[f"{b['id']}_BUS"] = f"{b['id']}_BUS"
    
    # Generators
    for g in data["generators"]:
        label = f"{g['id']} – {g['type']} {g['fuel']} – {g['kw']} kW / {g['kva']} kVA"
        try:
            net.create_generators(
                id=[g["id"]],
                voltage_level_id=[g["bus"]],
                bus_id=[f"{g['bus']}_BUS"],
                max_p=[g["kw"]/1000],
                min_p=[0],
                target_p=[(g["kw"]/1000)*0.8],
                target_v=[g.get("target_v", 13.8)],
                voltage_regulator_on=[True]
            )
        except Exception as e:
            print(f"Warning: Could not create generator {g['id']}: {e}")
    
    # Transformers
    for t in data["transformers"]:
        label = f"{t['id']} – {t['rated_s']} kVA"
        try:
            net.create_2_windings_transformers(
                id=[t["id"]],
                voltage_level1_id=[t["hv_bus"]],
                bus1_id=[f"{t['hv_bus']}_BUS"],
                voltage_level2_id=[t["lv_bus"]],
                bus2_id=[f"{t['lv_bus']}_BUS"],
                r=[0.5],
                x=[5.0],
                g=[0],
                b=[0],
                rated_u1=[t["hv_voltage"]],
                rated_u2=[t["lv_voltage"]],
                rated_s=[t["rated_s"]]
            )
        except Exception as e:
            print(f"Warning: Could not create transformer {t['id']}: {e}")
    
    # UPS (modeled as generators)
    for u in data["ups"]:
        label = f"{u['id']} – {u['type']} {u['battery']} ({u['function']}) – {u['kw']} kW / {u['kva']} kVA"
        try:
            net.create_generators(
                id=[u["id"]],
                voltage_level_id=[u["bus"]],
                bus_id=[f"{u['bus']}_BUS"],
                max_p=[u["kw"]/1000],
                min_p=[0],
                target_p=[(u["kw"]/1000)*0.8],
                target_v=[0.415],
                voltage_regulator_on=[False]
            )
        except Exception as e:
            print(f"Warning: Could not create UPS {u['id']}: {e}")
    
    # PDUs (modeled as loads)
    for p in data["pdus"]:
        # Find associated UPS from STS
        sts_entry = next((s for s in data["sts"] if s["load"] == p["id"]), None)
        if sts_entry:
            ups_id = sts_entry["source_a"]
            ups_entry = next(u for u in data["ups"] if u["id"] == ups_id)
            bus_id = f"{ups_entry['bus']}_BUS"
            voltage_level = ups_entry['bus']
        else:
            continue
        
        try:
            net.create_loads(
                id=[p["id"]],
                voltage_level_id=[voltage_level],
                bus_id=[bus_id],
                p0=[0.4],
                q0=[0.0]
            )
        except Exception as e:
            print(f"Warning: Could not create PDU {p['id']}: {e}")
    
    # Export metadata
    metadata_file = "pachyderm_metadata.json"
    with open(metadata_file, "w") as f:
        json.dump(data, f, indent=2)
    
    return net, data


def generate_diagram(network, metadata, title="PACHYDERM GLOBAL – Tier IV Data Center"):
    """
    Generate SVG single-line diagram with compact labels.
    
    Args:
        network: PowSyBl network object
        metadata: Parsed metadata dictionary
        title: Diagram title
        
    Returns:
        SVG string
    """
    try:
        # Generate network diagram using PowSyBl diagram library
        # Note: The diagram library may have different API depending on version
        svg_content = diagram.draw_network(
            network,
            title=title
        )
        return svg_content
    except Exception as e:
        print(f"Note: Diagram generation requires pypowsybl-diagram. Error: {e}")
        return None


def main():
    """Example usage of the PACHYDERM BOD generator."""
    
    bod_text = """
    13.8kV ring bus architecture with four diesel reciprocating generators and RMUs at each node.
    Static lithium-ion UPS systems support IT loads, while rotary flywheel UPS units support 
    mechanical cooling fans and pumps. All PDUs are dual-corded through STS connections.
    System includes zig-zag grounding transformers for neutral earthing.
    MV switchboards rated at 4000A with 65kAIC interrupt rating feed step-down transformers 
    to 415V LV switchboards with A/B redundancy.
    """
    
    print("=" * 70)
    print("PACHYDERM GLOBAL - Data Center Electrical Model Generator")
    print("=" * 70)
    print("\nParsing Basis of Design text...")
    
    # Build network
    network, metadata = build_network_from_description(bod_text, include_z_matrix=True)
    
    print(f"\n✅ Network created: {network.id}")
    print(f"   - Generators: {len(metadata['generators'])}")
    print(f"   - Transformers: {len(metadata['transformers'])}")
    print(f"   - UPS Systems: {len(metadata['ups'])}")
    print(f"   - PDUs: {len(metadata['pdus'])}")
    print(f"   - RMUs: {len(metadata['rmu'])}")
    print(f"   - MV Switchboards: {len(metadata['mv_swbd'])}")
    print(f"   - LV Switchboards: {len(metadata['lv_swbd'])}")
    print(f"   - Earthing Transformers: {len(metadata['earthing_tx'])}")
    print(f"   - Topology: {metadata['topology'].upper()}")
    
    # Generate diagram
    print("\nGenerating single-line diagram...")
    svg_data = generate_diagram(network, metadata)
    
    if svg_data:
        with open("pachyderm_tierIV_detailed.svg", "w", encoding="utf-8") as f:
            f.write(svg_data)
        print("✅ Diagram saved: pachyderm_tierIV_detailed.svg")
    
    print("✅ Metadata exported: pachyderm_metadata.json")
    print("\n" + "=" * 70)
    print("Generation complete!")
    print("=" * 70)


if __name__ == "__main__":
    main()
