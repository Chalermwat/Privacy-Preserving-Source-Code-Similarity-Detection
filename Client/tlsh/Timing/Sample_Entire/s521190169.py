def BubbleSort(A):
    #tot = 0
    flag = 1
    N = len(A)
    
    while flag:
        flag = 0
        for j in xrange(N-1,0,-1):
            if A[j][1] < A[j-1][1]:
                A[j],A[j-1] = A[j-1],A[j]
                flag = 1
                #tot += 1
    return A #,tot

def SelectionSort(A): 
    N = len(A)
    m = 0
    for i in range(N):
        minj = i
        for j in range(i,N):
            if A[j][1] < A[minj][1]:
                minj = j
        A[i],A[minj] = A[minj],A[i]
        if i != minj:
            m += 1
    return A

    
N = int(raw_input())
ls = raw_input().split()

tmp = BubbleSort(list(ls))
print ' '.join(map(str,tmp))
print 'Stable'

tmp2 = SelectionSort(list(ls))
print ' '.join(map(str,tmp2))
for k,j in zip(tmp,tmp2):
    if k != j:
        print 'Not stable'
        break
else:
    print 'Stable'