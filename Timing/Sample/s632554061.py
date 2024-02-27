#   ==========     //\\       //||     ||====//||
#       ||        //  \\        ||     ||   // ||
#       ||       //====\\       ||     ||  //  ||
#       ||      //      \\      ||     || //   ||
#   ========== //        \\  ========  ||//====|| 
#  code

def solve():
    MOD = 998244353
    n, k = map(int, input().split())
    segments = []
    for i in range(k):
        l, r = map(int, input().split())
        segments.append([l, r])
    
    dp = [0] * (n)
    dp[0] = 1
    pdp = [1] * (n)
    for i in range(1 , n):
        pdp[i] = pdp[i - 1] + dp[i]
    
    for j in range(n):
        for i in range(k):
            if j <= segments[i][1] and j >= segments[i][0]:
                dp[j] += pdp[j - segments[i][0]]
            elif j > segments[i][1]:
                dp[j] += pdp[j - segments[i][0]] - pdp[j - segments[i][1] - 1]
            dp[j] %= MOD
            # print(i, dp[j])
            if j > 0:
                pdp[j] = pdp[j - 1] + dp[j]
            else:
                pdp[j] = dp[j]
            pdp[j] %= MOD
    print(dp[n - 1])
    return

def main():
    t = 1
    # t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()