class Node:
    def __init__(self,v):
        self.v = v
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
    def push(self,v):
        n = Node(v)
        n.next = self.head
        self.head = n
    def pop(self):
        if self.head == None:
            return None
        n = self.head
        self.head = self.head.next
        return n.v

ops = raw_input().split(' ')

s = Stack()
for op in ops:
    if op == '+':
        a = s.pop()
        b = s.pop()
        s.push(a+b)
    elif op == '-':
        a = s.pop()
        b = s.pop()
        s.push(b-a)
    elif op == '*':
        a = s.pop()
        b = s.pop()
        s.push(a*b)
    else:
        num = int(op)
        s.push(num)

print s.pop()