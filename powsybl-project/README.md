# PowSyBl Single Line Diagram Project

This project demonstrates how to use PyPowSyBl for electrical network analysis and single line diagram generation.

## Setup

1. **Virtual Environment** (already created):
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

2. **Install Dependencies** (already done):
   ```powershell
   pip install pypowsybl matplotlib pandas
   ```

## Usage

### 1. Generate Single Line Diagrams (SLD)

Run the main example with IEEE 14-bus network:

```powershell
python example_sld.py
```

This will:
- Load the IEEE 14-bus test network
- Perform network analysis
- Run AC power flow
- Generate SVG single line diagrams for each substation

### 2. Create Custom Networks

Create your own network from scratch:

```powershell
python create_custom_network.py
```

### 3. Visualize Network Topology

Create a visual topology graph:

```powershell
python visualize_network.py
```

## Available Networks

PyPowSyBl includes several test networks:

- `create_ieee9()` - IEEE 9-bus system
- `create_ieee14()` - IEEE 14-bus system
- `create_ieee30()` - IEEE 30-bus system
- `create_ieee57()` - IEEE 57-bus system
- `create_ieee118()` - IEEE 118-bus system
- `create_four_substations_node_breaker_network()` - Example with breakers

## Key Features

### Network Analysis
- Load/create electrical networks
- Inspect substations, buses, lines, generators, loads
- View voltage levels and equipment ratings

### Power Flow Analysis
- AC/DC power flow calculations
- Voltage magnitude and angle analysis
- Power flow results visualization

### Single Line Diagrams
- Automatic SLD generation for substations
- SVG output format
- Customizable styling

### Supported File Formats
- XIIDM (XML-based format)
- UCTE
- CGMES
- PSS/E
- MATPOWER

## Example Code

```python
import pypowsybl.network as pn
import pypowsybl as pp

# Load network
network = pn.create_ieee14()

# Run power flow
results = pp.loadflow.run_ac(network)

# Generate single line diagram
substations = network.get_substations()
sld = network.get_single_line_diagram(substations.iloc[0]['id'])
sld.write_svg("output.svg")
```

## Documentation

- [PyPowSyBl Documentation](https://pypowsybl.readthedocs.io/)
- [PowSyBl Official Site](https://www.powsybl.org/)

## Troubleshooting

If you encounter script execution policy errors on Windows:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## Next Steps

1. Modify `create_custom_network.py` to build your specific network
2. Load your own network data files (XIIDM, CGMES, etc.)
3. Customize SLD styling and layout
4. Perform advanced analyses (contingency analysis, security analysis)
