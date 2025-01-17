import networkx as nx
import matplotlib.pyplot as plt
from itertools import combinations
import random
import math
import time

def generate_random_positions(num_vertices, spread=10, fixed_points=None):
    positions = {}
    for i in range(num_vertices):
        node = chr(65 + i)
        if fixed_points and node in fixed_points:
            positions[node] = fixed_points[node]
        else:
            positions[node] = (random.uniform(0, spread), random.uniform(0, spread))
    return positions

def generate_convex_positions(num_vertices, center=(0, 0), radius=5):
    positions = {}
    angle_between = 2 * math.pi / num_vertices
    for i in range(num_vertices):
        angle = angle_between * i
        x = center[0] + radius * math.cos(angle)
        y = center[1] + radius * math.sin(angle)
        node = chr(65 + i)
        positions[node] = (x, y)
    return positions

def generate_case_a_graph(num_vertices, cycle_nodes):
    G = nx.Graph()
    G.add_nodes_from(cycle_nodes)
    edges = []
    for i in range(len(cycle_nodes)):
        edge = (cycle_nodes[i], cycle_nodes[(i + 1) % len(cycle_nodes)])
        edges.append(edge)
    G.add_edges_from(edges)
    return G

def generate_case_b_graph():
    G = nx.Graph()
    pos = {
        'A': (3, 3),
        'B': (1, 0),
        'C': (2, 0),
        'D': (4, 0),
        'E': (5, 0)
    }
    G.add_nodes_from(pos.keys())
    edges = [('A', 'B'), ('B', 'C'), ('A','C'),('A', 'D'),('C', 'D'), ('D', 'E'), ('E', 'A')]
    G.add_edges_from(edges)
    node_colors = {
        'A': 'yellow',
        'B': 'black',
        'C': 'red',
        'D': 'black',
        'E': 'red'
    }
    return G, pos, node_colors

def visualize_case_a_graph(G, pos, graph_num):
    plt.figure(figsize=(6, 6))
    nx.draw_networkx_nodes(G, pos, node_color="lightblue", node_shape='o', node_size=800, edgecolors='black', linewidths=2)
    nx.draw_networkx_edges(G, pos, edge_color="black", width=2)
    nx.draw_networkx_labels(G, pos, font_size=15, font_color="white")
    plt.title(f"Case A: Cycle Graph\n(Graph {graph_num})")
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(f"case_a_graph_{graph_num}.png")
    plt.show()
    time.sleep(1.5)

def visualize_case_b_graph(G, pos, node_colors):
    plt.figure(figsize=(8, 6))
    colors = [node_colors[node] for node in G.nodes()]
    nx.draw_networkx_nodes(G, pos, node_color=colors, node_shape='o', node_size=800, edgecolors='black', linewidths=2)
    nx.draw_networkx_edges(G, pos, edge_color="black", width=2)
    nx.draw_networkx_labels(G, pos, font_size=15, font_color="white")
    plt.title("Case B: Collinear Segments as Single Edge")
    plt.axis('off')
    plt.tight_layout()
    plt.savefig("case_b_graph.png")
    plt.show()
    time.sleep(1.5)

def main():
    num_vertices = 5
    cycle_nodes_list = [
        ['A', 'B', 'C', 'D', 'E'],
        ['A', 'C', 'E', 'B', 'D'],
        ['A', 'B', 'D', 'E', 'C']
    ]

    pos_a = generate_convex_positions(num_vertices, center=(0, 0), radius=5)

    for i, cycle_nodes in enumerate(cycle_nodes_list, start=1):
        G_a = generate_case_a_graph(num_vertices, cycle_nodes)
        visualize_case_a_graph(G_a, pos_a, i)

    G_b, pos_b, node_colors_b = generate_case_b_graph()
    visualize_case_b_graph(G_b, pos_b, node_colors_b)

if __name__ == "__main__":
    main()
