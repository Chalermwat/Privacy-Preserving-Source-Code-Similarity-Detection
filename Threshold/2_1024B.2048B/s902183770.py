from collections import Counter, defaultdict
import sys
sys.setrecursionlimit(10 ** 5 + 10)
# input = sys.stdin.readline
from math import factorial
import heapq, bisect
import math
import itertools


import queue
from collections import deque




def main():
    num = int(input())
    data1 = list(map(int, input().split()))
    data2 = list(map(int, input().split()))

    dp1 = [0 for i in range(num)]
    dp2 = [0 for i in range(num)]

    dp1[0] = 1
    for i in range(1, num):
        if data1[i] > data1[i - 1]:
            dp1[i] = 1
        # else:
        #     dp1[i] = data1[i]

    data2 = data2[::-1]
    dp2[0] = 1
    for i in range(1, num):
        if data2[i] > data2[i - 1]:
            dp2[i] = 1
        # else:
        #     dp1[i] = data1[i]
    dp2 = dp2[::-1]
    data2 = data2[::-1]

    ans = 1
    mod = 10 ** 9 + 7
    for i in range(num):
        if dp1[i] and dp2[i]:
            if data1[i] == data2[i]:
                pass
            else:
                ans *= 0
        elif dp1[i]:
            if data1[i] <= data2[i]:
                pass
            else:
                ans *= 0
        elif dp2[i]:
            if data2[i] <= data1[i]:
                pass
            else:
                ans *= 0
        else:
            ans *= min(data1[i], data2[i])
        ans %= mod

    print(ans)






if __name__ == '__main__':
    main()

