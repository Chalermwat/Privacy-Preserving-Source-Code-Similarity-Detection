import copy

def bubbleSort(A):
    flag = 1
    while flag:
        flag = 0
        for j in range(len(A)-1,0,-1):#こういう書き方なんや……逆順処理
            if int(A[j][1]) < int(A[j-1][1]):
                A[j],A[j-1] = A[j-1],A[j]
                flag += 1
    return A

def selectionSort(A):
    for i in range(len(A)):
        minj = i
        for j in range(i,len(A)):
            if int(A[j][1]) < int(A[minj][1]):
                minj = j
        if i != minj:
            A[i],A[minj] = A[minj],A[i]
    return A

N = int(input())
lst1 = list(input().split())
lst2 =  copy.copy(lst1)
print(" ".join(bubbleSort(lst1)))
print("Stable")
print(" ".join(selectionSort(lst2)))
if lst1 == lst2:
    print("Stable")
else:
    print("Not stable")
