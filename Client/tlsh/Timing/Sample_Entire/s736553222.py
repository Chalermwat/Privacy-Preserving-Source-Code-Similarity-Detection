from __future__ import print_function
from collections import deque

q = deque()
n = 0
d = 0
r = {}
mind = 0
maxd = 0

for x, c in enumerate(raw_input()):
    if c == "\\":
        d += 1
        maxd = max(maxd, d)
        q.append(x)
        n += 1
    elif c == "/":
        d -= 1
        mind = min(mind, d)
        if n == 0:
            continue
        x0 = q.pop()
        n -= 1
        s = x - x0
        if (d + 1) in r:
            while r[d + 1] and r[d + 1][-1][0] > x0:
                s += r[d + 1].pop()[1]
        if d not in r:
            r[d] = deque()
        r[d].append((x, s))

a = 0
k = 0
l = []
for d in xrange(mind, maxd):
    if d in r:
        for x, s in r[d]:
            a += s
            k += 1
            l.append((x, s))
l.sort()

print(a)
print(k, *(s for x, s in l))