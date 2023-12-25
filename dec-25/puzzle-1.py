from networkx import connected_components
import networkx as nx

with open("input.txt") as file:
    lines = file.read().splitlines()

# Create undirected Graph
G = nx.Graph()
for line in lines:
    node, other_nodes = line.split(":")[0].strip(), line.split(":")[1].strip().split(" ")
    G.add_node(node)
    for x in other_nodes:
        G.add_node(x)
        G.add_edge(node, x)

print(G)

# Dividing the graph into two means its a cut and this provides the minimum cut of the graph
# Which is the one given as the requirement
# I need to refer old school algo class's flow algorithms & min-cut theories to do it myself rather than using library
# However, this has it already built in so why not use it?? But I should definitely try to implement that
cuts = list(nx.minimum_edge_cut(G))
print(cuts)

# Removing the edges in the min cut
G.remove_edge(cuts[0][0], cuts[0][1])
G.remove_edge(cuts[1][0], cuts[1][1])
G.remove_edge(cuts[2][0], cuts[2][1])

# This calculates the sizes of two disjoint sets once graph is divided by the cut
sub_graph = list(connected_components(G))
print(len(sub_graph[0]) * len(sub_graph[1]))
