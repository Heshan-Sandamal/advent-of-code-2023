with open("input.txt") as file:
    lines = file.read().splitlines()

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


# Traverse through the workflow
def traverse(part, current_wf):
    for conditions in current_wf["conditions"]:
        for category in part:
            symbol, category_value = category[0], int(category[1])

            if (len(conditions) == 2):
                condition, next_workflow = conditions[0], conditions[1]
                if (symbol in condition):
                    # condition exits for the symbol
                    if ("<" in condition):
                        cond_value = int(condition.split("<")[1])
                        if (category_value < cond_value):
                            if (next_workflow == "A"): return "A"
                            return next_workflow
                    else:
                        cond_value = int(condition.split(">")[1])
                        if (category_value > cond_value):
                            if (category_value > cond_value):
                                if (next_workflow == "A"): return "A"
                                return next_workflow

            else:
                return conditions[0]


# Calculate Total
def get_total(part):
    total = 0
    for x in part:
        total += int(x[1])
    return total


total = 0
for part in parts:
    current_wf = start_workflow
    while (True):
        next_wf = traverse(part, current_wf)
        if ("A" == next_wf):
            total += get_total(part)
            break
        elif ("R" == next_wf):
            break
        else:
            current_wf = workflows[next_wf]

print("Total", total)
