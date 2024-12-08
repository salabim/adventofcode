import aocd

data = aocd.get_data(year=2022, day=9)

fields1 = {(0,0)}
fields9 = {(0,0)}
x=[0 for _ in range(10)]
y=[0 for _ in range(10)]

for line in data.splitlines():
    direction, n = line.split()
    
    for _ in range(int(n)):
        for i in range(10):
            if i == 0:
                x[0] += -(direction == "L") + (direction =="R")
                y[0] += -(direction == "D") + (direction =="U")
            else:             
                diff_x = x[i-1]- x[i]
                diff_y = y[i-1] - y[i]
                if abs(diff_x) >=2 or abs(diff_y)>=2:
                    x[i]+= diff_x // (abs(diff_x) or 1)
                    y[i]+= diff_y // (abs(diff_y) or 1)
        fields1.add((x[1], y[1])) 
        fields9.add((x[9], y[9])) 
        
print(f"Part 1= {len(fields1)}")
print(f"Part 2= {len(fields9)}")
