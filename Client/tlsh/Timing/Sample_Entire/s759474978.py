def bubbleSort(cards):
    for i, _ in enumerate(cards):
        for j in range(len(cards) -1, i, -1):
            if int(cards[j][1]) <  int(cards[j-1][1]):
                cards[j], cards[j - 1] = cards[j - 1], cards[j]
    return cards
    
def selectionSort(cards):
    for i in range(len(cards)):
        min_j = i
        for j in range(i, len(cards)):
            if int(cards[j][1]) < int(cards[min_j][1]):
                min_j = j
        cards[i], cards[min_j] = cards[min_j], cards[i]
    return cards
    
N = int(input())
A = input().split()

temp = A.copy()
bs = bubbleSort(temp)

temp = A.copy()
ss = selectionSort(temp)

print(' '.join(bs))
print('Stable')
print(' '.join(ss))
if [a[:1] for a in bs] == [a[:1] for a in ss]:
    print('Stable')
else:
    print('Not stable')
