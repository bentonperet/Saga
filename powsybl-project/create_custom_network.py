"""
Create a custom electrical network from scratch
"""
import pypowsybl.network as pn

def create_simple_network():
    """
    Create a simple custom network:
    - 2 substations
    - 1 generator
    - 1 load
    - 1 transmission line
    """
    
    # Create empty network
    network = pn.create_empty("MyNetwork")
    
    # Add substations
    network.create_substations(id=["S1", "S2"], 
                               country=["US", "US"])
    
    # Add voltage levels
    network.create_voltage_levels(id=["VL1", "VL2"],
                                  substation_id=["S1", "S2"],
                                  topology_kind=["BUS_BREAKER", "BUS_BREAKER"],
                                  nominal_v=[400, 400])
    
    # Add buses
    network.create_buses(id=["B1", "B2"],
                        voltage_level_id=["VL1", "VL2"])
    
    # Add generator at bus 1
    network.create_generators(id=["GEN1"],
                             voltage_level_id=["VL1"],
                             bus_id=["B1"],
                             target_p=[100],
                             target_v=[400],
                             min_p=[0],
                             max_p=[200],
                             voltage_regulator_on=[True])
    
    # Add load at bus 2
    network.create_loads(id=["LOAD1"],
                        voltage_level_id=["VL2"],
                        bus_id=["B2"],
                        p0=[90],
                        q0=[30])
    
    # Add transmission line between substations
    network.create_lines(id=["LINE1"],
                        voltage_level1_id=["VL1"],
                        bus1_id=["B1"],
                        voltage_level2_id=["VL2"],
                        bus2_id=["B2"],
                        r=[0.5],    # Resistance in Ohms
                        x=[5.0],    # Reactance in Ohms
                        g1=[0],     # Conductance
                        g2=[0],
                        b1=[0],     # Susceptance
                        b2=[0])
    
    return network

def main():
    print("Creating custom network...")
    network = create_simple_network()
    
    print("\n=== Network Created ===")
    print(f"Network ID: {network.id}")
    print(f"Substations: {len(network.get_substations())}")
    print(f"Voltage Levels: {len(network.get_voltage_levels())}")
    print(f"Buses: {len(network.get_buses())}")
    print(f"Generators: {len(network.get_generators())}")
    print(f"Loads: {len(network.get_loads())}")
    print(f"Lines: {len(network.get_lines())}")
    
    # Run power flow
    import pypowsybl as pp
    print("\nRunning power flow...")
    results = pp.loadflow.run_ac(network)
    print(f"Status: {results[0].status}")
    
    # Show results
    print("\nBus voltages:")
    print(network.get_buses()[['voltage_level_id', 'v_mag', 'v_angle']])
    
    # Save network
    network.dump("custom_network.xiidm", "XIIDM")
    print("\nNetwork saved to: custom_network.xiidm")

if __name__ == "__main__":
    main()
