"""
アルゴリズムとデータ構造 P.116
をPythonで書いた
"""

s = input()
stack1 = list()
stack2 = list()
sm = 0

for i, c in enumerate(s):
    if c == '\\':
        stack1.append(i)
        continue

    if c == '/' and len(stack1) > 0:
        j = stack1.pop()
        sm += i - j
        a = i - j
        while len(stack2) > 0 and stack2[-1][0] > j:
            a += stack2.pop()[1]
        stack2.append((j, a))

print(sm)
ans = list()
ans.append(len(stack2))
for _, a in stack2:
    ans.append(a)
print(" ".join([str(i) for i in ans]))

