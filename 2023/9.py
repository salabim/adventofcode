import aocd

lines = """\
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45""".splitlines()

lines = aocd.get_data(year=2023, day=9).splitlines()
result = 0
for line in lines:
    n = [list(map(int, line.split()))]
    while True:
        n.append([(item1 - item0) for item0, item1 in zip(n[-1], n[-1][1:])])
        if not any(n[-1]):
            break
    n[-1].append(0)
    for i in range(len(n) - 2, -1, -1):
        n[i].append(n[i][-1] + n[i + 1][-1])
    result += n[i][-1]
print("Part 1=", result)


n = [list(map(int, line.split()))]
result = 0
for line in lines:
    n = [list(map(int, line.split()))]
    while True:
        n.append([(item1 - item0) for item0, item1 in zip(n[-1], n[-1][1:])])
        if not any(n[-1]):
            break
    n[-1] = [0] + n[-1]
    for i in range(len(n) - 2, -1, -1):
        n[i] = [n[i][0] - n[i + 1][0]] + n[i]
    result += n[i][0]
print("Part 2=", result)

