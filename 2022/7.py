import aocd

data = aocd.get_data(year=2022, day=7)


class Directory:
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.subdirs = set()
        self.files = {}

    def size(self):
        return sum(self.files.values()) + sum(subdir.size() for subdir in self.subdirs)

    def __repr__(self):
        return f'{self.parent or ""}/{self.name}'

    def walk(self):
        yield self
        for subdir in self.subdirs:
            yield from subdir.walk()


root = curdir = Directory(parent=None, name="root")

for line in data.splitlines():
    if line.startswith("$ cd"):
        cd = line[5:]
        if cd == "..":
            curdir = curdir.parent
        elif cd == "/":
            ...
        else:
            for subdir in curdir.subdirs:
                if subdir.name == cd:
                    break
            else:
                subdir = Directory(parent=curdir, name=cd)
                curdir.subdirs.add(subdir)
            curdir = subdir
    elif line.startswith("$ ls") or line.startswith("dir"):  # just ignore
        ...
    else:
        size, name = line.split()
        curdir.files[name] = int(size)

sizes = [d.size() for d in root.walk()]

print("Part 1", sum(size for size in sizes if size < 100000))

to_clear = root.size() - 40000000

print("Part 2", min(size for size in sizes if size >= to_clear))
