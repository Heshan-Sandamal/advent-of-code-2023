import math
from heapq import heappop, heappush

with open("input.txt") as file:
    lines = file.read().splitlines()

start = ()
grid = []
for line in lines:
    grid.append(list(line))

for x in range(len(grid)):
    for y in range(len(grid[x])):
        if (grid[x][y] == "S"):
            start = (x, y)
            grid[x][y] = "."
            break


# Check new x,y are valid cells
def is_valid_move(new_x, new_y):
    map_pos_x = new_x % len(grid[0])
    map_pos_y = new_y % len(grid)
    return (0 <= map_pos_x % len(grid[0]) < len(grid) and 0 <= map_pos_y < len(grid[0]) and grid[map_pos_x][
        map_pos_y] == ".")


# Get Neighbours of the current cell
def get_neighbours(steps, row, column, destination_count):
    neighbours = []
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for direction in directions:
        new_direction = (-direction[1], direction[0])
        new_x = (row + new_direction[0])
        new_y = (column + new_direction[1])
        if (is_valid_move(new_x, new_y) and steps <= destination_count):
            neighbours.append((steps + 1, (new_x, new_y)))
    return neighbours


# This uses the greedy approach to find the optimum path
# Always find the node with least heat loss

def calculate(destination_count):
    condition = 0 if destination_count % 2 == 0 else 1
    visited_nodes = set()
    priority_queue = [(0, start)]
    total = 0
    while priority_queue:
        node = heappop(priority_queue)
        (steps, cell) = node

        if ((cell) in visited_nodes):
            continue

        if (steps <= destination_count and steps % 2 == condition):
            total += 1

        visited_nodes.add(cell)

        neighbours = get_neighbours(steps, cell[0], cell[1], destination_count)
        for neighbour in neighbours:
            heappush(priority_queue, neighbour)
    return total


# It is almost impossible to calculate for steps 26501365 since it takes a lot of when steps > 1000
# But the output seems to have a some pattern specially with the given input grid has a pattern of diamonds
# Which gives a hint that the value can be derived if that pattern is identified
# The pattern can be seen with the differences of calculated  values
# Consider x1,x2...x26501365 as the reachable garden points with  given steps
# then calculate, y1 = x2 - x1, y2 = x3 - x2, z = y2 - y1
# Also, 26501365 = 65 + grid_size *  202300
# Pattern in my grid is, z = 30562 when x = 327 + n * grid_size, from n=0 to n=202298
diff = 0
diffs_list = []
for i in range(65, 800, 131):
    value = calculate(i)
    diffs_list.append(value - diff)
    print("i=" + str(i), "value=", value, "diff=", (value - diff), end=" | ")
    diff = value

print()

# Diffs of diffs
for i in range(len(diffs_list) - 1):
    print("y" + str(i + 1) + "-" + "y" + str(i) + "=", diffs_list[i + 1] - diffs_list[i], end=" , ")

print()

difference_of_y = 30562  # Derived by analyzing the difference between y values after y=2
y = [3896, 30721]  # First y values y0 and y1

# Here the sequence of y values can be generated by adding 30562 to each y after y=2
for i in range(2, 202302):
    y.append(y[i - 1] + 30562)

x = [3896]  # First x value when steps=65
# Then x can be calculated using the above y sequence
# x1 = x0 + y0, x2 = x1 + y1 ...... x26501365 = x26501364 + y26501364

for i in range(0, 202301):
    x.append(x[i] + y[i + 1])

print("Total", x[202300])
