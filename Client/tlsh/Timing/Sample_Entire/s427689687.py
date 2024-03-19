def bblsrt(cards):
    cards1 = cards.copy()
    for i in range(len(cards1)):
        for j in range(len(cards1) - 1, i, -1):
            if cards1[j][1] < cards1[j - 1][1]:
                cards1[j], cards1[j - 1] = cards1[j - 1], cards1[j]
    return cards1


def slcsrt(cards):
    cards2 = cards.copy()
    for i in range(len(cards2)):
        minj = i
        for j in range(i, len(cards2)):
            if cards2[j][1] < cards2[minj][1]:
                minj = j
        cards2[i], cards2[minj] = cards2[minj], cards2[i]
    return cards2


n = int(input())
C = list(input().split())
print(' '.join(bblsrt(C)))
print('Stable')
print(' '.join(slcsrt(C)))
print('Stable' if slcsrt(C) == bblsrt(C) else 'Not stable')

