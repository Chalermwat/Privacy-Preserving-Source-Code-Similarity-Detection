from collections import deque
import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")

def main():
    inf = 10 ** 6
    s = input()
    n = len(s)
    land = [0] * (n + 1)
    for i, c in enumerate(s):
        if c == "/":
            land[i + 1] = land[i] + 1
        elif c == "_":
            land[i + 1] = land[i]
        else:
            land[i + 1] = land[i] - 1
    # print(land)

    water = [0] * (n + 1)
    w = -inf
    i = n
    for l in land[::-1]:
        if l > w: w = l
        water[i] = w
        i -= 1
    w = -inf
    for i, l in enumerate(land):
        if l > w: w = l
        water[i] = min(water[i], w)
    # print(water)

    mm = []
    sum_d = 0
    for w, l in zip(water, land):
        d = w - l
        if d == 0 and sum_d:
            mm.append(sum_d)
            sum_d = 0
        else:
            sum_d += d

    print(sum(mm))
    print(len(mm), *mm)

main()

