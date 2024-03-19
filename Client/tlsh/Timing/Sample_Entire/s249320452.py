from collections import deque

slope = input()
down_slope   = deque()
total_slopes = deque()

for i in range(len(slope)):
    if slope[i] == '\\':
        down_slope.append(i)
    elif slope[i] == '/':
        area = 0
        if len(down_slope) > 0:
            while len(total_slopes) > 0 and total_slopes[-1][0] > down_slope[-1]:
                area += total_slopes[-1][1]
                total_slopes.pop()
            area += i-down_slope[-1]
            total_slopes.append([down_slope[-1],area])
            down_slope.pop()

if len(total_slopes) > 0:
    total_slopes = [i[1] for i in total_slopes]
    print(sum(total_slopes))
    print(len(total_slopes),end=' ')
    print(' '.join(map(str,total_slopes)))
else:
    print(0)
    print(0)
