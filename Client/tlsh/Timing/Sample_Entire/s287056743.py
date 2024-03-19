n, card = int(input()), input().split()
card1, card2 = card[:], card[:]

for i in range(n-1):
    for j in range(n-1, i, -1):
        if int(card1[j][1]) < int(card1[j-1][1]):
            card1[j], card1[j-1] = card1[j-1], card1[j]
print(" ".join(card1))
print("Stable")

for i in range(n-1):
    for j in range(i+1, n):
        if j == i+1:
            idx = j
        elif int(card2[idx][1]) > int(card2[j][1]):
            idx = j
    if int(card2[i][1]) > int(card2[idx][1]):
        card2[i], card2[idx] = card2[idx], card2[i]
print(" ".join(card2))
if card1 == card2:
    print("Stable")
else:
    print("Not stable")

