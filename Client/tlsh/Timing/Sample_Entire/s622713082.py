n = int(input())
card1 = list(input().split())
card2 = [i for i in card1]
def bubbleSort(c1:list, n:int):
    for i in range(n):
        for j in range(n-1, i, -1):
            if c1[j][1] < c1[j-1][1]:
                c1[j], c1[j-1] = c1[j-1], c1[j]
    return c1

def selectionSort(c2:list, n:int):
    for i in range(n):
        minj = i
        for j in range(i, n):
            if c2[j][1] < c2[minj][1]:
                minj = j
        c2[i], c2[minj] = c2[minj], c2[i]
    return c2

bubblesort = bubbleSort(card1, n)
selectionsort = selectionSort(card2, n)

flag = 0
for i in range(n):
    if bubblesort[i] != selectionsort[i]:
        flag = 1

print(" ".join(bubblesort))
print("Stable")
print(" ".join(selectionsort))
if flag:
    print("Not stable")
else:
    print("Stable")

