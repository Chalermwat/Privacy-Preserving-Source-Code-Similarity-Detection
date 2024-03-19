def main():
    from collections import deque
    from operator import itemgetter

    s = input()

    tot = 0
    areas = []

    dq = deque()
    for i, c in enumerate(s):
        # print(c, end='')

        if c == '\\':
            dq.append(i)
        elif c == '/':
            if dq:
                j = dq.pop()
                a = i - j
                tot += a

                while areas and areas[-1][0] > j:
                    a += areas.pop()[1]
                areas.append((i, a))

    print(tot)
    print(len(areas), *map(itemgetter(1), areas))


if __name__ == '__main__':
    main()

