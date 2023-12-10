with open("input.txt") as file:
    lines = file.read().splitlines()
from functools import cmp_to_key

chars = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
values = []


# Get count per each item
def get_count(value):
    counts = {}
    for x in list(value):
        if x in list(counts.keys()):
            counts[x] = counts[x] + 1
        else:
            counts[x] = 1
    return dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))


for line in lines:
    values.append({"value": line.split()[0], "bid": int(line.split()[1]), "counts": get_count(line.split()[0])})


def get_index_of_char(val1, val2):
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
            return 1
        elif item1_counts[x] > item2_counts[x]:
            return -1
    indexes = get_index_of_char(item1["value"], item2["value"])
    if (indexes[0] < indexes[1]):
        return -1
    return 1


sorted_list = sorted(values, key=cmp_to_key(compare))

total = 0
max_rank = len(lines)
for x in range(len(sorted_list)):
    total += sorted_list[x]["bid"] * (max_rank - x)
print(total)
