# coding: utf-8

def BubbleSort(A, n):
    for i in range(n-1):
        for j in range(n-1, i, -1):
            if int(A[j][1]) < int(A[j-1][1]):
                A[j], A[j-1] = A[j-1], A[j]
    return A


def SelectionSort(A, n):
    mini = 1
    for i in range(n):
        mini = i
        for j in range(i, n):
            if int(A[j][1]) < int(A[mini][1]):
                mini = j
        A[i], A[mini] = A[mini], A[i]
    return A

n = int(input())
A = input().split()

b_ans = BubbleSort(A[:], n)
s_ans = SelectionSort(A[:], n)

print(" ".join(b_ans))
print("Stable")
print(" ".join(s_ans))
if b_ans == s_ans:
    print("Stable")
else:
    print("Not stable")