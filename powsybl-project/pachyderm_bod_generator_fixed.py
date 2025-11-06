"""
PACHYDERM GLOBAL - Data Center Electrical Model Generator (FIXED)
Parses Basis of Design (BOD) text and generates PowSyBl single-line diagrams
with comprehensive metadata for Tier III/IV data center electrical systems.

FIXES IMPLEMENTED:
- Proper specification extraction (not word counting)
- Section-aware parsing
- Correct generator, transformer, UPS, RMU specifications
- PowSyBl substation hierarchy
- Reactive power handling for UPS
"""

import re
import math
import json
import pypowsybl as pp
from datetime import datetime
from typing import Dict, Any, Tuple, List

# Try to import diagram module (optional)
try:
    from pypowsybl import diagram
    DIAGRAM_AVAILABLE = True
except ImportError:
    DIAGRAM_AVAILABLE = False


def extract_generator_count(text: str) -> int:
    """
    Extract generator count from BOD using specification patterns.
    FIXED: No longer counts word occurrences.
    """
    # Extract generator section (match only level-2 headers, not ###)
    gen_section = re.search(r'##\s+GENERATOR SYSTEM.*?(?=\n## [A-Z]|\Z)', text, re.DOTALL | re.IGNORECASE)
    search_text = gen_section.group(0) if gen_section else text

    # Pattern 1: "N × power_rating generators" or "N generators"
    # Matches: "6 × 4.0 MW @ 13.8 kV Diesel Generators"
    patterns = [
        r'\*\*(\d+)\s*[×x]\s*[\d.]+\s*(?:MW|kW|kVA).*?[Gg]enerator',  # Bold format
        r'(\d+)\s*[×x]\s*[\d.]+\s*(?:MW|kW|kVA).*?[Gg]enerator',  # Plain format
        r'\*\*Quantity:\*\*\s*(\d+)',
        r'(\d+)\s*generators?\s*\(positions',  # Phase breakdown format
    ]

    for pattern in patterns:
        match = re.search(pattern, search_text, re.IGNORECASE)
        if match:
            return int(match.group(1))

    # Default fallback
    return 4


def extract_generator_rating(text: str) -> Tuple[int, int]:
    """
    Extract generator kW and kVA ratings from BOD.
    FIXED: Now parses actual specifications.
    Returns: (kw, kva)
    """
    # Extract generator section (match only level-2 headers, not ###)
    gen_section = re.search(r'##\s+GENERATOR SYSTEM.*?(?=\n## [A-Z]|\Z)', text, re.DOTALL | re.IGNORECASE)
    search_text = gen_section.group(0) if gen_section else text

    # Pattern: "N.N MW" or "N,NNN kW" @ voltage
    patterns = [
        r'\*\*(\d+(?:,\d+)?(?:\.\d+)?)\s*(MW|kW)\s*@',  # Bold format with @
        r'(\d+(?:,\d+)?(?:\.\d+)?)\s*(MW|kW)\s*@',  # Plain format with @
        r'[×x]\s*(\d+(?:,\d+)?(?:\.\d+)?)\s*(MW|kW)',  # After × symbol
        r'\|\s*\*\*Rating\*\*\s*\|\s*([\d,]+)\s*kW',  # Table format
        r'rated\s+([\d,]+)\s*kW',  # "rated N kW"
    ]

    for pattern in patterns:
        match = re.search(pattern, search_text, re.IGNORECASE)
        if match:
            value_str = match.group(1).replace(',', '')
            value = float(value_str)

            # Handle unit if present
            if len(match.groups()) > 1 and match.group(2):
                unit = match.group(2).upper()
                if unit == 'MW':
                    kw = int(value * 1000)
                else:
                    kw = int(value)
            else:
                kw = int(value)

            # Calculate kVA assuming 0.8 power factor (typical for generators)
            kva = int(kw / 0.8)
            return kw, kva

    # Default fallback
    return 2000, 2500


