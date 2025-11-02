# PACHYDERM GLOBAL - Data Center Electrical SLD Generator

Production-ready tool for generating PowSyBl single-line diagrams and comprehensive metadata from Basis of Design (BOD) text descriptions. Designed for Tier III/IV data center electrical systems.

## Features

### 🏗️ Electrical Components
- **Generators**: Reciprocating (Diesel/Gas) or Turbine with kW/kVA ratings
- **UPS Systems**: Static/Rotary with battery type (Li-ion/VRLA/Flywheel) and function (IT/Mechanical/Control)
- **Transformers**: Auto-sized based on load with MV→LV ratings
- **RMUs** (Ring Main Units): Automatic detection for ring bus topologies
- **MV/LV Switchboards**: With ampacity, interrupt ratings, and redundancy classification
- **Earthing Transformers**: Zig-Zag/Wye-Delta/NGR with 3×3 impedance matrices
- **STS** (Static Transfer Switches): For dual-cord PDU configurations
- **Parallel Generators**: Automatic sync bus detection and representation

### 🔌 Topologies Supported
- **Radial**: Single-feed with N+1 redundancy
- **Dual-Feed (A/B)**: Separate A and B switchgear with tie breakers
- **Ring Bus**: 4-node ring with RMUs for concurrent maintainability
- **Distributed Redundant (2N)**: Completely independent A and B power trains with no tie

### 📊 Output Files
- **SVG Single-Line Diagram**: Compact, labeled electrical one-line
- **JSON Metadata**: Complete system model with all component specifications
- **Validation Report**: Strict schema validation with alerts and recommendations

## Installation

```powershell
# Already installed packages:
# - pypowsybl
# - matplotlib
# - pandas
# - networkx

# Additional requirement for validation:
pip install jsonschema
```

## Quick Start

### 1. Generate Model from BOD Text

```python
python pachyderm_bod_generator.py
```

This runs the example configuration (13.8kV ring bus with diesel generators, static/rotary UPS, RMUs).

### 2. Validate Metadata

```python
python pachyderm_schema_validator.py
```

Validates the generated metadata and produces `validation_report.txt`.

## Custom Usage

### Example 1: Dual-Feed System

```python
from pachyderm_bod_generator import build_network_from_description

bod_text = """
Dual-feed 13.8kV MV switchboards A and B with two diesel reciprocating generators per side.
Each switchboard feeds two 2500 kVA transformers to 415V LV switchboards.
Static lithium-ion UPS systems support IT loads via STS for dual-cord PDUs.
Bus-tie breaker connects A and B switchgear for redundancy.
System includes zig-zag grounding transformers.
"""

network, metadata = build_network_from_description(bod_text, include_z_matrix=True)

print(f"Created {metadata['topology']} topology with:")
print(f"  - {len(metadata['generators'])} generators")
print(f"  - {len(metadata['transformers'])} transformers")
print(f"  - {len(metadata['ups'])} UPS systems")
```

**Expected Output:**
- 4 generators (2 on SWGR_A, 2 on SWGR_B)
- MV_SWBD_A and MV_SWBD_B with bus tie breaker
- 4 transformers (auto-sized based on PDU load)
- 4 LV switchboards with A/B redundancy
- Static UPS with Li-ion batteries for IT function
- STS connections for dual-cord PDUs

### Example 2: Ring Bus Topology

```python
bod_text = """
13.8kV ring bus with four nodes, each with RMU and one 2MW diesel generator.
Four 2500 kVA transformers feed 415V distribution.
Rotary flywheel UPS for mechanical loads (fans and pumps).
Static Li-ion UPS for IT server loads.
Neutral grounding via zig-zag transformers with 10Ω resistors.
"""

network, metadata = build_network_from_description(bod_text)

# Access specific components
for rmu in metadata['rmu']:
    print(f"RMU: {rmu}")

for ups in metadata['ups']:
    print(f"{ups['id']}: {ups['type']} {ups['battery']} ({ups['function']})")
```

**Expected Output:**
- 4 ring buses (RING_BUS_1 through RING_BUS_4)
- 4 RMUs with IN/OUT disconnectors
- 4 generators distributed across ring nodes
- Mixed UPS types: rotary for mechanical, static for IT

