file = open("input.txt")
lines = file.read().splitlines()

matrix = []
data = []
for row in lines:
    matrix.append(list(row))
print(matrix)


def is_symbol(x, y):
    return not matrix[x][y].isnumeric() and not matrix[x][y] == "."


def is_adjacent_symbol_exists(row, col):
    rows, cols = len(matrix), len(matrix[0])

    for i in range(max(0, row - 1), min(rows, row + 2)):
        for j in range(max(0, col - 1), min(cols, col + 2)):
            if i != row or j != col:
                if is_symbol(i, j):
                    return True
    return False


# Create Adjacent matrix indicating whether a symbol exists or not
adjacent_matrix = []
for x in range(len(matrix)):
    row = []
    for y in range(len(matrix[x])):
        if matrix[x][y].isnumeric():
            row.append(is_adjacent_symbol_exists(x, y))
        else:
            row.append(False)
    adjacent_matrix.append(row)

numbers = []
total = 0
for x in range(len(matrix)):
    num = ''
    adjacent_exists = False
    for y in range(len(matrix[x])):

        cell = matrix[x][y]
        if cell.isnumeric():
            num += cell
            adjacent_exists = adjacent_exists or adjacent_matrix[x][y]

            # for last row
            if adjacent_exists and y == len(matrix[x]) - 1:
                numbers.append(int(num))
                total += int(num)
        else:
            if adjacent_exists:
                numbers.append(int(num))
                total += int(num)
            num = ''
            adjacent_exists = False

print(numbers)
print("Total", total)
