def selectionSort(a,b):
    for i in range(len(a)):
        mini = i
        for j in range(i,len(a)):
            if a[j] < a[mini]:
                mini = j
        if i != mini:
            ret = a[i]
            a[i] = a[mini]
            a[mini] = ret
            ret = b[i]
            b[i] =b[mini]
            b[mini] = ret
    
    output = []           
    for i in range(len(a)):
        output.append(str(b[i])+str(a[i]))
    print(" ".join(output))
    return output
    
    
def bubblesort(a,b):
    swap = True
    while swap:
        swap = False
        for j in range(1,len(a))[::-1]:
            if a[j] < a[j-1]:
                ret = a[j]
                a[j] = a[j-1]
                a[j-1] = ret
                ret = b[j]
                b[j] = b[j-1]
                b[j-1] = ret
                swap = True
    output = []           
    for i in range(len(a)):
        output.append(str(b[i])+str(a[i]))
    print(" ".join(output))
    return output


n = int(input())
card = input().split()
number = []
mark = []
number2 = []
mark2 = []
for i in range(n):
    number.append(int(list(card[i])[1]))
    mark.append(list(card[i])[0])
    number2.append(int(list(card[i])[1]))
    mark2.append(list(card[i])[0])

output1 = bubblesort(number,mark)
print("Stable")
output2 = selectionSort(number2, mark2)
print("Stable" if output1 == output2 else "Not stable"  )