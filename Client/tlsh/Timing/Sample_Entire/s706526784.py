def calc(formura):
    if formura[-1] == '+':
        return int(formura[-3]) + int(formura[-2])
    elif formura[-1] == '-':
        return int(formura[-3]) - int(formura[-2])
    elif formura[-1] == '*':
        return int(formura[-3]) * int(formura[-2])
    elif formura[len(formura)-1] == '/':
        return int(formura[-3]) / int(formura[-2])


formura = [i for i in input().split()]
stack = []

for i in range(len(formura)):
    if formura[i] == '+' or formura[i] == '-' or formura[i] == '*' or formura[i] == '-':
        stack.append(formura[i])
        result = calc(stack)
        for j in range(3):
            stack.pop(-1)
        stack.append(result)
    else:
        stack.append(formura[i])

print(stack[0])