import itertools

file = open("input.txt")
lines = file.read().splitlines()

seeds = list(map(int, lines[0].split(": ")[1].split()))

# Store ranges for the seed [(start,end),(start,end)
ranges = []
for x in range(0, len(seeds), 2):
    ranges.append((seeds[x], seeds[x] + seeds[x + 1]))

# Holds Data
data = []
temp = []
for text in lines[2:]:
    if "map" in text:
        continue
    if text.strip() == "":
        data.append(temp)
        temp = []
        continue
    temp.append(list(map(int, text.split())))
data.append(temp)


# Map destination -> source
def map_destination_to_source(data_list, num):
    for data in data_list:
        dest, source, count = data
        if dest <= num < dest + count:
            return source + (num - dest)
    return num


# Check whether valid seed exists for the reversely derived seed value
def validate_seed_exists(seed):
    for actual_seed in ranges:
        start, dest = actual_seed
        start = int(start)
        if start <= seed <= dest:
            print(seed, val)
            return True
    return False


# Brute force approach : Checking all the possibilities for location
# To be optimized since this takes some time to provide the answer
for val in itertools.count():
    seed = map_destination_to_source(
        data[0],
        map_destination_to_source(
            data[1],
            map_destination_to_source(
                data[2],
                map_destination_to_source(
                    data[3],
                    map_destination_to_source(
                        data[4],
                        map_destination_to_source(
                            data[5],
                            map_destination_to_source(data[6], val)
                        ))))))
    if validate_seed_exists(seed):
        print("Min Location", val)
        print("seed", seed)
        break
