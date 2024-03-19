class Info:
    def __init__(self,arg_start,arg_end,arg_S):
        self.start = arg_start
        self.end = arg_end
        self.S = arg_S

POOL = []
LOC = []
cnt = 0
sum_S = 0

line = input()

for c in line:
    if c == "\\":
        LOC.append(cnt)
    elif c == "/":
        if len(LOC) == 0:
            continue
        tmp_start = LOC.pop()
        tmp_end = cnt
        tmp_S = tmp_end - tmp_start
        sum_S += tmp_S
        while len(POOL) > 0:
            if POOL[-1].start > tmp_start and POOL[-1].end < tmp_end:
                tmp_S += POOL[-1].S
                POOL.pop()
            else:
                break
        POOL.append(Info(tmp_start,tmp_end,tmp_S))
    else:
        pass
    cnt += 1

lst = [len(POOL)]
for i in range(len(POOL)):
    lst.append(POOL[i].S)
print(sum_S)
print(*lst)
