import aocd

example_data = aocd.models.Puzzle(year=2022, day=4).example_data

def spec_to_set(spec):
    return set(range(int(spec.split("-")[0]), int(spec.split("-")[1]) + 1))


total1 = total2 = 0
for line in aocd.get_data(day=4, year=2022).splitlines():
    set0 = spec_to_set(line.split(",")[0])
    set1 = spec_to_set(line.split(",")[1])
    if not ((set0 - set1) and (set1 - set0)):
        total1 += 1
    if set0 & set1:
        total2 += 1
print(f"Part 1 = {total1}")
print(f"Part 2 = {total2}")

# fmt:off

from aocd import get_data
print("Part 1 =", sum(bool(not((set(range(int(line.split(",")[0].split("-")[0]), int(line.split(",")[0].split("-")[1]) + 1)) - set(range(int(line.split(",")[1].split("-")[0]), int(line.split(",")[1].split("-")[1]) + 1))) and (set(range(int(line.split(",")[1].split("-")[0]), int(line.split(",")[1].split("-")[1]) + 1)) - set(range(int(line.split(",")[0].split("-")[0]), int(line.split(",")[0].split("-")[1]) + 1))))) for line in get_data(day=4, year=2022).splitlines()))       
print("Part 2 =", sum(bool(set(range(int(line.split(",")[0].split("-")[0]), int(line.split(",")[0].split("-")[1]) + 1)) & set(range(int(line.split(",")[1].split("-")[0]), int(line.split(",")[1].split("-")[1]) + 1))) for line in get_data(day=4, year=2022).splitlines()))

# fmt: on


print(
    "Part 1 =",
    sum(
        bool(
            not (
                (
                    set(range(int(line.split(",")[0].split("-")[0]), int(line.split(",")[0].split("-")[1]) + 1))
                    - set(range(int(line.split(",")[1].split("-")[0]), int(line.split(",")[1].split("-")[1]) + 1))
                )
                and (
                    set(range(int(line.split(",")[1].split("-")[0]), int(line.split(",")[1].split("-")[1]) + 1))
                    - set(range(int(line.split(",")[0].split("-")[0]), int(line.split(",")[0].split("-")[1]) + 1))
                )
            )
        )
        for line in get_data(day=4, year=2022).splitlines()
    ),
)
print(
    "Part 2 =",
    sum(
        bool(
            set(range(int(line.split(",")[0].split("-")[0]), int(line.split(",")[0].split("-")[1]) + 1))
            & set(range(int(line.split(",")[1].split("-")[0]), int(line.split(",")[1].split("-")[1]) + 1))
        )
        for line in get_data(day=4, year=2022).splitlines()
    ),
)

# 538
# 792
