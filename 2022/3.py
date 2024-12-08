
from aocd import get_data
import string

def priority(letter):
    return string.ascii_letters.index(letter) + 1

lines = get_data(day=3, year=2022).splitlines()
total = 0
for line in lines:
    common_char = (set(line[:len(line)//2]) & set(line[len(line)//2:])).pop()
    total += priority(common_char)
print(f"Part 1 {total}")

total = 0
for l0, l1, l2 in zip(lines[::3], lines[1::3], lines[2::3]):
    common_badge = (set(l0) & set(l1) & set(l2)).pop()
    total += priority(common_badge)
print(f"Part 2 {total}")
  
from aocd import get_data

print("Part 1", sum(" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".index((set(line[:len(line)//2]) & set(line[len(line)//2:])).pop()) for line in get_data(day=3, year=2022).splitlines()))

print("Part 2", sum (" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".index((set(l0) & set(l1) & set(l2)).pop()) for l0, l1, l2 in zip(get_data(day=3, year=2022).splitlines()[::3], get_data(day=3, year=2022).splitlines()[1::3], get_data(day=3, year=2022).splitlines()[2::3])))


       
# 8072
# 2567  
