import aocd
import salabim as sim
import math


class Crate(sim.Component):
    def setup(self, c):
        self.c = c
        self.an = sim.AnimateRectangle(
            (0, 0, 0.9, 0.9),
            text=c,
            x=lambda _, t, parent=self: sim.interpolate(t, parent.t0, parent.t1, parent.x0, parent.x1),
            y=lambda _, t, parent=self: sim.interpolate(t, parent.t0, parent.t1, parent.y0, parent.y1),
            layer=lambda _, t, parent=self: 0 if parent.t0 < t < parent.t1 else 1,
            fillcolor=lambda _, t, parent=self: "red" if parent.t0 < t < parent.t1 else "black",
            fontsize=env.pixel * 30,
        )


class Crane(sim.Component):
    def process(self):
        for line in lines:
            _, number, _, from_, _, to = line.split()
            env.move_text = line
            for i in range(int(number)):
                height_to = len(env.piles1[to])
                crate = env.piles1[from_].pop()
                env.piles1[to].append(crate)
                crate.x0, crate.x1 = crate.x1, int(to)
                crate.y0, crate.y1 = crate.y1, height_to
                distance = math.hypot(crate.x0 - crate.x1, crate.y0 - crate.y1)
                duration = distance / 5
                crate.t0 = env.now()
                crate.t1 = env.now() + duration
                yield self.hold(duration)


env = sim.Environment()
env.x0(-5)
env.x1(15)
env.y0(-1)
env.width(1024)
env.height(768)
env.pixel = (env.x1() - env.x0()) / env.width()

lines = aocd.get_data(year=2022, day=5).splitlines()
pile_names_line = next(line for line in lines if line.startswith(" 1"))
env.piles1 = {pile_name: [] for pile_name in pile_names_line.split()}
lines = iter(lines)  # iter makes that we can continue with the moves section easily

for line in lines:
    if not line:
        break
    for c, pile_name in zip(line, pile_names_line):
        if c.isalpha():
            env.piles1[pile_name].insert(0, Crate(c=c))

for pile_name, pile in env.piles1.items():
    x = int(pile_name)
    for i, crate in enumerate(pile):
        y = i
        crate.x0 = crate.x1 = x
        crate.y0 = crate.y1 = y
        crate.t0 = crate.t1 = env.now()

sim.AnimateText(
    x=4.5, y=-0.5, text="Advent of Code 2022, day 5 | simulation and animation by salabim | see www.salabim.org", fontsize=15 * env.pixel, text_anchor="c"
)
sim.AnimateText(x=4.5, y=13, text=lambda: env.move_text, fontsize=50 * env.pixel, text_anchor="c")
Crane()
env.animate(True)
do_video = False
if do_video:
    env.video_repeat(0)
    env.run(0)
    with env.video("aoc 5.mp4"):
        env.run(30)
else:
    env.run()
