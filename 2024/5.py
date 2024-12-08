import aocd
import itertools


lines = aocd.get_data(year=2024, day=5).splitlines()

rules = {tuple(line.split("|")) for line in lines}

results = dict.fromkeys((1, 2), 0)

for line in lines:
    if "," in line:
        part = 1
        update = line.split(",")
        if any(pair in rules for pair in itertools.combinations(reversed(update), 2)):
            for i, j in itertools.combinations(range(len(update)), 2):
                if (update[j], update[i]) in rules:
                    part = 2
                    update[i], update[j] = update[j], update[i]
                    if i > len(update) // 2:  # we have past the middle, so futher swaps won't change the middle value
                        break

        results[part] += int(update[len(update) // 2])

print("\n".join(f"Part {part}: {result}" for part, result in results.items()))

# Part 1 5948
# Part 2 3062
