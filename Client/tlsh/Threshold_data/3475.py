# region header
import sys
import math
from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter
from copy import deepcopy
from fractions import gcd
from functools import lru_cache, reduce
from heapq import heappop, heappush
from itertools import accumulate, groupby, product, permutations, combinations, combinations_with_replacement
from math import ceil, floor, factorial, log, sqrt, sin, cos
from operator import itemgetter
from string import ascii_lowercase, ascii_uppercase, digits
sys.setrecursionlimit(10**6)
rs = lambda: sys.stdin.readline().rstrip()
ri = lambda: int(rs())
rf = lambda: float(rs())
rs_ = lambda: [_ for _ in rs().split()]
ri_ = lambda: [int(_) for _ in rs().split()]
rf_ = lambda: [float(_) for _ in rs().split()]
INF = float('inf')
MOD = 10 ** 9 + 7
# endregion
N = ri()
C = [0] * (N - 1)
S = [0] * (N - 1)
F = [0] * (N - 1)
for i in range(N - 1):
    C[i], S[i], F[i] = ri_()
dp = [0] * N
for i in range(N):
    dp[i] = 0
    for j in range(i, N - 1):
        dp[j + 1] = C[j] + max(S[j], ceil(dp[j] / F[j]) * F[j])
    print(dp[N - 1])