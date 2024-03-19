# coding: utf-8
from collections import deque
input_line = input().strip()
stack1, stack2 = deque(), deque()
for index, i in enumerate(input_line):
    if i == "\\":
        stack1.append(index)
    elif i == "/" and len(stack1) != 0:
        a = stack1.pop()
        #池のマージ
        if len(stack2) != 0 and abs(stack2[-1][0] - a) == 1:
            stack2.append([a, index - a + stack2.pop()[1]])
        else:
            stack2.append([a, index - a])
        #さらにマージ
        while len(stack2) >= 2 and stack2[-1][0] < stack2[-2][0]:
            stack2.append([stack2[-1][0], stack2.pop()[1] + stack2.pop()[1]])
ans = [i[1] for i in stack2]
print(sum(ans))
ans.insert(0, len(ans))
print(*ans)