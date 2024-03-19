x = input()
S1 = []
S2 = []
current_position = 0
total_area = 0

for i in x:
    if i == '\\':
        S1.append(current_position)

    elif i == '/':
        try:
            start_position = S1.pop()
            distance = current_position - start_position
            total_area += distance
            S2.append([start_position, distance])

        except:
            continue

    current_position += 1

print(total_area)

S2.insert(0, [-1, -1])
S3 = []
if len(S2) == 1:print(0)
else:
    for i in range(len(S2)-1, -1, -1):
        x, y = S2[i]
        px, py = S2[i-1]
        if x < px:
            S2[i-1] = [x, y + py]
        else:
            S3.append(S2[i])

    print(len(S3), *[j for i, j in S3[::-1]])
