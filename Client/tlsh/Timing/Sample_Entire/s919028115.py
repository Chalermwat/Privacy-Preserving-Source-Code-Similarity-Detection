strs = input()
h = 0
heights = [0]
max_h = 0
k = []
sum = 0
for i, s in enumerate(strs, 1):
    if s=='\\':
        h -= 1
        heights.append(h)
    elif s=='/':
        h += 1
        heights.append(h)
        if h>max_h:
          max_h = h
          continue
        t = -2
        while t+i+1>=0:
            if heights[t]==h:
                sum += (-t-3)+1
                tmp = (-t-3)+1
                if len(k)>0:
                  c = len(k)
                  for ts, te, tm in k[::-1]:
                    c -= 1
                    if t+i+1<ts and te<i:
                        k.pop(c)
                        tmp += tm
                k.append([t+i+1, i, tmp])
                break
            else:
                t -= 1
                continue
    else:
        heights.append(h)
        continue
print(sum)
ans = [str(k[-1]) for k in k]
print(len(ans), *ans)
