from sys import stdin
from collections import deque
N,K = [int(x) for x in stdin.readline().rstrip().split()]
V = [int(x) for x in stdin.readline().rstrip().split()]
ans = 0
rev_V = V[::-1]

for L in range(0, K+1):
        for R in range(0, K+1):
            if L + R > min(K,N):
                break
            
            tmp = V[0:L] + rev_V[0:R]
            tmp.sort()
            tmp = deque(tmp)
            num = K - (L+R)
            stone = -1
            cnt = 0
            while stone < 0:
                if cnt >= num or len(tmp) == 0:
                    break
                stone = tmp.popleft()
                if stone >= 0:
                    tmp.append(stone)
                    break
                cnt += 1
            ans = max(ans, sum(tmp))

print(ans)