with open("input.txt") as file:
    lines = file.read().splitlines()

# Read rows
total, pattern, data = 0, [], []
for line in lines:
    if (line.strip() == ""):
        data.append(pattern)
        pattern = []
        continue
    pattern.append(line)
data.append(pattern)

# Create columns list
all_columns = []
for x in range(len(data)):
    columns = [[] for i in range(len(data[x][0]))]
    for pattern in data[x]:
        chars = list(pattern)
        for x in range(len(chars)):
            columns[x].append(chars[x])
    all_columns.append(columns)


# Check equality of one & second arrays
def is_equal(left, right):
    min_l = min(len(left), len(right))
    if (min_l < len(left)): left = left[len(left) - min_l:]
    if (min_l < len(right)): right = right[:min_l]
    return left[::-1] == right


# Calculate rows
row_counts = []
for patterns in data:
    index = 0
    for x in range(1, len(patterns)):
        left, right = patterns[:x], patterns[x:]
        if (is_equal(left, right)): index = x
    row_counts.append(index)

# Calculate columns
column_counts = []
for patterns in all_columns:
    index = 0
    for x in range(1, len(patterns)):
        left, right = patterns[:x], patterns[x:]
        if (is_equal(left, right)): index = x
    column_counts.append(index)

# Calculate total
total = 0
for t in range(len(data)):
    horizontal_location, vertical_location = row_counts[t], column_counts[t]
    if (horizontal_location != 0):
        total += horizontal_location * 100
    else:
        total += vertical_location

print("total", total)
