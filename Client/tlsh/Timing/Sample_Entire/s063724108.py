input_str = input().split(' ')

stack = []

left_num, right_num = 0, 0
for tmp_str in input_str:
    if tmp_str == '+':
        right_num = stack.pop()
        left_num = stack.pop()
        stack.append(left_num + right_num)

    elif tmp_str == '-':
        right_num = stack.pop()
        left_num = stack.pop()
        stack.append(left_num - right_num)

    elif tmp_str == '*':
        right_num = stack.pop()
        left_num = stack.pop()
        stack.append(left_num * right_num)

    elif tmp_str == '/':
        right_num = stack.pop()
        left_num = stack.pop()
        stack.append(left_num / right_num)

    else:
        stack.append(int(tmp_str))

print(stack.pop())
