class MyStack(object):
    """stack class

    Attributes:
        stack: stack
    """

    def __init__(self):
        self.stack = []

    def pop(self):
        """pop method

        Returns:
            popped object
        """
        return self.stack.pop()

    def push(self, value):
        """ push method
        Args:
            value: value to be pushed
        """
        self.stack.append(value)


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