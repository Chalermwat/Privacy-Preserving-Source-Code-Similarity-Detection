n = int(input())
s = input()
a = s.split()

def value(a, i):
    return int(a[i][-1])

def isstable(s, a, n):
    for i in range(n - 1):
        if value(a, i) == value(a, i + 1):
            v1 = s.index(a[i])
            v2 = s.index(a[i + 1])
            if v1 > v2:
                return "Not stable"
    return "Stable"

for i in range(n - 1):
    for j in range(i + 1, n)[::-1]:
        if value(a, j) < value(a, j - 1):
            a[j], a[j - 1] = a[j - 1], a[j]
print(" ".join(a))
print(isstable(s.split(), a, n))

a = s.split()

for i in range(n - 1):
    minj = i
    for j in range(i + 1, n):
        if value(a, j) < value(a, minj):
            minj = j
    a[i], a[minj] = a[minj], a[i]
print(" ".join(a))
print(isstable(s.split(), a, n))
