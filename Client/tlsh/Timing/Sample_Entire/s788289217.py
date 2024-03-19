from collections import namedtuple
C = namedtuple("C", "m v")


def bubble_sort(A0):
    A = A0.copy()
    for i in range(n - 1):
        for j in range(n - 1, i, -1):
            if A[j].v < A[j - 1].v:
                A[j], A[j - 1] = A[j - 1], A[j]
    return A, True


def selection_sort(A0):
    A = A0.copy()
    for i in range(n - 1):
        k = i
        for j in range(i + 1, n):
            if A[k].v > A[j].v:
                k = j
        if k != i:
            A[k], A[i] = A[i], A[k]
    return A


lst = ["Not stable", "Stable"]
n = int(input())
A = [C(x[0], x[1]) for x in input().split()]

B, j = bubble_sort(A)
print(*[(B[i].m + B[i].v) for i in range(n)])
print(lst[j])

S = selection_sort(A)
print(*[(S[i].m + S[i].v) for i in range(n)])
print(lst[B == S])

