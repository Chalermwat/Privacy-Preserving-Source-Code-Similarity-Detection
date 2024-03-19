def doc_string():
    """
    I can fly.
    """

list = []
stack = []
if __name__ == "__main__":
    list = raw_input().split()

    for var in list:
        try:
            stack.append(int(var))
        except:
            if var == "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(b + a)
            if var == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            if var == "*":
                a = stack.pop()
                b = stack.pop()
                stack.append(b * a)

    print stack.pop()