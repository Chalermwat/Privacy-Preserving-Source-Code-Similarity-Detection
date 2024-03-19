# coding: utf-8
s = list(input().rstrip())
ht = []
ponds=[]
for i, ch in enumerate(s):
    if ch == "\\":
        ht.append(i)
    elif ch == "/":
        if ht:
            b = ht.pop()
            ap = i - b
            if not ponds:
                ponds.append([b, ap])
            else:
                while ponds:
                    p = ponds.pop()
                    if p[0] > b:
                        ap += p[1]
                    else:
                        ponds.append([p[0],p[1]])
                        break
                ponds.append([b,ap])
    else:
        pass

ans = ""
area = 0
for point, ar in ponds:
    area += ar
    ans += " "
    ans += str(ar)
print(area)
print(str(len(ponds)) + ans)
