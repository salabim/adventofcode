import aocd
from math import sqrt, ceil, floor

lines = """\
Time:      7  15   30
Distance:  9  40  200""".splitlines()

lines = aocd.get_data(year=2023, day=6).splitlines()

result = 1
for t, d in zip(map(int, lines[0].split()[1:]), map(int, lines[1].split()[1:])):   
    result *= (floor((t + sqrt(t * t - 4 * d)) / 2-1e-8)-ceil((t - sqrt(t * t - 4 * d)) / 2+1e-8) +1)
print("part 1=", result)

t = int(lines[0][9:].replace(" ", ""))
d = int(lines[1][9:].replace(" ", ""))

print("part 2=", floor((t + sqrt(t * t - 4 * d)) / 2-1e-8)-ceil((t - sqrt(t * t - 4 * d)) / 2+1e-8) +1)

# 771628
# 27363861
