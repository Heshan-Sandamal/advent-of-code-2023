with open("input.txt") as file:
    lines = file.read().splitlines()

total = 0
data = []
for line in lines:
    data.append(list(map(int, line.split())))


def calculate_previous(sequence):
    values = []
    for i in range(1, len(sequence)):
        values.append((sequence[i] - sequence[i - 1]))

    if (len(set(values)) != 1):
        # if all values are not same, call the function again with new range values
        return sequence[0] - calculate_previous(values)
    else:
        # If all values are same, return first element of sequence - range[0] value
        return sequence[0] - values[0]


total = 0
for line in data:
    total += calculate_previous(line)
print("Total", total)
