string = input()

s = []
total = 0
s2 = []
for i in range(len(string)):
    if string[i] == '\\':
        s.append(i)
    elif string[i] == '/' and len(s) > 0:
        j = s.pop() # j: 対応する '\' の位置
        area = i - j # 面積
        total += area
        while len(s2) > 0 and s2[-1][0] > j: # s2[-1][0] == s2.pop()[0]
            area += s2[-1][1]
            s2.pop()
        s2.append([j, area]) # j: 水たまりの左端 / tmp: その水たまりの面積

ans = []
for i in range(len(s2)):
    ans.append(str(s2[i][1]))

print(total)
if len(ans) == 0:
    print(len(ans))
else:
    print(len(ans), end = ' ')
    print(' '.join(ans))
