import sys
from collections import deque

data = list(sys.stdin.readline()[:-1])

ponds = deque()
result = deque()
index = 0
amount = 0
lefs = deque()

for i in data:
    if i == "\\" or i == "_":
        ponds.append([i, index])
    else:
        count = 0
        while 1 <= len(ponds):
            pond, ind = ponds.pop()
            if pond == "\\":
                count += (index - ind)
                amount += count
                pre_pond = 0
                pre_left = 0
                while 0 < len(lefs) and ind < lefs[-1]:
                    pre_left = lefs.pop()
                    pre_pond += result.pop()
                lefs.append(ind)
                result.append(count + pre_pond)
                break
    index += 1

print(amount)
if 0 == len(result):
    print(0)
else:
    print(len(result), ' '.join(map(str, result)))