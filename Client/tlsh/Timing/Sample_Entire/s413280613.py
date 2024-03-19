S = [s for s in input()]

stack1 = []
stack2 = []

for i in range(len(S)):
    if S[i] == '\\':
        stack1.append(i)
    elif S[i] == '/':
        if len(stack1) != 0:
            pos = stack1.pop()
            area = i - pos
            while len(stack2) != 0:
                pair = stack2.pop()
                if pos < pair[0]:
                    area += pair[1]
                else:
                    stack2.append(pair)
                    break
            stack2.append((pos, area))

print(sum([s[1] for s in stack2]))
print(len(stack2), *[s[1] for s in stack2])
