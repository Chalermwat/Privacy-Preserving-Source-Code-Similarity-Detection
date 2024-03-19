stack = []
res = []

area = input()

for i, terrain in enumerate(area):
    if terrain == '\\':
        stack.append(i)
    elif terrain == '/' and len(stack)>0:
        left = stack.pop()
        pond = i - left
        if len(res) == 0 or left >= res[-1][0]:
            res.append([left,pond])
        else:
            while len(res) > 0 and left < res[-1][0] :
                pond += res[-1][1]
                res.pop()
            res.append([left,pond])

total = 0
ponds = []
for i in res:
    ponds.append(i[1])
    total += i[1]

ans = [len(res)]
ans += ponds
ans_new = " ".join(map(str,ans))

print(total)
print(ans_new)

