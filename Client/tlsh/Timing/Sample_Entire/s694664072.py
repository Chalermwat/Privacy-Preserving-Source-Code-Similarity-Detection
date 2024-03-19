from collections import deque

if __name__ == '__main__':
    x = [(int)(x) if x.isdigit() else x for x in input().split()]
    
    y = deque()

    for tmp in x:
        if tmp == '+':
            a = y.pop()
            b = y.pop()
            y.append(a+b)
        elif tmp == '-':
            a = y.pop()
            b = y.pop()
            y.append(b-a)
        elif tmp == '*':
            a = y.pop()
            b = y.pop()
            y.append(a*b)
        elif tmp == '/':
            a = y.pop()
            b = y.pop()
            y.append(b//a)
        else:
            y.append(tmp)

    print(y.pop())