from collections import deque

s1 = deque()
s2 = deque()

s = input()
totalarea = 0

for i,c in enumerate(s):
    if c == '\\':
        s1.append(i)
    elif s1 and c == '/':
        j = s1.pop()
        area = i - j
        totalarea +=  area
        subarea = area
        while s2 and s2[-1][0] > j:
            subarea += s2[-1][1]
            s2.pop()
        s2.append((j, subarea))

print(totalarea)
print(len(s2), end='')
if s2:
    print(" ",end="")
    areas = [str(puddle[1]) for puddle in s2]
    print(" ".join(areas))
else:
    print("")

