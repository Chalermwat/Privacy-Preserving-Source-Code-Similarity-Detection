from collections import deque
s = input()
S1 = deque()
S2 = deque()
total = 0
for i in range(len(s)):
    if s[i] == '\\':
        S1.append(i)
    elif s[i] == '/':
        if len(S1) != 0:
            a = S1.pop()
            total += i - a
            area = i - a
            if len(S2) != 0:
                while S2[-1][0] > a:
                    area += S2.pop()[1]
                    if len(S2) == 0:
                        break
                S2.append([a ,area])
            else:
                S2.append([a, area])
        else:
            pass
print(total)
if total == 0:
    print(0)
else:
    print(len(S2), ' '.join(map(lambda x: str(x[1]), S2)))
