import networkx as nx
import matplotlib.pyplot as plt

G = nx.read_graphml("my_graph.graphml")
pos = nx.kamada_kawai_layout(G)

def dijkstra_all_pairs_shortest_paths(graph):
    all_pairs_shortest_paths = {}
    for node in graph.nodes():
        lengths = nx.single_source_dijkstra_path_length(graph, node, weight='weight')
        all_pairs_shortest_paths[node] = lengths
    return all_pairs_shortest_paths

# Знаходження найкоротших шляхів для всіх пар вершин
shortest_paths = dijkstra_all_pairs_shortest_paths(G)

# Виведення результатів
for start_node, paths in shortest_paths.items():
    print(f"Найкоротші шляхи від вершини {start_node}:")
    for end_node, length in paths.items():
        print(f"  до вершини {end_node}: {length}")
    print()

# Візуалізація графа
edges = G.edges(data=True)
edge_colors = [d['weight'] for (u, v, d) in edges]
edge_widths = [d['weight'] / 2 for (u, v, d) in edges]

plt.figure(figsize=(12, 8))
nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=200)

edges_drawn = nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color=edge_colors, width=edge_widths)
nx.draw_networkx_labels(G, pos)

plt.colorbar(edges_drawn, label='Вага ребра')
plt.title("Псевдореальна транспортна мережа")
plt.show()
