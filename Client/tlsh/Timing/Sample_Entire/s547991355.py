S = input()
t = 0
H = [0]
for c in S:
    if c == '\\':
        t -= 1
        H.append(t)
    elif c == '_':
        H.append(t)
    elif c == '/':
        t += 1
        H.append(t)
L = [0 for _ in range(len(H))] 
for i in range(1, len(H)):
    L[i] = max(L[i-1], H[i])
R = [H[len(H)-1]]
for i in reversed(range(len(H)-1)):
    R.append(max(R[len(R)-1], H[i]))
R.reverse()
C = [min(L[i], R[i]) for i in range(len(H))]
D = 0
ans = []
for i in range(len(H)-1):
    D += (C[i] - H[i]) + (C[i+1] - H[i+1])
    if C[i+1] == H[i+1] and D != 0:
        ans.append(D // 2)
        D = 0
print(sum(ans))
ans.insert(0, len(ans))
print(' '.join(map(str, ans)))
