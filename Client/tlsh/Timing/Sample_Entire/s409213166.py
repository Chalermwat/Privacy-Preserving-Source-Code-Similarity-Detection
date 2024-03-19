def compare(s1, s2):
    if s1[1] > s2[1]:
        return 1
    elif s1[1] < s2[1]:
        return -1

    return 0

def bubbleSort(N, A):
    flag = True
    while flag:
        flag = False
        for i in xrange(N-1, 0, -1):
            if compare(A[i-1], A[i]) > 0:
                A[i-1], A[i] = A[i], A[i-1]
                flag = True

def selectSort(N, A):
    for i in xrange(N):
        minj = i
        for j in xrange(i, N):
            if compare(A[j], A[minj]) < 0:
                minj = j
        if minj != i:
            A[i], A[minj] = A[minj], A[i]

N = int(raw_input())
A = raw_input().split()
B = list(A)
bubbleSort(N, A)
print ' '.join(A)
print 'Stable'
selectSort(N, B)
print ' '.join(B)
if A == B:
    print 'Stable'
else:
    print 'Not stable'