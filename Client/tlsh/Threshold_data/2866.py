import sys,os
from collections import defaultdict, deque
from math import ceil, floor
if sys.version_info[1] >= 5:
    from math import gcd
else:
    from fractions import gcd
sys.setrecursionlimit(10**6)
write = sys.stdout.write
dbg = (lambda *something: print(*something)) if 'TERM_PROGRAM' in os.environ else lambda *x: 0
def main(given=sys.stdin.readline):
    input = lambda: given().rstrip()
    LMIIS = lambda: list(map(int,input().split()))
    II = lambda: int(input())
    MOD = 998244353
 
    N = II()
    D = LMIIS()
    num_D = [0]*N
    for d in D:
        num_D[d] += 1
    if D[0] != 0 or num_D[0] != 1:
        print(0)
        return
    ans = 1
    prev = 1
    dbg(num_D)
    for i,v in enumerate(num_D):
        if v == 0:
            if N-i != num_D.count(0):
                print(0)
                return
            break
        ans *= pow(prev,v,MOD)
        ans %= MOD
        prev = v
    print(ans)


    

    

if __name__ == '__main__':
    main()