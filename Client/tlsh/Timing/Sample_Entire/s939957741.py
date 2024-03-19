x = input()
y = []
z = []
n = 0
for i in range(len(x)):
    if x[i] == '\\':
        if n:
            y.append(n)
            n = 0
            if z:
                z.append(-1)
        z.append(i)
    elif x[i] == '/':
        if z:
            while True:
                p = z.pop()
                if p == -1:
                    n += y.pop()
                else:
                    break
            n += i-p
    else:
        pass
if n:
    y.append(n)
for j in range(y.count(0)):
    y.remove(0)
print(sum(y))
print(len(y), *y)


