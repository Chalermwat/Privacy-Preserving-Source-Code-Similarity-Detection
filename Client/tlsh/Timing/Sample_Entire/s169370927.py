input()
C = [[x[0], x[1]] for x in list(input().split())]
D = C.copy()
N = len(C)

# バブルソート
for i in range(0, N-1, 1):
    for j in range(N-1, i, -1):
        if C[j][1] < C[j-1][1]:
            tmp = C[j]
            C[j] = C[j-1]
            C[j-1] = tmp

# 選択ソート
for i in range(0, N-1, 1):
    minj = i
    for j in range(i, N, 1):
        if D[j][1] < D[minj][1]:
            minj = j
    tmp = D[i]
    D[i] = D[minj]
    D[minj] = tmp

# バブルソートの結果出力
length = len(C)
for i in range(length):
    if i == length - 1:
        print("".join(C[i]), end="")
    else:
        print("".join(C[i]), end=" ")

print("")
print("Stable")

# 選択ソートの結果出力
for i in range(length):
    if i == length - 1:
        print("".join(D[i]), end="")
    else:
        print("".join(D[i]), end=" ")

print("")
if C == D:
    print("Stable")
else:
    print("Not stable")

