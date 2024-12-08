import aocd

import itertools
import math
from collections import defaultdict
from ycecream import yc
import salabim as sim

lines = aocd.get_data(year=2023, day=8).splitlines()

instructions = itertools.cycle(lines[0])

network = {}
for line in lines[2:]:
    network[(line[0:3], "L")] = line[7:10]
    network[(line[0:3], "R")] = line[12:15]

env = sim.Environment()
env.animate(True)
env.width(600)
env.x1(600)
env.height(720)
env.show_time(False)
if True:
    env.video("8n.gif")
for part in (2,):
    if part == 1:
        nodes = ["AAA"]
    else:
        nodes = [node_dir[0] for node_dir in network.keys() if node_dir[0][2] == "A" and node_dir[1] == "L"]

    nodes_only=[node_dir[0] for node_dir in network.keys() if node_dir[1]=="L"]
    sorted_nodes_only=sorted(nodes_only, key=lambda name: name[2]+name[:1])
    nodes_per_end_letter=defaultdict(list)
    for node in sorted_nodes_only:
        nodes_per_end_letter[node[2]].append(node)

    nodes_copy=nodes[:]
    print(nodes)
    an={}
    node_text={}
    for i, v in enumerate(nodes_per_end_letter.values()):
        for j,name in enumerate(v):
            node_text[name]=f" {name} "
            an[name]=env.AnimateRectangle(spec=(0,0,28,9),text=node_text[name], textcolor="black",x=i*30+5, y=j*10+20, font="narrow", fontsize=10,fillcolor="", linecolor="")
    an_legend=env.AnimateText("Advent of Code, day 8, part 2.  Animated with salabim.", x=10,y=700,font="calibri",fontsize=20)
    an_legend=env.AnimateText(x=10,y=0,font="narrow")
    for n,instruction in enumerate(instructions, 1):
        an_legend.text=f"instruction={instruction} | n={n}"
        for i,color in enumerate (("red", "blue", "green", "orange","purple","yellow")):
            node=nodes[i]
            if instruction=="L":
                node_text[node]=f"<{node_text[node][1:]}"
            if instruction=="R":
                node_text[node]=f"{node_text[node][:-1]}>"
            an[node].text=node_text[node]
            an[node].fillcolor=color            
            nodes[i] = network[(nodes[i], instruction)]

        env.run(0.2)
        if n>=40:
            break
    
    an_ff=env.AnimateText("FAST FORWARD",x=env.x1()/2, y=env.y1()/2, text_anchor="c", fontsize=100,angle=45)
    env.run(2)
    an_ff.remove()

    nodes=nodes_copy
    print(nodes)

    instructions = itertools.cycle(lines[0])

    for i,color in enumerate (("red", "blue", "green", "orange","purple","yellow")):
        node=nodes[i]
#        an[node].fillcolor=color
        for n,instruction in enumerate(instructions, 1):
            if instruction=="L":
                node_text[node]=f"<{node_text[node][1:]}"
            if instruction=="R":
                node_text[node]=f"{node_text[node][:-1]}>"
            an[node].text=node_text[node]
            an[node].fillcolor=color
            node = network[(node, instruction)]

            if node[2] == "Z":
                an[node].fillcolor=color

                break
an_legend.text=f"instruction={instruction} | n={13524038372771}"

env.run(10)
env.video("")

