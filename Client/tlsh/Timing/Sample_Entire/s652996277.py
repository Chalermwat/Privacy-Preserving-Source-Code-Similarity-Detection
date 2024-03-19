# stack
class stack(object):
    def __init__(self):
        self.container = [] # Empty Stack
        self.topIndex = -1
    def push(self, elem):
        self.container.append(elem)
        self.topIndex += 1
    def pop(self):
        if self.topIndex > -1:
            elem = self.container[self.topIndex]
            del self.container[self.topIndex]
            self.topIndex -= 1
            return elem
        else:
            return None

def calc(ins):
    stk = stack()
    try:
        for sin in ins:
            if sin == '+':
                stk.push(stk.pop() + stk.pop())
            elif sin == '-':
                a, b = stk.pop(), stk.pop()
                stk.push(b - a)
            elif sin == '*':
                stk.push(stk.pop() * stk.pop())
            elif sin == '/':
                a, b = stk.pop(), stk.pop()
                stk.push(b / a)
            else:
                stk.push(int(sin))
        return stk.pop()
    except:
        print 'Bad Expr'

print calc(raw_input().split(' '))