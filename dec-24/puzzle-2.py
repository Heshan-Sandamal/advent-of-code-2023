import numpy
import numpy as np
from sympy import *

with open("input.txt") as file:
    lines = file.read().splitlines()

data = []
for line in lines:
    position, velocity = line.split("@")
    position_vector = np.array(list(map(int, position.split(","))), dtype=numpy.float64)
    velocity_vector = np.array(list(map(int, velocity.split(","))), dtype=numpy.float64)
    data.append(({"p": position_vector, "v": velocity_vector}))


# Equation of a line in 3d space is x = x0 + a * t , y = y0 + b * t, z = z0 + c * t
# (x0,y0,z0) - initial positions, (a,b,c) - velocities , t - time
# Inorder to find they are colliding, basically we need to equal the x,y,z coordinates in a particular time
# If check rock collide with first hailstone, then
# x0 + v0x * t1 = x1 + v1x * t1
# y0 + v0y * t1 = y1 + v1y * t1
# z0 + v0z * t1 = z1 + v1z * t1
# Here we have 7 unknown variables which can not be solved using 3 equations
# Hence we need to consider collision with 3 hailstones and build 9 equations to have 9 unknown variables
def calculate(cell1, cell2, cell3):
    x1, y1, z1, v1x, v1y, v1z = cell1["p"][0], cell1["p"][1], cell1["p"][2], cell1["v"][0], cell1["v"][1], cell1["v"][2]
    x2, y2, z2, v2x, v2y, v2z = cell2["p"][0], cell2["p"][1], cell2["p"][2], cell2["v"][0], cell2["v"][1], cell2["v"][2]
    x3, y3, z3, v3x, v3y, v3z = cell3["p"][0], cell3["p"][1], cell3["p"][2], cell3["v"][0], cell3["v"][1], cell3["v"][2]

    x0, y0, z0, t1, t2, t3, v0x, v0y, v0z = symbols(['x0', 'y0', 'z0', 't1', 't2', 't3', 'v0x', 'v0y', 'v0z'])

    # solution function need to have 0 in one side
    # so, x0 + v0x * t1 = x1 + v1x * t1 -----> x0 + v0x * t1 - (x1 + v1x * t1) = 0
    return solve(
        [
            x0 + v0x * t1 - (x1 + v1x * t1),
            y0 + v0y * t1 - (y1 + v1y * t1),
            z0 + v0z * t1 - (z1 + v1z * t1),
            x0 + v0x * t2 - (x2 + v2x * t2),
            y0 + v0y * t2 - (y2 + v2y * t2),
            z0 + v0z * t2 - (z2 + v2z * t2),
            x0 + v0x * t3 - (x3 + v3x * t3),
            y0 + v0y * t3 - (y3 + v3y * t3),
            z0 + v0z * t3 - (z3 + v3z * t3)
        ], [x0, y0, z0, t1, t2, t3, v0x, v0y, v0z]
    )


solution = calculate(
    data[0], data[1], data[2]
)[0]

print(solution)
print("Total", solution[0] + solution[1] + solution[2])
