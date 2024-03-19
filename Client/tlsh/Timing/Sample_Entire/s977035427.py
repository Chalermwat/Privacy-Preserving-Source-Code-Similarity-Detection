import math
import string
import itertools
import fractions
import heapq
import collections
import re
import array
import bisect
import sys
import random
import time
inf = 10**9


def main():
    s = input()

    stack = []
    flat_pools = []
    for (i, c) in enumerate(s):
        if c == '\\':
            stack.append(i)
        elif c == '/' and len(stack) > 0:
            flat_pools.append((stack.pop(), i))

    flat_pools.sort(key=lambda pool: pool[0])

    last_index = 0
    pools = []
    area = 0

    for pool in flat_pools:
        area += pool[1] - pool[0]
        if last_index <= pool[0]:
            pools.append(pool[1] - pool[0])
            last_index = pool[1]
        else:
            pools[-1] = pools[-1] + pool[1] - pool[0]

    pools.insert(0, len(pools))
    print(area)
    print(" ".join(map(str, pools)))


if __name__ == '__main__':
    main()

