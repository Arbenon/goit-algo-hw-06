import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

G = nx.read_graphml("my_graph.graphml")
pos = nx.kamada_kawai_layout(G)

def dfs_path(graph, start, goal):
    stack = [(start, [start])]
    visited = set()
    while stack:
        (vertex, path) = stack.pop()
        if vertex not in visited:
            if vertex == goal:
                return path
            visited.add(vertex)
            for neighbor in set(graph.neighbors(vertex)) - visited:
                stack.append((neighbor, path + [neighbor]))
    return None

def bfs_path(graph, start, goal):
    queue = deque([(start, [start])])
    visited = set()
    while queue:
        (vertex, path) = queue.popleft()
        if vertex not in visited:
            if vertex == goal:
                return path
            visited.add(vertex)
            for neighbor in set(graph.neighbors(vertex)) - visited:
                queue.append((neighbor, path + [neighbor]))
    return None

# Перевірка існуючих вузлів у графі
existing_nodes = list(G.nodes)
print("Існуючі вузли:", existing_nodes)

# Вибір точки для старту та фінішу
if len(existing_nodes) > 1:
    start_node = existing_nodes[0]
    end_node = existing_nodes[23]
else:
    raise ValueError("Граф має занадто мало вузлів для пошуку шляхів")

# Знаходження шляхів за допомогою DFS та BFS
dfs_result = dfs_path(G, start_node, end_node)
bfs_result = bfs_path(G, start_node, end_node)

# Виведення результатів
print("Шлях за допомогою DFS:", dfs_result)
print("Шлях за допомогою BFS:", bfs_result)

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
