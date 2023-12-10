with open("input.txt") as file:
    lines = file.read().splitlines()
from functools import cmp_to_key

chars = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

total = 0
data = []
bid = []
max_rank = len(lines)


# Get count per each item
def get_counts(val):
    counts = {}
    for x in list(val):
        if x in list(counts.keys()):
            counts[x] = counts[x] + 1
        else:
            counts[x] = 1
    return dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))


for line in lines:
    data.append({"val": line.split()[0], "bid": int(line.split()[1]), "counts": get_counts(line.split()[0])})

# Update most common character's count with 'J's counts and remove 'J's count from counts
for value in data:
    counts = value["counts"]
    if 'J' in counts:
        j_count = counts['J']
        if j_count != len(value["val"]):
            del counts['J']
            key = list(counts.keys())[0]
            counts[key] += j_count


def get_idx_of_char(val1, val2):
    idx1, idx2 = 0, 0
    for x, y in zip(list(val1), list(val2)):
        if x != y:
            idx1 = list.index(chars, x)
            idx2 = list.index(chars, y)
            break
    return idx1, idx2


def compare(item1, item2):
    item1_counts = list(item1["counts"].values())
    item2_counts = list(item2["counts"].values())

    min_length = min(len(item1_counts), len(item2_counts))
    for x in range(min_length):
        if item1_counts[x] < item2_counts[x]:
            return -1
        if item1_counts[x] > item2_counts[x]:
            return 1
    indexes = get_idx_of_char(item1["val"], item2["val"])
    if (indexes[0] < indexes[1]):
        return 1  # high index has the lower rank
    return -1


sorted_list = sorted(data, key=cmp_to_key(compare), reverse=True)
print(sorted_list)

total = 0
for x in range(len(sorted_list)):
    total += sorted_list[x]["bid"] * (max_rank - x)
print(total)
