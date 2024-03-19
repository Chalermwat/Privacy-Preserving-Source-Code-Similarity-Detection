# coding=utf-8

S1 = []
S2 = []
total_square = 0
j = 0

input = list(input())

for i, val in enumerate(input):
    sq = 0
    if val == '\\':
        S1.append(i)
    elif val == '/':
        if len(S1) > 0:
            j = S1.pop()
            total_square += (i - j)
            if len(S2) > 0:
                if (S2[-1][0] > j):
                    while (S2[-1][0] > j):
                        poped = S2.pop()
                        sq += poped[1]
                        if len(S2) == 0:
                            break
                    S2.append([j, sq + (i-j)])
                else:
                    S2.append([j, (i-j)])
            else:
                S2.append([j, i-j])

print(total_square)
print(len(S2), end = "")
for data in S2:
    print(' ' + str(data[1]), end = "")
print()