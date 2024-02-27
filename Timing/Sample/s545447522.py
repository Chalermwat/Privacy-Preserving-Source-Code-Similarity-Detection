(n,_),*s=[[*map(int,t.split())]for t in open(0)]
d=[1,-1]+[0]*2*n
for i in range(n):
  d[i]=(d[i-1]+d[i])%998244353
  for l,r in s:
    d[i+l]+=d[i]
    d[i-~r]-=d[i]
print(d[n-1])