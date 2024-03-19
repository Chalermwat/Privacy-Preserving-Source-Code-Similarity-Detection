N = int(input())
A = input().split()

def bubble_sort(A):
    for i in range(0, N):
        for j in range(i+1, N)[::-1]:
            if int(A[j][1]) < int(A[j-1][1]):
                A[j], A[j-1] = A[j-1], A[j]
    return A

def selection_sort(A):
    for i in range(0, N):
        min_i = i
        for j in range(i+1, N):
            if int(A[j][1]) < int(A[min_i][1]):
                min_i = j
        A[i], A[min_i] = A[min_i], A[i]
    return A

BA = bubble_sort(A[:])
SA = selection_sort(A[:])

print(' '.join([str(i) for i in BA]))
print('Stable')
print(' '.join([str(i) for i in SA]))
print('Stable' if SA == BA else 'Not stable')