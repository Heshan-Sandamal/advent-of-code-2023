with open("input.txt") as file:
    lines = file.read().splitlines()

data = []
str_list = lines[0].split(",")
for lens in str_list:
    if ("=" in lens):
        data.append({"label": lens.split("=")[0], "focal": lens.split("=")[1], "operation": "="})
    elif ("-" in lens):
        data.append({"label": lens.split("-")[0], "focal": None, "operation": "-"})


# Generate hash for the lens
def hash(str):
    total = 0
    for char in list(str):
        total += ord(char)
        total = (total * 17) % 256
    return total


# Check whether the lens includes in the box
def contains_lens(box, lens):
    for index, lens_in_box in enumerate(box):
        if (lens_in_box["label"] == lens["label"]):
            return index
    return -1


# Add / remove lens from the boxes
boxes = [[] for i in range(256)]
all_total = 0
for lens in data:
    box_number = hash(lens["label"])
    operation = lens["operation"]
    if (operation == "="):
        box = boxes[box_number]
        index = contains_lens(box, lens)
        if (index == -1):
            box.append(lens)
        else:
            box[index] = lens
    elif (operation == "-"):
        box = boxes[box_number]
        index = contains_lens(box, lens)
        if (index != -1):
            del box[index]

# Calculate total
total = 0
for index, box in enumerate(boxes):
    if (len(box) > 0):
        value = 0
        for index_in_box, lens in enumerate(box):
            value += (index + 1) * (index_in_box + 1) * int(lens["focal"])
        total += value

print(total)
