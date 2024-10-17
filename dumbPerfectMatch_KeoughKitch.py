import csv
import ast
import time

def process_graph(graph):
    """Converts list of edge tuples into a dictionary for bipartite matching."""
    g_dict = {}
    for edge in graph:
        left = edge[0]
        right = edge[1]
        if left in g_dict:
            g_dict[left].append(right)
        else:
            g_dict[left] = [right]
    return g_dict

def bipartite_match(graph):
    """Uses Kuhn's algorithm for bipartite matching."""
    left = list(graph.keys())
    right = []
    
    # Gather all unique right-hand side vertices
    for targets in graph.values():
        for target in targets:
            if target not in right:
                right.append(target)

    num_left = len(left)
    num_right = len(right)

    mt = [-1] * num_right  # Match result: right-hand side vertex to left-hand side vertex
    global used

    # Try to match each left vertex
    for v in range(num_left):
        used = [False] * num_left
        try_kuhn(graph, v, left, right, mt)

    # Count matches
    match_count = sum(1 for match in mt if match != -1)
    return match_count == num_left  # Return if it's a perfect match

def try_kuhn(graph, v, left, right, mt):
    """Kuhn's algorithm to find augmenting paths."""
    global used
    if used[v]:
        return False
    used[v] = True

    for r in graph[left[v]]:
        right_idx = right.index(r)  # Index in the right set
        if mt[right_idx] == -1 or try_kuhn(graph, mt[right_idx], left, right, mt):
            mt[right_idx] = v
            return True
    return False

def is_perfect_k_partite_graph(sets, edges):
    """Check if the k-partite graph has a perfect matching using Kuhn's algorithm."""
    k = len(sets)  # Number of partitions
    
    # We need to attempt bipartite matching between all adjacent pairs of partitions
    for part_i in range(k - 1):
        part_A = sets[part_i]
        part_B = sets[part_i + 1]

        # Create a subgraph with edges only between part_A and part_B
        subgraph = [(u, v) for u, v in edges if u in part_A and v in part_B or u in part_B and v in part_A]

        # Process the subgraph into a dictionary
        graph = process_graph(subgraph)

        # Use Kuhn's algorithm to check if there is a perfect matching
        if not bipartite_match(graph):
            return k, len(part_A), False  # Not a perfect matching

    return k, len(sets[0]), True  # All partitions have a perfect matching

def process_graph_from_csv(filename):
    """Read and process each k-partite graph from a CSV file, one graph at a time."""
    csv.field_size_limit(10**6)  # Set the field size limit to a larger value

    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        for idx, row in enumerate(reader):
            # Assume the first column is the partition sets and the second is the edges
            sets = ast.literal_eval(row[0])
            edges = ast.literal_eval(row[1])

            # Process the graph
            start_time = time.time()  # Start the timer
            k, n, perfect = is_perfect_k_partite_graph(sets, edges)
            result = "Perfect" if perfect else "Not Perfect"
            end_time = time.time()  # End the timer

            execution_time = end_time - start_time  # Calculate execution time
            print(f"Graph {idx + 1}: k = {k}, n = {n}, Status: {result} (Execution Time: {execution_time:.6f} seconds)")

if __name__ == "__main__":
    filename1 = "not_perfect_k_partite_graph.csv"  # Change to your CSV filename
    filename2 = "perfect_k_partite_graph.csv"  # Change to your CSV filename

    # Process graphs from both CSV files, one graph at a time
    process_graph_from_csv(filename1)
    process_graph_from_csv(filename2)
