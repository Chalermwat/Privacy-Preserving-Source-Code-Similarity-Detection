# bable sort
def bubbleSort(o_nums, n):
    nums=o_nums[:]
    for i in range(len(nums)-1):
        for j in range(len(nums)-1,i,-1):
            if nums[j][1]<nums[j-1][1]:
                nums[j],nums[j-1]=nums[j-1],nums[j]  
    return nums

# selection sort
def selectionSort(o_nums,n):
    nums=o_nums[:]
    for i in range(n):
        minj=i
        for j in range(i,n):
            if nums[j][1]<nums[minj][1]:
                minj=j
        if nums[i][1]!=nums[minj][1]:
            nums[i],nums[minj]=nums[minj],nums[i]
    return nums

n=int(input())
cards=list(input().split())

b=bubbleSort(cards, n)
s=selectionSort(cards,n)
print(*b)
print("Stable")
print(*s)
if bubbleSort(cards, n) == selectionSort(cards, n):
    print("Stable")
else:
    print("Not stable")