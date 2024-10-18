import networkx as nx
import csv
import random
import itertools

def create_perfect_k_partite_graph(k, n, additional_edges=0):
    """
    Create a perfect k-partite graph where nodes can only connect to adjacent partitions.
    Each node has exactly one connection to each adjacent partition.
    
    Parameters:
    k (int): Number of partitions
    n (int): Number of nodes per partition
    additional_edges (int): Number of additional random edges between adjacent partitions
    
    Returns:
    tuple: (sets, edges)
    """
    # Create k sets of n nodes each
    sets = [list(range(sum([n] * i), sum([n] * (i + 1)))) for i in range(k)]
    
    edges = set()
    # Connect each partition only to adjacent partitions
    for i in range(k-1):
        # Create perfect matching between adjacent partitions
        # Shuffle the target partition to ensure random but perfect matching
        target_nodes = sets[i+1].copy()
        random.shuffle(target_nodes)
        for node_i, node_j in zip(sets[i], target_nodes):
            edges.add((node_i, node_j))
    
    # Add additional random edges between adjacent partitions only
    for _ in range(additional_edges):
        # Select a random partition (except the last one)
        source_partition = random.randint(0, k-2)
        # Get source and target nodes from adjacent partitions
        source_node = random.choice(sets[source_partition])
        target_node = random.choice(sets[source_partition + 1])
        edges.add((source_node, target_node))
    
    return sets, edges

def create_not_perfect_k_partite_graph(k, n):
    """
    Create an imperfect k-partite graph by removing some edges
    between adjacent partitions, breaking the perfect matching.
    
    Parameters:
    k (int): Number of partitions
    n (int): Number of nodes per partition
    
    Returns:
    tuple: (sets, edges)
    """
    sets, edges = create_perfect_k_partite_graph(k, n)
    
    # Choose a random partition (except the last one)
    source_partition = random.randint(0, k-2)
    
    # Choose a random node from that partition
    node_to_disconnect = random.choice(sets[source_partition])
    
    # Remove all edges connected to this node
    edges_to_remove = {(u, v) for u, v in edges 
                      if u == node_to_disconnect or v == node_to_disconnect}
    edges.difference_update(edges_to_remove)
    
    return sets, edges

def write_graphs_to_csv(sets_perfect, edges_perfect, sets_not_perfect, edges_not_perfect):
    """
    Write the perfect and non-perfect graphs to corresponding CSV files.
    
    Parameters:
    sets_perfect (list of lists): List of partitions for the perfect graph
    edges_perfect (set): Set of edges for the perfect graph
    sets_not_perfect (list of lists): List of partitions for the non-perfect graph
    edges_not_perfect (set): Set of edges for the non-perfect graph
    """
    # Write perfect graph to CSV
    with open('perfect_k_partite_graph.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([sets_perfect, list(edges_perfect)])
    
    # Write non-perfect graph to CSV
    with open('not_perfect_k_partite_graph.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([sets_not_perfect, list(edges_not_perfect)])

def clear_file(filename):
    """Clear the contents of the specified file."""
    with open(filename, 'w') as file:
        pass

if __name__ == "__main__":
    mink = 2
    maxk = 6
    minn = 1
    maxn = 10
    
    # Clear files
    clear_file("not_perfect_k_partite_graph.csv")
    clear_file("perfect_k_partite_graph.csv")

    for k in range(mink,maxk):
        for n in range(minn, maxn):
            # Fewer additional edges since we can only connect adjacent partitions
            additional_edges = random.randint(1, 3)

            # Generate graphs
            sets_perfect, edges_perfect = create_perfect_k_partite_graph(k, n, additional_edges)
            sets_not_perfect, edges_not_perfect = create_not_perfect_k_partite_graph(k, n)
            
            # Write to CSV
            write_graphs_to_csv(sets_perfect, edges_perfect, sets_not_perfect, edges_not_perfect)

    print('Perfect and Non-Perfect graphs have been written to CSV files.')