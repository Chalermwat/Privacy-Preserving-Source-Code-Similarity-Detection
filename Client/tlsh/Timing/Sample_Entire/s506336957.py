N = int(raw_input())
line = raw_input()
A = line.strip().split(" ")
A2 = line.strip().split(" ")
for i in range(0, N):
    min_j = i
    for j in range(i, N):
        if int(A2[j][1:]) < int(A2[min_j][1:]):
            min_j = j
    A2[i], A2[min_j] = A2[min_j], A2[i]
select = " ".join(A2)
flag = True
while flag:
    flag = False
    for j in range(N-1, 0, -1):
        if int(A[j][1:]) < int(A[j-1][1:]):
            A[j], A[j-1] = A[j-1], A[j]
            flag = True
bubble = " ".join(A)
print bubble
print "Stable"
print select
if bubble == select:
    print "Stable"
else:
    print "Not stable"