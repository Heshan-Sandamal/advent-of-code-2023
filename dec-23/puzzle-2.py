import sys

sys.setrecursionlimit(100000000)
with open("input.txt") as file:
    lines = file.read().splitlines()

slopes = [">", "<", "^", "v"]
directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]

# Get Input
grid, start, end = [], (0, 0), ()
for line in lines:
    grid.append(list(line))

# start & end
start = [(0, i) for i, x in enumerate(grid[0]) if x == "."][0]
end = [(len(grid) - 1, i) for i, x in enumerate(grid[len(grid) - 1]) if x == "."][0]


# Check new x,y are valid cells
def is_valid_move(new_x, new_y):
    return (0 <= new_x < len(grid)
            and 0 <= new_y < len(grid[0])
            and (grid[new_x][new_y] == "." or grid[new_x][new_y] in slopes))


# Get neighbours
def get_neighbours(row, column):
    neighbors = []
    for direction in directions:
        new_x, new_y = row + direction[0], column + direction[1]
        if (is_valid_move(new_x, new_y)):
            neighbors.append([new_x, new_y])
    return neighbors


# Get all the intersection nodes which have more than 2 neighbours which acts as the different branches in the tree
def get_all_intersections(grid):
    intersections = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if is_valid_move(i, j) and len(get_neighbours(i, j)) > 2:
                intersections.append((i, j))
    return intersections


# Find the distance per each intersection node
def bfs(start, intersections):
    distances, visited_nodes = {}, set()
    queue = ([(0, start)])
    while queue:
        distance, (x, y) = queue.pop(0)
        if (x, y) in intersections and (x, y) != start:
            distances[(x, y)] = distance
            continue

        for new_x, new_y in get_neighbours(x, y):
            if (new_x, new_y) not in visited_nodes:
                visited_nodes.add((new_x, new_y))
                queue.append((distance + 1, (new_x, new_y)))
    return distances


# Create new graphs for intersection nodes
# Nodes are intersection nodes and edges are weights to travel to other intersection nodes
def create_intersections_graph(intersections):
    graph = {}
    for node in intersections:
        graph[node] = bfs(node, intersections)
    return graph


def get_adjacent_nodes(graph, node):
    return graph[node]


# DFS to go through all possible paths and find the longest path in the new graph
def dfs(graph, node, distance, chain=[]):
    if (node == end): return distance
    if (node in chain): return -1

    chain = chain[:] + [node]
    max_distance = 0

    for key, value in get_adjacent_nodes(graph, node).items():
        max_distance = max(max_distance, (dfs(graph, key, distance + value, chain)))

    return max_distance


# Get all intersections
intersections = get_all_intersections(grid)

# new graph with intersection nodes
graph = create_intersections_graph([start] + intersections + [end])

# Tried the same approach as puzzle-1 using DFS and it never terminated (It should work but don't know when :) :)
# Also tried BFS and also digkistra's with negative edges but did not give the answer
# Hence had to get a hint from reddit to see what can be done to optimize
# Basically since the original graph is too large, we need to convert it into a smaller graph
# Which nodes are the intersections and the edges are the distance between them
# And then we can use the same dfs approach as the first puzzle
print("Longest path distance ", dfs(graph, start, 0, []))
