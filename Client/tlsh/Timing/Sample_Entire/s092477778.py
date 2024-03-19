class Stack():
    def __init__(self):
        self.stack = [0 for _ in range(1000)]
        self.top = 0

    def push(self, n):
        self.top += 1
        self.stack[self.top] = n

    def pop(self):
        a = self.stack[self.top]
        del self.stack[self.top]
        self.top -= 1
        return a

    def lol(self):
        return self.stack[self.top]


def main():
    input_data = raw_input()
    data = input_data.strip().split(" ")
    st = Stack()
    for l in data:
        if l == "+":
            a = st.pop()
            b = st.pop()
            st.push(a + b)

        elif l == "-":
            a = st.pop()
            b = st.pop()
            st.push(b - a)

        elif l == "*":
            a = st.pop()
            b = st.pop()
            st.push(a * b)

        else:
            st.push(int(l))

    print st.lol()


if __name__ == '__main__':
    main()