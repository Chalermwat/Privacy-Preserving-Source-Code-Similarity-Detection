def bubblesort(N, A):
    C, flag = [] + A,  True
    while flag:
        flag = False
        for j in range(N-1, 0, -1):
            if int(C[j][1]) < int(C[j-1][1]):
                C[j], C[j-1] = C[j- 1], C[j]
                flag = True
    return C

def selectionSort(N, A):
    C = [] + A
    for i in range(N):
        minj = i
        for j in range(i,N):
            if int(C[j][1]) < int(C[minj][1]):
                minj = j
        C[i], C[minj] = C[minj], C[i]
    return C

N, A= int(input()), input().split()
Ab = bubblesort(N, A)
print(*Ab)
print('Stable')
As = selectionSort(N, A)
print(*As)
if Ab != As:
    print('Not stable')
else:
    print('Stable')