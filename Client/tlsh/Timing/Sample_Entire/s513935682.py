pos_latest = []

surface = input()

total = []
total_x = []
y = 0
x = 0
total_tmp = 0
for i in range(len(surface)):
    if surface[i] == "\\":
        pos_latest.append(x)
    if surface[i] == "/":
        if pos_latest:
            pos = pos_latest.pop()
            total.append(x-pos)
            total_x.append([pos, x, x-pos])
    x += 1

if sum(total) > 0:
    sorted_total_x = sorted(total_x)
    t_base = sorted_total_x[0][1]
    tmp = sorted_total_x[0][2]
    res = []
    
    for f, t, v in sorted_total_x[1:]:
        if t <= t_base:
            tmp += v
        else:
            res.append(int(tmp))
            tmp = v
            t_base = t
        if sum(res)>=sum(total):
            break
    res.append(int(tmp))

    print(sum(res))
    print(len(res), *res, sep=" ")
    
else:
    print(sum(total))
    print(0)

