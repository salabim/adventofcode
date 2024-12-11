import aocd
import collections
import functools
import peek

stones = list(map(int,aocd.get_data(year=2024, day=11).split()))

@functools.cache
def blink_stone(stone:int, steps:int) -> int:
    """Take the stone inscription and number of blink steps and returns the number of resulting
    stones"""
    if steps == 0:
        return 1
    if stone == 0:
        return blink_stone(1, steps - 1)
    stone_str = str(stone)
    stone_str_half, stone_str_odd = divmod(len(stone_str), 2)
    if not stone_str_odd:
        return (blink_stone(int(stone_str[:stone_str_half]), steps - 1) + 
                blink_stone(int(stone_str[stone_str_half:]), steps - 1))
    return blink_stone(stone * 2024, steps - 1)

peek(sum(blink_stone(stone, steps=25) for stone in stones), to_clipboard=True)
peek(sum(blink_stone(stone, steps=500) for stone in stones), to_clipboard=True)
   

# part1=186424
# part2=219838428124832
