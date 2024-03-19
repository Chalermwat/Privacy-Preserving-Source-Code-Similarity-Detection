import sys


Stack = []
MAX = 1000

def push(x):
    #if isFull():
    #    print "ERROR!"
    #    sys.exit()
    Stack.append(x)

def pop():
    #if isEmpty():
    #    print "ERROR!"
    #    sys.exit()
    Stack.pop(-1)

def cul(exp):
    for v in exp:
        if v == "+":
            x = reduce(lambda a,b:int(a)+int(b), Stack[-2:])
            for i in range(2):
                pop()
            push(x)
        elif v == "-":
            x = reduce(lambda a,b:int(a)-int(b), Stack[-2:])
            for i in range(2):
                pop()
            push(x)
        elif v == "*":
            x = reduce(lambda a,b:int(a)*int(b), Stack[-2:])
            for i in range(2):
                pop()
            push(x)
        else:
            push(v)

    return Stack[0]

if __name__ == "__main__":
    exp = sys.stdin.read().strip().split(" ")
    ans = cul(exp)
    print ans