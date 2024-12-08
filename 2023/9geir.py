
import aocd

lines = """\
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45""".splitlines()

lines = aocd.get_data(year=2023, day=9).splitlines()
data = [list(map(int,line.split())) for line in lines]

def extrapolate_forward(numbers):
    """Extrapolate a number series to find the next number in the series.

    ## Example:​
    >>> extrapolate_forward([1, 3, 6, 10, 15, 21])
    28
    """
    last_diff = [numbers[-1]]
    while any(diff != 0 for diff in numbers):
        numbers = [second - first for first, second in zip(numbers, numbers[1:])]
        last_diff.append(numbers[-1])
    return sum(last_diff)

def extrapolate_backward(numbers):
    """Extrapolate a number series to find the previous number in the series.

    ## Example:

    >>> extrapolate_backward([2, 4, 7, 11, 16, 22])
    1
    """
    first_diff = [numbers[0]]
    while any(diff != 0 for diff in numbers):
        numbers = [second - first for first, second in zip(numbers, numbers[1:])]
        first_diff.append(numbers[0])

    return sum((-1 if idx % 2 else 1) * diff for idx, diff in enumerate(first_diff))


print('Part 1=',sum(extrapolate_forward(numbers) for numbers in data))
print('Part 2=', sum(extrapolate_backward(numbers) for numbers in data))


