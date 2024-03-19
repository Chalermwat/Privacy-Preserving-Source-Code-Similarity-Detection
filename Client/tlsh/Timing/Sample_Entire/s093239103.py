# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_3_A
# Stack
# Result:
import sys

class Stack:
    def __init__(self):
        self.store = []

    def push(self, item):
        self.store.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.store.pop()

    def is_empty(self):
        if len(self.store) == 0:
            return True
        else:
            return False

    def __str__(self):
        """Show top to bottom"""
        val = ''
        for e in reversed(self.store):
            val += str(e) + ' '
        return val

def calculate(stack, func):
    v2 = stack.pop()
    v1 = stack.pop()
    return func(v1, v2)

items = sys.stdin.readline().rstrip().split(' ')
stack = Stack()

for e in items:
    if e == '+':
        v = calculate(stack, lambda v1, v2: v1 + v2)
    elif e == '-':
        v = calculate(stack, lambda v1, v2: v1 - v2)
    elif e == '*':
        v = calculate(stack, lambda v1, v2: v1 * v2)
    else:
        # numbers
        v = int(e)
    stack.push(v)

print stack.pop()