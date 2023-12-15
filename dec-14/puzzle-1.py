with open("input.txt") as file:
    lines = file.read().splitlines()

data = []
for line in lines:
    data.append(list(line))


# generate columns form rows and vice versa
def turn_matrix_90(data):
    new_matrix = [[] for _ in range(len(lines[0]))]
    for line in data:
        for x in range(len(line)):
            new_matrix[x].append(line[x])
    return new_matrix


# Tilt the list
def tilt(data_list):
    new_list, possible_index = data_list[:], 0
    for index, value in enumerate(data_list):
        if (value == "O"):
            if (index != possible_index):
                new_list[possible_index] = "O"
                new_list[index] = "."
            possible_index += 1
        elif (value == "#"):
            possible_index = index + 1
    return new_list


# Tilt the list to north side
def north(data):
    columns = turn_matrix_90(data)
    new_columns = []
    for index, column in enumerate(columns):
        new_columns.append(tilt(column))
    rows = turn_matrix_90(new_columns)
    return rows


# Calculate the load
def calculate_load(data):
    columns = turn_matrix_90(data)
    total = 0
    for x in range(len(columns)):
        for y in range(len(columns[x])):
            if (columns[x][y] == "O"):
                total += (len(columns[x]) - y)
    return total


print(calculate_load(north(data)))
