import aocd

lines = aocd.get_data(year=2023, day=4).splitlines()

print("part 1=", sum(int(2 ** (len(set(line.split(":")[1].split("|")[0].split()) & set(line.split(":")[1].split("|")[1].split())) - 1)) for line in lines))
# 23235


sum2 = 0
cards = [1 for _ in range(len(lines))]
for i, line in enumerate(lines):
    for j in range(i + 1, i + len(set(line.split(":")[1].split("|")[0].split()) & set(line.split(":")[1].split("|")[1].split())) + 1):
        cards[j] += cards[i]

print("part 2=", sum(cards))
#5920640

