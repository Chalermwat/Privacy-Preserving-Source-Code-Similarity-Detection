g = input()
l = []
q = []
n = 0
for x in range(len(g)):
    if g[x] == '\\':
        if n:
            l.append(n)
            n = 0
            if q:
                q.append(-1)
        q.append(x)
    elif g[x] == '/':
        if q:
            while True:
                p = q.pop()
                if p == -1:
                    n += l.pop()
                else:
                    break
            n += x-p
    else:
        pass
if n:
    l.append(n)
for j in range(l.count(0)):
    l.remove(0)
print(sum(l))
print(len(l), *l)