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


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def kock(n, p1, p2):
    if n == 0:
        return

    s = Coordinate((2 * p1.x + p2.x) / 3, (2 * p1.y + p2.y) / 3)
    t = Coordinate((p1.x + 2 * p2.x) / 3, (p1.y + 2 * p2.y) / 3)
    u = Coordinate(
        (t.x - s.x) * math.cos(math.pi / 3) -
        (t.y - s.y) * math.sin(math.pi / 3) + s.x,
        (t.x - s.x) * math.sin(math.pi / 3) +
        (t.y - s.y) * math.cos(math.pi / 3) + s.y
    )

    kock(n - 1, p1, s)
    print(s.x, s.y)
    kock(n - 1, s, u)
    print(u.x, u.y)
    kock(n - 1, u, t)
    print(t.x, t.y)
    kock(n - 1, t, p2)


def main():
    n = int(input())

    p1 = Coordinate(0, 0)
    p2 = Coordinate(100, 0)

    print(p1.x, p1.y)
    kock(n, p1, p2)
    print(p2.x, p2.y)


if __name__ == '__main__':
    main()

