import aocd
from collections import defaultdict
from pprint import pprint
from math import sqrt, ceil, floor

lines = """\
Time:      7  15   30
Distance:  9  40  200""".splitlines()

lines = aocd.get_data(year=2023, day=6).splitlines()

product = 1
for t, d in zip(map(int, lines[0].split()[1:]), map(int, lines[1].split()[1:])):
    n1 = ceil((t - sqrt(t * t - 4 * d)) / 2+1e-8)
    n2 = floor((t + sqrt(t * t - 4 * d)) / 2-1e-8)       
    n = n2 - n1 + 1
    product *= n
print("part 1=", product)
t = int(lines[0][9:].replace(" ", ""))
d = int(lines[1][9:].replace(" ", ""))
n1 = ceil((t - sqrt(t * t - 4 * d)) / 2)
n2 = floor((t + sqrt(t * t - 4 * d)) / 2)
n = n2 - n1 + 1   
print("part 2=", n)

# 771628
# 27363861