### Example 3: Distributed Redundant (2N) Topology

```python
bod_text = """
Distributed redundant 2N architecture with 13.8kV MV switchgear.
Completely independent A and B power trains with no tie breaker.
Two diesel generators per side, feeding separate transformers to isolated LV distribution.
Static lithium-ion UPS systems with dual-cord PDUs for IT loads.
Each path sized for 100% of load (true 2N).
"""

network, metadata = build_network_from_description(bod_text)

print(f"Topology: {metadata['topology']}")
print(f"MV Switchboards: {len(metadata['mv_swbd'])}")
for swbd in metadata['mv_swbd']:
    print(f"  {swbd['id']}: Redundancy = {swbd['redundancy']}")
```

**Expected Output:**
- 4 generators (2 on SWGR_A, 2 on SWGR_B)
- MV_SWBD_A and MV_SWBD_B with 2N redundancy classification
- NO tie breaker between A and B (completely isolated)
- 4 transformers (2 per path)
- 4 LV switchboards with 2N redundancy
- Each A/B path capable of carrying 100% load independently

### Example 4: Parallel Generators

```python
bod_text = """
13.8kV system with four diesel generators paralleled on common sync bus.
Generators feed MV switchboard with 4000A rating.
Two transformers to LV distribution with UPS and PDUs.
"""

network, metadata = build_network_from_description(bod_text)

# Check parallel configuration
if metadata['parallel_groups']:
    print("Generators are configured for parallel operation")
    # SYNC_BUS will be created automatically
```

## Component Detection Keywords

### Generators
- **Type**: "reciprocating", "recip", "engine" → RECIP | "turbine", "gas turbine" → TURBINE
- **Fuel**: "diesel" → DIESEL | "natural gas", "nat gas" → NAT_GAS | "biodiesel" → BIODIESEL
- **Parallel**: "paralleled", "sync", "common bus" → Creates SYNC_BUS

### UPS
- **Type**: "static" → STATIC | "rotary", "flywheel" → ROTARY
- **Battery**: "lithium", "li-ion" → LI-ION | "vrla" → VRLA | "flywheel" → FLYWHEEL | "nicd" → NICD
- **Function**: "it", "server" → IT | "mechanical", "fan", "pump" → MECHANICAL | "control" → CONTROL

### Earthing Transformers
- **Type**: "zig-zag", "zigzag" → ZIG-ZAG | "wye-delta" → WYE-DELTA | "ngr" → RESISTOR-GROUNDED
- **Auto-sized**: 1% of total transformer kVA
- **Impedance**: Auto-scaled with R/X ratio optimized for fault current

### Topology
- **Ring**: "ring", "ring bus"
- **Dual**: "dual", "a/b", "dual-feed"
- **Distributed Redundant**: "distributed", "2n", "distributed redundant"
- **RMU**: "rmu", "ring main" → Automatically creates RMUs for ring topology

## Metadata Structure

### Generator Entry
```json
{
  "id": "GEN_1",
  "bus": "SWGR_A",
  "type": "RECIP",
  "fuel": "DIESEL",
  "kw": 2000,
  "kva": 2500
}
```

### UPS Entry
```json
{
  "id": "UPS_1",
  "bus": "LV_BUS_1",
  "type": "STATIC",
  "battery": "LI-ION",
  "function": "IT",
  "kw": 500,
  "kva": 550
}
```

### Earthing Transformer (with 3×3 Z-matrix)
```json
{
  "id": "EARTH_TX_1",
  "type": "ZIG-ZAG",
  "rated_kva": 100,
  "impedance": {"r_ohm": 10.0, "x_ohm": 2.0},
  "z_matrix_3ph": [
    ["10.0 + j2.0", "2.0 + j0.5", "2.0 + j0.5"],
    ["2.0 + j0.5", "10.0 + j2.0", "2.0 + j0.5"],
    ["2.0 + j0.5", "2.0 + j0.5", "10.0 + j2.0"]
  ],
  "neutral_resistance_ohm": 10.0,
  "connected_bus": "RING_BUS_1",
  "grounding_connection": {
    "type": "RESISTIVE",
    "neutral_to_ground_path": "10 Ω NGR",
    "connection_impedance": "Z = 10.0 + j2.0 Ω",
    "ground_bus": "EARTH"
  }
}
```

