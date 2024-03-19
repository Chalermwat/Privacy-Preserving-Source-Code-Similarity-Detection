# coding: utf-8

def bubbleSort(C, N):
    for i in xrange(N):
        for j in xrange(N-1, i, -1):
            if C[j-1][1] > C[j][1]:
                C[j], C[j-1] = C[j-1], C[j]
    return C

def selectionSort(C, N):
    for i in xrange(N):
        minj = i
        for j in xrange(i, N):
            if C[minj][1] > C[j][1]:
                minj = j
        C[i], C[minj] = C[minj], C[i]
    return C

def isStable(in_, out_, N):
    for i in xrange(N):
        for j in xrange(i + 1, N):
            for a in xrange(N):
                for b in xrange(a + 1, N):
                    if in_[i][1] == in_[j][1] and in_[i] == out_[b] and in_[j] == out_[a]:
                        return False
    return True

def main():
    N = input()
    cards = raw_input().split()
    bubble = bubbleSort(cards[:], N)
    selection = selectionSort(cards[:], N)
    print ' '.join(bubble)
    print 'Stable' if isStable(cards, bubble, N) else 'Not stable'
    print ' '.join(selection)
    print 'Stable' if isStable(cards, selection, N) else 'Not stable'



if __name__ == '__main__':
    main()