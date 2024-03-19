class card:
    def __init__(self, types, value):
        self.types = types
        self.value = value

def bubbleSort(A, N):
    for i in range(0, N):
        for j in range(N - 1, i, -1):
            if A[j].value < A[j - 1].value:
                exchange(A, j - 1, j)
    printCards(A)
    print "Stable"

def selectionSort(A, N):
    origin = A[:]
    for i in range(0, N):
        minj = i
        for j in range(i, N):
            if A[j].value < A[minj].value:
                minj = j
        if i != minj:
            exchange(A, i, minj)
    printCards(A)
    if checkStable(origin, A, N):
        print "Stable"
    else:
        print "Not stable"

def exchange(array, i, j):
    tmp = array[i]
    array[i] = array[j]
    array[j] = tmp

def printCards(cards):
    print " ".join(t.types + str(t.value) for t in cards)

def checkStable(origin, sorted, N):
    for i in range(0, N - 1):
        if sorted[i].value == sorted[i + 1].value:
            if origin.index(sorted[i]) > origin.index(sorted[i + 1]):
                return False
    return True

if __name__ == "__main__":
    N = input()
    A = [card(c[0], int(c[1])) for c in raw_input().split()]
    bubbleSort(A[:], N)
    selectionSort(A[:], N)