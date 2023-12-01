file = open("input.txt")
lines = file.read().splitlines()

numberStrings = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def get_string_index(text):
    for idx in range(len(numberStrings)):
        if numberStrings[idx] in text:
            return idx
    return -1


total = 0
for text in lines:
    chars = list(text)
    digits = []
    last_index = 0
    for x in range(len(text)):
        if text[x].isnumeric():
            digits.append(text[x])
            last_index = x + 1
        else:
            index = get_string_index(text[last_index:x + 1])
            if index != -1:
                digits.append(str(index + 1))
                last_index = x - len(numberStrings[index]) + 1

    print(digits)
    number = ''
    length = len(digits)
    if length >= 2:
        number = digits[0] + digits[length - 1]
    elif length == 1:
        number = digits[0] * 2
    else:
        number = 0
    total += int(number)

    print(text, number)
print("Total : ", total)
