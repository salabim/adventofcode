import aocd
import itertools
import operator

lines = aocd.get_data(year=2024, day=7).splitlines()

result1=0
for line in lines:
    target=int(line.split(":")[0])
    factors=list(map(int,line.split(":")[1].split()))
    ok=False
    for ops in itertools.product((operator.add,operator.mul), repeat=len(factors)-1):
        calc=factors[0]
        for op, factor in zip(ops, factors[1:]):
            calc = op(calc, factor)
            if calc>target:
                break
        else:
            if calc == target:
                ok=True
        if ok:
            break
    if ok:
        result1+=target

print(result1)
result2=0
for line in lines:
    target=int(line.split(":")[0])
    factors=list(map(int,line.split(":")[1].split()))
    ok=False
    for ops in itertools.product((operator.add,operator.mul,lambda x,y:int(str(x)+str(y))), repeat=len(factors)-1):
        calc=factors[0]
        for op, factor in zip(ops, factors[1:]):
            if op == "concat":
                calc = int(str(calc)+str(factor))
            else:
                calc = op(calc, factor)
        else:
            if calc == target:
                ok=True
        if ok:
            break
    if ok:
        result2+=target

print(result2)

# #result1=5702958180383
# #result2=92612386119138