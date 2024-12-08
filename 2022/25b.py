import aocd

import collections
TO_SNAFU = {-2: "=", -1: "-", 0: "0", 1: "1", 2: "2"}
FROM_SNAFU = {snafu: dec for dec, snafu in TO_SNAFU.items()}


lines = aocd.get_data(year=2022, day=25).splitlines()

digits=collections.defaultdict(int)
for snafu in lines:
    for idx, digit in enumerate(snafu[::-1]):
        digits[idx] += FROM_SNAFU[digit]
for idx in digits:
    while digits[idx] < -2:
        digits[idx] += 5
        digits[idx + 1] -= 1
    while digits[idx] > 2:
        digits[idx] -= 5
        digits[idx + 1] += 1

print("".join(TO_SNAFU[digit] for _, digit in sorted(digits.items()))[::-1])
print('2=0-2-1-0=20-01-2-20')
