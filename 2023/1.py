import aocd

lines = aocd.get_data(year=2023, day=1).splitlines()
print("part 1=", sum(10 * int(next(filter(str.isdigit, line))) + int(next(filter(str.isdigit, reversed(line)))) for line in lines))

for lineno, line in enumerate(lines):
    result = ""
    for index in range(len(line)):
        for i, spelled in enumerate("one two three four five six seven eight nine".split(), 1):
            if line[index:].startswith(spelled):
                result += str(i)
                break
        else:
            result += line[index]
    lines[lineno] = result

print("part 2=",sum(10 * int(next(filter(str.isdigit, line))) + int(next(filter(str.isdigit, reversed(line)))) for line in lines))


part2 = sum(10 * int(next(filter(str.isdigit, line))) + int(next(filter(str.isdigit, reversed(line))))for line in aocd.get_data(year=2023, day=1).replace("one", "o1e").replace("two", "t2o").replace("three", "t3e").replace("four", "f4r").replace("five", "f5e").replace("six", "s6x").replace("seven", "s7n").replace("eight", "e8t").replace("nine", "n9e").splitlines())
print(part2)

# 54667
# 54203

