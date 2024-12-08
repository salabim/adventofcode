import aocd
import collections

data = aocd.get_data(year=2022, day=23)

def move(a, b):
    return a[0] + b[0], a[1] + b[1]

def test(a, b):
    return move(a, b) in elves


elves = {(row,column) for row, line in enumerate(data.splitlines()) for column, c in enumerate(line) if c == "#"}

directions = [[(-1, -1), (-1, 0), (-1, 1)], [(1, -1), (1, 0), (1, 1)], [(-1, -1), (0, -1), (1, -1)], [(-1, 1), (0, 1), (1, 1)]]
all_directions = [(r, c) for r in (-1, 0, 1) for c in (-1, 0, 1) if r or c]

n=1
while True:
    proposals = collections.defaultdict(list)
    for elf in elves:
        if any(test(elf, direction) for direction in all_directions):
            for direction in directions:
                if not any((test(elf, d) for d in direction)):
                    proposals[move(elf, direction[1])].append(elf)
                    break

    if len(proposals) == 0:
        print("Part 2 =",n)
        break

    for proposal, l in proposals.items():
        if len(l) == 1:
            elves.remove(l[0])
            elves.add(proposal)
    if n == 10:
        min_row = min(elf[0] for elf in elves)
        max_row = max(elf[0] for elf in elves)
        min_column = min(elf[1] for elf in elves)
        max_column = max(elf[1] for elf in elves)

        print("Part 1 =",(max_row-min_row+1) * (max_column-min_column+1) - len(elves))
    directions = directions[1:] + [directions[0]]
    n+=1
    