N, K = map(int, input().split())
L=[]
R=[]
for i in range(K):
  l,r= map(int, input().split())
  L.append(l)
  R.append(r)

dp=[0]*N
dp[0]=1
dpc=[0]*(N+1)
dpc[1]=1

for i in range(N):
  for j in range(K):
    dp[i]+=dpc[max(i-L[j]+1,0)]-dpc[max(i-R[j],0)]
  dp[i]%=998244353
  dpc[i+1]=dpc[i]+dp[i]

print(dp[N-1])