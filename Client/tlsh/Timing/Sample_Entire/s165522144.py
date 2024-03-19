s=input()


#\\///\_/\/\\\\/_/\\///__\\\_\\/_\/_/\
    

stack=[]
i=0
result=0
#みずたまりは、[左側の位置と、数量を表す]
mizutamari=[[-1,0]]
for item in s:
    #print(stack,mizutamari)
    if item=="\\":
        stack.append(i)
    elif item=="/":
        if len(stack)>0:
            temp=stack.pop()
            result+=i-temp
            left=mizutamari.pop()
            if left[0]>temp:
                vol=i-temp
                while 1:
                    vol=left[1]+vol
                    mizutamari.append([temp,vol])
                    if len(mizutamari)<=2:
                        break
                    bk=mizutamari.pop()
                    bkbk=mizutamari.pop()
                    if bkbk<bk:
                        mizutamari.append(bkbk)
                        mizutamari.append(bk)
                        break
                    else:
                        left=bkbk




                
            else:
                #print(left[0],"<",temp,":","naze",left,temp)
                mizutamari.append(left)
                mizutamari.append([temp,i-temp])
                #print(mizutamari)


    i+=1
print(result)
s=""
for item in mizutamari[1:]:
    s+=str(item[1])+" "

if result==0:
    print(0)
else:
    print(len(mizutamari)-1,s[:-1])
