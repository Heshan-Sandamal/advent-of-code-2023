with open("input.txt") as file:
    lines = file.read().splitlines()

total = 0
data = []
for line in lines:
    data.append(list(map(int, line.split())))


def calculate_next_value(sequence):
    values = []
    for i in range(1, len(sequence)):
        values.append((sequence[i] - sequence[i - 1]))

    if (len(set(values)) != 1):
        # if all values are not same, call the function again with new range values
        return sequence[len(sequence) - 1] + calculate_next_value(values)
    else:
        # If all values are same, return last element of sequence + range[0] value
        return sequence[len(sequence) - 1] + values[0]


total = 0
for line in data:
    total += calculate_next_value(line)

print("Total", total)
