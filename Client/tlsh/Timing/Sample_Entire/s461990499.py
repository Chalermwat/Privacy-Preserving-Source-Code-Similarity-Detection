import collections

S1 = collections.deque()
s_a = 0

S2 = collections.deque()

for i, j in enumerate(input()):
    if j == '\\':
        S1.append(i)
    elif j == '/':
        if S1:
            left_edge = S1.pop()
            diff = i - left_edge
            s_a += diff
            new_puddle_a = diff
            while True:
                if S2:
                    if S2[-1][0] > left_edge:
                        new_puddle_a += S2[-1][1]
                        S2.pop()
                    else:
                        break
                else:
                    break
            new_puddle = (left_edge, new_puddle_a)
            S2.append(new_puddle)
        else:
            pass


print(s_a)

num_of_puddles = len(S2)
puddles = str(num_of_puddles)

for i in range(num_of_puddles):
    puddle = S2.popleft()
    puddles += ' {0}'.format(str(puddle[1]))
else:
    print(puddles)