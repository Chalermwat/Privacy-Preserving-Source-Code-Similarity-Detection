def bubble(A, N):
    flag = True
    while flag:
        flag = False
        for j in range(N-1, 0, -1):
            if int(A[j][-1]) < int(A[j-1][-1]):
                A[j], A[j-1] = A[j-1], A[j]
                flag = True
    return A

def selection(A, N):
    for i in range(0, N):
        minj = i
        for j in range(i, N):
            if int(A[j][-1]) < int(A[minj][-1]):
                minj = j
        if i != minj:
            A[i], A[minj] = A[minj], A[i]
    return A

if __name__ == "__main__":
    N = int(input())
    A = input().split()

    A_bubble = bubble(A[:], N)
    print (*A_bubble)
    print ("Stable")

    A_selection = selection(A[:], N)
    print (*A_selection)
    if A_bubble == A_selection:
        print ("Stable")
    else:
        print ("Not stable")