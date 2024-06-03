import networkx as nx
import matplotlib.pyplot as plt
import random

random.seed(42)

num_nodes = 50

# Імовірність створення ребра між двома вузлами
prob_edge = 0.1

# Створення порожнього графа
G = nx.Graph()

# Додавання вузлів
for i in range(num_nodes):
    G.add_node(i)

# Додавання ребер з випадковою вагою
for i in range(num_nodes):
    for j in range(i + 1, num_nodes):
        if random.random() < prob_edge:
            weight = random.randint(1, 10)
            G.add_edge(i, j, weight=weight)

pos = nx.kamada_kawai_layout(G)

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
nx.write_graphml(G, "my_graph.graphml")
# Аналіз характеристик графа
print("Кількість вершин:", G.number_of_nodes())
print("Кількість ребер:", G.number_of_edges())

# Ступінь вершин
degree_sequence = sorted([d for n, d in G.degree()], reverse=True)
print("Максимальний ступінь вершини:", max(degree_sequence))
print("Мінімальний ступінь вершини:", min(degree_sequence))
print("Середній ступінь вершини:", sum(degree_sequence) / len(degree_sequence))
