import copy

n = int(input())

l = list(input().split())
C1 = []

for v in l:
    s = v[0]
    m = int(v[1])
    C1.append((s, m))

C2 = copy.deepcopy(C1)

for i in range(n):
    for j in range(n-1, i, -1):
        if C1[j][1] < C1[j-1][1]:
            C1[j], C1[j-1] = C1[j-1], C1[j]

for i in range(n):
    minj = i
    for j in range(i,n):
        if C2[j][1] < C2[minj][1]:
            minj = j
    C2[i], C2[minj] = C2[minj], C2[i]

result1 = [t[0]+str(t[1]) for  t in C1]
result2 = [t[0]+str(t[1]) for  t in C2]

print(" ".join(result1))
print("Stable")
print(" ".join(result2))
if result1 == result2:
    print("Stable")
else:
    print("Not stable")

