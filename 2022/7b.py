import aocd
import collections

data = aocd.get_data(year=2022, day=7)

my_sizes = collections.defaultdict(int)

for line in data.splitlines():
    if line.startswith("$ cd"):
        cd = line[5:]
        if cd == "..":
            curdir = "/".join(curdir.split("/")[:-1])
        elif cd == "/":
            curdir = ""
        else:
            curdir += "/" + cd

    elif line.startswith("$ ls"):
        my_sizes[curdir] = 0  # just in case there are more than two ls commands for the same directory

    elif not line.startswith("dir"):  # ignore dir lines
        my_sizes[curdir] += int(line.split()[0])

sizes = collections.defaultdict(int)
for curdir in my_sizes.keys():
    for d, size in my_sizes.items():
        if d.startswith(curdir):
            sizes[curdir] += my_sizes[d]

print("Part 1", sum(size for size in sizes.values() if size < 100000))
print("Part 2", min(size for size in sizes.values() if size >= sizes[""] - 40000000))
