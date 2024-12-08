import aocd


data = aocd.get_data(year=2022, day=10)

cycle = 1
total = 0
register = 1

def display():
    print()
    for i in range(6):
        print(crt[i*40: i*40+40])


def pos(cycle):
    x,y =divmod(cycle,40)
    return x,y
    
crt = ''
for line in data.splitlines():
#    print(line    )
    if line[:4] == 'noop':
        d = 1
        argument = 0
        
    elif line[:4] == 'addx':
        d = 2
        argument = int(line[5:])

    for _ in range(d):
        if cycle in (20, 60, 100, 140, 180, 220):
            total += register * cycle
            print(cycle, register, register * cycle)
        x = cycle % 40 -1
        print(x, register)
        if x in (register-1, register, register+1):
            c = '#'  
        else:
            c= ' '    
        crt += c 

        cycle +=1
    register +=  argument
display()     
print(total)
        
