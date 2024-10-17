import networkx as nx
import matplotlib.pyplot as plt

def create_k_partite_graph(k, n):
    """
    Create and visualize a k-partite graph where each partition has n nodes.
    
    Parameters:
    k (int): Number of partitions
    n (int): Number of nodes per partition
    """
    # Create k partitions, each with n nodes
    sets = [n] * k  # A list with k elements, each being n
    
    # Generate the complete k-partite graph
    G = nx.complete_multipartite_graph(*sets)
    
    # Draw the graph
    pos = nx.spring_layout(G)  # Layout for visualization
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500)
    plt.title(f'{k}-Partite Graph with {n} Nodes per Partition')
    plt.show()

if __name__ == "__main__":
    # Example: 4 partitions with 5 nodes each
    k = 4  # Number of partitions
    n = 5  # Number of nodes per partition
    create_k_partite_graph(k, n)