def extract_generator_fuel(text: str) -> str:
    """
    Extract fuel type from generator section only.
    FIXED: Context-aware to avoid confusion with house generators.
    """
    # Extract generator section only (match only level-2 headers, not ###)
    gen_section = re.search(r'##\s+GENERATOR SYSTEM.*?(?=\n## [A-Z]|\Z)', text, re.DOTALL | re.IGNORECASE)
    search_text = gen_section.group(0) if gen_section else text

    # Look for fuel type in specifications table
    fuel_spec = re.search(r'\|\s*\*\*Fuel\*\*\s*\|\s*([^|]+)', search_text, re.IGNORECASE)
    if fuel_spec:
        fuel_value = fuel_spec.group(1).lower()
        if 'diesel' in fuel_value and 'bio' not in fuel_value:
            return "DIESEL"
        elif 'natural gas' in fuel_value or 'nat gas' in fuel_value:
            return "NAT_GAS"
        elif 'biodiesel' in fuel_value:
            return "BIODIESEL"

    # Alternative: Look for fuel mentioned near generator rating
    fuel_pattern = r'(diesel|natural gas|nat gas|biodiesel).*?[Gg]enerator|[Gg]enerator.*?(diesel|natural gas|nat gas|biodiesel)'
    match = re.search(fuel_pattern, search_text, re.IGNORECASE)
    if match:
        fuel_type = (match.group(1) or match.group(2)).lower()
        if 'diesel' in fuel_type and 'bio' not in fuel_type:
            return "DIESEL"
        elif 'natural gas' in fuel_type or 'nat gas' in fuel_type:
            return "NAT_GAS"
        elif 'biodiesel' in fuel_type:
            return "BIODIESEL"

    return "DIESEL"  # Default to diesel


def extract_transformer_specs(text: str) -> Tuple[int, int]:
    """
    Extract transformer count and rating from BOD.
    FIXED: Now parses specifications instead of auto-calculating.
    Returns: (count, kva_per_unit)
    """
    # Extract transformer section
    tx_section = re.search(r'##\s*TRANSFORMER.*?(?=##|\Z)', text, re.DOTALL | re.IGNORECASE)
    search_text = tx_section.group(0) if tx_section else text

    # Pattern: "N × rating kVA" transformers
    # Matches: "8 × 3,500 kVA (13.8 kV/480V) Oil-Filled Transformers"
    patterns = [
        r'\*\*(\d+)\s*[×x]\s*([\d,]+)\s*kVA',  # Bold format
        r'(\d+)\s*[×x]\s*([\d,]+)\s*kVA',  # Plain format
        r'\|\s*\*\*Rating\*\*\s*\|\s*([\d,]+)\s*kVA',  # Table format
    ]

    count = None
    kva = None

    for pattern in patterns:
        match = re.search(pattern, search_text, re.IGNORECASE)
        if match:
            if len(match.groups()) == 2:
                count = int(match.group(1))
                kva = int(match.group(2).replace(',', ''))
                break
            else:
                kva = int(match.group(1).replace(',', ''))

    # If we found kVA but not count, look for count separately
    if kva and not count:
        count_patterns = [
            r'(\d+)\s*[×x].*?[Tt]ransformer',
            r'\*\*Configuration:\*\*.*?(\d+)\s*transformers',
        ]
        for pattern in count_patterns:
            count_match = re.search(pattern, search_text, re.IGNORECASE)
            if count_match:
                count = int(count_match.group(1))
                break

    # Default fallback (Phase 2 full build: 8 transformers)
    if not count:
        count = 8
    if not kva:
        kva = 3500

    return count, kva


def extract_rmu_count(text: str) -> int:
    """
    Extract RMU count from BOD.
    FIXED: No longer hardcoded to 4.
    """
    # Extract RMU section
    rmu_section = re.search(r'###\s*Ring Main Units.*?(?=##|\Z)', text, re.DOTALL | re.IGNORECASE)
    search_text = rmu_section.group(0) if rmu_section else text

    # Pattern: "N × RMUs" or "N RMUs"
    # Matches: "6 × RMUs (13.8 kV, 630A rated)"
    patterns = [
        r'(\d+)\s*[×x]\s*RMU',
        r'\*\*Equipment:\*\*\s*(\d+)\s*[×x]?\s*RMU',
    ]

    for pattern in patterns:
        match = re.search(pattern, search_text, re.IGNORECASE)
        if match:
            return int(match.group(1))

    # Default for ring topology
    return 4


