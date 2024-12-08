import aocd



data = aocd.get_data(year=2022, day=12)

grid={}
for y,line in enumerate(data.splitlines()):
    for x,c in enumerate(line):
        if c == 'S':
            start=(x,y)
            grid[start] = 0
        elif c=='E':
            end=(x,y)
            grid[end] = 26
        else:
            grid[x,y] = ord(c)-ord('a')

def solve(grid, start, end, part):
    visited = set()
    path = [(0, end)]
    while path:
        n, p0 = path.pop(0)
        if grid[p0] == 0 and (part == 2 or p0 == start):
            return n
        for dx,dy in ((-1, 0), (1,0), (0,-1),(0,1)): 
            p1 = p0[0]+dx, p0[1]+dy         
            if p1 not in visited and p1 in grid and grid[p1] >= grid[p0] - 1:
                visited.add(p1)
                path.append((n+1, p1))
 
print('Part 1 =',solve(grid,start,end,1)) 
print('Part 2 =',solve(grid,start,end,2))



