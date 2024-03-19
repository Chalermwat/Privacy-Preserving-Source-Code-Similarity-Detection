from collections import deque


def marge_ponds(lx, area_of_pond):
    global ponds
    if ponds and ponds[-1][0] > lx:
        return marge_ponds(lx, area_of_pond + ponds.pop()[1])
    return area_of_pond


terrains = input().strip()
x, last_x, ponds = 0, deque(), deque()

for terrain in terrains:
    if terrain == '\\':
        last_x.append(x)
    elif terrain == '/':
        if last_x:
            lx = last_x.pop()
            ponds.append((lx, marge_ponds(lx, x - lx)))
    x += 1

print(sum(pond[1] for pond in ponds))
ponds.appendleft((0, len(ponds)))
print(' '.join(map(str, [pond[1] for pond in ponds])))