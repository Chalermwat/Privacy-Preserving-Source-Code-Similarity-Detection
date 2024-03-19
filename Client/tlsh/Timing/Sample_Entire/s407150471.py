import sys
a = list(input().split())
stack = []
for i in range(len(a)):
    n = len(stack)
    if a[i] == '+':
        if (n-2) <0:
            sys.exit("スタックアンダーフロー")
        tmp = int(stack.pop(n-1)) + int(stack.pop(n-2))
        stack.append(tmp)
        
    elif a[i] == '-':
        if (n-2) <0:
            sys.exit("スタックアンダーフロー")
        tmp_1 = int(stack.pop(n-1))
        tmp_2 = int(stack.pop(n-2))
        tmp = tmp_2 - tmp_1
        stack.append(tmp)
        
    elif a[i] == '*':
        if (n-2) <0:
            sys.exit("スタックアンダーフロー")
        tmp = int(stack.pop(n-1)) * int(stack.pop(n-2))
        stack.append(tmp)
        
    elif a[i] == '/':
        if (n-2) <0:
            sys.exit("スタックアンダーフロー")
        tmp_1 = int(stack.pop(n-1))
        tmp_2 = int(stack.pop(n-2))
        tmp = tmp_2 / tmp_1
        stack.append(tmp)
    else:
        stack.append(int(a[i]))
print(stack[0])
