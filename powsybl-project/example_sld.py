"""
PowSyBl Single Line Diagram Example
This script demonstrates how to load/create a network and generate single line diagrams
"""
import pypowsybl as pp
import pypowsybl.network as pn

# Create a simple example network
def create_sample_network():
    """Create a simple 4-bus network for demonstration"""
    network = pn.create_four_substations_node_breaker_network()
    return network

# Load network from file (IEEE test cases)
def load_ieee_network():
    """Load IEEE 14-bus test network"""
    network = pn.create_ieee14()
    return network

# Generate single line diagram
def generate_sld(network, substation_id, output_file="sld_output.svg"):
    """
    Generate single line diagram for a specific substation
    
    Args:
        network: PowSyBl network object
        substation_id: ID of the substation to visualize
        output_file: Output SVG file path
    """
    # Get single line diagram for the substation
    sld = network.get_single_line_diagram(substation_id)
    
    # Write to SVG file
    sld.write_svg(output_file)
    print(f"Single line diagram saved to: {output_file}")

# Network analysis
def analyze_network(network):
    """Print basic network information"""
    print("\n=== Network Information ===")
    print(f"Network ID: {network.id}")
    
    # Substations
    substations = network.get_substations()
    print(f"\nSubstations ({len(substations)}):")
    print(substations[['id', 'name', 'country', 'TSO']].to_string())
    
    # Voltage levels
    voltage_levels = network.get_voltage_levels()
    print(f"\nVoltage Levels ({len(voltage_levels)}):")
    print(voltage_levels[['id', 'substation_id', 'nominal_v']].head(10).to_string())
    
    # Buses
    buses = network.get_buses()
    print(f"\nBuses ({len(buses)}):")
    print(buses[['voltage_level_id', 'v_mag', 'v_angle']].head(10).to_string())
    
    # Lines
    lines = network.get_lines()
    print(f"\nLines ({len(lines)}):")
    print(lines[['id', 'voltage_level1_id', 'voltage_level2_id', 'r', 'x']].head(10).to_string())
    
    # Generators
    generators = network.get_generators()
    print(f"\nGenerators ({len(generators)}):")
    print(generators[['id', 'voltage_level_id', 'target_p', 'target_v']].head(10).to_string())
    
    return substations

# Run power flow analysis
def run_powerflow(network):
    """Run AC power flow analysis"""
    print("\n=== Running Power Flow Analysis ===")
    results = pp.loadflow.run_ac(network)
    print(f"Power flow status: {results[0].status}")
    
    # Show bus results
    buses = network.get_buses()
    print("\nBus Voltages:")
    print(buses[['voltage_level_id', 'v_mag', 'v_angle']].head(10).to_string())

def main():
    print("PowSyBl Single Line Diagram Generator")
    print("=" * 50)
    
    # Choose network type
    print("\nLoading IEEE 14-bus test network...")
    network = load_ieee_network()
    
    # Analyze the network
    substations = analyze_network(network)
    
    # Run power flow
    run_powerflow(network)
    
    # Generate single line diagrams for all substations
    print("\n=== Generating Single Line Diagrams ===")
    for idx, substation in substations.iterrows():
        sub_id = substation['id']
        output_file = f"sld_{sub_id}.svg"
        try:
            generate_sld(network, sub_id, output_file)
        except Exception as e:
            print(f"Could not generate SLD for {sub_id}: {e}")
    
    print("\n=== Complete! ===")
    print("Check the generated SVG files in the current directory.")

if __name__ == "__main__":
    main()
