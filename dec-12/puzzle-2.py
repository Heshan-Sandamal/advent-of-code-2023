with open("input.txt") as file:
    lines = file.read().splitlines()

rows = []
patterns = []
for line in lines:
    dt = ((line.split(" ")[0] + "?") * 5)[:-1]
    pat = ((line.split(" ")[1] + ",") * 5)[:-1]
    rows.append(list(dt.split(" ")[0]))
    patterns.append(list(map(int, pat.split(","))))

# Took a long time to realize the solution since this cant be solved by brute force, had to write from the scratch again
# definitely need to use an approach which supports dynamic programming model to cache results
# Tricky part is to identify child problems which can be solved to solve the parent problem
# And then the overlapping sub-problems which can be cached

DP = {}


def calculate(rows, blocks, continuous_count, str, in_group=False):
    total = 0
    current = rows[0] if rows else None

    # This is an over-lapping sub-problem
    # For a particular index -> remaining rows, remaining_blocks, current hash count
    # Current continuous_count is important because of adjacent # prior to the current index will have an impact
    # Eg: ....##[sub-problem]
    key = hash((tuple(rows), tuple(blocks), continuous_count))
    if (key in DP):
        return DP[key]

    if (len(rows) == 0):
        # if blocks are zero -> matches the pattern
        # Or the last block should match remaining continuous count
        if (len(blocks) == 0 or (len(blocks)) == 1 and continuous_count == blocks[0]):
            print("match ", str)
            return 1
        else:
            return 0

    # When current cell is a dot
    # 2 scenarios
    #   -> dot could be in a group of # to perform a group Eg: ##.  with this we can terminate the current block
    #   -> it might not be in a group Eg: scenario like ..... which means we are still in the current block
    if (current == "."):
        if (len(blocks) > 0 and blocks[0] == continuous_count):
            # terminate the block
            total += calculate(rows[1:], blocks[1:], 0, str + ".", False)
        elif (in_group == False):
            total += calculate(rows[1:], blocks, 0, str + ".", False)
        else:
            # if dot is inside group and # count does not match the current block
            print("non-match ", str)

    # When current is a hash, we try to form a block but if continuous_count > block then this is not a match
    elif (current == "#"):
        if (len(blocks) > 0 and blocks[0] > continuous_count):
            total += calculate(rows[1:], blocks, continuous_count + 1, str + "#", True)
        else:
            # if hash count exceed the block count, this is not a match
            print("non-match ", str)

    # When current is ?, we need to check the possibilities for both # and .
    else:
        for x in ["#", "."]:
            if (x == "#"):
                if (len(blocks) > 0 and blocks[0] > continuous_count):
                    total += calculate(rows[1:], blocks, continuous_count + 1, str + "#", True)
                else:
                    # if hash count exceed the block count, this is not a match
                    print("non-match ", str)
            else:
                if (len(blocks) > 0 and blocks[0] == continuous_count):
                    total += calculate(rows[1:], blocks[1:], 0, str + ".", False)
                elif (in_group == False):
                    total += calculate(rows[1:], blocks, 0, str + ".", False)
                    # if dot is inside group and # count does not match the current block
                    print("non-match ", str)

    DP[key] = total
    return total


total = 0
for row, pattern in zip(rows, patterns):
    total += calculate(row, pattern, 0, "", False)

print("Total", total)