### MV Switchboard Entry
```json
{
  "id": "MV_SWBD_A",
  "voltage": 13.8,
  "rating_a": 4000,
  "interrupt_rating_ka": 65,
  "redundancy": "A",
  "feeds": ["TX_1", "TX_2"]
}
```

## Validation

The validator performs:

### Strict Schema Checks
- Required fields present
- Data types correct
- Enums valid

### Business Logic Validations
- Generator kVA ≥ kW (power factor check)
- UPS battery/type compatibility (e.g., rotary → flywheel)
- Earthing transformer R/X ratio (4-6 range recommended)
- Topology-specific requirements (RMU count for ring, dual switchboards for dual-feed)
- MV/LV switchboard redundancy classification

### Output Example

```
⚠️ [UPS_2] Rotary UPS with VRLA battery is uncommon
💡 Recommendation: Rotary UPS typically use flywheel energy storage

ℹ️ [UPS_1] Rotary UPS for IT loads requires careful synchronization
💡 Recommendation: Consider static UPS with Li-ion for IT critical loads per TIA-942-A
```

## Integration with Commissioning

The generated metadata is designed for:

1. **Power Flow Analysis**: Import into ETAP, DIgSILENT, or SKM PowerTools
2. **Fault Studies**: 3×3 Z-matrices support sequence component analysis
3. **Commissioning Checklists**: Export generator/UPS/TX specs to test plans
4. **BIM Integration**: JSON structure compatible with Revit electrical families
5. **Digital Twin**: Complete system model for operational simulations

## Standards Compliance

Referenced standards in validation:
- **IEEE 1100 (Emerald Book)**: Powering and Grounding Electronic Equipment
- **IEEE 142 (Green Book)**: Grounding of Industrial and Commercial Power Systems
- **TIA-942-A**: Telecommunications Infrastructure Standard for Data Centers
- **IEC 60909**: Short-circuit currents in three-phase a.c. systems

## Advanced Features

### Toggle 3×3 Impedance Matrix

```python
# Disable Z-matrix for simplified reports
network, metadata = build_network_from_description(
    bod_text, 
    include_z_matrix=False
)
```

### Custom Load Sizing

Edit transformer sizing logic in `parse_bod_description()`:

```python
pdu_count = 16  # Override auto-detection
total_load_kw = pdu_count * 150  # 150 kW per PDU instead of 100 kW
```

### Export Network to XIIDM Format

```python
network.dump("custom_network.xiidm", "XIIDM")
```

## Troubleshooting

### Issue: "pypowsybl-diagram not installed"
The diagram generation feature requires `pypowsybl-diagram`. The metadata and network will still be created successfully.

### Issue: Validation warnings about redundancy
Ensure BOD text explicitly mentions "A/B", "dual-feed", or "ring" for proper redundancy classification.

### Issue: Generator/UPS not detected
Use explicit keywords: "generator", "ups", "diesel", "lithium", etc. in your BOD text.

## File Structure

```
powsybl-project/
├── pachyderm_bod_generator.py       # Main parser and network builder
├── pachyderm_schema_validator.py    # Strict validation with alerts
├── pachyderm_metadata.json          # Generated metadata (output)
├── validation_report.txt            # Validation results (output)
├── pachyderm_tierIV_detailed.svg    # Single-line diagram (output)
└── PACHYDERM_README.md              # This file
```

## Next Steps

Based on your ChatGPT conversation, planned enhancements include:

1. **Dynamic Load Simulation**: Model load transfer when RMU/breaker opens
2. **Fault Current Studies**: Use 3×3 Z-matrices for ground fault analysis
3. **Maintenance Sequences**: Simulate generator/RMU isolation scenarios
4. **Google Drive Integration**: Auto-regenerate diagrams when BOD changes
5. **ETAP/EasyPower Export**: Direct integration with commercial power analysis tools

## Credits

Developed for **PACHYDERM GLOBAL** data center electrical design workflows.

**Architecture by**: Erik (Data Center Electrical Engineer)  
**Implementation**: PowSyBl Python API with custom BOD parsing layer

---

**Version**: 1.0.0  
**Last Updated**: 2025-11-02
