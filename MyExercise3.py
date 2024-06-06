import osmnx as ox
import networkx as nx

# Встановлюємо назву міста
city_name = "Kamianets-Podilskyi, Ukraine"

# Завантажуємо дані дорожньої мережі міста
G = ox.graph_from_place(city_name, network_type='drive')

# Змінюємо назви вузлів на коротші
mapping = {node: f'Node{i}' for i, node in enumerate(G.nodes())}
H = nx.relabel_nodes(G, mapping)

def dijkstra(graph, start):
    shortest_paths = {start: (None, 0)}
    current_node = start
    visited = set()

    while current_node is not None:
        visited.add(current_node)
        destinations = graph.neighbors(current_node)
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            edge_data = graph.get_edge_data(current_node, next_node)
            if 'length' not in edge_data[0]:
                print(f"Edge from {current_node} to {next_node} has no 'length' attribute.")
                continue
            weight = edge_data[0]['length'] + weight_to_current_node

            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)

        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return shortest_paths

        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])

    return shortest_paths

# Вибираємо стартову вершину
start_node = list(H.nodes())[0]

# Найкоротший шлях Дійкстри
shortest_paths = dijkstra(H, start_node)

# Результати у більш зручному форматі
def print_shortest_paths(shortest_paths):
    print("Найкоротші шляхи від початкової вершини:")
    for node, (prev, dist) in shortest_paths.items():
        print(f"Вершина: {node}, Попередня вершина: {prev}, Відстань: {dist:.2f}")

print_shortest_paths(shortest_paths)
