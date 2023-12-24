import sys
import numpy
import numpy as np

min_size, max_size = 200000000000000, 400000000000000

with open("input.txt") as file:
    lines = file.read().splitlines()


# Here this formula is derived by formulating the formula for each line
# x = x1 + v1x*t , y = y1 + v1y*t
# Then remove t from above 2 and create a formula for the line something like y = a*x + b using x1,v1x,y1,v1y
# Get the line formulas for a pair
# And then make them equal and find the x and y values of the intersection
def calculate(x1, y1, v1x, v1y, x2, y2, v2x, v2y):
    try:
        x = ((-v1x * v2x * y1 + (v1y * v2x * x1) + v1x * v2x * y2 - v1x * v2y * x2)) / (v1y * v2x - v1x * v2y)
        y = (v1y / v1x) * x + (y1 - (v1y * x1) / v1x)
        return x, y
    except ZeroDivisionError:
        return -sys.maxsize, -sys.maxsize


total = 0
data = []
for line in lines:
    position, velocity = line.split("@")
    position_vector = np.array(list(map(int, position.split(","))), dtype=numpy.float64)
    velocity_vector = np.array(list(map(int, velocity.split(","))), dtype=numpy.float64)
    data.append(({"p": position_vector, "v": velocity_vector}))

intersections = 0
for i, cell in enumerate(data):
    x1, y1, v1x, v1y = cell["p"][0], cell["p"][1], cell["v"][0], cell["v"][1]
    for other_cell in data[i + 1:]:
        x2, y2, v2x, v2y = other_cell["p"][0], other_cell["p"][1], other_cell["v"][0], other_cell["v"][1]

        # Get the intersection point
        x, y = calculate(x1, y1, v1x, v1y, x2, y2, v2x, v2y)

        # Check whether the intersection point falls within the given area
        if (min_size <= x <= max_size and min_size <= y <= max_size):

            # Check whether the point is a forward one by checking new coordinate is in the direction of the velocity
            # Eg: (x - x1) * v1x >0 means point new point's x coordinate is in the v1x direction
            # hence its a forward not a collision in the past
            if ((x - x1) * v1x >= 0 and (y - y1) * v1y >= 0 and (x - x2) * v2x > 0 and (y - y2) * v2y >= 0):
                intersections += 1

print("Intersections", intersections)
