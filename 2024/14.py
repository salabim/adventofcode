import aocd
import peek
import collections
import functools

data = aocd.get_data(year=2024, day=14)
width=101
height=103
midwidth=(width-1)//2
midheight=(height-1)//2
peek(midwidth,midheight)
n=100
count=collections.defaultdict(int)
for line in data.splitlines():
    px,py,vx,vy=eval(line.replace("p=","(").replace(" v=",",")+")")
    px=(px+(n*vx))%width
    py=(py+(n*vy))%height
    if px<midwidth and py<midheight:
        count[0]+=1
    if px>midwidth and py<midheight:
        count[1]+=1
    if px<midwidth and py>midheight:
        count[2]+=1
    if px>midwidth and py>midheight:
        count[3]+=1
   
result1 = count[0]* count[1]*count[2]*count[3]

peek(result1, to_clipboard=True)

import salabim as sim

class Step(sim.Component):
    def process(self):
        n=401
        while True:
            for x in range(width):
                for y in range(height):
                    an[x,y].visible=False
            for line in data.splitlines():
                px,py,vx,vy=eval(line.replace("p=","(").replace(" v=",",")+")")
                px=(px+(n*vx))%width
                py=(py+(n*vy))%height
                an[px,py].visible=True

            an_text.text=f"n={n}"
            n+=101 # n+=1
            self.hold(1)

env=sim.Environment()
env.maximum_number_of_bitmaps(1) 
an={}
for x in range(width):
    for y in range(height):
        an[x,y]=sim.AnimateRectangle((0,0,3,3),x=x*5,y=700-y*5, fillcolor="green")
        an_text=sim.AnimateText(x=10,y=10)
Step()
env.run(0)

env.animate(True)
env.run() 


# result1=225521010