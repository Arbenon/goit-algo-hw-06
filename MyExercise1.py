import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt

# Встановлюємо назву міста
city_name = "Kamianets-Podilskyi, Ukraine"

# Завантажуємо дані дорожньої мережі міста
G = ox.graph_from_place(city_name, network_type='drive')

# Проектуємо граф для кращої візуалізації
G = ox.project_graph(G)

# Візуалізуємо граф з білим фоном
fig, ax = ox.plot_graph(G, node_size=30, node_color='blue', edge_color='gray', edge_linewidth=1.5, bgcolor='white')

# Аналіз характеристик
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degree = dict(G.degree())

print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print(f"Ступінь вершин: {degree}")