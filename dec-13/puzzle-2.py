import math

with open("input.txt") as file:
    lines = file.read().splitlines()

total, pattern, data = 0, [], []
for line in lines:
    if (line.strip() == ""):
        data.append(pattern)
        pattern = []
        continue
    pattern.append(list(line))
data.append(pattern)

all_columns = []
# Create columns list
for x in range(len(data)):
    columns = [[] for i in range(len(data[x][0]))]
    for pattern in data[x]:
        chars = list(pattern)
        for x in range(len(chars)):
            columns[x].append(chars[x])
    all_columns.append(columns)


#  ------------- Puzzle 1 -------------------
def is_equal_puzzle1(left, right):
    min_l = min(len(left), len(right))
    if (min_l < len(left)):
        left = left[len(left) - min_l:]
    if (min_l < len(right)):
        right = right[:min_l]
    left.reverse()
    return left == right


row_counts_puzzle1 = []
for patterns in data:
    index = 0
    for x in range(1, len(patterns)):
        left, right = patterns[:x], patterns[x:]
        if (is_equal_puzzle1(left, right)): index = x
    row_counts_puzzle1.append(index)

column_counts_puzzle1 = []
for patterns in all_columns:
    index = 0
    for x in range(1, len(patterns)):
        left, right = patterns[:x], patterns[x:]
        if (is_equal_puzzle1(left, right)): index = x
    column_counts_puzzle1.append(index)


# --------------------------------------------------


# Calculate difference of two sides
def calculate_diff(left, right):
    diffs = []
    for index_of_list, (l, r) in enumerate(zip(left, right)):
        # capture element and index of the element where the difference is located
        difference = [(i, index_of_list) for i, (one, two) in enumerate(zip(l, r)) if one != two]
        if (len(difference) > 0): diffs.append(difference)
    return diffs


# Check equality of one & second arrays
def is_equal(left, right):
    min_l = min(len(left), len(right))
    if (min_l < len(left)):
        left = left[len(left) - min_l:]
    elif (min_l < len(right)):
        right = right[:min_l]

    diffs = calculate_diff(left[:], right[::-1])

    # If difference length is equal to 1, then update the left element
    if (diffs and len(diffs[0]) == 1):
        element, index_update = diffs[0][0][1], diffs[0][0][0]
        char = right[::-1][element][index_update]

        left_element = list(left[element])
        left_element[index_update] = char
        left[element] = left_element

        # Recursively call the same function with new left and right elements
        return is_equal(left, right)
    return left == right[::-1]


# Calculate horizontally
row_counts = []
for i, patterns in enumerate(data):
    index = 0
    for x in range(1, len(patterns)):
        left, right = patterns[:x], patterns[x:]
        # Check the two parts are equal and also the location does not equal to location in first part
        if (is_equal(left, right) and row_counts_puzzle1[i] != x):
            index = x
            break
    row_counts.append(index)

# Calculate vertically
column_counts = []
for i, patterns in enumerate(all_columns):
    index = 0
    for x in range(1, len(patterns)):
        left, right = patterns[:x], patterns[x:]
        # Check the two parts are equal and also the location does not equal to location in first part
        if (is_equal(left, right) and column_counts_puzzle1[i] != x):
            index = x
            break
    column_counts.append(index)

# Calculate total
total = 0
for t in range(len(data)):
    row_count, column_count = row_counts[t], column_counts[t]
    if (row_count != 0):
        total += row_count * 100
    else:
        total += column_count

print("total", total)
