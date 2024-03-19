import copy as cp

n = int(input())
A = [str(x) for x in input().split()]
AS = cp.copy(A)


def bubble(X):
    for i in range(n):
        X[i] = list(X[i])
        X[i][1] = int(X[i][1])

    for i in range(n):
        for j in range(n-1):
            if (X[j+1][1] < X[j][1]):
                X[j],X[j+1] = X[j+1],X[j]

    for i in range(n):
        X[i][1] = str(X[i][1])
        X[i] = "".join(X[i])
    return(X)


BA = bubble(A)



def minsort():

    for i in range(n):
        AS[i] = list(AS[i])
        AS[i][1] = int(AS[i][1])

    for i in range(n):
        minj = i
        for j in range(i,n):
            if (AS[j][1] < AS[minj][1]):
                minj = j

        if (minj != i):
            AS[i],AS[minj] = AS[minj],AS[i]

    for i in range(n):
        AS[i][1] = str(AS[i][1])
        AS[i] = "".join(AS[i])

    return(AS)

MA = minsort()


for k in range(n-1):
    print(str(BA[k])+" ",end = "")
print(str(BA[n-1]))
print("Stable")

for k in range(n-1):
    print(str(MA[k])+" ",end = "")
print(str(MA[n-1]))
if (BA == MA):
    print("Stable")
else :
    print("Not stable")

