import aocd
import itertools
import functools

data = aocd.get_data(year=2022, day=13)


def compare(left, right):
    for left, right in itertools.zip_longest(left, right):
        if left is None:
            return -1
        if right is None:
            return 1

        if isinstance(left, int) and isinstance(right, int):
            if left < right:
                return -1
            if left > right:
                return 1
        else:
            left = [left] if isinstance(left, int) else left
            right = [right] if isinstance(right, int) else right
            if compare(left, right):
                return compare(left, right)


print("Part 1 =", sum(index for index, line in enumerate(data.split("\n\n"), 1) if compare(*list(map(eval, line.split("\n")))) == 1))

packets = sorted([eval(line) for line in data.splitlines() if line] + [[[2]]] + [[[6]]], key=functools.cmp_to_key(compare))
print("Part 2 =", (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))
