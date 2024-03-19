inp = input()


lst = list(inp)
stk = []
stk2 = []

for i in range(len(lst)):
    if lst[i] == '\\':
        stk.append(i)
    if lst[i] == '/' and len(stk)>0:
        idx = stk.pop()
        a = i - idx
        if len(stk2) > 0:
            while(len(stk2) > 0):
                tmp = stk2.pop()
                if idx < tmp[0]:
                    a += tmp[1]
                else:
                    stk2.append(tmp)
                    break
        stk2.append([idx, a])

s = 0
l = []

for i in stk2:
    l.append((i[1]))
    s += i[1]
print(s)
if(len(stk2) > 0):
    print(len(stk2), end=' ')
    print(*l)
else:
    print("0")

