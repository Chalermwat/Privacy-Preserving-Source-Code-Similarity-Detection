# -*- coding: utf-8 -*-

S = input()

# 各地点の高さを求める
v = {'\\': -1, '_': 0, '/': 1}
h = 0  # 左端の高さ
H = [h]
for s in S:
    h += v[s]
    H.append(h)

# 右部分列の最大値
R = [0] * len(H)
R[-1] = -float('inf')
for i in range(len(R) - 2, -1, -1):
    R[i] = max(R[i+1], H[i+1])

A = []
i = 0
while True:
    # 左端の左斜面をスキップ
    while i < len(S) and S[i] != '\\':
        i += 1

    # 右側の縁と同じ高さまでスキップ
    while i < len(S) and (H[i] > R[i] or S[i] == '_'):
        i += 1

    if i >= len(S):
        break

    # 水たまりの面積を求める
    h = H[i]  # 左端の高さ
    a = 0     # 面積
    while i < len(S):
        a += (h - H[i]) + (H[i] - H[i+1])/2
        i += 1
        if H[i] == h: break
    A.append(int(a))

print(sum(A))
print(' '.join(map(str, [len(A)] + A)))
