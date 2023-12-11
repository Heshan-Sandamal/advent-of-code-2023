with open("input.txt") as file:
    lines = file.read().splitlines()

# Capture empty rows
empty_rows = []
for x in range(len(lines)):
    if ("#" not in lines[x]):
        empty_rows.append(x)

# Capture empty columns
empty_columns = []
columns = [[] for i in range(len(lines[0]))]

# Create columns list
for line in lines:
    chars = list(line)
    for x in range(len(chars)):
        columns[x].append(chars[x])

# Add empty column indexes
for x in range(len(columns)):
    if not "#" in ''.join(columns[x]):
        empty_columns.append(x)

# Capture galaxy's locations
galaxies = []
for x in range(len(lines)):
    for y in range(len(lines[x])):
        if (lines[x][y] == "#"):
            galaxies.append((x, y))

print("Galaxies count", len(galaxies))

pairs_list = []
distance = 0
pairs_count = 0
for x in galaxies:
    for y in galaxies:
        # To avoid calculating distance again for same pair
        pairs = sorted([x, y])
        if (x == y) or pairs in pairs_list:
            continue
        else:
            pairs_count += 1
            pairs_list.append(pairs)

            start_x, end_x = x[0], y[0]
            start_y, end_y = x[1], y[1]

            # Distance = difference_of_x + difference_of_y + number_of_empty_rows + number_of_empty_columns

            empty_rows_count = sum([1 for x in empty_rows if min(start_x, end_x) < x < max(start_x, end_x)])
            distance += abs(end_x - start_x) + (empty_rows_count * (1000000 - 1))

            emp_columns_count = sum([1 for y in empty_columns if min(start_y, end_y) < y < max(start_y, end_y)])
            distance += abs(end_y - start_y) + (emp_columns_count * (1000000 - 1))

print("pairs", pairs_count)
print("distance", distance)
