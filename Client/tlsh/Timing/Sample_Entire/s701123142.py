
class Stack():
    def __init__(self):
        self.l = []
    
    def push(self, e):
        self.l.append(e)
        
    def pop(self):
        return self.l.pop()

# def isint(s):
#     try: 
#         int(s)
#         return True
#     except ValueError:
#         return False

ope = {"+", "-", "*"}

s = Stack()
exp = input().strip().split()

for e in exp:
    if e in ope:
        if e == '+':
            s.push(s.pop() + s.pop())
        elif e == '-':
            tmp = s.pop()
            s.push(s.pop() - tmp)
        else:
            s.push(s.pop() * s.pop())
    else:
        s.push(int(e))
print(s.pop())