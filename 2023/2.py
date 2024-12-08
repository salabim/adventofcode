import aocd


# 12 red cubes, 13 green cubes, and 14 blue
lines = """\
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green""".splitlines()

lines = aocd.get_data(year=2023, day=2).splitlines()

target = dict(red=12, green=13, blue=14)
sum_id = 0
for line in lines:
    game, line = line.split(":")
    id = int(game[5:])
    match = True
    for sample in line.split(";"):
        for nc in sample.split(","):
            _, n, c = nc.split(" ")
            if int(n) > target[c]:
                match = False
    if match:
        sum_id += id
print(sum_id)
# 1867
sum_power = 0
for line in lines:
    game, line = line.split(":")
    id = int(game[5:])
    max_c = dict(red=0, blue=0, green=0)
    for sample in line.split(";"):
        for nc in sample.split(","):
            _, n, c = nc.split(" ")
            max_c[c] = max(max_c[c], int(n))
    power = max_c["red"] * max_c["blue"] * max_c["green"]
    sum_power += power

print(sum_power)
# 84538

