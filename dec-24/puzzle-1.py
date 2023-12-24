import sys

import numpy
import numpy as np

with open("input.txt") as file:
    lines = file.read().splitlines()

given_size = (200000000000000, 400000000000000)


def calculate(x1, y1, v1x, v1y, x2, y2, v2x, v2y):
    try:
        x = ((-v1x * v2x * y1 + (v1y * v2x * x1) + v1x * v2x * y2 - v1x * v2y * x2)) / (v1y * v2x - v1x * v2y)
        y = (v1y / v1x) * x + (y1 - (v1y * x1) / v1x)
        # y2 = (v2y * x) / v2x + (y2 - v2y * x2 / v2x)
        return x, y
    except ZeroDivisionError:
        return -sys.maxsize, -sys.maxsize


def equation_of_line(x0, y0, vx, vy):
    slope = vy / vx
    intercept = y0 - slope * x0
    return f"y = {slope} * x + {intercept}"


total = 0
data = []
for line in lines:
    position, velocity = line.split("@")
    position_vector = np.array(list(map(int, position.split(","))),dtype=numpy.float64)
    velocity_vector = np.array(list(map(int, velocity.split(","))),dtype=numpy.float64)

    data.append(({"p": position_vector, "v": velocity_vector}))

print(data)

intersections = 0
for i, cell in enumerate(data):
    x1, y1, v1x, v1y = cell["p"][0], cell["p"][1], cell["v"][0], cell["v"][1]
    other_cells = data[i + 1:]
    for other_cell in other_cells:
        x2, y2, v2x, v2y = other_cell["p"][0], other_cell["p"][1], other_cell["v"][0], other_cell["v"][1]
        x, y = calculate(x1, y1, v1x, v1y, x2, y2, v2x, v2y)

        if (given_size[0] <= x <= given_size[1] and given_size[0] <= y <= given_size[1]):
            if ((x - x1) * v1x >= 0 and (y - y1) * v1y >= 0 and (x - x2) * v2x > 0 and (y - y2) * v2y >= 0):
                intersections += 1

print("Intersections", intersections)
