with open("input.txt") as file:
    lines = file.read().splitlines()

instructions = list(lines[0])

values = []
total = 0
dict = {}
keys_a = []
keys_z = []

for line in lines[2:]:
    key = line.split(" = ")[0].strip()
    left = line.split(" = ")[1].split(", ")[0].strip()[1:]
    right = line.split(" = ")[1].split(", ")[1].strip()[:-1]
    dict[key] = [left, right]

    if (key.endswith('A')):
        keys_a.append(key)

    if (key.endswith('Z')):
        keys_z.append(key)


def get_next_element(element, instruction):
    if (instruction == "L"):
        return element[0]
    else:
        return element[1]


# This should give the answer but takes a huge time (but gives answer for the small example)
count = 0
while (True):
    x = instructions[count % len(instructions)]
    count += 1
    returns = []
    for i in range(len(keys_a)):
        element = get_next_element(dict[keys_a[i]], x)
        returns.append(element)
        keys_a[i] = element

    if set(returns) == set(keys_z):
        print(returns)
        print(keys_z)
        break

print(count)
