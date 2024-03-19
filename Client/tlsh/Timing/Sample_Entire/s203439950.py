def bubble(x):
    x = x + []
    n = len(x)
    for i in range(n):
        for j in range(i+1,n)[::-1]:
            if x[j] % 10 < x[j-1] % 10:
                x[j], x[j-1] = x[j-1], x[j]
    return x

def selection(x):
    x = x + []
    n = len(x)
    for i in range(n):
        mini = i
        for j in range(i, n):
            if x[j] % 10 < x[mini] % 10:
                mini = j
        if i != mini:
            x[i], x[mini] = x[mini], x[i]
    return x
    
def order(x):
    y = []
    for i in range(1,9):
        y.extend([e for e in x if e % 10 == i])
    return y

def output(x):
    for e in x:
        print 'SHDC'[e/10]+str(e % 10),
    print

def check(x, y):
    output(x)
    if y == order(x): 
        print 'Stable'
    else:
        print 'Not stable'
    return

n = input()
x = []
for s in raw_input().split():
    x.append('SHDC'.index(s[0])*10 + int(s[1]))
x0 = order(x)
check(bubble(x), x0)
check(selection(x), x0)