def bubble_sort(a):
    n = len(a)
    for j in range(n):
        m = n-1-j # n-1 to 0
        for i in range(m):
            if a[i][1] > a[i+1][1]:
                a[i],a[i+1] = a[i+1],a[i]
    return a


def selection_sort(a):
    MAXINT = 10
    n = len(a)
    for j in range(n):
        minv = MAXINT
        minp = -1
        for i in range(j,n):
            if int(a[i][1]) < minv:
                minv = int(a[i][1])
                minp = i
        a[minp],a[j]=a[j],a[minp]
    return a

def stable(a,f):
    b = f(a[:])
    print ' '.join(b)
    p = 1
    while p < 10:
        c = []
        d = []
        for i in range(len(a)):
            if a[i][1] == str(p):
                c.append(a[i])
            if b[i][1] == str(p):
                d.append(b[i])
        for i in range(len(c)):
            if c[i] != d[i]:
                print "Not stable"
                return
        p += 1
    print "Stable"

n = int(raw_input())
cards = raw_input().split(' ')

stable(cards[:],bubble_sort)
stable(cards[:],selection_sort)