s = input()
stack = []
n = len(s)

ans = 0
prev = 0
each = []
for i in range(n):
    if s[i] == '\\':
        stack.append(i)
    elif s[i] == '_':
        pass
    else:
        if len(stack) != 0:
            idx = stack.pop()
            ans += (i - idx)
            if len(stack) == 0:
                each.append(ans - prev)
                prev = ans

each2 = []
stack2 = []
ans2 = 0
prev2 = 0
if len(stack) >= 1:
    for i in range(n-1,stack[0],-1):
        if s[i] == '/':
            stack2.append(i)
        elif s[i] == '_':
            pass
        else:
            if len(stack2) != 0:
                idx = stack2.pop()
                ans2 += (idx - i)
                if len(stack2) == 0:
                    each2.append(ans2 - prev2)
                    prev2 = ans2
each2.reverse()
each.extend(each2)
print(ans)
if len(each) == 0:
    print(len(each))
else:
    print(len(each),end=" ")
    print(*each)