def extract_ups_specs(text: str) -> Dict[str, Any]:
    """
    Extract IT and Mechanical UPS specifications separately.
    FIXED: Section-aware parsing, distinguishes IT from Mechanical UPS.
    Returns: {
        'it_ups': {'count': int, 'kva_per_unit': int, 'type': str, 'battery': str},
        'mech_ups': {'count': int, 'kw_per_unit': int, 'type': str}
    }
    """
    result = {
        'it_ups': {'count': 0, 'kva_per_unit': 0, 'type': 'STATIC', 'battery': 'LI-ION'},
        'mech_ups': {'count': 0, 'kw_per_unit': 0, 'type': 'STATIC'}
    }

    # Extract IT UPS section (match only level-2 headers, not ###)
    it_ups_section = re.search(r'##\s+IT UPS.*?(?=\n## [A-Z]|\Z)', text, re.DOTALL | re.IGNORECASE)
    if it_ups_section:
        section = it_ups_section.group(0)

        # Pattern: "N × rating kVA IT UPS Modules" or "N-N × rating kVA"
        # Matches: "### Phase 1: 5-6 × 1,250 kVA IT UPS Modules" or "**Phase 1:** ..."
        patterns = [
            r'###\s*Phase 1:\s*(\d+)(?:-\d+)?\s*[×x]\s*([\d,]+)\s*kVA',  # Heading format
            r'\*\*Phase 1:\*\*\s*(\d+)(?:-\d+)?\s*[×x]\s*([\d,]+)\s*kVA',  # Bold format
            r'(\d+)(?:-\d+)?\s*[×x]\s*([\d,]+)\s*kVA.*?(?:IT\s+UPS|UPS\s+Module|module)',  # Standard format
            r'(\d+)(?:-\d+)?\s*modules?.*?of\s*([\d,]+)\s*kVA',  # "N modules of M kVA" format
        ]

        for pattern in patterns:
            match = re.search(pattern, section, re.IGNORECASE)
            if match:
                result['it_ups']['count'] = int(match.group(1))
                result['it_ups']['kva_per_unit'] = int(match.group(2).replace(',', ''))
                break

        # Detect battery type
        if 'lithium' in section.lower() or 'li-ion' in section.lower():
            result['it_ups']['battery'] = 'LI-ION'
        elif 'vrla' in section.lower():
            result['it_ups']['battery'] = 'VRLA'
        elif 'nicd' in section.lower():
            result['it_ups']['battery'] = 'NICD'

        # Detect UPS type
        if 'rotary' in section.lower():
            result['it_ups']['type'] = 'ROTARY'
        else:
            result['it_ups']['type'] = 'STATIC'

    # Extract Mechanical UPS section (match only level-2 headers, not ###)
    mech_ups_section = re.search(r'##\s+MECHANICAL UPS.*?(?=\n## [A-Z]|\Z)', text, re.DOTALL | re.IGNORECASE)
    if mech_ups_section:
        section = mech_ups_section.group(0)

        # Pattern: "N × rating kW Static UPS Modules"
        # Matches: "**Phase 1: 8 × 250 kW Static UPS Modules**" or heading format
        patterns = [
            r'###\s*Phase 1:\s*(\d+)\s*[×x]\s*([\d,]+)\s*kW',  # Heading format
            r'\*\*Phase 1:\*\*\s*(\d+)\s*[×x]\s*([\d,]+)\s*kW',  # Bold format
            r'(\d+)\s*[×x]\s*([\d,]+)\s*kW.*?(?:Static\s+UPS|UPS\s+Module|module)',  # Standard format
            r'(\d+)\s*modules?.*?of\s*([\d,]+)\s*kW',  # "N modules of M kW" format
        ]

        for pattern in patterns:
            match = re.search(pattern, section, re.IGNORECASE)
            if match:
                result['mech_ups']['count'] = int(match.group(1))
                result['mech_ups']['kw_per_unit'] = int(match.group(2).replace(',', ''))
                break

        # Detect UPS type
        if 'rotary' in section.lower():
            result['mech_ups']['type'] = 'ROTARY'
        else:
            result['mech_ups']['type'] = 'STATIC'

    return result


