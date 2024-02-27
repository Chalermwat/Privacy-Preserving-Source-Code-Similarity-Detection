import sys
sys.setrecursionlimit(10 ** 9)
# input = sys.stdin.readline    ####
def int1(x): return int(x) - 1
def II(): return int(input())
def MI(): return map(int, input().split())
def MI1(): return map(int1, input().split())
def LI(): return list(map(int, input().split()))
def LI1(): return list(map(int1, input().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def MS(): return input().split()
def LS(): return list(input())
def LLS(rows_number): return [LS() for _ in range(rows_number)]
def printlist(lst, k=' '): print(k.join(list(map(str, lst))))
INF = float('inf')
# from math import ceil, floor, log2
# from collections import deque, defaultdict
# from itertools import combinations as comb, combinations_with_replacement as comb_w, accumulate, product, permutations
# from heapq import heapify, heappop, heappush
# import numpy as np    # cumsum
# from bisect import bisect_left, bisect_right

def solve():
    N, K = MI()
    S = []
    mod = 998244353
    for i in range(K):
        l, r = MI()
        S.append((l, r))
    dp = [0] * (N+1)
    dp[1] = 1
    C = [0] * (N+1)
    C[1] = 1
    for i in range(2, N+1):
        for s in S:
            l = max(1, i - s[1])
            r = i - s[0]
            if r < 1:
                continue
            dp[i] += (C[r] - C[l-1]) % mod
        C[i] += (dp[i] + C[i-1]) % mod
    print(dp[N] % mod)
            
if __name__ == '__main__':
    solve()

