N = int(input())

C = input().split()

B = C[:]
S = C[:]

# bubble sort
flag = 1
while(flag):
    flag = 0
    for x in range(1, N):
        if B[x][1:] < B[x-1][1:]:
            B[x], B[x-1] = B[x-1], B[x]
            flag = 1

# sectionSot
for x in range(0,N):
    minj = x
    for j in range(x,N):
        if S[j][1:] < S[minj][1:]:
            minj = j
    if minj != x:
        S[x], S[minj] = S[minj], S[x]



print(" ".join(b for b in B))
print("Stable")


if(B == S):
    print(" ".join(b for b in S))
    print("Stable")
else:
    print(" ".join(b for b in S))
    print("Not stable")