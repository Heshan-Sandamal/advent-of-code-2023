import sys

sys.setrecursionlimit(100000000)
with open("input.txt") as file:
    lines = file.read().splitlines()

slopes = [">", "<", "^", "v"]
directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

# Get Input
grid, start, end = [], (0, 0), ()
for line in lines:
    grid.append(list(line))

# start & end
start = [(0, i) for i, x in enumerate(grid[0]) if x == "."][0]
end = [(len(grid) - 1, i) for i, x in enumerate(grid[len(grid) - 1]) if x == "."][0]


# Check new x,y are valid cells
def is_valid_move(new_x, new_y):
    return (0 <= new_x < len(grid)
            and 0 <= new_y < len(grid[0])
            and (grid[new_x][new_y] == "." or grid[new_x][new_y] in slopes))


def get_neighbours(steps, row, column):
    neighbors = []
    # if cell is type of slope
    if (grid[row][column] in slopes):
        new_direction = directions[slopes.index(grid[row][column])]
        new_x = row + new_direction[0]
        new_y = column + new_direction[1]
        if (is_valid_move(new_x, new_y)):
            neighbors.append((steps + 1, (new_x, new_y)))
    else:
        # If cell is .
        for direction in directions:
            new_x = row + direction[0]
            new_y = column + direction[1]
            if (is_valid_move(new_x, new_y)):
                neighbors.append((steps + 1, (new_x, new_y)))
    return neighbors


# This is not a scalable approach, But works for puzzle-1 since direction are limited
def dfs(node, distance, chain=[]):
    if (node == end): return distance
    if (node in chain): return -1

    chain = chain[:] + [node]
    max_distance = 0

    for neighbour in get_neighbours(distance, node[0], node[1]):
        max_distance = max(max_distance, (dfs(neighbour[1], neighbour[0], chain)))

    return max_distance


print(dfs(start, 0, []))
