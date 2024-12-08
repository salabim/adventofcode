import aocd
import collections

data = '''\
....#..
..###.#
#...#.#
.#...##
#.###..
##.#.##
.#..#..'''
data='''\
.....
..##.
..#..
.....
..##.
.....'''
#data = aocd.get_data(year=2022, day=23)
def dump(n):
    print(n)
    for row in range(-2,10):
        for column in range(-3,11):
            print('#' if ((row,column) in elves) else '.',end='')
        print()
    print()

def move(a,b):
    return a[0]+b[0],a[1]+b[1]
def test(a,b):
    return move(a,b) in elves
    
elves = set()
for row,line in enumerate(data.splitlines()):
    for column,c in enumerate(line):
        if c=='#' :
            elves.add((row, column))

dump(0)
directions = [ [(-1,-1),(-1,0),(-1,1)], [(1,-1), (1,0),(1,1)], [(-1,1),(0,1),(1,1)], [(-1,-1),(0,-1),(1,-1)]]
all_directions = [(r,c) for r in (-1,0,1) for c in (-1,0,1) if r or c]

for n in range(1,11):
    proposals=collections.defaultdict(list)
    for elf in elves:
        if any(test(elf,direction) for direction in all_directions):
            for direction in directions:
                if not any((test(elf,d) for d in direction)):
                    proposals[move(elf,direction[1])].append(elf)
                    break

    for proposal, l in proposals.items():
        if len(l) == 1:
            elves.remove(l[0])
            elves.add(proposal)
    dump(n)

    directions = directions[1:] + [directions[0]]
print('done')
    
            
            
    

                
                
                
    
