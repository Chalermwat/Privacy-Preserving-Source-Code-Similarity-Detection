import sys, os, math, bisect, itertools, collections, heapq, queue
# from scipy.sparse.csgraph import csgraph_from_dense, floyd_warshall
from decimal import Decimal
from collections import defaultdict, deque
import copy

sys.setrecursionlimit(10000000)

ii = lambda: int(sys.stdin.buffer.readline().rstrip())
il = lambda: list(map(int, sys.stdin.buffer.readline().split()))
fl = lambda: list(map(float, sys.stdin.buffer.readline().split()))
iln = lambda n: [int(sys.stdin.buffer.readline().rstrip()) for _ in range(n)]

iss = lambda: sys.stdin.buffer.readline().decode().rstrip()
sl = lambda: list(map(str, sys.stdin.buffer.readline().decode().split()))
isn = lambda n: [sys.stdin.buffer.readline().decode().rstrip() for _ in range(n)]

lcm = lambda x, y: (x * y) // math.gcd(x, y)

MOD = 10 ** 9 + 7
MAX = float('inf')


def calc_water(u, l, h):
    return ((u + l) * h) // 2


def main():
    if os.getenv("LOCAL"):
        sys.stdin = open("input.txt", "r")

    S = iss()
    stack = []

    water = []
    sum = 0
    for i in range(len(S)):
        s = S[i]
        if s == '\\':
            stack.append(i)
        elif s == '/' and len(stack) > 0:
            j = stack.pop()
            sum += i - j
            area = i - j
            while len(water) > 0 and water[-1][0] > j:
                w = water.pop()
                area += w[1]
            water.append([j, area])

    ret = []
    for i, w in water:
        ret.append(w)
    print(sum)
    print(len(ret), *ret)


if __name__ == '__main__':
    main()

