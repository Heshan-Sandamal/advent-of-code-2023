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
seed_soil_list = []
soil_fert_list = []
fert_water_list = []
water_light_list = []
light_temp_list = []
temp_humid_list = []
humid_location_list = []

# Get Input
for text in lines[1:]:
    if text.strip() == "":
        continue
    if text == "seed-to-soil map:":
        data = seed_soil_list
        continue
    if text == "soil-to-fertilizer map:":
        data = soil_fert_list
        continue
    if text == "fertilizer-to-water map:":
        data = fert_water_list
        continue
    if text == "water-to-light map:":
        data = water_light_list
        continue
    if text == "light-to-temperature map:":
        data = light_temp_list
        continue
    if text == "temperature-to-humidity map:":
        data = temp_humid_list
        continue
    if text == "humidity-to-location map:":
        data = humid_location_list
        continue
    data.append(list(map(int, text.split())))


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


for val in itertools.count():
    seed = map_destination_to_source(
        seed_soil_list,
        map_destination_to_source(
            soil_fert_list,
            map_destination_to_source(
                fert_water_list,
                map_destination_to_source(
                    water_light_list,
                    map_destination_to_source(
                        light_temp_list,
                        map_destination_to_source(
                            temp_humid_list,
                            map_destination_to_source(humid_location_list, val)
                        ))))))
    if validate_seed_exists(seed):
        print("Min Location", val)
        print("seed", seed)
        break
