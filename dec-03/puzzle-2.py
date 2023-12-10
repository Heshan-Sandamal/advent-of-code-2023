file = open("input.txt")
lines = file.read().splitlines()

matrix = []
number_obj = []
for row in lines:
    matrix.append(list(row))
print(matrix)


# Get all adjacent cells with numbers to *
# Return [(x,y),(x,y)]
def get_adjacent_cells_with_numbers(row, col):
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
def get_number(cell):
    row = cell[0]
    column = cell[1]
    number = matrix[row][column]

    # Add Left side of numbers
    i = column - 1
    while i >= 0 and matrix[row][i].isnumeric():
        number = str(matrix[row][i]) + str(number)
        i = i - 1

    # Add Right side of numbers
    j = column + 1
    while j < len(matrix[row]) and matrix[row][j].isnumeric():
        number = str(number) + str(matrix[row][j])
        j = j + 1

    return {"number": int(number), "row": row, "start_index": i + 1, "end_index": j - 1}


values = []
total = 0
for x in range(len(matrix)):
    row = []
    for y in range(len(matrix[x])):
        if matrix[x][y] == "*":
            adjacent_cells = get_adjacent_cells_with_numbers(x, y)

            if len(adjacent_cells) >= 2:
                prev = {"number": -1, "start_index": -1, "end_index": -1, "row": -1}
                number_array = []
                for cell in adjacent_cells:
                    number_obj = get_number(cell)
                    # Avoid adding the same number in the same row
                    if number_obj["row"] == prev["row"]:
                        if (prev["start_index"] != number_obj["start_index"]
                                and prev["end_index"] != number_obj["end_index"]):
                            number_array.append(number_obj["number"])
                            prev = number_obj
                    else:
                        number_array.append(number_obj["number"])
                        prev = number_obj

                if len(number_array) == 2:
                    total += (number_array[0] * number_array[1])
                    row.append(number_array)

    print("row", x, row)
print("Total", total)
