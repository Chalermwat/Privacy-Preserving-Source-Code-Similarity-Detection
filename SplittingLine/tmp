N = int(input())
T = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
mod = 10 ** 9 + 7
mountain = [T[0]]
for i in range(1, N):
    if T[i] > T[i - 1]:
        mountain.append(T[i])
    else:
        mountain.append(-T[i])
ans = 1
if N == 1:
    if T[0] != A[0]:
        print(0)
        exit()
for i in range(N - 1, -1, -1):
    if i == N - 1:
        if (A[i] > mountain[i]) & (mountain[i] > 0):
            ans = 0
            break
        mountain[i] = A[i]
    elif mountain[i] <= 0:
        if A[i] > A[i + 1]:
            if - mountain[i] >= A[i]:            
                mountain[i] = A[i]
            else:
                ans = 0
                break
        else:
            mountain[i] = -min(A[i], -mountain[i])
    else:
        if A[i] >= mountain[i]:
            continue
        else:
            ans = 0
            break
    if mountain[i] < 0:
        ans = (- ans * mountain[i]) % mod
print(ans)                