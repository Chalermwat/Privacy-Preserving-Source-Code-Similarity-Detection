length = int(input())
targ = [n for n in input().split(' ')]
selecttarg = targ[:]
#bubbleflag = 0
for l in range(length):
    for init in range(l):
        if targ[l - init][1] < targ[l - init - 1][1]:
            disp = targ[l-init]
            targ[l-init] = targ[l-init-1]
            targ[l-init-1] = disp
print(' '.join([str(n) for n in targ]))

print("Stable")

selectflag = 0
for l in range(length):
    value = l
    samevalue = l
    for init in range(l+1,length):
        if selecttarg[value][1] > selecttarg[init][1]:
            value = init
        elif selectflag != 1 and selecttarg[l][1] == selecttarg[init][1]:
            samevalue = init
    if samevalue != l and value != l and value > samevalue:
        selectflag = 1
    disp = selecttarg[l]
    selecttarg[l] = selecttarg[value]
    selecttarg[value] = disp
print(' '.join([str(n) for n in selecttarg]))
if selectflag == 0:
    print("Stable")
else:
    print("Not stable")