file = open("input.txt")
lines = file.read().splitlines()

redCubes = 12
greenCubes = 13
blueCubes = 14


def check_possibility(id, sets):
    for set in sets:
        reds = set["red"]
        blues = set["blue"]
        greens = set["green"]

        if reds > redCubes or greens > greenCubes or blues > blueCubes:
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
