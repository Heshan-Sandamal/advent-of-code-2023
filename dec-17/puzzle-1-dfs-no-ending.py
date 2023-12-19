import sys

sys.setrecursionlimit(100000000)
with open("input.txt") as file:
    lines = file.read().splitlines()

grid = []
for line in lines:
    grid.append(list(map(int, list(line))))

rows_length, columns_length = len(grid), len(grid[0])

direction = (0, 1)
visited = {}
cache = {}
heat_lost = {}


def is_valid_move(new_x, new_y, heat_lost):
    return 0 <= new_x < len(grid) and 0 <= new_y < len(grid[0])


# should have not used brute force DFS for searching this much which seems not giving the answer for a large grid
# Tried to use DFS + memorization but did not work
def calculate(grid, row, column, direction, consec, chain, distance):
    node = (row, column)
    cache_data = (row, column, direction)

    if (node in chain or len(chain) > 100):
        return sys.maxsize

    heat = grid[row][column]
    # if (node in heat_lost and heat_lost[node] < sum(distance + [heat])):
    #     return sys.maxsize

    chain = chain[:]
    if (row == rows_length - 1 and column == columns_length - 1):
        chain.append((node))
        visited[node] = grid[row][column]
        return grid[row][column]

    if 0 <= row < rows_length and 0 <= column < columns_length:
        chain.append((node))

        heat = grid[row][column]
        straight, left, right = sys.maxsize, sys.maxsize, sys.maxsize
        consec_length = consec + 1

        if (consec_length < 3):
            new_x = row + direction[0]
            new_y = column + direction[1]
            if (is_valid_move(new_x, new_y, distance + [heat])):
                straight = calculate(grid, new_x, new_y, direction, consec + 1, chain,
                                     distance + [heat])

        left_direction = (-direction[1], direction[0])
        new_x = row + left_direction[0]
        new_y = column + left_direction[1]
        if (is_valid_move(new_x, new_y, distance + [heat])):
            left = calculate(grid, new_x, new_y, left_direction, 0, chain, distance + [heat])

        right_direction = (direction[1], -direction[0])
        new_x = row + right_direction[0]
        new_y = column + right_direction[1]
        if (is_valid_move(new_x, new_y, distance + [heat])):
            right = calculate(grid, new_x, new_y, right_direction, 0, chain, distance + [heat])

        minV = min(left, right, straight)
        heat_loss_value = minV + heat
        visited[node] = heat_loss_value
        cache[cache_data] = heat_loss_value
        if (node not in heat_lost or heat_lost[node] > heat_loss_value):
            heat_lost[(row, column)] = heat_loss_value
        return minV + heat

    chain.append(node)
    cache[cache_data] = sys.maxsize
    visited[node] = sys.maxsize
    return sys.maxsize


value = calculate(grid, 0, 0, (0, 1), -1, [()], [])
print("Total", value - grid[0][0])
