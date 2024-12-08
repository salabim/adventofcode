import aocd
import functools

data = '''\
Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3'''
data = aocd.get_data(year=2022, day=15)
print(data)

def distance(x0,y0,x1,y1):
    return abs(x0-x1) + abs(y0-y1)
    
reports = set()
for line in data.splitlines():
    t = line.split('=')
    xs = int(t[1].split(',')[0])
    ys=int(t[2].split(':')[0])
    xb=int(t[3].split(',')[0])
    yb=int(t[4])
    reports.add((xs,ys,xb,yb))

    
impossible = set()
y=2000000
#y=10
for (xs,ys,xb,yb) in reports:
    r =distance(xs,ys,xb,yb)  -abs(ys-y)
    for x in range(xs-r, xs+r+1):
        impossible.add(x)

for (xs,ys,xb,yb) in reports:
    if yb==y:
        print(xb)
        impossible.discard(xb)
for x in range(0,4000001):
    if x not in impossible:
        print('..',x)

#print(sorted(impossible))
print(len(impossible))
    
def intersect(coord_sum, coord_dif):
    x = (coord_sum + coord_dif) // 2
    y = coord_sum - x
    return x, y

def answer(x, y):
    return (
        x in range(4000000 + 1) and y in range(4000000 + 1) and
        all(distance(xs, ys, x, y) > distance(xs, ys, xb, yb) for xs, ys, xb, yb in reports)
    )

def get_answer(x, y):
    return x * 4000000 + y

def main(xs, ys, xb, yb):
    r = distance(xs, ys, xb, yb) + 1
    return (xs + ys + r, xs + ys - r)

def off(xs, ys, xb, yb):
    r = distance(xs, ys, xb, yb) + 1
    return (xs - ys + r, xs - ys - r)

for s1 in reports:
    for s2 in reports:
        for m1 in main(*s1):
            for o2 in off(*s2):
                p = intersect(m1, o2)

                if answer(*p):
                    print(m1,o2)
                    print(get_answer(*p))
        for o1 in off(*s1):
            for m2 in main(*s2):
                p = intersect(o1, m2)
                if answer(*p):
                    print(get_answer(*p))
