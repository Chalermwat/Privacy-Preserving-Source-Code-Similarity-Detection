from collections import deque

s = input()

d = deque()
l = deque()


def calc_area(j, i):
    return i - j


for i, c in enumerate(s):
    if c == "\\":
        d.append(i)
    if c == "/":
        if len(d) == 0:
            continue

        j = d.pop()

        s = calc_area(j, i)
        while len(l) > 0:
            _j, _i, _s = l.pop()
            if j < _j:
                s += _s
            else:
                l.append((_j, _i, _s))
                break

        l.append((j, i, s))

ans = str(len(l))
sum_area = 0
for j, i, s in l:
    ans += " " + str(s)
    sum_area += s

print(sum_area)
print(ans)