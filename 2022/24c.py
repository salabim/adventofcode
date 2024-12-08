from aocd.models import Puzzle
from collections import deque
import numpy as np

puzzle = Puzzle(year=2022, day=24)

data = puzzle.input_data
# with open("2022/test2.txt") as file:
#     data = file.read()

data = [list(line[1:-1]) for line in data.splitlines()[1:-1]]

H = len(data)
W = len(data[0])

# arrays of deques for each type of bliz, True = occupied
u = []
d = []
l = []
r = []

data = np.array(data, dtype=str) # convert to np array to allow convenient column extraction

for y in range(H):
    r.append(deque([c == '>' for c in list(data[y])]))
    l.append(deque([c == '<' for c in list(data[y])]))

for x in range(W):
    u.append(deque([c == '^' for c in list(data[:,x])]))
    d.append(deque([c == 'v' for c in list(data[:,x])]))
    
def occupied(step, x, y):
    row = l[y].copy()
    row.rotate(-step)
    if row[x]:
        return True
    row = r[y].copy()
    row.rotate(step)
    if row[x]:
        return True
    col = u[x].copy()
    col.rotate(-step)
    if col[y]:
        return True
    col = d[x].copy()
    col.rotate(step)
    if col[y]:
        return True
    return False

directions = [(0, -1), (0, 1), (-1, 0), (1, 0), (0, 0)]

def in_bounds(x, y):
    if (x < 0 or
        x >= W or
        y < 0 or
        y >= H):
        return False
    return True

# BFS
def shortest(step0, start, end):
    next_queue = set()
    next_queue.add(start)
    step = step0

    done = False
    while not done and next_queue:
        queue = next_queue
        next_queue = set()
        for pos in queue:
            if pos == start or not occupied(step, pos[0], pos[1]):
                if pos == end:
                    done = True
                    break
                for direction in directions:
                    adj = (pos[0] + direction[0], pos[1] + direction[1]) # (xa + xb, ya + yb)
                    if adj == start or in_bounds(adj[0], adj[1]):
                        next_queue.add(adj)
            if done:
                break
        step += 1
    print(next_queue)
    return step

part1 = shortest(0, (0,-1), (W-1,H-1))
print('Part 1:', part1)
# puzzle.answer_a = part1

back = shortest(part1+1, (W-1,H), (0,0))
part2 = shortest(back, (0,-1), (W-1,H-1))
print('Part 2:', part2)
# puzzle.answer_b = part2