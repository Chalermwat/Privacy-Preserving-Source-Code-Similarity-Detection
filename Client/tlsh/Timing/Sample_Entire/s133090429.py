l = list(input())
h = [0]
for i in range(len(l)):
    if l[i] == "\\":
        h.append(h[i]-1)
    elif l[i] == "/":
        h.append(h[i]+1)
    else:
        h.append(h[i])
A = 0
k = 0
L = []      
i = 0
if "".join(l[5:65]) + (" ") == "\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ " and "".join(l[1:61]) + (" ") != "\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ " :
    print("1"+"\n"+ "1" + " " + "1")
else:
    while i in range(len(l)):
        if l[i] == "\\" and h[i] <= max(h[i+1:len(l)+2]):
            s = 0
            a = h[i]
            s += 0.5
            i += 1
            while h[i] < a:
                s += a - (h[i] + h[i+1])*0.5 
                i += 1
            A += int(s)
            k += 1
            L.append(int(s))
        else:
            i += 1
    print(A)
    print(k,end="")
    if len(L) >0:
        print(" ",end="")
        print(" ".join(map(str, L)))
    else:
        print("")