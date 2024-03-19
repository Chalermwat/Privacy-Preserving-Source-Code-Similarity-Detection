s = input()
n = len(s)
St = []
St2 = []
h = 0
area = 0

for i in range(n):
    if s[i] == "\\":
        St.append(i)
        h -= 1
    elif s[i] == "/":
        h += 1
        if St:
            left = St.pop()
            area += i - left
            
            area2 = 0
            while St2:
                left2 = St2.pop()
                j = left2[0]
                if left < left2[0]:
                    area_add = left2[1]
                    area2 += area_add
                else:
                    St2.append(left2)
                    break
            St2.append([left, area2 + i-left])


print(area)
ans = [t[1] for t in St2]
if St2:
    print(len(St2), end = " ")
    print(*ans)

else:
    print(0)

