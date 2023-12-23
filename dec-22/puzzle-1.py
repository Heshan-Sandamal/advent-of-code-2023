with open("input.txt") as file:
    lines = file.read().splitlines()

all_cells, mapper, max_height = set(), {}, 0


class Brick():
    def __init__(self, start, end):
        global max_height, all_cells, mapper
        super(Brick, self).__init__()
        self.start = start
        self.end = end
        self.height = end[2] - start[2]
        self.min_x = min(start[0], end[0])
        self.max_x = max(start[0], end[0])
        self.min_y = min(start[1], end[1])
        self.max_y = max(start[1], end[1])
        self.min_z = min(start[2], end[2])
        self.max_z = max(start[2], end[2])
        self.max_height = max(max_height, self.max_z)
        self.cells = []

        # Inorder to check the intersection with another brick, divide the brick into cells
        # Can use the ranges, but this seems much clear & simpler
        for x in range(self.min_x, self.max_x + 1):
            for y in range(self.min_y, self.max_y + 1):
                for z in range(self.min_z, self.max_z + 1):
                    self.cells.append((x, y, z))
                    all_cells.add((x, y, z))
                    mapper[(x, y, z)] = self

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end

    def __hash__(self):
        return hash((tuple(self.start), tuple(self.end)))


# Get input
bricks = []
for i, line in enumerate(lines):
    start, end = line.split("~")
    brick = Brick(list(map(int, start.split(","))), list(map(int, end.split(","))))
    bricks.append(brick)


def is_support_line_exists(cells_of_brick):
    for cell in cells_of_brick:
        if ((cell[0], cell[1], cell[2]) in all_cells):
            return True
    return False


def get_minimum_z_index(brick, min_z):
    global new_bricks_set
    if (len(all_cells) > 0 and min_z > 1):
        # Get coordinates of next lower line
        # There will be no change in x,y when falling. it just changes the z-index only
        cells_of_brick = [(x, y, min_z - 1) for x, y, z in brick.cells]

        # if there is a support line/brick exists, brick can't go further
        if (is_support_line_exists(cells_of_brick) == True):
            return min_z

        # If there is no support line/brick check whether the brick can be lowered more
        return get_minimum_z_index(brick, min_z - 1)
    else:
        return min_z


# Start from the lowest hence sort the bricks by z value
bricks = sorted(bricks, key=lambda x: x.min_z)
print([(x.start, x.end, x.min_z, x.max_z) for x in bricks])

# Starting from the lowest z and try to fall the bricks and generate new locations for bricks
# Populate the first row because these will anyway end up at the bottom
new_bricks_set = set()
for brick in bricks:
    if (brick.min_z == 1):
        br = Brick(brick.start, brick.end)
        new_bricks_set.add(br)


# Fall bricks until they found a support line(another brick)
def fall():
    for brick in bricks:
        new_z = get_minimum_z_index(brick, brick.min_z)
        start, end = brick.start, brick.end
        start[2], end[2] = new_z, new_z + brick.height

        # New brick location
        new_bricks_set.add(Brick(start, end))


# Check whether a brick can be fallen more after removing a particular cell
def try_fall_without_particular_brick(brick):
    for br in new_bricks_set:
        if (br != brick and br.min_z > 1):
            if (get_minimum_z_index(br, br.min_z) != br.min_z):
                return True
    return False


all_cells, mapper = set(), {}
fall()  # Fall the bricks until they reach a support line

new_bricks_set = sorted(new_bricks_set, key=lambda x: x.min_z)
print([(x.start, x.end, x.min_z, x.max_z) for x in new_bricks_set])

count = 0

# Per each brick, see whether if its removed, will any bricks be fallen
for brick in new_bricks_set:
    previous_cells = set(all_cells)  # store previous cells for next iteration
    all_cells = all_cells - set(brick.cells)  # Without current brick's cells
    if (not try_fall_without_particular_brick(brick)):
        count += 1
    all_cells = previous_cells

print("Count", count)
