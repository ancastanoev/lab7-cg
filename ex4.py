import matplotlib.pyplot as plt
import time

def define_convex_polygons():
    polygon1 = {
        'A': (1.0, 0.0),
        'B': (0.6235, 0.7818),
        'C': (-0.2225, 0.9749),
        'D': (-0.9003, 0.4357),
        'E': (-0.9003, -0.4357),
        'F': (-0.2225, -0.9749),
        'G': (0.6235, -0.7818)
    }

    polygon2 = {
        'A': (2.0, 1.0),
        'B': (3.0, 2.0),
        'C': (4.5, 1.5),
        'D': (4.0, 0.0),
        'E': (3.0, -1.0),
        'F': (1.5, -0.5),
        'G': (0.5, 0.5)
    }

    return [polygon1, polygon2]

def triangulate_polygon(vertices):
    vertex_labels = list(vertices.keys())
    polygon_edges = []

    for i in range(len(vertex_labels)):
        edge = (vertex_labels[i], vertex_labels[(i + 1) % len(vertex_labels)])
        polygon_edges.append(edge)

    anchor = vertex_labels[0]
    for label in vertex_labels[1:]:
        polygon_edges.append((anchor, label))

    return polygon_edges

def assign_vertex_colors(vertices):
    vertex_labels = list(vertices.keys())
    color_scheme = {}
    alternate_colors = ['blue', 'red']

    for idx, label in enumerate(vertex_labels):
        if label == 'A':
            color_scheme[label] = 'yellow'
        else:
            color_scheme[label] = alternate_colors[idx % 2]

    return color_scheme

def visualize_polygon(vertices, edges, coloring, example_idx):
    fig, ax = plt.subplots(figsize=(6, 6))

    for edge in edges:
        start, end = edge
        x_values = [vertices[start][0], vertices[end][0]]
        y_values = [vertices[start][1], vertices[end][1]]
        ax.plot(x_values, y_values, color='black', linewidth=1)

    for label, (x, y) in vertices.items():
        ax.scatter(x, y, color=coloring[label], s=100, zorder=5)
        ax.text(x + 0.1, y + 0.1, label, fontsize=12, color='black')

    ax.set_title(f'Convex Polygon Example {example_idx}', fontsize=14)
    ax.set_aspect('equal')
    ax.axis('off')

    plt.tight_layout()
    plt.show()

def main():
    polygons = define_convex_polygons()

    for i, polygon in enumerate(polygons, start=1):
        edges = triangulate_polygon(polygon)
        colors = assign_vertex_colors(polygon)

        print(f"\n--- Convex Polygon Example {i} ---")
        print("Vertices:")
        for vertex, coord in polygon.items():
            print(f"  {vertex}: {coord}")
        print("Edges:")
        for edge in edges:
            print(f"  {edge}")
        print("Vertex Colors:")
        for vertex, color in colors.items():
            print(f"  {vertex}: {color}")

        visualize_polygon(polygon, edges, colors, i)
        time.sleep(2)

if __name__ == "__main__":
    main()
