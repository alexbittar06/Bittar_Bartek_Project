import csv
import random

def create_complex_perfect_k_partite_graph(k, n, additional_edges=0):
    """
    Create a complex perfect k-partite graph where nodes can connect to multiple adjacent partitions.
    
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
    # Connect each partition to the next in a perfect manner
    for i in range(k - 1):
        # Each node in the current partition connects to each node in the next partition
        for node in sets[i]:
            for target_node in sets[i + 1]:
                edges.add((node, target_node))
    
    # Add additional random edges between adjacent partitions
    for _ in range(additional_edges):
        # Select a random partition (except the last one)
        source_partition = random.randint(0, k - 2)
        # Get source and target nodes from adjacent partitions
        source_node = random.choice(sets[source_partition])
        target_node = random.choice(sets[source_partition + 1])
        edges.add((source_node, target_node))
    
    return sets, edges

def create_complex_not_perfect_k_partite_graph(k, n):
    """
    Create an imperfect k-partite graph by removing several edges to ensure it's not perfect.
    
    Parameters:
    k (int): Number of partitions
    n (int): Number of nodes per partition
    
    Returns:
    tuple: (sets, edges)
    """
    sets, edges = create_complex_perfect_k_partite_graph(k, n)

    # Ensure that at least one edge is removed to make it imperfect
    # To guarantee non-perfection, we can remove connections to ensure at least one vertex
    # in the last partition is unmatched.
    
    # Randomly remove edges from the last partition
    if sets[-1]:  # Check if there are nodes in the last partition
        unmatched_node = random.choice(sets[-1])
        edges = {(u, v) for u, v in edges if v != unmatched_node}  # Remove all edges to this node

    return sets, edges

def write_graphs_to_csv(sets_perfect, edges_perfect, sets_not_perfect, edges_not_perfect):
    """Write the perfect and non-perfect graphs to corresponding CSV files."""
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
    mink = 3
    maxk = 4  # Adjusted to allow k=4
    minn = 3
    maxn = 5
    
    # Clear files
    clear_file("not_perfect_k_partite_graph.csv")
    clear_file("perfect_k_partite_graph.csv")

    for k in range(mink, maxk):
        for n in range(minn, maxn):
            # Fewer additional edges since we can only connect adjacent partitions
            additional_edges = random.randint(1, 3)

            # Generate graphs
            sets_perfect, edges_perfect = create_complex_perfect_k_partite_graph(k, n, additional_edges)
            sets_not_perfect, edges_not_perfect = create_complex_not_perfect_k_partite_graph(k, n)
            
            # Write to CSV
            write_graphs_to_csv(sets_perfect, edges_perfect, sets_not_perfect, edges_not_perfect)

    print('Complex Perfect and Non-Perfect graphs have been written to CSV files.')
