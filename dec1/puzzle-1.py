file = open("input.txt")
lines = file.read().splitlines()

total = 0
for text in lines:
    chars = list(text)
    integers = []
    for x in chars:
        if x.isnumeric():
            integers.append(x)

    number = ''
    length = len(integers)
    if length >= 2:
        number = integers[0] + integers[length - 1]
    elif length == 1:
        number = integers[0] * 2
    else:
        number = 0

    total += int(number)

print("Total : ", total)
