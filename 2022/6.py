import aocd

data = aocd.models.Puzzle(year=2022, day=6).example_data

data = aocd.get_data(year=2022, day=6)


def total(n):
    for i in range(n, len(data)):
        if len(set(data[i - n : i])) == n:
            return i


print(f"Part 1 = {total(4)}")
print(f"Part 2 = {total(14)}")

total = 0

import aocd

print("Part 1 =", next(i for i, marker in enumerate(zip(*(aocd.get_data(year=2022, day=6)[i:] for i in range(4))), 4) if len(set(marker)) == 4))
print("Part 1 =", next(i for i, marker in enumerate(zip(*(aocd.get_data(year=2022, day=6)[i:] for i in range(14))), 14) if len(set(marker)) == 14))

import aocd

data = aocd.get_data(year=2022, day=6)


def total(data, n):
    for i, marker in enumerate(zip(*(data[i:] for i in range(n))), n):
        if len(set(marker)) == n:
            return i


print(f"Part 1 = {total(data, 4)}")
print(f"Part 2 = {total(data, 14)}")

# 1598
# 2414

import aocd
import collections

data = aocd.get_data(year=2022, day=6)


def total(data, n):
    last_n = collections.deque(maxlen=n)
    for i, c in enumerate(data, 1):
        last_n += c  # we could also use c.append(last_n)
        if len(set(last_n)) == n:
            return i


print(f"Part 1 = {total(data, 4)}")
print(f"Part 2 = {total(data, 14)}")
