import copy

n = int(input())
A = list (map(str, input().split()))
B = copy.copy(A) 

def BubbleSort_dict(A, n):
    flag = 1    
    while flag:
        flag = 0
        for i in reversed(range(n-1)):
            if int(A[i][1]) > int(A[i+1][1]):
                a = A[i]
                A[i] = A[i+1]
                A[i+1] = a
                flag = 1
    return A
    
def SelectionSort_dict(A, n):
    for i in range(n):
        minj = i
        for j in range(i, n):
            if int(A[j][1]) < int(A[minj][1]):
                minj = j
        if i != minj:
            a = A[i]
            A[i] = A[minj]
            A[minj] = a
    return A

A1 = BubbleSort_dict(A, n)
A2 = SelectionSort_dict(B, n)

print(' '.join(A1))
print("Stable")
print(' '.join(A2))
if A1 == A2:
    print("Stable")
else:
    print("Not stable")
