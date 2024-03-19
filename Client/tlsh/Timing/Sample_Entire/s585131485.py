from copy import deepcopy as copy
n=int(input())
A=input().split()
C=copy(A)
for i in range(n):
  for j in range(n-1,i,-1):
    if C[j][1] < C[j-1][1]:
      k=C[j]
      C[j]=C[j-1]
      C[j-1]=k
print(*C)
for i in range(n-1):
  if C[i][1]==C[i+1][1] and A.index(C[i])>A.index(C[i+1]):
    print('Not stable')
    break
else:print('Stable')
C=copy(A)
for i in range(n):
  minj = i
  for j in range(i,n):
    if C[j][1] < C[minj][1]:
      minj = j
  k=C[i]
  C[i]=C[minj]
  C[minj]=k
print(*C)
for i in range(n-1):
  if C[i][1]==C[i+1][1] and A.index(C[i])>A.index(C[i+1]):
    print('Not stable')
    break
else:print('Stable')
