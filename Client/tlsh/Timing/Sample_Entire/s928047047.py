sum = 0
stack  = []
stack2 = []

str_inpt = input()

for i in range(len(str_inpt)):
  if str_inpt[i] == '\\':
    stack.append(i)
  elif str_inpt[i] == '/':
    if len(stack) < 1: continue
    pop_index = stack.pop(-1)
    area = i - pop_index
    sum += area
    while True:
      if len(stack2) < 1: break
      if stack2[-1][0] < pop_index: break
      if pop_index < stack2[-1][0]:
        pop_stack2 = stack2.pop(-1)
        area += pop_stack2[-1]

    stack2.append([pop_index, area])

print(sum)

if len(stack2) == 0:
  print('0')
else:
  print(str(len(stack2)) + ' ' + ' '.join([str(e[1]) for e in stack2]))
