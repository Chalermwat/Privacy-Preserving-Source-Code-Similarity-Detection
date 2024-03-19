from collections import deque


def main():
    stack = deque()
    diagram = input()
    square = []

    for index, value in enumerate(diagram):
        if value == '\\':
            stack.append(-index)
        elif value == '/':
            if len(stack) > 0:
                tmp = []
                while True:
                    tmp.append(stack.pop())
                    if tmp[-1] <= 0:
                        stack.append(sum(tmp[:-1]) + index + tmp[-1])
                        break
                if len(stack) == 1:
                    square.append(stack.pop())
    square.extend([i for i in stack if i > 0])

    print(sum(square))
    if sum(square) == 0:
        print(0)
    else:
        print('{} {}'.format(len(square), ' '.join([str(i) for i in square])))


if __name__ == '__main__':
    main()

