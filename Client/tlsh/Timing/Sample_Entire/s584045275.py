def bubble_sort(c, n):
    x = c[:]
    for i in range(n):
        for k in range(n-1, i, -1):
            if x[k][1] < x[k-1][1]:
                x[k], x[k-1] = x[k-1], x[k]
    return x

def selection_sort(c, n):
    x = c[:]
    for i in range(n):
        mink = i
        for k in range(i, n):
            if x[k][1] < x[mink][1]:
                mink = k
        x[i], x[mink] = x[mink], x[i]
    return x

n = int(input())
c = []
for i in list(input().split()):
    c.append((i[0], int(i[1]))) # tupleで渡す

b = bubble_sort(c, n)
print(" ".join(map(str, [i[0]+str(i[1]) for i in b])))
# bubble_sortは常に安定なソート
stable = True
print("Stable")

s = selection_sort(c, n)
print(" ".join(map(str, [i[0]+str(i[1]) for i in s])))
if b != s:
    stable = False
if stable:
    print("Stable")
else:
    print("Not stable")
