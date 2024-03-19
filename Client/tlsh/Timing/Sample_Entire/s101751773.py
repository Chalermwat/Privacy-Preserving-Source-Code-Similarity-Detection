import copy
n = int(input())
A = list(map(str,input().split()))
B = copy.copy(A)

def BubbleSort(A,n):
    for i in range(n):
        for j in range(n-1,i,-1):
            if int(A[j][1:2])<int(A[j-1][1:2]):
                v = A[j]
                A[j] = A[j-1]
                A[j-1] = v
    return A

def SelectionSort(A,n):
    for i in range(n):
        minj = i
        for j in range(i,n):
            if int(A[j][1:2])<int(A[minj][1:2]):
                minj = j
        v = A[i]
        A[i] = A[minj]
        A[minj] = v
    return A

print(' '.join(BubbleSort(A,n)))
print('Stable')
print(' '.join(SelectionSort(B,n)))
if BubbleSort(A,n) == SelectionSort(B,n):
    print('Stable')
else:
    print('Not stable')
