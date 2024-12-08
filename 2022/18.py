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

for line in data.splitlines():
    x,y,z = map(int, line.split(','))
    cubes.append((x,y,z))
    
    
minx = min(x for x,y,z in cubes)
miny = min(y for x,y,z in cubes)
minz = min(z for x,y,z in cubes)
maxx = max(x for x,y,z in cubes)
maxy = max(y for x,y,z in cubes)
maxz = max(z for x,y,z in cubes)

d =((-1,0,0),(+1,0,0), (0,-1,0),(0,+1,0),(0,0,1),(0,0,-1))
sides=collections.defaultdict(int)
for x,y,z in cubes:
    
    for dx,dy,dz in d:
        ax,ay,az = 2*x+dx, 2*y+dy, 2*z+dz
        
        sides[(ax,ay,az)]+=1
        
        
print(sum(v for v in sides.values() if v==1))

allcubes = [(x,y,z) for x in range(minx,maxx+1) for y in range(miny,maxy+1) for z in range(minz,maxz+1)]

sides=collections.defaultdict(int)
for x,y,z in allcubes:
    
    for dx,dy,dz in d:
        ax,ay,az = 2*x+dx, 2*y+dy, 2*z+dz
        
        sides[(ax,ay,az)]+=1
        
        
print(sum(v for v in sides.values() if v==1))
