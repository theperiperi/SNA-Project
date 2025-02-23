import networkx as nx
import matplotlib.pyplot as plt

# ------------------------------
# 1. Load the Graph
# ------------------------------

G = nx.read_edgelist("data.txt", nodetype=int)

# # Print basic info about the graph
# print("Graph Info:")
# print(nx.info(G))

# ------------------------------
# 2. Compute Betweenness Centrality
# ------------------------------

print("\nComputing betweenness centrality...")
# For exact computation, you can simply call:
betweenness = nx.betweenness_centrality(G)

# Optionally, show the top 5 nodes with highest betweenness centrality
top_betweenness = sorted(betweenness.items(), key=lambda x: x[1], reverse=True)[:5]
print("Top 5 nodes by betweenness centrality:")
for node, cent in top_betweenness:
    print(f"  Node {node}: {cent:.5f}")

# If the graph is too large and you want an approximation,
# you can use:
# betweenness = nx.betweenness_centrality(G, k=100, seed=42)

# ------------------------------
# 3. Compute Closeness Centrality
# ------------------------------

print("\nComputing closeness centrality...")
closeness = nx.closeness_centrality(G)
top_closeness = sorted(closeness.items(), key=lambda x: x[1], reverse=True)[:5]
print("Top 5 nodes by closeness centrality:")
for node, cent in top_closeness:
    print(f"  Node {node}: {cent:.5f}")

# ------------------------------
# 4. Compute Reciprocity
# ------------------------------

# Reciprocity is defined for directed graphs.
# Since the dataset is undirected, every edge is inherently reciprocal.
# However, we can convert G to a directed graph to demonstrate this.
DG = G.to_directed()
global_reciprocity = nx.reciprocity(DG)
print(f"\nGlobal Reciprocity (after converting to directed): {global_reciprocity:.5f}")

# ------------------------------
# 5. Compute Transitivity (Global Clustering Coefficient)
# ------------------------------

transitivity = nx.transitivity(G)
print(f"\nTransitivity (global clustering coefficient): {transitivity:.5f}")

# Optionally, compute the average clustering coefficient (local clustering)
avg_clustering = nx.average_clustering(G)
print(f"Average Clustering Coefficient: {avg_clustering:.5f}")

# ------------------------------
# Visualize a Small Portion of the Graph
# ------------------------------
# Warning: Visualizing the entire graph may not be informative due to its size.
# You might choose to visualize a subgraph:
#
# sub_nodes = list(G.nodes())[:100]  # For example, the first 100 nodes
# subG = G.subgraph(sub_nodes)
# nx.draw(subG, node_size=50, with_labels=True)
# plt.show()
