import aocd
import salabim as sim

env = sim.Environment()
env.animate(True)
env.animate3d(True)


data = aocd.get_data(year=2022, day=8)

lines = data.splitlines()
sim.Animate3dGrid(x_range=range(0, 101, 10), y_range=range(0, 101, 10))

for j in range(len(lines)):
    for i in range(len(lines[j])):
        h = int(lines[i][j])
        sim.Animate3dBox(x=i, y=j, z=0, x_len=0.5,y_len=0.5, z_len=h,z_ref=1,edge_color="red")

env.view(x_eye=212.9439,y_eye=133.0621,z_eye=177.5537,x_center=10.0000,y_center=20.0000,z_center=0.0000,field_of_view_y=45.0000)  # t=129.3706
env.width3d(950)
env.height3d(768)
env.position3d((0, 100))
env.background_color("black")
env.width(950)
env.height(768)
env.position((960, 100))

env.run(sim.inf)