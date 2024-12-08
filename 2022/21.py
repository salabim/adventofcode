import aocd
import bisect

data = '''\
root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32'''
data = aocd.get_data(year=2022, day=21)
print(data)


expressions = [line.replace(':','=') for line in data.splitlines()]
  
while True:
    for expression in expressions[:]:
        try:
            exec(expression, globals())
        except NameError:
            expressions.append(expression)
    try:
        print(int(root))
        break
    except NameError:
        ...

expressions = [line.replace(':','=') for line in data.splitlines()]

for i, expression in enumerate(expressions):
    if expression.startswith('root'):
        var0 = expression.split()[1]
        var1 = expression.split()[3]
        expressions[i] = '...'
        
    if expression.startswith('humn'):
        expressions[i]='...'
        print(expressions[i])
        
print(len(expressions))
        
def yell(expressions, humn, var0, var1):
    this_expressions=expressions[:]
    namespace = {'humn': humn}  
    while this_expressions:
        expressions_ = []
        for expression in this_expressions[:]:
            try:
                exec(expression, namespace)
            except NameError:
                expressions_.append(expression)
        this_expressions=expressions_
        
    return namespace[var0], namespace[var1]

i0=0
i1=1e30
r00,r10 = yell(expressions,0, var0, var1)
r01,r11 = yell(expressions,1, var0, var1)

if r00 == r01:
    var0, var1 = var1, var0
    target = r10
else:
    target = r10

while True:
    i = (i0+i1) // 2
    r0, _ = yell(expressions,i, var0, var1)   
    if target-r0<0:
        i0=i
    else:
        if target-r0>0:
            i1=i
        else:
            break
print(int(i))




