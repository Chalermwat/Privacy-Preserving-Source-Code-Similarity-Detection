class Cards:
    def __init__(self,shape,value):
        self.shape = shape
        self.value = value

n = int(input())
s = input().split(" ")
cards1 = []
for i in range(n):
    cards1.append(Cards(s[i][0],int(s[i][1])))
cards2 = list(cards1)
for i in range(n):
    for j in range(n-1,i,-1):
        if cards1[j].value < cards1[j-1].value:
            w = cards1[j]
            cards1[j] = cards1[j-1]
            cards1[j-1] = w
for i in range(n):
    if i == n-1:
        print("{0}{1}".format(cards1[i].shape,cards1[i].value))
    else:
        print("{0}{1}".format(cards1[i].shape,cards1[i].value),end=" ")
print("Stable")

for i in range(n):
    minj = i
    for j in range(i+1,n):
        if cards2[j].value < cards2[minj].value:
            minj = j
    w = cards2[i]
    cards2[i] = cards2[minj]
    cards2[minj] = w
for i in range(n):
    if i == n-1:
        print("{0}{1}".format(cards2[i].shape,cards2[i].value))
    else:
        print("{0}{1}".format(cards2[i].shape,cards2[i].value),end=" ")
for i in range(n):
    if cards1[i].shape != cards2[i].shape:
        print("Not stable")
        break
    if i == n-1:
        print("Stable")