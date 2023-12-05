file = open("input.txt")
lines = file.read().splitlines()

seeds = list(map(int, lines[0].split(": ")[1].split()))
print(seeds)

# Holds data
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


# Map source -> destination
def map_values(data_list, number):
    for data in data_list:
        dest, source, length = data
        if number == source:
            return dest
        elif source < number <= source + length:
            return dest + (number - source)
    return number


lt = []
for seed in seeds:
    lt.append(map_values(
        humid_location_list,
        map_values(
            temp_humid_list,
            map_values(
                light_temp_list,
                map_values(
                    water_light_list,
                    map_values(
                        fert_water_list,
                        map_values(
                            soil_fert_list,
                            map_values(seed_soil_list, seed)
                        )))))))

print("min", min(lt))
