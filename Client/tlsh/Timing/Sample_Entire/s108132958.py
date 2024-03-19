N = [x for x in input().split(' ')]
#データを格納するための整数型1次元配列
stack = []
for i in N:
    # +が入っていた場合
    if i == '+':
        num1 = stack.pop()
        num2 = stack.pop()
        stack.append(num1 + num2)
    # -が入っていた場合
    elif i == '-':
        num2 = stack.pop()
        num1 = stack.pop()
        stack.append(num1 - num2)
    # *が入っていた場合
    elif i == '*':
        num1 = stack.pop()
        num2 = stack.pop()
        stack.append(num1 * num2)
    #算術演算子( + - *)以外が入っていた場合
    else:
        stack.append(int(i))

#表示
print(stack.pop())
