def bubble_sort(A, N):
    cnt = 0
    flag = True
    while flag:
        flag = False
        for j in range(N - 1, 0, -1):
            if int(A[j - 1][1]) > int(A[j][1]):
                A[j - 1], A[j] = A[j], A[j - 1]
                flag = True
                cnt += 1
    return A

def selection_sort(A, N):
    cnt = 0
    for i in range(N):
        minj = i
        for j in range(i, N):
            if int(A[j][1]) < int(A[minj][1]):
                minj = j
        A[i], A[minj] = A[minj], A[i]
        if i != minj:
            cnt += 1
    return A

N = int(input())
A = input().split()
order_A = [[] for _ in range(10)]
for s in A:
    order_A[int(s[1])].append(s)

order_bubble = [[] for _ in range(10)]
b_sorted = bubble_sort(A[:], N)
for s in b_sorted:
    order_bubble[int(s[1])].append(s)
print(*b_sorted)
print('Stable' if order_A == order_bubble else 'Not stable')

s_stability = [[] for _ in range(10)]
s_sorted = selection_sort(A[:], N)
for s in s_sorted:
    s_stability[int(s[1])].append(s)
print(*s_sorted)
print('Stable' if order_A == s_stability else 'Not stable')
