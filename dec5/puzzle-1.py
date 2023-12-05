file = open("input.txt")
lines = file.read().splitlines()

seeds = list(map(int, lines[0].split(": ")[1].split()))
print(seeds)

# Get Input
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


# Map source -> destination
def map_values(data_list, number):
    for data in data_list:
        dest, source, length = data
        if number == source:
            return dest
        elif source < number <= source + length:
            return dest + (number - source)
    return number


print(len(data))

lt = []
for seed in seeds:
    lt.append(map_values(
        data[6],
        map_values(
            data[5],
            map_values(
                data[4],
                map_values(
                    data[3],
                    map_values(
                        data[2],
                        map_values(
                            data[1],
                            map_values(data[0], seed)
                        )))))))

print("min", min(lt))
