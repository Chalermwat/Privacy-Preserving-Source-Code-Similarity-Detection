#alds13c
from collections import deque

d_stack=deque()
res_stack=deque()
s = input()

for i in range(len(s)):
    #print(d_stack,res_stack)
    if s[i]=="\\":
        d_stack.append(i)
    elif s[i]=="/":
        if len(d_stack)==0:
            continue
        left = d_stack.pop()
        area = i-left
        #res_stack.append((left,area))
        if len(res_stack)>0:
            flag=True
            #merge_candidate = []
            mergeareasum=0
            while flag:
                if len(res_stack)>0 and left<res_stack[-1][0]:
                    mc = res_stack.pop()
                    mergeareasum += mc[1]
                    #res_stack.append((left,under[1]+area))
                else:
                    flag = False
                    res_stack.append((left,area+mergeareasum))
        else:
                res_stack.append((left,area))

ans=0
v_devided=[]
for pair in res_stack:
    ans += pair[1]
    v_devided.append(str(pair[1]))
print(ans)
if len(v_devided)>0:
    print(len(v_devided)," ".join(v_devided))
else:
    print(0)
