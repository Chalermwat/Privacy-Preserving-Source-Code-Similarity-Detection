S = input()
lake_sum = 0
stack1 = []
stack2 = []
for i in range(len(S)):
    if S[i] == '\\':
        stack1.append(i)
    elif S[i] == '/':
        if stack1 == []:
            continue
        j = stack1.pop()
        area = i - j
        lake_sum += area
        while True:
            if stack2 == []:
                break
            k, l = stack2.pop()
            if k < j:
                stack2.append((k, l))
                break
            area += l
        stack2.append((j, area))
print(lake_sum)
if stack2 == []:
    print(0)
else:
    lakes = []
    lakes.append(str(len(stack2)))
    for lake in stack2:
        lakes.append(str(lake[1]))
    print(' '.join(lakes))
