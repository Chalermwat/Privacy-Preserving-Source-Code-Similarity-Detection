lines = input()
stack_1 = []
stack_2 = []

area = 0
for i, line in enumerate(lines):
    if line == '\\':
        stack_1.append(i)
    elif line == '_':
        pass
    elif line == '/':
        if stack_1 == []:
            continue
        last_index = stack_1.pop()
        this_area = i - last_index
        area += this_area

        if stack_2 == []:
            stack_2.append((last_index, this_area))
            continue

        block_area = this_area
        while True:
            if stack_2 == []:
                break
            stack_2_index, stack_2_area = stack_2.pop()
            if stack_2_index < last_index:
                stack_2.append((stack_2_index, stack_2_area))
                break
            else:
                block_area += stack_2_area
        stack_2.append((last_index, block_area))

print(area)
kazu = len(stack_2)
kaku_menseki = [stack_2[i][1] for i in range(len(stack_2))]
kaku_menseki_out = ' '.join(map(str, kaku_menseki))
if kazu > 0:
    print(f'{kazu} {kaku_menseki_out}')
else:
    print(f'{kazu}')

