import aocd
import peek
from collections import Counter

lines = aocd.get_data(year=2024, day=1).splitlines()
# lines="""\
# 3   4
# 4   3
# 2   5
# 1   3
# 3   9
# 3   3""".splitlines()

l0=[]
l1=[]
for line in lines:
    n0,n1=line.split()
    l0.append(int(n0))
    l1.append(int(n1))

l0.sort()
l1.sort()
result1=0
for n0,n1 in zip(l0,l1):
    result1+=abs(n0-n1)
peek(result1)

result2 = sum(value*l1.count(value) for value in l0)

result2 = sum(Counter(l1)[value] * value * count for value, count in Counter(l0).items())
#result2 = sum

#result=1889772
#result=23228917