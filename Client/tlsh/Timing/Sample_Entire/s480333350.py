g = list(input())

sum, d, r, p = 0, 0, 0, 0
f = 0
lake_list = []

for c in g:
    if c == "\\":
        if f == 0:
            f, d, r = 1, 1, 1
        else:
            d += 1
            r += (1 + (d-1))
    elif c == "_":
        if f == 1:
            r += d
    else:
        if f == 1:
            d -= 1
            r += d
            if d == 0:
                f = 0
                sum += r
                lake_list.append([p, r])
                r = 0
    p += 1

d, r, p = 0, 0, len(g)-1
f = 0
g.reverse()

for c in g:
    if c == "/":
        if f == 0:
            f, d, r = 1, 1, 1
            pr = p
        else:
            d += 1
            r += (1 + (d-1))
    elif c == "_":
        if f == 1:
            r += d
    else:
        if f == 1:
            d -= 1
            r += d
            if d == 0:
                if [pr, r] not in lake_list:
                    sum += r
                    lake_list.append([pr, r])
                f = 0
                r = 0
    p -= 1

lake_list.sort()
print(sum)
print(len(lake_list), end="")
i = 0
while i != len(lake_list):
    print(" {}".format(lake_list[i][1]), end="")
    i += 1
print()

