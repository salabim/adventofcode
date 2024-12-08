import aocd


# 12 red cubes, 13 green cubes, and 14 blue

lines = aocd.get_data(year=2023, day=2).splitlines()
print(
    "part 1",
    sum(
        int(line.split(":")[0][5:])
        * all(
            int(nc.split(" ")[1]) <= dict(red=12, green=13, blue=14)[nc.split(" ")[2]] for sample in line.split(":")[1].split(";") for nc in sample.split(",")
        )
        for line in lines
    ),
)
print(
    "part 2=",
    sum(
        max(int(nc.split(" ")[1]) * (nc.split(" ")[2] == "red") for sample in line.split(":")[1].split(";") for nc in sample.split(","))
        * max(int(nc.split(" ")[1]) * (nc.split(" ")[2] == "blue") for sample in line.split(":")[1].split(";") for nc in sample.split(","))
        * max(int(nc.split(" ")[1]) * (nc.split(" ")[2] == "green") for sample in line.split(":")[1].split(";") for nc in sample.split(","))
        for line in lines
    ),
)

# 1867
# 84538
