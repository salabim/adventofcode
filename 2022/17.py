import aocd
import itertools


def move(rock,xdir,ydir):
    return { (x+xdir,y+ydir) for x,y in rock}

        
def drop(rock):
    for part in rock:
        chamber.add(tuple(part))
  
def can_move(rock,xdir,ydir):
    for x,y in rock:
        if (x+xdir, y+ydir) in chamber or not (0 <= x+xdir <= 6):
            return False
    return True
    
    
def dump(rock):
    for y0 in range(highest()+7,-1,-1):
        print('|' + ''.join(('@' if [x,y0] in rock else '#' if (x,y0) in chamber else '.') for x in range(7))+ '|')    
    print('+-------+')
data = '>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'
data = aocd.get_data(year=2022, day=17)
#print(data)
print(len(data))

def highest():
    return max(y for x,y in chamber)
    
chamber = set((x,0) for x in range(7))
print(highest())
shape0=((0,0),(1,0),(2,0),(3,0))
shape1=((1,0),(0,1),(1,1),(2,1),(1,2))
shape2=((0,0),(1,0),(2,0),(2,1),(2,2))
shape3=((0,0),(0,1),(0,2),(0,3))
shape4=((0,0),(1,0),(0,1),(1,1))
shapes=itertools.cycle((shape0,shape1,shape2,shape3,shape4))
shapenumbers=itertools.cycle(range(6))
jetstream=map(lambda c: -1 if c=='<' else +1, itertools.cycle(data))
jetstreamnumbers=itertools.cycle(range(len(data)))


    
store = set()
for _, shape, shapenumber, jetstreamnumber  in zip(range(2022), shapes,shapenumbers,jetstreamnumbers):
    yrock = highest() + 4
    xrock=2 
    rock = [[x+xrock,y+yrock] for x,y in shape]
#    dump(rock)
    while True:
        dirx=next(jetstream)
        if can_move(rock,dirx,0):
            rock=move(rock,dirx,0)
        if can_move(rock,0,-1):
            rock=move(rock,0,-1)
        else:
            drop(rock)
            break
    
    maxY = max([y for (x,y) in chamber])
    pattern = frozenset([(x,maxY-y) for (x,y) in chamber if maxY-y<=30])
    print(jetstreamnumber)
    
    if (pattern,shapenumber,jetstreamnumber) in store:
        print('bingo')
    else:
        store.add((pattern,shapenumber,jetstreamnumber))
#        print(shapenumber,jetstreamnumber)
        
print(highest())
            

            
            
