s = input()
depth_list = [0]*len(s)
max_depth = [0]*len(s)
d = 0
for i, c in enumerate(s):
    if c == "\\":
        d -= 1
    elif c == "/":
        d += 1
    depth_list[i] = d

m_d = d
for i in range(len(s)-1, -1, -1):
    if s[i] == "\\":
        d += 1
    elif s[i] == "/":
        d -= 1
    max_depth[i] = m_d
    m_d = max(m_d, d)

d = 0
m_d = 0
water = 0
puddles = [0]
for i, n in enumerate(depth_list):
    up = min(m_d, max_depth[i])
    if d < up and d != n or d == up and d > n:
        water += 0.5
    if d < n:
        d = n
    water += max(0, up - d)
    d = n
    m_d = max(m_d, d)

    if d == up and sum(puddles) < int(water):
        m_d = d
        puddles.append(int(water - sum(puddles)))
print(int(water))
print(str(len(puddles)-1)+(" "if len(puddles)>1 else "")+" ".join([str(n) for n in puddles[1:]]))