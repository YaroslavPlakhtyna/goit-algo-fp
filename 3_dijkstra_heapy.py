import heapq

import networkx as nx
import matplotlib.pyplot as plt


def create_weighted_graph():
    G = nx.Graph()

    friendships = {
        ("Alice", "Bob"): 4,
        ("Alice", "Charlie"): 4,
        ("Alice", "Fiona"): 4,
        ("Alice", "George"): 2,
        ("Bob", "Diana"): 4,
        ("Bob", "Judy"): 3,
        ("Bob", "Hannah"): 2,
        ("Charlie", "Ian"): 3,
        ("Diana", "Judy"): 4,
        ("Fiona", "George"): 4,
        ("Fiona", "Hannah"): 1,
        ("George", "Ian"): 4,
        ("Hannah", "Judy"): 4,
        ("Judy", "Alice"): 2,
    }

    for friendship, relationship in friendships.items():
        G.add_edge(friendship[0], friendship[1], weight=relationship)

    return G


def print_relations_table(distances, person):
    print(f"Closest relation to each different person for '{person}':")
    print("-" * 20)
    print("{:<10} {:<10}".format("Person", "Distance"))
    print("-" * 20)
    for p in distances:
        distance = distances[p]
        if distance != 0:
            if distance == float("infinity"):
                distance = "∞"
            else:
                distance = str(distance)
            print("{:<10} {:<10}".format(p, distance))
    print()


def dijkstra(graph, start):
    distances = {node: float("infinity") for node in graph}
    distances[start] = 0
    lookup = [(0, start)]

    while lookup:
        c_distance, current = heapq.heappop(lookup)
        if c_distance > distances[current]:
            continue

        for neighbour, attrs in graph[current].items():
            n_distance = c_distance + attrs["weight"]
            if n_distance < distances[neighbour]:
                distances[neighbour] = n_distance
                heapq.heappush(lookup, (n_distance, neighbour))

    return distances


if __name__ == "__main__":
    # Створення графу взаємовідносин з вагами, які відповідають ступеням близькості
    G = create_weighted_graph()

    # Знаходження найближчого відношення для кожної особи за
    # допомогою алгоритму Дейкстри на базі мінімальної купи
    for node in G.nodes:
        print_relations_table(dijkstra(G, node), node)

    # Візуалізація графу взаємовідносин
    pos = nx.spring_layout(G, seed=543)
    plt.figure(figsize=(12, 10))
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=4000,
        node_color="skyblue",
        font_size=15,
        width=2,
        font_weight="bold",
    )
    labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()
