with open("input.txt") as file:
    lines = file.read().splitlines()


# Holds module information
class Module():
    def __init__(self, type, name, children=[]):
        super(Module, self).__init__()
        self.type = type
        self.name = name
        self.children = children
        self.state = 0  # 0 for off 1 for on
        self.inputs_from_modules = {}

    def get_output(self, pulse, previous_module):
        # Flip Flop
        if (self.type == "%"):
            # Switch states and return H or L
            if (pulse == "L"):
                if (self.state == 0):
                    self.state = 1
                    return "H"
                else:
                    self.state = 0
                    return "L"
        # Conjunction
        elif (self.type == "&"):
            self.inputs_from_modules[previous_module.name] = pulse
            # Check all values of the input modules are H
            if (len(set(self.inputs_from_modules.values())) == 1
                    and list(self.inputs_from_modules.values())[0] == "H"):
                return "L"
            else:
                return "H"
        elif (self.type == "broadcaster"):
            return pulse
        elif (self.type == "output"):
            self.inputs_from_modules[previous_module.name] = pulse
            return pulse


# Get input
data, module_map = [], {}
for line in lines:
    module_name, children = line.split("->")
    if (module_name.strip() == "broadcaster"):
        type, name = "broadcaster", "broadcaster"
    else:
        type, name = module_name[0], module_name[1:]

    children = children.strip().split(",")
    children = [x.strip() for x in children]
    module = Module(type, name.strip(), children)
    module_map[name.strip()] = module
    data.append(module)

# Update input modules per each module and set their state default pulse as L
for module in data:
    for child in module.children:
        if (child not in module_map):
            module_map[child] = Module(child, child, [])
        module_map[child].inputs_from_modules[module.name] = "L"


# Process the module
def process(queue, module_name, pulse, previous):
    current_module = module_map[module_name]
    pulse = current_module.get_output(pulse, previous)
    if (pulse is None):
        return

    for name in current_module.children:
        queue.append((module_map[name], pulse, current_module))


# Since events needs to be processed in order, queue is needed to have FIFO behavior
def press_button(pulse):
    queue = [(module_map["broadcaster"], pulse, None)]
    while (len(queue) > 0):
        (module, pulse, current_module) = queue.pop(0)
        counts[pulse] += 1
        process(queue, module.name, pulse, current_module)


counts = {"H": 0, "L": 0, "K": 0}
count, button_count = 0, 1000
for x in range(button_count):
    press_button("L")

print("Pulse Count", counts["H"] * counts["L"])
