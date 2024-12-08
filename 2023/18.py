import aocd
import itertools


lines = aocd.get_data(year=2023, day=18).splitlines()

from itertools import starmap
from operator import mul

def shoelace_area(corners):
    x, y = [x for [x, _] in corners], [y for [_, y] in corners]
    x2 = x[1:] + [x[0]]
    y2 = y[1:] + [y[0]]
    area = abs(sum(starmap(mul, zip(x, y2))) - sum(starmap(mul, zip(x2, y)))) / 2
    return int(area)

def find_corners(directions):
    corners = [[0,0]]
    perimeter = 0
    for d, l in directions:
        past_corner = corners[-1]
        perimeter += l
        match d:
            case 'R':
                corners.append([past_corner[0] + l, past_corner[1]])
            case 'L':
                corners.append([past_corner[0] - l, past_corner[1]])
            case 'D':
                corners.append([past_corner[0], past_corner[1] + l])
            case 'U':
                corners.append([past_corner[0], past_corner[1] - l])
    return corners,perimeter

directions = lines
directions = [line.split() for line in directions]
init_directions = list(map(lambda d: [d[0], int(d[1])], directions))
corners, perimeter = find_corners(init_directions)
print(shoelace_area(corners) + perimeter // 2 + 1)
dir_map = {
    0: 'R',
    1: 'D',
    2: 'L',
    3: 'U'
}
fixed_directions = list(map(lambda d: [dir_map[int(d[2][-2])], int(d[2][2:-2], 16)], directions))

corners, perimeter = find_corners(fixed_directions)
print(shoelace_area(corners) + perimeter // 2 + 1)
        
