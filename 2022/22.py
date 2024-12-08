import aocd

data = '''\
        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5'''
data = aocd.get_data(year=2022, day=22)
grid = {}
max_column=0
max_row=0
for row, line in enumerate(data.splitlines()[:-2],1):
    for column,  c in enumerate(line,1):
        if c in '.#':
            grid[row, column]=c
            max_row=max(max_row,row)
            max_column =max(max_column,column)
print(max_column, max_row,len(grid))

def move(row,column, direction):
    row0= row
    column0=column
    while True:
        row,column = row+direction[0], column+direction[1]
        if row<1:
            row=max_row
        elif row>max_row:
            row=1
        if column<1:
            column=max_column
        elif column>max_column:
            column=1
        if (row,column) in grid:
            if grid[row,column] == '#':
                return row0, column0
            else:
                return row,column



seq = (0,1),(1,0),(0,-1),(-1,0)

right = {seq[i]:seq[(i+1)%4] for i in range(4)}
left = {seq[i]:seq[(i-1)%4] for i in range(4)}

instructions = data.splitlines()[-1].replace('R', ' R ').replace('L',' L ').split()

topleft = (1,min(c for r,c in grid if r == 1))

row,column = topleft
direction=(0,1)
for instruction in instructions:

    if instruction  =='R':
        direction = right[direction] 
    elif instruction ==  'L':
        direction=left[direction] 
    else:
        n = int(instruction)
        for _ in range(n):
            row,column = move(row,column,direction)


facing = seq.index(direction)
print(row*1000+column*4+facing)
        
        
        
