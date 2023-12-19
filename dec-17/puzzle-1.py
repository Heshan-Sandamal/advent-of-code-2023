import sys
from heapq import heappop, heappush

sys.setrecursionlimit(100000000)
with open("input.txt") as file:
    lines = file.read().splitlines()

grid = []
for line in lines:
    grid.append(list(map(int, list(line))))


def is_valid_move(new_x, new_y):
    return 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0])


def get_neighbours(heat_loss, row, column, direction, consecutive_count):
    neighbours = []
    if (direction == (-1, -1)):
        neighbours.append((grid[0][1], (0, 1), (0, 1), consecutive_count + 1))
        neighbours.append((grid[1][0], (1, 0), (1, 0), consecutive_count + 1))
        return neighbours

    # Go straight if consecutive count is less than 3
    if (consecutive_count < 3):
        new_x = row + direction[0]
        new_y = column + direction[1]
        if (is_valid_move(new_x, new_y)):
            distance = heat_loss + grid[new_x][new_y]
            neighbours.append((distance, (new_x, new_y), (direction[0], direction[1]), consecutive_count + 1))

    # Left side cell
    left_direction = (-direction[1], direction[0])
    new_x = row + left_direction[0]
    new_y = column + left_direction[1]
    if (is_valid_move(new_x, new_y)):
        distance = heat_loss + grid[new_x][new_y]
        neighbours.append((distance, (new_x, new_y), (left_direction[0], left_direction[1]), 1))

    # Right side cell
    right_direction = (direction[1], -direction[0])
    new_x = row + right_direction[0]
    new_y = column + right_direction[1]
    if (is_valid_move(new_x, new_y)):
        distance = heat_loss + grid[new_x][new_y]
        neighbours.append((distance, (new_x, new_y), (right_direction[0], right_direction[1]), 1))

    return neighbours


# This uses the greedy approach to find the optimum path
# Always find the node with least heat loss
visited_nodes = set()
priority_queue = [(0, (0, 0), (-1, -1), 0)]

while priority_queue:
    node = heappop(priority_queue)
    (heat_loss, cell, direction, steps) = node

    if cell[0] == len(grid) - 1 and cell[1] == len(grid[0]) - 1:
        print(heat_loss)
        break

    if ((cell, direction, steps) in visited_nodes):
        continue

    visited_nodes.add((cell, direction, steps))

    neighbours = get_neighbours(heat_loss, cell[0], cell[1], direction, steps)
    for neighbour in neighbours:
        heappush(priority_queue, neighbour)
