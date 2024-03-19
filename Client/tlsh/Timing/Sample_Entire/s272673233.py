import sys
readline = sys.stdin.readline
li = []
for i, s in enumerate(readline().strip()):
    if s == "\\":
        li.append([i, 0])
    elif s == "/":
        if li:
            if li[-1][1] == 0:
                li[-1][1] = i - li[-1][0]
            else:
                for j in range(len(li) - 1, -1, -1):
                    if li[j][1] == 0:
                        li = li[:j] + [[li[j][0], sum(tuple(zip(*li[j + 1:]))[1]) + i - li[j][0]]]
                        break
ans = []
for a in li:
    if a[1] != 0:
        ans.append(a[1])
print(sum(ans))
print(len(ans), *ans)

