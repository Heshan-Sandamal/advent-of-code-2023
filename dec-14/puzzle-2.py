with open("input.txt") as file:
    lines = file.read().splitlines()

total = 0
data = []
rocks = []
for line in lines:
    data.append(list(line))


# Create columns list
def turn_data_90(data):
    columns = [[] for i in range(len(lines[0]))]
    for row in data:
        for x in range(len(row)):
            columns[x].append(row[x])
    return columns


# Reverse the data in the matrix
def reverse(data):
    rows = []
    for row in data:
        new_row = row
        new_row.reverse()
        rows.append(new_row)
    return rows


# Tilt row
def tilt_row(row):
    new_row = row[:]
    possible_index = 0
    for index, value in enumerate(row):
        if (value == "O"):
            if (index != possible_index):
                new_row[possible_index] = "O"
                new_row[index] = "."
            possible_index += 1
        elif (value == "#"):
            possible_index = index + 1
    return new_row


# Tilt north
def north(data):
    columns = turn_data_90(data)
    new_columns = []
    for index, col in enumerate(columns):
        new_columns.append(tilt_row(col))
    return turn_data_90(new_columns)


# Tile west
def west(data):
    new_rows = []
    for index, col in enumerate(data):
        new_rows.append(tilt_row(col))
    return new_rows


# Tile South (reverse the columns -> tile north -> reverse the output -> generate rows)
def south(data):
    columns = reverse(turn_data_90(data))
    new_columns = []
    for col in enumerate(columns):
        new_columns.append(tilt_row(col))
    return turn_data_90(reverse(new_columns))


# Tilt east
def east(data):
    rows = reverse(data)
    new_rows = []
    for index, col in enumerate(rows):
        new_rows.append(tilt_row(col))
    return reverse(new_rows)


# Calculate load
def calculate_load(data):
    columns = turn_data_90(data)
    total = 0
    for x in range(len(columns)):
        for y in range(len(columns[x])):
            if (columns[x][y] == "O"):
                total += (len(columns[x]) - y)
    return total


cache = {}
i = 1
while (i <= 1000000000):
    hash_of_data = hash(str(data))
    # After the first hit in the cache, the same pattern continues so no need of iterating further
    if (hash_of_data in cache):
        index = list(cache.keys()).index(hash_of_data)
        remaining_iterations = (1000000000 - i) % (len(cache) - index)
        cache_sub_list = list(cache.values())[index:]
        # Answer
        print(calculate_load(cache_sub_list[(remaining_iterations) % len(cache_sub_list)]))
        break
    else:
        data = east(south(west(north(data))))
        cache[hash_of_data] = data
    i += 1
