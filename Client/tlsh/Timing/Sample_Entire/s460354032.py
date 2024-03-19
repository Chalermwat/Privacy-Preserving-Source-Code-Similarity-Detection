# PDF参考
# スタックS1
S1 = []
# スタックS2
S2 = []
tmp_total = 0
counter = 0
upper = 0
# 総面積
total_layer = 0

for i,symbol in enumerate(input()):
    if (symbol == '\\'):
        S1.append(i)
    elif (symbol == '/') and S1:
        i_p = S1.pop()
        total_layer = i - i_p
        if S2 :
            while S2 and S2[-1][0] > i_p:
                cal = S2.pop()
                total_layer += cal[1]
        S2.append((i, total_layer))
print(sum([j[1] for j in S2]))
if (len(S2) != 0):
    print(str(len(S2)) + ' ' + ' '.join([str(i[1]) for i in S2]))
else:
    print(str(len(S2)))
        

