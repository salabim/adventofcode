import aocd
import itertools

lines = aocd.get_data(year=2023, day=11).splitlines()
for part in (1, 2):
    galaxies = []
    columns = set()
    rows = set()
    extra = 1 if part == 1 else 1000000 - 1

    galaxies = [[i, j] for j, line in enumerate(lines) for i, c in enumerate(line) if c == "#"]
    columns = {galaxy[0] for galaxy in galaxies}
    rows = {galaxy[1] for galaxy in galaxies}

    for galaxy in galaxies:
        add = 0
        for column in range(len(lines[0])):
            if column not in columns:
                if galaxy[0] >= column:
                    add += extra
        galaxy[0] += add

        add = 0
        for row in range(len(lines)):
            if row not in rows:
                if galaxy[1] > row:
                    add += extra
        galaxy[1] += add

    print(f"part {part}={sum(abs(galaxy0[0] - galaxy1[0]) + abs(galaxy0[1] - galaxy1[1]) for galaxy0, galaxy1 in itertools.combinations(galaxies,2))}")
