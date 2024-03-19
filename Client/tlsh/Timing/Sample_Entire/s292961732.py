s = input()
i = 0
S1 = []
S2 = []
water = []
wtot = 0
while i < len(s):
    if s[i] == "\\":
        S1.append(i)
    elif s[i] == '/' and len(S1) != 0:
        w0 = (i - S1[-1])
        wtot += w0
        if len(S2) == 0:
            S2.append((S1[-1], w0))
        else:
            while len(S2) != 0 and S2[-1][0] > S1[-1]:
                w0 += S2[-1][1]
                S2.pop()
            S2.append((S1[-1], w0))
        S1.pop()
    i += 1

ans = str(wtot) + '\n' + str(len(S2))
for p in S2:
    ans += ' ' + str(p[1])
print(ans)

