def solve(N, LR):
    mod = 998244353

    dp = [0]*(N+1)
    dp[1] = 1
    dpsum = [0]*(N+1)
    dpsum[1] = 1

    for i in range(2, N+1):
        for lr in LR:
            left = i - lr[1]
            right = i - lr[0]
            if right < 0:
                continue
            left = max(left, 0)
            dp[i] += (dpsum[right] - dpsum[left-1])
            dp[i] %= mod
        dpsum[i] = dpsum[i-1] + dp[i]
        dpsum[i] %= mod

    return dp[N]


if __name__ == "__main__":
    N, K = map(int, input().split())
    LR = [list(map(int, input().split())) for _ in range(K)]
    print(solve(N, LR))
