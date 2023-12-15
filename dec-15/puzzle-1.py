with open("input.txt") as file:
    lines = file.read().splitlines()

total = 0
data = []
for line in lines:
    data.extend(line.split(","))


# Generate hash
def hash(total, char):
    total += ord(char)
    return (total * 17) % 256


all_total = 0
for str in data:
    total = 0
    for x in list(str):
        total = hash(total, x)
    all_total += total

print(all_total)
