# coding: utf-8

def areas_calc(strings):
    stack1 = []
    stack2 = []
    total_m = 0
    for i, s in enumerate(strings):
        if s == "\\":
            stack1.append(i)
        elif s == "_":
            continue
        elif s == '/':
            if len(stack1) > 0:
                previous_i = stack1.pop()
                m = i - previous_i
                total_m += m

                while len(stack2) > 0:
                    stacked_i, stacked_m = stack2.pop()
                    if previous_i < stacked_i:
                        m += stacked_m
                    else:
                        stack2.append((stacked_i, stacked_m))
                        stack2.append((previous_i, m))
                        break

                else:
                    stack2.append((previous_i, m))
    print(total_m)
    k = len(stack2)
    for_output = [str(k)] + [str(m) for i, m in stack2]
    print(' '.join(for_output))
    

if __name__ == "__main__":
    areas_calc(input())

