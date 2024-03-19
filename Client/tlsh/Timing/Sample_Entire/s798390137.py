data = [str(i) for i in input().split()]
stack = []


def is_int(num) -> bool:
    try:
        int(num)
    except ValueError:
        return False
    return True


for d in data:
    if is_int(d):
        stack.append(d)
    else:
        if d == '+':
            a = int(stack.pop())
            b = int(stack.pop())
            stack.append(a + b)
        elif d == '-':
            a = int(stack.pop())
            b = int(stack.pop())
            stack.append(b - a)
        elif d == '*':
            a = int(stack.pop())
            b = int(stack.pop())
            stack.append(a * b)
        else:
            raise ValueError('+, -, *以外の演算子が出現。')
print(stack.pop())
