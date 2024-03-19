s = input()

sum = 0
process_stack = []
puddle_stack = []

length = len(s)

for i in range(length):
    if s[i] == "\\":
        process_stack.append(i)
    elif s[i] == "/":
        if process_stack:
            edge = process_stack.pop()
            sum += i - edge
            puddle_sum = 0
            while puddle_stack:
                if puddle_stack[len(puddle_stack) - 1][0] < edge:
                    break;
                puddle_sum += puddle_stack.pop()[1]
            puddle_stack.append((edge, puddle_sum + i - edge))

print(sum)

result_string = ""
puddle_num = len(puddle_stack)
result_string += str(puddle_num)
for i in range(len(puddle_stack)):
    result_string += " "
    result_string += str(puddle_stack.pop(0)[1])

print(result_string)
