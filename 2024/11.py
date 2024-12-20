import aocd
import collections
import functools
import peek

data = aocd.get_data(year=2024, day=11)


@functools.lru_cache
def next_stone(stone):
    if stone == "0":
        return ["1"]
    if (length := len(stone)) % 2 == 0:
        return [stone[: length // 2], str(int(stone[length // 2 :]))]
    return [str(int(stone) * 2024)]


def number_of_stones(number_of_blinks):
    stones = collections.defaultdict(int, dict.fromkeys(data.split(), 1))

    for _ in range(number_of_blinks):
        next_stones = collections.defaultdict(int)
        for stone, number in stones.items():
            for stone1 in next_stone(stone):
                next_stones[stone1] += number
        stones = next_stones
    return sum(stones.values())

peek(number_of_stones(25), to_clipboard=True)
peek(number_of_stones(75), to_clipboard=True)

# part1=186424
# part2=219838428124832
