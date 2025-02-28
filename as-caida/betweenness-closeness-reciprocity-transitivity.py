import networkx as nx
import matplotlib.pyplot as plt
from tqdm import tqdm

# ------------------------------
# 1. Load the Graph
# ------------------------------

print("Checkpoint: Loading graph from file...")
G = nx.read_edgelist("as-caida/data.txt", nodetype=int)
print("Graph loaded!")
# print(nx.info(G))

# ------------------------------
# 2. Compute Betweenness Centrality
# ------------------------------

print("\nCheckpoint: Starting betweenness centrality computation...")
# For exact computation, you can simply call:
betweenness = nx.betweenness_centrality(G)
print("Betweenness centrality computed.")

# Show the top 10 nodes with highest betweenness centrality
top_betweenness = sorted(betweenness.items(), key=lambda x: x[1], reverse=True)[:10]
print("\nTop 10 nodes by betweenness centrality:")
for node, cent in top_betweenness:
    print(f"  Node {node}: {cent:.5f}")

# ------------------------------
# 3. Compute Closeness Centrality with Progress Checkpoints
# ------------------------------

print("\nCheckpoint: Starting closeness centrality computation...")
# Instead of using the built-in function (which doesn't offer progress info),
# we compute it manually with a progress bar.
closeness = {}

# Iterate over all nodes with tqdm progress bar
for node in tqdm(G.nodes(), desc="Computing closeness centrality"):
    # Compute shortest path lengths from this node to all reachable nodes
    sp_lengths = nx.single_source_shortest_path_length(G, node)
    total_distance = sum(sp_lengths.values())
    reachable_nodes = len(sp_lengths)
    
    # Closeness centrality formula:
    # If reachable_nodes > 1, then closeness = (reachable_nodes - 1) / total_distance
    if total_distance > 0 and reachable_nodes > 1:
        closeness[node] = (reachable_nodes - 1) / total_distance
    else:
        closeness[node] = 0.0

print("Closeness centrality computed.")

# Print the top 10 nodes by closeness centrality
top_closeness = sorted(closeness.items(), key=lambda x: x[1], reverse=True)[:10]
print("\nTop 10 nodes by closeness centrality:")
for node, cent in top_closeness:
    print(f"  Node {node}: {cent:.5f}")

# ------------------------------
# 4. Visualize Closeness Centrality Graph
# ------------------------------

print("\nCheckpoint: Visualizing closeness centrality graph...")
plt.figure(figsize=(12, 8))

# Use uniform node size instead of scaling by closeness
node_sizes = [150 for node in G.nodes()]

# Draw the graph
pos = nx.spring_layout(G, seed=42)  # Fixed layout for consistency
nx.draw(G, pos, node_size=node_sizes, with_labels=False, node_color='dodgerblue', edge_color='gray', alpha=0.7)

# Highlight top 10 nodes by closeness centrality
top_nodes = [node for node, _ in top_closeness]
nx.draw_networkx_nodes(G, pos, nodelist=top_nodes, node_size=800, node_color='red')

plt.title("Graph Visualization with Closeness Centrality (Top Nodes in Red)")
plt.show()

# ------------------------------
# 5. Compute Reciprocity
# ------------------------------

print("\nCheckpoint: Converting to directed graph and computing reciprocity...")
# Since the dataset is undirected, every edge is inherently reciprocal.
DG = G.to_directed()
global_reciprocity = nx.reciprocity(DG)
print(f"Global Reciprocity (after converting to directed): {global_reciprocity:.5f}")

# ------------------------------
# 6. Compute Transitivity (Global Clustering Coefficient)
# ------------------------------

print("\nCheckpoint: Computing transitivity and average clustering coefficient...")
transitivity = nx.transitivity(G)
print(f"Transitivity (global clustering coefficient): {transitivity:.5f}")

avg_clustering = nx.average_clustering(G)
print(f"Average Clustering Coefficient: {avg_clustering:.5f}")