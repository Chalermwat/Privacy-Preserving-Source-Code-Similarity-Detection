from collections import deque

stack = []
stack2 = []

input_line = input().rstrip()

menseki = 0

for i, s in enumerate(input_line):
    if s == "\\":
        stack.append(i)
    elif s == "/" and len(stack) > 0:
        j = stack.pop()
        menseki += (i - j)
        temp_menseki = 0
        while len(stack2) > 0 and j < stack2[-1][0]:
            temp_menseki += stack2.pop()[1]
                    
        stack2.append([j, temp_menseki + (i - j)])

print(menseki)
if len(stack2) > 0:
    print(len(stack2), " ".join([str(j[1]) for j in stack2]))
else:
    print("0")


