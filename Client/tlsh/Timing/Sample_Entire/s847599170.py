def bubbleSort(A,N):
    for i in range(0,N):
        for j in range(N-1,i,-1):
            if A[j][1] < A[j-1][1]:
                v = A[j]
                A[j] = A[j-1]
                A[j-1] = v
    return A

def selectionSort(A,N):
    for i in range(0,N):
        minj = i
        for j in range(i,N):
            if A[j][1] < A[minj][1]:
                minj = j
        v = A[i]
        A[i] = A[minj]
        A[minj] = v
    return A

if __name__ == '__main__':
    N = (int)(input())
    A1 = [[x[0],(int)(x[1])] for x in [list(x) for x in input().split()] ]
    A2 = A1.copy()

    resultA1 = bubbleSort(A1,N)
    resultA2 = selectionSort(A2,N)

    outputA1 = ' '.join( [x[0]+(str)(x[1]) for x in resultA1])
    outputA2 = ' '.join( [x[0]+(str)(x[1]) for x in resultA2])

    print(outputA1)
    print("Stable")
    print(outputA2)
    if outputA1 == outputA2 :
        print("Stable")
    else:
        print("Not stable")