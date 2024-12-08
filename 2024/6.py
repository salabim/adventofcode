import aocd
import collections
import peek

lines="""\
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...""".splitlines()

lines = aocd.get_data(year=2024, day=6).splitlines()

peek(len(lines),len(lines[0]))
def cycle(obs_pos):
    visited=set()
    pos = next((i,j) for (i,j) in grid if grid[(i,j)]=="^")
    if grid[obs_pos]!=".":
        return False
    dir=(0,-1)
    while grid[pos]:
        if (pos,dir) in visited:
            return True
        visited.add((pos,dir))
        while grid[pos[0]+dir[0],pos[1]+dir[1]]=="#" or (pos[0]+dir[0],pos[1]+dir[1])==obs_pos:
            dir=next_dir[dir]
        pos=(pos[0]+dir[0],pos[1]+dir[1]) 
    return False


grid = collections.defaultdict(str, {(i, j): c for j, line in enumerate(lines) for i, c in enumerate(line)})
pos = next((i,j) for (i,j) in grid if grid[(i,j)]=="^")

next_dir={(-1,0):(0,-1), (0,-1):(1,0), (1,0):(0,1), (0,1):(-1,0)}

visited=set()
dir=(0,-1)
while grid[pos]:

    visited.add(pos)
    if grid[pos[0]+dir[0],pos[1]+dir[1]]=="#":
        dir=next_dir[dir]
    pos=(pos[0]+dir[0],pos[1]+dir[1]) 

peek(len(visited))
visited1=list(visited)


result2=0
for obs_pos in visited1:
    result2+=cycle(obs_pos)

peek(result2)
