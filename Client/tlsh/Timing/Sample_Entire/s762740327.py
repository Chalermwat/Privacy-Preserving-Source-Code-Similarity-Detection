from collections import deque

class peke:
    def __init__(self,Start,End,S):
        self.start=Start
        self.end=End
        self.S=S
    

S1=deque()
S2=deque()
total=0
A=input()

for n in range(len(A)):
    if A[n]=='\\':
        S1.append(n)
    elif A[n]=='/' and S1:
        j=S1.pop()
        now=n-j
        total=total+now
        while S2:
            if S2[-1].start>j and S2[-1].end<n:
                now=now+S2[-1].S
                S2.pop()
            else:
                break
        S2.append(peke(j,n,now))

print(total)
print(len(S2),end ="")
while S2:
    print(" ",end="")
    print(S2[0].S,end="")
    S2.popleft()
print()

