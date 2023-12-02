file = open("input.txt")
lines = file.read().splitlines()

input_red_cubes = 12
input_green_cubes = 13
input_blue_cubes = 14


def check_possibility(id, sets):
    for values in sets:
        reds = values["red"]
        blues = values["blue"]
        greens = values["green"]

        if reds > input_red_cubes or greens > input_green_cubes or blues > input_blue_cubes:
            return 0

    print(id, sets)
    return id


total = 0
games = []
for text in lines:
    game = {}
    sets = []

    id = text.split(":")[0].split(" ")[1]
    data = text.split(":")[1]

    for sub in data.split(";"):
        counts = {"red": 0, "blue": 0, "green": 0}
        for pick in sub.split(","):
            pick = pick.strip()
            counts[pick.split(" ")[1]] = int(pick.split(" ")[0])
        sets.append(counts)

    game = {"id": int(id), "sets": sets}
    games.append(game)

print(games)

total = 0
for itr in games:
    total += check_possibility(itr["id"], itr["sets"])

print("Total : ", total)
