n,k=map(int,input().split())
ll=[list(map(int,input().split())) for _ in range(k)]
dp=[0]*(3*n)
dp[0]=1
dp[1]=-1
for i in range(n):
    for l,r in ll:
        dp[l+i]+=dp[i]
        dp[i+r+1]-=dp[i]
    dp[i+1]=(dp[i]+dp[i+1])%998244353
print(dp[n-1])