#coding:utf-8
#1_2_C

def BubbleSort(cards, n):
    for i in range(n):
        for j in range(n-1, i, -1):
            if cards[j][1] < cards[j-1][1]:
                cards[j], cards[j-1] = cards[j-1], cards[j]
    return cards

def SelectionSort(cards, n):
    for i in range(n):
        minj = i
        for j in range(i, n):
            if cards[minj][1] > cards[j][1]:
                minj = j
        cards[i], cards[minj] = cards[minj], cards[i]
    return cards

n = int(input())
cards = input().split()
copy = list(cards)

print(*BubbleSort(cards, n))
print("Stable")
print(*SelectionSort(copy, n))
print("Stable" if cards == copy else "Not stable")