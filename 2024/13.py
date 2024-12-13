import aocd
import peek

data = """\
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""

data = aocd.get_data(year=2024, day=13)

results = dict.fromkeys((1, 2), 0)
machines = data.split("\n\n")
for machine in machines:
    items = machine.split("+")
    ax = int(items[1].split(",")[0])
    ay = int(items[2].split("\n")[0])
    bx = int(items[3].split(",")[0])
    by = int(items[4].split("\n")[0])
    px = int(items[4].split("=")[1].split(",")[0])
    py = int(items[4].split("=")[2])
    for part in (1, 2):
        px = int(items[4].split("=")[1].split(",")[0]) + (0 if part == 1 else 10000000000000)
        py = int(items[4].split("=")[2]) + (0 if part == 1 else 10000000000000)

        b = (px * ay - py * ax) / (bx * ay - by * ax)
        a = (px - b * bx) / ax

        if a % 1 == 0 and b % 1 == 0:
            results[part] += int(a * 3 + b)

peek(results)

# result1=33209
# result2=83102355665474
