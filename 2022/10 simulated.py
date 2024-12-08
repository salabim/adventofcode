import aocd
import textwrap
import salabim as sim

data = aocd.get_data(year=2022, day=10)

class AoC(sim.Component):
    def process(self):
        cycle = 1
        total = 0
        x = 1
           
        crt = ''
        for line in data.splitlines():
            for _ in range(1 if line[0] == 'n' else 2):
                total += x * cycle * (cycle % 40 == 20)       
                crt += '#' if max(x,1)  <=cycle % 40 <=x+2 else '.'
                cycle +=1
            x += 0 if line[0] == 'n' else int(line[5:]) 
             
        print(f'Part 1 = {total}')
        print('Part 2')
        
        print('\n'.join(textwrap.wrap(crt,40)))
            
