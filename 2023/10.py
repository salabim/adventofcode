import aocd
from pprint import pprint


lines = aocd.get_data(year=2023, day=10).splitlines()
    
def neighbour(p, dir):
    dis = dict(N=(0,-1), S=(0,1), W=(-1,0), E=(1,0))
    return  (p[0]+dis[dir][0],p[1]+dis[dir][1])

def other(dir,kind):
    return kind.replace(dir,'')

opposite=dict(N='S', S='N', W='E', E='W')
                                            
link={'|':'NS', '-':'WE', 'L':'NE', 'J':'NW', '7':'SW', 'F':'SE','S':''}
grid={(i,j):link[c] for j,line in enumerate(lines) for i,c in enumerate(line) if c!='.'}
spos =next( ij for ij, c in grid.items() if c=='')

grid[spos]=''.join(dir for dir in list('NSWE') if neighbour(spos,dir) and opposite[dir] in grid[neighbour(spos,dir)])
     
dir=grid[spos][0]
pos=neighbour(spos,dir)
n=0
while pos != spos:
    dir=other(opposite[dir],grid[pos])
    pos=neighbour(pos,dir) 
    n+=1 
print('part 1=',(n+1)//2)

            

    

