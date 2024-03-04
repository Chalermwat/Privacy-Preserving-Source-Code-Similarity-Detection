import sys
from itertools import combinations_with_replacement

input = sys.stdin.readline


def main():
    N, M, Q = map(int, input().split())
    abcd = [None] * Q
    for i in range(Q):
        abcd[i] = list(map(int, input().split()))
        abcd[i][0] -= 1
        abcd[i][1] -= 1

    ans = 0
    for A in combinations_with_replacement(range(1, M + 1), N):
        score = 0
        for a, b, c, d in abcd:
            if A[b] - A[a] == c:
                score += d
        if score > ans:
            ans = score

    print(ans)


if __name__ == "__main__":
    main()
