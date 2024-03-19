# -*- coding: utf-8 -*-

line = map(str, raw_input())
place = 0
area = 0
stack1 = []
stack2 = []
for i in line:
    if i == '\\':
        stack1.append(place)
    elif i == '/':
        if len(stack1) != 0:
            j = stack1.pop()
            s = place-j
            area += s
            while len(stack2) != 0:
                if stack2[-1][0] <= j:
                    break
                tmp = stack2.pop()
                s += tmp[1]
            stack2.append([j, s])
    place += 1
print area
temp = []
for a in stack2:
    temp.append(a[1])
if len(stack2) > 0:
    print len(stack2),
    print " ".join(map(str, temp))
else:
    print len(stack2)