def BubbleTrump(C, N):
    i = 0
    while i < N:
        j = N - 1
        while j > i:
            if int(C[j][1]) < int(C[j-1][1]):
                c = C[j]
                C[j] = C[j - 1]
                C[j - 1] = c
            j -= 1
        i += 1
    return C

def SelectionTrump(C, N):
    i = 0
    while i < N:
        minj = i
        j = i
        while j < N:
            if int(C[j][1]) < int(C[minj][1]):
                minj = j
            j += 1
        if minj != i:
            c = C[i]
            C[i] = C[minj]
            C[minj] = c
        i += 1
    return C

n = int(input())
C = list(map(str, input().split(' ')))
ans = ''
Cb = BubbleTrump(C.copy(), n)
ans += ' '.join(map(str, Cb)) + '\nStable\n'
Cs = SelectionTrump(C.copy(), n)
q = 0
f = 1
while q < n:
    if Cb[q] != Cs[q]:
        f = 0
    q += 1
ans += ' '.join(map(str, Cs)) + '\n'
if f == 0:
    ans += 'Not stable'
else:
    ans += 'Stable'
print(ans)
