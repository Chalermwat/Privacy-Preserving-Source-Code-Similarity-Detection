"RPN using stack for AOJ ALDS1_3_A: Stack"

# coding: utf-8


def rpn(exp):
    """
    rpn calculation
    >>> rpn(['1', '2', '+', '3', '4', '-', '*'])
    -3
    """

    stack = []
    for elem in exp:
        if elem == '+':
            stack.append(int(stack.pop()) + int(stack.pop()))
        elif elem == '-':
            stack.append(-int(stack.pop()) + int(stack.pop()))
        elif elem == '*':
            stack.append(int(stack.pop()) * int(stack.pop()))
        elif elem == '/':
            stack.append(int(stack.pop()) / int(stack.pop()))
        else:
            stack.append(elem)

    print(stack.pop())


def main():
    "main function"

    exp = list(input().split(' '))
    rpn(exp)

if __name__ == '__main__':
    # import doctest
    # doctest.testmod()

    main()