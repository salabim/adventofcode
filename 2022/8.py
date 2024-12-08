import aocd


data = aocd.get_data(year=2022, day=8)

lines = data.splitlines()


total = 0
for j in range(len(lines)):
    for i in range(len(lines[j])):
        h = lines[i][j]
        visible_left = all(lines[k][j] < h for k in range(i - 1, -1, -1))
        visible_right = all(lines[k][j] < h for k in range(i + 1, len(lines[j])))
        visible_up = all(lines[i][l] < h for l in range(j - 1, -1, -1))
        visible_down = all(lines[i][l] < h for l in range(j + 1, len(lines)))
        total += any((visible_left, visible_right, visible_up, visible_down))

print(f"Part 1 = {total}")

maxscore = 0
for j in range(len(lines)):
    for i in range(len(lines[j])):
        h = lines[i][j]
        score_up = next((score for score, k in enumerate(range(i - 1, -1, -1), 1) if lines[k][j] >= h), i)
        score_down = next((score for score, k in enumerate(range(i + 1, len(lines[j])), 1) if lines[k][j] >= h), len(lines[j]) - i - 1)
        score_right = next((score for score, l in enumerate(range(j - 1, -1, -1), 1) if lines[i][l] >= h), j)
        score_left = next((score for score, l in enumerate(range(j + 1, len(lines)), 1) if lines[i][l] >= h), len(lines) - j - 1)
        maxscore = max(maxscore, score_left * score_right * score_up * score_down)


print(f"Part 2 = {maxscore}")
