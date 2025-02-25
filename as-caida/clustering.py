import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
from tqdm import tqdm

# ------------------------------
# 1. Load the Graph
# ------------------------------

print("Checkpoint: Loading graph from file...")
G = nx.read_edgelist("as-caida/data.txt", nodetype=int)
print("Graph loaded!")

# ------------------------------
# 2. Compute Clustering Coefficients
# ------------------------------
print("Computing local clustering coefficients...")
local_clustering = nx.clustering(G)

print("Computing global clustering coefficient...\n")
global_clustering = nx.transitivity(G)

# Compute the average local clustering coefficient
avg_local_clustering = sum(local_clustering.values()) / len(local_clustering)

# Get the first 10 nodes and their local clustering coefficients
first_10_nodes = list(local_clustering.items())[:10]

# Convert to DataFrame for better visualization
df = pd.DataFrame(first_10_nodes, columns=["Node", "Local Clustering Coefficient"])
print(df)

# ------------------------------
# 3. Display Results
# ------------------------------
print(f"Global Clustering Coefficient: {global_clustering:.6f}")
print(f"Average Local Clustering Coefficient: {avg_local_clustering:.6f}")

# Display the table
#print("\nFirst 10 Nodes with Local Clustering Coefficients:")
#print(df.to_string(index=False))

# ------------------------------
# 4. Visualize Clustering Distribution
# ------------------------------
plt.figure(figsize=(10,6))
plt.hist(local_clustering.values(), bins=20, edgecolor='black', alpha=0.75)
plt.xlabel("Local Clustering Coefficient")
plt.ylabel("Number of Nodes")
plt.title("Distribution of Local Clustering Coefficients")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()