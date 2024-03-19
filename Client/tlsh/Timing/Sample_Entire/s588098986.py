def RPN(states):

        operator = {
           '+' :(lambda x, y: x + y),
           '-' :(lambda x, y: x - y),
           '*' :(lambda x, y: x * y),
           '/' :(lambda x, y: float(x)/y)
        }
        stack = []
        for index, z in enumerate(states):
                if z not in operator.keys ():
                        stack.append(int(z))
                        continue
                y = stack.pop()
                x = stack.pop()
                stack.append(operator[z](x,y))
        print (stack[0])
        return (stack[0])

if __name__ == '__main__':
        import sys
        RPN(input().split(" "))