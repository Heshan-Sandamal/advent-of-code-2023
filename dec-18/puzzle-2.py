from shapely import Polygon

with open("input.txt") as file:
    lines = file.read().splitlines()

grid, inputs = [], []
for line in lines:
    data = line.split(" ")
    inputs.append((data[0], int(data[1]), data[2]))


# Calculate areas of the polygon including the edges
# Bit similar to day 10
# This is a small hack to get the area easily, Need to look at a proper algo for this later
def get_area(cells):
    return int(Polygon(cells).buffer(0.5, join_style=2).area)


grid, start, direction = [], (0, 0), (1, 0)
current, cells = start, [start]
for x in range(len(inputs)):

    value = int(inputs[x][2][2:-2], 16)
    direction_string = str(inputs[x][2][len(inputs[x][2]) - 2])
    steps = value
    new_direction = (0, 0)

    if (direction_string == "0"): new_direction = (0, 1)
    if (direction_string == "2"): new_direction = (0, -1)
    if (direction_string == "1"): new_direction = (1, 0)
    if (direction_string == "3"): new_direction = (-1, 0)

    current = (current[0] + new_direction[0] * steps, current[1] + new_direction[1] * steps)
    cells.append(current)
    direction = new_direction

print(get_area(cells))
