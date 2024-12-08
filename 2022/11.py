import aocd
import collections
import functools

data = '''\
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1'''
#data = aocd.get_data(year=2022, day=11)

Monkey = collections.namedtuple('Monkey', 'name items ops divby true_monkey false_monkey')
monkies = {}

    
@functools.lru_cache()
def op(name, item):
    return eval(monkies[name].ops, {'old':item})    
    
@functools.lru_cache()
def divby_(name, item):
    return item % monkies[name].divby == 0
    
specs = data.split('\n\n')

def solve(number_of_rounds, divider):
        
    for spec in specs:
        lines = spec.splitlines()
        name = lines[0].split()[-1][:-1]
        items = collections.deque(map(int,lines[1][18:].replace(' ','').split(',')))
        ops = lines[2].split('=')[1]
        divby = int(lines[3].split('by')[1])
        true_monkey = lines[4].split()[-1]
        false_monkey = lines[5].split()[-1]    
    #    print(f'{repr(name)}{items} {ops} {divby} {repr(true_monkey)} {repr(false_monkey)}')
        monkies[name]=Monkey(name, items, ops, divby,  true_monkey, false_monkey)
    
        
    count = dict.fromkeys(monkies, 0)
    
    for round in range(number_of_rounds):
        if round % 1 == 0:
            print(round,end=' ')
        for monkey in monkies.values():
            while monkey.items:
                count[monkey.name] +=1
                item =monkey.items.popleft()
                item =  op(monkey.name, item)
#                item = item // divider
                if divby_(monkey.name,item):
                    monkies[monkey.true_monkey].items.append(item)
                else:
                    monkies[monkey.false_monkey].items.append(item)
    print(count.values())
    counts = sorted(count.values())
    
    print(counts[-2]*counts[-1])
    
solve(20,3)
solve(1000, 1)
