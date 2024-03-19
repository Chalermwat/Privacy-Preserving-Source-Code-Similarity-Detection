from collections import namedtuple


def BubbleSort(C, N):
    for i in range(N):
        for j in range(N-1, i, -1):
            if C[j].value < C[j-1].value:
                C[j], C[j-1] = C[j-1], C[j]


def SelectionSort(C, N):
    for i in range(N):
        minj = i
        for j in range(i, N):
            if C[j].value < C[minj].value:
                minj = j
        C[i], C[minj] = C[minj], C[i]


Card = namedtuple('Card', 'mark value')
n = int(input())
a = [Card(i[0], int(i[1])) for i in input().split()]
b = a[:]

BubbleSort(a, n)
SelectionSort(b, n)

print(" ".join([i.mark + str(i.value) for i in a]))
print("Stable")
print(" ".join([i.mark + str(i.value) for i in b]))
print("Stable" if a == b else "Not stable")