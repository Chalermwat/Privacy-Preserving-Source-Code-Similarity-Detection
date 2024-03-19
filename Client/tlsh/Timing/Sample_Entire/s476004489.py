import sys
from collections import deque
def input():
    return sys.stdin.readline()[:-1]
A = input()

total = 0
total_each = deque()
S1 = deque()
S2 = deque()
for j,a in enumerate(A):
    #print('j = {}, S2 = {}'.format(j,S2))
    if a == '\\':
        S1.append(j)
    elif a=='/':
        try:
            i = S1.pop()
            val_new = j-i
            total += val_new
            
            if len(S2)==0:
                S2.append((i,val_new))
                continue
            
            while True:
                if len(S2)>0:
                    a,val = S2[-1]
                    if a<i:
                        S2.append((i, val_new))
                        break
                    elif i<a:
                        _ = S2.pop()
                        val_new = val + val_new
                else:
                    S2.append((i,val_new))
                    break
        except:
            pass
print(total)
ans = [len(S2)]
for _ in range(len(S2)):
    a,val = S2.popleft()
    ans.append(val)
print(*ans)
