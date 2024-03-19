s=input()
slash=[]
area=0

slash_2=[]
area_2=[]

for i in range(len(s)):
    if s[i]=="\\":
        slash.append(i)
    elif s[i]=="/":
        try: 
            j=slash.pop()
            area=area+i-j
            a=i-j
            while len(area_2) > 0 and slash_2[len(slash_2)-1] >j:
                a=a+area_2[len(slash_2)-1]
                area_2.pop()
                slash_2.pop() 
            slash_2.append(j)     
            area_2.append(a)
        except: pass


if area==0:
    print(0)
    print(0)
else:
    print(area)
    print(str(len(area_2))+" "+" ".join(map(str, area_2)))
