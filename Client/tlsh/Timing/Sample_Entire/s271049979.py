s = input()

length = len(s)

a = [0] * (length + 1)
b = [0] * length
y = 0
for i in range(length):
    if s[i] == '/':
        y += 1
    elif s[i] == '\\':
        y -= 1
    a[i + 1] = y

m = -30000
for i in range(length, 0, -1):
    m = max(m, a[i])
    b[i - 1] = m

i = 0
memory = []
while i < length:
    if a[i] > b[i]:
        i += 1
        continue

    start = a[i]
    i += 1
    base = 1
    d_from = s[i - 1]
    ws_part = 0
    while i < length + 1 and a[i] < start:
        d_to = s[i]
        ws_part += base
        if d_from == '\\' and d_to == '\\':
            base += 2
        if d_from == '\\' and d_to == '_':
            base += 1
        if d_from == '/' and d_to == '/':
            base -= 2
        if d_from == '/' and d_to == '_':
            base -= 1
        if d_from == '_' and d_to == '\\':
            base += 1
        if d_from == '_' and d_to == '/':
            base -= 1
        d_from = d_to
        i += 1

    if ws_part > 0:
        ws_part += 1
        memory.append(ws_part // 2)

print(sum(memory))
if memory:
    print(len(memory), ' '.join(map(str, memory)))
else:
    print(len(memory))

