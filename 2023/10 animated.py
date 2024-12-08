from PIL import Image
import salabim as sim 

import aocd
from pprint import pprint



lines = aocd.get_data(year=2023, day=10).splitlines()

    
def neighbour(p, dir):
    if dir=='N':
        ij=(p[0],p[1]-1)
    if dir=='S':
        ij=(p[0],p[1]+1)
    if dir=='W':
        ij=(p[0]-1,p[1])         
    if dir=='E':
        ij=(p[0]+1,p[1])
    if ij in grid:
        return ij
    else:
        return None

def other(dir,kind):
    if dir == kind[0]:
        return kind[1]
    return kind[0]
          
def opposite(dir):
    if dir == 'N':
        return 'S'
    if dir == 'S':
        return 'N'
    if dir == 'W':
        return 'E'
    if dir == 'E':
        return 'W'                 
                                            
link={'|':'NS', '-':'WE', 'L':'NE', 'J':'NW', '7':'SW', 'F':'SE','S':'*'}
grid={(i,j):link[c] for j,line in enumerate(lines) for i,c in enumerate(line) if c!='.'}
spos =next( ij for ij, c in grid.items() if c=='*')
print(spos)


d=''
if neighbour(spos,'N') and 'S' in grid[neighbour(spos,'N')]:
    d+='N'
if neighbour(spos,'S') and 'N' in grid[neighbour(spos,'S')]:
    d+='S'
if neighbour(spos,'W') and 'E' in grid[neighbour(spos,'W')]:
    d+='W'                 
if neighbour(spos,'E') and 'W' in grid[neighbour(spos,'E')]:
    d+='E' 
grid[spos]=d

p = spos
dir=d[0]
next_p=neighbour(p,dir)
#pprint(f'{p=}')
#pprint(f'{next_p=}')
loop=[]
n=0
while next_p != spos:
    loop.append(next_p)
    p=next_p
    dir=other(opposite(dir),grid[p])
    next_p=neighbour(p,dir)
    n+=1 
result = (n+1)//2
print('part 1=',(n+1)//2)

pics="""\
NS
.101.
.101.
.101.
.101.
.101.
EW
.....
11111
00000
11111
.....
NE
.101.
.1011
.1000
.1111
.....
NW
.101.
1101.
0001.
1111.
.....
SW
.....
1111.
0001.
1101.
.101.
SE
.....
.1111
.1000
.1011
.101."""

images={}
for line in pics.splitlines():
    if len(line) == 2:
        spec=line
        images[spec,False] = Image.new("RGB", (5,5), (0,0,0))
        images[spec,True] = Image.new("RGB", (5,5), (0,0,0))
        j=0
    else:
        for i,c in enumerate(line):
            if c == "1":
                images[spec,False].putpixel((i,j),(255,255,255))
                images[spec,True].putpixel((i,j),(255,255,255))
            if c=="0":
                images[spec,True].putpixel((i,j),(255,0,0))
        j+=1    

env = sim.Environment()
env.animate(True)
env.background_color("white")
env.width(768+20,True)
env.show_time(False)
env.fps(10)
env.AnimateText("Advent of Code | Day 10 | animated with salabim.", angle=90,x=40,y=30,font="calibri",fontsize=30)
an_label=env.AnimateText(x=48,y=5)
env.video("10.gif")
an={}
for (i,j), c in grid.items():
    an[(i,j)]=env.AnimateImage(x=i*5+50,y=j*5+30,image=images[c,False])
n=1
for p0,p1 in zip(loop[:result+1],loop[-1:result-1:-1]):
    an[p0].image=images[grid[p0],True]
    an[p1].image=images[grid[p1],True]
    n+=1
    an_label.text=f"distance={n}"
    env.run(5/result)
#env.run(100)
env.run(2)
env.video("")

