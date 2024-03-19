import sys
from operator import itemgetter
from collections import deque

input = sys.stdin.readline


def main():
    S = input().rstrip()

    stack = deque()
    M = []
    for i, s in enumerate(S):
        if s == "/":
            if len(stack) == 0:
                pass
            else:
                j = stack.pop()
                M.append((j, i))
        elif s == "\\":
            stack.append(i)
        else:
            pass

    M.sort(key=itemgetter(0))
    L = []
    r = -1
    for i, j in M:
        if r < i:
            r = j
            L.append(j - i)
        else:
            L[-1] += (j - i)

    A = sum(L)
    k = len(L)

    print(A)
    if k == 0:
        print(k)
    else:
        print(" ".join([str(k), " ".join(map(str, L))]))


if __name__ == "__main__":
    main()

