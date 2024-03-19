#バブルソート
def BubbleSort(C,N):
    for i in range (0,N,1):
        for j in range(N-1,i,-1):
            if int(C[j][1:2]) < int(C[j-1][1:2]):
                tmp = C[j]
                C[j] = C[j-1]
                C[j-1] = tmp
    print(' '.join(C))

    
                
#選択ソート
def SelectionSort(C,N):
    for i in range(0,N,1):
        minj = i
        for j in range(i,N,1):
            if int(C[j][1:2]) < int(C[minj][1:2]):
                minj = j
        tmp = C[i]
        C[i] = C[minj]
        C[minj] = tmp
    print(' '.join(C))



N = int(input())
A = list(input().split())
Bubble_A = A.copy()
Selection_A = A.copy()

BubbleSort(Bubble_A,N)
print("Stable")
SelectionSort(Selection_A,N)
flag = True
for Bubble,Selection in zip(Bubble_A,Selection_A):
    if Bubble != Selection:
        flag = False
if flag :
    print("Stable")
else:
    print("Not stable")

