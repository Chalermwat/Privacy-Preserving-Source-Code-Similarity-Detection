from sys import stdin
from collections import deque

sect = stdin.readline().lstrip("/_").rstrip("\n\\_")
stack = deque()
res = deque()

for i in range(len(sect)):
    if sect[i] == "\\":
        stack.append(i)
    elif sect[i] == "/":
        if len(stack) != 0:
            b = stack.pop()
            if len(res) == 0:
                res.append( (b, i-b) )
            elif b > res[-1][0]:
                res.append( (b, i-b) )
            else: # 水たまりを結合
                sum_L = i-b
                while len(res) != 0:
                    if res[-1][0] > b:
                    	sum_L += res[-1][1]
                    	res.pop()
                    else:
                    	break

                res.append((b, sum_L))

res = [x[1] for x in res]
print(sum(res))
print(len(res), *res)
