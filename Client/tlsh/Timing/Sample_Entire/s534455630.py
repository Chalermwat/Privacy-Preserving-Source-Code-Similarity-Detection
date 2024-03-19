s=input()
stack_all=[]
stack_A=[]
point=0
#stack_allで全体の面積をはじめに求める
for i,j in enumerate(s):
    if j=="\\":
        stack_all.append(i)
    elif j=="/":
        try:
            left=stack_all.pop()
            po=i-left
            point +=po
            stack_A.append([left,po])
        except:continue
print(point)

#stack_Aに水が溜まっていくのをスタックしておく
#この過程で数字の小さいものは大きいものの上にきていることがわかるから重ねていく
stack_A.insert(0,[-1,-1])
stack_B=[]
if len(stack_A)==1:print(0)
else:
    for i in range(len(stack_A)-1,-1,-1):
        x,y=stack_A[i]
        px,py=stack_A[i-1]
        if x<px:
            stack_A[i-1]=[x,y+py]
        else:
            stack_B.append(stack_A[i])
    print(len(stack_B),*[j for i,j in stack_B[::-1]])
