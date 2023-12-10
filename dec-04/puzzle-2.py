file = open("input.txt")
lines = file.read().splitlines()

match_counts = []
for text in lines:
    data = text.split(":")[1]
    winning = data.split("|")[0].strip().split()
    my_numbers = data.split("|")[1].strip().split()

    # Get Match Counts
    matches = 0
    for x in my_numbers:
        if x in winning:
            matches += 1
    match_counts.append(matches)

# Get Instances based on match counts
instances = [1 for i in range(len(match_counts))]
for x in range(len(match_counts)):
    match_count = match_counts[x]
    if match_count > 0:
        for y in range(match_count):
            next_index = x + (y + 1)
            if next_index < len(instances):
                instances[next_index] = instances[next_index] + instances[x]

print("Total", sum(instances))
