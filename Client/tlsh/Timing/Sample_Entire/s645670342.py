value = input();

j = 0
s = 0
n = len(value)
stack1 = list()
stack2 = []#[[[] for i in range(2)] for j in range(n)]
while(j < n):
    if value[j] == '\\':
        stack1.append(j)
    if value[j] == '/' :
        if len(stack1) != 0:
            idx1 = stack1[-1]
            idx2 = j
            stack2.append([idx1,idx2 - idx1])
            stack1.pop(-1)
            s += 1
    if s - 2 >= 0:
        if stack2[s-1][0] < stack2[s-2][0]:
            stack2[s-2][0] = stack2[s-1][0]
            stack2[s-2][1] += stack2[s-1][1]
            s -= 1
            stack2.pop(-1)
        
    j += 1

if s - 2 >= 0:
    for i in reversed(range(2, s+1)):
        if stack2[i-1][0] < stack2[i-2][0]:
            stack2[i-2][0] = stack2[i-1][0]
            stack2[i-2][1] += stack2[i-1][1]
            #s -= 1
            stack2.pop(i-1)


sumi = 0
s = len(stack2)
for i in range(0, s):
    sumi += stack2[i][1]
    
print(sumi)
if sumi == 0:
    print(s)
else:
    print(s, end = " ")

for i in range(0, s):
    if i != s - 1:
        print(stack2[i][1], end=" ")
    else:
        print(stack2[i][1])