def parse_bod_description(text: str, include_z_matrix: bool = True) -> Dict[str, Any]:
    """
    Parse Basis of Design text into structured electrical components.
    FIXED: Uses proper specification extraction instead of word counting.

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
    # Look for MV distribution voltage (typically mentioned with "MV", "distribution", or "ring")
    mv_voltage_patterns = [
        r'(\d+(?:\.\d+)?)\s*kV.*?(?:MV|medium voltage|distribution|ring|dual-ring)',
        r'(?:MV|medium voltage|distribution|ring).*?(\d+(?:\.\d+)?)\s*kV',
    ]

    nominal_voltage = 13.8  # default
    for pattern in mv_voltage_patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            voltage = float(match.group(1))
            if 10 <= voltage <= 50:  # Typical MV range
                nominal_voltage = voltage
                break

    # If no MV voltage found, use first voltage match (old behavior as fallback)
    if nominal_voltage == 13.8:
        voltage_match = re.search(r'(\d+(?:\.\d+)?)\s*kV', text)
        if voltage_match:
            voltage = float(voltage_match.group(1))
            if 10 <= voltage <= 50:
                nominal_voltage = voltage

    # --- Detect topology ---
    if "ring" in text.lower() or "ring bus" in text.lower() or "dual-ring" in text.lower():
        elements["topology"] = "ring"
    elif "dual" in text.lower() or "a/b" in text.lower() or "dual-feed" in text.lower():
        elements["topology"] = "dual"
    elif "distributed" in text.lower() or "2n" in text.lower() or "distributed redundant" in text.lower():
        elements["topology"] = "distributed_redundant"

    # --- Create MV Buses ---
    if elements["topology"] == "ring":
        # FIXED: Use extracted RMU count, not hardcoded 4
        rmu_count = extract_rmu_count(text)
        for i in range(rmu_count):
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
        elements["buses"].extend([
            {"id": "SWGR_A", "voltage": nominal_voltage},
            {"id": "SWGR_B", "voltage": nominal_voltage}
        ])
        # No tie breaker in true 2N
    else:
        elements["buses"].append({"id": "MAIN_SWGR", "voltage": nominal_voltage})

    # --- Generator Detection and Classification ---
    # FIXED: Use proper extraction functions
    gen_count = extract_generator_count(text)
    rating_kw, rating_kva = extract_generator_rating(text)
    fuel = extract_generator_fuel(text)

    # Determine generator type
    g_type = "RECIP"
    if "turbine" in text.lower() or "gas turbine" in text.lower():
        g_type = "TURBINE"

    paralleled = any(k in text.lower() for k in ["paralleled", "parallel", "sync", "common bus"])

    for i in range(gen_count):
        bus_target = (
            f"RING_BUS_{(i % len([b for b in elements['buses'] if 'RING' in b['id']])) + 1}" if elements["topology"] == "ring"
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
        elements["parallel_groups"].append("SYNC_BUS")
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
    # FIXED: Use extracted RMU count
    if "rmu" in text.lower() or "ring main" in text.lower() or elements["topology"] == "ring":
        rmu_count = extract_rmu_count(text)
        for i in range(rmu_count):
            rmu_id = f"RMU_{i+1}"
            elements["rmu"].append(rmu_id)
            elements["buses"].append({"id": f"{rmu_id}_BUS", "voltage": nominal_voltage})

            # RMU switches: IN, OUT, FEEDER
            if elements["topology"] == "ring":
                ring_buses = [b for b in elements["buses"] if 'RING_BUS' in b['id']]
                ring_count = len(ring_buses)
                elements["switches"].extend([
                    {"id": f"{rmu_id}_IN", "bus1": f"RING_BUS_{(i % ring_count) + 1}",
                     "bus2": f"{rmu_id}_BUS", "kind": "DISCONNECTOR", "open": False},
                    {"id": f"{rmu_id}_OUT", "bus1": f"{rmu_id}_BUS",
                     "bus2": f"RING_BUS_{((i + 1) % ring_count) + 1}", "kind": "DISCONNECTOR", "open": False}
                ])

    # --- Transformer Sizing ---
    # FIXED: Use extracted transformer specifications
    xfmr_count, tx_kva = extract_transformer_specs(text)

    for i in range(xfmr_count):
        hv_bus = f"RMU_{i+1}_BUS" if elements["rmu"] and i < len(elements["rmu"]) else (
            "SWGR_A" if i % 2 == 0 and elements["topology"] in ["dual", "distributed_redundant"]
            else "SWGR_B" if elements["topology"] in ["dual", "distributed_redundant"]
            else "MAIN_SWGR"
        )
        lv_bus = f"LV_BUS_{i+1}"
        elements["buses"].append({"id": lv_bus, "voltage": 0.48})
        elements["transformers"].append({
            "id": f"TX_{i+1}",
            "hv_bus": hv_bus,
            "lv_bus": lv_bus,
            "hv_voltage": nominal_voltage,
            "lv_voltage": 0.48,
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
            "voltage": 0.48,
            "rating_a": 3200,
            "interrupt_rating_ka": 65,
            "redundancy": redundancy_type,
            "feeds": []
        })

    # --- UPS Detection (type, battery, function) ---
    # FIXED: Use section-aware UPS extraction
    ups_specs = extract_ups_specs(text)

    # Create IT UPS modules
    for i in range(ups_specs['it_ups']['count']):
        lv_bus = f"LV_BUS_{(i % xfmr_count) + 1}"
        kva = ups_specs['it_ups']['kva_per_unit']
        kw = int(kva * 0.8)  # Assume 0.8 PF

        elements["ups"].append({
            "id": f"IT_UPS_{i+1}",
            "bus": lv_bus,
            "type": ups_specs['it_ups']['type'],
            "battery": ups_specs['it_ups']['battery'],
            "function": "IT",
            "kw": kw,
            "kva": kva
        })

    # Create Mechanical UPS modules
    for i in range(ups_specs['mech_ups']['count']):
        lv_bus = f"LV_BUS_{(i % xfmr_count) + 1}"
        kw = ups_specs['mech_ups']['kw_per_unit']
        kva = int(kw / 0.9)  # Assume 0.9 PF for mechanical loads

        elements["ups"].append({
            "id": f"MECH_UPS_{i+1}",
            "bus": lv_bus,
            "type": ups_specs['mech_ups']['type'],
            "battery": "LI-ION",  # Static UPS typically use lithium
            "function": "MECHANICAL",
            "kw": kw,
            "kva": kva
        })

    # --- PDUs and STS ---
    # Estimate PDU count from cabinet count or default
    pdu_pattern = r'(\d+)\s*cabinets?'
    pdu_match = re.search(pdu_pattern, text, re.IGNORECASE)
    pdu_count = int(pdu_match.group(1)) * 2 if pdu_match else 8  # 2 PDUs per cabinet

    ups_count = len(elements["ups"])
    if ups_count > 0:
        for i in range(pdu_count):
            a_source = f"{elements['ups'][i % ups_count]['id']}"
            b_source = f"{elements['ups'][(i + 1) % ups_count]['id']}"

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


def build_network_from_description(text: str, include_z_matrix: bool = True) -> Tuple[pp.network.Network, Dict[str, Any]]:
    """
    Build PowSyBl network from BOD text description.
    FIXED: Proper substation hierarchy and reactive power handling.

    Args:
        text: BOD text description
        include_z_matrix: If True, include 3x3 impedance matrices in metadata

    Returns:
        Tuple of (network, metadata_dict)
    """
    data = parse_bod_description(text, include_z_matrix)
    net = pp.network.create_empty("PACHYDERM_TierIV")

    # FIXED: Create substations first, then voltage levels
    # Group buses by voltage level
    voltage_groups = {}
    for bus in data["buses"]:
        voltage = bus["voltage"]
        if voltage not in voltage_groups:
            voltage_groups[voltage] = []
        voltage_groups[voltage].append(bus)

    # Create substations for each voltage level
    substation_map = {}
    for voltage, buses in voltage_groups.items():
        # Determine substation name based on voltage
        if voltage > 100:  # HV (345 kV, etc.)
            sub_id = "SUB_HV"
        elif voltage > 1:  # MV (13.8 kV, etc.)
            sub_id = "SUB_MV"
        else:  # LV (0.48 kV, etc.)
            sub_id = "SUB_LV"

        # Create substation if it doesn't exist
        if sub_id not in substation_map:
            net.create_substations(id=[sub_id])
            substation_map[sub_id] = []

        # Create voltage levels within substation
        for bus in buses:
            vl_id = bus["id"]
            net.create_voltage_levels(
                id=[vl_id],
                substation_id=[sub_id],
                topology_kind=['BUS_BREAKER'],
                nominal_v=[voltage]
            )
            substation_map[sub_id].append(vl_id)

            # Create bus within voltage level
            bus_id = f"{vl_id}_BUS"
            net.create_buses(
                id=[bus_id],
                voltage_level_id=[vl_id]
            )

    # Generators
    for g in data["generators"]:
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

    # Transformers (now with proper substation hierarchy)
    for t in data["transformers"]:
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

    # UPS (modeled as generators with reactive power)
    # FIXED: Set reactive power explicitly
    for u in data["ups"]:
        try:
            # Calculate reactive power assuming power factor
            p_mw = u["kw"] / 1000
            pf = 0.9
            q_mvar = p_mw * math.sqrt((1 - pf**2) / pf**2)

            net.create_generators(
                id=[u["id"]],
                voltage_level_id=[u["bus"]],
                bus_id=[f"{u['bus']}_BUS"],
                max_p=[u["kw"]/1000],
                min_p=[0],
                target_p=[(u["kw"]/1000)*0.8],
                target_v=[0.48],
                target_q=[q_mvar],  # FIXED: Set reactive power
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
            ups_entry = next((u for u in data["ups"] if u["id"] == ups_id), None)
            if ups_entry:
                bus_id = f"{ups_entry['bus']}_BUS"
                voltage_level = ups_entry['bus']
            else:
                continue
        else:
            # If no STS, use first LV bus
            if data["buses"]:
                lv_buses = [b for b in data["buses"] if b["voltage"] < 1]
                if lv_buses:
                    voltage_level = lv_buses[0]["id"]
                    bus_id = f"{voltage_level}_BUS"
                else:
                    continue
            else:
                continue

        try:
            net.create_loads(
                id=[p["id"]],
                voltage_level_id=[voltage_level],
                bus_id=[bus_id],
                p0=[0.1],  # 100 kW per PDU
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
    if not DIAGRAM_AVAILABLE:
        print(f"Note: Diagram generation requires pypowsybl-diagram (optional package)")
        return None

    try:
        svg_content = diagram.draw_network(
            network,
            title=title
        )
        return svg_content
    except Exception as e:
        print(f"Note: Diagram generation error: {e}")
        return None


def main():
    """Example usage of the FIXED PACHYDERM BOD generator."""

    bod_text = """
    13.8kV ring bus architecture with four diesel reciprocating generators and RMUs at each node.
    Static lithium-ion UPS systems support IT loads, while rotary flywheel UPS units support
    mechanical cooling fans and pumps. All PDUs are dual-corded through STS connections.
    System includes zig-zag grounding transformers for neutral earthing.
    MV switchboards rated at 4000A with 65kAIC interrupt rating feed step-down transformers
    to 480V LV switchboards with A/B redundancy.
    """

    print("=" * 70)
    print("PACHYDERM GLOBAL - Data Center Electrical Model Generator (FIXED)")
    print("=" * 70)
    print("\nParsing Basis of Design text...")

    # Build network
    network, metadata = build_network_from_description(bod_text, include_z_matrix=True)

    print(f"\nNetwork created: {network.id}")
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
        print("Diagram saved: pachyderm_tierIV_detailed.svg")

    print("Metadata exported: pachyderm_metadata.json")
    print("\n" + "=" * 70)
    print("Generation complete!")
    print("=" * 70)


if __name__ == "__main__":
    main()
