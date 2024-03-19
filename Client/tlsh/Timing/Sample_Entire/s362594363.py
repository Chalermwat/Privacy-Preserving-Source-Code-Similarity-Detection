class Info:
    def __init__(self,arg_start,arg_end,arg_S):
        self.start = arg_start
        self.end = arg_end
        self.S = arg_S


LOC = []
POOL = []

line = input()
loc = 0
sum_S = 0

for ch in line:

    if ch == '\\':

        LOC.append(loc)

    elif ch == '/':

        if len(LOC) == 0:
            continue

        tmp_start = int(LOC.pop())
        tmp_end = loc
        tmp_S = tmp_end-tmp_start;
        sum_S += tmp_S;

        #既に突っ込まれている池の断片が、今回の断片の部分区間になるなら統合する
        while len(POOL) > 0:
            if POOL[-1].start > tmp_start and POOL[-1].end < tmp_end:
                tmp_S += POOL[-1].S
                POOL.pop()
            else:
                break

        POOL.append(Info(tmp_start,tmp_end,tmp_S))

    else:
        pass

    loc += 1

print("%d"%(sum_S))
print("%d"%(len(POOL)),end = "")

while len(POOL) > 0:
    print(" %d"%(POOL[0].S),end = "") #先頭から
    POOL.pop(0)

print()

