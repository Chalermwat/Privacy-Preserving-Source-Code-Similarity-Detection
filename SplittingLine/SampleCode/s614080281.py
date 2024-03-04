p = 10**9+7
N = int(input())
T = list(map(int,input().split()))
A = list(map(int,input().split()))
H = [0 for _ in range(N)]
flag = 0
if T[N-1]!=A[0]:
    flag = 1
hmax = A[0]
if flag==0:
    indmaxT=0
    H[0] = T[0]
    for i in range(1,N):
        if T[i]>T[i-1]:
            H[i] = T[i]
            if H[i]==hmax:
                indmaxT = i
                break
    indmaxA = N-1
    H[N-1] = A[N-1]
    for i in range(N-2,-1,-1):
        if A[i]>A[i+1]:
            H[i]=A[i]
            if H[i]==hmax:
                indmaxA = i
                break
    if indmaxA<indmaxT:
        flag = 1
if flag==1:
    print(0)
else:
    cnt = 1
    cur = 0
    for i in range(1,indmaxT):
        if H[i]==0:
            cnt = (cnt*H[cur])%p
        elif H[i]>0:
            cur = i
    cur = N-1
    for i in range(N-2,indmaxA,-1):
        if H[i]==0:
            cnt = (cnt*H[cur])%p
        elif H[i]>0:
            cur = i
    for i in range(indmaxT+1,indmaxA):
        cnt = (cnt*hmax)%p
    print(cnt)