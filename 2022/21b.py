import aocd
import collections

data = aocd.get_data(year=2022, day=21)


expressions = [compile(line.replace(":", "="), "", "exec") for line in data.splitlines()]

while True:
    for expression in expressions[:]:
        try:
            exec(expression, globals())
        except NameError:
            expressions.append(expression)
    try:
        print("Part 1 =", int(root))
        break
    except NameError:
        ...



expressions = []

for line in data.splitlines():
    if line.startswith("root"):
        var0 = line.split()[1]
        var1 = line.split()[3]
    elif not line.startswith("humn"):
        expressions.append(compile(line.replace(":", "="), "", "exec"))


def yell(expressions, humn, var0, var1):
    remaining_expressions = collections.deque(expressions)
    while remaining_expressions:
        expression = remaining_expressions.popleft()
        try:
            exec(expression, {}, locals())
        except NameError:
            remaining_expressions.append(expression)

    return eval(var0), eval(var1)


i0 = 0
i1 = 10000000000000000
var0_where_humn_is_0, var1_where_humn_is_0 = yell(expressions, 0, var0, var1)
var0_where_humn_is_1, var1_where_humn_is_1 = yell(expressions, 1, var0, var1)

if var0_where_humn_is_0 == var0_where_humn_is_1:
    var0, var1 = var1, var0
    goal = var0_where_humn_is_0
else:
    goal = var1_where_humn_is_0

while True:
    i = (i0 + i1) // 2
    var0_where_humn_is_i, _ = yell(expressions, i, var0, var1)
    if goal < var0_where_humn_is_i:
        i0 = i
    elif goal > var0_where_humn_is_i:
        i1 = i
    else:
        break
print("Part 2 =", i)
