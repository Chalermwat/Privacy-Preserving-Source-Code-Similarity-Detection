import sys


Stack = []

def push(x):
    Stack.append(x)

def pop():
    Stack.pop(-1)


def cul(exp):
    for val in exp:
        if val in ["+", "-", "*"]:
            a = int(Stack[-2])
            b = int(Stack[-1])
            if val == "+":
                x = a + b
            elif val == "-":
                x = a - b
            elif val == "*":
                x = a * b
            for i in range(2):
                pop()
            push(x)
        else:
            push(val)

    return Stack[0]


if __name__ == "__main__":
    exp = sys.stdin.read().strip().split(" ")
    ans = cul(exp)
    print ans