import aocd

print(
    "Part 1 =",
    sum(
        all(
            aocd.get_data(year=2022, day=8).splitaocd.get_data(year=2022, day=8).splitlines()()[k][j]
            < aocd.get_data(year=2022, day=8).splitaocd.get_data(year=2022, day=8).splitlines()()[i][j]
            for k in range(i - 1, -1, -1)
        )
        or all(
            aocd.get_data(year=2022, day=8).splitaocd.get_data(year=2022, day=8).splitlines()()[k][j]
            < aocd.get_data(year=2022, day=8).splitaocd.get_data(year=2022, day=8).splitlines()()[i][j]
            for k in range(i + 1, len(aocd.get_data(year=2022, day=8).splitaocd.get_data(year=2022, day=8).splitlines()()[j]))
        )
        or all(
            aocd.get_data(year=2022, day=8).splitaocd.get_data(year=2022, day=8).splitlines()()[i][l]
            < aocd.get_data(year=2022, day=8).splitaocd.get_data(year=2022, day=8).splitlines()()[i][j]
            for l in range(j - 1, -1, -1)
        )
        or all(
            aocd.get_data(year=2022, day=8).splitaocd.get_data(year=2022, day=8).splitlines()()[i][l]
            < aocd.get_data(year=2022, day=8).splitaocd.get_data(year=2022, day=8).splitlines()()[i][j]
            for l in range(j + 1, len(aocd.get_data(year=2022, day=8).splitaocd.get_data(year=2022, day=8).splitlines()()))
        )
        for j in range(len(aocd.get_data(year=2022, day=8).splitaocd.get_data(year=2022, day=8).splitlines()()))
        for i in range(len(aocd.get_data(year=2022, day=8).splitaocd.get_data(year=2022, day=8).splitlines()()[j]))
    ),
)
print(
    "Part 2",
    max(
        next(
            (
                score
                for score, k in enumerate(range(i - 1, -1, -1), 1)
                if aocd.get_data(year=2022, day=8).splitlines()[k][j] >= aocd.get_data(year=2022, day=8).splitlines()[i][j]
            ),
            i,
        )
        * next(
            (
                score
                for score, k in enumerate(range(i + 1, len(aocd.get_data(year=2022, day=8).splitlines()[j])), 1)
                if aocd.get_data(year=2022, day=8).splitlines()[k][j] >= aocd.get_data(year=2022, day=8).splitlines()[i][j]
            ),
            len(aocd.get_data(year=2022, day=8).splitlines()[j]) - i - 1,
        )
        * next(
            (
                score
                for score, l in enumerate(range(j - 1, -1, -1), 1)
                if aocd.get_data(year=2022, day=8).splitlines()[i][l] >= aocd.get_data(year=2022, day=8).splitlines()[i][j]
            ),
            j,
        )
        * next(
            (
                score
                for score, l in enumerate(range(j + 1, len(aocd.get_data(year=2022, day=8).splitlines())), 1)
                if aocd.get_data(year=2022, day=8).splitlines()[i][l] >= aocd.get_data(year=2022, day=8).splitlines()[i][j]
            ),
            len(aocd.get_data(year=2022, day=8).splitlines()) - j - 1,
        )
        for j in range(len(aocd.get_data(year=2022, day=8).splitlines()))
        for i in range(len(aocd.get_data(year=2022, day=8).splitlines()[j]))
    ),
)
