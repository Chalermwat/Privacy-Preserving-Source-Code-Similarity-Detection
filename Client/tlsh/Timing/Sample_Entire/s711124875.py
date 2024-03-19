
o = list()
top = -1
for s in input().split():
    if s.isdigit():
        o.append(int(s))
        top += 1
    else:
        if s is "+":
            n = o[top]+o[top-1]
            o.pop(top)
            top-=1
            o.pop(top)
            top-=1
            o.append(n)
            top+=1
        if s is "-":
            n = o[top-1] - o[top]
            o.pop(top)
            top -= 1
            o.pop(top)
            top -= 1
            o.append(n)
            top+=1
        if s is "*":
            n = o[top]*o[top-1]
            o.pop(top)
            top -= 1
            o.pop(top)
            top -= 1
            o.append(n)
            top+=1


print(o[0])