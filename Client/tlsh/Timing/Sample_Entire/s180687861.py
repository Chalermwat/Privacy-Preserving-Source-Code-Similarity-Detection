def min(a,b,c):
    if a<b and a<c:
        return a
    elif b<c:
        return b
    else:
        return c


def calc(x):
    try:
        a=x.index("+")
    except:
        a=300
    try:
        b=x.index("-")
    except:
        b=300
    try:
        c=x.index("*")
    except:
        c=300

    ind=min(a,b,c)

    if ind==300:
        return x[0]
    
    if x[ind]=="+":
        x.insert(ind-2,int(x[ind-2])+int(x[ind-1]))
    elif x[ind]=="-":
        x.insert(ind-2,int(x[ind-2])-int(x[ind-1]))
    else:
        x.insert(ind-2,int(x[ind-2])*int(x[ind-1]))
    x.pop(ind-1)
    x.pop(ind-1)
    x.pop(ind-1)
    return calc(x)


operas=input().split(" ")
print (calc(operas))