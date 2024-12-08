import aocd

data = aocd.get_data(year=2022, day=7)


class Directory:
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.subdirs = set()
        self._size = 0

    def size(self):
        return self._size + sum(subdir.size() for subdir in self.subdirs)

    def walk(self):
        yield self
        for subdir in self.subdirs:
            yield from subdir.walk()


root = Directory(parent=None, name="root")

for line in data.splitlines():
    if line.startswith("$ cd"):
        cd = line[5:]
        if cd == "..":
            curdir = curdir.parent
        elif cd == "/":
            curdir = root
        else:
            subdir = next((subdir for subdir in curdir.subdirs if subdir.name == cd), None)
            if subdir is None:
                subdir = Directory(parent=curdir, name=cd)
                curdir.subdirs.add(subdir)
            curdir = subdir

    elif line.startswith("$ ls"):
        curdir._size = 0  # just in case there are more than two ls commands for the same directory

    elif not line.startswith("dir"):  # ignore dir lines
        curdir._size += int(line.split()[0])

sizes = [d.size() for d in root.walk()]

print("Part 1", sum(size for size in sizes if size < 100000))


print("Part 2", min(size for size in sizes if size >= root.size() - 40000000))
