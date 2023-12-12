with open("input.txt") as file:
    lines = file.read().splitlines()
import itertools

rows = []
patterns = []
for line in lines:
    rows.append(list(line.split(" ")[0]))
    patterns.append(list(map(int, line.split(" ")[1].split(","))))


def generate_contiguous_count_array(lt):
    values = []
    count = 0
    for x in range(len(lt)):
        if (lt[x] == "#"):
            count += 1
            if (x == len(lt) - 1):
                values.append(count)
            continue
        else:
            if (count != 0):
                values.append(count)
            count = 0
    return values


total = 0
for row, pattern in zip(rows, patterns):
    q_count = sum(1 for t in row if t == "?")
    all_permutations = list(itertools.product(['.', '#'], repeat=q_count))
    count = 0
    row_copy = [i for i in row]
    for perm in all_permutations:
        index = 0
        for t in range(len(row)):
            if (row[t] == "?"):
                row_copy[t] = perm[index]
                index += 1
        contiguous_array_response = generate_contiguous_count_array(row_copy)
        if (contiguous_array_response == pattern):
            count += 1
    total += count

print("Total", total)
