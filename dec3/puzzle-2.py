file = open("input.txt")
lines = file.read().splitlines()

matrix = []
data = []
for row in lines:
    matrix.append(list(row))
print(matrix)


# Get all adjacent cell to *
# Return [(x,y),(x,y)]
def get_adjacent_cells_indexes(row, col):
    rows, cols = len(matrix), len(matrix[0])

    indexes = []
    for i in range(max(0, row - 1), min(rows, row + 2)):
        for j in range(max(0, col - 1), min(cols, col + 2)):
            if i != row or j != col:
                if is_adj_number_exists(i, j):
                    indexes.append((i, j))
    return indexes


def is_adj_number_exists(x, y):
    return matrix[x][y].isnumeric()


# Create number using left numbers + given cell + right numbers
def get_number(cell_indexes):
    number = matrix[cell_indexes[0]][cell_indexes[1]]
    x = cell_indexes[0]

    # Add Left side of numbers
    i = cell_indexes[1] - 1
    while i >= 0 and matrix[x][i].isnumeric():
        number = str(matrix[x][i]) + str(number)
        i = i - 1

    # Add Right side of numbers
    j = cell_indexes[1] + 1
    while j < len(matrix[x]) and matrix[x][j].isnumeric():
        number = str(number) + str(matrix[x][j])
        j = j + 1

    return {"number": int(number), "row": x, "start_index": i + 1, "end_index": j - 1}


values = []
total = 0
for x in range(len(matrix)):
    row = []
    for y in range(len(matrix[x])):
        if matrix[x][y] == "*":
            all_adjacent_cell_indexes = get_adjacent_cells_indexes(x, y)

            if len(all_adjacent_cell_indexes) >= 2:
                prev = {"number": -1, "start_index": -1, "end_index": -1, "row": -1}
                number_array = []
                for cellIndexes in all_adjacent_cell_indexes:
                    data = get_number(cellIndexes)
                    # Avoid adding the same number in the same row
                    if data["row"] == prev["row"]:
                        if prev["start_index"] != data["start_index"] and prev["end_index"] != data["end_index"]:
                            number_array.append(data["number"])
                            prev = data
                    else:
                        number_array.append(data["number"])
                        prev = data

                if len(number_array) == 2:
                    total += (number_array[0] * number_array[1])
                    row.append(number_array)

    print("row", x, row)
print("Total", total)
