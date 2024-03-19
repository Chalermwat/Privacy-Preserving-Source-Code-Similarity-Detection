class card:

    def __init__(self,cv):
        c = cv[0:1]
        v = int(cv[1:2])
        self.c = c
        self.v = v
    

    def self_str(self):
        q = str(str(self.c) + str(self.v))
        return q


n = int(input())
a = list(map(card, input().split()))


b = a[:]
c = a[:]

for i in range(n):
    for j in range(n-1, i, -1):
        if b[j].v < b[j-1].v:
            b[j], b[j-1] = b[j-1],b[j]

print(" ".join(x.self_str() for x in b))

coua = ["" for i in range(10)]
coub = ["" for i in range(10)]
conb = ""
for i in range(n):
    for j in range(n):
        if i != j:
            if a[i].v == a[j].v:
                coua[a[i].v] += a[i].c
            if b[i].v == b[j].v:
                coub[b[i].v] += b[i].c
if coua == coub:
     conb = "Stable"
else:
    conb = "Not stable"
print(conb)





for i in range(n):
    mini = i
    for j in range(i, n):
        if c[j].v < c[mini].v:
            mini = j
    c[mini], c[i] = c[i], c[mini]

print(" ".join(x.self_str() for x in c))

couc = ["" for i in range(10)]
conc = ""
for i in range(n):
    for j in range(n):
        if i != j:
            if c[i].v == c[j].v:
                couc[c[i].v] += c[i].c
if coua == couc:
     conc = "Stable"
else:
    conc = "Not stable"

print(conc)