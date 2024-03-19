n=int(raw_input())
r=raw_input().split()

def BubbleSort(c, n):
    for i in range(n):
        for j in range(n-1, i, -1):
            if int(c[j][-1]) < int(c[j-1][-1]):
                c[j], c[j-1]=c[j-1],c[j]
    return c

def SelectionSort(c, n):
    for i in range(n):
        m=i
        for j in range(i, n):
            if int(c[j][-1]) < int(c[m][-1]):
                m=j
        c[i],c[m]=c[m],c[i]
    return c

l=list(r)
a=BubbleSort(l, n)
print ' '.join(a)
print 'Stable'
l=list(r)
b=SelectionSort(l, n)
print ' '.join(b)
if a==b:
    print 'Stable'
else:
    print 'Not stable'
