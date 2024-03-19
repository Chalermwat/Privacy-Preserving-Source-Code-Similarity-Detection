class Stack:
    def __init__(self, stack = None):
        if type(stack) is type([]):
            self.stack = stack
            self.top = len(stack)
        else:
            self.stack = []
            self.top = 0
            
    def isEmpty(self):
        return self.top == 0
    
    def isFull(self):
        return self.top >= MAX - 1
            
    def push(self, e):
        if len(self.stack) != (self.top):
            self.stack[self.top] = e
        else:
            self.stack.append(e)
        self.top += 1
           
    def pop(self):
        self.top -= 1
        return self.stack[self.top]

S = input().split(" ")

operators = ["+", "-", "*"]


stack = Stack()
for s in S:
    if s in operators:
        a = stack.pop()
        b = stack.pop()
#         print("%d %s %d"%(a, s, b))
        result = eval("%d %s %d"%(b, s, a))
        stack.push(result)
    else:
        stack.push(int(s))
print (stack.pop())