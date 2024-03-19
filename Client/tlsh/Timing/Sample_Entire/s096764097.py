mod = 998244353
n,k =map(int,input().split())
step =[0]*(n+1)
# step[0]=1
step[1]=1
stepsum=[0]*(n+1)
stepsum[1]=1
l=[0]*k
r=[0]*k
for i in range(k):
    l[i],r[i]=map(int,input().split())

for i in range(2,n+1):
    for j in range(k):
        li = i - r[j]
        ri = i - l[j]
        if ri <= 0:
            continue
        # li = max(1,li)
        step[i] += stepsum[ri] - stepsum[max(0,li-1)]
        # step[i] %= mod
        # print(step)
    stepsum[i] = ( stepsum[i-1] + step[i] )%mod


print(step[n]%mod)