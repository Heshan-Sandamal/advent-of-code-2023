import numpy as np
from shapely import Polygon

with open("input.txt") as file:
    lines = file.read().splitlines()

grid, inputs = [], []
for line in lines:
    dt = line.split(" ")
    inputs.append((dt[0], int(dt[1]), dt[2]))


# Calculate areas of the polygon including the edges
# Bit similar to day 10
# This is a small hack to get the area easily, Need to look at a proper algo for this later
def get_area(cells):
    return int(Polygon(cells).buffer(0.5, join_style=2).area)

def PolyArea(x,y):
    return 0.5*np.abs(np.dot(x,np.roll(y,1))-np.dot(y,np.roll(x,1)))

# Calculate Path
grid, start, direction = [], (0, 0), (1, 0)
current, cells = start, [start]
for x in range(len(inputs)):
    directionS, steps, color = inputs[x][0], int(inputs[x][1]), inputs[x][2]
    new_direction = (0, 0)

    if (directionS == "R"): new_direction = (0, 1)
    if (directionS == "L"): new_direction = (0, -1)
    if (directionS == "D"): new_direction = (1, 0)
    if (directionS == "U"): new_direction = (-1, 0)

    for x in range(steps):
        current = (current[0] + new_direction[0] * 1, current[1] + new_direction[1] * 1)
        cells.append(current)
    direction = new_direction

print(get_area(cells))
