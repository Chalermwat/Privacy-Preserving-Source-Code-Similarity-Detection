class Stack:
    def __init__(self):
        self.values = []

    def push(self,v):
        self.values.append(v)

    def pop(self):
        if len(self.values) == 0:
            raise
        else:
            v = self.values[len(self.values)-1]
            del self.values[len(self.values)-1]
            return v

symbols = raw_input().split(' ')

stack = Stack()
for s in symbols:
    if not s in ['+', '-', '*']:
        stack.push(s)
    else:
        v1 = int(stack.pop())
        v2 = int(stack.pop())
        if s == '+':
            stack.push(v1+v2)
        elif s == '-':
            stack.push(v2-v1)
        elif s == '*':
            stack.push(v1*v2)

print stack.pop()