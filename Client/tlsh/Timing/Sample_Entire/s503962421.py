n = int(input())
lst = input().split()
bub, sel = lst[:], lst[:]
def stable(sls):
    s, i = 1, n-1
    while s*i:
        if sls[i][1] == sls[i-1][1]:
            if lst.index(sls[i]) < lst.index(sls[i-1]) :
                s = 0
        i -= 1
    print('Stable' if s else 'Not stable')

for i in range(n):
    m = i
    for j in range(n-1,i,-1):
        if bub[j][1] < bub[j-1][1]:
            bub[j-1:j+1] = bub[j], bub[j-1]
    for k in range(i, n):
        if sel[k][1] < sel[m][1]:
            m = k
    if m != i:
        sel[i], sel[m] = sel[m], sel[i]

print(*bub)
stable(bub)
print(*sel)
stable(sel)