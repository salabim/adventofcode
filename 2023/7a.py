import aocd
from collections import Counter

lines = aocd.get_data(year=2023, day=7).splitlines()

for part in (1, 2):
    if part == 1:
        order = "23456789TJQKA"
    else:
        order = "J23456789TQKA"

    def type_1(hand):
        counter = Counter(hand).values()
        sorted_counter = tuple(sorted(counter))
        return {(5,): 6, (1, 4): 5, (2, 3): 4, (1, 1, 3): 3, (1, 2, 2): 2, (1, 1, 1, 2): 1, (1, 1, 1, 1, 1): 0}[sorted_counter]

    def type_(hand):
        if part == 1 or len(set(hand)) == 1:
            return type_1(hand)
        else:
            return max(type_1(hand.replace("J", v)) for v in set(hand) - {"J"})

    score_bids = []
    for line in lines:
        hand, bid = line.split()
        score_bids.append(((type_(hand), tuple(order.index(c) for c in hand)), bid))

    sorted_score_bids = sorted(score_bids, key=lambda score_bid: score_bid[0])
    print(f"part {part}={sum(i *int(score_bid[1]) for i, score_bid in enumerate(sorted_score_bids, 1))}")
