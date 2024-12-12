import aocd
import peek

data = aocd.get_data(year=2024, day=12)

lines = data.splitlines()

coords = {x + 1j * y: c for y, r in enumerate(lines) for x, c in enumerate(r.strip())}
dir_corners = [0.5 + 0.5j, 0.5 - 0.5j, -0.5 + 0.5j, -0.5 - 0.5j]
visited = set()


def adjacent(coord, dirs=[1, 1j, -1, -1j]):
    return [coord + d for d in dirs]


def fill_region(c):
    visited.add(c)
    region = [c]
    for adj in adjacent(c):
        if coords.get(adj) == coords[c] and adj not in visited:
            region += fill_region(adj)
    return region


result1 = 0
result2 = 0
for c, char in coords.items():
    if c in visited:
        continue

    perimeter, corners = 0, set()

    for r in (region := fill_region(c)):
        perimeter += sum(adj not in region for adj in adjacent(r))

        for corner in adjacent(r, dir_corners):
            k = [adj for adj in adjacent(corner, dir_corners) if adj in region]
            if len(k) in [1, 3]:
                corners.add(corner)
            elif abs(k[0] - k[1]) != 1:
                corners |= {corner, corner + 0.1}

    result1 += perimeter * len(region)
    result2 += len(corners) * len(region)

peek(result1, to_clipboard=True)
peek(result2, to_clipboard=True)
