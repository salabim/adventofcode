looses = dict(A="Z", B="X", C="Y")
draws = dict(A="X", B="Y", C="Z")
wins = dict(A="Y", B="Z", C="X")
points = dict(X=1, Y=2, Z=3)


def score(you, me):
    result = points[me]
    if wins[you] == me:
        result += 6
    if draws[you] == me:
        result += 3
    return result


total = 0
with open("2.txt", "r") as file:
    for line in file.readlines():
        if line.strip():
            total += score(line[0], line[2])
print(total)

total = 0
with open("2.txt", "r") as file:
    for line in file.readlines():
        line = line.strip()
        if line:
            you = line[0]
            if line[2] == "Z":
                me = wins[you]
            elif line[2] == "Y":
                me = draws[you]
            else:
                me = looses[you]
            total += score(you, me)
print(total)


print(sum(dict(BX=1, CY=2, AZ=3, AX=4, BY=5, CZ=6, CX=7, AY=8, BZ=9)[line[0] + line[2]] for line in open("2.txt", "r") if line.strip()))
print(sum(dict(BX=1, CY=6, AZ=8, AX=3, BY=5, CZ=7, CX=2, AY=4, BZ=9)[line[0] + line[2]] for line in open("2.txt", "r") if line.strip()))

from aocd import get_data
print(sum(dict(BX=1, CY=2, AZ=3, AX=4, BY=5, CZ=6, CX=7, AY=8, BZ=9)[line[0] + line[2]] for line in get_data(day=2, year=2022).splitlines()))
print(sum(dict(BX=1, CY=6, AZ=8, AX=3, BY=5, CZ=7, CX=2, AY=4, BZ=9)[line[0] + line[2]] for line in get_data(day=2, year=2022).splitlines()))
