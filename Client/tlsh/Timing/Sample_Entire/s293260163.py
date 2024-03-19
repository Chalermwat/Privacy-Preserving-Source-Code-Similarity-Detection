N = int(input())
l = [list(i) for i in input().split()]

a = l.copy()
frag = 1
i = 0
while frag:
    frag = 0
    for j in range(N-1,i,-1):
        if a[j][1] < a[j-1][1]:
            a[j], a[j-1] = a[j-1], a[j]
        frag = 1
    i += 1 
bubble_a = ["".join(a[i]) for i in range(N)]
print(" ".join(bubble_a))
print("Stable")

a = l.copy()
for i in range(N):
    minj = i
    for j in range(i,N):
        if a[j][1] < a[minj][1]:
            minj = j
    if i != minj:
        a[i], a[minj] = a[minj], a[i]
selection_a = ["".join(a[i]) for i in range(N)]
print(" ".join(selection_a))

if bubble_a == selection_a:
    print("Stable")
else:
    print("Not stable")