def Main():
    cross = input().replace("\n", "")

    S = list()
    V = list()
    ans = list()

    for i in range(len(cross)):
        r = cross[i]

        if r == "\\":
            S.append(i)
        elif r == "/":
            if len(S) > 0:
                j = S.pop()
                v = i - j
                V.append([v, j])

    while len(V) > 0 :
        total = 0
        [v, j] = V.pop()
        total += v

        while True:
            if len(V) > 0:
                [vv, jj] = V.pop()

                if jj > j:
                    total += vv
                else:
                    V.append([vv, jj])
                    ans.append(total)
                    break
            else:
                ans.append(total)
                break

    print("{}".format(sum(ans)))
    print(len(ans), *reversed(ans))

Main()
