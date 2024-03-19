def bubble(A):
    #标记是否需要继续冒泡
    flag =True;
    n=len(A)
    i=0
    while flag:
        flag=False
        for j in range(n-1,i,-1):
           if A[j][1]<A[j-1][1]:
               A[j],A[j-1]=A[j-1],A[j]
               flag=True
        i+=1
 
 
#选择排序法
def selection(A):
    n=len(A)
    for i in range(n):
        minj=i
        for j in range(i,n):
            if A[j][1]<A[minj][1]:
                minj=j
        if i!=minj:
            A[i],A[minj]=A[minj],A[i]
             
   
           
n=int(input())
ss=[x for x in input().split()]     
ss2=ss.copy()
 
 
bubble(ss)
for i in range(len(ss)-1):
    print(ss[i],end=' ')
print(ss[-1])
print('Stable')
    
 
selection(ss2)
for i in range(len(ss2)-1):
    print(ss2[i],end=' ')
print(ss2[-1])
if ss==ss2:
    print('Stable')
else:
    print('Not stable')
