import aocd

from collections import defaultdict
order ='23456789TJQKA'
lines = """\
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483""".splitlines()
lines = aocd.get_data(year=2023, day=7).splitlines()
def type_(hand):
    s=defaultdict(int)
    for c in hand:
        s[c]+=1
    s=sorted(s.values())
    if s == [5]:
        return 6
    if s==[1,4]:
        return 5
    if s==[2,3]:
        return 4
    if s==[1,1,3]:
        return 3
    if s==[1,2,2]:
        return 2
    if s==[1,1,1,2]:
        return 1
    return 0

 
def strength(hand):
    result=0
    for c in hand:
        result=result*100+order.index(c)
    return result

#sorted = sorted(lines, key)
score_bid=[]
for line in lines:
    hand, bid = line.split()
    t=type_(hand)
    s=strength(hand)
    score = t * 100000000000 + s
    score_bid.append((score,bid))
    

sorted_score_bids=sorted(score_bid, key=lambda score_bid:score_bid[0])
result=0
for i,score_bid in enumerate( sorted_score_bids,1):
    result+=i*int(score_bid[1])
print('part 1=',result)

order ='J23456789TQKA'
def type_(hand):
    s=defaultdict(int)
    for c in hand:
        s[c]+=1
    s=sorted(s.values())
    if s == [5]:
        return 6
    if s==[1,4]:
        return 5
    if s==[2,3]:
        return 4
    if s==[1,1,3]:
        return 3
    if s==[1,2,2]:
        return 2
    if s==[1,1,1,2]:
        return 1
    return 0

def type_(hand):
    result=max(type_(hand.replace('J',v)) for v in set(hand))
    return result
    
def strength(hand):
    result=0
    for c in hand:
        result=result*100+order.index(c)
    return result

#sorted = sorted(lines, key)
score_bid=[]
for line in lines:
    hand, bid = line.split()
    t=max_type(hand)
    s=strength(hand)
    score = t * 100000000000 + s
    score_bid.append((score,bid))
    
sorted_score_bids=sorted(score_bid, key=lambda score_bid:score_bid[0])
result=0
for i,score_bid in enumerate( sorted_score_bids,1):
    result+=i*int(score_bid[1])
print('part 2=',result)

#part 1= 249748283
#part 2= 248029057
