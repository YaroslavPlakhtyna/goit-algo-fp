import heapq

import networkx as nx
import matplotlib.pyplot as plt


def calculate_positions(heap):
    pos = {}
    lvl_width = 1
    curr_idx = 0
    curr_depth = 0
    while curr_idx < len(heap):
        for i in range(lvl_width):
            if curr_idx + i < len(heap):
                pos[curr_idx + i] = (i - lvl_width / 2.0 + 0.5, -curr_depth)
                print(pos[curr_idx + i])
        curr_depth += 1
        curr_idx += lvl_width
        lvl_width *= 2
    return pos


def add_edges(graph, heap):
    for i, value in enumerate(heap):
        graph.add_node(i, color="skyblue", label=value)

    for i in range(1, len(heap)):
        graph.add_edge((i - 1) // 2, i)
    return graph


def draw_heap(heap):
    tree = nx.DiGraph()
    tree = add_edges(tree, heap)

    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(
        tree,
        pos=calculate_positions(heap),
        labels=labels,
        arrows=False,
        node_size=2500,
        node_color=colors,
    )
    plt.show()


if __name__ == "__main__":
    heap = [0, 4, 5, 10, 15, 20, 25, 30, 1, 3, 6, 9, 12, 15, 18]
    heapq.heapify(heap)
    draw_heap(heap)
