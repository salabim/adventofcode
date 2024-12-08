import aocd


lines = aocd.get_data(year=2023, day=4).splitlines()
sum1 = 0
for line in lines:
    wins, owns = line.split(":")[1].split("|")
    win = set(wins.split())
    own = set(owns.split())
    sum1 += int(2 ** (len(win & own) - 1))
print("part 1=", sum1)
# 23235


sum2 = 0
cards = [1 for _ in range(len(lines))]
for i, line in enumerate(lines):
    wins, owns = line.split(":")[1].split("|")
    win = set(wins.split())
    own = set(owns.split())
    n = len(win & own)
    for j in range(i + 1, i + n + 1):
        cards[j] += cards[i]

print("part 2=", sum(cards))
# 5920640

