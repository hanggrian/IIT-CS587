# filename: network_graph_diagram.py
import matplotlib.pyplot as plt
import networkx as nx

def create_network_graph():
    # Create a directed graph
    G = nx.DiGraph()

    # Adding nodes for phases
    phases = [
        '1. Scoping and Requirements Gathering', 
        '2. System Design', 
        '3. Technology Selection', 
        '4. Implementation Plan',
        '5. Development & Customization', 
        '6. Training & Deployment', 
        '7. Testing & Quality Assurance',
        '8. Maintenance & Support',
        '9. Evaluation & Continuous Improvement'
    ]
    for idx, phase in enumerate(phases, 1):
        G.add_node(phase)

    # Adding edges to define sequence of phases
    edges = [
        ('1. Scoping and Requirements Gathering', '2. System Design'),
        ('2. System Design', '3. Technology Selection'),
        ('3. Technology Selection', '4. Implementation Plan'),
        ('4. Implementation Plan', '5. Development & Customization'),
        ('5. Development & Customization', '6. Training & Deployment'),
        ('6. Training & Deployment', '7. Testing & Quality Assurance'),
        ('7. Testing & Quality Assurance', '8. Maintenance & Support'),
        ('8. Maintenance & Support', '9. Evaluation & Continuous Improvement')
    ]
    G.add_edges_from(edges)

    # Define the layout to visualize the graph well
    pos = nx.spring_layout(G, seed=42)

    # Draw nodes and edges
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=4000, edge_color='k', linewidths=1, font_size=10, arrows=True)

    # Save the diagram
    plt.savefig('network_graph.png')
    plt.show()
    print("Network graph diagram created and saved as 'network_graph.png'.")

create_network_graph()