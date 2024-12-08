import aocd

import itertools
import math


lines = aocd.get_data(year=2023, day=8).splitlines()

instructions = itertools.cycle(lines[0])

network = {}
for line in lines[2:]:
    network[(line[0:3], "L")] = line[7:10]
    network[(line[0:3], "R")] = line[12:15]

for part in (1, 2):
    if part == 1:
        nodes = ["AAA"]
    else:
        nodes = [node_dir[0] for node_dir in network.keys() if node_dir[0][2] == "A" and node_dir[1] == "L"]

    cycle_lengths = []
    visiteds=[]
    for node in nodes:
        visiteds.append({node})
        for cycle_length, instruction in enumerate(instructions, 1):
            node = network[(node, instruction)]
            visiteds[-1].add(node)
            if node[2] == "Z":
                break
        cycle_lengths.append(cycle_length)
    print(f"Part {part} =", math.lcm(*cycle_lengths))
    for visited0, cycle_length0 in zip(visiteds,cycle_lengths):
        print(len(visited0),cycle_length0,cycle_length0/len(visited0))
