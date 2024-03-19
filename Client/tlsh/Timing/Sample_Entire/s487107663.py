import copy


def BubbleSort(C, n):
    flag = 1
    while flag:
        flag = 0
        for i in range(n-1, 0, -1):
            if int(C[i][1]) < int(C[i - 1][1]):
                C[i], C[i-1] = C[i-1], C[i]
                flag = 1
    return C


def SelectionSort(C, n):
    for i in range(n-1):
        minj = i
        for j in range(i, n):
            if int(C[j][1]) < int(C[minj][1]):
                minj = j
        if minj != i:
            C[i], C[minj] = C[minj], C[i]
    return C


n = int(input())
C = list(input().split())
C2 = C.copy()

print(*BubbleSort(C, n), sep=' ')
print("Stable")
print(*SelectionSort(C2, n), sep=' ')
if C ==C2:
    print("Stable")
else:
    print("Not stable")

