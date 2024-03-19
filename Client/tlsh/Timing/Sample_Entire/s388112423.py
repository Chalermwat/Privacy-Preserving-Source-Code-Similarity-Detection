def BubbleSort(C,N):
    for i in range(N):
        j = N-1
        while True:
            if j == 0:
                break
            a,b = list(C[j]),list(C[j-1])
            if a[1] < b[1]:
                tmp = C[j-1]
                C[j-1] = C[j]
                C[j] = tmp
            j -= 1
    return C

def SelectionSort(D,N):
    for i in range(N):
        minj = i
        for j in range(i,N):
            a,b = list(D[j]),list(D[minj])
            if a[1] < b[1]:
                minj = j
        tmp = D[i]
        D[i] = D[minj]
        D[minj] = tmp
    return D

n = int(input())
d = input().split()
d2 = list(d)
d = BubbleSort(d,n)
for i in range(len(d)-1):
    print(d[i],end = ' ')
print(d[-1])
print('Stable')
d2 = SelectionSort(d2,n)
for i in range(len(d2)-1):
    print(d2[i],end = ' ')
print(d2[-1])
if d2 == d:
    print('Stable')
else:
    print('Not stable')