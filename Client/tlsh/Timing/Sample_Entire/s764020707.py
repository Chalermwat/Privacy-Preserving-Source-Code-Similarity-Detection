#ALDS1_2-C Sort 1 - Stable Sort
def selectionSort(A,N):
    c=0
    for i in range(N):
        minj = i
        j=i
        while j<N:
            if(int(A[j][1])<int(A[minj][1])):
                minj = j
            j+=1
        if(i!=minj):
            A[i],A[minj]=A[minj],A[i]
            c+=1
    return c

def bubbleSort(A,N):
    c=0
    flag=1
    while flag:
        flag=0
        j=N-1
        while j>0:
            if(int(A[j][1])<int(A[j-1][1])):
                c+=1
                A[j],A[j-1]=A[j-1],A[j]
                flag=1
            j-=1
    return c

N=int(input())
A=input().split()
checkA=[""]*9
for i in range(N):
    checkA[int(A[i][1])-1]+=A[i][0]

B=[]+A
C=[]+A

bubbleSort(B,N)
checkB=[""]*9
for i in range(N):
    checkB[int(B[i][1])-1]+=B[i][0]
S=""
for i in range(N-1):
    S+=B[i]+" "
S+=str(B[-1])
print(S)
if(checkB==checkA):
    print("Stable")
else:
    print("Not stable")
    
selectionSort(C,N)
checkC=[""]*9
for i in range(N):
    checkC[int(C[i][1])-1]+=C[i][0]
S=""
for i in range(N-1):
    S+=C[i]+" "
S+=str(C[-1])
print(S)
if(checkC==checkA):
    print("Stable")
else:
    print("Not stable")