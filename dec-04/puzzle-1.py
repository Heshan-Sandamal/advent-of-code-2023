file = open("input.txt")
lines = file.read().splitlines()

total = 0
for text in lines:
    data = text.split(":")[1]
    winning = data.split("|")[0].strip().split()
    my_numbers = data.split("|")[1].strip().split()

    value = -1
    matches = []
    for x in my_numbers:
        if x in winning:
            matches.append(x)
            value += 1

    if value != -1:
        total += 2 ** value

print("Total", total)
