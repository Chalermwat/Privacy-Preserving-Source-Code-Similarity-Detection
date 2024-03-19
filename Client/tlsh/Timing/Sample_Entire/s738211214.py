def BubbleSort(C, N):
    for i in xrange(0,N):
        for j in xrange(N-1,i,-1):
            if int(C[j][1]) < int(C[j-1][1]):
                tmp = C[j]
                C[j] = C[j-1]
                C[j-1] = tmp
    return C

def SelectionSort(C, N):
    for i in xrange(0,N):
        minj = i
        for j in xrange(i,N):
            if int(C[j][1]) < int(C[minj][1]):
                minj = j
        if minj != i:
            tmp = C[i]
            C[i] = C[minj]
            C[minj] = tmp
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
    N = int(raw_input())
    A = raw_input().split()
    BA = BubbleSort(A[:], N)
    SA = SelectionSort(A[:], N)
    print ' '.join(BA)
    if isStable(A, BA,N):
        print "Stable"
    else:
        print "Not stable"
    print ' '.join(SA)
    if isStable(A, SA,N):
        print "Stable"
    else:
        print "Not stable"

    return 0

if __name__ == "__main__":
    main()