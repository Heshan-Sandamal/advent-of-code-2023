with open("input.txt") as file:
    lines = file.read().splitlines()

times = int(lines[0].split(":")[1].strip().replace(" ", ""))
distances = int(lines[1].split(":")[1].strip().replace(" ", ""))

ways = sum([1 for t in range(times) if t * (times - t) > distances])

print("Total", ways)
