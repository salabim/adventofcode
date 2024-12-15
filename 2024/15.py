import aocd
import peek


def solve(part, gps=0):
    grid_as_str = data.split("\n\n")[0]
    if part==2:
        grid_as_str = grid_as_str.replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@.")

    grid = {complex(x, y): c for y, r in enumerate(grid_as_str.split("\n")) for x, c in enumerate(r)}

    pos = [c for c, char in grid.items() if char == "@"][0]
    grid[pos] = "."

    def collect(c):
        if grid[c + d] not in "]O[":
            return {}
        dn = d + ("]O[".index(grid[c + d]) - 1 if d.imag else 0)
        return {c + d: grid[c + d], c + dn: grid[c + dn]} | collect(c + d) | collect(c + dn)

    for m in moves:
        d = move_to_dir[m]
        if grid[pos + d] != "#":
            blocks = collect(pos)
            for x, char in blocks.items():
                if grid[x + d] == "#":
                    break
            else:
                for x, char in blocks.items():
                    grid[x] = "."
                for x, char in blocks.items():
                    grid[x + d] = char
                pos = pos + d
    result=int(sum(x.imag * 100 + x.real for x, c in grid.items() if c in "[O"))
    peek(part,result)

data = aocd.get_data(year=2024, day=15)

move_to_dir = {"<": -1, ">": 1, "^": -1j, "v": 1j}
moves = data.split("\n\n")[1].replace("\n", "")

solve(1)
solve(2)

# 1349898
# 1376686
