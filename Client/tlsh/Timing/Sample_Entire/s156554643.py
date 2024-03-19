# coding: utf-8
# Stable Sort 2018/3/12

class Card(object):
    def __init__(self, card):
        self.value = int(card[1])
        self.card = card

    def __repr__(self):
        return self.card


def BubbleSort(C, N):
    for i in range(N):
        for j in reversed(range(i+1, N)):
            if C[j].value < C[j-1].value:
                C[j], C[j-1] = C[j-1], C[j]
    return C


def SelectionSort(C, N):
    for i in range(N):
        minj = i
        for j in range(i, N):
            if C[j].value < C[minj].value:
                minj = j
        C[i], C[minj] = C[minj], C[i]
    return C


def isStable(inl, out):
    n = len(inl)
    for i in range(n):
        for j in range(i+1, n):
            for a in range(n):
                for b in range(a+1, n):
                    if inl[i].value == inl[j].value and inl[i] == out[b] and inl[j] == out[a]:
                        return False
    return True


def print_stable(inl, out):
    if isStable(inl, out):
        print "Stable"
    else:
        print "Not stable"


if __name__ == "__main__":
    N = int(raw_input())
    inputs = raw_input().split()
    C = []
    for i in inputs:
        C.append(Card(i))
    Cb = BubbleSort(list(C), N)
    print " ".join([i.card for i in Cb])
    print_stable(C, Cb)
    Cs = SelectionSort(list(C), N)
    print " ".join([i.card for i in Cs])
    print_stable(C, Cs)

