import aocd
import collections

lines = aocd.get_data(year=2024, day=10).splitlines()

grid = collections.defaultdict(lambda: -1, {(i, j): int(c) for j, line in enumerate(lines) for i, c in enumerate(line)})


def walk(i, j, target):
    global result2
    if grid[i, j] == target:
        if grid[i, j] == 9:
            seen.add((i, j))
            result2 += 1
        else:
            walk(i + 1, j, target + 1)
            walk(i - 1, j, target + 1)
            walk(i, j + 1, target + 1)
            walk(i, j - 1, target + 1)


result1 = 0
result2 = 0
for i, j in list(grid.keys()):
    if grid[i, j] == 0:
        seen = set()
        walk(i, j, 0)
        result1 += len(seen)

print(f"Part1: {result1}")
print(f"Part2: {result2}")
