n,k=map(int,input().split())
dp=[0 for i in range(n+1)]
acc=[0 for i in range(n+1)]
dp[1]=1
mod=998244353
acc[1]=1
l,r=[],[]
for i in range(k):
    a,b=map(int,input().split())
    l.append(a)
    r.append(b)
for i in range(2,n+1):
    for j in range(k):
        if i-l[j]<0:
            continue
        dp[i]+=(acc[i-l[j]]-acc[max(0,i-r[j]-1)])
        dp[i]%=mod
    acc[i]=(acc[i-1]+dp[i])%mod
print(dp[-1])