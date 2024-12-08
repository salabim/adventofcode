import aocd
import itertools

lines = aocd.get_data(year=2023, day=14).splitlines()

rocks = set()
cubes = set()

for i, line in enumerate(lines):
    for j, char in enumerate(line.strip()):
        if char == '#':
            cubes.add((i, j))
        elif char == 'O':
            rocks.add((i, j))
    m = j+1
n = i+1
print(n, m)

def tilt(direction):
    def ordering(i, j):
        if direction == 'N':
            return i
        elif direction == 'S':
            return -i
        elif direction == 'W':
            return j
        elif direction == 'E':
            return -j
    compass = {'N': (-1, 0), 'S': (1, 0), 'W': (0, -1), 'E': (0, 1)}
    for rock in sorted(list(rocks), key=lambda pos: ordering(pos[0], pos[1])):
        pos = rock
        while True:
            next_space = (compass[direction][0] + pos[0], compass[direction][1] + pos[1])
            if not (0 <= next_space[0] < n and 0 <= next_space[1] < m):
                break
            if next_space not in rocks and next_space not in cubes:
                pos = next_space
            else:
                break
        if pos != rock:
            rocks.remove(rock)
            rocks.add(pos)

def get_load(rocks):
    return sum(n-i for i, j in rocks)

def print_grid():
    grid=[['.' for _ in range(m)] for _ in range(n)]
    for i, j in rocks:
        grid[i][j] = 'O'
    for i, j in cubes:
        grid[i][j] = '#'
    for row in grid:
        print(''.join(row))

def get_sig(rocks):
    # unique hashable representation of the rock locations
    return tuple(sorted(rocks))

boards = {}
cache_hit_count = 0
for k in range(1000000000):
    if get_sig(rocks) in boards:
        cache_hit_count += 1
        if cache_hit_count == 2:
            break
        boards = {}  # clear out the non-repeating data
    boards[get_sig(rocks)] = k
    tilt('N')
    if k == 0:
        # part 1
        print("Part 1:", get_load(rocks))
    tilt('W')
    tilt('S')
    tilt('E')

# part 2
period = len(boards.values())
start = min(boards.values())
term = ((1000000000 - start) % period)+start

for b in boards.keys():
    if boards[b] == term:
        print("Part 2:", get_load(b))
        break
