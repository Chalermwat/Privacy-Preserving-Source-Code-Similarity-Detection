N = input()
A = map(str,raw_input().split())
Ab = A[:]
As = A[:]

def BubbleSort(A,N):
    for i in range(N):
        flag = 0
        for i in range(1,N):
            j = N - i
            if A[j][1] < A[j-1][1]:
                v = A[j]
                A[j] = A[j-1]
                A[j-1] = v
                flag = 1

def SelectionSort(A,N):
    for i in range(N):
        minj = i
        for j in range(i,N):
            if A[j][1] < A[minj][1]:
                minj = j
        v = A[i]
        A[i] = A[minj]
        A[minj] = v

def Output(A):
    for i in range(N-1):
        print A[i],
    print A[-1]

def Stable(AA):
    n = []
    for i in range(N-1):
        if AA[i][1] == AA[i+1][1] and AA[i][1] not in n:
            n.append(AA[i][1])
    l = []
    m = []
    for item in n:
        for i in range(N):
            if AA[i][1] == item:
                l.append(AA[i])
            if A[i][1] == item:
                m.append(A[i])
    if l == m:
        msg = "Stable"
    else:
        msg = "Not stable"
    print msg

SelectionSort(As,N)
BubbleSort(Ab,N)

Output(Ab)
Stable(Ab)
Output(As)
Stable(As)