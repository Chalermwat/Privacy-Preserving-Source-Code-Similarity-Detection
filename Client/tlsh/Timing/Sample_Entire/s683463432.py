if __name__ == '__main__':
    s1 = []
    s2 = []

    data = input()
    total_sum = 0
    for i in range(len(data)):
        if data[i] == '\\':
            s1.append(i)
        elif data[i] == '/' and len(s1) > 0:
            j = s1.pop()
            a = i - j
            total_sum += a

            while (len(s2) and s2[-1][0] > j):
                temp = s2.pop()
                a += temp[1]
            s2.append([j, a])

    print(total_sum)
    length = len(s2)
    if not length:
        print(length)
    else:
        print(length, end=' ')
    for i in range(0, length):
        endl = ' '
        if i == length - 1:
            endl = '\n'
        print(s2[i][1], end=endl)


