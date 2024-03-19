def is_stable(oline, line):
    for i in range(N):
        for j in range(i+1, N):
            for a in range(N):
                for b in range(a+1, N):
                    if (oline[i][1] == oline[j][1]) & (oline[i] == line[b]) & (oline[j] == line[a]):
                        return False
    return True

N = int(input())
line = input().split()
oline = line.copy()
#BubbleSort
for i in range(N):
    for j in range(N-1, i, -1):
        if int(line[j][1]) < int(line[j-1][1]):
            tmp = line[j]
            line[j] = line[j-1]
            line[j-1] = tmp
print(' '.join(line))
print(('Not stable', 'Stable')[is_stable(oline, line)])

#SelectionSort
line = oline.copy()
for i in range(N):
    minj = i
    for j in range(i+1, N):
        if int(line[minj][1]) > int(line[j][1]):
            minj = j
    tmp = line[i]
    line[i] = line[minj]
    line[minj] = tmp
print(' '.join(line))

print(('Not stable', 'Stable')[is_stable(oline, line)])