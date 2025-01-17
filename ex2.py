import turtle
import math
import time

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
    cx, cy = center
    angle_step = 360 / steps
    for step in range(steps):
        angle = math.radians(step * angle_step)
        ray_end = (
            cx + radius * math.cos(angle),
            cy + radius * math.sin(angle),
        )

        closest_intersection = None
        min_distance = float("inf")
        for i in range(len(polygon)):
            seg_start = polygon[i]
            seg_end = polygon[(i + 1) % len(polygon)]
            intersection = find_intersection(center, ray_end, seg_start, seg_end)
            if intersection:
                dist = math.sqrt((intersection[0] - cx) ** 2 + (intersection[1] - cy) ** 2)
                if dist < min_distance:
                    min_distance = dist
                    closest_intersection = intersection

        if closest_intersection:
            turtle.penup()
            turtle.goto(center)
            turtle.pendown()
            turtle.goto(closest_intersection)
            turtle.update()

def draw_diagonal(p1, p2):
    turtle.penup()
    turtle.goto(p1)
    turtle.pendown()
    turtle.color("red")
    turtle.goto(p2)
    turtle.color("blue")

def main():
    turtle.setup(width=1500, height=700)
    turtle.speed(0.6)
    turtle.tracer(0, 0)
    time.sleep(1)

    scale_factor = 30

    points = [
        (0, 5), (-1, -2), (3, -2), (3, 0), (3, 2), (1, 2)
    ]
    points = scale_points(points, scale_factor)

    turtle.clear()
    interior_point_a = (1 * scale_factor, 1 * scale_factor)
    draw_polygon(points, "lightgray")

    turtle.penup()
    turtle.color("blue")
    for i, point in enumerate(points, start=1):
        turtle.goto(point)
        turtle.dot(10)
        turtle.write(f"P{i}", align="left", font=("Arial", 14, "normal"))

    turtle.color("red")
    turtle.goto(interior_point_a)
    turtle.dot(12, "red")
    turtle.write("Camera A", align="left", font=("Arial", 10, "normal"))

    turtle.color("blue")
    rotate_ray(interior_point_a, 20 * scale_factor, 360, points)

    turtle.penup()
    turtle.goto(-300, -250)
    turtle.color("black")
    turtle.write("Case (a): Single Camera with Rotating Ray", align="left", font=("Arial", 16, "bold"))

    turtle.update()
    time.sleep(4)

    turtle.clear()
    draw_polygon(points, "lightgray")

    draw_diagonal(points[1], points[5])

    turtle.color("blue")
    for i, point in enumerate(points, start=1):
        turtle.goto(point)
        turtle.dot(10)
        turtle.write(f"P{i}", align="left", font=("Arial", 14, "normal"))

    region1 = [points[0], points[1], points[5]]
    region2 = [points[1], points[5], points[4], points[3], points[2]]

    camera_b1 = (0.2 * scale_factor, 3.5 * scale_factor)
    camera_b2 = (2 * scale_factor, 1.5 * scale_factor)

    turtle.color("red")
    turtle.penup()
    turtle.goto(camera_b1)
    turtle.dot(12, "red")
    turtle.write("Camera 1", align="left", font=("Arial", 10, "normal"))
    rotate_ray(camera_b1, 15 * scale_factor, 360, region1)

    turtle.color("green")
    turtle.penup()
    turtle.goto(camera_b2)
    turtle.dot(12, "green")
    turtle.write("Camera 2", align="left", font=("Arial", 10, "normal"))
    rotate_ray(camera_b2, 15 * scale_factor, 360, region2)

    turtle.penup()
    turtle.goto(-300, -250)
    turtle.color("black")
    turtle.write("Case (b): Two Cameras with Diagonal (P2-P6) and Rotating Rays", align="left", font=("Arial", 16, "bold"))

    turtle.update()
    turtle.done()

if __name__ == "__main__":
    main()
