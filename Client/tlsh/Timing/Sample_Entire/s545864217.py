def print_list(l):
    for i, n in enumerate(l):
        if i == N - 1:
            print(l[i])
        else:
            print(l[i], end=' ')

N = int(input())
A = input().split()
B = list(A)
for i in range(N):
    for j in range(N-1, i, -1):
        if int(A[j][1]) < int(A[j-1][1]):
            w = A[j]; A[j] = A[j-1]; A[j-1] = w
print_list(A)
print('Stable')

for i in range(N):
    min_j = i
    for j in range(i, N):
        if int(B[j][1]) < int(B[min_j][1]):
            min_j = j
    w = B[i]; B[i] = B[min_j]; B[min_j] = w
print_list(B)
if A == B:
    print('Stable')
else:
    print('Not stable')

