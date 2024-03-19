import sys
from collections import deque


def input(): return sys.stdin.readline().strip()


L = []
T = deque()
A = deque()
left = 0
total = 0

s = input()
for i, c in enumerate(s):
    if c == '\\':
        T.append(i)
    elif c == '/':
        if len(T) == 0:
            continue
        if i == 0:
            continue
        left = T.pop()
        area = (left, i - left)
        A.append(area)
        total += area[1]

while len(A) > 0:
    if len(A) == 1:
        a1 = A.pop()
        L.append(str(a1[1]))
        break
    a1 = A.pop()
    a2 = A.pop()
    if a1[0] < a2[0]:
        A.append((a1[0], a1[1] + a2[1]))
    else:
        L.append(str(a1[1]))
        A.append(a2)

print(total)
L.reverse()
print((str(len(L)) + ' ' + ' '.join(L)).strip())

