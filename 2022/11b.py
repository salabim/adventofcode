import aocd
import collections


def solve(number_of_rounds, divider):
    data = aocd.get_data(year=2022, day=11)

    Monkey = collections.namedtuple("Monkey", "name items ops divby choose")
    monkies = {}

    specs = data.split("\n\n")

    modulo = 1

    for spec in specs:
        lines = spec.splitlines()
        name = lines[0].split()[-1][:-1]
        items = list(map(int, lines[1][18:].replace(" ", "").split(",")))
        ops = lines[2].split("=")[1]
        divby = int(lines[3].split("by")[1])
        modulo *= divby
        choose = (lines[5].split()[-1], lines[4].split()[-1])
        monkies[name] = Monkey(name, items, ops, divby, choose)

    count = dict.fromkeys(monkies, 0)

    for _ in range(number_of_rounds):
        for monkey in monkies.values():
            for item in monkey.items:
                item = eval(monkey.ops, {"old": item}) % modulo
                item //= divider
                monkies[monkey.choose[item % monkey.divby == 0]].items.append(item)
            count[monkey.name] += len(monkey.items)
            monkey.items.clear()
    counts = sorted(count.values())
    return counts[-2] * counts[-1]


print(f"Part 1 = {solve(20, 3)}")
print(f"Part 2 = {solve(10000, 1)}")
