import aocd

data = aocd.get_data(year=2022, day=14)


def solve(part):
    blocked = set()

    for line in data.splitlines():
        points = line.split(" -> ")
        for point0, point1 in zip(points, points[1:]):
            x0, y0 = list(map(int, point0.split(",")))
            x1, y1 = list(map(int, point1.split(",")))
            for x in range(min(x0, x1), max(x0, x1) + 1):
                for y in range(min(y0, y1), max(y0, y1) + 1):
                    blocked.add((x, y))

    maxy = max(y for (x, y) in blocked)

    n = 0
    while True:
        x0 = 500
        y0 = 0
        while True:
            if (part == 1 and y0 == maxy) or (500, 0) in blocked:
                return n
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
        blocked.add((x0, y0))
        n += 1

for part in (1, 2):
    print(f"Part {part} = {solve(part)}")
