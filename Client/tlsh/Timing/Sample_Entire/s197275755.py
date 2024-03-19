# your code goes here
N=int(input())
Ci=[i for i in input().split()]
C=[]
for i in range(N):
   # print(C)
    C.append([])
    C[i].append(Ci[i][0])
  #  print(C)
    C[i].append(int(Ci[i][1]))
Cb=C
fl=1
#print(Cb)
while fl==1:
    fl=0
    for j in range(N-1):
   #     print(Cb)
        if Cb[N-1-j][1]<Cb[N-2-j][1]:
       #     print(Cb)
            t=Cb[N-1-j]
            Cb[N-1-j]=Cb[N-2-j]
            Cb[N-2-j]=t
            fl=1
        #    print(C)
for i in range(N):
    Cb[i][1]=str(Cb[i][1])
 #   print(Cb)
    Cb[i]="".join(Cb[i])
print(" ".join(Cb))
p="Stable"
print(p)
C=[]
for i in range(N):
 #   print(C)
    C.append([])
    C[i].append(Ci[i][0])
  #  print(C)
    C[i].append(int(Ci[i][1]))
Co=[]
for i in range(N):
    Co.append([])
  #  print(Co)
    Co[i].append(Ci[i][0])
    Co[i].append(int(Ci[i][1]))
for i in range(N-1):
    minj=i
    for j in range(i,N):
    #    print(C)
        if C[j][1]<C[minj][1]:
            minj=j
        elif C[j][1]==C[minj][1]:
            k=0
            while k<N and C[minj][1]!=Co[k][1]:
                k+=1
    #        print (j)
            if k<N and C[minj][0]!=Co[k][0]:
                p="Not stable"
    if i!=minj:
        t=C[i]
        C[i]=C[minj]
        C[minj]=t
   # print(minj)
for i in range(N):
    C[i][1]=str(C[i][1])
    C[i]="".join(C[i])
print(" ".join(C))
print(p)