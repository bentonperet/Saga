"""
Visualize network topology using matplotlib and networkx
"""
import pypowsybl.network as pn
import matplotlib.pyplot as plt
import networkx as nx

def create_network_graph(network):
    """Create a NetworkX graph from PowSyBl network"""
    G = nx.Graph()
    
    # Add buses as nodes
    buses = network.get_buses()
    for idx, bus in buses.iterrows():
        G.add_node(bus['voltage_level_id'], 
                   voltage=bus.get('v_mag', 0))
    
    # Add lines as edges
    lines = network.get_lines()
    for idx, line in lines.iterrows():
        G.add_edge(line['voltage_level1_id'], 
                   line['voltage_level2_id'],
                   label=line['id'])
    
    return G

def visualize_topology(network, output_file="network_topology.png"):
    """Create a topology visualization"""
    G = create_network_graph(network)
    
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(G, k=2, iterations=50)
    
    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_size=700, node_color='lightblue')
    
    # Draw edges
    nx.draw_networkx_edges(G, pos, width=2, alpha=0.6)
    
    # Draw labels
    nx.draw_networkx_labels(G, pos, font_size=10)
    
    plt.title(f"Network Topology: {network.id}")
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"Topology diagram saved to: {output_file}")
    plt.close()

def main():
    print("Loading network...")
    network = pn.create_ieee14()
    
    print("Creating topology visualization...")
    visualize_topology(network)
    
    print("Done!")

if __name__ == "__main__":
    main()
