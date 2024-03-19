import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

def main():
    t = input().strip()
    s = []
    # A = 0
    ans = []
    prevA = 0
    for i in range(len(t)):
        if t[i] == '\\':
            s.append(i)
        elif len(s) > 0 and t[i] == '/':
            p = s.pop()
            k = i - p
            ans.append((p, k))
            q = 0
            while len(ans) > 0:
                # print(ans)
                g, h = ans[-1]
                if g >= p:
                    q += h
                    ans.pop()
                else:
                    break
            # for j in range(len(ans) - len(s)):
            #     print('i: ', i)
            #     print('j: ', j)
            #     print('ans: ', ans)
            #     q += ans.pop()
                # print('q: ', q)
            if q != 0:
                ans.append((p, q))
        # elif len(s) > 0 and t[i] == '_':
        #     A += 1

    v = 0
    for i in range(len(ans)):
        v += ans[i][1]
    print(v)
    print(len(ans), end='')
    for i in range(len(ans)):
        print(' {}'.format(ans[i][1]), end='')
    print('')

if __name__ == '__main__':
    main()

