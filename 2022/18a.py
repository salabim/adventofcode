import aocd
import collections


data = '''\
2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5'''

data = aocd.get_data(year=2022, day=18)


cubes = []
inside=set()
outside=set()

for line in data.splitlines():
    x,y,z = map(int, line.split(','))
    cubes.append((x,y,z))
    
print(len(cubes))
    


def reaches_outside(x, y, z, part):

    if (x, y, z) in outside:
        return True
    if (x, y, z) in inside:
        return False
    seen, qubes = set(), collections.deque([(x, y, z)])
    while qubes:
        x, y, z = qubes.popleft()
        if (x, y, z) in cubes:
            continue
        if (x, y, z) in seen:
            continue
        seen.add((x, y, z))
        if len(seen) > (5000 if part == 2 else 0):
            for p in seen:
                outside.add(p)
            return True
        for _ in [-1, 1]:
            qubes.append((x + 1, y, z))
            qubes.append((x - 1, y, z))
            qubes.append((x, y + 1, z))
            qubes.append((x, y - 1, z))
            qubes.append((x, y, z + 1))
            qubes.append((x, y, z - 1))
    for p in seen:
        inside.add(p)
    return False

def analyze_cubes(part):
    outside.clear()
    inside.clear()
    surface_area=0
    for (x, y, z) in cubes:
        if reaches_outside(x + 1, y, z, part):
            surface_area += 1
        if reaches_outside(x - 1, y, z, part):
            surface_area += 1
        if reaches_outside(x, y + 1, z, part):
            surface_area += 1
        if reaches_outside(x, y - 1, z, part):
            surface_area += 1
        if reaches_outside(x, y, z + 1, part):
            surface_area += 1
        if reaches_outside(x, y, z - 1, part):
            surface_area += 1
    return surface_area

print(analyze_cubes(1))
print(analyze_cubes(2))




