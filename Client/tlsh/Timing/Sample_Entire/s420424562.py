from queue import LifoQueue

MAP = input()

que = LifoQueue()
res = LifoQueue()

for i, m in enumerate(MAP):
    if m=='\\':
        que.put(i)
    elif m=='/':
        if not que.empty():
            j = que.get(False)
            v = i - j
            t = (j, v)
            while not res.empty():
                pre = res.get(False)
                if (pre[0] > j):
                    t = (t[0], t[1] + pre[1])
                else:
                    res.put(pre)
                    res.put(t)
                    break
            else:
                res.put(t)

summaly = 0
lakes = []
while not res.empty():
    v = res.get()
    lakes.append(v[1])
    summaly += v[1]

print(summaly)
print(len(lakes), *(reversed(lakes)))

