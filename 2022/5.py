import aocd
import copy

lines = aocd.get_data(year=2022, day=5).splitlines()

pile_names_line = next(line for line in lines if line.startswith(" 1"))
piles1 = {pile_name: [] for pile_name in pile_names_line.split()}
lines = iter(lines)  # iter makes that we can continue with the moves section easily

for line in lines:
    if not line:  # break on empty line
        break
    for c, pile_name in zip(line, pile_names_line):
        if c.isalpha():
            piles1[pile_name].insert(0, c)

max_height = 0

piles2 = copy.deepcopy(piles1)
for line in lines:
    _, number, _, from_, _, to = line.split()
    index = len(piles2[from_]) - int(number)
    for i in range(int(number)):
        piles1[to].append(piles1[from_].pop())
        piles2[to].append(piles2[from_].pop(index))
    max_height = max(max_height, len(piles1[to]))
print(max_height)
message1 = "".join(piles1[pile_name][-1] for pile_name in piles1)
message2 = "".join(piles2[pile_name][-1] for pile_name in piles1)
print(f"Part 1 = {message1}")
print(f"Part 2 = {message2}")


# LBLVVTVLP
# TPFFBDRJD
