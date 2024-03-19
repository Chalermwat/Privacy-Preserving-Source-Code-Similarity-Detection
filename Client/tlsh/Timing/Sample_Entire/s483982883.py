n, *aa = open(0).read().split()

def bubble(aa):
    aa = list(map(list, aa))
    n = len(aa)
    for i in range(n):
        for j in range(n-1, i, -1):
            if aa[j-1][1] > aa[j][1]:
                aa[j-1], aa[j] = aa[j], aa[j-1]
    aa = list(map(lambda x: ''.join(x), aa))
    return aa

def selection(aa):
    aa = list(map(list, aa))
    n = len(aa)
    for i in range(n):
        mini = i
        for j in range(i, n):
            if aa[j][1] < aa[mini][1]:
                mini = j
        aa[mini], aa[i] = aa[i], aa[mini]
    aa = list(map(lambda x: ''.join(x), aa))
    return aa

bres = bubble(aa)
sres = selection(aa)

print(*bres)
print('Stable')
print(*sres)
if bres == sres:
    print('Stable')
else:
    print('Not stable')
