from collections import deque
x = input()
A = 0
S1 = deque()
S2 = deque()

for i in range(len(x)):
    if x[i] == "\\":
        S1.append(i)
    elif x[i] == "/" and len(S1) > 0 :
        j = S1.pop()
        A += i - j
        a  = i - j
        while  len(S2) > 0 and S2[-1][0] > j:
            a += S2[-1][1]
            S2.pop()
        S2.append([j,a])
print(A)

if len(S2)== 0:
    print(0)
else:
    print(len(S2),"",end="")
    for i in range(len(S2)):
        if i == len(S2) - 1:
            print(S2[i][1])
        else:
            print(S2[i][1],"",end="")
