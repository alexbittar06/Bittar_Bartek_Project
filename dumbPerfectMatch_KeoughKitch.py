import csv
import ast
import time
from collections import defaultdict

def process_graph(graph):
    """Converts set of edge tuples into a dictionary for bipartite matching."""
    g_dict = defaultdict(list)
    for edge in graph:
        left, right = edge
        g_dict[left].append(right)
    return g_dict

def bipartite_match(graph, part_A, part_B):
    """Uses Kuhn's algorithm for bipartite matching."""
    left = list(graph.keys())
    right = list(set(v for targets in graph.values() for v in targets))  # Unique right vertices

    # Ensure that the graph includes all vertices from part_A and part_B
    if len(left) < len(part_A) or len(right) < len(part_B):
        return False  # If some vertices are missing, it's not a perfect match

    num_left = len(left)
    num_right = len(right)

    # Map right vertices to their indices for faster lookup
    right_index_map = {v: i for i, v in enumerate(right)}

    mt = [-1] * num_right  # Match result: right-hand side vertex to left-hand side vertex
    used = [False] * num_left

    def try_kuhn(v):
        """Kuhn's algorithm to find augmenting paths."""
        if used[v]:
            return False
        used[v] = True

        for r in graph[left[v]]:
            right_idx = right_index_map[r]  # Use the index from the map
            if mt[right_idx] == -1 or try_kuhn(mt[right_idx]):
                mt[right_idx] = v
                return True
        return False

    # Try to match each left vertex
    for v in range(num_left):
        used = [False] * num_left
        if not try_kuhn(v):
            return False  # Return False if the matching fails for any left vertex

    # Check that all left vertices are matched (ensuring a perfect match)
    return all(m != -1 for m in mt[:len(part_B)])  # Only check the portion that corresponds to part_B

def is_perfect_k_partite_graph(sets, edges):
    """Check if the k-partite graph has a perfect matching using Kuhn's algorithm between every pair of partitions."""
    k = len(sets)  # Number of partitions

    # We need to run bipartite matching between every pair of partitions
    for part_i in range(k):
        part_A = sets[part_i]
        for part_j in range(k):
            if part_i == part_j:
                continue  # Skip matching a partition with itself
            
            part_B = sets[part_j]

            # Create a subgraph with edges only between part_A and part_B
            subgraph = {(u, v) for u, v in edges if (u in part_A and v in part_B) or (u in part_B and v in part_A)}

            # Process the subgraph into a dictionary
            graph = process_graph(subgraph)

            # Use Kuhn's algorithm to check if there is a perfect matching
            if not bipartite_match(graph, part_A, part_B):
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
            edges = set(ast.literal_eval(row[1]))  # Convert edges to set

            # Process the graph
            start_time = time.time()  # Start the timer
            k, n, perfect = is_perfect_k_partite_graph(sets, edges)
            result = "Perfect" if perfect else "Not Perfect"
            end_time = time.time()  # End the timer

            execution_time = end_time - start_time  # Calculate execution time
            print(f"Graph {idx + 1}: k = {k}, n = {n}, Status: {result} (Execution Time: {execution_time:.6f} seconds)")

def dumbPerfectMatch_KeoughKitch():
    filename1 = "not_perfect_k_partite_graph.csv"  # Change to your CSV filename
    filename2 = "perfect_k_partite_graph.csv"  # Change to your CSV filename

    # Process graphs from both CSV files, one graph at a time
    process_graph_from_csv(filename1)
    process_graph_from_csv(filename2)

if __name__ == "__main__":
    dumbPerfectMatch_KeoughKitch()
