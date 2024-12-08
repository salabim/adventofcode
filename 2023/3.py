from collections import defaultdict
import aocd
import pprint

lines="""\
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..""".splitlines()
lines = aocd.get_data(year=2023, day=3).splitlines()

def check(x,y):
    borders=set()
    for ix in (-1,0,1):
        for iy in (-1,0,1):
            if (x+ix,y+iy) in s:
                borders.add((x+ix, y+iy))
    return borders

s= {}
sxy={}

for x,line in enumerate(lines):
    for y,c in enumerate(line):
        if c not in '0123456789.':
           s[(x,y)]=c
           sxy[(x,y)]=set()

sum1=0
adjacent=defaultdict(set)
for x,line in enumerate(lines):
    number=""
    for y,c in enumerate(line+"."):
        if number=="":
            if c.isdigit():
                borders = check(x,y)
                number_borders = borders
                number=c
               
        else:
            if c.isdigit():
                borders = check(x,y)
                number_borders |= borders
                number=number+c
            else:
                if number_borders:
                    sum1+=int(number)
                    for xy in number_borders:
                        sxy[xy].add((x,y,int(number)))
                number=""
sum2=0
for xy,c in s.items():
    if c == "*":
        if len(sxy[xy])==2:
            product=1
            for x,y,n in sxy[xy]:
                product*=n
            sum2+=product

print("Part 1=",sum1)
print("Part 2=",sum2)

#56070
#91622824
