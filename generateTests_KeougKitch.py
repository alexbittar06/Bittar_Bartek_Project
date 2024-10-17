import networkx as nx
import csv
import random

def create_perfect_k_partite_graph(k, n, additional_edges=0):
    """
    Create a perfect k-partite graph where each node has a unique connection to each other partition.
    
    Parameters:
    k (int): Number of partitions
    n (int): Number of nodes per partition
    additional_edges (int): Number of additional random edges to add
    
    Returns:
    tuple: (sets, edges)
    """
    sets = [list(range(sum([n] * i), sum([n] * (i + 1)))) for i in range(k)]
    
    # Generate the perfect k-partite graph: unique connections between partitions
    edges = set()  # Use a set to store edges and prevent duplicates
    for i in range(k):
        for j in range(i + 1, k):
            for node_i, node_j in zip(sets[i], sets[j]):
                edges.add((node_i, node_j))
    
    # Add additional random edges
    for _ in range(additional_edges):
        u = random.choice(range(k))  # Randomly select a partition
        v = random.choice(range(k))  # Randomly select a different partition
        if u != v:  # Ensure we're not connecting within the same partition
            node_i = random.choice(sets[u])
            node_j = random.choice(sets[v])
            edges.add((node_i, node_j))  # Add to the set; no duplicates will occur
    
    return sets, list(edges)  # Convert to list before returning

def create_not_perfect_k_partite_graph(k, n, additional_edges=0):
    """
    Create a non-perfect k-partite graph by violating unique connection rules between partitions.
    
    Parameters:
    k (int): Number of partitions
    n (int): Number of nodes per partition
    additional_edges (int): Number of additional random edges to add
    
    Returns:
    tuple: (sets, edges)
    """
    sets = [list(range(sum([n] * i), sum([n] * (i + 1)))) for i in range(k)]
    
    # Generate the graph with non-unique connections: randomizing/removing edges between partitions
    edges = set()  # Use a set to store edges and prevent duplicates
    for i in range(k):
        for j in range(i + 1, k):
            for node_i in sets[i]:
                node_j = random.choice(sets[j])
                if random.random() > 0.5:  # Add some randomness to edge selection
                    edges.add((node_i, node_j))  # Add to the set; no duplicates will occur
    
    # Add additional random edges while ensuring non-perfection
    for _ in range(additional_edges):
        u = random.choice(range(k))  # Randomly select a partition
        v = random.choice(range(k))  # Randomly select a different partition
        if u != v:  # Ensure we're not connecting within the same partition
            node_i = random.choice(sets[u])
            node_j = random.choice(sets[v])
            # Avoid adding edges that would make the graph perfect
            if (node_i, node_j) not in edges and not all((node_i, other_node) in edges for other_node in sets[v]):
                edges.add((node_i, node_j))  # Add to the set; no duplicates will occur
    
    return sets, list(edges)  # Convert to list before returning

def write_graphs_to_csv(sets_perfect, edges_perfect, sets_not_perfect, edges_not_perfect):
    """
    Write the perfect and non-perfect graphs to corresponding CSV files.
    
    Parameters:
    sets_perfect (list of lists): List of partitions for the perfect graph.
    edges_perfect (list of tuples): List of edges for the perfect graph.
    sets_not_perfect (list of lists): List of partitions for the non-perfect graph.
    edges_not_perfect (list of tuples): List of edges for the non-perfect graph.
    """
    # Write perfect graph to CSV
    with open('perfect_k_partite_graph.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        
        # Write header if the file is empty
        if file.tell() == 0:
            writer.writerow(["Partition Sets (Perfect)", "Edges (Perfect)"])
        
        # Write graph data
        writer.writerow([sets_perfect, edges_perfect])
    
    # Write non-perfect graph to CSV
    with open('not_perfect_k_partite_graph.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        
        # Write header if the file is empty
        if file.tell() == 0:
            writer.writerow(["Partition Sets (Not Perfect)", "Edges (Not Perfect)"])
        
        # Write graph data
        writer.writerow([sets_not_perfect, edges_not_perfect])

def clear_file(filename):
    """Clear the contents of the specified file."""
    with open(filename, 'w') as file:
        pass  # Opening in 'w' mode clears the file

if __name__ == "__main__":
    n = 4  # Number of nodes per partition
    
    # Range that k will go to
    mink = 2
    maxk = 15
    
    # Clear files
    clear_file("not_perfect_k_partite_graph.csv")
    clear_file("perfect_k_partite_graph.csv")

    for i in range(mink, maxk):
        # Randomize the number of additional edges for this graph
        additional_edges = random.randint(3, 7)  # Random number of edges between 1 and 5

        # Generate a perfect k-partite graph with additional random edges
        sets_perfect, edges_perfect = create_perfect_k_partite_graph(i, n, additional_edges)
        
        # Generate a non-perfect k-partite graph
        sets_not_perfect, edges_not_perfect = create_not_perfect_k_partite_graph(i, n, additional_edges)

        # Write both graphs to their corresponding CSV files
        write_graphs_to_csv(sets_perfect, edges_perfect, sets_not_perfect, edges_not_perfect)

    print('Perfect and Non-Perfect graphs have been written to CSV files.')
