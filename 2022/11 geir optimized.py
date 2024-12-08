# Standard library imports
import aocd
import math
import time


def parse_data(puzzle_input):
    """Parse input."""
    return {idx: parse_monkey(lines) for idx, lines in enumerate(puzzle_input.split("\n\n"))}


def parse_monkey(lines):
    """Parse information about one monkey.
    ## Example:
    >>> lines = '''
    ... Monkey 2:
    ...   Starting items: 84, 93, 70
    ...   Operation: new = old + 2
    ...   Test: divisible by 5
    ...     If true: throw to monkey 5
    ...     If false: throw to monkey 1
    ... '''
    >>> parse_monkey(lines)  # doctest: +ELLIPSIS
    {'items': [84, 93, 70], 'operation': '+ 2', 'operate': <function ...>,
     'divisible_by': 5, 'to_monkey': (1, 5)}
    """
    monkey = {}
    for line in lines.split("\n"):
        match line.split():
            case ["Starting", "items:", *items]:
                monkey["items"] = [int(item.strip(",")) for item in items]
            case ["Operation:", *_, "+", number]:
                monkey["operation"] = f"+ {number}"
                monkey["operate"] = lambda old, number=int(number): old + number
            case ["Operation:", *_, "*", "old"]:
                monkey["operation"] = "^2"
                monkey["operate"] = lambda old: old**2
            case ["Operation:", *_, "*", number]:
                monkey["operation"] = f"* {number}"
                monkey["operate"] = lambda old, number=int(number): old * number
            case ["Test:", *_, number]:
                monkey["divisible_by"] = int(number)
            case ["If", "true:", *_, number]:
                monkey["to_monkey"] = int(number)
            case ["If", "false:", *_, number]:
                monkey["to_monkey"] = (int(number), monkey["to_monkey"])
            case _:
                pass
    return monkey


def part1(monkeys):
    """Solve part 1."""
    return chase(monkeys, rounds=20, reducer=3)


def part2(monkeys):
    """Solve part 2."""
    return chase(monkeys, rounds=10_000, reducer=1)


def chase(monkeys, rounds, reducer):
    """Chase the monkeys for the given number of rounds.
    >>> monkeys = {
    ...     0: {"items": [4, 1, 8], "operate": lambda o: o + 4, "divisible_by": 11, "to_monkey": (2, 1)},
    ...     1: {"items": [], "operate": lambda o: o * 3, "divisible_by": 7, "to_monkey": (0, 2)},
    ...     2: {"items": [0, 6], "operate": lambda o: o * o, "divisible_by": 13, "to_monkey": (1, 0)},
    ... }
    >>> chase(monkeys, 3, 2)
    80
    """
    counts = [0] * len(monkeys)
    modulo = math.prod(monkey["divisible_by"] for monkey in monkeys.values())
    for _ in range(rounds):
        for monkey_id in range(len(monkeys)):
            counts[monkey_id] += len(monkeys[monkey_id]["items"])
            inspect(monkeys, monkey_id, reducer, modulo)
    return math.prod(sorted(counts)[-2:])


def inspect(monkeys, monkey_id, reducer, modulo):
    monkey = monkeys[monkey_id]
    for item in monkey["items"]:
        new_item = (monkey["operate"](item) // reducer) % modulo
        to_monkey = monkey["to_monkey"][new_item % monkey["divisible_by"] == 0]
        monkeys[to_monkey]["items"].append(new_item)
    monkey["items"].clear()


data = parse_data(aocd.get_data(year=2022, day=11))
t0 = time.perf_counter()
print(part2(data))
print(time.perf_counter() - t0)
