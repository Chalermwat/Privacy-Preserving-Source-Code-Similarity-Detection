inpu = input()
back = list(r"\\")[0]

stack = []
area = 0
area_sub = []
for i,symbol in enumerate(inpu):
    if symbol == back:
        stack.append(i)
        #print(back)
    elif symbol == "/":
        #print(symbol)
        if len(stack)>0:
            a = stack.pop()
            area += i-a
            
            area2 = 0
            while len(area_sub) and a<area_sub[-1][0]:
                pre = area_sub.pop()
                area2 += pre[1]
            area2 += i-a 
            area_sub.append([a,area2])
print(area)

#print(" ".join(a for a in area_sub))
if len(area_sub) > 0: 
    print(len(area_sub), end=" ")
    ar = [a[1] for a in area_sub]
    print(*ar)
else:
    print(len(area_sub))
