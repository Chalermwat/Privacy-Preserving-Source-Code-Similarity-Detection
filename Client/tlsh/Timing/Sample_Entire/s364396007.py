class Stack:
    def __init__(self):
        self.values = []
        self.n = 0

    def pop(self):
        if self.n == 0:
            raise Exception("stack underflow")
        else:
            v = self.values[-1]
            del self.values[-1]
            self.n -= 1
            return v

    def push(self,x):
        self.values.append(x)
        self.n += 1


operators = set(['+', '-', '*'])
stack = Stack()

for op in raw_input().split(' '):
    if op in operators:
        b = stack.pop()
        a = stack.pop()
        if op == '+':
            stack.push(a+b)
        elif op == '-':
            stack.push(a-b)
        elif op == '*':
            stack.push(a*b)
        else:
            raise Exception("Unkown operator")
    else:
        stack.push(int(op))

print stack.pop()