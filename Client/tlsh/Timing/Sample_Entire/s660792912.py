# -*- coding: utf-8 -*-

import sys

I = list(input())

A = 0
L = []
LH = []
k = 0
while len(I) > 0:
    i = I.pop()

    if i == '/':
        d = 1
        a = 0.5
        tmp_I = ['/']

        # print("[{}] d: {}".format(i, d))

        while len(I) > 0:
            i = I.pop()

            tmp_I.append(i)

            if i == '/':
                d += 1
                a += 0.5 + d - 1
            elif i == '\\':
                a += 0.5 + d - 1
                d -= 1
                if d == 0:
                    A += a
                    L.append(a)
                    k += 1
                    tmp_I = []
                    break
            elif i == '_':
                a += d

            # print("[{}] d: {}".format(i, d))

        # print("{}".format(tmp_I))

        if len(tmp_I) > 0:
            d = a = 0
            while len(tmp_I) > 0:
                i = tmp_I.pop()
                # print("{}".format(i))
                if i == '\\':
                    d += 1
                    a += 0.5 + d - 1
                elif i == '_':
                    a += d
                elif i == '/' and d > 0:
                    a += 0.5 + d - 1
                    d -= 1

                    if d == 0:
                        # print("Add tmp: {} ({})".format(a, tmp_I))
                        A += a
                        LH.append(a)
                        k += 1
                        a = 0

print(int(A))
sys.stdout.write(str(k))
for l in LH:
    sys.stdout.write(" {}".format(int(l)))
while len(L) > 0:
    sys.stdout.write(" {}".format(int(L.pop())))
sys.stdout.write('\n')