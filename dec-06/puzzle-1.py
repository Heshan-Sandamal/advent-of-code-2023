with open("input.txt") as file:
    lines = file.read().splitlines()

times = list(map(int, lines[0].split(":")[1].strip().split()))
distances = list(map(int, lines[1].split(":")[1].strip().split()))

total_ways = 1
for time, distance in zip(times, distances):
    ways = sum(1 for t in range(time) if t * (time - t) > distance)
    total_ways *= ways

print("Total:", total_ways)