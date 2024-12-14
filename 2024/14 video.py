import aocd
import peek
import salabim as sim

data = aocd.get_data(year=2024, day=14)
width=101
height=103

class Step(sim.Component):
    def process(self):
        n=7769
        while True:
            for x,y in an:
                an[x,y].visible=False
            for line in data.splitlines():
                px,py,vx,vy=eval(line.replace("p=","(").replace(" v=",",")+")")
                px=(px+(n*vx))%width
                py=(py+(n*vy))%height
                an[px,py].visible=True

            an_text.text=f"{n} seconds"
            if n==7774:
                an_text.text=f"{n} seconds !!!!"

                self.hold(4)
            n+=1 # n+=101
            self.hold(1)

env=sim.Environment(animate=True)
env.show_time(False)
env.width(700)
env.height(700)
env.x1(700)
an={(x,y): sim.AnimateRectangle((0,0,5,5),x=x*6+50,y=(height-y)*6+50, fillcolor="green",visible=False) for x in range(width)  for y in range(height)}
an_text=sim.AnimateText(x=10,y=30)
sim.AnimateText(x=10,y=10,text="AoC 2024 day 14 | Animated with salabim | See www.salabim.org for details.")
Step()

env.fps(1)
with env.video("14.gif"):
    env.run(15) 


# result1=225521010