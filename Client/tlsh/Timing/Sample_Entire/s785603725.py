# coding: utf-8
# Here your code !

def BubbleSort(A, N):
    count = 0
    flag = 1
    while flag:
        flag = 0
        for i in range(1, N):
            if int(A[N - i][1]) < int(A[N - i - 1][1]):
                A[N - i], A[N - i - 1] = A[N - i - 1], A[N - i]
                flag = 1
    return A


def SelectionSort(C, N):
    for i in range(N):
        minj = i

        for j in range(i, N):
            if int(C[j][1]) < int(C[minj][1]):
                minj = j
        if i != minj:
            C[i], C[minj] = C[minj], C[i]
    return C


if __name__ == '__main__':
    n = int(input())
    data = input().split()
    selection = data[:]
    data = BubbleSort(data, n)
#    print(" ".join(BubbleSort(data, n)))
    print(" ".join(data))
    print("Stable")
    selection = SelectionSort(selection, n)
    print(" ".join(selection))
    if data == selection:
        print("Stable")
    else:
        print("Not stable")