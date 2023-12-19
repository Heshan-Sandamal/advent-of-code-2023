from anytree import NodeMixin, RenderTree, PreOrderIter

with open("input.txt") as file:
    lines = file.read().splitlines()


# Node details
class WNode(NodeMixin):
    def __init__(self, foo, parent=None, condition=None):
        super(WNode, self).__init__()
        self.foo = foo
        self.parent = parent
        self.condition = condition

    def _post_detach(self, parent):
        self.weight = None


# Get Input
total, workflows, parts, start_workflow = 0, {}, [], None
parts_section = False
for line in lines:
    if (line.strip() == ""):
        parts_section = True
        continue

    if (parts_section == False):
        data = {}
        wf_name, conditions = line[:-1].split("{")
        data["name"] = wf_name
        data["conditions"] = [i.split(":") for i in conditions.split(",")]
        workflows[wf_name] = data

        if (wf_name == "in"): start_workflow = data
        continue

    parts.append([i.split("=") for i in line[1:-1].split(",")])


def traverse(current_wf, previousNode):
    invert = []
    for conditions in current_wf["conditions"]:
        if (len(invert) > 0):
            previousNode = invert.pop()
        condition = conditions[0]

        # For conditions with < or >
        if (len(conditions) == 2):
            next_wf_id = conditions[1]
            if (next_wf_id == "R" or next_wf_id == "A"):
                next_wf = next_wf_id
            else:
                next_wf = workflows[next_wf_id]["name"]

            if ("<" in condition):
                symbol, cond_value = condition.split("<")[0], condition.split("<")[1]
                new_node = WNode(next_wf, parent=previousNode, condition=condition)
                if (next_wf != "R" and next_wf != "A"):
                    traverse(workflows[next_wf], new_node)

                # invert condition when the above condition is false.
                # This is the parent for next condition in the workflow
                invert.append(
                    WNode("N", parent=previousNode, condition=symbol + ">=" + cond_value)
                )
            else:
                symbol, cond_value = condition.split(">")[0], condition.split(">")[1]
                new_node = WNode(next_wf, parent=previousNode, condition=condition)
                if (next_wf != "R" and next_wf != "A"):
                    traverse(workflows[next_wf], new_node)

                # invert condition when the above condition is false.
                # This is the parent for next condition in the workflow
                invert.append(
                    WNode("N", parent=previousNode, condition=symbol + "<=" + cond_value)
                )

        else:
            next_wf_id = conditions[0]
            if (next_wf_id == "R" or next_wf_id == "A"):
                next_wf = next_wf_id
            else:
                next_wf = workflows[next_wf_id]["name"]

            new_node = WNode(next_wf, parent=previousNode, condition=condition)
            if (next_wf != "R" and next_wf != "A"):
                traverse(workflows[next_wf], new_node)


current_workflow, currentNode = start_workflow, WNode("in", parent=None, condition=None)

# Traverse through the workflow starting from current node
traverse(current_workflow, currentNode)

# Print Generated Tree
for pre, _, node in RenderTree(currentNode):
    print("%s%s (%s)" % (pre, node.foo, node.condition or 0))


# Get all paths to leafs with Accepted state
def allpaths(start):
    skip = len(start.path) - 1
    return [leaf.path[skip:] for leaf in PreOrderIter(start, filter_=lambda node: node.is_leaf and node.foo == "A")]


# Calculate the ranges for each and calculate the total combinations
def calculate(path):
    global total
    range = {"x": [1, 4000], "a": [1, 4000], "m": [1, 4000], "s": [1, 4000]}
    for workflow in path:
        condition = workflow.condition
        if (condition != None):
            if ("<=" in condition):
                symbol, condition_value = condition.split("<=")[0], int(condition.split("<=")[1])
                current_range = range[symbol]
                if (current_range[1] > condition_value): current_range[1] = condition_value

            elif (">=" in condition):
                symbol, condition_value = condition.split(">=")[0], int(condition.split(">=")[1])
                current_range = range[symbol]
                if (current_range[0] < condition_value): current_range[0] = condition_value

            elif ("<" in condition):
                symbol, condition_value = condition.split("<")[0], int(condition.split("<")[1]) - 1
                current_range = range[symbol]
                if (current_range[1] > condition_value): current_range[1] = condition_value

            elif (">" in condition):
                symbol, condition_value = condition.split(">")[0], int(condition.split(">")[1])
                current_range = range[symbol]
                if (current_range[0] < condition_value): current_range[0] = condition_value + 1

    return (range["x"][1] - range["x"][0] + 1) * (range["a"][1] - range["a"][0] + 1) * (
            range["m"][1] - range["m"][0] + 1) * (range["s"][1] - range["s"][0] + 1)


total = 0
for path in allpaths(currentNode):
    total += calculate(path)

print("Total", total)
