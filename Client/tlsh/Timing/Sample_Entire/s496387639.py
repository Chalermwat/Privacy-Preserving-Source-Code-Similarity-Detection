from collections import deque
from sys import stdin
data = list(stdin.readline().rstrip())
i_stack, a_stack, b_stack = deque(), deque(), deque()
ans = 0
for i, c in enumerate(data):
    if c == '\\':
        i_stack.append(i)
    elif c == '/' and len(i_stack) != 0:
        j = i_stack.pop()
        diff = i - j
        ans += diff 
        while a_stack and a_stack[-1] > j:
            diff += b_stack.pop()
            a_stack.pop()
        a_stack.append(j)
        b_stack.append(diff)
print(ans)
print(len(a_stack), *b_stack)
