import copy

n = int(input())
a = input().split()
b = copy.deepcopy(a)

for i in range(n):
    for j in range(n - 1 - i):
        if int(a[j][1]) > int(a[j + 1][1]):
            tmp = a[j]
            a[j] = a[j + 1]
            a[j + 1] = tmp

ra = " ".join(a)

print(ra)
print("Stable")

for i in range(n - 1):
    minj = i
    for j in range(i + 1, n):
        if int(b[j][1]) < int(b[minj][1]):
            minj = j
    if minj != i:
        tmp = b[i]
        b[i] = b[minj]
        b[minj] = tmp

rb = " ".join(b)
print(rb)

if ra == rb:
    print("Stable")
else:
    print("Not stable")