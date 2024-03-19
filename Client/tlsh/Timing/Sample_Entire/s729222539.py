from collections import deque
s = input()
g = deque()
p = deque()
for i in range(len(s)):
    if s[i] == "\\":
        g.append(i)
    elif s[i] == "/":
        a = 0
        if len(g) > 0:
            while True:
                if len(p) > 0 and p[-1][0] > g[-1]:
                    a += p[-1][1]
                    p.pop()
                else:
                    break
            a += i - g[-1]
            p.append([g[-1], a])
            g.pop()
for i in range(len(p)):
    p[i] = p[i][1]
if len(p) > 0:
    print(sum(p))
    print(len(p), end = " ")
    print(" ".join(map(str, p)))
else:
    print(0)
    print(0)
