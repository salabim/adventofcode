import aocd
import collections

lines = aocd.get_data(year=2024, day=10).splitlines()

grid = collections.defaultdict(lambda: -1, {complex(a, b): int(c) for b, line in enumerate(lines) for a, c in enumerate(line)})


def walk(a, target):
    global result2
    if grid[a] == target:
        if grid[a] == 9:
            seen.add((a))
            result2 += 1
        else:
            for d in (-1, 1, -1j, 1j):
                walk(a + d, target + 1)


result1 = 0
result2 = 0
for a in list(grid.keys()):
    if grid[a] == 0:
        seen = set()
        walk(a, 0)
        result1 += len(seen)

print(f"Part1: {result1}")
print(f"Part2: {result2}")

