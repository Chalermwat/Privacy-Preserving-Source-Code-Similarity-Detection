class Pond:
    def __init__(self, arg_left, arg_area):
        self.left = arg_left
        self.area = arg_area

form = input()
stack = []
stack2 = []
totalArea = 0
for i in range(len(form)):
    #'/'以外なら積む
    tmpForm = form[i]
    if tmpForm == '\\':
        stack.append(i)
    #'/'なら直前の\を探しに行く
    elif tmpForm == '/' and len(stack) > 0:
        xLeft = stack.pop()
        xRight = i
        tmpArea = xRight - xLeft
        totalArea += tmpArea

        #池が連続する場合の処理
        while len(stack2) > 0 and stack2[-1].left > xLeft:
            tmpArea += stack2.pop().area

        stack2.append(Pond(xLeft, tmpArea)) #新たな池を登録

print(totalArea)
ans = []
ans.append(len(stack2))
for pond in stack2:
    ans.append(pond.area)
print(' '.join(map(str, ans)))

