n = int(input())
A = input().rstrip().split()
B = list(map(lambda x:int(x[1]), A))
C = list(enumerate(B))
D = list(enumerate(B))

Cb = C
nums = [n - i for i in range(1, n)]
flag = 1

while flag == 1:
    flag = 0
    for j in nums:
        if Cb[j][1] < Cb[j - 1][1]:
            Cb[j], Cb[j - 1] = Cb[j - 1], Cb[j]
            flag = 1
        else:
            pass
Ab = [A[Cb[i][0]] for i in range(n)]
print(*Ab)
bstable = 1
for j in range(n - 1):
    if Cb[j + 1][1] == Cb[j][1] and Cb[j + 1][0] < Cb[j][0]:
        bstable = 0
        break
if bstable == 1:
    print("Stable")
else:
    print("Not stable")

Cs = D
for i in range(n):
    minj = i
    for j in range(i, n):
        if Cs[j][1] < Cs[minj][1]:
            minj = j
        else:
            pass
    Cs[i], Cs[minj] = Cs[minj], Cs[i]
    
As = [A[Cs[i][0]] for i in range(n)]
print(*As)
cstable = 1
for j in range(n - 1):
    if Cs[j + 1][1] == Cs[j][1] and Cs[j + 1][0] < Cs[j][0]:
        cstable = 0
        break
if cstable == 1:
    print("Stable")
else:
    print("Not stable")

