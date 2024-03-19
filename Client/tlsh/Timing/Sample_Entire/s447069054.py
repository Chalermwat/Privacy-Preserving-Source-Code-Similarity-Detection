import copy

def bubble_sort(C):
    for i in range(len(C)):
        for j in range(len(C)-1, i, -1):
            if int(C[j][1]) < int(C[j-1][1]):
                C[j], C[j-1] = C[j-1], C[j]
    return C

def selection_sort(C):
    for i in range(len(C)):
        minj = i
        for j in range(i, len(C)):
            if int(C[minj][1]) > int(C[j][1]):
                minj = j
        C[minj], C[i], = C[i], C[minj]
    return C

if __name__ == '__main__':
    n = int(input())
    B = input().split()
    C_bubble = bubble_sort(copy.deepcopy(B))
    print(*C_bubble)
    print('Stable')
    C_selection = selection_sort(copy.deepcopy(B))
    print(*C_selection)
    if C_bubble == C_selection:
        print('Stable')
    else:
        print('Not stable')

