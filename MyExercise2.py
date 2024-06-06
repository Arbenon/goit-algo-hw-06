from collections import deque
import osmnx as ox

city_name = "Kamianets-Podilskyi, Ukraine"

G = ox.graph_from_place(city_name, network_type='drive')

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    paths = {start: [start]}

    while queue:
        vertex = queue.popleft()
        for neighbor in graph.neighbors(vertex):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                paths[neighbor] = paths[vertex] + [neighbor]
    return paths

def dfs(graph, start, path=None, visited=None):
    if path is None:
        path = [start]
    if visited is None:
        visited = set()
    visited.add(start)
    paths = {start: path}

    for neighbor in graph.neighbors(start):
        if neighbor not in visited:
            new_paths = dfs(graph, neighbor, path + [neighbor], visited)
            paths.update(new_paths)
    return paths

# Вибираємо стартову вершину
start_node = list(G.nodes())[0]  # Вибираємо першу вершину в графі

# Запуск BFS та DFS
bfs_paths = bfs(G, start_node)
dfs_paths = dfs(G, start_node)

# Функція для друку шляхів у зручному форматі
def print_paths(paths, num_paths=5):
    print(f"Вивід перших {num_paths} шляхів:")
    for i, (node, path) in enumerate(paths.items()):
        if i >= num_paths:
            break
        print(f"Вершина: {node}, Шлях: {path}")

print("BFS шляхи:")
print_paths(bfs_paths)

print("\nDFS шляхи:")
print_paths(dfs_paths)
