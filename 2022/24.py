import aocd

data = '''\
#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#'''
#data = aocd.get_data(year=2022, day=24)

def lcm(num1,num2):
    for x in range(1,max(num1,num2)):
        if (num1 % x) == 0 and (num2 % x) == 0:
            e=x
    lcm = (num1 * num2) // e
    return lcm
    
x=data.splitlines()
number_of_cycles = lcm(len(x)-2, len(x[0])-2)
print(cycle)


blizzards=set()
direction = {'^': (-1,0), 'v':(1,0), '<':(0,-1), '>':(0,1)}
for row, line in enumerate(data.splitlines()):
    for column, c in enumerate(line):
        if c in direction:
            blizzards.add((row, column, direction[c]))

for cycle in range(number_of_cycles):
    
    for blizzard in blizzards:
                     
print(blizzards)
