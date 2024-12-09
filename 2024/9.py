# this is an extremely not even quick and dirty solution
# but its works

import aocd
import peek

spec = aocd.get_data(year=2024, day=9)
fs = []
state = 1
id = 0
for n, i in enumerate(spec, 1):
    for _ in range(int(i)):
        fs.append(id if state == 1 else -1)
    state = 1 - state
    if state:
        id += 1

left = 0
right = len(fs) - 1
while True:
    while fs[right] == -1:
        right -= 1
    while fs[left] != -1:
        left += 1
    if left > right:
        break
    fs[left] = fs[right]
    fs[right] = -1



result1 = 0
for pos, id in enumerate(fs):
    if id == -1:
        break
    result1 += pos * id

peek(result1)

class Block:
    def __init__(self, length, id):
        self.length=length
        self.id=id

    def __repr__(self):
        return f"Block(length={self.length}, id={self.id})"


blocks = []
lengths = {}
state = 1
id = 0
for n, i in enumerate(spec, 1):
    blocks.append(Block(length=int(i), id=id if state == 1 else -1))
    if state:
        lengths[id] = int(i)
    state = 1 - state
    if state:
        id += 1

for id in reversed(lengths):
    for pos in range(len(blocks)):
        if blocks[pos].id == id:
            break
        if blocks[pos].id == -1 and blocks[pos].length >= lengths[id]:  # it fits
            blocks[pos].length -= lengths[id]
            for pos1 in range(pos, len(blocks)):
                if blocks[pos1].id == id:  # found the block
                    block = blocks.pop(pos1)
                    break
            blocks.insert(pos, block)
            blocks.insert(pos1,Block(length=block.length,id=-1))
            for _ in range(2):
                for pos0 in range(len(blocks)-1):
                    if blocks[pos0]==-1 and blocks[pos1]==-1:
                        blocks[pos0].length+=blocks[pos1].length
                        blocks.pop(pos1)


            break



fs=[]
for block in blocks:
    for _ in range(int(block.length)):
        fs.append(block.id)

result2 = 0
for pos, id in enumerate(fs):
    if id != -1:
        result2 += pos * id

peek(result2)
