# -*- coding:utf-8 -*-

def Selection_Sort(A,n):
    for i in range(n):
        mini = i
        for j in range(i,n): #i以上の要素において最小のAをminiに格納
            if int(A[j][1]) < int(A[mini][1]):
                mini = j
        if A[i] != A[mini]:
            A[i], A[mini] = A[mini], A[i]
    return A
    
def Bubble_Sort(A, n):
    for i in range(n):
        for j in range(n-1,i,-1):
            if int(A[j][1]) < int(A[j-1][1]):
                A[j], A[j-1] = A[j-1], A[j]
    return A
    
n = int(input())
A = input().strip().split()

B = A[:]
A = Bubble_Sort(A,n)
print (' '.join(A))
print ("Stable")
B =Selection_Sort(B,n)
print (' '.join(B))

if A == B:
    print ("Stable")
else:
    print ("Not stable")