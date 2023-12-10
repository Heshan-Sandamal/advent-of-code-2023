from matplotlib.path import Path

with open("input.txt") as file:
    lines = file.read().splitlines()

data = []
for line in lines:
    data.append(list(line))

# Identify start node
start = (0, 0)
for x in range(len(data)):
    for y in range(len(data[0])):
        if (data[x][y] == 'S'):
            start = (x, y)
            break
print("Start", start)


# Move based on the pipe ( For a given pipe, the movement direction is determined by the previous cell's position )
# Eg: for | , if previous cell's row < current row , the movement is downwards else upwards
def move(x, y, prev_x, prev_y):
    current_x, current_y = x, y
    cell = data[x][y]
    if (cell == "|"):
        if (prev_x < x):
            x += 1
        else:
            x -= 1
    elif (cell == "-"):
        if (prev_y < y):
            y += 1
        else:
            y -= 1
    elif (cell == "L"):
        if (x > prev_x):
            y += 1
        else:
            x -= 1
    elif (cell == "J"):
        if (x > prev_x):
            y -= 1
        else:
            x -= 1
    elif (cell == "7"):
        if (prev_y < y):
            x += 1
        elif (x < prev_x):
            y -= 1
    elif (cell == "F"):
        if (x < prev_x):
            y += 1
        else:
            x += 1
    return x, y, current_x, current_y


# Stores the path
cells = []

# Start & Initial move
x, y = start
cells.append((x, y))
cells.append((x - 1, y))
x, y, previous_x, previous_y = move(x - 1, y, x, y)
cells.append((x, y))

count = 2
while (True):
    x, y, previous_x, previous_y = move(x, y, previous_x, previous_y)
    count += 1
    cells.append((x, y))
    if (data[x][y] == "S"):
        break

p = Path(cells)
total = 0
for y in range(len(lines)):
    for x in range(len(lines[0])):
        if (x, y) in cells:
            continue
        # Checks the tile falls inside the area covered by the cells
        """ todo: Need to come up with the internal logic instead of using matplotlib to check whether the point falls within the area 
        (however, this works perfectly) """
        if p.contains_point((x, y)):
            total += 1

print("Total tiles", total)
