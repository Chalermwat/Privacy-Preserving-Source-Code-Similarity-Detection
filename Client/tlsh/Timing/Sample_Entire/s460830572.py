N = int(input())
C1 = input().split()
C2 = C1[:]

def bubbleSort(C, N):
    for i in range(N):
        for j in range(N-1, i, -1):
            if int(C[j][1]) < int(C[j-1][1]):
                tmp = C[j]
                C[j] = C[j-1]
                C[j-1] = tmp
        i += 1
    return C

def selectionSort(C, N):
    for i in range(N):
        minj = i
        for j in range(i, N):
            if int(C[j][1]) < int(C[minj][1]):
                minj = j
        if minj != i:
            tmp = C[minj]
            C[minj] = C[i]
            C[i] = tmp
        i += 1
    return C

bubbleSort_result = ' '.join(bubbleSort(C1, N))
selectionSort_result = ' '.join(selectionSort(C2, N))

print(bubbleSort_result)
print('Stable')
print(selectionSort_result)
if bubbleSort_result == selectionSort_result:
    print('Stable')
else:
    print('Not stable')