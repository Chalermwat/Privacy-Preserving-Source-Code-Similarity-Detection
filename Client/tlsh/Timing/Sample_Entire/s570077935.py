if __name__ == '__main__':
    from collections import deque
    str = input()
    stack1,stack2 = deque([]),deque([])
    sum = 0

    for i in range(len(str)):
        if str[i] == '\\':
            stack1.append(i)
        elif str[i] == '/':
            if stack1 != deque([]):
                x = stack1.pop()
                stack2.append([x,i-x])

        while len(stack2) >= 2 and stack2[len(stack2) - 2][0] > stack2[len(stack2) - 1][0]:
            a = stack2.pop()
            b = stack2.pop()
            stack2.append([a[0],a[1]+b[1]])

    #全面積算出、出力
    for i in range(len(stack2)):
        sum += stack2[i][1]
    print(sum)
    if len(stack2) > 0:
        print(len(stack2),end = " ")
    else:
        print(len(stack2))
    for i in range(len(stack2)):
        if i == len(stack2) - 1:
            print(stack2[i][1])
        else:
            print(stack2[i][1],end = " ")

