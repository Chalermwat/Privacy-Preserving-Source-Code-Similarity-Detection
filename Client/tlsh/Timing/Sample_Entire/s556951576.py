import bisect, collections, copy, heapq, itertools, math, string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())

from collections import deque
A = S()
Down = deque([])
S = deque([])

for i in range(len(A)):
    if A[i] == '\\':
        Down.append(i)
    elif A[i] == '/' and len(Down) != 0:
        j = Down.pop()
        a = i - j
        while len(S) > 0 and S[-1][0] > j:
            a += S.pop()[1]
        S.append((j, a))
ans = []
for i in range(len(S)):
    ans.append(S[i][1])
print(sum(ans))
ans.insert(0, len(ans))
print(' '.join(map(str, ans)))
