import aocd
import itertools
import collections
import peek

lines = """\
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............""".splitlines()

lines = aocd.get_data(year=2024, day=8).splitlines()

grid = collections.defaultdict(str, {(i, j): c for j, line in enumerate(lines) for i, c in enumerate(line)})

frequency_to_loc = collections.defaultdict(list)
for loc, frequency in grid.items():
    if frequency != ".":
        frequency_to_loc[frequency].append(loc)

for part in (1, 2):
    locps = set()
    for frequency in frequency_to_loc:
        for loc0, loc1 in itertools.permutations(frequency_to_loc[frequency], 2):
            for i in [1] if part == 1 else range(1000):
                locp = loc1[0] + i * (loc1[0] - loc0[0]), loc1[1] + i * (loc1[1] - loc0[1])
                if locp in grid:
                    locps.add(locp)
                else:
                    break
    print(f"Part {part}: {len(locps)}")

# Part 1: 269
# Part 2: 949
