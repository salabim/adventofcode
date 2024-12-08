import aocd

lines = aocd.get_data(year=2023, day=9).splitlines()
for part in (1, 2):
    result = 0
    for line in lines:
        n = [list(map(int, line.split()))]
        while True:
            n.append([(item1 - item0) for item0, item1 in zip(n[-1], n[-1][1:])])
            if not any(n[-1]):
                break
        if part == 1:
            n[-1].append(0)
            for i in range(len(n) - 2, -1, -1):
                n[i] += [n[i][-1] + n[i + 1][-1]]
            result += n[0][-1]
        if part == 2:
            n[-1] = [0] + n[-1]
            for i in range(len(n) - 2, -1, -1):
                n[i] = [n[i][0] - n[i + 1][0]] + n[i]
            result += n[0][0]
    print(f"Part {part}={result}")
