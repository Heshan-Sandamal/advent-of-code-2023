import sys
from heapq import heappop, heappush

sys.setrecursionlimit(100000000)
with open("input.txt") as file:
    lines = file.read().splitlines()

# Get Input
grid, start = [], ()
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
    return (0 <= new_x < len(grid) and 0 <= new_y < len(grid[0]) and grid[new_x][new_y] == ".")


# Get Neighbours of the current cell
def get_neighbours(steps, row, column):
    neighbors = []
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for direction in directions:
        new_direction = (-direction[1], direction[0])
        new_x = row + new_direction[0]
        new_y = column + new_direction[1]
        if (is_valid_move(new_x, new_y) and steps <= 64):
            neighbors.append((steps + 1, (new_x, new_y)))
    return neighbors


# BFS to find the nodes
visited_nodes = set()
priority_queue = [(0, start)]
nodes = set()
while priority_queue:
    node = heappop(priority_queue)
    (steps, cell) = node

    if ((cell) in visited_nodes):
        continue

    # <= & %2 is because if this cell is visited and steps count is even then it can have a loop and come to same cell
    if (steps <= 64 and steps % 2 == 0):
        nodes.add(cell)

    visited_nodes.add((cell))

    neighbours = get_neighbours(steps, cell[0], cell[1])
    for neighbour in neighbours:
        heappush(priority_queue, neighbour)

print(sorted(nodes))
print(len(nodes))
