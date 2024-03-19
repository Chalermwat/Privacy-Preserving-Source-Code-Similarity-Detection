class Card:
    def __init__(self, inf):
        self.num = int(inf[1])
        self.inf = inf

n, card = int(input()), [Card(i) for i in input().split()]
card1 = card[:]

for i in range(n-1):
    for j in range(n-1, i, -1):
        if card[j].num < card[j-1].num:
             card[j], card[j-1] = card[j-1], card[j]
print(" ".join([i.inf for i in card]))
print("Stable")

for i in range(n-1):
    for j in range(i+1, n):
        if j == i+1:
            idx = j
        elif card1[idx].num > card1[j].num:
            idx = j
    if card1[i].num > card1[idx].num:
        card1[i], card1[idx] = card1[idx], card1[i]
print(" ".join([i.inf for i in card1]))
if card == card1:
    print("Stable")
else:
    print("Not stable")

