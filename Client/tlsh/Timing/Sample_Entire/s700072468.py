class MyStack(object):
    """stack class

    Attributes:
        stack: stack
    """

    def __init__(self):
        self.stack = [0] * 1000
        self.top = 0

    def pop(self):
        """pop method

        Returns:
            popped object
        """
        if self.top - 1 < 0:
            print("Stack Underflow")
        else:
            value = self.stack[self.top]
            self.stack[self.top] = 0
            self.top -= 1
            return value

    def push(self, value):
        """ push method
        Args:
            value: value to be pushed
        """
        if self.top + 1 >= len(self.stack):
            print("Stack Overflow")
        else:
            self.top += 1
            self.stack[self.top] = value

sequence = raw_input().split()
operators = {"*": "*", "+": "+", "-": "-"}
stack = MyStack()
for s in sequence:
    if s in operators:
        value2 = stack.pop()
        value1 = stack.pop()
        stack.push(str(eval(value1 + operators[s] + value2)))
    else:
        stack.push(s)

print(stack.pop())