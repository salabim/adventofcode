import aocd

lines = aocd.get_data(year=2024, day=2).splitlines()


def is_safe(report):
    return (sorted(report) == report or sorted(report, reverse=True) == report) and all(abs(i0 - i1) in (1, 2, 3) for i0, i1 in zip(report, report[1:]))


reports = [[*map(int, line.split())] for line in aocd.get_data(year=2024, day=2).splitlines()]
print("Part1: ", sum(is_safe(report) for report in reports))
print("Part2: ", sum(any(is_safe(report[:i] + report[i + 1 :]) for i in range(len(report))) for report in reports))
