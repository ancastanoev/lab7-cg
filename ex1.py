import turtle
import math

def draw_polygon(points, color):
    turtle.penup()
    turtle.goto(points[0])
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for point in points[1:]:
        turtle.goto(point)
    turtle.goto(points[0])
    turtle.end_fill()
    turtle.update()

def scale_points(points, scale):
    return [(x * scale, y * scale) for x, y in points]

def find_intersection(ray_start, ray_end, seg_start, seg_end):
    x1, y1 = ray_start
    x2, y2 = ray_end
    x3, y3 = seg_start
    x4, y4 = seg_end
    denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if abs(denom) < 1e-6:
        return None
    t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / denom
    u = ((x1 - x3) * (y1 - y2) - (y1 - y3) * (x1 - x2)) / denom
    if 0 <= t <= 1 and 0 <= u <= 1:
        intersect_x = x1 + t * (x2 - x1)
        intersect_y = y1 + t * (y2 - y1)
        return intersect_x, intersect_y
    return None

def rotate_ray(center, radius, steps, polygon):
    angle_step = 360 / steps
    for step in range(steps):
        angle = math.radians(step * angle_step)
        ray_end = (
            center[0] + radius * math.cos(angle),
            center[1] + radius * math.sin(angle),
        )
        closest_intersection = None
        min_distance = float("inf")
        for i in range(len(polygon)):
            seg_start = polygon[i]
            seg_end = polygon[(i + 1) % len(polygon)]
            intersection = find_intersection(center, ray_end, seg_start, seg_end)
            if intersection:
                dist = math.sqrt((intersection[0] - center[0]) ** 2 + (intersection[1] - center[1]) ** 2)
                if dist < min_distance:
                    min_distance = dist
                    closest_intersection = intersection
        if closest_intersection:
            turtle.penup()
            turtle.goto(center)
            turtle.pendown()
            turtle.goto(closest_intersection)
            turtle.update()
        turtle.color("blue")
        turtle.speed(0.5)

def main():
    turtle.setup(width=1200, height=800)
    turtle.speed(0)
    turtle.tracer(0, 0)
    scale_factor = 20
    points = [
        (4, -4), (6, -4), (9, -6), (11, -6), (11, 6),
        (9, 6), (6, 4), (4, 4),
        (-5, 6), (-7, 4), (-7, -4), (-5, -6)
    ]
    points = scale_points(points, scale_factor)
    interior_point = (2 * scale_factor, 0 * scale_factor)
    draw_polygon(points, "lightgray")
    turtle.penup()
    turtle.color("blue")
    for i, point in enumerate(points, start=1):
        turtle.goto(point)
        turtle.dot(10)
        turtle.write(f"P{i}", align="left", font=("Arial", 14, "normal"))
    turtle.update()
    turtle.goto(interior_point)
    turtle.dot(12, "red")
    turtle.write("Camera", align="left", font=("Arial", 14, "bold"))
    turtle.update()
    turtle.tracer(1)
    rotate_ray(interior_point, 20 * scale_factor, 360, points)
    turtle.done()

if __name__ == "__main__":
    main()
