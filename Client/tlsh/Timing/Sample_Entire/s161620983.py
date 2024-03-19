n = input()

s1 = []
s2 = []

for i in range(len(n)):
    if n[i] == '\\':
        s1.append(i)
    elif n[i] == '/' and len(s1) > 0:
        a = s1.pop(-1)
        s2.append([a, i - a])

i = 0
while len(s2) > 1:
    if i == len(s2) - 1:
        break
    elif s2[i][0] > s2[i + 1][0]:
        s2[i + 1][1] += s2.pop(i)[1]
        i = 0
    else:
        i += 1

s = []
total = 0
for i in s2:
    s.append(str(int(i[1])))
    total += int(i[1])
print(total)
if len(s2) == 0:
    print('0')
else:
    print('{} {}'.format(len(s2), ' '.join(s)))
