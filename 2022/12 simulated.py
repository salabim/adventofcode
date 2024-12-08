import aocd
import salabim as sim


data = aocd.get_data(year=2022, day=12)

env = sim.Environment()
env.background_color("black")


def onpath(p):
    if done:
        return p in queue[0]
    else:
        return any(p in path for path in queue)


grid = {}
for y, line in enumerate(data.splitlines()):
    for x, c in enumerate(line):
        if c == "S":
            start = (x, y)
            grid[start] = 0
        elif c == "E":
            end = (x, y)
            grid[end] = 26
        else:
            grid[x, y] = ord(c) - ord("a")
            sim.AnimateRectangle(
                spec=(0, 0, 12, 12),
                x=23 + 14 * x,
                y=50 + 14 * y,
                fillcolor=lambda arg, t, x=x, y=y: "green"
                if onpath((x, y))
                else "lightgreen"
                if (x, y) in visited
                else env.colorinterpolate(grid[x, y], 0, 26, "white", "red"),
            )


env.run(0)
env.animate(True)
sim.AnimateText(
    x=512, y=20, text="Advent of Code 2022, day 12 | simulation and animation by salabim | see www.salabim.org", fontsize=15, text_anchor="c", textcolor="white"
)
done = False
do_video = True

visited = set()
queue = [[end]]
if do_video:
    env.video("12.mp4")
env.run(1)

while queue:
    path = queue.pop(0)
    p0 = path[-1]
    if grid[p0] == 0 and p0 == start:
        break
    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        p1 = p0[0] + dx, p0[1] + dy
        if p1 not in visited and p1 in grid and grid[p1] >= grid[p0] - 1:
            visited.add(p1)
            new_path = list(path)
            new_path.append(p1)
            queue.append(new_path)
            env.run(0.005)
done = False
if do_video:
    env.run(2)
    env.video_close()
else:
    env.run(sim.inf)

print(path)
