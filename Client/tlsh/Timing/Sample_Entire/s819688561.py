import copy

def bubbleSort(cards):
    C = copy.copy(cards)
    for i in range(0, len(C)):
        for j in range(len(C) - 1, i, -1):
            if C[j][1] < C[j-1][1]:
                C[j-1], C[j] = C[j], C[j-1]
    return C

def selectionSort(cards):
    C = copy.copy(cards)
    for i in range(0, len(C)):
        min = i
        for j in range(i, len(C)):
            if C[j][1] < C[min][1]:
                min = j
        C[i], C[min] = C[min], C[i]
    return C


N = int(input())
cards = input().split()

CB = bubbleSort(cards)
CS = selectionSort(cards)
print(' '.join(CB))
print('Stable')
print(' '.join(CS))
if CB == CS:
    print('Stable')
else:
    print('Not stable')