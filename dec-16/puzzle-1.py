import sys
sys.setrecursionlimit(100000000)

with open("input.txt") as file:
    lines = file.read().splitlines()

grid = []
for line in lines:
    grid.append(list(line))

rows_length, columns_length = len(grid), len(grid[0])

# directions right = (0,1) , left = (0,-1) , up => (-1,0) , down -> (1,0)
row, column, direction = 0, 0, (0, 1)

energized_tiles, all_traversed = [], []


# Travers the grid
def traverse(row, column, direction):
    global energized_tiles
    if 0 <= row < rows_length and 0 <= column < columns_length:
        cell, cell_point = grid[row][column], (row, column)

        energized_tiles.append(cell_point)
        if ((cell_point, direction) in all_traversed):
            return
        else:
            all_traversed.append((cell_point, direction))

        if (cell == "."):
            traverse(row + direction[0], column + direction[1], direction)
        elif (cell == "/"):
            new_direction = (-direction[1], -direction[0])
            traverse(row + new_direction[0], column + new_direction[1], new_direction)
        elif cell == '\\':
            new_direction = (direction[1], direction[0])
            traverse(row + new_direction[0], column + new_direction[1], new_direction)
        elif (cell == "|"):
            # horizontal
            if (direction[0] == 0):
                new_direction1 = (-direction[1], -direction[0])
                new_direction2 = (direction[1], direction[0])
                traverse(row + new_direction1[0], column + new_direction1[1], new_direction1)
                traverse(row + new_direction2[0], column + new_direction2[1], new_direction2)
            else:
                # Vertical (no change in direction)
                traverse(row + direction[0], column + direction[1], direction)
        elif (cell == "-"):
            # Vertical
            if (direction[1] == 0):
                new_direction1 = (-direction[1], -direction[0])
                new_direction2 = (direction[1], direction[0])
                traverse(row + new_direction1[0], column + new_direction1[1], new_direction1)
                traverse(row + new_direction2[0], column + new_direction2[1], new_direction2)
            else:
                # horizontal (no change in direction)
                traverse(row + direction[0], column + direction[1], direction)


traverse(0, 0, (0, 1))
print(len(set(energized_tiles)))
