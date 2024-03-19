import copy

def BubbleSort(C, N):
    for i in range(0,N):
        for j in range(N-1,i,-1):
            if C[j][1:] < C[j-1][1:]:
                #  C[j] と C[j-1] を交換
                C[j] , C[j-1] = C[j-1] , C[j]
    ret = " ".join(C)
    print(ret)
    print("Stable")
    return ret

def SelectionSort(C, N):
    for i in range(0,N):
        minj = i
        for j in range(i,N):
            if C[j][1:] < C[minj][1:]:
                minj = j
        # C[i] と C[minj] を交換
        C[i] , C[minj] = C[minj] , C[i]
    ret = " ".join(C)
    print(ret)
    return ret

N = int(input())
C = input().split(" ")
ret_B = BubbleSort(copy.deepcopy(C),N)
ret_S = SelectionSort(copy.deepcopy(C),N)
if ret_B == ret_S:
    print("Stable")
else:
    print("Not stable")

