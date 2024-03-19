def bubble(d):
    for i in range(len(d) - 1):
        for j in range(len(d) - 1, i, -1):
            if int(d[j][1]) < int(d[j - 1][1]):
                d[j],d[j - 1] = d[j - 1],d[j]

def selection(d):
    for i in range(len(b)):
        min_j = i
        for j in range(i, len(d)):
            if int(d[j][1]) < int(d[min_j][1]):
                min_j = j
        if min_j != i:
            d[i],d[min_j] = d[min_j], d[i]

n = int(input())
a = list(map(str, input().split()))

b = a.copy()
c = a.copy()

bubble(b)
selection(c)

for d in [b, c]:
    print(" ".join(d))
    if d == b:
        print("Stable")
    else:
        print("Not stable")