import aocd
import itertools

def hash(s):
    result = 0
    for i in map(ord,s):
        result=((result+i)*17)%256
    return result

codes = aocd.get_data(year=2023, day=15).split(",")

print(f"Part 1 =", sum(map(hash,codes)))

p1, labels, boxes = 0, {}, [[] for _ in range(256)]
for HASH in codes:
    initiate = 0
    for e, x in enumerate(HASH):
        if x in "-=":
            box, sign, label, focal = initiate, x, *HASH.split(x)
        initiate = ((initiate + ord(x)) * 17) % 256
    p1 += initiate
    labels[label] = labels.get(label, {})
    if sign == "-" and label in boxes[box]:
        boxes[box].remove(label)
        labels[label].pop(box)
    elif sign == "=":
        labels[label][box] = int(focal)
        if label not in boxes[box]:
            boxes[box].append(label)
print(p1, sum(sum((x + 1) * (y + 1) * labels[label][x] for y, label in enumerate(box)) for x, box in enumerate(boxes)))