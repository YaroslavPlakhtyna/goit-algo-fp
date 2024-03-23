import uuid

import networkx as nx
import matplotlib.pyplot as plt

from collections import deque


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.id = str(uuid.uuid4())


def lighten(color, scale_factor=1.1):
    assert color.startswith("#") and len(color) == 7

    color = color[1:]

    r, g, b = int(color[:2], 16), int(color[2:4], 16), int(color[4:], 16)
    r, g, b = [int(max(min(c * scale_factor, 255), 0)) for c in (r, g, b)]

    return f"#{r:02x}{g:02x}{b:02x}"


def dfs_colorize(graph, node, color):
    def dfs(graph, node, visited=None):
        nonlocal color
        if not visited:
            visited = set()
        visited.add(node)
        graph.nodes[node]["color"] = color
        color = lighten(color)
        for neighbor in graph[node].keys():
            if neighbor not in visited:
                dfs(graph, neighbor, visited)

    dfs(graph, node)


def bfs_colorize(graph, queue, color):
    def bfs(graph, queue, visited=None):
        nonlocal color
        if visited is None:
            visited = set()
        if not queue:
            return
        node = queue.popleft()
        if node not in visited:
            graph.nodes[node]["color"] = color
            color = lighten(color)
            visited.add(node)
            for id in graph[node].keys():
                if id not in visited:
                    queue.extend([id])
        bfs(graph, queue, visited)

    bfs(graph, queue)


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_colorized_trees(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)
    print(pos)
    start_color = "#c53c74"

    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}

    fig, axs = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle("Colorized binary trees", fontsize=16)

    dfs_colorize(tree, tree_root.id, start_color)
    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    axs[0].set_title("DFS")
    plt.subplot(121)
    nx.draw(
        tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors
    )

    bfs_colorize(tree, deque([tree_root.id]), start_color)
    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    axs[1].set_title("BFS")
    plt.subplot(122)
    nx.draw(
        tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors
    )

    plt.show()


if __name__ == "__main__":
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.left.left.left = Node(15)
    root.left.left.right = Node(20)
    root.left.right.left = Node(25)
    root.left.right.right = Node(30)
    root.right = Node(1)
    root.right.left = Node(3)
    root.right.right = Node(6)
    root.right.left.left = Node(9)
    root.right.left.right = Node(12)
    root.right.right.left = Node(16)
    root.right.right.right = Node(18)

    draw_colorized_trees(root)
