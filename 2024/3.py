import aocd
import re

s = aocd.get_data(year=2024, day=3)


def score(s):
    return sum(
        eval(match.group().replace("mul(", "").replace(")", "").replace(",", "*"))
        for matchNum, match in enumerate(re.finditer(r"mul\([0-9]+,[0-9]+\)", s, re.MULTILINE), start=1)
    )


print("Part1:", score(s))

print("Part2:", sum(score(part.split("do()", 1)[1]) for part in ("(don't()do()" + s).split("don't()") if len(part.split("do()", 1)) == 2))

# result1=159892596
# result2=92626942
