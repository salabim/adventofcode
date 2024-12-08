import aocd
import salabim as sim

env = sim.Environment()
env.animate(True)
env.background_color("black")

do_video = False
if do_video:
    env.video("14.gif")
time_step = 0.01
data = aocd.get_data(year=2022, day=14)

blocked = set()

for line in data.splitlines():
    points = line.split(" -> ")
    for point0, point1 in zip(points, points[1:]):
        x0, y0 = list(map(int, point0.split(",")))
        x1, y1 = list(map(int, point1.split(",")))
        for x in range(min(x0, x1), max(x0, x1) + 1):
            for y in range(min(y0, y1), max(y0, y1) + 1):
                blocked.add((x, y))
                sim.AnimateRectangle(spec=(0, 0, 2, 2), x=512 + (x - 500) * 4, y=700 - (y * 4), fillcolor="white")

maxy = max(y for (x, y) in blocked)
part = 1
env.n = 1


class Sand(sim.Component):
    def process(self):
        while True:
            x0 = 500
            y0 = 0
            an = sim.AnimateRectangle(spec=(0, 0, 2, 2), fillcolor="yellow")
            while True:
                yield self.hold(time_step)

                if not env.done:
                    an.x = 512 + (x0 - 500) * 4
                    an.y = 700 - (y0 * 4)

                if (part == 1 and y0 == maxy + 2) or (500, 0) in blocked:
                    env.done = True
                if part == 2 and y0 == maxy + 1:
                    break
                if (x0, y0 + 1) not in blocked:
                    y0 += 1
                elif (x0 - 1, y0 + 1) not in blocked:
                    x0 -= 1
                    y0 += 1
                elif (x0 + 1, y0 + 1) not in blocked:
                    x0 += 1
                    y0 += 1
                else:
                    break
            if (x0, y0) not in blocked:
                env.n += 1
                blocked.add((x0, y0))


env.done = False
while not env.done:
    Sand()
    env.run(time_step)
    env.run(time_step)
if do_video:
    env.run(1)
    env.video_close()
else:
    env.run(sim.inf)
