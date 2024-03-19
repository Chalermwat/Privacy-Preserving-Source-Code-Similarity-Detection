from collections import deque

T = input()
A = deque()
d = 0
s = 0
for i, token in enumerate(T):
    if token == "\\":
        s += d + 0.5
        if not d:
            l = i
        d += 1
    elif token == "/":
        if not d:
            continue
        d -= 1
        s += d + 0.5
        if not d:
            A.append((l, s))
            s = 0
    else:
        s += d
B = deque()
d = 0
s = 0
for i in range(len(T) - 1, -1, -1):
    token = T[i]
    if token == "/":
        s += d + 0.5
        d += 1
    elif token == "\\":
        if not d:
            continue
        d -= 1
        s += d + 0.5
        if not d:
            B.appendleft((i, s))
            s = 0
    else:
        s += d
S = set(A) | set(B)
S = list(S)
S.sort()
S = [round(s[1]) for s in S]
print(sum(S))
print(len(S), *S)

