import aocd
import collections
import salabim as sim

env=sim.Environment()
env.animate(True)
env.background_color("black")


data = aocd.get_data(year=2022, day=23)

def move(a, b):
    return a[0] + b[0], a[1] + b[1]

def test(a, b):
    return move(a, b) in elves


elves = {(row,column) for row, line in enumerate(data.splitlines()) for column, c in enumerate(line) if c == "#"}

an = {}
an_n = sim.AnimateText(x=100,y=720)
for elf in elves:
    an[elf] =sim.AnimateRectangle(spec=(0,0,3,3), x=200+elf[1]*5, y=80+elf[0]*5, fillcolor="yellow")


class Show(sim.Component):
    def process(self):
        directions = [[(-1, -1), (-1, 0), (-1, 1)], [(1, -1), (1, 0), (1, 1)], [(-1, -1), (0, -1), (1, -1)], [(-1, 1), (0, 1), (1, 1)]]
        all_directions = [(r, c) for r in (-1, 0, 1) for c in (-1, 0, 1) if r or c]

        n=1
        while True:
            proposals = collections.defaultdict(list)
            for elf in elves:
                if any(test(elf, direction) for direction in all_directions):
                    for direction in directions:
                        if not any((test(elf, d) for d in direction)):
                            proposals[move(elf, direction[1])].append(elf)
                            break

            if len(proposals) == 0:
                break

            for proposal, l in proposals.items():
                if len(l) == 1:
                    from_ = l[0]
                    to_ = proposal
                    elves.remove(from_)
                    elves.add(to_)
                    an[to_]=an[from_]
                    an[to_].x = 200+to_[1]*5
                    an[to_].y = y=80+to_[0]*5
                    del an[from_]
            

            yield self.hold(0.01)
            an_n.text="Advent of Code Year: 2022 Day:23 - Animation with salabim. www.salabim.org  - round "+ str(n)        
            directions = directions[1:] + [directions[0]]
            n+=1
Show()
do_video=True
if do_video:
    env.show_time(False)
    env.video("23.mp4")
    env.run(till=11)
    env.video_close()
else:
    env.run(sim.inf)