total_stack = []
single_stack = []

def main():
    input_line = input()
    total = 0

    for i,s in enumerate(input_line):
        if s == "\\":
            total_stack.append(i)
        elif s == "/" and len(total_stack) != 0:
            a = total_stack.pop()
            total += i - a
            area = 0
            while len(single_stack) != 0 and a < single_stack[-1][0]:
                area += single_stack.pop()[1]
            single_stack.append([a, area + i - a])

    print(total)
    print(' '.join([str(len(single_stack))] + [str(i[1]) for i in single_stack]))

if __name__ == '__main__':
    main()
