from collections import deque
import sys

# downには「\」の数を入れる
down = deque()
edge = deque()
pool = deque()

for i, j in enumerate(sys.stdin.readline().splitlines()[0]):
    if j == "\\":
        down.append(i)
    # downが空でなく、かつ右斜面の場合
    elif down and j == "/":
        left = down.pop()
        area = i - left

        # edgeが空になるまで
        while edge:
            # 右端が
            if edge[-1] < left:
                break
            edge.pop()
            area += pool.pop()

        edge.append(left)
        pool.append(area)

print(sum(pool))
print(len(pool), *pool)

