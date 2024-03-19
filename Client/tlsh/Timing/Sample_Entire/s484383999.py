# coding: utf-8
# Your code here!

x = input()
lst = list(x)
pt = []
rst = []
k = 0

# point get
cnt = 0
tmp = ""
for s in lst:
    if s == "/":
        if tmp == "_" or tmp == "/":
            cnt += 1
    elif s == "\\":
        if tmp == "\\":
            cnt -= 1
    else:
        if tmp == "\\":
            cnt -= 1

    pt += [cnt]
    tmp = s

#メンセキ
i,xs,m2 = 0,0,0
for s in lst:
    if s == "/":
        if i == xs and xs > 0:
            rst += [m2]
            k += 1
            xs,m2 = 0,0
    elif s == "_":
        pass
    else:
        try:
            x = pt[i+1:].index(pt[i])+i+1
            m2 += x-i
            if xs < x:
                xs = x
        except:
            pass
    i += 1
           
print(sum(rst))
print(k,*rst)

