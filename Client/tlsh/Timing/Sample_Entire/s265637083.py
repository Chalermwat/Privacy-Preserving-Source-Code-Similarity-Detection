def marge_ponds(lx, area_of_pond):
    global ponds
    if ponds:
        lp = ponds.pop()
        if lp[0] > lx:
            return marge_ponds(lx, area_of_pond + lp[1])
        else:
            ponds.append(lp)
    return area_of_pond


terrains = input().strip()
x, last_x, ponds = 0, [], []

for terrain in terrains:
    if terrain == '\\':
        last_x.append(x)
    elif terrain == '/':
        if last_x:
            lx = last_x.pop()
            area_of_pond = marge_ponds(lx, x - lx)
            ponds.append((lx, area_of_pond))
    x += 1

print(sum(pond[1] for pond in ponds))
ponds.insert(0, (0, len(ponds)))
print(' '.join(map(str, [pond[1] for pond in ponds])))