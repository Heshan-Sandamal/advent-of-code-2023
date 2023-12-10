with open("input.txt") as file:
    lines = file.read().splitlines()

instructions = list(lines[0])

values = []
total = 0
dict = {}
for line in lines[2:]:
    key = line.split(" = ")[0]
    left = line.split(" = ")[1].split(", ")[0].strip()[1:]
    right = line.split(" = ")[1].split(", ")[1].strip()[:-1]
    dict[key] = [left, right]


def get_next_element(element, instruction):
    if (instruction == "L"):
        return element[0]
    else:
        return element[1]


count = 0
element = "AAA"
while (True):
    x = instructions[count % len(instructions)]
    count += 1
    element = get_next_element(dict[element], x)
    if (element == "ZZZ"):
        break

print(count)
