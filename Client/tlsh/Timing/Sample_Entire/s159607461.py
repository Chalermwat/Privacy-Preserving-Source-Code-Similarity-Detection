from copy import deepcopy
def bubbleSort(C, N):
    for i in range(N):
        for j in range(N - 1, i, - 1):
            if C[j][1] < C[j - 1][1]:
                C[j], C[j - 1] = C[j - 1], C[j]

def selectionSort(C, N):
    for i in range(N):
        minj = i
        for j in range(i, N):
            if C[j][1] < C[minj][1]:
                minj = j
        C[i], C[minj] = C[minj], C[i]

N = int(input())
C = list(map(str, input().split()))
C1 = deepcopy(C)
C2 = deepcopy(C)
bubbleSort(C1, N)
selectionSort(C2, N)
O = [[] for _ in range(9)]
for i in range(N):
    j = int(C[i][1]) - 1
    O[j].append(C[i][0])
O1 = [[] for _ in range(9)]
for i in range(N):
    j = int(C1[i][1]) - 1
    O1[j].append(C1[i][0])
O2 = [[] for _ in range(9)]
for i in range(N):
    j = int(C2[i][1]) - 1
    O2[j].append(C2[i][0])
for i in range(N):
    if i == N - 1:
        print(C1[i])
    else:
        print(C1[i], end=' ')
if O == O1:
    print('Stable')
else:
    print('Not stable')
for i in range(N):
    if i == N - 1:
        print(C2[i])
    else:
        print(C2[i], end=' ')
if O == O2:
    print('Stable')
else:
    print('Not stable')
