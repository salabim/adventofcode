import aocd
import collections
import itertools

Report = collections.namedtuple("Report", "sensor beacon")
Point = collections.namedtuple("Point", "x y")


data = aocd.get_data(year=2022, day=15)


def distance(point0, point1):
    return abs(point0.x - point1.x) + abs(point0.y - point1.y)


reports = set()
for line in data.splitlines():
    xs, ys, xb, yb = tuple(map(int, ("".join(c if c in "0123456789-" else " " for c in line)).split()))
    reports.add(Report(Point(xs, ys), Point(xb, yb)))


def part1(reports):
    impossible = set()
    y = 2000000
    for report in reports:
        r = distance(report.sensor, report.beacon) - abs(report.sensor.y - y)
        for x in range(report.sensor.x - r, report.sensor.x + r + 1):
            impossible.add(x)

    for report in reports:
        if report.beacon.y == y:
            impossible.discard(report.beacon.x)
    return len(impossible)


def part2(reports):
    def dir0(report):
        r = distance(report.sensor, report.beacon) + 1
        return (report.sensor.x + report.sensor.y + r, report.sensor.x + report.sensor.y - r)

    def dir1(report):
        r = distance(report.sensor, report.beacon) + 1
        return (report.sensor.x - report.sensor.y + r, report.sensor.x - report.sensor.y - r)

    for report0, report1 in itertools.product(reports, reports):
        for m0, m1 in itertools.chain(itertools.product(dir0(report0), dir1(report1)), itertools.product(dir0(report1), dir1(report0))):
            point = Point((m0 + m1) // 2, m0 - (m0 + m1) // 2)
            if (
                0 <= point.x <= 4000000
                and 0 <= point.y <= 4000000
                and all(distance(report.sensor, point) > distance(report.sensor, report.beacon) for report in reports)
            ):
                return point.x * 4000000 + point.y


print("Part 1 =", part1(reports))
print("Part 2 =", part2(reports))
