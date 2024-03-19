def buble(lst):

    src_list = list(lst)
    flag=True
    while flag:
        flag = False
        for idx in range(len(lst)-1, 0, -1):
            if int(lst[idx][1]) < int(lst[idx-1][1]):
                tmp=lst[idx]
                lst[idx]=lst[idx-1]
                lst[idx-1]=tmp
                flag=True

    flag_stable = True
    for num in range(0, 9):
        tmp1 = []
        tmp2 = []
        for i in range(0, len(lst)):
            if int(lst[i][1]) == num:
                tmp1.append(lst[i])
            if int(src_list[i][1]) == num:
                tmp2.append(src_list[i])

        if tmp1 != tmp2:
           flag_stable = False
           break
    print " ".join(lst)

    if flag_stable:
        print "Stable"
    else:
        print "Not stable"

def selection(lst):

    src_list = list(lst)
    for i in range(len(lst)):
        m = i
        for j in range(i,len(lst)):
            if int(lst[m][1]) > int(lst[j][1]):
                m=j
        tmp=lst[i]
        lst[i]=lst[m]
        lst[m]=tmp

    flag_stable = True
    for num in range(0, 9):
        tmp1 = []
        tmp2 = []
        for i in range(0, len(lst)):
            if int(lst[i][1]) == num:
                tmp1.append(lst[i])
            if int(src_list[i][1]) == num:
                tmp2.append(src_list[i])

        if tmp1 != tmp2:
           flag_stable = False
           break

    print " ".join(lst)
    if flag_stable:
        print "Stable"
    else:
        print "Not stable"


n=raw_input()
lst1 = raw_input().split()
lst2 = list(lst1)

buble(lst1)
selection(lst2)