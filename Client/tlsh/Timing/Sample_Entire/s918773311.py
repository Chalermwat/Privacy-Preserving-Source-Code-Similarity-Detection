from collections import deque

codes = input()

s1 = deque([])
s2 = deque([])

sums = 0
for idx1, ch in enumerate(codes):
    if ch == '\\':
        s1.append(idx1)
    elif ch == '/' and len(s1) > 0:
        idx2 = s1.pop()
        area = idx1 - idx2
        sums += area
        while len(s2) > 0 and s2[-1][0] > idx2:
            area += s2.pop()[1]
        s2.append([idx2, area])

output = []
while len(s2) > 0:
    output.append(s2.pop()[1])
output.reverse()
print(sum(output))
output.insert(0, len(output))
print(" ".join(map(str, output)))
