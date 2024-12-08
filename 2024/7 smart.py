import aocd

lines = aocd.get_data(year=2024, day=7).splitlines()


def solve(i, rest, factors, part):
    if i == 0:
        if rest == factors[0]:
            yield 1
        else:
            return
    else:
        for op in "+*" if part == 1 else "+*|":
            if op == "+":
                value = rest - factors[i]
                if value < 0:
                    continue
            elif op == "*":
                value, remainder = divmod(rest, factors[i])
                if remainder:
                    continue
            elif op == "|":
                if not str(rest).endswith(str(factors[i])):
                    continue
                value_as_str = str(rest)[: len(str(rest)) - len(str(factors[i]))]
                if value_as_str == "":
                    continue
                value = int(value_as_str)

            yield from solve(i=i - 1, rest=value, factors=factors, part=part)


for part in (1, 2):
    result = 0
    for line in lines:
        target = int(line.split(":")[0])
        factors = list(map(int, line.split(":")[1].split()))
        if any(solve(i=len(factors) - 1, rest=target, factors=factors, part=part)):
            result += target

    print(f"Part {part}: {result}")


# #result1=5702958180383
# #result2=92612386119138
