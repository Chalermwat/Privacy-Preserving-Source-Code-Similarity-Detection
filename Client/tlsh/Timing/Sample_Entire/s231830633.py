string = input()

h = 0
A = [h]
for c in string:
    if c == "/": h += 1
    elif c == "\\": h -= 1
    A.append(h)

flg = False
ans1 = []
ans2 = []

forward = True
while len(A) > 1:
    h = 0
    B = [0]

    for i in range(len(A) - 1):
        if not flg: B = [0]

        d = A[i + 1] - A[i]
        if d < 0: flg = True
        h += d

        if h <= 0:
            B.append(h)

            if h == 0:
                if len(B) > 2:
                    if forward: ans1.append(abs(sum(B)))
                    else: ans2.append(abs(sum(B)))
                B = []
                flg = False
        else:
            h = 0

    A = B.copy()
    A.reverse()
    forward = (forward + 1) % 2

ans2.reverse()
ans = ans1 + ans2

print(sum(ans))
print(len(ans), *ans)
