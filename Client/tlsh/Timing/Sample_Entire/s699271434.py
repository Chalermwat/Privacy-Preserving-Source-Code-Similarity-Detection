expr = input().split()
my_stack = []
def push(stack, item):
    return stack.append(item)

def pop(stack):
    return stack[:-1], stack[-1]

for item in expr:
    if item.isdigit():
        push(my_stack, int(item))
    elif item == '+':
        my_stack, a = pop(my_stack)
        my_stack, b = pop(my_stack)
        push(my_stack, a + b)
    elif item == '-':
        # not a - b
        my_stack, a = pop(my_stack)
        my_stack, b = pop(my_stack)
        push(my_stack, b - a)
    elif item == '*':
        my_stack, a = pop(my_stack)
        my_stack, b = pop(my_stack)
        push(my_stack, a * b)

print(my_stack[0])