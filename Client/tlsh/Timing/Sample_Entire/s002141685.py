hoge1 = list()
hoge2 = list()
total = 0
for num, c in enumerate(input()):
    if c == '\\':
        hoge1.append(num)
    elif c == '/':
        if not hoge1:
            continue
        last_index = hoge1.pop()
        S = num - last_index
        if not hoge2:
            hoge2.append((last_index, S))
        else:
            if last_index >= hoge2[-1][0]:
                hoge2.append((last_index, S))
            else:
                new_S = S
                for i, j in hoge2[::-1]:
                    if last_index >= i:
                        break
                    else:
                        new_S += hoge2.pop()[1] 
                hoge2.append((last_index, new_S))

totals = [x[1] for x in hoge2]
print (sum(totals))
totals.insert(0, len(hoge2))
print (' '.join([str(x) for x in totals]))
