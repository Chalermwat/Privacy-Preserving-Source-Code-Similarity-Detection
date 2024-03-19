import copy

def stable(origin, new):
    for i in range(n-1):
        if int(new[i][1]) == int(new[i+1][1]):
            if origin.index(new[i]) > origin.index(new[i+1]):
                return False
    return True

n = int(raw_input())
a_origin = raw_input().split()

a = copy.copy(a_origin)
b = copy.copy(a_origin)

# bubble sort
for i in range(n):
    for j in range(n-1, i, -1):
        if int(a[j][1]) < int(a[j-1][1]):
            tmp = a[j]
            a[j] = a[j-1]
            a[j-1] = tmp

for i in range(n):
    if i == n-1:
        print a[i]
    else:
        print a[i], 

if stable(a_origin, a):
    print 'Stable'
else:
    print 'Not stable'

# selection sort
for i in range(n):
    minj = i
    for j in range(i, n):
        if int(b[j][1]) < int(b[minj][1]):
            minj = j
    tmp = b[i]
    b[i] = b[minj]
    b[minj] = tmp

for i in range(n):
    if i == n-1:
        print b[i]
    else:
        print b[i],

if stable(a_origin, b):
    print 'Stable'
else:
    print 'Not stable'