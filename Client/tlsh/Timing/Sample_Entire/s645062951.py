def isop(s):
    if s == "+" or s == "-" or s == "*":
        return True
    return False


def main():
    line = list(input().split())
    stack = []
    while len(line) > 0:
        tmp = line.pop()
        if isop(tmp):
            stack.append(tmp)
        else:
            stack.append(int(tmp))
        while len(stack) > 2 and isop(stack[-1]) == False and isop(stack[-2]) == False:
            num1 = stack.pop(-1)
            num2 = stack.pop(-1)
            op = stack.pop(-1)
            if op == "+":
                stack.append(num1 + num2)
            elif op == "-":
                stack.append(num1 - num2)
            else:
                stack.append(num1 * num2)

    print(*stack)


if __name__ == '__main__':
    main()
