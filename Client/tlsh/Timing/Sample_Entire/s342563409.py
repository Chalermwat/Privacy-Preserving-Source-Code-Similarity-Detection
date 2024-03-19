class Stack():
    def __init__(self):
        self.stack = [0 for _ in range(200)]
        self.top = 0

    def isEmpty(self):
        return self.top == 0

    def isFull(self):
        return self.top >= len(self.stack) - 1

    def push(self, x):
        if self.isFull():
            print "error"
            return exit()
        self.top += 1
        self.stack[self.top] = x

    def pop(self):
        if self.isEmpty():
            print "error"
            return exit()
        a = self.stack[self.top]
        del self.stack[self.top]
        self.top -= 1
        return a

    def lol(self):
        return self.stack[self.top]

def main():
    st = Stack()
    data = raw_input().split()
    for i in data:
        if i == '+':
            b = int(st.pop())
            a = int(st.pop())
            st.push(a + b)
        elif i == '-':
            b = int(st.pop())
            a = int(st.pop())
            st.push(a - b)
        elif i == '*':
            b = int(st.pop())
            a = int(st.pop())
            st.push(a * b)
        else:
            st.push(i)
    print st.lol()

if __name__ == '__main__':
    main()