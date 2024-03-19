mod = 998244353

# 貰うDP
def main(N, S):
    dp = [0 if n != 0 else 1 for n in range(N)]     # dp[i]はマスiに行く通り数． (答えはdp[-1]), dp[0] = 1 (最初にいる場所だから1通り)
    A = [0 if n != 0 else 1 for n in range(N)]      # dp[i] = A[i] - A[i-1] (i >= 1), A[0] = dp[0] = 1 (i = 0) が成り立つような配列を考える．

    for i in range(1, N):   # 今いる点 (注目点)
        for l, r in S:  # 選択行動範囲 (l: 始点, r: 終点)
            if i - l < 0:   # 注目点が選択行動範囲の始点より手前の場合 → 注目点に来るために使用することはできない．
                break
            else:           # 注目点に来るために使用することができる場合
                dp[i] += A[i-l] - A[max(i-r, 0)-1]  # lからrの間で，注目点に行くために使用できる点を逆算． そこに行くことができる = 選択行動範囲の値を選択することで注目点に達することができる通り数．
        dp[i] %= mod
        A[i] = (A[i-1] + dp[i]) % mod
    print(dp[-1])

if __name__ == '__main__':
    N, K = list(map(int, input().split()))
    S = {tuple(map(int, input().split())) for k in range(K)}
    S = sorted(list(S), key = lambda x:x[0])    # 始点でsort (範囲の重複がないため)
    main(N, S)