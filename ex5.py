import matplotlib.pyplot as plt
import time
from itertools import cycle
from matplotlib.lines import Line2D


def plot_triangulation(examples):
    for example in examples:
        fig, ax = plt.subplots(figsize=(6, 6))
        points = example['points']
        A, B, C, D, E, F = points['A'], points['B'], points['C'], points['D'], points['E'], points['F']
        polygon_points = [A, C, D, E, B, A]
        triangulation_edges = example['triangulation_edges']
        subset_edges = example['subset_edges']

        ax.plot(*zip(*polygon_points), label="Polygon Edges", color="brown")

        # Plot triangulation edges in gray dotted lines
        for edge in triangulation_edges:
            ax.plot(*zip(*edge), linestyle="dotted", color="gray")

        point_color = 'blue'

        for label, (x, y) in points.items():
            ax.scatter(x, y, color=point_color, s=50, zorder=5)
            ax.annotate(label, (x, y), textcoords="offset points", xytext=(5, 5), ha='left', fontsize=10, color="blue")

        if subset_edges:
            for edge in subset_edges:
                ax.plot(*zip(*edge), color="orange", linewidth=2)

        ax.axhline(0, color='black', linewidth=0.5)
        ax.axvline(0, color='black', linewidth=0.5)
        ax.grid(color='gray', linestyle='--', linewidth=0.5)
        ax.set_title(example['title'])
        ax.set_xlabel("X-axis")
        ax.set_ylabel("Y-axis")
        ax.set_aspect('equal', 'box')
        plt.tight_layout()

        custom_lines = [
            Line2D([0], [0], color='brown', lw=2, label='Polygon Edges'),
            Line2D([0], [0], color='gray', linestyle='dotted', lw=2, label='Triangulation Edges'),
            Line2D([0], [0], color='orange', lw=2, label='Subset Triangulation (F-D, B-D & F-B)'),
            Line2D([0], [0], marker='o', color='w', markerfacecolor=point_color, markersize=8, label='Points')
        ]
        ax.legend(handles=custom_lines, loc='upper right', fontsize='small')

        plt.show(block=False)
        time.sleep(3)
        plt.close(fig)


def main():
    examples = []

    example1 = {
        'title': "Example 1",
        'points': {
            'A': (-6.74, 4.36),
            'B': (2.54, 4.72),
            'C': (-8.2, -3.6),
            'D': (3.12, -2.16),
            'E': (2.97, -0.43),
            'F': (-0.15, -0.75)
        },
        'triangulation_edges': [
            ((-0.15, -0.75), (-6.74, 4.36)),
            ((-0.15, -0.75), (2.54, 4.72)),
            ((-0.15, -0.75), (-8.2, -3.6)),
            ((-0.15, -0.75), (3.12, -2.16)),
            ((-0.15, -0.75), (2.97, -0.43))
        ],
        'subset_edges': [
            ((3.12, -2.16), (-0.15, -0.75)),  # F-D
            ((2.54, 4.72), (3.12, -2.16)),  # B-D
            ((-0.15, -0.75), (2.54, 4.72))  # F-B
        ]
    }
    examples.append(example1)

    example3 = {
        'title': "Example 2 (Random) ",
        'points': {
            'A': (6.74, 4.36),
            'B': (-2.54, 4.72),
            'C': (8.2, -3.6),
            'D': (-3.12, -2.16),
            'E': (-2.97, -0.43),
            'F': (0.15, 2.75)
        },
        'triangulation_edges': [
            ((0.15, 2.75), (6.74, 4.36)),
            ((0.15, 2.75), (-2.54, 4.72)),
            ((0.15, 2.75), (8.2, -3.6)),
            ((0.15, 2.75), (-3.12, -2.16)),
            ((0.15, 2.75), (-2.97, -0.43))
        ],
        'subset_edges': [
            ((-3.12, -2.16), (0.15, 2.75)),
            ((-2.54, 4.72), (-3.12, -2.16)),
            ((0.15, 2.75), (-2.54, 4.72))
        ]
    }
    examples.append(example3)

    plot_triangulation(examples)


if __name__ == "__main__":
    main()
