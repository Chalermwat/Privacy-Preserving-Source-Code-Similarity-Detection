#!/usr/bin/python
# -*- coding: UTF-8 -*-

import math
import sys


def calc_p(a, b, c):
    u = {a, b, c}
    if len(u) == 3:
        return 6
    if len(u) == 2:
        return 3
    if len(u) == 1:
        return 1
    else:
        raise


def std_in():
    return sys.stdin.readline().strip()


def _main():
    N = int(std_in())
    fn = [0] * N
    if N == 1:
        x_max = 1
    else:
        x_max = int(math.sqrt(N - 2)) - 1

    n2 = [i**2 for i in range(1, x_max + 1)]

    ij = [[0 for _ in range(1, x_max + 1)] for _ in range(1, x_max + 1)]
    for i in range(x_max):
        for j in range(i, x_max):
            ij[i][j] = (i+1) * (j+1)

    for x in range(1, x_max + 1):
        y_min = x
        x2 = n2[x-1]
        for y in range(y_min, x_max + 1):
            z_min = y
            y2 = n2[y-1]
            xy = ij[x-1][y-1]
            tmp_n = x2 + xy + y2
            if tmp_n > N:
                break
            for z in range(z_min, x_max + 1):
                z2 = n2[z-1]
                yz = ij[y-1][z-1]
                zx = ij[x-1][z-1]
                n = tmp_n + z2 + yz + zx
                if n > N:
                    break
                fn[n-1] += calc_p(x, y, z)

    print(*fn, sep="\n")


if __name__ == "__main__":
    _main()
