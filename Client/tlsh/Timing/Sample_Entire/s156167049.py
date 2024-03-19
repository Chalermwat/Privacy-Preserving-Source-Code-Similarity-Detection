visited = {0: -1}
height = 0
pools = []
for i, c in enumerate(input()):
    if c == '\\':
        height -= 1
    elif c == '/':
        height += 1
        if height in visited:
            width = i - visited[height]
            sm = 0
            while pools and pools[-1][0] > visited[height]:
                x, l = pools.pop()
                sm += l
            pools.append((i, sm + width - 1))
    visited[height] = i

print(sum(l for x, l in pools))
if pools:
    print(len(pools), ' '.join(str(l) for x, l in pools))
else:
    print(0)