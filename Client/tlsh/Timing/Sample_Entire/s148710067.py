from collections import deque
from sys import stdin

A = input()
d = deque([])
e = deque([])
area = 0
areas = deque([])

for a,b in enumerate(A):
    if b == "\\":
        d.append(a)
    elif b == "/" and d != deque([]):
        x = d.pop()
        area += a - x
        areas.append([x,a,a-x])

menseki = 0
kaitou = []
prev_start,prev_end = 20000,0
while len(areas) > 0:
    temp = areas.pop()
    if temp[0] > prev_start and temp[1] < prev_end:
        menseki += temp[2]
    else:
        if menseki != 0:
            kaitou.append(menseki)
        menseki = temp[2]
        prev_start, prev_end = temp[0],temp[1]
    if len(areas) == 0:
        kaitou.append(menseki)

print(sum(kaitou))
kaitou.append(len(kaitou))
print(*kaitou[::-1])

