def SelectionSort(A, N):
    for i in range(N):
        minj = i
        for j in range(i, N):
            if A[j][1:] < A[minj][1:]:
                minj = j
        #if i != minj:
            #times += 1
        A[i], A[minj] = A[minj], A[i]
        #print(*A)
    return A

def BubbleSort(A, N):
    for i in range(N):
        for j in reversed(range(i+1, N)):
            if A[j][1:] < A[j-1][1:]:
                A[j], A[j-1] = A[j-1], A[j]

    return A

N= int(input())
A = [str(x) for x in input().split()]
B = [0 for i in range(N)]
for i in range(N):
    B[i] = A[i]
bubble = BubbleSort(A, N)
selection = SelectionSort(B, N)
#print(A, B)
#print(*A)
print(*bubble)
print('Stable')
print(*selection)
if bubble == selection:
    print('Stable')
else:
    print('Not stable')