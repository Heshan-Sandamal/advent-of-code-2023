file = open("input.txt")
lines = file.read().splitlines()


def get_power(sets):
    min_reds = 0
    min_blues = 0
    min_greens = 0

    for values in sets:
        reds = values["red"]
        blues = values["blue"]
        greens = values["green"]

        if reds > min_reds:
            min_reds = reds
        if greens > min_greens:
            min_greens = greens
        if blues > min_blues:
            min_blues = blues

    return min_reds * min_blues * min_greens


total = 0
games = []
for text in lines:
    game = {}
    sets = []

    id = text.split(":")[0].split(" ")[1]
    data = text.split(":")[1]

    for sub in data.split(";"):
        dict = {"red": 0, "blue": 0, "green": 0}
        for pick in sub.split(","):
            pick = pick.strip()
            dict[pick.split(" ")[1]] = int(pick.split(" ")[0])
        sets.append(dict)

    game = {"id": int(id), "sets": sets}
    games.append(game)

print(games)

total = 0
for itr in games:
    total += get_power(itr["sets"])

print("Total : ", total)
