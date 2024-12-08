import aocd
import collections


lines = aocd.get_data(year=2024, day=4).splitlines()

grid = collections.defaultdict(str, {(i, j): c for j, line in enumerate(lines) for i, c in enumerate(line)})

print("Part 1:",sum(
    "".join(grid[i + k * di, j + k * dj] for k in range(4)) == "XMAS"
    for i in range(len(lines))
    for j in range(len(lines[0]))
    for di in (-1, 0, 1)
    for dj in (-1, 0, 1)
))


print("Part 2:", sum(
    grid[i, j] == "A" and {grid[i + 1, j + 1], grid[i - 1, j - 1]} == {grid[i + 1, j - 1], grid[i - 1, j + 1]} == set("MS")
    for i in range(len(lines))
    for j in range(len(lines[0]))
))
