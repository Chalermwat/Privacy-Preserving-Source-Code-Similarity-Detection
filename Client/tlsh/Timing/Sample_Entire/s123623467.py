from copy import copy

n = int(input())
cards = [(s[0],int(s[1])) for s in input().split()]

cards_1 = copy(cards)
cards_2 = copy(cards)

need_to_sort = True
while need_to_sort:
    need_to_sort = False
    for index in range(len(cards_1) - 1, 0, -1):
        if cards_1[index][1] < cards_1[index-1][1]:
            cards_1[index], cards_1[index-1] = cards_1[index-1], cards_1[index]
            need_to_sort = True

print(" ".join([s[0]+ str(s[1]) for s in cards_1]))
print("Stable")

for idx1 in range(len(cards_2)):
    mins = idx1
    for idx2 in range(idx1, len(cards_2)):
        if cards_2[idx2][1] < cards_2[mins][1]:
            mins = idx2
    
    if mins != idx1:
        cards_2[idx1], cards_2[mins] = cards_2[mins], cards_2[idx1]

print(" ".join([s[0]+ str(s[1]) for s in cards_2]))

is_stable = True
for index in range(n):
    if cards_1[index] != cards_2[index]:
        is_stable = False
        break

print("Stable" if is_stable else "Not stable")
