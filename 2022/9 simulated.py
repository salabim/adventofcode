import aocd
import salabim as sim

env = sim.Environment()
env.animate(True)
env.x0(-200)
env.x1(120)
env.y0(-160)
pixel = (env.x1() - env.x0()) / env.width()


for i in range(-173, 98, 10):
    for j in range(-149, 66, 10):
        sim.AnimateCircle(radius=0.1, x=i, y=j)

sim.AnimateText(
    x=-70, y=-150, text="Advent of Code 2022, day 9 | simulation and animation by salabim | see www.salabim.org", fontsize=15 * pixel, text_anchor="c"
)


class AoC(sim.Component):
    def process(self):
        sim.AnimateCircle(radius=1, x=lambda: x[9], y=lambda: y[9])

        data = aocd.get_data(year=2022, day=9)

        fields1 = {(0, 0)}
        fields9 = {(0, 0)}
        x = [0 for _ in range(10)]
        y = [0 for _ in range(10)]

        for line in data.splitlines():
            direction, n = line.split()

            for _ in range(int(n)):
                for i in range(10):
                    if i == 0:
                        x[0] += -(direction == "L") + (direction == "R")
                        y[0] += -(direction == "D") + (direction == "U")
                    else:
                        diff_x = x[i - 1] - x[i]
                        diff_y = y[i - 1] - y[i]
                        if abs(diff_x) >= 2 or abs(diff_y) >= 2:
                            x[i] += -1 if diff_x < 0 else 1 if diff_x > 0 else 0
                            y[i] += -1 if diff_y < 0 else 1 if diff_y > 0 else 0

                if (x[9], y[9]) not in fields9:
                    sim.AnimateCircle(radius=1, x=x[9], y=y[9], fillcolor="red", linecolor="", layer=1)

                fields1.add((x[1], y[1]))
                fields9.add((x[9], y[9]))
                yield self.hold(0.001)
        env.main().activate()


AoC()
do_video = False
if do_video:
    env.video("9.gif")
    env.run(sim.inf)
    env.run(3)
    env.video_close()
    env
else:
    env.run(sim.inf)
    env.run(5)
    print(env.now())
print("Done")