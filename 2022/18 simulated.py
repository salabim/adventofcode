import aocd
import collections
import salabim as sim

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

env = sim.Environment()
env.animate(True)
env.animate3d(True)
env.position((1024,0))



cubes = []

for line in data.splitlines():
    x,y,z = map(int, line.split(','))
    cubes.append((x,y,z))

for x,y,z in cubes:
    sim.Animate3dBox(x_len=1, y_len=1, z_len=1, x=x, y=y, z=z)

env.run(sim.inf)
