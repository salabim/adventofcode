import aocd
import itertools
from functools import cache

lines = aocd.get_data(year=2023, day=12).splitlines()


@cache
def solve(line, counts, pos, current_count, countpos):
    if pos == len(line):
        return len(counts) == countpos
    if line[pos] == "#":
        return solve(line, counts, pos + 1, current_count + 1, countpos)
    if line[pos] == "." or countpos == len(counts):
        if countpos < len(counts) and current_count == counts[countpos]:
            return solve(line, counts, pos + 1, 0, countpos + 1)
        if current_count == 0:
            return solve(line, counts, pos + 1, 0, countpos)
        return 0
    hash = solve(line, counts, pos + 1, current_count + 1, countpos)
    dot_count = 0
    if current_count == counts[countpos]:
        dot_count = solve(line, counts, pos + 1, 0, countpos + 1)
    elif current_count == 0:
        dot_count = solve(line, counts, pos + 1, 0, countpos)
    return hash + dot_count


for part in (1, 2):
    result = 0
    n = 1 if part == 1 else 5
    for line in lines:
        result += solve(line="?".join([line.split()[0]] * n) + ".", counts=tuple(map(int, line.split()[1].split(","))) * n, pos=0, current_count=0, countpos=0)
    print(f"Part {part}={result}")

