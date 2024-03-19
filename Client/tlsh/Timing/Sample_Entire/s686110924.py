def bubbleSort(A,N):
    for i in range(N):
        for j in range(N-1,i,-1):
            if A[j][1:] < A[j-1][1:] :
                A[j] , A[j-1] = A[j-1] , A[j]
    return A

def selectionSort(A,N):
    for i in range(N):
        minj = i
        for j in range(i,N):
            if A[j][1:] < A[minj][1:]:
                minj = j
        A[i] , A[minj] = A[minj] , A[i]
    return A

N =int(input())
cards = input().split()
bub , sel =cards[:] , cards[:]
X = bubbleSort(bub , N)
print(*X)
print("Stable")
Y = selectionSort(sel,N)
print(*Y)
print("Stable" if X == Y else "Not stable")